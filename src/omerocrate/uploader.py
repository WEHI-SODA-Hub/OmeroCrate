from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Literal, cast
from rdflib import Graph, URIRef
from rdflib.query import ResultRow
from rdflib.term import Identifier
from functools import cached_property
from omero import model, gateway, grid
from omero.model import enums
from omero.rtypes import rstring, rbool
import yaml
from omero.model.enums import ChecksumAlgorithmSHA1160
from urllib.parse import urlparse
from shutil import copyfileobj

Namespaces = dict[str, URIRef]
Variables = dict[str, Identifier]

@dataclass
class OmeroUploader:
    """
    Class that handles the conversion between RO-Crate metadata and OMERO objects.
    Users are encouraged to subclass this and override any of the public methods to customize the behavior.
    Refer to the method documentation for more information.
    """
    conn: gateway.BlitzGateway
    "OMERO connection object, typically obtained using [`from_env`][omerocrate.gateway.from_env]"
    crate: Path
    "Path to the directory containing the crate"
    transfer_type: Literal["ln", "ln_s", "ln_rn", "cp", "cp_rm", "upload", "upload_rm"] = "upload"
    """
    Transfer method, which determines how images are sent to OMERO.
    `ln_s` is "in-place" importing, but it requires that this process has acess to both the image and permissions to write to the OMERO server.
    """

    @property
    def namespaces(self) -> Namespaces:
        """
        Namespaces/prefixes used in all SPARQL queries.
        Override this to add or adjust prefixes, e.g. if you are using additional vocabularies.
        """
        return {
            "schema": URIRef("http://schema.org/"),
            "crate": URIRef(f"{self.crate.as_uri()}/"),
            "omerocrate": URIRef("https://w3id.org/WEHI-SODA-Hub/omerocrate/"),
            "ome": URIRef("http://www.openmicroscopy.org/Schemas/OME/2016-06/"),
        }

    @cached_property
    def graph(self) -> Graph:
        """
        RO-Crate metadata as an RDF graph.
        Typically you don't need to override this method.
        """
        return Graph().parse(source=self.crate / "ro-crate-metadata.json", format='json-ld')

    def select_many(self, query: str, namespaces: Namespaces = {}, variables: Variables = {}) -> Iterable[ResultRow]:
        """
        Helper method for running a SPARQL query on the RO-Crate metadata that returns multiple results.
        Typically you don't need to override this method.
        """
        result = self.graph.query(
            query,
            initNs={
                **self.namespaces,
                **namespaces
            },
            initBindings={
                **variables
            }
        )
        if not result.type == "SELECT":
            raise ValueError("Only SELECT queries are supported")
        return cast(Iterable[ResultRow], result)

    def select_one(self, query: str, namespaces: Namespaces = {}, variables: Variables = {}) -> ResultRow:
        """
        Helper method for running a SPARQL query on the RO-Crate metadata that should return exactly one result.
        Typically you don't need to override this method.
        """
        result = list(self.select_many(query, namespaces, variables))
        if len(result) != 1:
            raise ValueError(f"Expected exactly one result, but got {len(result)}")
        return result[0]

    @cached_property
    def root_dataset_id(self) -> Identifier:
        """
        Returns the ID of the root dataset in the crate.
        You shouldn't need to override this method as this function should work for any conformant RO-Crate.
        """
        result = self.select_one("""
            SELECT ?dataset_id
            WHERE {
                ?dataset_id a schema:Dataset .
                crate:ro-crate-metadata.json schema:about ?dataset_id .
            }
        """)
        return result['dataset_id']
    
    def make_dataset(self) -> gateway.DatasetWrapper:
        """
        Creates the OMERO dataset wrapper that corresponds to this crate.
        Override to customize the dataset creation.
        This method should not actually save the dataset!
        """
        dataset = gateway.DatasetWrapper(self.conn, model.DatasetI())

        result = self.select_one("""
            SELECT ?name ?description
            WHERE {
                ?root schema:name ?name .
                ?root schema:name ?description .
            }
        """, variables={"root": self.root_dataset_id})

        dataset.setName(result['name'])
        dataset.setDescription(result['description'])
        return dataset

    def make_images(self, dataset: gateway.DatasetWrapper) -> Iterable[gateway.ImageWrapper]:
        """
        Creates an OMERO image wrapper for the given path.
        Override to customize the image creation.
        This method should not actually save the image!
        """
        for result in self.select_many("""
            SELECT *
            WHERE {
                ?file_path a schema:MediaObject ;
                    omerocrate:upload true ;
                OPTIONAL {
                    ?file_path schema:name ?name .
                }
                OPTIONAL {
                    ?file_path schema:description ?description .
                }
            }
        """):
            image = gateway.ImageWrapper(self.conn, model.ImageI())

            # Attach the image file
            fileset = model.FilesetI()
            image_path = self.path_from_image_result(result)
            entry = model.FilesetEntryI()
            entry.setClientPath(rstring(image_path))
            fileset.addFilesetEntry(entry)
            image.fileset = fileset

            # Add metadata
            if result.name is None:
                image.setName(image_path.name)
            else:
                image.setName(str(result.name))
            if result.description is not None:
                image.setName(str(result.description))
            yield image

    def connect(self):
        """
        Connects to the OMERO server.
        """
        if not self.conn.isConnected():
            result = self.conn.connect()
            if not result:
                raise ValueError(f"Could not connect to OMERO: {self.conn.getLastError()}")

    def synchronise(self, dataset: gateway.DatasetWrapper, images: Iterable[gateway.ImageWrapper]) -> None:
        """
        Synchronises the dataset and images with the OMERO server.
        Can be overridden to upload in alternative ways such as the taskqueue or CLI
        """
        client = self.conn.c
        repo = client.getManagedRepository()
        algorithm = model.ChecksumAlgorithmI()
        algorithm.setValue(rstring(enums.ChecksumAlgorithmSHA1160))
        dataset.save()
        for image in images:
            dataset._linkObject(image, "DatasetImageLinkI")
            upload = model.UploadJobI()
            image.fileset.linkJob(upload)
            importer = repo.importFileset(
                image.fileset,
                grid.ImportSettings(
                    checksumAlgorithm=algorithm,
                    doThumbnails = rbool(True),
                    noStatsInfo = rbool(False)
                ))
            
            path = image.fileset.getFilesetEntry(0)._clientPath.getValue()
            upload_file = importer.getUploader(0)
            offset = 0
            with open(path, "rb") as f:
                while chunk := f.read(4096):
                    upload_file.write(chunk, offset, len(chunk))
                    offset += len(chunk)
            upload_file.close()
            importer.verifyUpload([client.sha1(path)])
            image.save()
            dataset._linkObject(image, "DatasetImageLinkI")


    # def upload_images(self, image_paths: Iterable[Path], dataset: gateway.DatasetWrapper) -> Iterable[gateway.ImageWrapper]:
    #     """
    #     Uploads a set of images to OMERO.
    #     You could override this to use a different method of importing images.

    #     Params:
    #         image_paths: Paths to image files to upload
    #         dataset: OMERO dataset to add the images to

    #     Returns: Wrapped OMERO image object
    #     """

    #     if self.conn.host is None or self.conn.port is None:
    #         raise ValueError("OMERO connection not initialized")

    #     # Running import via CLI is very ugly, but using the Python API doesn't let us capture the output
    #     result = subprocess.run([
    #         "omero",
    #         "import",
    #         "-d", str(dataset.getId()),
    #         "--server", self.conn.host,
    #         "--port", self.conn.port,
    #         "--key", self.conn._getSessionId(),
    #         "--transfer", self.transfer_type,
    #         *image_paths,
    #         "--output",
    #         "yaml"
    #     ], stdout=subprocess.PIPE, check=True)
    #     for image in yaml.safe_load_all(result.stdout):
    #         yield cast(gateway.ImageWrapper, self.conn.getObject("Image", image[0]["Image"][0]))

    def add_image_to_dataset(self, dataset: gateway.DatasetWrapper, image: gateway.ImageWrapper) -> None:
        dataset._linkObject(image, "DatasetImageLinkI")

    def path_from_image_result(self, result: ResultRow) -> Path:
        """
        Converts a SPARQL result row to a Path object.
        """
        return Path(urlparse(result['file_path']).path)

    # def process_images(self, dataset: gateway.DatasetWrapper):
    #     """
    #     Runs the image selection query and processes each result.
    #     Typically you don't need to override this method: either `process_image` or `image_query` should be enough.
    #     """
    #     results = list(self.select_many(self.image_query))
    #     image_paths = [self.path_from_image_result(result) for result in results]
    #     wrappers = list(self.upload_images(image_paths, dataset=dataset))
    #     for image, result in zip(wrappers, results):
    #         self.process_image(image, result, dataset)

    def execute(self) -> gateway.DatasetWrapper:
        """
        Runs the entire processing workflow.
        Typically you don't need to override this method.
        """
        self.connect()
        dataset = self.make_dataset()
        images = self.make_images(dataset)
        self.synchronise(dataset, images)
        return dataset

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Literal, cast
from rdflib import Graph, URIRef
from rdflib.query import ResultRow
from rdflib.term import Identifier
from functools import cached_property
from omero import model, gateway
from omero.cli import CLI
import yaml
from urllib.parse import urlparse
import subprocess

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
            "crate": URIRef(f"{self.crate.as_uri()}/")
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
        Creates the OMERO dataset that correspons to this crate.
        Override to customize the dataset creation.
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
        dataset.save()
        # See https://github.com/ome/omero-py/issues/451
        dataset._oid = dataset._obj.id.val
        return dataset

    def connect(self):
        """
        Connects to the OMERO server.
        """
        if not self.conn.isConnected():
            result = self.conn.connect()
            if not result:
                raise ValueError(f"Could not connect to OMERO: {self.conn.getLastError()}")

    def upload_images(self, image_paths: Iterable[Path], dataset: gateway.DatasetWrapper) -> Iterable[gateway.ImageWrapper]:
        """
        Uploads a set of images to OMERO.
        You could override this to use a different method of importing images.

        Params:
            image_path: Path to the image file

        Returns: Wrapped OMERO image object
        """

        if self.conn.host is None or self.conn.port is None:
            raise ValueError("OMERO connection not initialized")

        # Running import via CLI is very ugly, but using the Python API doesn't let us capture the output
        result = subprocess.run([
            "omero",
            "import",
            "-d", str(dataset.getId()),
            "--server", self.conn.host,
            "--port", self.conn.port,
            "--key", self.conn._getSessionId(),
            "--transfer", self.transfer_type,
            *image_paths,
            "--output",
            "yaml"
        ], stdout=subprocess.PIPE, check=True)
        for image in yaml.safe_load_all(result.stdout):
            yield cast(gateway.ImageWrapper, self.conn.getObject("Image", image[0]["Image"][0]))

    def add_image_to_dataset(self, dataset: gateway.DatasetWrapper, image: gateway.ImageWrapper) -> None:
        dataset._linkObject(image, "DatasetImageLinkI")

    image_query = """
        SELECT ?file_path
        WHERE {
            ?file_path a schema:MediaObject ;
            FILTER (STRAFTER(STR(?file_path), ".") IN ("jpg", "jpeg", "png", "tiff", "tif", "bmp", "gif"))
        }
    """
    """
    Query for selecting images and their metadata from the crate. Override this to customize the selection.
    For example, to select only images whose MIME type starts with "image/", you can use:
    ```sparql
        WHERE {
            ?file_path a schema:MediaObject ;
            schema:encodingFormat ?img_format .
            FILTER STRSTARTS(?img_format, "image/")
        }
        ```
    """

    def process_image(self, image: gateway.ImageWrapper, result: ResultRow, dataset: gateway.DatasetWrapper) -> None:
        """
        Handles the processing of a single image extracted from the crate.
        By default, this does nothing.
        Override this to e.g. add additional metadata to the image using the `image` wrapper.
        """

    def path_from_image_result(self, result: ResultRow) -> Path:
        """
        Converts a SPARQL result row to a Path object.
        """
        return Path(urlparse(result['file_path']).path)

    def process_images(self, dataset: gateway.DatasetWrapper):
        """
        Runs the image selection query and processes each result.
        Typically you don't need to override this method: either `process_image` or `image_query` should be enough.
        """
        results = list(self.select_many(self.image_query))
        image_paths = [self.path_from_image_result(result) for result in results]
        wrappers = list(self.upload_images(image_paths, dataset=dataset))
        for image, result in zip(wrappers, results):
            self.process_image(image, result, dataset)

    def execute(self) -> gateway.DatasetWrapper:
        """
        Runs the entire processing workflow.
        Typically you don't need to override this method.
        """
        self.connect()
        dataset = self.make_dataset()
        self.process_images(dataset)
        return dataset

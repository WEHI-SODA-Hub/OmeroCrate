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
    conn: gateway.BlitzGateway
    "OMERO connection object, typically obtained using `ezomero.connect()`"
    crate: Path
    "Path to the directory containing the crate"
    cli: CLI = field(default_factory=CLI)
    "OMERO CLI runner"

    def __post_init__(self):
        # CLI has no subcommands without plugins
        self.cli.loadplugins()

    @property
    def namespaces(self) -> Namespaces:
        return {
            "schema": URIRef("http://schema.org/"),
            "crate": URIRef(f"{self.crate.as_uri()}/")
        }

    @cached_property
    def graph(self) -> Graph:
        return Graph().parse(source=self.crate / "ro-crate-metadata.json", format='json-ld')

    def select_many(self, query: str, namespaces: Namespaces = {}, variables: Variables = {}) -> Iterable[ResultRow]:
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
        result = list(self.select_many(query, namespaces, variables))
        if len(result) != 1:
            raise ValueError(f"Expected exactly one result, but got {len(result)}")
        return result[0]

    @cached_property
    def root_dataset_id(self) -> Identifier:
        result = self.select_one("""
            SELECT ?dataset_id
            WHERE {
                ?dataset_id a schema:Dataset .
                crate:ro-crate-metadata.json schema:about ?dataset_id .
            }
        """)
        return result['dataset_id']
    
    def make_dataset(self) -> gateway.DatasetWrapper:
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
        return dataset

    def connect(self):
        if not self.conn.isConnected():
            result = self.conn.connect()
            if not result:
                raise ValueError(f"Could not connect to OMERO: {self.conn.getLastError()}")

    def upload_image(self, image_path: str, transfer_type: Literal["ln", "ln_s", "ln_rn", "cp", "cp_rm", "upload", "upload_rm"]="upload") -> gateway.ImageWrapper:
        """
        Uploads an image to OMERO.

        Params:
            image_path: Path to the image file
            transfer_type: Transfer method, which determines how the image is sent to OMERO.
                `ln_s` is "in-place" importing, but it requires that this process has acess to both the image and permissions to write to the OMERO server.
        
        Returns: Wrapped OMERO image object
        """

        if self.conn.host is None or self.conn.port is None:
            raise ValueError("OMERO connection not initialized")
        result = subprocess.run([
            "omero",
            "import",
            "--server", self.conn.host,
            "--port", self.conn.port,
            "--key", self.conn._getSessionId(),
            "--transfer", transfer_type,
            # "--transfer=ln_s",
            image_path,
            "--output",
            "yaml"
        ], stdout=subprocess.PIPE, check=True)
        parsed: list[dict[str, Any]] = yaml.safe_load(result.stdout)
        image_id = parsed[0]["Image"][0]
        return cast(gateway.ImageWrapper, self.conn.getObject("Image", image_id))

    def add_image_to_dataset(self, dataset: gateway.DatasetWrapper, image: gateway.ImageWrapper):
        dataset._linkObject(image, "DatasetImageLinkI")

    def add_images(self, dataset: gateway.DatasetWrapper):
        """
        Override this to customize how images are selected from the crate.
        For example, to select using MIME type:
        ```
        WHERE {
            ?file_path a schema:MediaObject ;
            schema:encodingFormat ?img_format .
            FILTER STRSTARTS(?img_format, "image/")
        }
        ```
        """
        for result in self.select_many("""
            SELECT ?file_path
            WHERE {
                ?file_path a schema:MediaObject ;
                FILTER (STRAFTER(STR(?file_path), ".") IN ("jpg", "jpeg", "png", "tiff", "tif", "bmp", "gif"))
            }
            """):
            # Convert the URI to a path
            uri = urlparse(result['file_path'])
            image = self.upload_image(uri.path)
            self.add_image_to_dataset(dataset, image)


    def execute(self):
        self.connect()
        dataset = self.make_dataset()
        self.add_images(dataset)

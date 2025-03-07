from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, cast
from omero.gateway import BlitzGateway
from rdflib import Graph, URIRef
from rdflib.query import ResultRow
from rdflib.term import Identifier
from functools import cached_property
from omero import model, gateway
from omero.cli import CLI
from contextlib import redirect_stdout
from io import StringIO
import yaml

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

    def link_image(self, image_path: str) -> int:
        output = StringIO()
        with redirect_stdout(output):
            self.cli.invoke([
                "import",
                "--",
                "--transfer=ln_s",
                image_path,
                "--output",
                "yaml"
            ])
        parsed: list[dict[str, Any]] = yaml.safe_load(output.getvalue())
        return parsed[0]["Image"][0]

    def add_images(self, dataset: gateway.DatasetWrapper):
        for result in self.select_many("""
            SELECT ?file_path
            WHERE {
                ?file_path a schema:MediaObject ;
                schema:encodingFormat ?img_format .
                FILTER STRSTARTS(?img_format, "image/")
            """):
            self.link_image(str(result['file_path']))

    def execute(self):
        self.connect()
        dataset = self.make_dataset()

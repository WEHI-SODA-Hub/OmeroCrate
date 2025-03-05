from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, cast
from omero.gateway import BlitzGateway
from rdflib import Graph, URIRef
from rdflib.query import ResultRow
from rdflib.term import Identifier
from functools import cached_property
from omero import model, gateway

Namespaces = dict[str, URIRef]
Variables = dict[str, Identifier]

@dataclass
class OmeroUploader:
    conn: gateway.BlitzGateway
    "OMERO connection object, typically obtained using `ezomero.connect()`"
    crate: Path
    "Path to the directory containing the crate"

    @property
    def namespaces(self) -> Namespaces:
        return {
            "schema": URIRef("http://schema.org/"),
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
                ?dataset_id a omero:Dataset .
                "ro-crate-metadata.json" schema:about ?dataset_id .
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
        """)

        dataset.setName(result['name'])
        dataset.setDescription(result['description'])
        dataset.save()
        return dataset

    def upload(self):

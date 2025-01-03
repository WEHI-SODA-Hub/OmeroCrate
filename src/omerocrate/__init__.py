from pathlib import Path
from typing import Iterable
import ezomero
from omero.gateway import BlitzGateway
from rdflib.query import ResultRow
from rdflib import Graph
from rdflib.term import Identifier
from omero.model import ProjectI

def query_to_dicts(graph: Graph, query: str, prefixes: dict) -> Iterable[dict[str, Identifier]]:
    for row in graph.query(query, initNs=prefixes):
        if not isinstance(row, ResultRow):
            raise ValueError("Invalid result. Are you sure the query was a select query?")
        else:
            yield row.asdict()


def upload_crate(crate: Path, connection: BlitzGateway):
    """
    Params:
        crate: Path to the directory containing the crate
        connection: Omero connection object, typically obtained using `ezomero.connect()`
    """
    graph = Graph().parse(source=crate / "ro-crate-metadata.json", format='json-ld')
    prefixes = {
        "crate": f"file://{crate}/",
        "schema": "http://schema.org/",
        # "omero": "http://schema.org/",
    }

    result = graph.query("""
        CONSTRUCT {
            crate: a <http://www.openmicroscopy.org/Schemas/OME/2016-06/Dataset> ;
            schema:name ?dataset_name ;
            schema:hasPart ?file_id .
        }
        WHERE {
            crate: schema:name ?dataset_name .
            ?file_id a schema:MediaObject .
        }
    """, initNs=prefixes)
    print(result.serialize(format="ttl").decode())

    for row in graph.query("""
        SELECT ?dataset_name
        WHERE {
            crate: schema:name ?dataset_name
        }
    """, initNs=prefixes):
        dataset_name  = str(row.dataset_name)

    print(dataset_name)

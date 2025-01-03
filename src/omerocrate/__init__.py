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
        "omero": "http://www.openmicroscopy.org/Schemas/OME/2016-06/"
    }

    result = graph.query("""
        CONSTRUCT {
            ?file_id a omero:Image ;
                omero:pixels ?pixels_id .

            ?pixels_id a omero:Pixels ;
                omero:tiff_data ?tiff_data_id .
            
            ?tiff_data_id a omero:TiffData ;
                omero:uuid ?uuid_id .
                         
            ?uuid_id a omero:UUID ;
                omero:value ?uuid ;
                omero:file_name ?file_name .
        }
        WHERE {
            # Match all files that are TIFFs
            ?file_id a schema:MediaObject ;
                schema:encodingFormat ?img_format .

            FILTER STRSTARTS(?img_format, "image/")

            BIND(BNODE() AS ?pixels_id)
            BIND(BNODE() AS ?uuid_id)
            BIND(BNODE() AS ?tiff_data_id)
            BIND(UUID() AS ?uuid)
            BIND(STR(?file_id) AS ?file_name)
        }
    """, initNs=prefixes)
    print(result.serialize(format="json-ld", context=prefixes, auto_compact=True).decode())

    for row in graph.query("""
        SELECT ?dataset_name
        WHERE {
            crate: schema:name ?dataset_name
        }
    """, initNs=prefixes):
        dataset_name  = str(row.dataset_name)

    print(dataset_name)

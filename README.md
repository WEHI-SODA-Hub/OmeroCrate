# OmeROCrate

Integration layer between the OMERO image platform and RO-Crate metadata standard.

## Design

The core idea used here is that SPARQL queries can idiomatically map from RO-Crate JSON-LD to OMERO data structures.
OMERO's schema is defined in terms of XML.

One way to do this might be to have the user write SPARQL that maps to a structure similar to OMERO XML directly, and then use the [RDF XML](https://www.w3.org/TR/rdf-syntax-grammar) format to write XML, which then gets processed (to flatten out `<rdf:Description>` elements for example), which then gets ingested into OMERO. However, this probably won't work as we can't control how the choice between elements and attributes is made when serializing to RDF/XML.
```python
from rdflib import Graph
from linkml_runtime.dumpers import RDFLibDumper

def to_omero(json_ld: str, user_defined_query: str) -> str:
    graph = Graph()
    graph.parse(json_ld, format="json-ld")
    result = graph.query(user_defined_query)
    return result.serialize(format="xml") # Doesn't actually return the right XML structure
```

Another intuitive idea would be to avoid SPARQL, and load the RO-Crate into Python using some mechanism such as a LinkML importer, and then have the user write a function to convert this to XML. This is not elegant because the way the user might want to navigate the RO-Crate graph is not easily facilitated in Python.
```python
from linkml_runtime.loaders import JSONLoader
from linkml_runtime.dumpers import XMLDumper # Doesn't exist yet: https://github.com/linkml/linkml/issues/2498
from typing import Callable
from .omero_linkml import all_classes

def to_omero(json_ld: str, user_defined_func: Callable) -> str:
    rocrate = JSONLoader.load(json_ld, all_classes) # Doesn't work yet: https://github.com/linkml/linkml/issues/2477
    omero_metadata = user_defined_func(rocrate)
    return XMLDumper().dump(omero_metadata)
```

Another approach will be to generate a LinkML schema for OMERO using [this PR](https://github.com/linkml/schema-automator/pull/153), then generate Pydantic classes from that schema. The user will then write SPARQL that maps from RO-Crate to these Pydantic classes, which then get automatically mapped to XML and ingested into OMERO. Alternatively we could bypass XML and write a simple mapping layer for all the Pydantic classes.
```python
from rdflib import Graph
from linkml_runtime.loaders import RDFLibLoader
from linkml_runtime.dumpers import XMLDumper # Doesn't exist yet: https://github.com/linkml/linkml/issues/2498
from .omero_linkml import all_classes

def to_omero(json_ld: str, user_query: str) -> str:
    g = Graph()
    g.parse(json_ld, format="json-ld")
    result = g.query(user_query).serialize()
    omero_metadata = RDFLibLoader().load(result, all_classes) # Doesn't work yet: https://github.com/linkml/linkml/issues/2477
    return XMLDumper().dump(omero_metadata)
```

Since the LinkML ecosystem has some difficulties with loading into an unknown series of classes, we could first generate Pydantic dataclasses using [`xsdata`](https://xsdata.readthedocs.io/en/latest/), and then run the SPARQL conversion as above, but time loading into the xsdata classes 
```python
from rdflib import Graph
from linkml_runtime.loaders import RDFLibLoader
from xsdata.formats.dataclass.serializers import XmlSerializer
from .omero_xsdata import OME

def to_omero(json_ld: str, user_query: str):
    g = Graph()
    g.parse(json_ld, format="json-ld")
    result = g.query(user_query)
    omero_metadata = RDFLibLoader().load(result, OME)
    return XmlSerializer().render(omero_metadata)
```
Unfortunately this doesn't seem to work, as the `RDFLibLoader` requires a LinkML schema.
`xsdata` provides a JSON loader, but converting from the RDF graph to standard JSON that can be loaded by it is not trivial.

OMERO has a [JSON API](https://omero.readthedocs.io/en/stable/developers/json-api.html), which would be easy to map into, but the API doesn't support creating all entity types yet.

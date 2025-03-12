The core idea used here is that SPARQL queries can idiomatically map from RO-Crate JSON-LD to OMERO data structures.
OMERO's schema is defined in terms of XML.

One way to do this might be to have the user write SPARQL that maps to a structure similar to OMERO XML directly, and then use the [RDF XML](https://www.w3.org/TR/rdf-syntax-grammar) format to write XML, which then gets processed (to flatten out `<rdf:Description>` elements for example), which then gets ingested into OMERO. However, this probably won't work as we can't control how the choice between elements and attributes is made when serializing to RDF/XML.

Another approach will be to generate a LinkML schema for OMERO using [this PR](https://github.com/linkml/schema-automator/pull/153), then generate Pydantic classes from that schema. The user will then write SPARQL that maps from RO-Crate to these Pydantic classes, which then get automatically mapped to XML and ingested into OMERO. Alternatively we could bypass XML and write a simple mapping layer for all the Pydantic classes.

OMERO has a [JSON API](https://omero.readthedocs.io/en/stable/developers/json-api.html), which would be easy to map into, but the API doesn't support creating all entity types yet.

from __future__ import annotations
from dataclasses import dataclass
from typing import IO, Any
from rdflib import Graph, URIRef, Literal
from rdflib.serializer import Serializer
from xml.etree import ElementTree 

"""
rx:root [
    el:div [
        el:p [
            rx:content: "Hello World!" ;
            attr:style "color: red" ;
        ] 
        el:img [
            attr:src "http://example.com/image.jpg" ;
        ] 
    ]
] .
"""

prefixes = {
    "rx": "rdf_to_xml",
    "attr": "rx:attributes",
    "el": "rx:elements",
}

def element_to_xml(pred: URIRef, object: URIRef, graph: Graph) -> ElementTree.Element:
    element = ElementTree.Element(pred.split(":")[1])
    for sub_pred, sub_obj in graph.predicate_objects(object):
        if not isinstance(sub_obj, URIRef):
            raise ValueError("Expected URIRef")
        if  sub_pred.startswith("rx:content"):
            element.text = str(sub_obj)
        elif sub_pred.startswith("attr:"):
            element.set(pred.split(":")[1], str(sub_obj))
        elif sub_pred.startswith("tag:") and isinstance(sub_obj, URIRef):
            element.append(element_to_xml(sub_pred, sub_obj, graph))
    return element


def graph_to_xml(graph: Graph) -> ElementTree.ElementTree:

    URIRef("rdf_to_xml:root")
    tree = ElementTree.ElementTree(element=element_to_xml(URIRef("rdf_to_xml:root")))
    return tree

@dataclass
class XmlSerializer(Serializer):
    store: Graph

    # root: str
    "The tag type which will become the root element of the XML document."

    def serialize(
        self,
        stream: IO[bytes],
        base: str | None = None,
        encoding: str | None = None,
        **args: Any,
    ) -> None:
        for pred, obj in self.store.predicate_objects(URIRef("rdf_to_xml:root")):

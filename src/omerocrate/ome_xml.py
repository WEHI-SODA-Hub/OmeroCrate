from importlib.abc import Traversable
from pathlib import Path

from jinja2 import Template
from rdflib import Graph
from importlib.resources import files


def build_xml(graph: Graph, template: Traversable = files('omerocrate') / "ome_xml.jinja2") -> str:
    return Template(template.read_text()).render(graph=graph, list=list)

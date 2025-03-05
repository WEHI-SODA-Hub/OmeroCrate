from jinja2 import Template
import pytest
from pathlib import Path

from rdflib import Graph

@pytest.fixture
def foaf_graph() -> Graph:
    path = Path() / "test/foaf.json"
    graph = Graph()
    graph.parse(str(path), format="json-ld")
    return graph

@pytest.fixture
def template(foaf_graph: Graph) -> Template:
    path = Path() / "test/sparql.jinja2"
    return Template(path.read_text())#, extensions=["omerocrate.SparqlExtension"])


def test_sparql_template(template: Template, foaf_graph: Graph):
    ret = template.render(graph=foaf_graph)
    assert ret
    # env = Environment(
    #     loader=PackageLoader(__name__),
    # )

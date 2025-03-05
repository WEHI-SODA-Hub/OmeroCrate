from pathlib import Path
import pytest
from rdflib import Graph
from omerocrate.ome_xml import OmeXmlBuilder
from xml.etree import ElementTree
from rdfcrate import uris, bioschemas
from rdflib import Graph, URIRef, Literal, RDF

image_id = URIRef("image.tiff")

def make_graph() -> Graph:
    """
    Creates a simple RO-Crate with an image derived from a tissue sample.
    """
    graph = Graph()
    graph.add((image_id, RDF.type, uris.File))
    graph.add((image_id, RDF.type, uris.ImageObject))


    return graph

def add_date(graph: Graph):
    graph.add((image_id, uris.dateCreated, Literal("2020-01-01")))

def add_tissue(graph: Graph):
    tissue = URIRef("#tissue")
    graph.add((tissue, RDF.type, bioschemas.BioSample))
    graph.add((tissue, uris.description, Literal("Whole blood sample")))

    creation = URIRef("#create_image")
    graph.add((creation, RDF.type, bioschemas.LabProcess))
    graph.add((creation, bioschemas.input, tissue))
    graph.add((creation, uris.result, image_id))

def xml_equal(a: str, b: str) -> bool:
    return ElementTree.canonicalize(a.strip(), strip_text=True) == ElementTree.canonicalize(b.strip(), strip_text=True)

def test_no_date():
    graph = make_graph()
    parsed = OmeXmlBuilder(graph=graph).serialize()
    assert xml_equal(parsed, """
        <?xml version="1.0" encoding="UTF-8"?>
        <OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2016-06" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2016-06/ome.xsd">
            <Image Name="image.tiff">
                <Pixels>
                    <TiffData>
                        <UUID FileName="image.tiff"/>
                    </TiffData>
                </Pixels>
            </Image>
        </OME>
    """)

def test_date():
    graph = make_graph()
    add_date(graph)
    # If the date is present, it should be added to the XML
    parsed = OmeXmlBuilder(graph=graph).serialize()
    assert xml_equal(parsed, """
        <OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2016-06" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2016-06/ome.xsd">
            <Image Name="image.tiff">
                <AcquisitionDate>2020-01-01</AcquisitionDate>
                <Pixels>
                    <TiffData>
                        <UUID FileName="image.tiff"/>
                    </TiffData>
                </Pixels>
            </Image>
        </OME>
    """)

def test_tissue():
    graph = make_graph()
    add_tissue(graph)
    # If the date is present, it should be added to the XML
    parsed = OmeXmlBuilder(graph=graph).serialize()
    assert xml_equal(parsed, """
        <OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2016-06" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2016-06/ome.xsd">
            <Image Name="image.tiff">
                <AcquisitionDate>2020-01-01</AcquisitionDate>
                <Pixels>
                    <TiffData>
                        <UUID FileName="image.tiff"/>
                    </TiffData>
                </Pixels>
                <TagAnnotation ID="#tissue"/>
            </Image>
            <StructuredAnnotations>
                <TagAnnotation ID="#tissue">
                    <Description>Sample tissue type</Description>
                    <Value>Whole blood sample</Value>
                </TagAnnotation>
            </StructuredAnnotations>
        </OME>
    """)

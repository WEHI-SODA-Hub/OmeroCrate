from rdflib import Graph
from omerocrate.xml_export import XmlSerializer
from io import BytesIO
from xml.etree import ElementTree

def xml_equal(a: str, b: str) -> bool:
    return ElementTree.fromstring(a) == ElementTree.fromstring(b)

def test_xml_serializer():
    input = Graph()
    input.parse(data="""
    @prefix rx <rdf_to_xml://> .
    @prefix attr rx:attributes .
    @prefix el rx:elements .

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
    """, format="turtle")
    serializer = XmlSerializer(input)

    output = BytesIO()
    serializer.serialize(output)
    expected = """
    <div>
        <p style="color: red">Hello World!</p>
        <img src="http://example.com/image.jpg" />
    </div>
    """

    assert xml_equal(output.getvalue().decode(), expected)

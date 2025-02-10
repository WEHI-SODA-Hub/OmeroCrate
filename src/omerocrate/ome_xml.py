from dataclasses import dataclass, field
from typing import ClassVar, Iterable, Type, cast

from pydantic import BaseModel
from rdflib import Graph
from rdflib.query import ResultRow
from rdflib.term import Identifier
from omerocrate.ome_schema import Ome, Image, StructuredAnnotations, Pixels, TiffData, AnnotationRef, TagAnnotation, PixelType, PixelsDimensionOrder
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.bindings import XmlSerializer, XmlContext
from xsdata.formats.dataclass.serializers.config import SerializerConfig



@dataclass
class OmeXmlBuilder:
    graph: Graph
    model: Ome = field(default_factory=lambda : Ome())
    namespaces: ClassVar[dict[str, str]] = {
        "schema": "http://schema.org/",
        "bioschemas_drafts": "https://discovery.biothings.io/view/bioschemastypesdrafts/",
        "bioschemas": "https://discovery.biothings.io/view/bioschemastypes/"
    }
    counter: int = 0

    def query(self, query: str, vars: dict[str, Identifier] | None = None) -> Iterable[ResultRow]:
        result = self.graph.query(query, initNs=self.namespaces, initBindings=vars)
        if not result.type == "SELECT":
            raise ValueError("Only SELECT queries are supported")
        return cast(Iterable[ResultRow], result)

    def make_id(self, typ: Type[BaseModel]) -> str:
        self.counter += 1
        return f"{typ.__name__.title()}:{self.counter}"

    def build(self):
        anns = StructuredAnnotations()
        self.model.structured_annotations = anns
        for row in self.query('''
            SELECT *
            WHERE {
                ?image_path a schema:ImageObject .
                OPTIONAL { ?image_path schema:dateCreated ?image_date . }
            }
            '''
        ):
            img = Image(
                    id=self.make_id(Image),
                    name=row.image_path,
                    pixels=Pixels(
                        id=self.make_id(Pixels),
                        tiff_data=[TiffData(
                            uuid=TiffData.Uuid(
                                file_name=row.image_path
                            )
                        )],
                        dimension_order=PixelsDimensionOrder.XYZCT,
                        type_value=PixelType.INT32,
                        size_c=1,
                        size_t=1,
                        size_x=1,
                        size_y=1,
                        size_z=1
                    ),
                    acquisition_date=XmlDateTime.from_string(row.image_date) if row.image_date else None
                )

            for row in self.query('''
                SELECT *
                WHERE {
                    ?tissue_id a bioschemas_drafts:BioSample ;
                        schema:description ?tissue_description .

                    ?process_id a bioschemas_drafts:LabProcess ;
                        bioschemas:input ?tissue_id ;
                        schema:result ?image_path .
                }
            ''', vars={"image_path": row.image_path}):
                anns.tag_annotation.append(
                    TagAnnotation(
                        id=str(row.tissue_id),
                        value=row.tissue_description
                    )
                )
                img.annotation_ref.append(AnnotationRef(id=str(row.tissue_id)))
            self.model.image.append(img)

    def serialize(self) -> str:
        context = XmlContext()
        xml_serializer = XmlSerializer(context=context, config=SerializerConfig(
            schema_location="http://www.openmicroscopy.org/Schemas/OME/2016-06/ome.xsd"
        ))

        self.build()
        return xml_serializer.render(self.model, ns_map={
            # Default namespace
            None: "http://www.openmicroscopy.org/Schemas/OME/2016-06"
        })

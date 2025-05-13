from rdflib import URIRef

#: If set to true, upload to OMERO
upload = URIRef("https://w3id.org/WEHI-SODA-Hub/omerocrate/upload")

#: Must link to a `MediaObject` that this is the segmentation for
segmentation_for = URIRef("https://w3id.org/WEHI-SODA-Hub/omerocrate/segmentationFor")

#: The QName of this element in the XML Schema is `{http://www.openmicroscopy.org/Schemas/OME/2016-06}ExperimenterRef`
#: We approximate this QName in an RDF idiomatic way by just joining the URIs
#: This links an object to an existing OMERO user group
experimenter_group = URIRef("http://www.openmicroscopy.org/Schemas/OME/2016-06/ExperimenterGroupRef")

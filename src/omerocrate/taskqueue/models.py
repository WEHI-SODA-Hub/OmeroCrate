from __future__ import annotations
from typing import List, Any, Annotated
from pydantic import BaseModel, Field

KeyValue = tuple[str, Any]

class Image(BaseModel):
    name: Annotated[str, Field(description="Image name")]
    description: Annotated[str, Field(description="Image description")]
    key_values: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of key-value pairs associated with this image",
        alias="keyValues"
    )]
    file_path: Annotated[str, Field(
        description="Path to the image file on disk",
        alias="filePath"
    )]
    tag: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of tags associated with this image"
    )]


class Dataset(BaseModel):
    name: Annotated[str, Field(description="Dataset name")]
    description: Annotated[str, Field(description="Dataset description")]
    key_values: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of key-value pairs to be added to this dataset",
        alias="keyValues"
    )]
    tag: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of tags associated with this dataset"
    )]
    image: Annotated[List[Image], Field(
        default_factory=list,
        description="List of images in this dataset"
    )]


class Project(BaseModel):
    name: Annotated[str, Field(description="Project name")]
    description: Annotated[str, Field(description="Project description")]
    key_values: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of key-value pairs to be added to this project",
        alias="keyValues"
    )]
    tag: Annotated[List[KeyValue], Field(
        default_factory=list,
        description="List of tags associated with this project"
    )]
    dataset: Annotated[List[Dataset], Field(
        default_factory=list,
        description="List of datasets in this project"
    )]


class Upload(BaseModel):
    group: Annotated[str, Field(
        description="The OMERO group name"
    )]
    import_user: Annotated[str, Field(
        description="Username of the user importing the data",
        alias="importUser"
    )]
    project: Annotated[List[Project], Field(
        description="List of projects to be uploaded"
    )]

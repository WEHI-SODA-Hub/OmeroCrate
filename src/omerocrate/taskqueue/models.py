from __future__ import annotations
from datetime import datetime
from typing import List, Any, Annotated, Literal, Optional, Union
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict, AliasChoices

KeyValue = tuple[str, Any]

class TaskQueueBase(BaseModel):
    """
    Base class for all models in this module
    """
    model_config = ConfigDict(
        serialize_by_alias=True,
    )

class ImageRequest(TaskQueueBase):
    """
    Fields needed to upload an image to OMERO
    """
    name: Annotated[str, Field(description="Image name")]
    description: Annotated[str, Field(description="Image description")]
    file_path: Annotated[str, Field(
        description="Path to the image file on disk",
        validation_alias=AliasChoices("filePath", "file_path"),
        alias="filePath"
    )]
    key_values: list[KeyValue] = Field(
        default_factory=list,
        description="List of key-value pairs associated with this image",
        alias="keyValues"
    )
    tag: list[KeyValue] = Field(
        default_factory=list,
        description="List of tags associated with this image"
    )


class DatasetFields(TaskQueueBase):
    """
    Common fields for Dataset and DatasetRequest
    """
    name: Annotated[str, Field(description="Dataset name")]
    description: Annotated[str, Field(description="Dataset description")]
    key_values: list[KeyValue] = Field(
        default_factory=list,
        description="List of key-value pairs to be added to this dataset",
        alias="keyValues"
    )
    tag: list[KeyValue] = Field(
        default_factory=list,
        description="List of tags associated with this dataset"
    )


class DatasetRequest(DatasetFields):
    image: list[ImageRequest] = Field(
        default_factory=list,
        description="List of images in this dataset"
    )


class ProjectFields(TaskQueueBase):
    name: Annotated[str, Field(description="Project name")]
    description: Annotated[str, Field(description="Project description")]
    key_values: list[KeyValue] = Field(
        default_factory=list,
        description="List of key-value pairs to be added to this project",
        alias="keyValues"
    )
    tag: list[KeyValue] = Field(
        default_factory=list,
        description="List of tags associated with this project"
    )

class ProjectRequest(ProjectFields):
    """
    Fields needed to upload a project to OMERO
    """
    dataset: Annotated[List[DatasetRequest], Field(
        default_factory=list,
        description="List of datasets in this project"
    )]

class UploadFields(TaskQueueBase):
    """
    Common fields for UploadRequest and `UploadResult`
    """
    group: Annotated[str, Field(
        description="The OMERO group name"
    )]
    import_user: Annotated[str, Field(
        description="Username of the user importing the data",
        alias="importUser",
        validation_alias=AliasChoices("importUser", "import_user")
    )]

class UploadRequest(UploadFields):
    """
    Data structure used to upload images to OMERO
    """
    project: list[ProjectRequest] = Field(
        description="List of projects to be uploaded",
        default_factory=list,
    )

State = Annotated[Literal[
    "PENDING", "FAILURE", "STARTED", "SUCCESS"
], Field(
    description="The status of the upload task"
)]

class UploadReponse(TaskQueueBase):
    """
    Response schema from the /send-task/gs_import_run_omero_import endpoint
    """
    task_id: Annotated[str, Field(
        description="The ID of the task in the task queue",
        alias="task-id"
    )]
    state: State

TimeStamp = Annotated[Optional[datetime], BeforeValidator(
    lambda v: v if v is None else datetime.fromtimestamp(v),
), Field(description="Timestamp of an event")]

class UploadStatus(TaskQueueBase):
    uuid: str
    name: str
    state: State
    received: TimeStamp
    sent: None
    started: TimeStamp
    rejected: TimeStamp
    succeeded: TimeStamp
    failed: TimeStamp
    retried: None
    revoked: None
    args: str
    kwargs: str
    eta: None
    expires: None
    retries: int
    worker: str
    result: Optional[str]
    exception: Optional[str]
    timestamp: TimeStamp
    runtime: Optional[float]
    traceback: Optional[str]
    exchange: None
    routing_key: None
    clock: int
    client: None
    root: str
    root_id: str
    parent: None
    parent_id: None
    children: list

class ImportSummary(TaskQueueBase):
    number_of_files: str
    number_of_omero_images: str
    number_of_errors: str
    importer_time: str
    error: None
    exception: None
    file_exists: None
    clientpath: None
    plateId: None
    imageId: str
    time: str

ImportStatus = Annotated[Literal["SUCCEEDED", "FAILED"], Field(
    alias="importStatus",
    description="The status of part the import task"
)]

class SuccessImageResponse(ImageRequest):
    """
    Data returned by the task queue after the image has been imported
    """
    import_status: ImportStatus
    import_summary: Annotated[ImportSummary, Field(
        alias="importSummary"
    )]
    object_id: Annotated[list[int], Field(
        alias="objectId"
    )]
    fileset_id: Annotated[str, Field(
        alias="filesetId"
    )]

class FailureImageResponse(ImageRequest):
    """
    Data returned by the task queue after the image has been imported
    """
    import_status: Annotated[Literal["FAILED"], Field(
        alias="importStatus"
    )]
    import_summary: Annotated[str, Field(
        alias="importSummary"
    )]
    object_id: Annotated[None, Field(
        alias="objectId"
    )]
    fileset_id: Annotated[None, Field(
        alias="filesetId"
    )]

class DatasetResult(DatasetFields):
    image: list[Union[SuccessImageResponse, FailureImageResponse]]
    import_status: ImportStatus

class ProjectResult(ProjectFields):
    dataset: List[DatasetResult]
    import_status: ImportStatus

class UploadResult(UploadFields):
    project: List[ProjectResult]
    import_status: ImportStatus

class UploadResultSet(TaskQueueBase):
    task_id: Annotated[str, Field(alias='task-id')]
    state: State
    result: List[UploadResult]

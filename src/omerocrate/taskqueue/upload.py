import asyncio
from pathlib import Path
from typing import AsyncIterable, Any, Optional
from omero import gateway, model
import httpx
import os

from pydantic import Field, computed_field

from omerocrate.taskqueue import models as upload_models
from omerocrate.uploader import OmeroUploader
from uuid import uuid4

class TaskqueueUploader(OmeroUploader):
    """
    Subclass of OmeroUploader that uses `gs-taskqueue` to upload images to OMERO.
    """
    client: httpx.AsyncClient = Field(default_factory=httpx.AsyncClient, description="HTTP client for making requests to the Flower API server")
    host: str = Field(default_factory=lambda: os.environ["FLOWER_HOST"], description="Host of the Flower API server")
    username: str = Field(default_factory=lambda: os.environ["FLOWER_USER"], description="Username for the Flower API server")
    password: str = Field(default_factory=lambda: os.environ["FLOWER_PASSWORD"], description="Password for the Flower API server")

    @computed_field
    @property
    def http_auth(self) -> tuple[str, str]:
        """
        Returns the HTTP authentication credentials for the Flower API server.
        """
        return (self.username, self.password)

    async def upload_images(self, image_paths: list[Path], **kwargs: Any) -> AsyncIterable[gateway.ImageWrapper]:
        req = upload_models.UploadRequest(
            project=[upload_models.ProjectRequest(
                name=str(uuid4()),
                description=str(uuid4()),
                dataset=[upload_models.DatasetRequest(
                    name=str(uuid4()),
                    description=str(uuid4()),
                    image=[upload_models.ImageRequest(
                        name=str(uuid4()),
                        description=str(uuid4()),
                        file_path=str(path)
                    ) for path in image_paths]
                )]
            )],
            group="grp_omeplus",
            import_user=os.environ["OMERO_USER"],
        )

        task_id = (await self.upload_to_omero(req)).task_id
        while True:
            await asyncio.sleep(1)
            status = await self.upload_status(task_id)
            if status.state in {"SUCCESS", "FAILURE"}:
                break
        result = await self.upload_result(task_id)
        if (error := self.error_from_result(result)) is not None:
            raise Exception(error)
        for upload in result.result:
            for project in upload.project:
                for dataset in project.dataset:
                    for image in dataset.image:
                        if isinstance(image, upload_models.SuccessImageResponse):
                            for image_id in image.object_id:
                                yield gateway.ImageWrapper(conn=self.conn, obj=model.ImageI(image_id))

    def error_from_result(self, result: upload_models.UploadResultSet) -> Optional[str]:
        """
        Returns an error message if the upload failed, or None if it succeeded.
        """
        if result.state != "SUCCESS":
            return "Entire upload failed."
        for upload in result.result:
            if upload.import_status != "SUCCEEDED":
                return "Singular upload failed"
            for project in upload.project:
                for dataset in project.dataset:
                    if dataset.import_status != "SUCCEEDED":
                        return "Dataset upload failed."
                    for image in dataset.image:
                        if image.import_status != "SUCCEEDED":
                            return f"Image {image.file_path} upload failed with status {image.import_summary}"

    async def upload_to_omero(self, upload: upload_models.UploadRequest) -> upload_models.UploadReponse:
        """
        Submits the upload request to the Flower API server and returns the API response.
        """
        response = await self.client.post(
            f"{self.host}/flower/api/task/send-task/gs_import_run_omero_import" ,
            auth=self.http_auth,
            json={"args": [upload.model_dump()]},
            # verify=False
        )
        response.raise_for_status()
        return upload_models.UploadReponse.model_validate(response.json())

    async def upload_status(self, task_id: str):
        URL_CHECK_INFO = f"{self.host}/flower/api/task/info/{task_id}" 

        # Check the task status
        response = await self.client.get(
            URL_CHECK_INFO,
            auth=self.http_auth
        )
        response.raise_for_status()
        return upload_models.UploadStatus.model_validate(response.json())
        
    async def upload_result(self, task_id: str):
        response = await self.client.get(
            f"{self.host}/flower/api/task/result/{task_id}",
            auth=self.http_auth
        )
        response.raise_for_status()
        return upload_models.UploadResultSet.model_validate(response.json())

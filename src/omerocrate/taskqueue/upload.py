from pathlib import Path
from typing import Iterable, Any, Optional
from omero import gateway
import requests
import os

from omerocrate.taskqueue import models as upload_models
from omerocrate.uploader import OmeroUploader

class TaskqueueUploader(OmeroUploader):
    """
    Subclass of OmeroUploader that uses `gs-taskqueue` to upload images to OMERO.
    """
    def upload_images(self, image_paths: list[Path], **kwargs: Any) -> Iterable[gateway.ImageWrapper]:
        req = upload_models.Upload(
            project=[upload_models.Project(
                name="",
                description="",
                dataset=[upload_models.Dataset(
                    name="",
                    description="",
                    image=[upload_models.Image(
                        name="",
                        description="",
                        file_path=str(path)
                    ) for path in image_paths]
                )]
            )],
            group="",
            import_user=os.environ["OMERO_USER"],
        )

        upload_to_omero(req)

def upload_to_omero(upload: upload_models.Upload, host: Optional[str] = os.environ.get("FLOWER_HOST"), username: Optional[str] = os.environ.get("FLOWER_USER"), password: Optional[str] = os.environ.get("FLOWER_PASSWORD")) -> None:
    URL_SUBMIT = f"{host}/flower/api/task/send-task/gs_import_run_omero_import" 
    # URL_CHECK_INFO = f"{host}/flower/api/task/info/{task_id}" 
    # URL_RESULT = f"{host}/flower/api/task/result/{task_id}" 
    # URL_AUTH = ('HTACCESS_USERNAME', 'HTACCESS_PASSWORD')
    if host is None or username is None or password is None:
        raise ValueError("Host, username and password must be set")

    # Submit the task
    response = requests.post(
        URL_SUBMIT,
        auth=(username, password),
        data=upload.model_dump(),
        verify=False
    )
    response.raise_for_status()
    return response.json()

    # task_id = response.json()["task-id"]
    # print(f"Task submitted with id: {task_id}")

    # # Check the task status
    # response = requests.get(
    #     URL_CHECK_INFO.format(task_id=task_id),
    #     auth=URL_AUTH)
    # response.raise_for_status()

    # run_time = response.json()["runtime"]
    # while run_time is None:
    #     response = requests.get(
    #         URL_CHECK_INFO.format(task_id=task_id),
    #         auth=URL_AUTH)
    #     response.raise_for_status()
    #     print(f"Status: {response.json()['state']}")
    #     run_time = response.json()["runtime"]
    #     time.sleep(1)

    # # Get the result
    # response = requests.get(
    #     URL_RESULT.format(task_id=task_id),
    #     auth=URL_AUTH)
    # print(f"Import status: {response.json()['result'][0]['importStatus']}")

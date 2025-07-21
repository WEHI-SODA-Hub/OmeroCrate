from pathlib import Path
from dotenv import load_dotenv
import pytest
from omerocrate.uploader import OmeroUploader, ApiUploader
from omerocrate.taskqueue.upload import TaskqueueUploader
from omero.gateway import BlitzGateway, ImageWrapper, DatasetWrapper

from omerocrate.utils import delete_dataset

@pytest.mark.asyncio
async def test_upload_default(abstract_crate: Path, connection: BlitzGateway):
    uploader = ApiUploader(
        conn=connection,
        crate=abstract_crate
    )
    dataset = await uploader.execute()
    assert dataset.name == "Abstract art"
    assert dataset.countChildren() == 1
    for image in dataset.listChildren():
        assert "Color Study" in image.name
    delete_dataset(dataset)

@pytest.mark.asyncio
async def test_upload_queue(abstract_crate: Path, connection: BlitzGateway):
    load_dotenv()
    uploader = TaskqueueUploader(
        conn=connection,
        crate=abstract_crate
    )
    dataset = await uploader.execute()
    assert dataset.name == "Abstract art"
    assert dataset.countChildren() == 1
    assert dataset.getDetails().getGroup().getName() == "Abstract art", "The dataset group should be the crate name"
    for image in dataset.listChildren():
        assert "Color Study" in image.name
    delete_dataset(dataset)

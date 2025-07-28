from pathlib import Path
from dotenv import load_dotenv
import pytest
from omerocrate.uploader import ApiUploader, OmeroUploader
from omerocrate.taskqueue.upload import TaskqueueUploader
from omero.gateway import BlitzGateway
import os

from omerocrate.utils import delete_dataset

async def test_uploader(uploader: OmeroUploader):
    load_dotenv()
    dataset = await uploader.execute()
    assert dataset.name == "Abstract art"
    assert dataset.countChildren() == 1
    assert dataset.getDetails().getGroup().getName() == "Abstract art", "The dataset group should be the crate name"
    for image in dataset.listChildren():
        assert "Color Study" in image.name
    delete_dataset(dataset)


@pytest.mark.asyncio
async def test_upload_default(abstract_crate: Path, connection: BlitzGateway):
    uploader = ApiUploader(
        conn=connection,
        crate=abstract_crate
    )
    await test_uploader(uploader)

@pytest.mark.skipif(not os.environ.get("FLOWER_HOST"), reason="OMERO taskqueue not available")
@pytest.mark.asyncio
async def test_upload_queue(abstract_crate: Path, connection: BlitzGateway):
    uploader = TaskqueueUploader(
        conn=connection,
        crate=abstract_crate
    )
    await test_uploader(uploader)

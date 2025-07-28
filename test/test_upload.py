from pathlib import Path
import pytest
from omerocrate.uploader import ApiUploader, OmeroUploader
from omerocrate.taskqueue.upload import TaskqueueUploader
from omero.gateway import BlitzGateway
from .util import check_art_dataset, requires_flower


@pytest.mark.parametrize("uploader", [
    ApiUploader,
    pytest.param(TaskqueueUploader, marks=requires_flower)
])
@pytest.mark.asyncio
async def test_upload_api(abstract_crate: Path, connection: BlitzGateway, Uploader: type[OmeroUploader]):
    uploader = Uploader(
        conn=connection,
        crate=abstract_crate
    )
    dataset = await uploader.execute()
    check_art_dataset(dataset)
    # Test twice to ensure that the tests work with an existing group
    dataset = await uploader.execute()
    check_art_dataset(dataset)

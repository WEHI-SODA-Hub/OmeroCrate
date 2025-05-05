from pathlib import Path
from omerocrate.uploader import OmeroUploader, ApiUploader
from omero.gateway import BlitzGateway, ImageWrapper, DatasetWrapper

from omerocrate.utils import delete_dataset

def test_upload_default(abstract_crate: Path, connection: BlitzGateway):
    uploader = ApiUploader(
        conn=connection,
        crate=abstract_crate
    )
    dataset = uploader.execute()
    assert dataset.name == "Abstract art"
    assert dataset.countChildren() == 1
    for image in dataset.listChildren():
        assert "Color Study" in image.name
    delete_dataset(dataset)

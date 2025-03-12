from pathlib import Path
from omerocrate.uploader import OmeroUploader
from omero.gateway import BlitzGateway, ImageWrapper, DatasetWrapper

from omerocrate.utils import delete_dataset

def test_upload_default(ca_imaging_1021: Path, connection: BlitzGateway):
    uploader = OmeroUploader(
        conn=connection,
        crate=ca_imaging_1021
    )
    dataset = uploader.execute()
    assert dataset.name == "Ca-imaging (with stimulation)"
    assert dataset.countChildren() == 24
    delete_dataset(dataset)

def test_custom_uploader(ca_imaging_1021: Path, connection: BlitzGateway):
    from calcium_uploader import CalciumUploader
    uploader = CalciumUploader(
        conn=connection,
        crate=ca_imaging_1021
    )
    dataset = uploader.execute()
    assert dataset.name == "Ca-imaging (with stimulation)"
    assert dataset.countChildren() == 24
    # Not all images have acquisition dates, but some do
    assert any(child.getAcquisitionDate() is not None for child in dataset.listChildren())
    delete_dataset(dataset)

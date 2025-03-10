from pathlib import Path
from omerocrate.uploader import OmeroUploader
from omerocrate.gateway import from_env
from omero.gateway import BlitzGateway
import os
import dotenv

# To run the tests, each user will need to provide credentials for their own OMERO server
# .env is a convenient way to store these credentials
dotenv.load_dotenv()

def test_upload_report(ca_imaging_1021: Path):
    uploader = OmeroUploader(
        conn = from_env(),
        crate=ca_imaging_1021
    )
    dataset = uploader.execute()
    assert dataset.name == "Ca-imaging (with stimulation)"
    assert dataset.countChildren() == 24

from pathlib import Path
from omerocrate.uploader import OmeroUploader, BlitzGateway
import os
import dotenv

dotenv.load_dotenv()

def test_upload_report(ca_imaging_1021: Path):
    uploader = OmeroUploader(
        conn = BlitzGateway(
            username=os.environ["OMERO_USER"],
            passwd=os.environ["OMERO_PASSWORD"],
            host=os.environ["OMERO_HOST"],
            port=os.environ["OMERO_PORT"],
            secure=True
        ),
        crate=ca_imaging_1021
    )
    uploader.execute()

from pathlib import Path
from omero.gateway import BlitzGateway
from typer.testing import CliRunner
from util import check_art_dataset
from omerocrate.cli import app
import pytest
    connection.setGroupNameForSession("Abstract art")
@pytest.mark.parametrize("uploader", ["omerocrate.ApiUploader", "omerocrate.TaskqueueUploader"])
def test_cli(connection: BlitzGateway, abstract_crate: Path, uploader: str):
    result = CliRunner(mix_stderr=False).invoke(app, [str(abstract_crate), "--uploader", uploader])
    # Can't query the dataset unless we are in the right group
    connection.setGroupNameForSession("Abstract art")
    # Parse the dataset ID from the output
    dataset = connection.getObject("Dataset", int(result.stdout))
    check_art_dataset(dataset)

import os
from pathlib import Path
from omero.gateway import DatasetWrapper
import pytest
from omerocrate.utils import delete_dataset
from dotenv import get_key

def check_art_dataset(dataset: DatasetWrapper):
    """
    Check if the test dataset has been uploaded correctly
    """
    assert dataset.name == "Abstract art"
    assert dataset.countChildren() == 1
    assert dataset.getDetails().getGroup().getName() == "Abstract art", "The dataset group should be the crate name"
    for image in dataset.listChildren():
        assert "Color Study" in image.name
    delete_dataset(dataset)

root = Path(__file__).parent.parent
requires_flower= pytest.mark.skipif(not (os.environ.get("FLOWER_HOST") or get_key(root / ".env", "FLOWER_HOST")), reason="OMERO taskqueue not available")

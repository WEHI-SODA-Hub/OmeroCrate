from omero.gateway import DatasetWrapper
from omerocrate.utils import delete_dataset


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

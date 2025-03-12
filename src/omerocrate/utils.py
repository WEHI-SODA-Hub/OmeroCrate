from omero.gateway import DatasetWrapper

def delete_dataset(dataset: DatasetWrapper):
    """
    Delete a dataset and all its children.
    """
    dataset._conn.deleteObjects("Dataset", [dataset._obj.id.val], deleteChildren=True, deleteAnns=True, wait=True)

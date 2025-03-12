from pathlib import Path
from typing import Annotated
import typer

from omerocrate.gateway import from_env
from omerocrate.uploader import OmeroUploader

app = typer.Typer(help="CLI for uploading RO-Crates to OMERO")

@app.command(help="Upload an RO-Crate to OMERO")
def upload(crate: Annotated[Path, typer.Argument(help="Path to the directory containing the RO-Crate")]):
    uploader = OmeroUploader(
        conn=from_env(),
        crate=crate
    )
    uploader.execute()

def main():
    app()

from pathlib import Path
from typing import Annotated
import typer
from importlib import import_module
from asyncio import run
from omerocrate.gateway import from_env
from omerocrate.uploader import OmeroUploader

app = typer.Typer(help="CLI for uploading RO-Crates to OMERO")

@app.command(help="Upload an RO-Crate to OMERO")
def upload(
    crate: Annotated[Path, typer.Argument(help="Path to the directory containing the RO-Crate")],
    uploader_path: Annotated[str, typer.Option("--uploader", "-u", help="Module path to the OmeroUploader class")] = "omerocrate.ApiUploader"
):
    module_path, cls_name = uploader_path.rsplit('.', 1)
    module = import_module(module_path)
    uploader_cls = getattr(module, cls_name)
    if not issubclass(uploader_cls, OmeroUploader):
        raise typer.BadParameter(f"{uploader_path} is not a valid OmeroUploader class")
    
    uploader = uploader_cls(
        conn=from_env(),
        crate=crate
    )
    dataset = run(uploader.execute())
    # stderr
    typer.echo(f"Uploaded dataset with ID: {dataset.id} and name: {dataset.name}", err=True)
    # stdout
    typer.echo(dataset.id)

def main():
    app()

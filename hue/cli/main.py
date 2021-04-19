import typer

from hue import __version__

from . import bridge, light

app = typer.Typer()
app.add_typer(bridge.app, name="bridge", help="Interact with the Bridge API")
app.add_typer(light.app, name="light", help="Interact with the Lights API")


@app.command()
def version():
    """Show version of hue-api installed"""
    typer.echo(f"hue-api version: {__version__}")

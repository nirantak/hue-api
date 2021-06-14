import typer

from hue import __version__
from hue.cli.console import console

from . import bridge, light

app = typer.Typer(name="hue")
app.add_typer(bridge.app, name="bridge", help="Interact with the Bridge API")
app.add_typer(light.app, name="light", help="Interact with the Lights API")


@app.command()
def version():
    """Show version of hue-api installed"""
    console.print(f"hue-api version: {__version__}")

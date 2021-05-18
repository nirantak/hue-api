import asyncio
import json

import typer

from hue import Bridge
from hue.cli.console import console

app = typer.Typer()


@app.command()
def discover():
    resp = asyncio.run(Bridge.discover())
    console.print(f"Hue Bridges discovered: {json.dumps(resp, indent=2)}")

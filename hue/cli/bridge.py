import asyncio
import json

import typer

from hue import Bridge

app = typer.Typer()


@app.command()
def discover():
    resp = asyncio.run(Bridge.discover())
    typer.echo(f"Hue Bridges discovered: {json.dumps(resp, indent=2)}")

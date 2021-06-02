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


@app.command()
def info(
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    bridge = Bridge(ip=ip, user=user)
    resp = asyncio.run(bridge.get_info())
    console.print(json.dumps(resp, indent=2))


@app.command()
def get(
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    bridge = Bridge(ip=ip, user=user)
    resp = asyncio.run(bridge.get_config())
    console.print(json.dumps(resp, indent=2))

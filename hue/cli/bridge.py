import asyncio
import json

import typer

from hue import Bridge
from hue.cli.console import console

app = typer.Typer()


@app.command()
def discover():
    """Discover online Bridges in the local network"""
    resp = asyncio.run(Bridge.discover())
    console.print(f"Hue Bridges Discovered:\n{json.dumps(resp, indent=2)}")


@app.command()
def info(
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """List all the information about a Hue Bridge"""
    bridge = Bridge(ip=ip, user=user)
    resp = asyncio.run(bridge.get_info())
    console.print(f"[{ip}] Bridge Info:\n{json.dumps(resp, indent=2)}")


@app.command()
def get(
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Get the config of a Bridge"""
    bridge = Bridge(ip=ip, user=user)
    resp = asyncio.run(bridge.get_config())
    console.print(f"[{ip}] Bridge Config:\n{json.dumps(resp, indent=2)}")

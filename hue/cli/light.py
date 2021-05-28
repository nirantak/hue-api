import asyncio
import json

import typer

from hue import Light
from hue.cli.console import console

app = typer.Typer()


@app.command()
def info(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.get_info())
    console.print(json.dumps(resp, indent=2))


@app.command()
def get(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.get_state())
    console.print(json.dumps(resp, indent=2))


@app.command()
def on(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.switch_on())
    console.print(json.dumps(resp, indent=2))


@app.command()
def off(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.switch_off())
    console.print(json.dumps(resp, indent=2))


@app.command()
def toggle(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.toggle())
    console.print(json.dumps(resp, indent=2))

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
    """List all the information about a Hue Light"""
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.get_info())
    console.print(f"[{ip}] Light {id}:\n{json.dumps(resp, indent=2)}")


@app.command()
def get(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Get the state of a Light"""
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.get_state())
    console.print(f"[{ip}] Light {id} State:\n{json.dumps(resp, indent=2)}")


@app.command()
def on(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Power on a light"""
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.power_on())
    console.print(f"[{ip}] Light {id} On:\n{json.dumps(resp, indent=2)}")


@app.command()
def off(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Power off a light"""
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.power_off())
    console.print(f"[{ip}] Light {id} Off:\n{json.dumps(resp, indent=2)}")


@app.command()
def toggle(
    id: int = typer.Argument(1),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Toggle the power state of a light"""
    light = Light(id, ip=ip, user=user)
    resp = asyncio.run(light.toggle())
    console.print(f"[{ip}] Light {id} Toggle:\n{json.dumps(resp, indent=2)}")

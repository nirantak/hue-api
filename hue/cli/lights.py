import asyncio
import json

import typer

from hue import LightGroup
from hue.cli.console import console

app = typer.Typer()


@app.command()
def info(
    name: str = typer.Argument(...),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """List information of light group"""
    group = LightGroup(name=name, ip=ip, user=user)
    resp = asyncio.run(group.get_info())
    console.print(f"[{ip}] Light Group {repr(name)} Info:\n{json.dumps(resp, indent=2)}")


@app.command()
def list(
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """List all light groups"""
    resp = asyncio.run(LightGroup.list(ip, user))
    console.print(f"[{ip}] Light Groups:\n{json.dumps(resp, indent=2)}")


@app.command()
def on(
    name: str = typer.Argument(...),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Power on a light group"""
    group = LightGroup(name=name, ip=ip, user=user)
    resp = asyncio.run(group.power_on())
    console.print(f"[{ip}] Light Group {repr(name)} On:\n{json.dumps(resp, indent=2)}")


@app.command()
def off(
    name: str = typer.Argument(...),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Power off a light group"""
    group = LightGroup(name=name, ip=ip, user=user)
    resp = asyncio.run(group.power_off())
    console.print(f"[{ip}] Light Group {repr(name)} Off:\n{json.dumps(resp, indent=2)}")


@app.command()
def toggle(
    name: str = typer.Argument(...),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
):
    """Toggle a light group on and off"""
    group = LightGroup(name=name, ip=ip, user=user)
    resp = asyncio.run(group.toggle())
    console.print(f"[{ip}] Light Group {repr(name)} Toggle:\n{json.dumps(resp, indent=2)}")


@app.command()
def brightness(
    name: str = typer.Argument(...),
    ip: str = typer.Option(..., "--ip", "-i", envvar="HUE_BRIDGE_IP"),
    user: str = typer.Option(..., "--user", "-u", envvar="HUE_BRIDGE_USER"),
    bri: int = typer.Option(..., "--brightness", "-b", min=1, max=255),
):
    """Power off a light group"""
    group = LightGroup(name=name, ip=ip, user=user)
    resp = asyncio.run(group.set_brightness(bri))
    console.print(f"[{ip}] Light Group {repr(name)} Brightness:\n{json.dumps(resp, indent=2)}")

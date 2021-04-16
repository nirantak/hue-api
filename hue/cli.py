import os

import typer

app = typer.Typer()
HUE_BRIDGE_IP = os.environ.get("HUE_BRIDGE_IP")
HUE_BRIDGE_USER = os.environ.get("HUE_BRIDGE_USER")


@app.command()
def test():
    typer.echo("Hue CLI - coming soon")


if __name__ == "__main__":
    app()

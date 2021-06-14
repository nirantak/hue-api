from typer.testing import CliRunner

from hue import __version__, cli


def test_command_line_interface():
    """Test the CLI"""
    runner = CliRunner()

    res = runner.invoke(cli.app, ["--help"])
    assert res.exit_code == 0
    assert "Usage: hue" in res.output
    assert "Show this message and exit" in res.output

    res = runner.invoke(cli.app, ["version"])
    assert res.exit_code == 0
    assert res.output == f"hue-api version: {__version__}\n"

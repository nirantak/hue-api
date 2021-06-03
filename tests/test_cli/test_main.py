from typer.testing import CliRunner

from hue import __version__, cli


def test_command_line_interface():
    """Test the CLI"""
    runner = CliRunner()

    res = runner.invoke(cli.app, ["--help"])
    assert res.exit_code == 0
    assert "Show this message and exit" in res.output

    res = runner.invoke(cli.app, ["version"])
    assert res.exit_code == 0
    assert f"{__version__}" in res.output

from typer.testing import CliRunner

from hue import cli


def test_command_line_interface():
    """Test the CLI"""
    runner = CliRunner()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert "Hue CLI" in result.output
    help_result = runner.invoke(cli.app, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit" in help_result.output

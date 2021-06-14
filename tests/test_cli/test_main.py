from typer.testing import CliRunner

from hue import __version__, cli


class TestCLI:
    def test_cli_init(self):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["--help"])
        assert res.exit_code == 0
        assert "Usage: hue" in res.output
        assert "Show this message and exit" in res.output

    def test_cli_version(self):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["version"])
        assert res.exit_code == 0
        assert res.output == f"hue-api version: {__version__}\n"

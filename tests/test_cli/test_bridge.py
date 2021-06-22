import os
from unittest.mock import patch

from faker import Faker
from typer.testing import CliRunner

from hue import cli


class TestBridgeCLI:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()

    @classmethod
    def setup_class():
        try:
            del os.environ["HUE_BRIDGE_IP"]
            del os.environ["HUE_BRIDGE_USER"]
        except KeyError:
            pass

    @patch("hue.api.bridge.Bridge.discover", return_value={})
    def test_bridge_discover(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["bridge", "discover", "--help"])
        assert res.exit_code == 0
        assert "Discover online Bridges in the local network" in res.output

        res = runner.invoke(cli.app, ["bridge", "discover"])
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == "Hue Bridges Discovered:\n{}\n"

    @patch("hue.api.bridge.Bridge.get_info", return_value={})
    def test_bridge_info(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["bridge", "info", "--help"])
        assert res.exit_code == 0
        assert "List all the information about a Hue Bridge" in res.output

        res = runner.invoke(cli.app, ["bridge", "info", "-i", self.ip, "-u", self.user])
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Bridge Info:\n{{}}\n"

    @patch("hue.api.bridge.Bridge.get_info", return_value={})
    def test_bridge_info_failure(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["bridge", "info"])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--ip'" in res.output

        res = runner.invoke(cli.app, ["bridge", "info", "-i", self.ip])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--user'" in res.output

    @patch("hue.api.bridge.Bridge.get_config", return_value={})
    def test_bridge_config(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["bridge", "get", "--help"])
        assert res.exit_code == 0
        assert "Get the config of a Bridge" in res.output

        res = runner.invoke(cli.app, ["bridge", "get", "-i", self.ip, "-u", self.user])
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Bridge Config:\n{{}}\n"

    @patch("hue.api.bridge.Bridge.get_config", return_value={})
    def test_bridge_config_failure(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["bridge", "get"])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--ip'" in res.output

        res = runner.invoke(cli.app, ["bridge", "get", "-i", self.ip])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--user'" in res.output

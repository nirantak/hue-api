import os
from unittest.mock import patch

from faker import Faker
from typer.testing import CliRunner

from hue import cli


class TestLightCLI:
    fake = Faker()
    num = fake.random_int()
    ip = fake.ipv4_private()
    user = fake.uuid4()

    @classmethod
    def setup_class():
        try:
            del os.environ["HUE_BRIDGE_IP"]
            del os.environ["HUE_BRIDGE_USER"]
        except KeyError:
            pass

    @patch("hue.api.light.Light.get_info", return_value={})
    def test_light_info(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "info", "--help"])
        assert res.exit_code == 0
        assert "List all the information about a Hue Light" in res.output

        res = runner.invoke(
            cli.app, ["light", "info", str(self.num), "-i", self.ip, "-u", self.user]
        )
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num}:\n{{}}\n"

    @patch("hue.api.light.Light.get_info", return_value={})
    def test_light_info_failure(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "info"])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--ip'" in res.output

        res = runner.invoke(cli.app, ["light", "info", "-i", self.ip])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--user'" in res.output

    @patch("hue.api.light.Light.get_state", return_value={})
    def test_light_state(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "get", "--help"])
        assert res.exit_code == 0
        assert "Get the state of a Light" in res.output

        res = runner.invoke(
            cli.app, ["light", "get", str(self.num), "-i", self.ip, "-u", self.user]
        )
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num} State:\n{{}}\n"

    @patch("hue.api.light.Light.get_state", return_value={})
    def test_light_config_failure(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "get"])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--ip'" in res.output

        res = runner.invoke(cli.app, ["light", "get", "-i", self.ip])
        assert res.exit_code == 2
        assert api_mock.call_count == 0
        assert "Error: Missing option '--user'" in res.output

    @patch("hue.api.light.Light.power_on", return_value={})
    def test_light_power_on(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "on", "--help"])
        assert res.exit_code == 0
        assert "Power on a light" in res.output

        res = runner.invoke(cli.app, ["light", "on", str(self.num), "-i", self.ip, "-u", self.user])
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num} On:\n{{}}\n"

    @patch("hue.api.light.Light.power_off", return_value={})
    def test_light_power_off(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "off", "--help"])
        assert res.exit_code == 0
        assert "Power off a light" in res.output

        res = runner.invoke(
            cli.app, ["light", "off", str(self.num), "-i", self.ip, "-u", self.user]
        )
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num} Off:\n{{}}\n"

    @patch("hue.api.light.Light.toggle", return_value={})
    def test_light_toggle(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "toggle", "--help"])
        assert res.exit_code == 0
        assert "Toggle the power state of a light" in res.output

        res = runner.invoke(
            cli.app, ["light", "toggle", str(self.num), "-i", self.ip, "-u", self.user]
        )
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num} Toggle:\n{{}}\n"

    @patch("hue.api.light.Light.set_brightness", return_value={})
    def test_light_brightness(self, api_mock):
        runner = CliRunner()

        res = runner.invoke(cli.app, ["light", "brightness", "--help"])
        assert res.exit_code == 0
        assert "Set the brightness of a light" in res.output

        res = runner.invoke(
            cli.app, ["light", "brightness", str(self.num), "-b", 1, "-i", self.ip, "-u", self.user]
        )
        assert res.exit_code == 0
        assert api_mock.call_count == 1
        assert res.output == f"[{self.ip}] Light {self.num} Brightness:\n{{}}\n"

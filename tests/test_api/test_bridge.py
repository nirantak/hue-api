from unittest.mock import patch

import pytest
from faker import Faker

from hue import Bridge


class TestBridge:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()

    def test_bridge_init(self):
        bridge = Bridge(ip=self.ip, user=self.user)
        assert bridge.ip == self.ip
        assert bridge.user == self.user
        assert str(bridge) == f"<Bridge {self.ip}>"

    def test_bridge_url(self):
        bridge = Bridge(ip=self.ip, user=self.user)
        assert bridge.url == f"http://{self.ip}/api/{self.user}"

    @patch("hue.api.http.get_json")
    @pytest.mark.asyncio
    async def test_bridge_discover(self, mock_http):
        bridge = Bridge(ip=self.ip, user=self.user)
        await bridge.discover()
        mock_http.assert_called_once_with("https://discovery.meethue.com/")
        assert mock_http.call_count == 1

    @patch("hue.api.http.get_json")
    @pytest.mark.asyncio
    async def test_bridge_info(self, mock_http):
        mock_resp = {"state": True}
        mock_http.return_value = mock_resp
        bridge = Bridge(ip=self.ip, user=self.user)
        resp = await bridge.get_info()
        mock_http.assert_called_once_with(f"http://{self.ip}/api/{self.user}")
        assert mock_http.call_count == 1
        assert resp == mock_resp
        assert bridge.info == mock_resp

    @patch("hue.api.bridge.Bridge.get_info")
    @pytest.mark.asyncio
    async def test_bridge_config(self, mock_http):
        mock_resp = {"config": {"state": True}}
        mock_http.return_value = mock_resp
        bridge = Bridge(ip=self.ip, user=self.user)
        resp = await bridge.get_config()
        assert mock_http.call_count == 1
        assert resp == mock_resp["config"]

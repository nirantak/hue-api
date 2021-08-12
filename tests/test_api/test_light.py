from unittest.mock import MagicMock, patch

import pytest
from faker import Faker

from hue import Light


class TestLight:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()
    num = fake.random_int()
    mock_resp = {
        "state": {"on": True, "bri": 200, "xy": [0.5, 0.5]},
        "name": f"Light {num}",
    }

    def test_light_init(self):
        light = Light(self.num, ip=self.ip, user=self.user)
        assert light.id == self.num
        assert light.ip == self.ip
        assert light.user == self.user
        assert light.on is None
        assert light.info == {}
        assert light.state == {}
        assert light.saved_state == {}
        assert str(light) == f"<Light {self.num}>"
        assert repr(light) == f"<Light id={self.num} on={None} ip={self.ip}>"

    def test_light_url(self):
        light = Light(self.num, ip=self.ip, user=self.user)
        assert light.url == f"http://{self.ip}/api/{self.user}/lights/{self.num}"

    @patch("hue.api.http.get_json")
    @pytest.mark.asyncio
    async def test_light_info(self, mock_http):
        mock_http.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        resp = await light.get_info()
        mock_http.assert_called_once_with(f"http://{self.ip}/api/{self.user}/lights/{self.num}")
        assert mock_http.call_count == 1
        assert resp == self.mock_resp
        assert light.info == self.mock_resp

    @patch("hue.api.light.Light.get_info")
    @pytest.mark.asyncio
    async def test_light_get_state(self, mock_http):
        mock_http.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        resp = await light.get_state()
        assert mock_http.call_count == 1
        assert resp == self.mock_resp["state"]
        assert light.state == self.mock_resp["state"]
        assert light.on == self.mock_resp["state"]["on"]

    @pytest.mark.parametrize("state", [None, {"bri": 1}])
    @patch("hue.api.http.put")
    @patch("hue.api.light.Light.get_state")
    @pytest.mark.asyncio
    async def test_light_set_state(self, mock_http_get, mock_http_put, state):
        mock_http_put.return_value.json = MagicMock(return_value=self.mock_resp)
        light = Light(self.num, ip=self.ip, user=self.user)
        state = self.mock_resp["state"] if state is None else state
        resp = await light.set_state(state)
        mock_http_put.assert_called_once_with(
            f"http://{self.ip}/api/{self.user}/lights/{self.num}/state",
            state,
        )
        assert mock_http_put.call_count == 1
        assert mock_http_get.call_count == 1
        assert resp == self.mock_resp

    @patch("hue.api.light.Light.get_state")
    @pytest.mark.asyncio
    async def test_light_save_state(self, mock_http):
        mock_http.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        resp = await light.save_state()
        assert mock_http.call_count == 1
        assert resp == self.mock_resp
        assert light.saved_state == self.mock_resp

    @patch("hue.api.light.Light.set_state")
    @pytest.mark.asyncio
    async def test_light_restore_state(self, mock_http):
        mock_http.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        light.saved_state = self.mock_resp
        resp = await light.restore_state()
        mock_http.assert_called_once_with(self.mock_resp)
        assert mock_http.call_count == 1
        assert resp == self.mock_resp

    @pytest.mark.parametrize("power,state", [("on", True), ("off", False)])
    @patch("hue.api.light.Light.set_state")
    @pytest.mark.asyncio
    async def test_light_power(self, mock_http, power, state):
        mock_http.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        power_method = getattr(light, f"power_{power}")
        resp = await power_method()
        mock_http.assert_called_once_with({"on": state})
        assert mock_http.call_count == 1
        assert resp == self.mock_resp

    @pytest.mark.parametrize("power", [(True,), (False,)])
    @patch("hue.api.light.Light.set_state")
    @patch("hue.api.light.Light.get_state")
    @pytest.mark.asyncio
    async def test_light_toggle(self, mock_http_get, mock_http_set, power):
        mock_http_set.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        light.on = power
        resp = await light.toggle()
        mock_http_set.assert_called_once_with({"on": not power})
        assert mock_http_get.call_count == 1
        assert mock_http_set.call_count == 1
        assert resp == self.mock_resp

    @pytest.mark.parametrize("brightness", [1, 128, 255])
    @patch("hue.api.light.Light.set_state")
    @patch("hue.api.light.Light.get_state")
    @pytest.mark.asyncio
    async def test_light_brightness(self, mock_http_get, mock_http_set, brightness):
        mock_http_set.return_value = self.mock_resp
        light = Light(self.num, ip=self.ip, user=self.user)
        resp = await light.set_brightness(brightness)
        mock_http_set.assert_called_once_with({"bri": brightness})
        assert mock_http_get.call_count == 1
        assert mock_http_set.call_count == 1
        assert resp == self.mock_resp

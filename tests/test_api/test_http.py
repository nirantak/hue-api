from unittest.mock import MagicMock, patch

import pytest
from faker import Faker

from hue.api import http


class TestHttp:
    fake = Faker()
    url = fake.uri()
    mock_resp = {"status": 200, "data": {}}
    mock_json = fake.json()

    @patch("httpx.AsyncClient.get")
    @pytest.mark.asyncio
    async def test_http_get(self, mock_client):
        mock_client.return_value = self.mock_json
        resp = await http.get(self.url)
        mock_client.assert_called_once_with(self.url)
        assert mock_client.call_count == 1
        assert resp == self.mock_json

    @patch("hue.api.http.get")
    @pytest.mark.asyncio
    async def test_http_get_json(self, mock_client):
        mock_client.return_value.json = MagicMock(return_value=self.mock_resp)
        resp = await http.get_json(self.url)
        mock_client.assert_called_once_with(self.url)
        assert mock_client.call_count == 1
        assert resp == self.mock_resp

    @patch("httpx.AsyncClient.put")
    @pytest.mark.asyncio
    async def test_http_put(self, mock_client):
        mock_client.return_value = self.mock_resp
        resp = await http.put(self.url, self.mock_json)
        mock_client.assert_called_once_with(self.url, json=self.mock_json)
        assert mock_client.call_count == 1
        assert resp == self.mock_resp

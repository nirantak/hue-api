from __future__ import annotations

from typing import Any

from . import http


class Bridge:
    """Interact with the Hue Bridge API"""

    def __init__(self: Bridge, *, ip: str, user: str):
        self.ip: str = ip
        self.user: str = user
        self.info: dict[str, Any] = {}

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} {self.ip}>"

    @property
    def url(self) -> str:
        """Return the Hue Bridge URL"""
        return f"http://{self.ip}/api/{self.user}"

    @staticmethod
    async def discover() -> dict[str, str]:
        """Discover Hue Bridges available in this local network"""
        return await http.get_json("https://discovery.meethue.com/")

    async def get_info(self) -> dict[str, Any]:
        """List all the information about a Hue Bridge"""
        self.info = await http.get_json(self.url)
        return self.info

    async def get_config(self) -> dict[str, Any]:
        """Get the config of a Hue Bridge"""
        resp = await self.get_info()
        return resp["config"]

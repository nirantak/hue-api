from __future__ import annotations

from typing import Any

from . import http


class Bridge:
    """
    Interact with the Hue Bridge API

    Example:
        >>> from hue import Bridge
        >>> bridge = Bridge(ip="192.168.1.10", user="xxxx")

    Attributes:
        ip: IP address of the Hue Bridge
        user: The secret user id used to access the Hue API
        info: The last Bridge information stored in the object
            by calling `get_info()` or `get_config()`
    """

    def __init__(self: Bridge, *, ip: str, user: str) -> Bridge:
        """
        Initialize a Hue Bridge object

        Arguments:
            ip: IP address of the Hue Bridge, get it by running `hue bridge discover`
            user: The secret user id created to access the Hue API

        Returns:
            An object of class Bridge
        """
        self.ip: str = ip
        self.user: str = user
        self.info: dict[str, Any] = {}

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} {self.ip}>"

    @property
    def url(self) -> str:
        """Returns the Hue Bridge URL"""
        return f"http://{self.ip}/api/{self.user}"

    @staticmethod
    async def discover() -> list[dict[str, str]]:
        """
        Discover Hue Bridges available in this local network

        Returns:
            A list of Hue Bridges discovered in the local network
        """
        return await http.get_json("https://discovery.meethue.com/")

    async def get_info(self) -> dict[str, Any]:
        """
        List all the information about the Hue Bridge

        Returns:
            A dictionary of all the information about the Hue Bridge
        """
        self.info = await http.get_json(self.url)
        return self.info

    async def get_config(self) -> dict[str, Any]:
        """
        Get the current config of the Bridge

        Returns:
            A dictionary of the configuration of the Hue Bridge
        """
        resp = await self.get_info()
        return resp["config"]

from __future__ import annotations

from typing import Any

from . import http


class Bridge:
    def __init__(self: Bridge, *, ip: str, user: str):
        self.ip: str = ip
        self.user: str = user
        self.info: dict[str, Any] = {}

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} {self.ip}>"

    @property
    def url(self) -> str:
        return f"http://{self.ip}/api/{self.user}"

    @staticmethod
    async def discover() -> dict[str, str]:
        return await http.get_json("https://discovery.meethue.com/")

    async def get_info(self) -> dict[str, Any]:
        self.info = await http.get_json(self.url)
        return self.info

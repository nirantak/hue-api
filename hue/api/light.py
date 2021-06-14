from __future__ import annotations

from typing import Any

from . import http
from .bridge import Bridge


class Light(Bridge):
    def __init__(self: Light, id: int, *, ip: str, user: str):
        self.id: int = id
        self.on: bool = None
        self.info: dict[str, Any] = {}
        self.state: dict[str, Any] = {}
        self.saved_state: dict[str, Any] = {}
        super().__init__(ip=ip, user=user)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} {self.id}>"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} id={self.id} on={self.on} ip={self.ip}>"

    @property
    def url(self) -> str:
        return f"{super().url}/lights/{self.id}"

    async def get_info(self) -> dict[str, Any]:
        self.info = await http.get_json(self.url)
        return self.info

    async def get_state(self) -> dict[str, Any]:
        resp = await self.get_info()
        self.state = resp["state"]
        self.on = resp["state"]["on"]
        return self.state

    async def set_state(self, state: dict[str, Any]) -> dict[str, Any]:
        data = {"on": bool(state.get("on"))}
        for key in ["bri", "hue", "sat", "xy", "ct"]:
            value = state.get(key)
            if value:
                data[key] = value
        resp = await http.put(f"{self.url}/state", data)
        await self.get_state()
        return resp.json()

    async def save_state(self) -> dict[str, Any]:
        self.saved_state = await self.get_state()
        return self.saved_state

    async def restore_state(self) -> dict[str, Any]:
        resp = await self.set_state(self.saved_state)
        return resp

    async def power_on(self) -> dict[str, Any]:
        return await self.set_state({"on": True})

    async def power_off(self) -> dict[str, Any]:
        return await self.set_state({"on": False})

    async def toggle(self) -> dict[str, Any]:
        await self.get_state()
        return await self.set_state({"on": not self.on})

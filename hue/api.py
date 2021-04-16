from __future__ import annotations

from typing import Any

from hue import http


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


class Light(Bridge):
    def __init__(self: Light, id: int, *, ip: str, user: str):
        self.id: int = id
        self.on: bool = None
        self.info: dict[str, Any] = {}
        self.saved_state: dict[str, Any] = {}
        self.current_state: dict[str, Any] = {}
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
        self.current_state = resp["state"]
        self.on = resp["state"]["on"]
        return self.current_state

    async def set_state(
        self, state: dict[str, Any]
    ) -> tuple[bool, dict[str, Any]]:
        data = {"on": bool(state.get("on"))}
        for i in ["bri", "hue", "sat", "xy", "ct"]:
            s = state.get(i)
            if s:
                data[i] = s
        self.on = data["on"]
        resp = await http.put(f"{self.url}/state", data)
        return (resp.status_code == 200, resp.json())

    async def save_state(self) -> dict[str, Any]:
        self.saved_state = await self.get_state()
        return self.saved_state

    async def restore_state(self) -> dict[str, Any]:
        state = await self.set_state(self.saved_state)
        self.on = state["on"]
        return state

    async def switch_on(self) -> bool:
        self.on = True
        status, _ = await self.set_state(self.id, {"on": True})
        return status

    async def switch_off(self) -> bool:
        self.on = False
        status, _ = await self.set_state(self.id, {"on": False})
        return status

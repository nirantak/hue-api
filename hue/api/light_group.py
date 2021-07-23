from __future__ import annotations

from copy import deepcopy

from . import http
from .bridge import Bridge


class LightGroup(Bridge):
    """
    Interact with the Hue Lights API

    Example:
        >>> from hue import LightGroup
        >>> bridge = LightGroup("All", ip="192.168.1.10", user="xxxx")

    Attributes:
        name: Name of the Hue Light group
        ip (str): IP address of the Hue Bridge
        user (str): The secret user id used to access the Hue API
    """

    def __init__(self: LightGroup, name: str, *, ip: str, user: str) -> LightGroup:
        """
        Initialize a Hue Light object

        Arguments:
            name: The name of the Light group to control
            ip: IP address of the Hue Bridge, get it by running `hue bridge discover`
            user: The secret user id created to access the Hue API

        Returns:
            An object of class Light
        """
        self.name: str = name
        self.lights = None
        self.group_state = None
        self.on = None
        self.id = None
        self.brightness = None
        super().__init__(ip=ip, user=user)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} {self.name}>"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"<{class_name} id={self.name} ip={self.ip}>"

    @staticmethod
    async def list(ip: str, user: str):
        groups = (await http.get(f"http://{ip}/api/{user}/groups")).json()
        try:
            return [group["name"] for group in groups.values()]
        except (AttributeError, KeyError) as exc:
            print(exc)
        return None

    async def set_state(self, state):
        return (await http.put(f"{super().url}/groups/{self.id}/action", state)).json()

    async def get_state(self):
        groups = await http.get_json(f"{super().url}/groups")
        try:
            for group_id, group in groups.items():
                if group["name"] == self.name:
                    self.lights = [int(light_id) for light_id in group["lights"]]
                    self.on = group["action"]["on"]
                    self.id = group_id
                    self.brightness = group["action"]["bri"]
                    self.group_state = deepcopy(group)
                    return
            group_names = [repr(group["name"]) for group in groups.values()]
            print(
                f"unknown light group {repr(self.name)}, "
                f"known groups are: {', '.join(group_names)}"
            )
        except Exception as exc:
            print(exc)

    async def get_info(self):
        await self.get_state()
        return self.group_state

    async def power_on(self):
        await self.get_state()
        return await self.set_state({"on": True})

    async def power_off(self):
        await self.get_state()
        return await self.set_state({"on": False})

    async def toggle(self):
        await self.get_state()
        if self.on:
            return await self.power_off()
        else:
            return await self.power_on()

    async def set_brightness(self, brightness):
        await self.get_state()
        return await self.set_state({"bri": brightness})

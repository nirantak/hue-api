from __future__ import annotations

from typing import Any

from . import http
from .bridge import Bridge


class Light(Bridge):
    """
    Interact with the Hue Lights API

    Examples:
        >>> from hue import Light
        >>> light = Light(1, ip="192.168.1.10", user="xxxx")
        >>> print(light.url)
        http://192.168.1.10/api/xxxx/lights/1

    Attributes:
        id: ID of the Hue Light
        ip (str): IP address of the Hue Bridge
        user (str): The secret user id used to access the Hue API
        on: The last saved power state of the Light,
            saved by calling any light operation from the object
        state: The last saved Light state stored in the object
            saved by calling any light operation from the object
        saved_state: The Light state stored in the object by calling `save_state()`,
        info: The last saved Light information stored in the object by calling `get_info()`
    """

    def __init__(self: Light, id: int, *, ip: str, user: str) -> Light:
        """
        Initialize a Hue Light object

        Arguments:
            id: The ID (number) of the Light to control
            ip: IP address of the Hue Bridge, get it by running `hue bridge discover`
            user: The secret user id created to access the Hue API

        Returns:
            An object of class Light
        """
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
        """Returns the Hue Light URL"""
        return f"{super().url}/lights/{self.id}"

    async def get_info(self) -> dict[str, Any]:
        """
        List all the information about a Hue Light

        Returns:
            A dictionary of all the information about the Hue Light
        """
        self.info = await http.get_json(self.url)
        return self.info

    async def get_state(self) -> dict[str, Any]:
        """
        Get the current state of the Light

        Returns:
            A dictionary of the current state of the Hue Light
        """
        resp = await self.get_info()
        self.state = resp["state"]
        self.on = resp["state"]["on"]
        return self.state

    async def set_state(self, state: dict[str, Any]) -> list[dict[str, dict[str, Any]]]:
        """
        Set the state of the Light.
        See [this link](https://developers.meethue.com/develop/hue-api/lights-api/#set-light-state)
        for details

        Arguments:
            state: The state to set the light to, it may consist of the following keys:

                    "on":             bool,
                    "bri":            int,                # 1 to 254
                    "hue":            int,                # 0 to 65535
                    "sat":            int,                # 0 to 254
                    "xy":             list[float, float], # [0-1.0, 0-1.0]
                    "ct":             int,                # 153 to 500
                    "alert":          string,             # "none", "select", "lselect"
                    "effect":         string,             # "none", "colorloop"
                    "transitiontime": int,
                    "bri_inc":        int,                # -254 to 254
                    "sat_inc":        int,                # -254 to 254
                    "hue_inc":        int,                # -65534 to 65534
                    "ct_inc":         int,                # -65534 to 65534
                    "xy_inc":         list[float, float],

        Returns:
            A list of dictionaries with key=success/error and value=state element changed
        """
        data = {}
        for key in [
            "on",
            "bri",
            "hue",
            "sat",
            "xy",
            "ct",
            "alert",
            "effect",
            "transitiontime",
            "bri_inc",
            "sat_inc",
            "hue_inc",
            "ct_inc",
            "xy_inc",
        ]:
            value = state.get(key)
            if value is not None:
                data[key] = value
        resp = await http.put(f"{self.url}/state", data)
        await self.get_state()
        return resp.json()

    async def save_state(self) -> dict[str, Any]:
        """
        Save the current state of the Light in the object

        Returns:
            A dictionary of the current state of the Light that will be saved
        """
        self.saved_state = await self.get_state()
        return self.saved_state

    async def restore_state(self) -> list[dict[str, dict[str, Any]]]:
        """
        Restore the saved state (set by calling `save_state()`) of the Light

        Returns:
            A list of dictionaries with key=success/error and value=state element changed
        """
        resp = await self.set_state(self.saved_state)
        return resp

    async def power_on(self) -> list[dict[str, dict[str, Any]]]:
        """
        Power on the Light

        Returns:
            A list of dictionaries with key=success/error and value=state element changed
        """
        return await self.set_state({"on": True})

    async def power_off(self) -> list[dict[str, dict[str, Any]]]:
        """
        Power off the Light

        Returns:
            A list of dictionaries with key=success/error and value=state element changed
        """
        return await self.set_state({"on": False})

    async def toggle(self) -> list[dict[str, dict[str, Any]]]:
        """
        Toggle the power state of the Light

        Returns:
            A list of dictionaries with key=success/error and value=state element changed
        """
        await self.get_state()
        return await self.set_state({"on": not self.on})

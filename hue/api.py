import os
from typing import Any

import httpx

HUE_API: str = (
    f"http://{os.environ['HUE_BRIDGE_IP']}/api/{os.environ['HUE_BRIDGE_USER']}"
)
ORIGINAL_STATE: dict[Any] = {}


async def switch_on(light: int) -> bool:
    status, resp = await set_state(light, {"on": True})
    print(f"Light {light} ON resp: {resp}")
    return status


async def switch_off(light: int) -> bool:
    status, resp = await set_state(light, {"on": False})
    print(f"Light {light} OFF resp: {resp}")
    return status


async def get_light(light: int) -> dict[Any]:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{HUE_API}/lights/{light}")
        resp = resp.json()
        print(f"Light {light} resp: {resp}")
        return resp


async def get_state(light: int) -> dict[Any]:
    resp = await get_light(light)
    return resp["state"]


async def set_state(light: int, state: dict[Any]) -> tuple[bool, dict[Any]]:
    async with httpx.AsyncClient() as client:
        data = {"on": bool(state.get("on"))}
        for i in ["bri", "hue", "sat", "xy", "ct"]:
            if s := state.get(i):
                data[i] = s

        resp = await client.put(f"{HUE_API}/lights/{light}/state", json=data)
        print(f"Light {light} resp: {resp.text}")
        return (resp.status_code == httpx.codes.OK, resp.json())


async def save_state(light: int) -> dict[Any]:
    global ORIGINAL_STATE
    ORIGINAL_STATE = await get_state(light)
    return ORIGINAL_STATE


async def restore_state(light: int) -> dict[Any]:
    return await set_state(light, ORIGINAL_STATE)

from __future__ import annotations

from typing import Any

import httpx


async def get(url: str) -> httpx.Response:
    resp = None
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    return resp


async def get_json(url: str) -> dict[Any, Any]:
    resp = await get(url)
    return resp.json()


async def put(url: str, data: dict[Any, Any]) -> httpx.Response:
    resp = None
    async with httpx.AsyncClient() as client:
        resp = await client.put(url, json=data)
    return resp


async def post(url: str, data: dict[Any, Any]) -> httpx.Response:
    resp = None
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=data)
    return resp

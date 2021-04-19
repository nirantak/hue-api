# Hue API

> _Async API for controlling Hue Lights_

[![Python Tests](https://github.com/nirantak/hue-api/actions/workflows/python-test.yml/badge.svg)](https://github.com/nirantak/hue-api/actions/workflows/python-test.yml)
[![Publish Package](https://github.com/nirantak/hue-api/actions/workflows/python-publish.yml/badge.svg)](https://github.com/nirantak/hue-api/actions/workflows/python-publish.yml)
[![Package Version](https://img.shields.io/pypi/v/hue-api)](https://pypi.org/project/hue-api/)
![Package Status](https://img.shields.io/pypi/status/hue-api)
![Python Versions](https://img.shields.io/pypi/pyversions/hue-api)

## Installation

This is an async client for interacting with the Hue Bridge API, to control Hue Lights.

The minimum Python version required to run this is 3.7

Install the package using pip:

```shell
pip install hue-api
```

- Go to [discovery.meethue.com](https://discovery.meethue.com/) to get the Hue bridge IP address.
- Follow [this link](https://developers.meethue.com/develop/get-started-2/#so-lets-get-started) to create a Hue API user if not already known, and set the env variable `HUE_BRIDGE_USER` ([API reference](https://developers.meethue.com/develop/hue-api/7-configuration-api/#create-user)).

## Usage

```python
from hue import api

# Set the light id to control
light = 1

# from an async function
async def main():
  await api.switch_on(light)

# or from a sync context
import asyncio
asyncio.run(api.switch_on(light))
```

## Available methods

- `switch_on(light: int) -> bool`

  Turn `light` on

- `switch_off(light: int) -> bool`

  Turn `light` off

- `get_light(light: int) -> dict[Any]`

  Get all the information about `light`

- `get_state(light: int) -> dict[Any]`

  Get the current state of `light`

- `set_state(light: int, state: dict[Any]) -> tuple[bool, dict[Any]]`

  Set the state of `light`

  Input values of "bri", "hue", "sat", "xy", "ct" in `state`

  Returns the success value and the current state

- `save_state(light: int) -> dict[Any]`

  Save the current state of `light`

- `restore_state(light: int) -> dict[Any]`

  Restore the last saved state of `light`

## Changelog

See the file [CHANGELOG.md](CHANGELOG.md)

## License

This project is licensed under the terms of the [MIT license](LICENSE)

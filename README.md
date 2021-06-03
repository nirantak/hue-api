# Hue API

> _Async API for controlling Hue Lights_

[![Python Tests](https://github.com/nirantak/hue-api/actions/workflows/python-test.yml/badge.svg)](https://github.com/nirantak/hue-api/actions/workflows/python-test.yml)
[![Publish Package](https://github.com/nirantak/hue-api/actions/workflows/python-publish.yml/badge.svg)](https://github.com/nirantak/hue-api/actions/workflows/python-publish.yml)
[![Package Version](https://img.shields.io/pypi/v/hue-api)](https://pypi.org/project/hue-api/)
![Package Status](https://img.shields.io/pypi/status/hue-api)
![Python Versions](https://img.shields.io/pypi/pyversions/hue-api)

## Installation

This is an async client to interact with the Hue Bridge API.

The minimum Python version required to run this is 3.7

Install the package using pip:

```bash
pip install hue-api
hue version

# To find your Hue Bridge IP address go to discovery.meethue.com, or run:
hue bridge discover
```

## Usage

Follow [this link](https://developers.meethue.com/develop/get-started-2/#so-lets-get-started) to create a Hue API user if not already known ([API reference](https://developers.meethue.com/develop/hue-api/7-configuration-api/#create-user))

```python
from hue import Bridge, Light

# Create a light object with the light id (number), Bridge IP and user
light = Light(1, ip="your-hue-bridge-ip", user="hue-api-user")

# from an async function
async def main():
  await Bridge.discover()
  await light.power_on()

# or from a sync context
import asyncio
asyncio.run(Bridge.discover())
asyncio.run(light.power_on())
```

## Changelog

See the file [CHANGELOG.md](CHANGELOG.md)

## License

This project is licensed under the terms of the [MIT license](LICENSE)

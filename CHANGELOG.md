# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0).

## 0.3.1 (2021-04-20)

### Fixed

- Fix power state bug in `Light.restore_state()`
- Store latest light state in `Light.state` instead of `Light.current_state`

## 0.3.0 (2021-04-20)

### Added

- Use Class based API for Lights
- Add API for Hue Bridge, along with cli for Bridge IP discovery
- New color methods for conversion between formats
- Use flit for packaging

### Removed

- The API does not read environment variables for bridge config now

## 0.2.0 (2021-04-16)

### Added

- Add typer for cli
- Compatibility for Python 3.7+

## 0.1.1 (2021-04-15)

### Added

- Add documentation

### Fixed

- Fix minimum python version required 3.9
- Fix tox tests

## 0.1.0 (2021-04-15)

- First release

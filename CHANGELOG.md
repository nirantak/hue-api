# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0).

See all releases on [GitHub](https://github.com/nirantak/hue-api/releases) or [PyPI](https://pypi.org/project/hue-api/#history).

## [v0.4.3](https://github.com/nirantak/hue-api/releases/tag/v0.4.3) (2021-06-30)

### Added

- Update dependencies
- Add release links to changelog

## [v0.4.1](https://github.com/nirantak/hue-api/releases/tag/v0.4.1) (2021-06-22)

### Added

- Update dependencies
- Add mkdocs for documentation [hue-api.nirantak.com](https://hue-api.nirantak.com/)

## [v0.4.0](https://github.com/nirantak/hue-api/releases/tag/v0.4.0) (2021-06-14)

### Added

- More CLI commands for Hue API
- Update installed package versions
- Add test coverage
- Minimum Python version supported is now 3.8

## [v0.3.1](https://github.com/nirantak/hue-api/releases/tag/v0.3.1) (2021-04-20)

### Fixed

- Fix power state bug in `Light.restore_state()`
- Store latest light state in `Light.state` instead of `Light.current_state`

## [v0.3.0](https://github.com/nirantak/hue-api/releases/tag/v0.3.0) (2021-04-20)

### Added

- Use Class based API for Lights
- Add API for Hue Bridge, along with cli for Bridge IP discovery
- New color methods for conversion between formats
- Use flit for packaging

### Removed

- The API does not read environment variables for bridge config now

## [v0.2.0](https://github.com/nirantak/hue-api/releases/tag/v0.2.0) (2021-04-16)

### Added

- Add typer for cli
- Compatibility for Python 3.7+

## [v0.1.1](https://github.com/nirantak/hue-api/releases/tag/v0.1.1) (2021-04-15)

### Added

- Add documentation

### Fixed

- Fix minimum python version required 3.9
- Fix tox tests

## [v0.1.0](https://github.com/nirantak/hue-api/releases/tag/v0.1.0) (2021-04-15)

- First release

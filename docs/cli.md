# `hue`

**Usage**:

```console
$ hue [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `bridge`: Interact with the Hue Bridge API
* `light`: Interact with the Hue Lights API
* `version`: Show version of hue-api installed

## `hue bridge`

Interact with the Hue Bridge API

**Usage**:

```console
$ hue bridge [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `discover`: Discover online Bridges in the local network
* `get`: Get the config of a Bridge
* `info`: List all the information about a Hue Bridge

### `hue bridge discover`

Discover online Bridges in the local network

**Usage**:

```console
$ hue bridge discover [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `hue bridge get`

Get the config of a Bridge

**Usage**:

```console
$ hue bridge get [OPTIONS]
```

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

### `hue bridge info`

List all the information about a Hue Bridge

**Usage**:

```console
$ hue bridge info [OPTIONS]
```

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

## `hue light`

Interact with the Hue Lights API

**Usage**:

```console
$ hue light [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the state of a Light
* `info`: List all the information about a Hue Light
* `off`: Power off a light
* `on`: Power on a light
* `toggle`: Toggle the power state of a light

### `hue light get`

Get the state of a Light

**Usage**:

```console
$ hue light get [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: [default: 1]

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

### `hue light info`

List all the information about a Hue Light

**Usage**:

```console
$ hue light info [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: [default: 1]

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

### `hue light off`

Power off a light

**Usage**:

```console
$ hue light off [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: [default: 1]

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

### `hue light on`

Power on a light

**Usage**:

```console
$ hue light on [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: [default: 1]

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

### `hue light toggle`

Toggle the power state of a light

**Usage**:

```console
$ hue light toggle [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: [default: 1]

**Options**:

* `-i, --ip TEXT`: [env var: HUE_BRIDGE_IP; required]
* `-u, --user TEXT`: [env var: HUE_BRIDGE_USER; required]
* `--help`: Show this message and exit.

## `hue version`

Show version of hue-api installed

**Usage**:

```console
$ hue version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

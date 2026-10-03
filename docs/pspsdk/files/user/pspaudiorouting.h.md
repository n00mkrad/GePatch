[PSPSDK documentation](../../README.md) › Files

# user/pspaudiorouting.h

## Functions

### `sceAudioRoutingSetMode()`

```c
int sceAudioRoutingSetMode(int mode);
```

Set routing mode.

**Parameters:**

- `mode` – The routing mode to set (0 or 1)

**Returns:** the previous routing mode, or \< 0 on error

### `sceAudioRoutingGetMode()`

```c
int sceAudioRoutingGetMode(void);
```

Get routing mode.

**Returns:** the current routing mode.

### `sceAudioRoutingGetVolumeMode()`

```c
int sceAudioRoutingGetVolumeMode(void);
```

Get the current routing volume mode.

**Returns:** The current routing volume mode.

### `sceAudioRoutingSetVolumeMode()`

```c
int sceAudioRoutingSetVolumeMode(int vol_mode);
```

Set the routing volume mode.

**Parameters:**

- `vol_mode` – The routing volume to set (`0` or `1`).

**Returns:** `0` on success, `< 0` on error.

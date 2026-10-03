[PSPSDK documentation](../../README.md) › Files

# wlan/pspwlan.h

## Functions

### `sceWlanDevIsPowerOn()`

```c
int sceWlanDevIsPowerOn(void);
```

Determine if the wlan device is currently powered on.

**Returns:** 0 if off, 1 if on

### `sceWlanGetSwitchState()`

```c
int sceWlanGetSwitchState(void);
```

Determine the state of the Wlan power switch.

**Returns:** 0 if off, 1 if on

### `sceWlanGetEtherAddr()`

```c
int sceWlanGetEtherAddr(uint8_t *etherAddr);
```

Get the Ethernet Address of the wlan controller.

**Parameters:**

- `etherAddr` – pointer to a buffer of uint8_t (NOTE: it only writes to 6 bytes, but requests 8 so pass it 8 bytes just in case)

**Returns:** 0 on success, \< 0 on error

### `sceWlanDevAttach()`

```c
int sceWlanDevAttach(void);
```

Attach to the wlan device.

**Returns:** 0 on success, \< 0 on error.

### `sceWlanDevDetach()`

```c
int sceWlanDevDetach(void);
```

Detach from the wlan device.

**Returns:** 0 on success, \< 0 on error/

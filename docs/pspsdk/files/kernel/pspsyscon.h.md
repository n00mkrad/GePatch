[PSPSDK documentation](../../README.md) › Files

# kernel/pspsyscon.h

```c
#include <pspkerneltypes.h>
```

Topics: [Interface to the sceSyscon_driver library.](../../topics/Syscon.md)

## Macros

### `SCE_LED_POWER`

```c
#define SCE_LED_POWER 1
```

### `LED_ON`

```c
#define LED_ON 1
```

### `LED_OFF`

```c
#define LED_OFF 0
```

## Functions

### `sceSysconPowerStandby()`

```c
void sceSysconPowerStandby(void);
```

Force the PSP to go into standby.

### `sceSysconResetDevice()`

```c
void sceSysconResetDevice(int unk1, int unk2);
```

Reset the PSP.

**Parameters:**

- `unk1` – Unknown, pass 1.
- `unk2` – Unknown, pass 1.

### `sceSysconCtrlLED()`

```c
int sceSysconCtrlLED(int SceLED, int state);
```

Control an LED.

**Parameters:**

- `SceLED` – The led to toggle (only SCE_LED_POWER).
- `state` – Whether to turn on or off.

### `sceSysconCtrlHRPower()`

```c
int sceSysconCtrlHRPower(int power);
```

Control the remote control power.

**Parameters:**

- `power` – 1 is on, 0 is off.

**Returns:** \< 0 on error.

### `sceSysconGetHPConnect()`

```c
s8 sceSysconGetHPConnect(void);
```

Get the headphone connection status.

**Returns:** 1 if the headphone is connected, 0 if the headphone is disconnected.

### `sceSysconSetHPConnectCallback()`

```c
int sceSysconSetHPConnectCallback(void(*)(int), int unk0);
```

### `sceSysconSetHRPowerCallback()`

```c
int sceSysconSetHRPowerCallback(void(*)(int), int unk0);
```

### `sceSysconGetPommelVersion()`

```c
int sceSysconGetPommelVersion(int *version);
```

Get the PSP's Pommel version.

**Parameters:**

- `version` – A pointer to an int to receive the Pommel version into.

### `sceSysconGetBaryonVersion()`

```c
int sceSysconGetBaryonVersion(int *version);
```

Get the PSP's Baryon version.

**Parameters:**

- `version` – A pointer to an int to receive the Baryon version into.

### `sceSysconGetPolestarVersion()`

```c
int sceSysconGetPolestarVersion(int *version);
```

Get the PSP's Polestar version.

**Parameters:**

- `version` – A pointer to an int to receive the Polestar version into.

### `sceSysconGetTimeStamp()`

```c
int sceSysconGetTimeStamp(s8 *timeStamp);
```

Get the baryon timestamp string.

**Parameters:**

- `timeStamp` – A pointer to a string at least 12 bytes long.

### `sceSysconReceiveSetParam()`

```c
int sceSysconReceiveSetParam(int n, u8 *buf);
```

### `sceSysconCtrlUsbPower()`

```c
int sceSysconCtrlUsbPower(u8 power);
```

Controls power supply to the USB accessory port (PSP Cam, GPS, etc.).

**Parameters:**

- `power` – 1 to turn on, 0 to turn off

**Returns:** 0 if success, \< 0 otherwise

### `sceSysconGetUsbPowerCtrl()`

```c
u8 sceSysconGetUsbPowerCtrl(void);
```

Gets the power status of the USB accessory port (PSP Cam, GPS, etc.).

**Returns:** 1 if powered on, 0 otherwise

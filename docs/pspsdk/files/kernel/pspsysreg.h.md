[PSPSDK documentation](../../README.md) › Files

# kernel/pspsysreg.h

```c
#include <pspkerneltypes.h>
```

Topics: [Interface to the sceSysreg_driver library.](../../topics/Sysreg.md)

## Functions

### `sceSysregMeResetEnable()`

```c
int sceSysregMeResetEnable(void);
```

Enable the ME reset.

**Returns:** \< 0 on error.

### `sceSysregMeResetDisable()`

```c
int sceSysregMeResetDisable(void);
```

Disable the ME reset.

**Returns:** \< 0 on error.

### `sceSysregVmeResetEnable()`

```c
int sceSysregVmeResetEnable(void);
```

Enable the VME reset.

**Returns:** \< 0 on error.

### `sceSysregVmeResetDisable()`

```c
int sceSysregVmeResetDisable(void);
```

Disable the VME reset.

**Returns:** \< 0 on error.

### `sceSysregMeBusClockEnable()`

```c
int sceSysregMeBusClockEnable(void);
```

Enable the ME bus clock.

**Returns:** \< 0 on error.

### `sceSysregMeBusClockDisable()`

```c
int sceSysregMeBusClockDisable(void);
```

Disable the ME bus clock.

**Returns:** \< 0 on error.

### `sceSysregGetTachyonVersion()`

```c
int sceSysregGetTachyonVersion(void);
```

Get the PSP's Tachyon version.

### `sceSysregKirkBusClockEnable()`

```c
int sceSysregKirkBusClockEnable(void);
```

### `sceSysregAtaBusClockEnable()`

```c
int sceSysregAtaBusClockEnable(void);
```

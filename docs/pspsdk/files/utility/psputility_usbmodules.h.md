[PSPSDK documentation](../../README.md) › Files

# utility/psputility_usbmodules.h

```c
#include <psptypes.h>
```

## Macros

### `PSP_USB_MODULE_PSPCM`

```c
#define PSP_USB_MODULE_PSPCM 1
```

### `PSP_USB_MODULE_ACC`

```c
#define PSP_USB_MODULE_ACC 2
```

### `PSP_USB_MODULE_MIC`

```c
#define PSP_USB_MODULE_MIC 3
```

### `PSP_USB_MODULE_CAM`

```c
#define PSP_USB_MODULE_CAM 4
```

### `PSP_USB_MODULE_GPS`

```c
#define PSP_USB_MODULE_GPS 5
```

## Functions

### `sceUtilityLoadUsbModule()`

```c
int sceUtilityLoadUsbModule(int module);
```

Load a usb module (PRX) from user mode.

Available on firmware 2.70 and higher only.

**Parameters:**

- `module` – module number to load (PSP_USB_MODULE_xxx)

**Returns:** 0 on success, \< 0 on error

### `sceUtilityUnloadUsbModule()`

```c
int sceUtilityUnloadUsbModule(int module);
```

Unload a usb module (PRX) from user mode.

Available on firmware 2.70 and higher only.

**Parameters:**

- `module` – module number to be unloaded

**Returns:** 0 on success, \< 0 on error

[PSPSDK documentation](../../README.md) › Files

# usb/pspusb.h

## Macros

### `PSP_USBBUS_DRIVERNAME`

```c
#define PSP_USBBUS_DRIVERNAME "USBBusDriver"
```

### `PSP_USB_ACTIVATED`

```c
#define PSP_USB_ACTIVATED 0x200
```

### `PSP_USB_CABLE_CONNECTED`

```c
#define PSP_USB_CABLE_CONNECTED 0x020
```

### `PSP_USB_CONNECTION_ESTABLISHED`

```c
#define PSP_USB_CONNECTION_ESTABLISHED 0x002
```

## Functions

### `sceUsbStart()`

```c
int sceUsbStart(const char *driverName, int size, void *args);
```

Start a USB driver.

**Parameters:**

- `driverName` – name of the USB driver to start
- `size` – Size of arguments to pass to USB driver start
- `args` – Arguments to pass to USB driver start

**Returns:** 0 on success

### `sceUsbStop()`

```c
int sceUsbStop(const char *driverName, int size, void *args);
```

Stop a USB driver.

**Parameters:**

- `driverName` – name of the USB driver to stop
- `size` – Size of arguments to pass to USB driver stop
- `args` – Arguments to pass to USB driver stop

**Returns:** 0 on success

### `sceUsbActivate()`

```c
int sceUsbActivate(u32 pid);
```

Activate a USB driver.

**Parameters:**

- `pid` – Product ID for the default USB Driver

**Returns:** 0 on success

### `sceUsbDeactivate()`

```c
int sceUsbDeactivate(u32 pid);
```

Deactivate USB driver.

**Parameters:**

- `pid` – Product ID for the default USB driver

**Returns:** 0 on success

### `sceUsbGetState()`

```c
int sceUsbGetState(void);
```

Get USB state.

**Returns:** OR'd PSP_USB\_\* constants

### `sceUsbGetDrvState()`

```c
int sceUsbGetDrvState(const char *driverName);
```

Get state of a specific USB driver.

**Parameters:**

- `driverName` – name of USB driver to get status from

**Returns:** 1 if the driver has been started, 2 if it is stopped

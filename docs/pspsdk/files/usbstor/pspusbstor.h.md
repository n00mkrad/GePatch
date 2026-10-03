[PSPSDK documentation](../../README.md) › Files

# usbstor/pspusbstor.h

## Macros

### `PSP_USBSTOR_DRIVERNAME`

```c
#define PSP_USBSTOR_DRIVERNAME "USBStor_Driver"
```

## Functions

### `sceUsbstorBootRegisterNotify()`

```c
int sceUsbstorBootRegisterNotify(u32 eventFlag);
```

Register an eventFlag to send notifications to.

**Parameters:**

- `eventFlag` – eventFlag created with sceKernelCreateEventFlag

**Returns:** 0 on success

### `sceUsbstorBootUnregisterNotify()`

```c
int sceUsbstorBootUnregisterNotify(u32 eventFlag);
```

Unregister a previously registered eventFlag.

**Parameters:**

- `eventFlag` – eventFlag created with sceKernelCreateEventFlag

**Returns:** 0 on success

### `sceUsbstorBootSetCapacity()`

```c
int sceUsbstorBootSetCapacity(u32 size);
```

Tell the USBstorBoot driver the size of MS.

**Note:** I'm not sure if this is the actual size of the media or not as it seems to have no bearing on what size windows detects. PSPPET passes 0x800000

**Parameters:**

- `size` – capacity of memory stick

**Returns:** 0 on success

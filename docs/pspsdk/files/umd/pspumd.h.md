[PSPSDK documentation](../../README.md) › Files

# umd/pspumd.h

Topics: [UMD Kernel Library](../../topics/UMD.md)

## Data Structures

### `struct pspUmdInfo`

UMD Info struct.

| Field | Description |
|---|---|
| `unsigned int size` | Set to sizeof(pspUmdInfo) |
| `unsigned int type` | One or more of [pspUmdTypes](#enum-pspumdtypes). |

## Typedefs

### `pspUmdInfo`

```c
typedef struct pspUmdInfo pspUmdInfo;
```

UMD Info struct.

### `UmdCallback`

```c
typedef int(* UmdCallback) (int unknown, int event))(int unknown, int event);
```

UMD Callback function.

## Enumerations

### `enum pspUmdTypes`

Enumeration for UMD types.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UMD_TYPE_GAME` | `0x10` |  |
| `PSP_UMD_TYPE_VIDEO` | `0x20` |  |
| `PSP_UMD_TYPE_AUDIO` | `0x40` |  |

### `enum pspUmdState`

Enumeration for UMD drive state.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UMD_NOT_PRESENT` | `0x01` |  |
| `PSP_UMD_PRESENT` | `0x02` |  |
| `PSP_UMD_CHANGED` | `0x04` |  |
| `PSP_UMD_INITING` | `0x08` |  |
| `PSP_UMD_INITED` | `0x10` |  |
| `PSP_UMD_READY` | `0x20` |  |

### `enum UmdDriveStat`

Enumeration for UMD stats (legacy)

| Enumerator | Value | Description |
|---|---|---|
| `UMD_WAITFORDISC` | `PSP_UMD_PRESENT` | Wait for disc to be inserted. |
| `UMD_WAITFORINIT` | `PSP_UMD_READY` | Wait for the UMD to be initialised so it can be accessed from the mapped drive. |

## Functions

### `sceUmdCheckMedium()`

```c
int sceUmdCheckMedium(void);
```

Check whether there is a disc in the UMD drive.

**Returns:** 0 if no disc present, anything else indicates a disc is inserted.

### `sceUmdGetDiscInfo()`

```c
int sceUmdGetDiscInfo(pspUmdInfo *info);
```

Get the disc info.

**Parameters:**

- `info` – A pointer to a [pspUmdInfo](#struct-pspumdinfo) struct

**Returns:** \< 0 on error

### `sceUmdActivate()`

```c
int sceUmdActivate(int unit, const char *drive);
```

Activates the UMD drive.

**Parameters:**

- `unit` – The unit to initialise (probably). Should be set to 1.
- `drive` – A prefix string for the fs device to mount the UMD on (e.g. "disc0:")

**Returns:** \< 0 on error

**Example::**

```c
// Wait for disc and mount to filesystem
int i;
i = sceUmdCheckMedium();
if(i == 0)
{
   sceUmdWaitDriveStat(PSP_UMD_PRESENT);
}
sceUmdActivate(1, "disc0:"); // Mount UMD to disc0: file system
sceUmdWaitDriveStat(PSP_UMD_READY);
// Now you can access the UMD using standard sceIo functions
```

### `sceUmdDeactivate()`

```c
int sceUmdDeactivate(int unit, const char *drive);
```

Deativates the UMD drive.

**Parameters:**

- `unit` – The unit to initialise (probably). Should be set to 1.
- `drive` – A prefix string for the fs device to mount the UMD on (e.g. "disc0:")

**Returns:** \< 0 on error

### `sceUmdWaitDriveStat()`

```c
int sceUmdWaitDriveStat(int stat);
```

Wait for the UMD drive to reach a certain state.

**Parameters:**

- `stat` – One or more of [pspUmdState](#enum-pspumdstate)

**Returns:** \< 0 on error

### `sceUmdWaitDriveStatWithTimer()`

```c
int sceUmdWaitDriveStatWithTimer(int stat, unsigned int timeout);
```

Wait for the UMD drive to reach a certain state.

**Parameters:**

- `stat` – One or more of [pspUmdState](#enum-pspumdstate)
- `timeout` – Timeout value in microseconds

**Returns:** \< 0 on error

### `sceUmdWaitDriveStatCB()`

```c
int sceUmdWaitDriveStatCB(int stat, unsigned int timeout);
```

Wait for the UMD drive to reach a certain state (plus callback)

**Parameters:**

- `stat` – One or more of [pspUmdState](#enum-pspumdstate)
- `timeout` – Timeout value in microseconds

**Returns:** \< 0 on error

### `sceUmdCancelWaitDriveStat()`

```c
int sceUmdCancelWaitDriveStat(void);
```

Cancel a sceUmdWait\* call.

**Returns:** \< 0 on error

### `sceUmdGetDriveStat()`

```c
int sceUmdGetDriveStat(void);
```

Get (poll) the current state of the UMD drive.

**Returns:** \< 0 on error, one or more of [pspUmdState](#enum-pspumdstate) on success

### `sceUmdSetDriveStatus()`

```c
void sceUmdSetDriveStatus(int status);
```

Sets the current state of the UMD drive.

**Parameters:**

- `status` – The UMD state to set. One or more of [pspUmdState](#enum-pspumdstate).

### `sceUmdGetErrorStat()`

```c
int sceUmdGetErrorStat(void);
```

Get the error code associated with a failed event.

**Returns:** \< 0 on error, the error code on success

### `sceUmdRegisterUMDCallBack()`

```c
int sceUmdRegisterUMDCallBack(int cbid);
```

Register a callback for the UMD drive.

**Note:** Callback is of type UmdCallback

**Parameters:**

- `cbid` – A callback ID created from sceKernelCreateCallback

**Returns:** \< 0 on error

**Example::**

```c
int umd_callback(int unknown, int event)
{
     //do something
}     
int cbid = sceKernelCreateCallback("UMD Callback", umd_callback, NULL);
sceUmdRegisterUMDCallBack(cbid);
```

### `sceUmdUnRegisterUMDCallBack()`

```c
int sceUmdUnRegisterUMDCallBack(int cbid);
```

Un-register a callback for the UMD drive.

**Parameters:**

- `cbid` – A callback ID created from sceKernelCreateCallback

**Returns:** \< 0 on error

### `sceUmdReplacePermit()`

```c
int sceUmdReplacePermit(void);
```

Permit UMD disc being replaced.

**Returns:** \< 0 on error

### `sceUmdReplaceProhibit()`

```c
int sceUmdReplaceProhibit(void);
```

Prohibit UMD disc being replaced.

**Returns:** \< 0 on error

[PSPSDK documentation](../../README.md) › Files

# utility/psputility_netconf.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct pspUtilityNetconfAdhoc`

```c
struct pspUtilityNetconfAdhoc {
    unsigned char name[8];
    unsigned int timeout;
};
```

### `struct _pspUtilityNetconfData`

| Field | Description |
|---|---|
| `pspUtilityDialogCommon base` |  |
| `int action` |  |
| `struct pspUtilityNetconfAdhoc * adhocparam` | One of pspUtilityNetconfActions. |
| `int hotspot` |  |
| `int hotspot_connected` | Set to 1 to allow connections with the 'Internet Browser' option set to 'Start' (ie.<br>hotspot connection) |
| `int wifisp` | Will be set to 1 when connected to a hotspot style connection. |

## Typedefs

### `pspUtilityNetconfData`

```c
typedef struct _pspUtilityNetconfData pspUtilityNetconfData;
```

## Enumerations

### `enum pspUtilityNetconfActions`

| Enumerator | Description |
|---|---|
| `PSP_NETCONF_ACTION_CONNECTAP` |  |
| `PSP_NETCONF_ACTION_DISPLAYSTATUS` |  |
| `PSP_NETCONF_ACTION_CONNECT_ADHOC` |  |

## Functions

### `sceUtilityNetconfInitStart()`

```c
int sceUtilityNetconfInitStart(pspUtilityNetconfData *data);
```

Init the Network Configuration Dialog Utility.

**Parameters:**

- `data` – pointer to pspUtilityNetconfData to be initialized

**Returns:** 0 on success, \< 0 on error

### `sceUtilityNetconfShutdownStart()`

```c
int sceUtilityNetconfShutdownStart(void);
```

Shutdown the Network Configuration Dialog Utility.

**Returns:** 0 on success, \< 0 on error

### `sceUtilityNetconfUpdate()`

```c
int sceUtilityNetconfUpdate(int unknown);
```

Update the Network Configuration Dialog GUI.

**Parameters:**

- `unknown` – unknown; set to 1

**Returns:** 0 on success, \< 0 on error

### `sceUtilityNetconfGetStatus()`

```c
int sceUtilityNetconfGetStatus(void);
```

Get the status of a running Network Configuration Dialog.

**Returns:** one of pspUtilityDialogState on success, \< 0 on error

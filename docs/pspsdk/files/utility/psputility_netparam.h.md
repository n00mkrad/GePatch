[PSPSDK documentation](../../README.md) › Files

# utility/psputility_netparam.h

```c
#include <psptypes.h>
```

## Data Structures

### `union netData`

Datatype for sceUtilityGetNetParam since it can return a u32 or a string we use a union to avoid ugly casting.

```c
union netData {
    u32 asUint;
    char asString[128];
};
```

## Macros

### `PSP_NETPARAM_NAME`

```c
#define PSP_NETPARAM_NAME 0
```

### `PSP_NETPARAM_SSID`

```c
#define PSP_NETPARAM_SSID 1
```

### `PSP_NETPARAM_SECURE`

```c
#define PSP_NETPARAM_SECURE 2
```

### `PSP_NETPARAM_WEPKEY`

```c
#define PSP_NETPARAM_WEPKEY 3
```

### `PSP_NETPARAM_IS_STATIC_IP`

```c
#define PSP_NETPARAM_IS_STATIC_IP 4
```

### `PSP_NETPARAM_IP`

```c
#define PSP_NETPARAM_IP 5
```

### `PSP_NETPARAM_NETMASK`

```c
#define PSP_NETPARAM_NETMASK 6
```

### `PSP_NETPARAM_ROUTE`

```c
#define PSP_NETPARAM_ROUTE 7
```

### `PSP_NETPARAM_MANUAL_DNS`

```c
#define PSP_NETPARAM_MANUAL_DNS 8
```

### `PSP_NETPARAM_PRIMARYDNS`

```c
#define PSP_NETPARAM_PRIMARYDNS 9
```

### `PSP_NETPARAM_SECONDARYDNS`

```c
#define PSP_NETPARAM_SECONDARYDNS 10
```

### `PSP_NETPARAM_PROXY_USER`

```c
#define PSP_NETPARAM_PROXY_USER 11
```

### `PSP_NETPARAM_PROXY_PASS`

```c
#define PSP_NETPARAM_PROXY_PASS 12
```

### `PSP_NETPARAM_USE_PROXY`

```c
#define PSP_NETPARAM_USE_PROXY 13
```

### `PSP_NETPARAM_PROXY_SERVER`

```c
#define PSP_NETPARAM_PROXY_SERVER 14
```

### `PSP_NETPARAM_PROXY_PORT`

```c
#define PSP_NETPARAM_PROXY_PORT 15
```

### `PSP_NETPARAM_UNKNOWN1`

```c
#define PSP_NETPARAM_UNKNOWN1 16
```

### `PSP_NETPARAM_UNKNOWN2`

```c
#define PSP_NETPARAM_UNKNOWN2 17
```

### `PSP_NETPARAM_ERROR_BAD_NETCONF`

```c
#define PSP_NETPARAM_ERROR_BAD_NETCONF 0x80110601
```

### `PSP_NETPARAM_ERROR_BAD_PARAM`

```c
#define PSP_NETPARAM_ERROR_BAD_PARAM 0x80110604
```

## Functions

### `sceUtilityCheckNetParam()`

```c
int sceUtilityCheckNetParam(int id);
```

Check existance of a Net Configuration.

**Parameters:**

- `id` – id of net Configuration (1 to n)

**Returns:** 0 on success,

### `sceUtilityGetNetParam()`

```c
int sceUtilityGetNetParam(int conf, int param, netData *data);
```

Get Net Configuration Parameter.

**Parameters:**

- `conf` – Net Configuration number (1 to n) (0 returns valid but seems to be a copy of the last config requested)
- `param` – which parameter to get
- `data` – parameter data

**Returns:** 0 on success,

### `sceUtilityCreateNetParam()`

```c
int sceUtilityCreateNetParam(int conf);
```

Create a new Network Configuration.

**Note:** This creates a new configuration at conf and clears 0

**Parameters:**

- `conf` – Net Configuration number (1 to n)

**Returns:** 0 on success

### `sceUtilitySetNetParam()`

```c
int sceUtilitySetNetParam(int param, const void *val);
```

Sets a network parameter.

**Note:** This sets only to configuration 0

**Parameters:**

- `param` – Which parameter to set
- `val` – Pointer to the the data to set

**Returns:** 0 on success

### `sceUtilityCopyNetParam()`

```c
int sceUtilityCopyNetParam(int src, int dest);
```

Copies a Network Configuration to another.

**Parameters:**

- `src` – Source Net Configuration number (0 to n)
- `dest` – Destination Net Configuration number (0 to n)

**Returns:** 0 on success

### `sceUtilityDeleteNetParam()`

```c
int sceUtilityDeleteNetParam(int conf);
```

Deletes a Network Configuration.

**Parameters:**

- `conf` – Net Configuration number (1 to n)

**Returns:** 0 on success

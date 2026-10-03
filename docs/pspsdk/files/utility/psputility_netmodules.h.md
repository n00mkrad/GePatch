[PSPSDK documentation](../../README.md) › Files

# utility/psputility_netmodules.h

```c
#include <psptypes.h>
```

## Macros

### `PSP_NET_MODULE_COMMON`

```c
#define PSP_NET_MODULE_COMMON 1
```

### `PSP_NET_MODULE_ADHOC`

```c
#define PSP_NET_MODULE_ADHOC 2
```

### `PSP_NET_MODULE_INET`

```c
#define PSP_NET_MODULE_INET 3
```

### `PSP_NET_MODULE_PARSEURI`

```c
#define PSP_NET_MODULE_PARSEURI 4
```

### `PSP_NET_MODULE_PARSEHTTP`

```c
#define PSP_NET_MODULE_PARSEHTTP 5
```

### `PSP_NET_MODULE_HTTP`

```c
#define PSP_NET_MODULE_HTTP 6
```

### `PSP_NET_MODULE_SSL`

```c
#define PSP_NET_MODULE_SSL 7
```

### `SCE_ERROR_NET_MODULE_NOT_LOADED`

```c
#define SCE_ERROR_NET_MODULE_NOT_LOADED (0x80110803)
```

An error code used as a return value.

## Functions

### `sceUtilityLoadNetModule()`

```c
int sceUtilityLoadNetModule(int module);
```

Load a network module (PRX) from user mode.

Load PSP_NET_MODULE_COMMON and PSP_NET_MODULE_INET to use infrastructure WifI (via an access point). Available on firmware 2.00 and higher only.

**Parameters:**

- `module` – module number to load (PSP_NET_MODULE_xxx)

**Returns:** 0 on success, \< 0 on error

### `sceUtilityUnloadNetModule()`

```c
int sceUtilityUnloadNetModule(int module);
```

Unload a network module (PRX) from user mode.

Available on firmware 2.00 and higher only.

**Parameters:**

- `module` – module number be unloaded

**Returns:** 0 on success, \< 0 on error

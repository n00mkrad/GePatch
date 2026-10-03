[PSPSDK documentation](../../README.md) › Files

# registry/pspreg.h

```c
#include <psptypes.h>
```

Topics: [Registry Kernel Library](../../topics/Reg.md)

## Data Structures

### `struct RegParam`

Struct used to open a registry.

| Field | Description |
|---|---|
| `unsigned int regtype` |  |
| `char name[256]` | Seemingly never used, set to [SYSTEM_REGISTRY](#system_registry). |
| `unsigned int namelen` | Length of the name. |
| `unsigned int unk2` | Unknown, set to 1. |
| `unsigned int unk3` | Unknown, set to 1. |

## Macros

### `SYSTEM_REGISTRY`

```c
#define SYSTEM_REGISTRY "/system"
```

System registry path.

### `REG_KEYNAME_SIZE`

```c
#define REG_KEYNAME_SIZE 27
```

Size of a keyname, used in [sceRegGetKeys](#scereggetkeys).

## Typedefs

### `REGHANDLE`

```c
typedef unsigned int REGHANDLE;
```

Typedef for a registry handle.

## Enumerations

### `enum RegKeyTypes`

Key types.

| Enumerator | Value | Description |
|---|---|---|
| `REG_TYPE_DIR` | `1` | Key is a directory. |
| `REG_TYPE_INT` | `2` | Key is an integer (4 bytes) |
| `REG_TYPE_STR` | `3` | Key is a string. |
| `REG_TYPE_BIN` | `4` | Key is a binary string. |

## Functions

### `sceRegOpenRegistry()`

```c
int sceRegOpenRegistry(struct RegParam *reg, int mode, REGHANDLE *h);
```

Open the registry.

**Parameters:**

- `reg` – A filled in [RegParam](#struct-regparam) structure
- `mode` – Open mode (set to 1)
- `h` – Pointer to a REGHANDLE to receive the registry handle

**Returns:** 0 on success, \< 0 on error

### `sceRegFlushRegistry()`

```c
int sceRegFlushRegistry(REGHANDLE h);
```

Flush the registry to disk.

**Parameters:**

- `h` – The open registry handle

**Returns:** 0 on success, \< 0 on error

### `sceRegCloseRegistry()`

```c
int sceRegCloseRegistry(REGHANDLE h);
```

Close the registry.

**Parameters:**

- `h` – The open registry handle

**Returns:** 0 on success, \< 0 on error

### `sceRegOpenCategory()`

```c
int sceRegOpenCategory(REGHANDLE h, const char *name, int mode, REGHANDLE *hd);
```

Open a registry directory.

**Parameters:**

- `h` – The open registry handle
- `name` – The path to the dir to open (e.g. /CONFIG/SYSTEM)
- `mode` – Open mode (can be 1 or 2, probably read or read/write
- `hd` – Pointer to a REGHANDLE to receive the registry dir handle

**Returns:** 0 on success, \< 0 on error

### `sceRegRemoveCategory()`

```c
int sceRegRemoveCategory(REGHANDLE h, const char *name);
```

Remove a registry dir.

**Parameters:**

- `h` – The open registry dir handle
- `name` – The name of the key

**Returns:** 0 on success, \< 0 on error

### `sceRegCloseCategory()`

```c
int sceRegCloseCategory(REGHANDLE hd);
```

Close the registry directory.

**Parameters:**

- `hd` – The open registry dir handle

**Returns:** 0 on success, \< 0 on error

### `sceRegFlushCategory()`

```c
int sceRegFlushCategory(REGHANDLE hd);
```

Flush the registry directory to disk.

**Parameters:**

- `hd` – The open registry dir handle

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeyInfo()`

```c
int sceRegGetKeyInfo(REGHANDLE hd, const char *name, REGHANDLE *hk, unsigned int *type, SceSize *size);
```

Get a key's information.

**Parameters:**

- `hd` – The open registry dir handle
- `name` – Name of the key
- `hk` – Pointer to a REGHANDLE to get registry key handle
- `type` – Type of the key, on of [RegKeyTypes](#enum-regkeytypes)
- `size` – The size of the key's value in bytes

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeyInfoByName()`

```c
int sceRegGetKeyInfoByName(REGHANDLE hd, const char *name, unsigned int *type, SceSize *size);
```

Get a key's information by name.

**Parameters:**

- `hd` – The open registry dir handle
- `name` – Name of the key
- `type` – Type of the key, on of [RegKeyTypes](#enum-regkeytypes)
- `size` – The size of the key's value in bytes

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeyValue()`

```c
int sceRegGetKeyValue(REGHANDLE hd, REGHANDLE hk, void *buf, SceSize size);
```

Get a key's value.

**Parameters:**

- `hd` – The open registry dir handle
- `hk` – The open registry key handler (from [sceRegGetKeyInfo](#scereggetkeyinfo))
- `buf` – Buffer to hold the value
- `size` – The size of the buffer

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeyValueByName()`

```c
int sceRegGetKeyValueByName(REGHANDLE hd, const char *name, void *buf, SceSize size);
```

Get a key's value by name.

**Parameters:**

- `hd` – The open registry dir handle
- `name` – The key name
- `buf` – Buffer to hold the value
- `size` – The size of the buffer

**Returns:** 0 on success, \< 0 on error

### `sceRegSetKeyValue()`

```c
int sceRegSetKeyValue(REGHANDLE hd, const char *name, const void *buf, SceSize size);
```

Set a key's value.

**Parameters:**

- `hd` – The open registry dir handle
- `name` – The key name
- `buf` – Buffer to hold the value
- `size` – The size of the buffer

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeysNum()`

```c
int sceRegGetKeysNum(REGHANDLE hd, int *num);
```

Get number of subkeys in the current dir.

**Parameters:**

- `hd` – The open registry dir handle
- `num` – Pointer to an integer to receive the number

**Returns:** 0 on success, \< 0 on error

### `sceRegGetKeys()`

```c
int sceRegGetKeys(REGHANDLE hd, char *buf, int num);
```

Get the key names in the current directory.

**Parameters:**

- `hd` – The open registry dir handle
- `buf` – Buffer to hold the NUL terminated strings, should be num\*REG_KEYNAME_SIZE
- `num` – Number of elements in buf

**Returns:** 0 on success, \< 0 on error

### `sceRegCreateKey()`

```c
int sceRegCreateKey(REGHANDLE hd, const char *name, int type, SceSize size);
```

Create a key.

**Parameters:**

- `hd` – The open registry dir handle
- `name` – Name of the key to create
- `type` – Type of key (note cannot be a directory type)
- `size` – Size of the allocated value space

**Returns:** 0 on success, \< 0 on error

### `sceRegRemoveRegistry()`

```c
int sceRegRemoveRegistry(struct RegParam *reg);
```

Remove a registry (HONESTLY, DO NOT USE)

**Parameters:**

- `reg` – Filled out registry parameter

**Returns:** 0 on success, \< 0 on error

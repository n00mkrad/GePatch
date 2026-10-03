[PSPSDK documentation](../../README.md) › Files

# utility/psputility_avmodules.h

```c
#include <psptypes.h>
```

## Macros

### `PSP_AV_MODULE_AVCODEC`

```c
#define PSP_AV_MODULE_AVCODEC 0
```

### `PSP_AV_MODULE_SASCORE`

```c
#define PSP_AV_MODULE_SASCORE 1
```

### `PSP_AV_MODULE_ATRAC3PLUS`

```c
#define PSP_AV_MODULE_ATRAC3PLUS 2
```

### `PSP_AV_MODULE_MPEGBASE`

```c
#define PSP_AV_MODULE_MPEGBASE 3
```

### `PSP_AV_MODULE_MP3`

```c
#define PSP_AV_MODULE_MP3 4
```

### `PSP_AV_MODULE_VAUDIO`

```c
#define PSP_AV_MODULE_VAUDIO 5
```

### `PSP_AV_MODULE_AAC`

```c
#define PSP_AV_MODULE_AAC 6
```

### `PSP_AV_MODULE_G729`

```c
#define PSP_AV_MODULE_G729 7
```

## Functions

### `sceUtilityLoadAvModule()`

```c
int sceUtilityLoadAvModule(int module);
```

Load an audio/video module (PRX) from user mode.

Available on firmware 2.00 and higher only.

**Parameters:**

- `module` – module number to load (PSP_AV_MODULE_xxx)

**Returns:** 0 on success, \< 0 on error

### `sceUtilityUnloadAvModule()`

```c
int sceUtilityUnloadAvModule(int module);
```

Unload an audio/video module (PRX) from user mode.

Available on firmware 2.00 and higher only.

**Parameters:**

- `module` – module number to be unloaded

**Returns:** 0 on success, \< 0 on error

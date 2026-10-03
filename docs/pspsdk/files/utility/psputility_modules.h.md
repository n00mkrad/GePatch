[PSPSDK documentation](../../README.md) › Files

# utility/psputility_modules.h

```c
#include <psptypes.h>
```

## Macros

### `PSP_MODULE_NET_COMMON`

```c
#define PSP_MODULE_NET_COMMON 0x0100
```

### `PSP_MODULE_NET_ADHOC`

```c
#define PSP_MODULE_NET_ADHOC 0x0101
```

### `PSP_MODULE_NET_INET`

```c
#define PSP_MODULE_NET_INET 0x0102
```

### `PSP_MODULE_NET_PARSEURI`

```c
#define PSP_MODULE_NET_PARSEURI 0x0103
```

### `PSP_MODULE_NET_PARSEHTTP`

```c
#define PSP_MODULE_NET_PARSEHTTP 0x0104
```

### `PSP_MODULE_NET_HTTP`

```c
#define PSP_MODULE_NET_HTTP 0x0105
```

### `PSP_MODULE_NET_SSL`

```c
#define PSP_MODULE_NET_SSL 0x0106
```

### `PSP_MODULE_USB_PSPCM`

```c
#define PSP_MODULE_USB_PSPCM 0x0200
```

### `PSP_MODULE_USB_MIC`

```c
#define PSP_MODULE_USB_MIC 0x0201
```

### `PSP_MODULE_USB_CAM`

```c
#define PSP_MODULE_USB_CAM 0x0202
```

### `PSP_MODULE_USB_GPS`

```c
#define PSP_MODULE_USB_GPS 0x0203
```

### `PSP_MODULE_AV_AVCODEC`

```c
#define PSP_MODULE_AV_AVCODEC 0x0300
```

### `PSP_MODULE_AV_SASCORE`

```c
#define PSP_MODULE_AV_SASCORE 0x0301
```

### `PSP_MODULE_AV_ATRAC3PLUS`

```c
#define PSP_MODULE_AV_ATRAC3PLUS 0x0302
```

### `PSP_MODULE_AV_MPEGBASE`

```c
#define PSP_MODULE_AV_MPEGBASE 0x0303
```

### `PSP_MODULE_AV_MP3`

```c
#define PSP_MODULE_AV_MP3 0x0304
```

### `PSP_MODULE_AV_VAUDIO`

```c
#define PSP_MODULE_AV_VAUDIO 0x0305
```

### `PSP_MODULE_AV_AAC`

```c
#define PSP_MODULE_AV_AAC 0x0306
```

### `PSP_MODULE_AV_G729`

```c
#define PSP_MODULE_AV_G729 0x0307
```

### `PSP_MODULE_NP_COMMON`

```c
#define PSP_MODULE_NP_COMMON 0x0400
```

### `PSP_MODULE_NP_SERVICE`

```c
#define PSP_MODULE_NP_SERVICE 0x0401
```

### `PSP_MODULE_NP_MATCHING2`

```c
#define PSP_MODULE_NP_MATCHING2 0x0402
```

### `PSP_MODULE_NP_DRM`

```c
#define PSP_MODULE_NP_DRM 0x0500
```

### `PSP_MODULE_IRDA`

```c
#define PSP_MODULE_IRDA 0x0600
```

### `SCE_ERROR_MODULE_ALREADY_LOADED`

```c
#define SCE_ERROR_MODULE_ALREADY_LOADED (0x80111102)
```

An error code used as a return value.

## Functions

### `sceUtilityLoadModule()`

```c
int sceUtilityLoadModule(int module);
```

Load a module (PRX) from user mode.

**Parameters:**

- `module` – module to load (PSP_MODULE_xxx)

**Returns:** 0 on success, \< 0 on error

### `sceUtilityUnloadModule()`

```c
int sceUtilityUnloadModule(int module);
```

Unload a module (PRX) from user mode.

**Parameters:**

- `module` – module to unload (PSP_MODULE_xxx)

**Returns:** 0 on success, \< 0 on error

[PSPSDK documentation](../../README.md) › Files

# user/pspmodulemgr.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
```

Topics: [Module Manager Library](../../topics/ModuleMgr.md)

## Data Structures

### `struct SceKernelLMOption`

```c
struct SceKernelLMOption {
    SceSize size;
    SceUID mpidtext;
    SceUID mpiddata;
    unsigned int flags;
    char position;
    char access;
    char creserved[2];
};
```

### `struct SceKernelSMOption`

```c
struct SceKernelSMOption {
    SceSize size;
    SceUID mpidstack;
    SceSize stacksize;
    int priority;
    unsigned int attribute;
};
```

### `struct SceKernelModuleInfo`

```c
struct SceKernelModuleInfo {
    SceSize size;
    char nsegment;
    char reserved[3];
    int segmentaddr[4];
    int segmentsize[4];
    unsigned int entry_addr;
    unsigned int gp_value;
    unsigned int text_addr;
    unsigned int text_size;
    unsigned int data_size;
    unsigned int bss_size;
    unsigned short attribute;
    unsigned char version[2];
    char name[28];
};
```

## Macros

### `PSP_MEMORY_PARTITION_KERNEL`

```c
#define PSP_MEMORY_PARTITION_KERNEL 1
```

### `PSP_MEMORY_PARTITION_USER`

```c
#define PSP_MEMORY_PARTITION_USER 2
```

### `SCE_SECURE_INSTALL_ID_LEN`

```c
#define SCE_SECURE_INSTALL_ID_LEN (16)
```

## Typedefs

### `SceKernelLMOption`

```c
typedef struct SceKernelLMOption SceKernelLMOption;
```

### `SceKernelSMOption`

```c
typedef struct SceKernelSMOption SceKernelSMOption;
```

### `SceKernelModuleInfo`

```c
typedef struct SceKernelModuleInfo SceKernelModuleInfo;
```

## Functions

### `sceKernelLoadModule()`

```c
SceUID sceKernelLoadModule(const char *path, int flags, SceKernelLMOption *option);
```

Load a module.

**Note:** This function restricts where it can load from (such as from flash0) unless you call it in kernel mode. It also must be called from a thread.

**Parameters:**

- `path` – The path to the module to load.
- `flags` – Unused, always 0 .
- `option` – Pointer to a mod_param_t structure. Can be NULL.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelLoadModuleMs()`

```c
SceUID sceKernelLoadModuleMs(const char *path, int flags, SceKernelLMOption *option);
```

Load a module from MS.

**Note:** This function restricts what it can load, e.g. it wont load plain executables.

**Parameters:**

- `path` – The path to the module to load.
- `flags` – Unused, set to 0.
- `option` – Pointer to a mod_param_t structure. Can be NULL.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelLoadModuleMs2()`

```c
SceUID sceKernelLoadModuleMs2(int apitype, const char *path, int flags, SceKernelLMOption *option);
```

Alias for `sceKernelLoadModuleForLoadExecVSHMs2`

**Attention:** Needs to link to `pspmodulemgr_kernel` stub.

### `sceKernelLoadModuleByID()`

```c
SceUID sceKernelLoadModuleByID(SceUID fid, int flags, SceKernelLMOption *option);
```

Load a module from the given file UID.

**Parameters:**

- `fid` – The module's file UID.
- `flags` – Unused, always 0.
- `option` – Pointer to an optional [SceKernelLMOption](#struct-scekernellmoption) structure.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelLoadModuleBufferUsbWlan()`

```c
SceUID sceKernelLoadModuleBufferUsbWlan(SceSize bufsize, void *buf, int flags, SceKernelLMOption *option);
```

Load a module from a buffer using the USB/WLAN API.

Can only be called from kernel mode, or from a thread that has attributes of 0xa0000000.

**Parameters:**

- `bufsize` – Size (in bytes) of the buffer pointed to by buf.
- `buf` – Pointer to a buffer containing the module to load. The buffer must reside at an address that is a multiple to 64 bytes.
- `flags` – Unused, always 0.
- `option` – Pointer to an optional [SceKernelLMOption](#struct-scekernellmoption) structure.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelStartModule()`

```c
int sceKernelStartModule(SceUID modid, SceSize argsize, void *argp, int *status, SceKernelSMOption *option);
```

Start a loaded module.

**Parameters:**

- `modid` – The ID of the module returned from LoadModule.
- `argsize` – Length of the args.
- `argp` – A pointer to the arguments to the module.
- `status` – Returns the status of the start.
- `option` – Pointer to an optional [SceKernelSMOption](#struct-scekernelsmoption) structure.

**Returns:** modID (modID > 0) UID of the module that was started and made resident, 0 on success for modules that don't need to be made resident, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelStopModule()`

```c
int sceKernelStopModule(SceUID modid, SceSize argsize, void *argp, int *status, SceKernelSMOption *option);
```

Stop a running module.

**Parameters:**

- `modid` – The UID of the module to stop.
- `argsize` – The length of the arguments pointed to by argp.
- `argp` – Pointer to arguments to pass to the module's module_stop() routine.
- `status` – Return value of the module's module_stop() routine.
- `option` – Pointer to an optional [SceKernelSMOption](#struct-scekernelsmoption) structure.

**Returns:** ??? on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelUnloadModule()`

```c
int sceKernelUnloadModule(SceUID modid);
```

Unload a stopped module.

**Parameters:**

- `modid` – The UID of the module to unload.

**Returns:** ??? on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelSelfStopUnloadModule()`

```c
int sceKernelSelfStopUnloadModule(int unknown, SceSize argsize, void *argp);
```

Stop and unload the current module.

**Parameters:**

- `unknown` – Unknown (I've seen 1 passed).
- `argsize` – Size (in bytes) of the arguments that will be passed to module_stop().
- `argp` – Pointer to arguments that will be passed to module_stop().

**Returns:** ??? on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelStopUnloadSelfModule()`

```c
int sceKernelStopUnloadSelfModule(SceSize argsize, void *argp, int *status, SceKernelSMOption *option);
```

Stop and unload the current module.

**Parameters:**

- `argsize` – Size (in bytes) of the arguments that will be passed to module_stop().
- `argp` – Poitner to arguments that will be passed to module_stop().
- `status` – Return value from module_stop().
- `option` – Pointer to an optional [SceKernelSMOption](#struct-scekernelsmoption) structure.

**Returns:** ??? on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelQueryModuleInfo()`

```c
int sceKernelQueryModuleInfo(SceUID modid, SceKernelModuleInfo *info);
```

Query the information about a loaded module from its UID.

**Note:** This fails on v1.0 firmware (and even it worked has a limited structure) so if you want to be compatible with both 1.5 and 1.0 (and you are running in kernel mode) then call this function first then [pspSdkQueryModuleInfoV1](../sdk/pspsdk.h.md#pspsdkquerymoduleinfov1) if it fails, or make separate v1 and v1.5+ builds.

**Parameters:**

- `modid` – The UID of the loaded module.
- `info` – Pointer to a [SceKernelModuleInfo](#struct-scekernelmoduleinfo) structure.

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelGetModuleIdList()`

```c
int sceKernelGetModuleIdList(SceUID *readbuf, int readbufsize, int *idcount);
```

Get a list of module IDs.

NOTE: This is only available on 1.5 firmware and above. For V1 use [pspSdkGetModuleIdList](../sdk/pspsdk.h.md#pspsdkgetmoduleidlist).

**Parameters:**

- `readbuf` – Buffer to store the module list.
- `readbufsize` – Number of elements in the readbuffer.
- `idcount` – Returns the number of module ids

**Returns:** >= 0 on success

### `sceKernelGetModuleIdByAddress()`

```c
int sceKernelGetModuleIdByAddress(const void *moduleAddr);
```

Get the ID of the module occupying the address.

**Parameters:**

- `moduleAddr` – A pointer to the module

**Returns:** >= 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

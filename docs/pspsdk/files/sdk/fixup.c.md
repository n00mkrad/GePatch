[PSPSDK documentation](../../README.md) › Files

# sdk/fixup.c

```c
#include <pspkernel.h>
#include <string.h>
```

## Data Structures

### `struct SceLibStubEntry`

```c
struct SceLibStubEntry {
    char * moduleName;
    unsigned short version;
    unsigned short attr;
    unsigned char structsz;
    unsigned char numVars;
    unsigned short numFuncs;
    u32 * nidList;
    u32 * stubs;
};
```

### `struct PspModuleExport`

```c
struct PspModuleExport {
    const char * name;
    u32 flags;
    u8 unk;
    u8 v_count;
    u16 f_count;
    u32 * exports;
};
```

## Functions

### `pspSdkFindExport()`

```c
static void * pspSdkFindExport(SceModule *modInfo, const char *exportName, u32 nid);
```

## Variables

### `module_info`

```c
SceModuleInfo module_info;
```

**Also defined in this file** (documented with the declaration):

- [`pspSdkFixupImports`](pspsdk.h.md#pspsdkfixupimports)

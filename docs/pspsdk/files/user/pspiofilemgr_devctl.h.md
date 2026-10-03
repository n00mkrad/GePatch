[PSPSDK documentation](../../README.md) › Files

# user/pspiofilemgr_devctl.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct SceDevInf`

```c
struct SceDevInf {
    uint32_t maxClusters;
    uint32_t freeClusters;
    uint32_t maxSectors;
    int32_t sectorSize;
    int32_t sectorCount;
};
```

### `struct SceDevctlCmd`

```c
struct SceDevctlCmd {
    SceDevInf * dev_inf;
};
```

## Macros

### `SCE_PR_GETDEV`

```c
#define SCE_PR_GETDEV 0x02425818
```

## Typedefs

### `SceDevInf`

```c
typedef struct SceDevInf SceDevInf;
```

### `SceDevctlCmd`

```c
typedef struct SceDevctlCmd SceDevctlCmd;
```

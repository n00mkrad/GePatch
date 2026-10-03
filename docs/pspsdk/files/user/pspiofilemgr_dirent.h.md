[PSPSDK documentation](../../README.md) › Files

# user/pspiofilemgr_dirent.h

```c
#include <pspiofilemgr_stat.h>
```

## Data Structures

### `struct SceIoFatDirentPrivate`

```c
struct SceIoFatDirentPrivate {
    SceSize size;
    char s_name[13];
    char __padding__[3];
    char l_name[1024];
};
```

### `struct SceIoDirent`

Describes a single directory entry.

| Field | Description |
|---|---|
| `SceIoStat d_stat` | File status. |
| `char d_name[256]` | File name. |
| `SceIoFatDirentPrivate * d_private` | Device-specific data. |
| `int dummy` |  |

## Typedefs

### `SceIoFatDirentPrivate`

```c
typedef struct SceIoFatDirentPrivate SceIoFatDirentPrivate;
```

### `SceIoDirent`

```c
typedef struct SceIoDirent SceIoDirent;
```

Describes a single directory entry.

[PSPSDK documentation](../../README.md) › Files

# gu/sceGuInit.c

```c
#include "guInternal.h"
#include <pspuser.h>
#include <pspge.h>
#include <pspdisplay.h>
```

## Macros

### `ZV()`

```c
#define ZV(command) (uint32_t)(command << 24 | 0x00000000)
```

### `CV()`

```c
#define CV(command, value) (uint32_t)(command << 24 | value)
```

## Functions

### `sceGuResetGlobalVariables()`

```c
static void sceGuResetGlobalVariables(void);
```

### `callbackFin()`

```c
void callbackFin(int id, void *arg);
```

### `callbackSig()`

```c
void callbackSig(int id, void *arg);
```

## Variables

### `ge_init_list`

```c
unsigned int ge_init_list[][];
```

**Also defined in this file** (documented with the declaration):

- [`sceGuInit`](pspgu.h.md#sceguinit)
- [`guGetInit`](pspgu.h.md#gugetinit)

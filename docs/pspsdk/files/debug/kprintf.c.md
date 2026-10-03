[PSPSDK documentation](../../README.md) › Files

# debug/kprintf.c

```c
#include <pspkernel.h>
#include <pspdebug.h>
```

## Functions

### `sceKernelRegisterKprintfHandler()`

```c
int sceKernelRegisterKprintfHandler(void *func, void *args);
```

### `_pspDebugDefaultKprintfHandler()`

```c
static void _pspDebugDefaultKprintfHandler(const char *format, u32 *args);
```

### `_pspDebugKprintfHandler()`

```c
static void _pspDebugKprintfHandler(void *arg, const char *format, u32 *args);
```

## Variables

### `curr_handler`

```c
PspDebugKprintfHandler curr_handler;
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugInstallKprintfHandler`](pspdebug.h.md#pspdebuginstallkprintfhandler)

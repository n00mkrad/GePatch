[PSPSDK documentation](../../README.md) › Files

# debug/stacktrace.c

```c
#include <pspuser.h>
#include <pspdebug.h>
#include <string.h>
#include <stddef.h>
```

## Macros

### `CALL`

```c
#define CALL 0x0C000000
```

### `CALL_MASK`

```c
#define CALL_MASK 0xFC000000
```

### `IS_CALL()`

```c
#define IS_CALL(x) (((x) & CALL_MASK) == CALL)
```

### `CALL_ADDR()`

```c
#define CALL_ADDR(x) (((x) & ~CALL_MASK) << 2)
```

## Functions

### `validAddress()`

```c
static int validAddress(u32 *addr);
```

### `_pspDebugDoStackTrace()`

```c
static int _pspDebugDoStackTrace(u32 *sp, u32 *sp_end, u32 *ra, PspDebugStackTrace *trace, int max);
```

## Variables

### `_ftext`

```c
u32 _ftext;
```

### `_etext`

```c
u32 _etext;
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugGetStackTrace2`](pspdebug.h.md#pspdebuggetstacktrace2)

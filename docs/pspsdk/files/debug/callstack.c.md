[PSPSDK documentation](../../README.md) › Files

# debug/callstack.c

```c
#include "pspdebug.h"
```

## Data Structures

### `struct _returnCache`

```c
struct _returnCache {
    unsigned int * returnAddress;
    int raOffset;
    int spAdjust;
};
```

## Macros

### `RESTORE_RETURNVAL`

```c
#define RESTORE_RETURNVAL 0x8fbf0000
```

### `RESTORE_RETURNVAL_MASK`

```c
#define RESTORE_RETURNVAL_MASK 0xffff0000
```

### `RESTORE_RETURNVAL2`

```c
#define RESTORE_RETURNVAL2 0xdfbf0000
```

### `RESTORE_RETURNVAL3`

```c
#define RESTORE_RETURNVAL3 0x7bbf0000
```

### `ADJUST_STACKP_C`

```c
#define ADJUST_STACKP_C 0x27bd0000
```

### `ADJUST_STACKP_C_MASK`

```c
#define ADJUST_STACKP_C_MASK 0xffff0000
```

### `ADJUST_STACKP_V`

```c
#define ADJUST_STACKP_V 0x03a1e821
```

### `ADJUST_STACKP_V_MASK`

```c
#define ADJUST_STACKP_V_MASK 0xffffffff
```

### `SET_UPPER_C`

```c
#define SET_UPPER_C 0x3c010000
```

### `SET_UPPER_C_MASK`

```c
#define SET_UPPER_C_MASK 0xffff0000
```

### `OR_LOWER_C`

```c
#define OR_LOWER_C 0x34210000
```

### `OR_LOWER_C_MASK`

```c
#define OR_LOWER_C_MASK 0xffff0000
```

### `SET_LOWER_C`

```c
#define SET_LOWER_C 0x34010000
```

### `SET_LOWER_C_MASK`

```c
#define SET_LOWER_C_MASK 0xffff0000
```

### `RETURN`

```c
#define RETURN 0x03e00008
```

### `CALL()`

```c
#define CALL(f) (0x0c000000 | (((int) (f)) >> 2))
```

### `HASH_SIZE`

```c
#define HASH_SIZE 256
```

### `HASH()`

```c
#define HASH(ra) ((((int) (ra)) >> 2) & (HASH_SIZE - 1))
```

### `TRUE`

```c
#define TRUE 1
```

### `FALSE`

```c
#define FALSE 0
```

## Typedefs

### `ReturnCacheRec`

```c
typedef struct _returnCache ReturnCacheRec;
```

### `ReturnCachePtr`

```c
typedef struct _returnCache * ReturnCachePtr;
```

### `Bool`

```c
typedef int Bool;
```

## Functions

### `pspGetReturnAddress()`

```c
unsigned int * pspGetReturnAddress();
```

### `pspGetStackPointer()`

```c
unsigned int * pspGetStackPointer();
```

### `main()`

```c
int main();
```

## Variables

### `returnCache`

```c
ReturnCacheRec returnCache[256][256];
```

### `_ftext`

```c
unsigned int _ftext;
```

### `_etext`

```c
unsigned int _etext;
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugGetStackTrace`](pspdebug.h.md#pspdebuggetstacktrace)

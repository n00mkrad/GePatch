[PSPSDK documentation](../../README.md) › Files

# libcglue/lock.c

The lock API functions required by newlib.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/lock.h>
#include <reent.h>
#include <pspthreadman.h>
```

## Data Structures

### `struct __lock`

```c
struct __lock {
    SceLwMutexWorkarea mutex;
};
```

## Functions

### `__common_lock_init()`

```c
static void __common_lock_init(_LOCK_T lock);
```

### `__common_lock_init_recursive()`

```c
static void __common_lock_init_recursive(_LOCK_T lock);
```

### `__common_lock_close()`

```c
static void __common_lock_close(_LOCK_T lock);
```

### `__common_lock_close_recursive()`

```c
static void __common_lock_close_recursive(_LOCK_T lock);
```

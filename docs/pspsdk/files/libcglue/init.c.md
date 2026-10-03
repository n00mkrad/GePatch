[PSPSDK documentation](../../README.md) › Files

# libcglue/init.c

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/param.h>
#include <pspuser.h>
```

## Functions

### `__init_cwd()`

```c
void __init_cwd(char *argv_0);
```

### `__timezone_update()`

```c
void __timezone_update();
```

### `__fdman_init()`

```c
void __fdman_init();
```

### `__init_mutex()`

```c
void __init_mutex();
```

### `pthread_init()`

```c
void pthread_init();
```

### `__psp_free_heap()`

```c
void __psp_free_heap();
```

### `__deinit_mutex()`

```c
void __deinit_mutex();
```

### `__locks_init()`

```c
void __locks_init();
```

### `__locks_deinit()`

```c
void __locks_deinit();
```

### `__gprof_cleanup()`

```c
void __gprof_cleanup();
```

Writes gmon.out dump file and stops profiling Called from atexit() handler; will dump out a gmon.out file at cwd with all collected information.

### `__libpthreadglue_init()`

```c
void __libpthreadglue_init();
```

### `__libcglue_deinit()`

```c
void __libcglue_deinit();
```

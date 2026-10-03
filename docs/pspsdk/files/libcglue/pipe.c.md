[PSPSDK documentation](../../README.md) › Files

# libcglue/pipe.c

```c
#include <stdio.h>
#include <errno.h>
#include <sys/syslimits.h>
#include <sys/types.h>
#include <psptypes.h>
#include <pspthreadman.h>
#include <pspmodulemgr.h>
#include <pspkerror.h>
#include "fdman.h"
```

## Functions

### `__set_errno()`

```c
int __set_errno(int code);
```

### `__pipe_peekmsgsize()`

```c
size_t __pipe_peekmsgsize(int fd);
```

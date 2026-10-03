[PSPSDK documentation](../../README.md) › Files

# libcglue/cwd.c

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/param.h>
#include <dirent.h>
#include <errno.h>
```

## Functions

### `__get_drive()`

```c
int __get_drive(const char *d);
```

## Variables

### `__cwd`

```c
char __cwd[MAXNAMLEN+1][MAXNAMLEN+1];
```

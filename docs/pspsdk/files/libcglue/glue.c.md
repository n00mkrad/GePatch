[PSPSDK documentation](../../README.md) › Files

# libcglue/glue.c

```c
#include <stdio.h>
#include <errno.h>
#include <malloc.h>
#include <stdarg.h>
#include <string.h>
#include <time.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <pwd.h>
#include <sys/time.h>
#include <sys/timeb.h>
#include <sys/times.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/statvfs.h>
#include <sys/syslimits.h>
#include <psptypes.h>
#include <pspiofilemgr.h>
#include <pspmodulemgr.h>
#include <pspsysmem.h>
#include <pspthreadman.h>
#include <psputils.h>
#include <pspsdk.h>
#include <psprtc.h>
#include <psputility.h>
#include "fdman.h"
```

## Macros

### `DEFAULT_HEAP_THRESHOLD_SIZE_KB`

```c
#define DEFAULT_HEAP_THRESHOLD_SIZE_KB 512
```

## Functions

### `__get_drive()`

```c
int __get_drive(const char *d);
```

### `__path_absolute()`

```c
int __path_absolute(const char *in, char *out, int len);
```

### `__set_errno()`

```c
int __set_errno(int code);
```

### `__pipe_read()`

```c
int __pipe_read(int fd, void *buf, size_t len);
```

### `__pipe_close()`

```c
int __pipe_close(int fd);
```

### `__pipe_write()`

```c
int __pipe_write(int fd, const void *buf, size_t len);
```

### `__pipe_nonblocking_read()`

```c
int __pipe_nonblocking_read(int fd, void *buf, size_t len);
```

### `__pipe_nonblocking_write()`

```c
int __pipe_nonblocking_write(int fd, const void *buf, size_t len);
```

### `__socket_close()`

```c
int __socket_close(int sock);
```

### `_open()`

```c
int _open(const char *buf, int flags, int mode);
```

### `_stat()`

```c
int _stat(const char *filename, struct stat *buf);
```

## Variables

### `sce_newlib_heap_kb_size`

```c
unsigned int sce_newlib_heap_kb_size;
```

### `sce_newlib_heap_threshold_kb_size`

```c
unsigned int sce_newlib_heap_threshold_kb_size;
```

### `__cwd`

```c
char __cwd[MAXNAMLEN+1][MAXNAMLEN+1];
```

### `__sbrk_mutex`

```c
SceLwMutexWorkarea __sbrk_mutex;
```

### `__dummy_passwd`

```c
struct passwd __dummy_passwd;
```

### `__psp_heap_blockid`

```c
SceUID __psp_heap_blockid;
```

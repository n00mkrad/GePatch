[PSPSDK documentation](../../README.md) › Files

# kernel/pspstdio_kernel.h

```c
#include <psptypes.h>
#include <pspkerneltypes.h>
#include <pspiofilemgr.h>
```

Topics: [Driver interface to Stdio](../../topics/Stdio_Kernel.md)

## Functions

### `sceKernelStdoutReopen()`

```c
int sceKernelStdoutReopen(const char *file, int flags, SceMode mode);
```

Function reopen the stdout file handle to a new file.

**Parameters:**

- `file` – The file to open.
- `flags` – The open flags
- `mode` – The file mode

**Returns:** \< 0 on error.

### `sceKernelStderrReopen()`

```c
int sceKernelStderrReopen(const char *file, int flags, SceMode mode);
```

Function reopen the stderr file handle to a new file.

**Parameters:**

- `file` – The file to open.
- `flags` – The open flags
- `mode` – The file mode

**Returns:** \< 0 on error.

### `fdprintf()`

```c
int fdprintf(int fd, const char *format,...);
```

fprintf but for file descriptors

**Parameters:**

- `fd` – file descriptor from sceIoOpen
- `format` – format string
- `...` – variables

**Returns:** number of characters printed, \<0 on error

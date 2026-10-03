[PSPSDK documentation](../../README.md) › Files

# user/pspstdio.h

```c
#include <pspkerneltypes.h>
```

Topics: [Stdio Library](../../topics/Stdio.md)

## Functions

### `sceKernelStdin()`

```c
SceUID sceKernelStdin(void);
```

Function to get the current standard in file no.

**Returns:** The stdin fileno

### `sceKernelStdout()`

```c
SceUID sceKernelStdout(void);
```

Function to get the current standard out file no.

**Returns:** The stdout fileno

### `sceKernelStderr()`

```c
SceUID sceKernelStderr(void);
```

Function to get the current standard err file no.

**Returns:** The stderr fileno

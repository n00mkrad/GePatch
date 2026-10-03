[PSPSDK documentation](../../README.md) › Files

# debug/gdb-kernellib.c

```c
#include <pspkernel.h>
#include <pspdebug.h>
```

## Functions

### `putDebugChar()`

```c
void putDebugChar(char ch);
```

### `getDebugChar()`

```c
char getDebugChar(void);
```

### `sceKernelDcacheWBinvAll()`

```c
void sceKernelDcacheWBinvAll(void);
```

### `sceKernelIcacheClearAll()`

```c
void sceKernelIcacheClearAll(void);
```

### `_gdbSupportLibFlushCaches()`

```c
void _gdbSupportLibFlushCaches(void);
```

### `_gdbSupportLibReadByte()`

```c
int _gdbSupportLibReadByte(unsigned char *address, unsigned char *dest);
```

### `_gdbSupportLibWriteByte()`

```c
int _gdbSupportLibWriteByte(char val, unsigned char *dest);
```

### `_gdbSupportLibInit()`

```c
int _gdbSupportLibInit(void);
```

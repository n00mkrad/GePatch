[PSPSDK documentation](../../README.md) › Files

# debug/gdb-userlib.c

```c
#include <pspkernel.h>
#include <pspdebug.h>
#include <string.h>
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

### `io_init()`

```c
static int io_init(PspIoDrvArg *arg);
```

### `io_exit()`

```c
static int io_exit(PspIoDrvArg *arg);
```

### `io_read()`

```c
static int io_read(PspIoDrvFileArg *arg, char *data, int len);
```

### `io_write()`

```c
static int io_write(PspIoDrvFileArg *arg, const char *data, int len);
```

### `sceKernelDcacheWBinvAll()`

```c
void sceKernelDcacheWBinvAll(void);
```

### `sceKernelIcacheClearAll()`

```c
void sceKernelIcacheClearAll(void);
```

### `io_devctl()`

```c
static int io_devctl(PspIoDrvFileArg *arg, const char *devname, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

### `_gdbSupportLibReadByte()`

```c
int _gdbSupportLibReadByte(unsigned char *address, unsigned char *dest);
```

### `_gdbSupportLibWriteByte()`

```c
int _gdbSupportLibWriteByte(char val, unsigned char *dest);
```

### `_gdbSupportLibFlushCaches()`

```c
void _gdbSupportLibFlushCaches(void);
```

### `_gdbSupportLibInit()`

```c
int _gdbSupportLibInit(void);
```

## Variables

### `sio_fd`

```c
int sio_fd = -1;
```

### `g_initialised`

```c
int g_initialised = 0;
```

### `sio_funcs`

```c
PspIoDrvFuncs sio_funcs =
{
	io_init,
	io_exit,
	NULL,
	NULL,
	io_read,
	io_write,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	io_devctl,
	NULL,
};
```

### `sio_driver`

```c
PspIoDrv sio_driver =
{
	"sio", 0x10, 0x800, "SIO", &sio_funcs
};
```

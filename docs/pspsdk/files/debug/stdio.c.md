[PSPSDK documentation](../../README.md) › Files

# debug/stdio.c

```c
#include <pspkernel.h>
#include <pspdebug.h>
#include <unistd.h>
```

## Macros

### `dbgprintf`

```c
#define dbgprintf pspDebugScreenPrintf
```

## Functions

### `io_init()`

```c
static int io_init(PspIoDrvArg *arg);
```

### `io_exit()`

```c
static int io_exit(PspIoDrvArg *arg);
```

### `io_open()`

```c
static int io_open(PspIoDrvFileArg *arg, char *file, int mode, SceMode mask);
```

### `io_close()`

```c
static int io_close(PspIoDrvFileArg *arg);
```

### `io_read()`

```c
static int io_read(PspIoDrvFileArg *arg, char *data, int len);
```

### `io_write()`

```c
static int io_write(PspIoDrvFileArg *arg, const char *data, int len);
```

### `io_lseek()`

```c
static SceOff io_lseek(PspIoDrvFileArg *arg, SceOff ofs, int whence);
```

### `io_ioctl()`

```c
static int io_ioctl(PspIoDrvFileArg *arg, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

### `io_remove()`

```c
static int io_remove(PspIoDrvFileArg *arg, const char *name);
```

### `io_mkdir()`

```c
static int io_mkdir(PspIoDrvFileArg *arg, const char *name, SceMode mode);
```

### `io_rmdir()`

```c
static int io_rmdir(PspIoDrvFileArg *arg, const char *name);
```

### `io_dopen()`

```c
static int io_dopen(PspIoDrvFileArg *arg, const char *dir);
```

### `io_dclose()`

```c
static int io_dclose(PspIoDrvFileArg *arg);
```

### `io_dread()`

```c
static int io_dread(PspIoDrvFileArg *arg, SceIoDirent *dir);
```

### `io_getstat()`

```c
static int io_getstat(PspIoDrvFileArg *arg, const char *file, SceIoStat *stat);
```

### `io_chstat()`

```c
static int io_chstat(PspIoDrvFileArg *arg, const char *file, SceIoStat *stat, int bits);
```

### `io_rename()`

```c
static int io_rename(PspIoDrvFileArg *arg, const char *oldname, const char *newname);
```

### `io_chdir()`

```c
static int io_chdir(PspIoDrvFileArg *arg, const char *dir);
```

### `io_mount()`

```c
static int io_mount(PspIoDrvFileArg *arg);
```

### `io_umount()`

```c
static int io_umount(PspIoDrvFileArg *arg);
```

### `io_devctl()`

```c
static int io_devctl(PspIoDrvFileArg *arg, const char *devname, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

### `io_unknown()`

```c
static int io_unknown(PspIoDrvFileArg *arg);
```

### `tty_init()`

```c
static int tty_init(void);
```

## Variables

### `g_initialised`

```c
int g_initialised = 0;
```

### `g_stdin_handler`

```c
PspDebugInputHandler g_stdin_handler = NULL;
```

### `g_stdout_handler`

```c
PspDebugPrintHandler g_stdout_handler = NULL;
```

### `g_stderr_handler`

```c
PspDebugPrintHandler g_stderr_handler = NULL;
```

### `g_in_sema`

```c
SceUID g_in_sema = 0;
```

### `g_out_sema`

```c
SceUID g_out_sema = 0;
```

### `tty_funcs`

```c
PspIoDrvFuncs tty_funcs =
{
	io_init,
	io_exit,
	io_open,
	io_close,
	io_read,
	io_write,
	io_lseek,
	io_ioctl,
	io_remove,
	io_mkdir,
	io_rmdir,
	io_dopen,
	io_dclose,
	io_dread,
	io_getstat,
	io_chstat,
	io_rename,
	io_chdir,
	io_mount,
	io_umount,
	io_devctl,
	io_unknown,
};
```

### `tty_driver`

```c
PspIoDrv tty_driver =
{
	"tty", 0x10, 0x800, "TTY", &tty_funcs
};
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugInstallStdinHandler`](pspdebug.h.md#pspdebuginstallstdinhandler)
- [`pspDebugInstallStdoutHandler`](pspdebug.h.md#pspdebuginstallstdouthandler)
- [`pspDebugInstallStderrHandler`](pspdebug.h.md#pspdebuginstallstderrhandler)

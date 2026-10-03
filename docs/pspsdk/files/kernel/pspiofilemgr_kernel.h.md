[PSPSDK documentation](../../README.md) › Files

# kernel/pspiofilemgr_kernel.h

```c
#include <psptypes.h>
#include <pspkerneltypes.h>
#include <pspiofilemgr.h>
```

Topics: [Driver interface to IoFileMgr](../../topics/IoFileMgr_Kernel.md)

## Data Structures

### `struct PspIoDrvArg`

Structure passed to the init and exit functions of the io driver system.

| Field | Description |
|---|---|
| `struct PspIoDrv * drv` | Pointer to the original driver which was added. |
| `void * arg` | Pointer to a user defined argument (if written by the driver will preseve across calls. |

### `struct PspIoDrvFileArg`

Structure passed to the file functions of the io driver system.

| Field | Description |
|---|---|
| `u32 unk1` | Unknown. |
| `u32 fs_num` | The file system number, e.g.<br>if a file is opened as host5:/myfile.txt this field will be 5 |
| `PspIoDrvArg * drv` | Pointer to the driver structure. |
| `u32 unk2` | Unknown, again. |
| `void * arg` | Pointer to a user defined argument, this is preserved on a per file basis. |

### `struct PspIoDrvFuncs`

Structure to maintain the file driver pointers.

```c
struct PspIoDrvFuncs {
    int(* IoInit)(PspIoDrvArg *arg);
    int(* IoExit)(PspIoDrvArg *arg);
    int(* IoOpen)(PspIoDrvFileArg *arg, char *file, int flags, SceMode mode);
    int(* IoClose)(PspIoDrvFileArg *arg);
    int(* IoRead)(PspIoDrvFileArg *arg, char *data, int len);
    int(* IoWrite)(PspIoDrvFileArg *arg, const char *data, int len);
    SceOff(* IoLseek)(PspIoDrvFileArg *arg, SceOff ofs, int whence);
    int(* IoIoctl)(PspIoDrvFileArg *arg, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
    int(* IoRemove)(PspIoDrvFileArg *arg, const char *name);
    int(* IoMkdir)(PspIoDrvFileArg *arg, const char *name, SceMode mode);
    int(* IoRmdir)(PspIoDrvFileArg *arg, const char *name);
    int(* IoDopen)(PspIoDrvFileArg *arg, const char *dirname);
    int(* IoDclose)(PspIoDrvFileArg *arg);
    int(* IoDread)(PspIoDrvFileArg *arg, SceIoDirent *dir);
    int(* IoGetstat)(PspIoDrvFileArg *arg, const char *file, SceIoStat *stat);
    int(* IoChstat)(PspIoDrvFileArg *arg, const char *file, SceIoStat *stat, int bits);
    int(* IoRename)(PspIoDrvFileArg *arg, const char *oldname, const char *newname);
    int(* IoChdir)(PspIoDrvFileArg *arg, const char *dir);
    int(* IoMount)(PspIoDrvFileArg *arg);
    int(* IoUmount)(PspIoDrvFileArg *arg);
    int(* IoDevctl)(PspIoDrvFileArg *arg, const char *devname, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
    int(* IoUnk21)(PspIoDrvFileArg *arg);
};
```

### `struct PspIoDrv`

| Field | Description |
|---|---|
| `const char * name` | The name of the device to add. |
| `u32 dev_type` | Device type, this 0x10 is for a filesystem driver. |
| `u32 unk2` | Unknown, set to 0x800. |
| `const char * name2` | This seems to be the same as name but capitalised :/. |
| `PspIoDrvFuncs * funcs` | Pointer to a filled out functions table. |

## Typedefs

### `PspIoDrvArg`

```c
typedef struct PspIoDrvArg PspIoDrvArg;
```

Structure passed to the init and exit functions of the io driver system.

### `PspIoDrvFileArg`

```c
typedef struct PspIoDrvFileArg PspIoDrvFileArg;
```

Structure passed to the file functions of the io driver system.

### `PspIoDrvFuncs`

```c
typedef struct PspIoDrvFuncs PspIoDrvFuncs;
```

Structure to maintain the file driver pointers.

### `PspIoDrv`

```c
typedef struct PspIoDrv PspIoDrv;
```

## Functions

### `sceIoAddDrv()`

```c
int sceIoAddDrv(PspIoDrv *drv);
```

Adds a new IO driver to the system.

**Note:** This is only exported in the kernel version of IoFileMgr

**Parameters:**

- `drv` – Pointer to a filled out driver structure

**Returns:** \< 0 on error.

**Example::**

```c
PspIoDrvFuncs host_funcs = { ... };
PspIoDrv host_driver = { "host", 0x10, 0x800, "HOST", &host_funcs };
sceIoDelDrv("host");
sceIoAddDrv(&host_driver);
```

### `sceIoDelDrv()`

```c
int sceIoDelDrv(const char *drv_name);
```

Deletes a IO driver from the system.

**Note:** This is only exported in the kernel version of IoFileMgr

**Parameters:**

- `drv_name` – Name of the driver to delete.

**Returns:** \< 0 on error

### `sceIoReopen()`

```c
int sceIoReopen(const char *file, int flags, SceMode mode, SceUID fd);
```

Reopens an existing file descriptor.

**Parameters:**

- `file` – The new file to open.
- `flags` – The open flags.
- `mode` – The open mode.
- `fd` – The old filedescriptor to reopen

**Returns:** \< 0 on error, otherwise the reopened fd.

### `sceIoGetThreadCwd()`

```c
int sceIoGetThreadCwd(SceUID uid, char *dir, int len);
```

Get the current working directory for a thread.

**Parameters:**

- `uid` – The UID of the thread
- `dir` – A character buffer in which to store the cwd
- `len` – The length of the buffer

**Returns:** Number of characters written to buf, if no cwd then 0 is returned.

### `sceIoChangeThreadCwd()`

```c
int sceIoChangeThreadCwd(SceUID uid, char *dir);
```

Set the current working directory for a thread.

**Parameters:**

- `uid` – The UID of the thread
- `dir` – The directory to set

**Returns:** 0 on success, \< 0 on error

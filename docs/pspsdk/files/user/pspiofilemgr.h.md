[PSPSDK documentation](../../README.md) › Files

# user/pspiofilemgr.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspiofilemgr_fcntl.h>
#include <pspiofilemgr_stat.h>
#include <pspiofilemgr_dirent.h>
#include <pspiofilemgr_devctl.h>
```

Topics: [File IO Library](../../topics/FileIO.md)

## Enumerations

### `enum IoAssignPerms`

Permission value for the sceIoAssign function.

| Enumerator | Value | Description |
|---|---|---|
| `IOASSIGN_RDWR` | `0` | Assign the device read/write. |
| `IOASSIGN_RDONLY` | `1` | Assign the device read only. |

## Functions

### `sceIoOpen()`

```c
SceUID sceIoOpen(const char *file, int flags, SceMode mode);
```

Open or create a file for reading or writing.

**Example1: Open a file for reading:**

```c
if(!(fd = sceIoOpen("device:/path/to/file", O_RDONLY, 0777)) {
     // error
}
```

**Example2: Open a file for writing, creating it if it doesnt exist:**

```c
if(!(fd = sceIoOpen("device:/path/to/file", O_WRONLY|O_CREAT, 0777)) {
     // error
}
```

**Parameters:**

- `file` – Pointer to a string holding the name of the file to open
- `flags` – Libc styled flags that are or'ed together
- `mode` – File access mode.

**Returns:** A non-negative integer is a valid fd, anything else an error

### `sceIoOpenAsync()`

```c
SceUID sceIoOpenAsync(const char *file, int flags, SceMode mode);
```

Open or create a file for reading or writing (asynchronous)

**Parameters:**

- `file` – Pointer to a string holding the name of the file to open
- `flags` – Libc styled flags that are or'ed together
- `mode` – File access mode.

**Returns:** A non-negative integer is a valid fd, anything else an error

### `sceIoClose()`

```c
int sceIoClose(SceUID fd);
```

Delete a descriptor.

```c
sceIoClose(fd);
```

**Parameters:**

- `fd` – File descriptor to close

**Returns:** \< 0 on error

### `sceIoCloseAsync()`

```c
int sceIoCloseAsync(SceUID fd);
```

Delete a descriptor (asynchronous)

**Parameters:**

- `fd` – File descriptor to close

**Returns:** \< 0 on error

### `sceIoRead()`

```c
int sceIoRead(SceUID fd, void *data, SceSize size);
```

Read input.

**Example::**

```c
bytes_read = sceIoRead(fd, data, 100);
```

**Parameters:**

- `fd` – Opened file descriptor to read from
- `data` – Pointer to the buffer where the read data will be placed
- `size` – Size of the read in bytes

**Returns:** The number of bytes read

### `sceIoReadAsync()`

```c
int sceIoReadAsync(SceUID fd, void *data, SceSize size);
```

Read input (asynchronous)

**Example::**

```c
bytes_read = sceIoRead(fd, data, 100);
```

**Parameters:**

- `fd` – Opened file descriptor to read from
- `data` – Pointer to the buffer where the read data will be placed
- `size` – Size of the read in bytes

**Returns:** \< 0 on error.

### `sceIoWrite()`

```c
int sceIoWrite(SceUID fd, const void *data, SceSize size);
```

Write output.

**Example::**

```c
bytes_written = sceIoWrite(fd, data, 100);
```

**Parameters:**

- `fd` – Opened file descriptor to write to
- `data` – Pointer to the data to write
- `size` – Size of data to write

**Returns:** The number of bytes written

### `sceIoWriteAsync()`

```c
int sceIoWriteAsync(SceUID fd, const void *data, SceSize size);
```

Write output (asynchronous)

**Parameters:**

- `fd` – Opened file descriptor to write to
- `data` – Pointer to the data to write
- `size` – Size of data to write

**Returns:** \< 0 on error.

### `sceIoLseek()`

```c
SceOff sceIoLseek(SceUID fd, SceOff offset, int whence);
```

Reposition read/write file descriptor offset.

**Example::**

```c
pos = sceIoLseek(fd, -10, SEEK_END);
```

**Parameters:**

- `fd` – Opened file descriptor with which to seek
- `offset` – Relative offset from the start position given by whence
- `whence` – Set to SEEK_SET to seek from the start of the file, SEEK_CUR seek from the current position and SEEK_END to seek from the end.

**Returns:** The position in the file after the seek.

### `sceIoLseekAsync()`

```c
int sceIoLseekAsync(SceUID fd, SceOff offset, int whence);
```

Reposition read/write file descriptor offset (asynchronous)

**Parameters:**

- `fd` – Opened file descriptor with which to seek
- `offset` – Relative offset from the start position given by whence
- `whence` – Set to SEEK_SET to seek from the start of the file, SEEK_CUR seek from the current position and SEEK_END to seek from the end.

**Returns:** \< 0 on error. Actual value should be passed returned by the [sceIoWaitAsync](#sceiowaitasync) call.

### `sceIoLseek32()`

```c
int sceIoLseek32(SceUID fd, int offset, int whence);
```

Reposition read/write file descriptor offset (32bit mode)

**Example::**

```c
pos = sceIoLseek32(fd, -10, SEEK_END);
```

**Parameters:**

- `fd` – Opened file descriptor with which to seek
- `offset` – Relative offset from the start position given by whence
- `whence` – Set to SEEK_SET to seek from the start of the file, SEEK_CUR seek from the current position and SEEK_END to seek from the end.

**Returns:** The position in the file after the seek.

### `sceIoLseek32Async()`

```c
int sceIoLseek32Async(SceUID fd, int offset, int whence);
```

Reposition read/write file descriptor offset (32bit mode, asynchronous)

**Parameters:**

- `fd` – Opened file descriptor with which to seek
- `offset` – Relative offset from the start position given by whence
- `whence` – Set to SEEK_SET to seek from the start of the file, SEEK_CUR seek from the current position and SEEK_END to seek from the end.

**Returns:** \< 0 on error.

### `sceIoRemove()`

```c
int sceIoRemove(const char *file);
```

Remove directory entry.

**Parameters:**

- `file` – Path to the file to remove

**Returns:** \< 0 on error

### `sceIoMkdir()`

```c
int sceIoMkdir(const char *dir, SceMode mode);
```

Make a directory file.

**Parameters:**

- `dir`
- `mode` – Access mode.

**Returns:** Returns the value 0 if its succesful otherwise -1

### `sceIoRmdir()`

```c
int sceIoRmdir(const char *path);
```

Remove a directory file.

**Parameters:**

- `path` – Removes a directory file pointed by the string path

**Returns:** Returns the value 0 if its succesful otherwise -1

### `sceIoChdir()`

```c
int sceIoChdir(const char *path);
```

Change the current directory.

**Parameters:**

- `path` – The path to change to.

**Returns:** \< 0 on error.

### `sceIoRename()`

```c
int sceIoRename(const char *oldname, const char *newname);
```

Change the name of a file.

**Parameters:**

- `oldname` – The old filename
- `newname` – The new filename

**Returns:** \< 0 on error.

### `sceIoDopen()`

```c
SceUID sceIoDopen(const char *dirname);
```

Open a directory.

**Example::**

```c
int dfd;
dfd = sceIoDopen("device:/");
if(dfd >= 0)
{ Do something with the file descriptor }
```

**Parameters:**

- `dirname` – The directory to open for reading.

**Returns:** If >= 0 then a valid file descriptor, otherwise a Sony error code.

### `sceIoDread()`

```c
int sceIoDread(SceUID fd, SceIoDirent *dir);
```

Reads an entry from an opened file descriptor.

**Parameters:**

- `fd` – Already opened file descriptor (using sceIoDopen)
- `dir` – Pointer to an io_dirent_t structure to hold the file information

**Returns:**

Read status

- 0 - No more directory entries left
- \> 0 - More directory entired to go
- \< 0 - Error

### `sceIoDclose()`

```c
int sceIoDclose(SceUID fd);
```

Close an opened directory file descriptor.

**Parameters:**

- `fd` – Already opened file descriptor (using sceIoDopen)

**Returns:** \< 0 on error

### `sceIoDevctl()`

```c
int sceIoDevctl(const char *dev, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

Send a devctl command to a device.

**Example: Sending a simple command to a device (not a real devctl):**

```c
sceIoDevctl("ms0:", 0x200000, indata, 4, NULL, NULL);
```

**Parameters:**

- `dev` – String for the device to send the devctl to (e.g. "ms0:")
- `cmd` – The command to send to the device
- `indata` – A data block to send to the device, if NULL sends no data
- `inlen` – Length of indata, if 0 sends no data
- `outdata` – A data block to receive the result of a command, if NULL receives no data
- `outlen` – Length of outdata, if 0 receives no data

**Returns:** 0 on success, \< 0 on error

### `sceIoAssign()`

```c
int sceIoAssign(const char *dev1, const char *dev2, const char *dev3, int mode, void *unk1, long unk2);
```

Assigns one IO device to another (I guess)

**Parameters:**

- `dev1` – The device name to assign.
- `dev2` – The block device to assign from.
- `dev3` – The filesystem device to mape the block device to dev1
- `mode` – Read/Write mode. One of IoAssignPerms.
- `unk1` – Unknown, set to NULL.
- `unk2` – Unknown, set to 0.

**Returns:** \< 0 on error.

**Example: Reassign flash0 in read/write mode.:**

```c
    sceIoUnassign("flash0");
sceIoAssign("flash0", "lflash0:0,0", "flashfat0:", IOASSIGN_RDWR, NULL, 0);
```

### `sceIoUnassign()`

```c
int sceIoUnassign(const char *dev);
```

Unassign an IO device.

**Parameters:**

- `dev` – The device to unassign.

**Returns:** \< 0 on error

**Example: See ::sceIoAssign**

### `sceIoGetstat()`

```c
int sceIoGetstat(const char *file, SceIoStat *stat);
```

Get the status of a file.

**Parameters:**

- `file` – The path to the file.
- `stat` – A pointer to an io_stat_t structure.

**Returns:** \< 0 on error.

### `sceIoChstat()`

```c
int sceIoChstat(const char *file, SceIoStat *stat, int bits);
```

Change the status of a file.

**Parameters:**

- `file` – The path to the file.
- `stat` – A pointer to an io_stat_t structure.
- `bits` – Bitmask defining which bits to change.

**Returns:** \< 0 on error.

### `sceIoIoctl()`

```c
int sceIoIoctl(SceUID fd, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

Perform an ioctl on a device.

**Parameters:**

- `fd` – Opened file descriptor to ioctl to
- `cmd` – The command to send to the device
- `indata` – A data block to send to the device, if NULL sends no data
- `inlen` – Length of indata, if 0 sends no data
- `outdata` – A data block to receive the result of a command, if NULL receives no data
- `outlen` – Length of outdata, if 0 receives no data

**Returns:** 0 on success, \< 0 on error

### `sceIoIoctlAsync()`

```c
int sceIoIoctlAsync(SceUID fd, unsigned int cmd, void *indata, int inlen, void *outdata, int outlen);
```

Perform an ioctl on a device.

(asynchronous)

**Parameters:**

- `fd` – Opened file descriptor to ioctl to
- `cmd` – The command to send to the device
- `indata` – A data block to send to the device, if NULL sends no data
- `inlen` – Length of indata, if 0 sends no data
- `outdata` – A data block to receive the result of a command, if NULL receives no data
- `outlen` – Length of outdata, if 0 receives no data

**Returns:** 0 on success, \< 0 on error

### `sceIoSync()`

```c
int sceIoSync(const char *device, unsigned int unk);
```

Synchronise the file data on the device.

**Parameters:**

- `device` – The device to synchronise (e.g. msfat0:)
- `unk` – Unknown

### `sceIoWaitAsync()`

```c
int sceIoWaitAsync(SceUID fd, SceInt64 *res);
```

Wait for asyncronous completion.

**Parameters:**

- `fd` – The file descriptor which is current performing an asynchronous action.
- `res` – The result of the async action.

**Returns:** \< 0 on error.

### `sceIoWaitAsyncCB()`

```c
int sceIoWaitAsyncCB(SceUID fd, SceInt64 *res);
```

Wait for asyncronous completion (with callbacks).

**Parameters:**

- `fd` – The file descriptor which is current performing an asynchronous action.
- `res` – The result of the async action.

**Returns:** \< 0 on error.

### `sceIoPollAsync()`

```c
int sceIoPollAsync(SceUID fd, SceInt64 *res);
```

Poll for asyncronous completion.

**Parameters:**

- `fd` – The file descriptor which is current performing an asynchronous action.
- `res` – The result of the async action.

**Returns:** \< 0 on error.

### `sceIoGetAsyncStat()`

```c
int sceIoGetAsyncStat(SceUID fd, int poll, SceInt64 *res);
```

Get the asyncronous completion status.

**Parameters:**

- `fd` – The file descriptor which is current performing an asynchronous action.
- `poll` – If 0 then waits for the status, otherwise it polls the fd.
- `res` – The result of the async action.

**Returns:** \< 0 on error.

### `sceIoCancel()`

```c
int sceIoCancel(SceUID fd);
```

Cancel an asynchronous operation on a file descriptor.

**Parameters:**

- `fd` – The file descriptor to perform cancel on.

**Returns:** \< 0 on error.

### `sceIoGetDevType()`

```c
int sceIoGetDevType(SceUID fd);
```

Get the device type of the currently opened file descriptor.

**Parameters:**

- `fd` – The opened file descriptor.

**Returns:** \< 0 on error. Otherwise the device type?

### `sceIoChangeAsyncPriority()`

```c
int sceIoChangeAsyncPriority(SceUID fd, int pri);
```

Change the priority of the asynchronous thread.

**Parameters:**

- `fd` – The opened fd on which the priority should be changed.
- `pri` – The priority of the thread.

**Returns:** \< 0 on error.

### `sceIoSetAsyncCallback()`

```c
int sceIoSetAsyncCallback(SceUID fd, SceUID cb, void *argp);
```

Sets a callback for the asynchronous action.

**Parameters:**

- `fd` – The filedescriptor currently performing an asynchronous action.
- `cb` – The UID of the callback created with [sceKernelCreateCallback](pspthreadman.h.md#scekernelcreatecallback)
- `argp` – Pointer to an argument to pass to the callback.

**Returns:** \< 0 on error.

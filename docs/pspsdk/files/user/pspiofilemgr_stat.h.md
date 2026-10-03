[PSPSDK documentation](../../README.md) › Files

# user/pspiofilemgr_stat.h

```c
#include <psptypes.h>
#include <pspkerneltypes.h>
```

## Data Structures

### `struct SceIoStat`

Structure to hold the status information about a file.

| Field | Description |
|---|---|
| `SceMode st_mode` |  |
| `unsigned int st_attr` |  |
| `SceOff st_size` | Size of the file in bytes. |
| `ScePspDateTime sce_st_ctime` | Creation time. |
| `ScePspDateTime sce_st_atime` | Access time. |
| `ScePspDateTime sce_st_mtime` | Modification time. |
| `unsigned int st_private[6]` | Device-specific data. |

## Macros

### `FIO_S_ISLNK()`

```c
#define FIO_S_ISLNK(m) (((m) & FIO_S_IFMT) == FIO_S_IFLNK)
```

### `FIO_S_ISREG()`

```c
#define FIO_S_ISREG(m) (((m) & FIO_S_IFMT) == FIO_S_IFREG)
```

### `FIO_S_ISDIR()`

```c
#define FIO_S_ISDIR(m) (((m) & FIO_S_IFMT) == FIO_S_IFDIR)
```

### `FIO_SO_ISLNK()`

```c
#define FIO_SO_ISLNK(m) (((m) & FIO_SO_IFMT) == FIO_SO_IFLNK)
```

### `FIO_SO_ISREG()`

```c
#define FIO_SO_ISREG(m) (((m) & FIO_SO_IFMT) == FIO_SO_IFREG)
```

### `FIO_SO_ISDIR()`

```c
#define FIO_SO_ISDIR(m) (((m) & FIO_SO_IFMT) == FIO_SO_IFDIR)
```

## Typedefs

### `SceIoStat`

```c
typedef struct SceIoStat SceIoStat;
```

Structure to hold the status information about a file.

## Enumerations

### `enum IOAccessModes`

Access modes for st_mode in [SceIoStat](#struct-sceiostat) (confirm?).

| Enumerator | Value | Description |
|---|---|---|
| `FIO_S_IFMT` | `0xF000` | Format bits mask. |
| `FIO_S_IFLNK` | `0x4000` | Symbolic link. |
| `FIO_S_IFDIR` | `0x1000` | Directory. |
| `FIO_S_IFREG` | `0x2000` | Regular file. |
| `FIO_S_ISUID` | `0x0800` | Set UID. |
| `FIO_S_ISGID` | `0x0400` | Set GID. |
| `FIO_S_ISVTX` | `0x0200` | Sticky. |
| `FIO_S_IRWXU` | `0x01C0` | User access rights mask. |
| `FIO_S_IRUSR` | `0x0100` | Read user permission. |
| `FIO_S_IWUSR` | `0x0080` | Write user permission. |
| `FIO_S_IXUSR` | `0x0040` | Execute user permission. |
| `FIO_S_IRWXG` | `0x0038` | Group access rights mask. |
| `FIO_S_IRGRP` | `0x0020` | Group read permission. |
| `FIO_S_IWGRP` | `0x0010` | Group write permission. |
| `FIO_S_IXGRP` | `0x0008` | Group execute permission. |
| `FIO_S_IRWXO` | `0x0007` | Others access rights mask. |
| `FIO_S_IROTH` | `0x0004` | Others read permission. |
| `FIO_S_IWOTH` | `0x0002` | Others write permission. |
| `FIO_S_IXOTH` | `0x0001` | Others execute permission. |

### `enum IOFileModes`

File modes, used for the st_attr parameter in [SceIoStat](#struct-sceiostat) (confirm?).

| Enumerator | Value | Description |
|---|---|---|
| `FIO_SO_IFMT` | `0x0038` | Format mask. |
| `FIO_SO_IFLNK` | `0x0008` | Symlink. |
| `FIO_SO_IFDIR` | `0x0010` | Directory. |
| `FIO_SO_IFREG` | `0x0020` | Regular file. |
| `FIO_SO_IROTH` | `0x0004` | Hidden read permission. |
| `FIO_SO_IWOTH` | `0x0002` | Hidden write permission. |
| `FIO_SO_IXOTH` | `0x0001` | Hidden execute permission. |

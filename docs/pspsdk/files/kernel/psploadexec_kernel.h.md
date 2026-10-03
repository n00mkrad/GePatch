[PSPSDK documentation](../../README.md) › Files

# kernel/psploadexec_kernel.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <psploadexec.h>
```

Topics: [Interface to the LoadExecForKernel library.](../../topics/LoadExecKernel.md)

## Data Structures

### `struct SceKernelLoadExecVSHParam`

Structure for LoadExecVSH\* functions.

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure in bytes. |
| `SceSize args` | Size of the arguments string. |
| `void * argp` | Pointer to the arguments strings. |
| `const char * key` | The key, usually "game", "updater" or "vsh". |
| `u32 vshmain_args_size` | The size of the vshmain arguments. |
| `void * vshmain_args` | vshmain arguments that will be passed to vshmain after the program has exited |
| `char * configfile` | "/kd/pspbtcnf_game.txt" or "/kd/pspbtcnf.txt" if not supplied (max.<br>256 chars) |
| `u32 unk4` | An unknown string (max.<br>256 chars) probably used in 2nd stage of loadexec |
| `u32 unk5` | unknown flag default value = 0x10000 |

## Typedefs

### `SceKernelLoadExecVSHParam`

```c
typedef struct SceKernelLoadExecVSHParam SceKernelLoadExecVSHParam;
```

Structure for LoadExecVSH\* functions.

## Functions

### `sceKernelExitVSHVSH()`

```c
int sceKernelExitVSHVSH(struct SceKernelLoadExecVSHParam *param);
```

Restart the vsh.

**Parameters:**

- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL

**Returns:** \< 0 on some errors.

**Note:** - when called in game mode it will have the same effect that sceKernelExitGame

### `sceKernelLoadExecVSHDisc()`

```c
int sceKernelLoadExecVSHDisc(const char *file, struct SceKernelLoadExecVSHParam *param);
```

Executes a new executable from a disc.

It is the function used by the firmware to execute the EBOOT.BIN from a disc.

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL.

**Returns:** \< 0 on some errors.

### `sceKernelLoadExecVSHDiscUpdater()`

```c
int sceKernelLoadExecVSHDiscUpdater(const char *file, struct SceKernelLoadExecVSHParam *param);
```

Executes a new executable from a disc.

It is the function used by the firmware to execute an updater from a disc.

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL.

**Returns:** \< 0 on some errors.

### `sceKernelLoadExecVSHMs1()`

```c
int sceKernelLoadExecVSHMs1(const char *file, struct SceKernelLoadExecVSHParam *param);
```

Executes a new executable from a memory stick.

It is the function used by the firmware to execute an updater from a memory stick.

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL.

**Returns:** \< 0 on some errors.

### `sceKernelLoadExecVSHMs2()`

```c
int sceKernelLoadExecVSHMs2(const char *file, struct SceKernelLoadExecVSHParam *param);
```

Executes a new executable from a memory stick.

It is the function used by the firmware to execute games (and homebrew :P) from a memory stick.

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL.

**Returns:** \< 0 on some errors.

### `sceKernelLoadExecVSHMs3()`

```c
int sceKernelLoadExecVSHMs3(const char *file, struct SceKernelLoadExecVSHParam *param);
```

Executes a new executable from a memory stick.

It is the function used by the firmware to execute ... ?

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecVSHParam](#struct-scekernelloadexecvshparam) structure, or NULL.

**Returns:** \< 0 on some errors.

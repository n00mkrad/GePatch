[PSPSDK documentation](../../README.md) › Files

# user/psploadexec.h

```c
#include <psptypes.h>
```

Topics: [LoadExec Library](../../topics/LoadExec.md)

## Data Structures

### `struct SceKernelLoadExecParam`

Structure to pass to loadexec.

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure. |
| `SceSize args` | Size of the arg string. |
| `void * argp` | Pointer to the arg string. |
| `const char * key` | Encryption key ? |

## Typedefs

### `SceKernelLoadExecParam`

```c
typedef struct SceKernelLoadExecParam SceKernelLoadExecParam;
```

Structure to pass to loadexec.

## Functions

### `sceKernelRegisterExitCallback()`

```c
int sceKernelRegisterExitCallback(int cbid);
```

Register callback.

**Note:** By installing the exit callback the home button becomes active. However if sceKernelExitGame is not called in the callback it is likely that the psp will just crash.

**Example::**

```c
int exit_callback(void) { sceKernelExitGame(); }

cbid = sceKernelCreateCallback("ExitCallback", exit_callback, NULL);
sceKernelRegisterExitCallback(cbid);
```

**Parameters:**

- `cbid` – Callback id

**Returns:** \< 0 on error

### `sceKernelExitGame()`

```c
void sceKernelExitGame(void);
```

Exit game and go back to the PSP browser.

**Note:** You need to be in a thread in order for this function to work

### `sceKernelLoadExec()`

```c
int sceKernelLoadExec(const char *file, SceKernelLoadExecParam *param);
```

Execute a new game executable, limited when not running in kernel mode.

**Parameters:**

- `file` – The file to execute.
- `param` – Pointer to a [SceKernelLoadExecParam](#struct-scekernelloadexecparam) structure, or NULL.

**Returns:** \< 0 on error, probably.

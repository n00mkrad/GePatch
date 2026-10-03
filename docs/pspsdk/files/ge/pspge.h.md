[PSPSDK documentation](../../README.md) › Files

# ge/pspge.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct PspGeContext`

Stores the state of the GE.

```c
struct PspGeContext {
    unsigned int context[512];
};
```

### `struct SceGeStack`

Structure storing a stack (for CALL/RET)

| Field | Description |
|---|---|
| `unsigned int stack[8]` | The stack buffer. |

### `struct PspGeCallbackData`

Structure to hold the callback data.

| Field | Description |
|---|---|
| `PspGeCallback signal_func` | GE callback for the signal interrupt. |
| `void * signal_arg` | GE callback argument for signal interrupt. |
| `PspGeCallback finish_func` | GE callback for the finish interrupt. |
| `void * finish_arg` | GE callback argument for finish interrupt. |

### `struct PspGeListArgs`

| Field | Description |
|---|---|
| `unsigned int size` | Size of the structure (16) |
| `PspGeContext * context` | Pointer to a context. |
| `u32 numStacks` | Number of stacks to use. |
| `SceGeStack * stacks` | Pointer to the stacks (unused) |

### `struct PspGeBreakParam`

Drawing queue interruption parameter.

```c
struct PspGeBreakParam {
    unsigned int buf[4];
};
```

### `struct PspGeStack`

Structure storing a stack (for CALL/RET).

| Field | Description |
|---|---|
| `unsigned int stack[8]` | The stack buffer. |

## Typedefs

### `PspGeContext`

```c
typedef struct PspGeContext PspGeContext;
```

Stores the state of the GE.

### `PspGeCallback`

```c
typedef void(* PspGeCallback) (int id, void *arg))(int id, void *arg);
```

Typedef for a GE callback.

### `PspGeCallbackData`

```c
typedef struct PspGeCallbackData PspGeCallbackData;
```

Structure to hold the callback data.

### `PspGeListArgs`

```c
typedef struct PspGeListArgs PspGeListArgs;
```

### `PspGeBreakParam`

```c
typedef struct PspGeBreakParam PspGeBreakParam;
```

Drawing queue interruption parameter.

### `PspGeMatrixTypes`

```c
typedef enum PspGeMatrixTypes PspGeMatrixTypes;
```

GE matrix types.

### `PspGeListState`

```c
typedef enum PspGeListState PspGeListState;
```

List status for [sceGeListSync()](#scegelistsync) and [sceGeDrawSync()](#scegedrawsync).

## Enumerations

### `enum PspGeMatrixTypes`

GE matrix types.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_GE_MATRIX_BONE0` | `0` | Bone matrices. |
| `PSP_GE_MATRIX_BONE1` |  |  |
| `PSP_GE_MATRIX_BONE2` |  |  |
| `PSP_GE_MATRIX_BONE3` |  |  |
| `PSP_GE_MATRIX_BONE4` |  |  |
| `PSP_GE_MATRIX_BONE5` |  |  |
| `PSP_GE_MATRIX_BONE6` |  |  |
| `PSP_GE_MATRIX_BONE7` |  |  |
| `PSP_GE_MATRIX_WORLD` |  | World matrix. |
| `PSP_GE_MATRIX_VIEW` |  | View matrix. |
| `PSP_GE_MATRIX_PROJECTION` |  | Projection matrix. |
| `PSP_GE_MATRIX_TEXGEN` |  |  |

### `enum PspGeListState`

List status for [sceGeListSync()](#scegelistsync) and [sceGeDrawSync()](#scegedrawsync).

| Enumerator | Value | Description |
|---|---|---|
| `PSP_GE_LIST_DONE` | `0` |  |
| `PSP_GE_LIST_QUEUED` |  |  |
| `PSP_GE_LIST_DRAWING_DONE` |  |  |
| `PSP_GE_LIST_STALL_REACHED` |  |  |
| `PSP_GE_LIST_CANCEL_DONE` |  |  |

## Functions

### `sceGeEdramGetSize()`

```c
unsigned int sceGeEdramGetSize(void);
```

Get the size of VRAM.

**Returns:** The size of VRAM (in bytes).

### `sceGeEdramSetSize()`

```c
int sceGeEdramSetSize(int size);
```

Sets the EDRAM size to be enabled.

**Parameters:**

- `size` – -size The size (0x200000 or 0x400000). Will return an error if 0x400000 is specified for the PSP FAT.

**Returns:** Zero on success, otherwise less than zero.

### `sceGeEdramGetAddr()`

```c
void * sceGeEdramGetAddr(void);
```

Get the eDRAM address.

**Returns:** A pointer to the base of the eDRAM.

### `sceGeGetCmd()`

```c
unsigned int sceGeGetCmd(int cmd);
```

Retrieve the current value of a GE command.

**Parameters:**

- `cmd` – The GE command register to retrieve (0 to 0xFF, both included).

**Returns:** The value of the GE command, \< 0 on error.

### `sceGeGetMtx()`

```c
int sceGeGetMtx(int type, void *matrix);
```

Retrieve a matrix of the given type.

**Parameters:**

- `type` – One of [PspGeMatrixTypes](#enum-pspgematrixtypes).
- `matrix` – Pointer to a variable to store the matrix.

**Returns:** \< 0 on error.

### `sceGeGetStack()`

```c
int sceGeGetStack(int stackId, PspGeStack *stack);
```

Retrieve the stack of the display list currently being executed.

**Parameters:**

- `stackId` – The ID of the stack to retrieve.
- `stack` – Pointer to a structure to store the stack, or NULL to not store it.

**Returns:** The number of stacks of the current display list, \< 0 on error.

### `sceGeSaveContext()`

```c
int sceGeSaveContext(PspGeContext *context);
```

Save the GE's current state.

**Parameters:**

- `context` – Pointer to a [PspGeContext](#struct-pspgecontext).

**Returns:** \< 0 on error.

### `sceGeRestoreContext()`

```c
int sceGeRestoreContext(const PspGeContext *context);
```

Restore a previously saved GE context.

**Parameters:**

- `context` – Pointer to a [PspGeContext](#struct-pspgecontext).

**Returns:** \< 0 on error.

### `sceGeListEnQueue()`

```c
int sceGeListEnQueue(const void *list, void *stall, int cbid, PspGeListArgs *arg);
```

Enqueue a display list at the tail of the GE display list queue.

**Parameters:**

- `list` – The head of the list to queue.
- `stall` – The stall address. If NULL then no stall address is set and the list is transferred immediately.
- `cbid` – ID of the callback set by calling sceGeSetCallback
- `arg` – Structure containing GE context buffer address

**Returns:** The ID of the queue, \< 0 on error.

### `sceGeListEnQueueHead()`

```c
int sceGeListEnQueueHead(const void *list, void *stall, int cbid, PspGeListArgs *arg);
```

Enqueue a display list at the head of the GE display list queue.

**Parameters:**

- `list` – The head of the list to queue.
- `stall` – The stall address. If NULL then no stall address is set and the list is transferred immediately.
- `cbid` – ID of the callback set by calling sceGeSetCallback
- `arg` – Structure containing GE context buffer address

**Returns:** The ID of the queue, \< 0 on error.

### `sceGeListDeQueue()`

```c
int sceGeListDeQueue(int qid);
```

Cancel a queued or running list.

**Parameters:**

- `qid` – The ID of the queue.

**Returns:** \< 0 on error.

### `sceGeListUpdateStallAddr()`

```c
int sceGeListUpdateStallAddr(int qid, void *stall);
```

Update the stall address for the specified queue.

**Parameters:**

- `qid` – The ID of the queue.
- `stall` – The new stall address.

**Returns:** \< 0 on error

### `sceGeListSync()`

```c
int sceGeListSync(int qid, int syncType);
```

Wait for syncronisation of a list.

**Parameters:**

- `qid` – The queue ID of the list to sync.
- `syncType` – 0 if you want to wait for the list to be completed, or 1 if you just want to peek the actual state.

**Returns:** The specified queue status, one of [PspGeListState](#enum-pspgeliststate).

### `sceGeDrawSync()`

```c
int sceGeDrawSync(int syncType);
```

Wait for drawing to complete.

**Parameters:**

- `syncType` – 0 if you want to wait for the drawing to be completed, or 1 if you just want to peek the state of the display list currently being executed.

**Returns:** The current queue status, one of [PspGeListState](#enum-pspgeliststate).

### `sceGeSetCallback()`

```c
int sceGeSetCallback(PspGeCallbackData *cb);
```

Register callback handlers for the the GE.

**Parameters:**

- `cb` – Configured callback data structure.

**Returns:** The callback ID, \< 0 on error.

### `sceGeUnsetCallback()`

```c
int sceGeUnsetCallback(int cbid);
```

Unregister the callback handlers.

**Parameters:**

- `cbid` – The ID of the callbacks, returned by [sceGeSetCallback()](#scegesetcallback).

**Returns:** \< 0 on error

### `sceGeBreak()`

```c
int sceGeBreak(int mode, PspGeBreakParam *pParam);
```

Interrupt drawing queue.

**Parameters:**

- `mode` – If set to 1, reset all the queues.
- `pParam` – Unused (just K1-checked).

**Returns:** The stopped queue ID if mode isn't set to 0, otherwise 0, and \< 0 on error.

### `sceGeContinue()`

```c
int sceGeContinue(void);
```

Restart drawing queue.

**Returns:** \< 0 on error.

### `sceGeEdramSetAddrTranslation()`

```c
int sceGeEdramSetAddrTranslation(int width);
```

Set the eDRAM address translation mode.

**Parameters:**

- `width` – 0 to not set the translation width, otherwise 512, 1024, 2048 or 4096.

**Returns:** The previous width if it was set, otherwise 0, \< 0 on error.

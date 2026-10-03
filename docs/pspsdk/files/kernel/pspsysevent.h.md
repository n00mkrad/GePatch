[PSPSDK documentation](../../README.md) › Files

# kernel/pspsysevent.h

## Data Structures

### `struct PspSysEventHandler`

```c
struct PspSysEventHandler {
    int size;
    char * name;
    int type_mask;
    int(* handler)(int ev_id, char *ev_name, void *param, int *result);
    int r28;
    int busy;
    _PspSysEventHandler * next;
    int reserved[9];
};
```

## Typedefs

### `_PspSysEventHandler`

```c
typedef struct PspSysEventHandler _PspSysEventHandler;
```

### `PspSysEventHandlerFunc`

```c
typedef int(* PspSysEventHandlerFunc) (int ev_id, char *ev_name, void *param, int *result))(int ev_id, char *ev_name, void *param, int *result);
```

### `PspSysEventHandler`

```c
typedef struct PspSysEventHandler PspSysEventHandler;
```

## Functions

### `sceKernelSysEventDispatch()`

```c
int sceKernelSysEventDispatch(int ev_type_mask, int ev_id, char *ev_name, void *param, int *result, int break_nonzero, PspSysEventHandler *break_handler);
```

Dispatch a SysEvent event.

**Parameters:**

- `ev_type_mask` – the event type mask
- `ev_id` – the event id
- `ev_name` – the event name
- `param` – the pointer to the custom parameters
- `result` – the pointer to the result
- `break_nonzero` – set to 1 to interrupt the calling chain after the first non-zero return
- `break_handler` – the pointer to the event handler having interrupted

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferSysEventHandler()`

```c
PspSysEventHandler * sceKernelReferSysEventHandler(void);
```

Get the first SysEvent handler (the rest can be found with the linked list).

**Returns:** 0 on error, handler on success

### `sceKernelIsRegisterSysEventHandler()`

```c
int sceKernelIsRegisterSysEventHandler(PspSysEventHandler *handler);
```

Check if a SysEvent handler is registered.

**Parameters:**

- `handler` – the handler to check

**Returns:** 0 if the handler is not registered

### `sceKernelRegisterSysEventHandler()`

```c
int sceKernelRegisterSysEventHandler(PspSysEventHandler *handler);
```

Register a SysEvent handler.

**Parameters:**

- `handler` – the handler to register

**Returns:** 0 on success, \< 0 on error

### `sceKernelUnregisterSysEventHandler()`

```c
int sceKernelUnregisterSysEventHandler(PspSysEventHandler *handler);
```

Unregister a SysEvent handler.

**Parameters:**

- `handler` – the handler to unregister

**Returns:** 0 on success, \< 0 on error

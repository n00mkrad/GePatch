[PSPSDK documentation](../../README.md) › Files

# kernel/pspexception.h

```c
#include <pspkerneltypes.h>
```

## Functions

### `sceKernelRegisterDefaultExceptionHandler()`

```c
int sceKernelRegisterDefaultExceptionHandler(void *func);
```

Register a default exception handler.

**Parameters:**

- `func` – Pointer to the exception handler function

**Note:** The exception handler function must start with a NOP

**Returns:** 0 on success, \< 0 on error

### `sceKernelRegisterExceptionHandler()`

```c
int sceKernelRegisterExceptionHandler(int exno, void *func);
```

Register a exception handler.

**Parameters:**

- `exno` – The exception number
- `func` – Pointer to the exception handler function

**Returns:** 0 on success, \< 0 on error

### `sceKernelRegisterPriorityExceptionHandler()`

```c
int sceKernelRegisterPriorityExceptionHandler(int exno, int priority, void *func);
```

Register a exception handler with a priority.

**Parameters:**

- `exno` – The exception number
- `priority` – The priority of the exception
- `func` – Pointer to the exception handler function

**Returns:** 0 on success, \< 0 on error

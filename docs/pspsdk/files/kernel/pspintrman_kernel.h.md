[PSPSDK documentation](../../README.md) › Files

# kernel/pspintrman_kernel.h

```c
#include <pspkerneltypes.h>
```

Topics: [Interrupt Manager Kernel](../../topics/IntrManKern.md)

## Functions

### `sceKernelRegisterIntrHandler()`

```c
int sceKernelRegisterIntrHandler(int intno, int no, void *handler, void *arg1, void *arg2);
```

Register an interrupt handler.

**Parameters:**

- `intno` – The interrupt number to register.
- `no` – The queue number.
- `handler` – Pointer to the handler.
- `arg1` – Unknown (probably a set of flags)
- `arg2` – Unknown (probably a common pointer)

**Returns:** 0 on success.

### `sceKernelReleaseIntrHandler()`

```c
int sceKernelReleaseIntrHandler(int intno);
```

Release an interrupt handler.

**Parameters:**

- `intno` – The interrupt number to release

**Returns:** 0 on success

### `sceKernelEnableIntr()`

```c
int sceKernelEnableIntr(int intno);
```

Enable an interrupt.

**Parameters:**

- `intno` – Interrupt to enable.

**Returns:** 0 on success.

### `sceKernelDisableIntr()`

```c
int sceKernelDisableIntr(int intno);
```

Disable an interrupt.

**Parameters:**

- `intno` – Interrupt to disable.

**Returns:** 0 on success.

### `sceKernelIsIntrContext()`

```c
int sceKernelIsIntrContext(void);
```

Check if we are in an interrupt context or not.

**Returns:** 1 if we are in an interrupt context, else 0

### `sceKernelQuerySystemCall()`

```c
int sceKernelQuerySystemCall(void *function);
```

Query system call number of `function`.

**Parameters:**

- `function` [in] – A function pointer of the function to get the syscall number.

**Returns:** System call number if `>= 0`, `< 0` on error.

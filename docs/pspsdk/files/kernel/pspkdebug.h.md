[PSPSDK documentation](../../README.md) › Files

# kernel/pspkdebug.h

```c
#include <pspkerneltypes.h>
```

Topics: [Interface to the KDebugForKernel library.](../../topics/Kdebug.md)

## Typedefs

### `PspDebugPutChar`

```c
typedef void(* PspDebugPutChar) (unsigned short *args, unsigned int ch))(unsigned short *args, unsigned int ch);
```

Typedef for the debug putcharacter handler.

## Functions

### `sceKernelRegisterDebugPutchar()`

```c
void sceKernelRegisterDebugPutchar(PspDebugPutChar func);
```

Register a debug put character handler.

**Parameters:**

- `func` – The put character function to register.

### `sceKernelGetDebugPutchar()`

```c
PspDebugPutChar sceKernelGetDebugPutchar(void);
```

Get the debug put character handler.

**Returns:** The current debug putchar handler

### `Kprintf()`

```c
void Kprintf(const char *format,...);
```

Kernel printf function.

**Parameters:**

- `format` – The format string.
- `...` – Arguments for the format string.

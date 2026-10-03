[PSPSDK documentation](../../README.md) › Files

# debug/sio.c

```c
#include <pspkernel.h>
#include <pspuser.h>
#include <pspkdebug.h>
#include <pspdebug.h>
#include <pspsyscon.h>
```

## Macros

### `PSP_UART4_FIFO`

```c
#define PSP_UART4_FIFO 0xBE500000
```

### `PSP_UART4_STAT`

```c
#define PSP_UART4_STAT 0xBE500018
```

### `PSP_UART4_DIV1`

```c
#define PSP_UART4_DIV1 0xBE500024
```

### `PSP_UART4_DIV2`

```c
#define PSP_UART4_DIV2 0xBE500028
```

### `PSP_UART4_CTRL`

```c
#define PSP_UART4_CTRL 0xBE50002C
```

### `PSP_UART_CLK`

```c
#define PSP_UART_CLK 96000000
```

### `PSP_UART_TXFULL`

```c
#define PSP_UART_TXFULL 0x20
```

### `PSP_UART_RXEMPTY`

```c
#define PSP_UART_RXEMPTY 0x10
```

## Functions

### `sceHprmEnd()`

```c
int sceHprmEnd(void);
```

### `sceSysregUartIoEnable()`

```c
int sceSysregUartIoEnable(int uart);
```

### `get_debug_register()`

```c
static u32 * get_debug_register(void);
```

### `PutCharDebug()`

```c
static void PutCharDebug(unsigned short *data, unsigned int type);
```

## Variables

### `g_enablekprintf`

```c
int g_enablekprintf = 0;
```

### `sceKernelRemoveByDebugSection`

```c
u32 sceKernelRemoveByDebugSection;
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugSioPutchar`](pspdebug.h.md#pspdebugsioputchar)
- [`pspDebugSioGetchar`](pspdebug.h.md#pspdebugsiogetchar)
- [`pspDebugSioPuts`](pspdebug.h.md#pspdebugsioputs)
- [`pspDebugSioPutData`](pspdebug.h.md#pspdebugsioputdata)
- [`pspDebugSioPutText`](pspdebug.h.md#pspdebugsioputtext)
- [`pspDebugSioSetBaud`](pspdebug.h.md#pspdebugsiosetbaud)
- [`pspDebugSioInit`](pspdebug.h.md#pspdebugsioinit)
- [`pspDebugEnablePutchar`](pspdebug.h.md#pspdebugenableputchar)
- [`pspDebugSioInstallKprintf`](pspdebug.h.md#pspdebugsioinstallkprintf)
- [`pspDebugSioEnableKprintf`](pspdebug.h.md#pspdebugsioenablekprintf)
- [`pspDebugSioDisableKprintf`](pspdebug.h.md#pspdebugsiodisablekprintf)

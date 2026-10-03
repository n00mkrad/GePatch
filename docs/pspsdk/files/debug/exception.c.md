[PSPSDK documentation](../../README.md) › Files

# debug/exception.c

```c
#include <pspkernel.h>
#include <pspdisplay.h>
#include <pspdebug.h>
```

## Functions

### `_pspDebugExceptionHandler()`

```c
void _pspDebugExceptionHandler(void);
```

### `sceKernelRegisterDefaultExceptionHandler()`

```c
int sceKernelRegisterDefaultExceptionHandler(void *func);
```

### `_pspDebugDefaultHandler()`

```c
static void _pspDebugDefaultHandler(PspDebugRegBlock *regs);
```

### `_pspDebugTrapEntry()`

```c
void _pspDebugTrapEntry(void);
```

The entry point for our exception "trap".

## Variables

### `curr_handler`

```c
PspDebugErrorHandler curr_handler = NULL;
```

### `_pspDebugExceptRegs`

```c
PspDebugRegBlock _pspDebugExceptRegs;
```

### `regName`

```c
const unsigned char regName[32][5][32][5] =
{
    "zr", "at", "v0", "v1", "a0", "a1", "a2", "a3",
    "t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",
    "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7",
    "t8", "t9", "k0", "k1", "gp", "sp", "fp", "ra"
};
```

### `codeTxt`

```c
const char* codeTxt[32][32] =
{
	"Interrupt", "TLB modification", "TLB load/inst fetch", "TLB store",
	"Address load/inst fetch", "Address store", "Bus error (instr)",
	"Bus error (data)", "Syscall", "Breakpoint", "Reserved instruction",
	"Coprocessor unusable", "Arithmetic overflow", "Unknown 13", "Unknown 14",
	"FPU Exception", "Unknown 16", "Unknown 17", "Unknown 18",
	"Unknown 20", "Unknown 21", "Unknown 22", "Unknown 23",
	"Unknown 24", "Unknown 25", "Unknown 26", "Unknown 27",
	"Unknown 28", "Unknown 29", "Unknown 30", "Unknown 31"
};
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugInstallErrorHandler`](pspdebug.h.md#pspdebuginstallerrorhandler)
- [`pspDebugDumpException`](pspdebug.h.md#pspdebugdumpexception)

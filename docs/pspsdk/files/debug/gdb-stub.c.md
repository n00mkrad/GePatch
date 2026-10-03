[PSPSDK documentation](../../README.md) › Files

# debug/gdb-stub.c

```c
#include <pspiofilemgr.h>
#include <pspuser.h>
#include <pspdebug.h>
#include <string.h>
#include <signal.h>
```

## Data Structures

### `struct sw_breakpoint`

```c
struct sw_breakpoint {
    unsigned int addr;
    unsigned int oldinst;
    unsigned int active;
};
```

### `struct hard_trap_info`

```c
struct hard_trap_info {
    unsigned char tt;
    unsigned char signo;
};
```

## Macros

### `DEBUG_PRINTF()`

```c
#define DEBUG_PRINTF(fmt, ...)
```

### `MAX_BUF`

```c
#define MAX_BUF 2048
```

### `SW_BREAK_INST`

```c
#define SW_BREAK_INST 0x0000000d
```

### `BEQ_OPCODE`

```c
#define BEQ_OPCODE 0x4
```

### `BEQL_OPCODE`

```c
#define BEQL_OPCODE 0x14
```

### `BGTZ_OPCODE`

```c
#define BGTZ_OPCODE 0x7
```

### `BGTZL_OPCODE`

```c
#define BGTZL_OPCODE 0x17
```

### `BLEZ_OPCODE`

```c
#define BLEZ_OPCODE 0x6
```

### `BLEZL_OPCODE`

```c
#define BLEZL_OPCODE 0x16
```

### `BNE_OPCODE`

```c
#define BNE_OPCODE 0x5
```

### `BNEL_OPCODE`

```c
#define BNEL_OPCODE 0x15
```

### `REGIMM_OPCODE`

```c
#define REGIMM_OPCODE 0x1
```

### `BGEZ_OPCODE`

```c
#define BGEZ_OPCODE 0x1
```

### `BGEZAL_OPCODE`

```c
#define BGEZAL_OPCODE 0x11
```

### `BGEZALL_OPCODE`

```c
#define BGEZALL_OPCODE 0x13
```

### `BGEZL_OPCODE`

```c
#define BGEZL_OPCODE 0x3
```

### `BLTZ_OPCODE`

```c
#define BLTZ_OPCODE 0
```

### `BLTZAL_OPCODE`

```c
#define BLTZAL_OPCODE 0x10
```

### `BLTZALL_OPCODE`

```c
#define BLTZALL_OPCODE 0x12
```

### `BLTZL_OPCODE`

```c
#define BLTZL_OPCODE 0x2
```

### `J_OPCODE`

```c
#define J_OPCODE 0x2
```

### `JAL_OPCODE`

```c
#define JAL_OPCODE 0x3
```

### `SPECIAL_OPCODE`

```c
#define SPECIAL_OPCODE 0
```

### `JALR_OPCODE`

```c
#define JALR_OPCODE 0x9
```

### `JR_OPCODE`

```c
#define JR_OPCODE 0x8
```

### `COP0_OPCODE`

```c
#define COP0_OPCODE 0x10
```

### `COP1_OPCODE`

```c
#define COP1_OPCODE 0x11
```

### `COP2_OPCODE`

```c
#define COP2_OPCODE 0x12
```

### `BCXF_OPCODE`

```c
#define BCXF_OPCODE 0x100
```

### `BCXFL_OPCODE`

```c
#define BCXFL_OPCODE 0x102
```

### `BCXT_OPCODE`

```c
#define BCXT_OPCODE 0x101
```

### `BCXTL_OPCODE`

```c
#define BCXTL_OPCODE 0x103
```

## Functions

### `pspDebugBreakpoint()`

```c
void pspDebugBreakpoint(void);
```

### `putDebugChar()`

```c
void putDebugChar(char ch);
```

### `getDebugChar()`

```c
char getDebugChar(void);
```

### `_gdbSupportLibWriteByte()`

```c
int _gdbSupportLibWriteByte(char val, unsigned char *dest);
```

### `_gdbSupportLibReadByte()`

```c
int _gdbSupportLibReadByte(unsigned char *address, unsigned char *dest);
```

### `pspDebugResumeFromException()`

```c
void pspDebugResumeFromException(void);
```

### `_gdbSupportLibFlushCaches()`

```c
void _gdbSupportLibFlushCaches(void);
```

### `sceKernelSuspendIntr()`

```c
int sceKernelSuspendIntr(void);
```

### `sceKernelResumeIntr()`

```c
void sceKernelResumeIntr(int intr);
```

### `handle_exception()`

```c
static void handle_exception(PspDebugRegBlock *regs);
```

### `_GdbExceptionHandler()`

```c
void _GdbExceptionHandler(void);
```

### `putpacket()`

```c
static void putpacket(unsigned char *buffer);
```

### `get_char()`

```c
static char get_char(void);
```

### `stdout_handler()`

```c
static int stdout_handler(const char *data, int len);
```

### `hex()`

```c
static int hex(unsigned char ch);
```

### `getpacket()`

```c
static void getpacket(char *buffer);
```

### `computeSignal()`

```c
static int computeSignal(int tt);
```

### `_GdbTrapEntry()`

```c
static void _GdbTrapEntry(PspDebugRegBlock *regs);
```

### `_gdbSupportLibInit()`

```c
int _gdbSupportLibInit(void);
```

### `mem2hex()`

```c
static char * mem2hex(unsigned char *mem, char *buf, int count);
```

### `hex2mem()`

```c
static char * hex2mem(char *buf, char *mem, int count, int binary);
```

### `hexToInt()`

```c
static int hexToInt(char **ptr, unsigned int *intValue);
```

### `step_generic()`

```c
static void step_generic(PspDebugRegBlock *regs, int skip);
```

### `build_trap_cmd()`

```c
void build_trap_cmd(int sigval, PspDebugRegBlock *regs);
```

### `handle_query()`

```c
static void handle_query(char *str);
```

### `asm()`

```c
asm(".global pspDebugBreakpoint\n" ".set noreorder\n" "pspDebugBreakpoint:\tbreak\n" "jr $31\n" "nop\n");
```

## Variables

### `_pspDebugResumePatch`

```c
u32 _pspDebugResumePatch;
```

### `_GdbExceptRegs`

```c
PspDebugRegBlock* _GdbExceptRegs;
```

### `initialised`

```c
int initialised = 0;
```

### `input`

```c
char input[2048][2048];
```

### `output`

```c
char output[2048][2048];
```

### `hexchars`

```c
const char hexchars[][] ="0123456789abcdef";
```

### `last_cmd`

```c
char last_cmd = 0;
```

### `attached`

```c
int attached = 0;
```

### `g_stepbp`

```c
struct sw_breakpoint g_stepbp[2][2];
```

### `hard_trap_info`

```c
struct hard_trap_info hard_trap_info[][] = {
	{ 6, SIGBUS },
	{ 7, SIGBUS },
	{ 9, SIGTRAP },
	{ 10, SIGILL },
	{ 12, SIGFPE },
	{ 13, SIGTRAP },
	{ 14, SIGSEGV },
	{ 15, SIGFPE },
	{ 23, SIGSEGV },
	{ 31, SIGSEGV },
	{ 0, 0}
};
```

**Also defined in this file** (documented with the declaration):

- [`pspDebugGdbStubInit`](pspdebug.h.md#pspdebuggdbstubinit)

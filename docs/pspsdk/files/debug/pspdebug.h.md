[PSPSDK documentation](../../README.md) › Files

# debug/pspdebug.h

```c
#include <psptypes.h>
#include <pspmoduleinfo.h>
```

Topics: [Debug Utility Library](../../topics/Debug.md)

## Data Structures

### `struct _PspDebugRegBlock`

Structure to hold the register data associated with an exception.

| Field | Description |
|---|---|
| `u32 frame[6]` |  |
| `u32 r[32]` | Array of the 32 GPRs. |
| `u32 status` | The status register. |
| `u32 lo` | lo |
| `u32 hi` |  |
| `u32 badvaddr` |  |
| `u32 cause` |  |
| `u32 epc` |  |
| `float fpr[32]` |  |
| `u32 fsr` |  |
| `u32 fir` |  |
| `u32 frame_ptr` |  |
| `u32 unused` |  |
| `u32 index` |  |
| `u32 random` |  |
| `u32 entrylo0` |  |
| `u32 entrylo1` |  |
| `u32 context` |  |
| `u32 pagemask` |  |
| `u32 wired` |  |
| `u32 cop0_7` |  |
| `u32 cop0_8` |  |
| `u32 cop0_9` |  |
| `u32 entryhi` |  |
| `u32 cop0_11` |  |
| `u32 cop0_12` |  |
| `u32 cop0_13` |  |
| `u32 cop0_14` |  |
| `u32 prid` |  |
| `u32 padding[100]` |  |

### `struct _PspDebugStackTrace`

Structure to hold a single stack trace entry.

| Field | Description |
|---|---|
| `u32 call_addr` | The address which called the function. |
| `u32 func_addr` | The address of the function called. |

### `struct _PspDebugProfilerRegs`

Structure to hold the psp profiler register values.

```c
struct _PspDebugProfilerRegs {
    volatile u32 enable;
    volatile u32 systemck;
    volatile u32 cpuck;
    volatile u32 internal;
    volatile u32 memory;
    volatile u32 copz;
    volatile u32 vfpu;
    volatile u32 sleep;
    volatile u32 bus_access;
    volatile u32 uncached_load;
    volatile u32 uncached_store;
    volatile u32 cached_load;
    volatile u32 cached_store;
    volatile u32 i_miss;
    volatile u32 d_miss;
    volatile u32 d_writeback;
    volatile u32 cop0_inst;
    volatile u32 fpu_inst;
    volatile u32 vfpu_inst;
    volatile u32 local_bus;
};
```

## Typedefs

### `PspDebugRegBlock`

```c
typedef struct _PspDebugRegBlock PspDebugRegBlock;
```

Structure to hold the register data associated with an exception.

### `PspDebugErrorHandler`

```c
typedef void(* PspDebugErrorHandler) (PspDebugRegBlock *regs))(PspDebugRegBlock *regs);
```

Defines a debug error handler.

### `PspDebugKprintfHandler`

```c
typedef int(* PspDebugKprintfHandler) (const char *format, u32 *args))(const char *format, u32 *args);
```

Type for Kprintf handler.

### `PspDebugStackTrace`

```c
typedef struct _PspDebugStackTrace PspDebugStackTrace;
```

Structure to hold a single stack trace entry.

### `PspDebugProfilerRegs`

```c
typedef struct _PspDebugProfilerRegs PspDebugProfilerRegs;
```

Structure to hold the psp profiler register values.

### `PspDebugPrintHandler`

```c
typedef int(* PspDebugPrintHandler) (const char *data, int len))(const char *data, int len);
```

Type for the debug print handlers.

### `PspDebugInputHandler`

```c
typedef int(* PspDebugInputHandler) (char *data, int len))(char *data, int len);
```

Type for the debug input handler.

## Functions

### `pspDebugScreenInit()`

```c
void pspDebugScreenInit(void);
```

Initialise the debug screen.

### `pspDebugScreenInitEx()`

```c
void pspDebugScreenInitEx(void *vram_base, int mode, int setup);
```

Extended debug screen init.

**Parameters:**

- `vram_base` – Base address of frame buffer, if NULL then sets a default
- `mode` – Colour mode
- `setup` – Setup the screen if 1

### `pspDebugScreenPrintf()`

```c
void pspDebugScreenPrintf(const char *fmt,...);
```

Do a printf to the debug screen.

**Parameters:**

- `fmt` – Format string to print
- `...` – Arguments

### `pspDebugScreenKprintf()`

```c
void pspDebugScreenKprintf(const char *format,...);
```

Do a printf to the debug screen.

**Note:** This is for kernel mode only as it uses a kernel function to perform the printf instead of using vsnprintf, use normal printf for user mode.

**Parameters:**

- `format` – Format string to print
- `...` – Arguments

### `pspDebugScreenEnableBackColor()`

```c
void pspDebugScreenEnableBackColor(int enable);
```

Enable or disable background colour writing (defaults to enabled)

**Parameters:**

- `enable` – Set 1 to to enable background color, 0 for disable

### `pspDebugScreenSetBackColor()`

```c
void pspDebugScreenSetBackColor(u32 color);
```

Set the background color for the text.

**Note:** To reset the entire screens bg colour you need to call pspDebugScreenClear

**Parameters:**

- `color` – A 32bit RGB colour

### `pspDebugScreenSetTextColor()`

```c
void pspDebugScreenSetTextColor(u32 color);
```

Set the text color.

**Parameters:**

- `color` – A 32 bit BGR color

### `pspDebugScreenSetColorMode()`

```c
void pspDebugScreenSetColorMode(int mode);
```

Set the color mode (you must have switched the frame buffer appropriately)

**Parameters:**

- `mode` – Color mode

### `pspDebugScreenPutChar()`

```c
void pspDebugScreenPutChar(int x, int y, u32 color, u8 ch);
```

Draw a single character to the screen.

**Parameters:**

- `x` – The x co-ordinate to draw to (pixel units)
- `y` – The y co-ordinate to draw to (pixel units)
- `color` – The text color to draw
- `ch` – The character to draw

### `pspDebugScreenSetXY()`

```c
void pspDebugScreenSetXY(int x, int y);
```

Set the current X and Y co-ordinate for the screen (in character units)

### `pspDebugScreenSetOffset()`

```c
void pspDebugScreenSetOffset(int offset);
```

Set the video ram offset used for the screen.

**Parameters:**

- `offset` – Offset in bytes

### `pspDebugScreenSetBase()`

```c
void pspDebugScreenSetBase(u32 *base);
```

Set the video ram base used for the screen.

**Parameters:**

- `base` – Base address in bytes

### `pspDebugScreenGetX()`

```c
int pspDebugScreenGetX(void);
```

Get the current X co-ordinate (in character units)

**Returns:** The X co-ordinate

### `pspDebugScreenGetY()`

```c
int pspDebugScreenGetY(void);
```

Get the current Y co-ordinate (in character units)

**Returns:** The Y co-ordinate

### `pspDebugScreenClear()`

```c
void pspDebugScreenClear(void);
```

Clear the debug screen.

### `pspDebugScreenPrintData()`

```c
int pspDebugScreenPrintData(const char *buff, int size);
```

Print non-nul terminated strings.

**Parameters:**

- `buff` – Buffer containing the text.
- `size` – Size of the data

**Returns:** The number of characters written

### `pspDebugScreenPuts()`

```c
int pspDebugScreenPuts(const char *str);
```

Print a string.

**Parameters:**

- `str` – String

**Returns:** The number of characters written

### `pspDebugGetStackTrace()`

```c
int pspDebugGetStackTrace(unsigned int *results, int max);
```

Get a MIPS stack trace (might work :P)

**Parameters:**

- `results` – List of points to store the results of the trace, (up to max)
- `max` – Maximum number of back traces

**Returns:** The number of frames stored in results.

### `pspDebugScreenClearLineEnable()`

```c
void pspDebugScreenClearLineEnable(void);
```

Enable the clear line function that allows debug to clear the screen.

### `pspDebugScreenClearLineDisable()`

```c
void pspDebugScreenClearLineDisable(void);
```

Disable the clear line function that causes flicker on constant refreshes.

### `pspDebugInstallErrorHandler()`

```c
int pspDebugInstallErrorHandler(PspDebugErrorHandler handler);
```

Install an error handler to catch unhandled exceptions.

**Parameters:**

- `handler` – Pointer to a handler function. If set to NULL it will default to resetting the screen and dumping the error.

**Returns:** \< 0 on error

### `pspDebugDumpException()`

```c
void pspDebugDumpException(PspDebugRegBlock *regs);
```

Dump an exception to screen using the pspDebugScreen functions.

**Note:** This function will not setup the screen for debug output, you should call sceDebugScreenInit before using it if it isn't already.

**Parameters:**

- `regs` – Pointer to a register block.

### `pspDebugInstallKprintfHandler()`

```c
int pspDebugInstallKprintfHandler(PspDebugKprintfHandler handler);
```

Install a Kprintf handler into the system.

**Parameters:**

- `handler` – Function pointer to the handler.

**Returns:** \< 0 on error.

### `pspDebugGetStackTrace2()`

```c
int pspDebugGetStackTrace2(PspDebugRegBlock *regs, PspDebugStackTrace *trace, int max);
```

Do a stack trace from the current exception.

**Note:** This function really isn't too general purpose and it is more than likely to generate a few false positives but I consider that better then missing out calls entirely. You have to use your discretion, your code and a objdump to work out if some calls are completely surprious or not ;)

**Parameters:**

- `regs` – Pointer to a register block from an exception.
- `trace` – Pointer to an array of PspDebugStackTrace structures.
- `max` – The maximum number of traces to make.

**Returns:** The number of functions found.

### `pspDebugProfilerEnable()`

```c
void pspDebugProfilerEnable(void);
```

Enables the profiler hardware.

### `pspDebugProfilerDisable()`

```c
void pspDebugProfilerDisable(void);
```

Disables the profiler hardware.

### `pspDebugProfilerClear()`

```c
void pspDebugProfilerClear(void);
```

Clear the profiler registers.

### `pspDebugProfilerGetRegs()`

```c
void pspDebugProfilerGetRegs(PspDebugProfilerRegs *regs);
```

Get the profiler register state.

**Parameters:**

- `regs` – A pointer to a PspDebugProfilerRegs structure.

### `pspDebugProfilerPrint()`

```c
void pspDebugProfilerPrint(void);
```

Print the profiler registers to screen.

### `pspDebugInstallStdinHandler()`

```c
int pspDebugInstallStdinHandler(PspDebugInputHandler handler);
```

Install a handler for stdin (so you can use normal stdio functions)

**Parameters:**

- `handler` – A pointer to input handler, NULL to disable.

**Returns:** \< 0 on error, else 0.

### `pspDebugInstallStdoutHandler()`

```c
int pspDebugInstallStdoutHandler(PspDebugPrintHandler handler);
```

Install a print handler for stdout (so you can use normal print functions)

**Parameters:**

- `handler` – A pointer to print handler, NULL to disable.

**Returns:** \< 0 on error, else 0.

### `pspDebugInstallStderrHandler()`

```c
int pspDebugInstallStderrHandler(PspDebugPrintHandler handler);
```

Install a print handler for stderr (so you can use normal print functions)

**Parameters:**

- `handler` – A pointer to print handler, NULL to disable.

**Returns:** \< 0 on error, else 0.

### `pspDebugSioPutchar()`

```c
void pspDebugSioPutchar(int ch);
```

Put a character to the remote sio.

**Parameters:**

- `ch` – Character to write.

### `pspDebugSioGetchar()`

```c
int pspDebugSioGetchar(void);
```

Get a character from the remote sio.

**Returns:** The character read or -1 if no characters available.

### `pspDebugSioPuts()`

```c
void pspDebugSioPuts(const char *str);
```

Write a string to the sio port.

**Parameters:**

- `str` – String to write.

### `pspDebugSioPutData()`

```c
int pspDebugSioPutData(const char *data, int len);
```

Write a set of data to the sio port.

**Parameters:**

- `data` – Pointer to the data to send.
- `len` – Length of the data.

**Returns:** Number of characters written.

### `pspDebugSioPutText()`

```c
int pspDebugSioPutText(const char *data, int len);
```

Write a set of data to the sio port converting single line feeds to CRLF and single CR to CRLF.

**Parameters:**

- `data` – Pointer to the data to send.
- `len` – Length of the data.

**Returns:** Number of characters written.

### `pspDebugSioInit()`

```c
void pspDebugSioInit(void);
```

Initialise the remote SIO port (defaults to 4800 8N1).

**Note:** will delay 2 seconds to wait for the power to come up.

### `pspDebugSioSetBaud()`

```c
void pspDebugSioSetBaud(int baud);
```

Set the baud rate of the SIO, e.g.

4800/9600..115200.

**Parameters:**

- `baud` – The baudrate to set.

### `pspDebugEnablePutchar()`

```c
void pspDebugEnablePutchar(void);
```

Enable debug character output.

Needs to be called in order for the default Kprintf handler to work.

### `pspDebugSioInstallKprintf()`

```c
void pspDebugSioInstallKprintf(void);
```

Install a kprintf debug putchar handler.

Implicitly calls [pspDebugEnablePutchar](#pspdebugenableputchar) so you do not need to call it explicitly. Sio must be initialised before calling this function however.

### `pspDebugGdbStubInit()`

```c
void pspDebugGdbStubInit(void);
```

Install the gdb stub handler.

### `pspDebugBreakpoint()`

```c
void pspDebugBreakpoint(void);
```

Generate a breakpoint exception.

### `pspDebugSioEnableKprintf()`

```c
void pspDebugSioEnableKprintf(void);
```

Enable the kprintf handler (once installed)

### `pspDebugSioDisableKprintf()`

```c
void pspDebugSioDisableKprintf(void);
```

Disable the kprintf handler (once installed)

### `pspScreenshotSave()`

```c
int pspScreenshotSave(const char *filename);
```

Save a screenshot to a file.

**Parameters:**

- `filename` – The filename to save the screenshot for the current frame buffer displayed on the screen. The filename will be saved with a BMP extension.

**Returns:** 0 on success, -1 on error

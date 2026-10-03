[PSPSDK documentation](../README.md) › Topics

# Debug Utility Library

Headers: [`debug/pspdebug.h`](../files/debug/pspdebug.h.md)

## Data Structures

- [`struct _PspDebugRegBlock`](../files/debug/pspdebug.h.md#struct-_pspdebugregblock) – Structure to hold the register data associated with an exception.
- [`struct _PspDebugStackTrace`](../files/debug/pspdebug.h.md#struct-_pspdebugstacktrace) – Structure to hold a single stack trace entry.
- [`struct _PspDebugProfilerRegs`](../files/debug/pspdebug.h.md#struct-_pspdebugprofilerregs) – Structure to hold the psp profiler register values.

## Typedefs

- [`PspDebugRegBlock`](../files/debug/pspdebug.h.md#pspdebugregblock) – Structure to hold the register data associated with an exception.
- [`PspDebugErrorHandler`](../files/debug/pspdebug.h.md#pspdebugerrorhandler) – Defines a debug error handler.
- [`PspDebugKprintfHandler`](../files/debug/pspdebug.h.md#pspdebugkprintfhandler) – Type for Kprintf handler.
- [`PspDebugStackTrace`](../files/debug/pspdebug.h.md#pspdebugstacktrace) – Structure to hold a single stack trace entry.
- [`PspDebugProfilerRegs`](../files/debug/pspdebug.h.md#pspdebugprofilerregs) – Structure to hold the psp profiler register values.
- [`PspDebugPrintHandler`](../files/debug/pspdebug.h.md#pspdebugprinthandler) – Type for the debug print handlers.
- [`PspDebugInputHandler`](../files/debug/pspdebug.h.md#pspdebuginputhandler) – Type for the debug input handler.

## Functions

- [`pspDebugScreenInit()`](../files/debug/pspdebug.h.md#pspdebugscreeninit) – Initialise the debug screen.
- [`pspDebugScreenInitEx()`](../files/debug/pspdebug.h.md#pspdebugscreeninitex) – Extended debug screen init.
- [`pspDebugScreenPrintf()`](../files/debug/pspdebug.h.md#pspdebugscreenprintf) – Do a printf to the debug screen.
- [`pspDebugScreenKprintf()`](../files/debug/pspdebug.h.md#pspdebugscreenkprintf) – Do a printf to the debug screen.
- [`pspDebugScreenEnableBackColor()`](../files/debug/pspdebug.h.md#pspdebugscreenenablebackcolor) – Enable or disable background colour writing (defaults to enabled)
- [`pspDebugScreenSetBackColor()`](../files/debug/pspdebug.h.md#pspdebugscreensetbackcolor) – Set the background color for the text.
- [`pspDebugScreenSetTextColor()`](../files/debug/pspdebug.h.md#pspdebugscreensettextcolor) – Set the text color.
- [`pspDebugScreenSetColorMode()`](../files/debug/pspdebug.h.md#pspdebugscreensetcolormode) – Set the color mode (you must have switched the frame buffer appropriately)
- [`pspDebugScreenPutChar()`](../files/debug/pspdebug.h.md#pspdebugscreenputchar) – Draw a single character to the screen.
- [`pspDebugScreenSetXY()`](../files/debug/pspdebug.h.md#pspdebugscreensetxy) – Set the current X and Y co-ordinate for the screen (in character units)
- [`pspDebugScreenSetOffset()`](../files/debug/pspdebug.h.md#pspdebugscreensetoffset) – Set the video ram offset used for the screen.
- [`pspDebugScreenSetBase()`](../files/debug/pspdebug.h.md#pspdebugscreensetbase) – Set the video ram base used for the screen.
- [`pspDebugScreenGetX()`](../files/debug/pspdebug.h.md#pspdebugscreengetx) – Get the current X co-ordinate (in character units)
- [`pspDebugScreenGetY()`](../files/debug/pspdebug.h.md#pspdebugscreengety) – Get the current Y co-ordinate (in character units)
- [`pspDebugScreenClear()`](../files/debug/pspdebug.h.md#pspdebugscreenclear) – Clear the debug screen.
- [`pspDebugScreenPrintData()`](../files/debug/pspdebug.h.md#pspdebugscreenprintdata) – Print non-nul terminated strings.
- [`pspDebugScreenPuts()`](../files/debug/pspdebug.h.md#pspdebugscreenputs) – Print a string.
- [`pspDebugGetStackTrace()`](../files/debug/pspdebug.h.md#pspdebuggetstacktrace) – Get a MIPS stack trace (might work :P)
- [`pspDebugScreenClearLineEnable()`](../files/debug/pspdebug.h.md#pspdebugscreenclearlineenable) – Enable the clear line function that allows debug to clear the screen.
- [`pspDebugScreenClearLineDisable()`](../files/debug/pspdebug.h.md#pspdebugscreenclearlinedisable) – Disable the clear line function that causes flicker on constant refreshes.
- [`pspDebugInstallErrorHandler()`](../files/debug/pspdebug.h.md#pspdebuginstallerrorhandler) – Install an error handler to catch unhandled exceptions.
- [`pspDebugDumpException()`](../files/debug/pspdebug.h.md#pspdebugdumpexception) – Dump an exception to screen using the pspDebugScreen functions.
- [`pspDebugInstallKprintfHandler()`](../files/debug/pspdebug.h.md#pspdebuginstallkprintfhandler) – Install a Kprintf handler into the system.
- [`pspDebugGetStackTrace2()`](../files/debug/pspdebug.h.md#pspdebuggetstacktrace2) – Do a stack trace from the current exception.
- [`pspDebugProfilerEnable()`](../files/debug/pspdebug.h.md#pspdebugprofilerenable) – Enables the profiler hardware.
- [`pspDebugProfilerDisable()`](../files/debug/pspdebug.h.md#pspdebugprofilerdisable) – Disables the profiler hardware.
- [`pspDebugProfilerClear()`](../files/debug/pspdebug.h.md#pspdebugprofilerclear) – Clear the profiler registers.
- [`pspDebugProfilerGetRegs()`](../files/debug/pspdebug.h.md#pspdebugprofilergetregs) – Get the profiler register state.
- [`pspDebugProfilerPrint()`](../files/debug/pspdebug.h.md#pspdebugprofilerprint) – Print the profiler registers to screen.
- [`pspDebugInstallStdinHandler()`](../files/debug/pspdebug.h.md#pspdebuginstallstdinhandler) – Install a handler for stdin (so you can use normal stdio functions)
- [`pspDebugInstallStdoutHandler()`](../files/debug/pspdebug.h.md#pspdebuginstallstdouthandler) – Install a print handler for stdout (so you can use normal print functions)
- [`pspDebugInstallStderrHandler()`](../files/debug/pspdebug.h.md#pspdebuginstallstderrhandler) – Install a print handler for stderr (so you can use normal print functions)
- [`pspDebugSioPutchar()`](../files/debug/pspdebug.h.md#pspdebugsioputchar) – Put a character to the remote sio.
- [`pspDebugSioGetchar()`](../files/debug/pspdebug.h.md#pspdebugsiogetchar) – Get a character from the remote sio.
- [`pspDebugSioPuts()`](../files/debug/pspdebug.h.md#pspdebugsioputs) – Write a string to the sio port.
- [`pspDebugSioPutData()`](../files/debug/pspdebug.h.md#pspdebugsioputdata) – Write a set of data to the sio port.
- [`pspDebugSioPutText()`](../files/debug/pspdebug.h.md#pspdebugsioputtext) – Write a set of data to the sio port converting single line feeds to CRLF and single CR to CRLF.
- [`pspDebugSioInit()`](../files/debug/pspdebug.h.md#pspdebugsioinit) – Initialise the remote SIO port (defaults to 4800 8N1).
- [`pspDebugSioSetBaud()`](../files/debug/pspdebug.h.md#pspdebugsiosetbaud) – Set the baud rate of the SIO, e.g.
- [`pspDebugEnablePutchar()`](../files/debug/pspdebug.h.md#pspdebugenableputchar) – Enable debug character output.
- [`pspDebugSioInstallKprintf()`](../files/debug/pspdebug.h.md#pspdebugsioinstallkprintf) – Install a kprintf debug putchar handler.
- [`pspDebugGdbStubInit()`](../files/debug/pspdebug.h.md#pspdebuggdbstubinit) – Install the gdb stub handler.
- [`pspDebugBreakpoint()`](../files/debug/pspdebug.h.md#pspdebugbreakpoint) – Generate a breakpoint exception.
- [`pspDebugSioEnableKprintf()`](../files/debug/pspdebug.h.md#pspdebugsioenablekprintf) – Enable the kprintf handler (once installed)
- [`pspDebugSioDisableKprintf()`](../files/debug/pspdebug.h.md#pspdebugsiodisablekprintf) – Disable the kprintf handler (once installed)
- [`pspScreenshotSave()`](../files/debug/pspdebug.h.md#pspscreenshotsave) – Save a screenshot to a file.

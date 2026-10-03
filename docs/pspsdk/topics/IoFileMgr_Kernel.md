[PSPSDK documentation](../README.md) › Topics

# Driver interface to IoFileMgr

This module contains the imports for the kernel's IO routines.

Headers: [`kernel/pspiofilemgr_kernel.h`](../files/kernel/pspiofilemgr_kernel.h.md)

## Data Structures

- [`struct PspIoDrvArg`](../files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvarg) – Structure passed to the init and exit functions of the io driver system.
- [`struct PspIoDrvFileArg`](../files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvfilearg) – Structure passed to the file functions of the io driver system.
- [`struct PspIoDrvFuncs`](../files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvfuncs) – Structure to maintain the file driver pointers.
- [`struct PspIoDrv`](../files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrv)

## Typedefs

- [`PspIoDrvArg`](../files/kernel/pspiofilemgr_kernel.h.md#pspiodrvarg) – Structure passed to the init and exit functions of the io driver system.
- [`PspIoDrvFileArg`](../files/kernel/pspiofilemgr_kernel.h.md#pspiodrvfilearg) – Structure passed to the file functions of the io driver system.
- [`PspIoDrvFuncs`](../files/kernel/pspiofilemgr_kernel.h.md#pspiodrvfuncs) – Structure to maintain the file driver pointers.
- [`PspIoDrv`](../files/kernel/pspiofilemgr_kernel.h.md#pspiodrv)

## Functions

- [`sceIoAddDrv()`](../files/kernel/pspiofilemgr_kernel.h.md#sceioadddrv) – Adds a new IO driver to the system.
- [`sceIoDelDrv()`](../files/kernel/pspiofilemgr_kernel.h.md#sceiodeldrv) – Deletes a IO driver from the system.
- [`sceIoReopen()`](../files/kernel/pspiofilemgr_kernel.h.md#sceioreopen) – Reopens an existing file descriptor.
- [`sceIoGetThreadCwd()`](../files/kernel/pspiofilemgr_kernel.h.md#sceiogetthreadcwd) – Get the current working directory for a thread.
- [`sceIoChangeThreadCwd()`](../files/kernel/pspiofilemgr_kernel.h.md#sceiochangethreadcwd) – Set the current working directory for a thread.

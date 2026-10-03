[PSPSDK documentation](../README.md) › Topics

# UMD Kernel Library

This module contains the imports for UMD drive.

Headers: [`umd/pspumd.h`](../files/umd/pspumd.h.md)

## Data Structures

- [`struct pspUmdInfo`](../files/umd/pspumd.h.md#struct-pspumdinfo) – UMD Info struct.

## Typedefs

- [`pspUmdInfo`](../files/umd/pspumd.h.md#pspumdinfo) – UMD Info struct.
- [`UmdCallback`](../files/umd/pspumd.h.md#umdcallback) – UMD Callback function.

## Enumerations

- [`pspUmdTypes`](../files/umd/pspumd.h.md#enum-pspumdtypes) – Enumeration for UMD types.
- [`pspUmdState`](../files/umd/pspumd.h.md#enum-pspumdstate) – Enumeration for UMD drive state.
- [`UmdDriveStat`](../files/umd/pspumd.h.md#enum-umddrivestat) – Enumeration for UMD stats (legacy)

## Functions

- [`sceUmdCheckMedium()`](../files/umd/pspumd.h.md#sceumdcheckmedium) – Check whether there is a disc in the UMD drive.
- [`sceUmdGetDiscInfo()`](../files/umd/pspumd.h.md#sceumdgetdiscinfo) – Get the disc info.
- [`sceUmdActivate()`](../files/umd/pspumd.h.md#sceumdactivate) – Activates the UMD drive.
- [`sceUmdDeactivate()`](../files/umd/pspumd.h.md#sceumddeactivate) – Deativates the UMD drive.
- [`sceUmdWaitDriveStat()`](../files/umd/pspumd.h.md#sceumdwaitdrivestat) – Wait for the UMD drive to reach a certain state.
- [`sceUmdWaitDriveStatWithTimer()`](../files/umd/pspumd.h.md#sceumdwaitdrivestatwithtimer) – Wait for the UMD drive to reach a certain state.
- [`sceUmdWaitDriveStatCB()`](../files/umd/pspumd.h.md#sceumdwaitdrivestatcb) – Wait for the UMD drive to reach a certain state (plus callback)
- [`sceUmdCancelWaitDriveStat()`](../files/umd/pspumd.h.md#sceumdcancelwaitdrivestat) – Cancel a sceUmdWait\* call.
- [`sceUmdGetDriveStat()`](../files/umd/pspumd.h.md#sceumdgetdrivestat) – Get (poll) the current state of the UMD drive.
- [`sceUmdSetDriveStatus()`](../files/umd/pspumd.h.md#sceumdsetdrivestatus) – Sets the current state of the UMD drive.
- [`sceUmdGetErrorStat()`](../files/umd/pspumd.h.md#sceumdgeterrorstat) – Get the error code associated with a failed event.
- [`sceUmdRegisterUMDCallBack()`](../files/umd/pspumd.h.md#sceumdregisterumdcallback) – Register a callback for the UMD drive.
- [`sceUmdUnRegisterUMDCallBack()`](../files/umd/pspumd.h.md#sceumdunregisterumdcallback) – Un-register a callback for the UMD drive.
- [`sceUmdReplacePermit()`](../files/umd/pspumd.h.md#sceumdreplacepermit) – Permit UMD disc being replaced.
- [`sceUmdReplaceProhibit()`](../files/umd/pspumd.h.md#sceumdreplaceprohibit) – Prohibit UMD disc being replaced.

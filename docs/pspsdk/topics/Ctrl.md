[PSPSDK documentation](../README.md) › Topics

# Controller Kernel Library

This module contains the imports for controllers (buttons, pad).

Headers: [`ctrl/pspctrl.h`](../files/ctrl/pspctrl.h.md)

## Data Structures

- [`struct SceCtrlData`](../files/ctrl/pspctrl.h.md#struct-scectrldata) – Controller data.
- [`struct SceCtrlLatch`](../files/ctrl/pspctrl.h.md#struct-scectrllatch) – Controller latch data.

## Typedefs

- [`SceCtrlLatch`](../files/ctrl/pspctrl.h.md#scectrllatch) – Controller latch data.

## Enumerations

- [`PspCtrlButtons`](../files/ctrl/pspctrl.h.md#enum-pspctrlbuttons) – Enumeration representing digital controller button flags.
- [`PspCtrlMode`](../files/ctrl/pspctrl.h.md#enum-pspctrlmode) – Controller mode.

## Functions

- [`sceCtrlSetSamplingCycle()`](../files/ctrl/pspctrl.h.md#scectrlsetsamplingcycle) – Set the controller cycle setting.
- [`sceCtrlGetSamplingCycle()`](../files/ctrl/pspctrl.h.md#scectrlgetsamplingcycle) – Get the controller current cycle setting.
- [`sceCtrlSetSamplingMode()`](../files/ctrl/pspctrl.h.md#scectrlsetsamplingmode) – Set the controller mode.
- [`sceCtrlGetSamplingMode()`](../files/ctrl/pspctrl.h.md#scectrlgetsamplingmode) – Get the current controller mode.
- [`sceCtrlPeekBufferPositive()`](../files/ctrl/pspctrl.h.md#scectrlpeekbufferpositive) – Read latest controller data from the controller service.
- [`sceCtrlPeekBufferNegative()`](../files/ctrl/pspctrl.h.md#scectrlpeekbuffernegative)
- [`sceCtrlReadBufferPositive()`](../files/ctrl/pspctrl.h.md#scectrlreadbufferpositive) – Read new controller data from the controller service.
- [`sceCtrlReadBufferNegative()`](../files/ctrl/pspctrl.h.md#scectrlreadbuffernegative)
- [`sceCtrlPeekLatch()`](../files/ctrl/pspctrl.h.md#scectrlpeeklatch) – Read latest latch data from the controller service.
- [`sceCtrlReadLatch()`](../files/ctrl/pspctrl.h.md#scectrlreadlatch) – Read new latch data from the controller service.
- [`sceCtrlSetIdleCancelThreshold()`](../files/ctrl/pspctrl.h.md#scectrlsetidlecancelthreshold) – Set analog threshold relating to the idle timer.
- [`sceCtrlGetIdleCancelThreshold()`](../files/ctrl/pspctrl.h.md#scectrlgetidlecancelthreshold) – Get the idle threshold values.

## Variables

- [`Rsrv`](../files/ctrl/pspctrl.h.md#rsrv) – Reserved bytes.
- [`SceCtrlData`](../files/ctrl/pspctrl.h.md#scectrldata)

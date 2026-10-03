[PSPSDK documentation](../README.md) › Topics

# Interrupt Manager

This module contains routines to manage interrupts.

Headers: [`user/pspintrman.h`](../files/user/pspintrman.h.md)

## Data Structures

- [`struct tag_IntrHandlerOptionParam`](../files/user/pspintrman.h.md#struct-tag_intrhandleroptionparam)

## Typedefs

- [`PspIntrHandlerOptionParam`](../files/user/pspintrman.h.md#pspintrhandleroptionparam)

## Enumerations

- [`PspInterrupts`](../files/user/pspintrman.h.md#enum-pspinterrupts)
- [`PspSubInterrupts`](../files/user/pspintrman.h.md#enum-pspsubinterrupts)

## Functions

- [`sceKernelCpuSuspendIntr()`](../files/user/pspintrman.h.md#scekernelcpususpendintr) – Suspend all interrupts.
- [`sceKernelCpuResumeIntr()`](../files/user/pspintrman.h.md#scekernelcpuresumeintr) – Resume all interrupts.
- [`sceKernelCpuResumeIntrWithSync()`](../files/user/pspintrman.h.md#scekernelcpuresumeintrwithsync) – Resume all interrupts (using sync instructions).
- [`sceKernelIsCpuIntrSuspended()`](../files/user/pspintrman.h.md#scekerneliscpuintrsuspended) – Determine if interrupts are suspended or active, based on the given flags.
- [`sceKernelIsCpuIntrEnable()`](../files/user/pspintrman.h.md#scekerneliscpuintrenable) – Determine if interrupts are enabled or disabled.
- [`sceKernelRegisterSubIntrHandler()`](../files/user/pspintrman.h.md#scekernelregistersubintrhandler) – Register a sub interrupt handler.
- [`sceKernelReleaseSubIntrHandler()`](../files/user/pspintrman.h.md#scekernelreleasesubintrhandler) – Release a sub interrupt handler.
- [`sceKernelEnableSubIntr()`](../files/user/pspintrman.h.md#scekernelenablesubintr) – Enable a sub interrupt.
- [`sceKernelDisableSubIntr()`](../files/user/pspintrman.h.md#scekerneldisablesubintr) – Disable a sub interrupt handler.
- [`QueryIntrHandlerInfo()`](../files/user/pspintrman.h.md#queryintrhandlerinfo)

## Variables

- [`PspInterruptNames`](../files/user/pspintrman.h.md#pspinterruptnames)

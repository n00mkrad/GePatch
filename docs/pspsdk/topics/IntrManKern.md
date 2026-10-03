[PSPSDK documentation](../README.md) › Topics

# Interrupt Manager Kernel

This module contains routines to manage interrupts.

Headers: [`kernel/pspintrman_kernel.h`](../files/kernel/pspintrman_kernel.h.md)

## Functions

- [`sceKernelRegisterIntrHandler()`](../files/kernel/pspintrman_kernel.h.md#scekernelregisterintrhandler) – Register an interrupt handler.
- [`sceKernelReleaseIntrHandler()`](../files/kernel/pspintrman_kernel.h.md#scekernelreleaseintrhandler) – Release an interrupt handler.
- [`sceKernelEnableIntr()`](../files/kernel/pspintrman_kernel.h.md#scekernelenableintr) – Enable an interrupt.
- [`sceKernelDisableIntr()`](../files/kernel/pspintrman_kernel.h.md#scekerneldisableintr) – Disable an interrupt.
- [`sceKernelIsIntrContext()`](../files/kernel/pspintrman_kernel.h.md#scekernelisintrcontext) – Check if we are in an interrupt context or not.
- [`sceKernelQuerySystemCall()`](../files/kernel/pspintrman_kernel.h.md#scekernelquerysystemcall) – Query system call number of `function`.

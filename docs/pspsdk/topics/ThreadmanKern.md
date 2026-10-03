[PSPSDK documentation](../README.md) › Topics

# Thread Manager kernel functions

This module contains routines to threads in the kernel.

Headers: [`kernel/pspthreadman_kernel.h`](../files/kernel/pspthreadman_kernel.h.md)

## Data Structures

- [`struct SceThreadContext`](../files/kernel/pspthreadman_kernel.h.md#struct-scethreadcontext) – Thread context Structues for the thread context taken from florinsasu's post on the forums.
- [`struct SceSCContext`](../files/kernel/pspthreadman_kernel.h.md#struct-scesccontext)
- [`struct SceKernelThreadKInfo`](../files/kernel/pspthreadman_kernel.h.md#struct-scekernelthreadkinfo) – Structure to hold the status information for a thread (kernel form) 1.5 form.

## Typedefs

- [`SceKernelThreadKInfo`](../files/kernel/pspthreadman_kernel.h.md#scekernelthreadkinfo) – Structure to hold the status information for a thread (kernel form) 1.5 form.

## Functions

- [`sceKernelSuspendAllUserThreads()`](../files/kernel/pspthreadman_kernel.h.md#scekernelsuspendalluserthreads) – Suspend all user mode threads in the system.
- [`sceKernelIsUserModeThread()`](../files/kernel/pspthreadman_kernel.h.md#scekernelisusermodethread) – Checks if the current thread is a usermode thread.
- [`sceKernelGetUserLevel()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetuserlevel) – Get the user level of the current thread.
- [`sceKernelGetSyscallRA()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetsyscallra) – Get the return address of the current thread's syscall.
- [`sceKernelGetThreadKernelStackFreeSize()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetthreadkernelstackfreesize) – Get the free stack space on the kernel thread.
- [`sceKernelCheckThreadKernelStack()`](../files/kernel/pspthreadman_kernel.h.md#scekernelcheckthreadkernelstack) – Check the thread kernel stack.
- [`sceKernelExtendKernelStack()`](../files/kernel/pspthreadman_kernel.h.md#scekernelextendkernelstack) – Extend the kernel thread stack.
- [`sceKernelGetSystemStatusFlag()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetsystemstatusflag) – Get the system status flag.
- [`sceKernelAllocateKTLS()`](../files/kernel/pspthreadman_kernel.h.md#scekernelallocatektls) – Setup the KTLS allocator.
- [`sceKernelFreeKTLS()`](../files/kernel/pspthreadman_kernel.h.md#scekernelfreektls) – Free the KTLS allocator.
- [`sceKernelGetKTLS()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetktls) – Get the KTLS of the current thread.
- [`sceKernelGetThreadKTLS()`](../files/kernel/pspthreadman_kernel.h.md#scekernelgetthreadktls) – Get the KTLS of a thread.
- [`sceKernelReferThreadDebugStatus()`](../files/kernel/pspthreadman_kernel.h.md#scekernelreferthreaddebugstatus) – Refer kernel version of thread information.

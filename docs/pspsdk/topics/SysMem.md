[PSPSDK documentation](../README.md) › Topics

# System Memory Manager

This module contains routines to manage heaps of memory.

Headers: [`user/pspsysmem.h`](../files/user/pspsysmem.h.md)

## Typedefs

- [`SceKernelSysMemAlloc_t`](../files/user/pspsysmem.h.md#scekernelsysmemalloc_t)

## Enumerations

- [`PspSysMemBlockTypes`](../files/user/pspsysmem.h.md#enum-pspsysmemblocktypes) – Specifies the type of allocation used for memory blocks.

## Functions

- [`sceKernelAllocPartitionMemory()`](../files/user/pspsysmem.h.md#scekernelallocpartitionmemory) – Allocate a memory block from a memory partition.
- [`sceKernelFreePartitionMemory()`](../files/user/pspsysmem.h.md#scekernelfreepartitionmemory) – Free a memory block allocated with [sceKernelAllocPartitionMemory](../files/user/pspsysmem.h.md#scekernelallocpartitionmemory).
- [`sceKernelGetBlockHeadAddr()`](../files/user/pspsysmem.h.md#scekernelgetblockheadaddr) – Get the address of a memory block.
- [`sceKernelTotalFreeMemSize()`](../files/user/pspsysmem.h.md#scekerneltotalfreememsize) – Get the total amount of free memory.
- [`sceKernelMaxFreeMemSize()`](../files/user/pspsysmem.h.md#scekernelmaxfreememsize) – Get the size of the largest free memory block.
- [`sceKernelDevkitVersion()`](../files/user/pspsysmem.h.md#scekerneldevkitversion) – Get the firmware version.
- [`sceKernelSetCompiledSdkVersion()`](../files/user/pspsysmem.h.md#scekernelsetcompiledsdkversion) – Set the version of the SDK with which the caller was compiled.
- [`sceKernelGetCompiledSdkVersion()`](../files/user/pspsysmem.h.md#scekernelgetcompiledsdkversion) – Get the SDK version set with [sceKernelSetCompiledSdkVersion()](../files/user/pspsysmem.h.md#scekernelsetcompiledsdkversion).

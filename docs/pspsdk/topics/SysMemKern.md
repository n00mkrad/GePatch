[PSPSDK documentation](../README.md) › Topics

# System Memory Manager Kernel

This module contains routines to manage heaps of memory.

Headers: [`kernel/pspsysmem_kernel.h`](../files/kernel/pspsysmem_kernel.h.md)

## Data Structures

- [`struct _PspSysmemPartitionInfo`](../files/kernel/pspsysmem_kernel.h.md#struct-_pspsysmempartitioninfo)
- [`struct SceGameInfo`](../files/kernel/pspsysmem_kernel.h.md#struct-scegameinfo)
- [`struct _uidControlBlock`](../files/kernel/pspsysmem_kernel.h.md#struct-_uidcontrolblock) – Structure of a UID control block.
- [`struct SceSysmemPartInfo`](../files/kernel/pspsysmem_kernel.h.md#struct-scesysmempartinfo)
- [`struct SceSysmemPartTable`](../files/kernel/pspsysmem_kernel.h.md#struct-scesysmemparttable)
- [`struct PspPartitionData`](../files/kernel/pspsysmem_kernel.h.md#struct-psppartitiondata)
- [`struct PspSysMemPartition`](../files/kernel/pspsysmem_kernel.h.md#struct-pspsysmempartition)

## Typedefs

- [`PspSysmemPartitionInfo`](../files/kernel/pspsysmem_kernel.h.md#pspsysmempartitioninfo)
- [`SceGameInfo`](../files/kernel/pspsysmem_kernel.h.md#scegameinfo)
- [`SceUidControlBlock`](../files/kernel/pspsysmem_kernel.h.md#sceuidcontrolblock)
- [`uidControlBlock`](../files/kernel/pspsysmem_kernel.h.md#uidcontrolblock)
- [`PspPartitionData`](../files/kernel/pspsysmem_kernel.h.md#psppartitiondata)
- [`PspSysMemPartition`](../files/kernel/pspsysmem_kernel.h.md#pspsysmempartition)

## Functions

- [`sceKernelQueryMemoryPartitionInfo()`](../files/kernel/pspsysmem_kernel.h.md#scekernelquerymemorypartitioninfo) – Query the parition information.
- [`sceKernelPartitionTotalFreeMemSize()`](../files/kernel/pspsysmem_kernel.h.md#scekernelpartitiontotalfreememsize) – Get the total amount of free memory.
- [`sceKernelPartitionMaxFreeMemSize()`](../files/kernel/pspsysmem_kernel.h.md#scekernelpartitionmaxfreememsize) – Get the size of the largest free memory block.
- [`sceKernelSysMemDump()`](../files/kernel/pspsysmem_kernel.h.md#scekernelsysmemdump) – Get the kernel to dump the internal memory table to Kprintf.
- [`sceKernelSysMemDumpBlock()`](../files/kernel/pspsysmem_kernel.h.md#scekernelsysmemdumpblock) – Dump the list of memory blocks.
- [`sceKernelSysMemDumpTail()`](../files/kernel/pspsysmem_kernel.h.md#scekernelsysmemdumptail) – Dump the tail blocks.
- [`sceKernelSetDdrMemoryProtection()`](../files/kernel/pspsysmem_kernel.h.md#scekernelsetddrmemoryprotection) – Set the protection of a block of ddr memory.
- [`sceKernelCreateHeap()`](../files/kernel/pspsysmem_kernel.h.md#scekernelcreateheap) – Create a heap.
- [`sceKernelAllocHeapMemory()`](../files/kernel/pspsysmem_kernel.h.md#scekernelallocheapmemory) – Allocate a memory block from a heap.
- [`sceKernelFreeHeapMemory()`](../files/kernel/pspsysmem_kernel.h.md#scekernelfreeheapmemory) – Free a memory block allocated from a heap.
- [`sceKernelDeleteHeap()`](../files/kernel/pspsysmem_kernel.h.md#scekerneldeleteheap) – Delete a heap.
- [`sceKernelHeapTotalFreeSize()`](../files/kernel/pspsysmem_kernel.h.md#scekernelheaptotalfreesize) – Get the amount of free size of a heap, in bytes.
- [`sceKernelGetSceUidControlBlock()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetsceuidcontrolblock) – Get a UID control block.
- [`sceKernelGetSceUidControlBlockWithType()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetsceuidcontrolblockwithtype) – Get a UID control block on a particular type.
- [`sceKernelGetUidmanCB()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetuidmancb) – Get the root of the UID tree (1.5+ only)
- [`sceKernelDeleteUID()`](../files/kernel/pspsysmem_kernel.h.md#scekerneldeleteuid) – Delete a UID.
- [`sceKernelGetModel()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetmodel) – Get the model of PSP.
- [`sceKernelSetCompiledSdkVersion()`](../files/kernel/pspsysmem_kernel.h.md#scekernelsetcompiledsdkversion) – Set the version of the SDK with which the caller was compiled.
- [`sceKernelGetCompiledSdkVersion()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetcompiledsdkversion) – Get the SDK version set with [sceKernelSetCompiledSdkVersion()](../files/kernel/pspsysmem_kernel.h.md#scekernelsetcompiledsdkversion).
- [`sceKernelGetGameInfo()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetgameinfo) – Gets the information of the game.
- [`sceKernelGetSystemStatus()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetsystemstatus) – Gets the current status of the system.
- [`sceKernelGetUIDcontrolBlock()`](../files/kernel/pspsysmem_kernel.h.md#scekernelgetuidcontrolblock) – Get a UID control block.

[PSPSDK documentation](../README.md) › Topics

# Interface to the LoadCoreForKernel library.

Headers: [`kernel/psploadcore.h`](../files/kernel/psploadcore.h.md)

## Data Structures

- [`struct SceModule`](../files/kernel/psploadcore.h.md#struct-scemodule) – Describes a loaded module in memory.
- [`struct SceLoadCoreBootModuleInfo`](../files/kernel/psploadcore.h.md#struct-sceloadcorebootmoduleinfo)
- [`struct SceLibraryEntryTable`](../files/kernel/psploadcore.h.md#struct-scelibraryentrytable) – Defines a library and its exported functions and variables.
- [`struct SceLibraryStubTable`](../files/kernel/psploadcore.h.md#struct-scelibrarystubtable) – Specifies a library and a set of imports from that library.
- [`struct SceLoadCoreExecFileInfo`](../files/kernel/psploadcore.h.md#struct-sceloadcoreexecfileinfo)

## Macros

- [`SCE_KERNEL_MAX_MODULE_SEGMENT`](../files/kernel/psploadcore.h.md#sce_kernel_max_module_segment)

## Typedefs

- [`SceKernelRebootBeforeForKernel`](../files/kernel/psploadcore.h.md#scekernelrebootbeforeforkernel) – Reboot preparation functions.
- [`SceKernelRebootPhaseForKernel`](../files/kernel/psploadcore.h.md#scekernelrebootphaseforkernel)
- [`SceModule`](../files/kernel/psploadcore.h.md#scemodule) – Describes a loaded module in memory.
- [`SceLibraryEntryTable`](../files/kernel/psploadcore.h.md#scelibraryentrytable) – Defines a library and its exported functions and variables.
- [`SceLibraryStubTable`](../files/kernel/psploadcore.h.md#scelibrarystubtable) – Specifies a library and a set of imports from that library.
- [`SceLoadCoreExecFileInfo`](../files/kernel/psploadcore.h.md#sceloadcoreexecfileinfo)

## Enumerations

- [`SceModuleAttribute`](../files/kernel/psploadcore.h.md#enum-scemoduleattribute) – Module type attributes.
- [`SceModulePrivilegeLevel`](../files/kernel/psploadcore.h.md#enum-scemoduleprivilegelevel) – Module Privilege Levels - These levels define the permissions a module can have.

## Functions

- [`sceKernelGetModuleList()`](../files/kernel/psploadcore.h.md#scekernelgetmodulelist) – Gets the current module list.
- [`sceKernelModuleCount()`](../files/kernel/psploadcore.h.md#scekernelmodulecount) – Get the number of loaded modules.
- [`sceKernelFindModuleByName()`](../files/kernel/psploadcore.h.md#scekernelfindmodulebyname) – Find a module by it's name.
- [`sceKernelFindModuleByAddress()`](../files/kernel/psploadcore.h.md#scekernelfindmodulebyaddress) – Find a module from an address.
- [`sceKernelFindModuleByUID()`](../files/kernel/psploadcore.h.md#scekernelfindmodulebyuid) – Find a module by it's UID.
- [`sceKernelIcacheClearAll()`](../files/kernel/psploadcore.h.md#scekernelicacheclearall) – Invalidate the CPU's instruction cache.
- [`sceKernelCheckExecFile()`](../files/kernel/psploadcore.h.md#scekernelcheckexecfile) – Check an executable file.
- [`sceKernelProbeExecutableObject()`](../files/kernel/psploadcore.h.md#scekernelprobeexecutableobject) – Probe an executable file.
- [`sceKernelGetModuleIdListForKernel()`](../files/kernel/psploadcore.h.md#scekernelgetmoduleidlistforkernel) – Receive a list of UIDs of loaded modules.
- [`sceKernelCheckPspConfig()`](../files/kernel/psploadcore.h.md#scekernelcheckpspconfig)

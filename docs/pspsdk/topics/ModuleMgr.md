[PSPSDK documentation](../README.md) › Topics

# Module Manager Library

This module contains the imports for the kernel's module management routines.

Headers: [`user/pspmodulemgr.h`](../files/user/pspmodulemgr.h.md)

## Data Structures

- [`struct SceKernelLMOption`](../files/user/pspmodulemgr.h.md#struct-scekernellmoption)
- [`struct SceKernelSMOption`](../files/user/pspmodulemgr.h.md#struct-scekernelsmoption)
- [`struct SceKernelModuleInfo`](../files/user/pspmodulemgr.h.md#struct-scekernelmoduleinfo)

## Macros

- [`PSP_MEMORY_PARTITION_KERNEL`](../files/user/pspmodulemgr.h.md#psp_memory_partition_kernel)
- [`PSP_MEMORY_PARTITION_USER`](../files/user/pspmodulemgr.h.md#psp_memory_partition_user)
- [`SCE_SECURE_INSTALL_ID_LEN`](../files/user/pspmodulemgr.h.md#sce_secure_install_id_len)

## Typedefs

- [`SceKernelLMOption`](../files/user/pspmodulemgr.h.md#scekernellmoption)
- [`SceKernelSMOption`](../files/user/pspmodulemgr.h.md#scekernelsmoption)
- [`SceKernelModuleInfo`](../files/user/pspmodulemgr.h.md#scekernelmoduleinfo)

## Functions

- [`sceKernelLoadModule()`](../files/user/pspmodulemgr.h.md#scekernelloadmodule) – Load a module.
- [`sceKernelLoadModuleMs()`](../files/user/pspmodulemgr.h.md#scekernelloadmodulems) – Load a module from MS.
- [`sceKernelLoadModuleMs2()`](../files/user/pspmodulemgr.h.md#scekernelloadmodulems2) – Alias for `sceKernelLoadModuleForLoadExecVSHMs2`
- [`sceKernelLoadModuleByID()`](../files/user/pspmodulemgr.h.md#scekernelloadmodulebyid) – Load a module from the given file UID.
- [`sceKernelLoadModuleBufferUsbWlan()`](../files/user/pspmodulemgr.h.md#scekernelloadmodulebufferusbwlan) – Load a module from a buffer using the USB/WLAN API.
- [`sceKernelStartModule()`](../files/user/pspmodulemgr.h.md#scekernelstartmodule) – Start a loaded module.
- [`sceKernelStopModule()`](../files/user/pspmodulemgr.h.md#scekernelstopmodule) – Stop a running module.
- [`sceKernelUnloadModule()`](../files/user/pspmodulemgr.h.md#scekernelunloadmodule) – Unload a stopped module.
- [`sceKernelSelfStopUnloadModule()`](../files/user/pspmodulemgr.h.md#scekernelselfstopunloadmodule) – Stop and unload the current module.
- [`sceKernelStopUnloadSelfModule()`](../files/user/pspmodulemgr.h.md#scekernelstopunloadselfmodule) – Stop and unload the current module.
- [`sceKernelQueryModuleInfo()`](../files/user/pspmodulemgr.h.md#scekernelquerymoduleinfo) – Query the information about a loaded module from its UID.
- [`sceKernelGetModuleIdList()`](../files/user/pspmodulemgr.h.md#scekernelgetmoduleidlist) – Get a list of module IDs.
- [`sceKernelGetModuleIdByAddress()`](../files/user/pspmodulemgr.h.md#scekernelgetmoduleidbyaddress) – Get the ID of the module occupying the address.

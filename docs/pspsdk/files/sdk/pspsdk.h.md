[PSPSDK documentation](../../README.md) › Files

# sdk/pspsdk.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspmodulemgr.h>
#include <pspmoduleinfo.h>
#include <pspthreadman.h>
```

Topics: [PSPSDK Utility Library](../../topics/PSPSDK.md)

## Functions

### `pspSdkQueryModuleInfoV1()`

```c
int pspSdkQueryModuleInfoV1(SceUID uid, SceKernelModuleInfo *modinfo);
```

Query a modules information from its uid.

**Note:** this is a replacement function for the broken kernel sceKernelQueryModuleInfo in v1.0 firmware DO NOT use on a anything above that version. This also needs kernel mode access where the normal one has a user mode stub.

**Parameters:**

- `uid` – The UID of the module to query.
- `modinfo` – Pointer a module [SceKernelModuleInfo](../user/pspmodulemgr.h.md#struct-scekernelmoduleinfo) structure.

**Returns:** \< 0 on error.

### `pspSdkGetModuleIdList()`

```c
int pspSdkGetModuleIdList(SceUID *readbuf, int readbufsize, int *idcount);
```

Get the list of module IDs.

**Note:** This is a replacement function for the missing v1.5 sceKernelGetModuleIdList on v1.0 firmware. DO NOT use on anything above that version.

**Parameters:**

- `readbuf` – Buffer to store the module list.
- `readbufsize` – Number of elements in the readbuffer.
- `idcount` – Returns the number of module ids

**Returns:** >= 0 on success

### `pspSdkInstallNoDeviceCheckPatch()`

```c
int pspSdkInstallNoDeviceCheckPatch(void);
```

Patch the sceModuleManager module to nullify LoadDeviceCheck() calls.

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

**Note:** This function must be called while running in kernel mode. The program must also be linked against the pspkernel library.

### `pspSdkInstallNoPlainModuleCheckPatch()`

```c
int pspSdkInstallNoPlainModuleCheckPatch(void);
```

Patch sceLoadCore module to remove loading plain module checks.

**Note:** This function must be called while running in kernel mode.

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkInstallKernelLoadModulePatch()`

```c
int pspSdkInstallKernelLoadModulePatch(void);
```

Patch sceLoadModuleWithApiType to remove the kernel check in loadmodule allowing all modules to load.

**Note:** This function must be called while running in kernel mode

**Returns:** 0 on success

### `pspSdkLoadStartModule()`

```c
SceUID pspSdkLoadStartModule(const char *filename, int mpid);
```

Load a module and start it.

**Parameters:**

- `filename` – Path to the module.
- `mpid` – Memory parition ID to use to load the module int.

**Returns:** - The UID of the module on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkLoadStartModuleWithArgs()`

```c
SceUID pspSdkLoadStartModuleWithArgs(const char *filename, int mpid, int argc, char *const argv[]);
```

Load a module and start it with arguments.

**Parameters:**

- `filename` – Path to the module.
- `mpid` – Memory parition ID to use to load the module int.
- `argc` – Number of arguments to pass to start module
- `argv` – Array of arguments

**Returns:** - The UID of the module on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkFixupImports()`

```c
void pspSdkFixupImports(int moduleId);
```

Manually fixup library imports for late binding modules.

**Parameters:**

- `moduleId` – Id of the module to fixup

### `pspSdkLoadInetModules()`

```c
int pspSdkLoadInetModules();
```

Load Inet related modules.

**Note:** You must be in kernel mode to execute this function.

**Returns:** - 0 on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkInetInit()`

```c
int pspSdkInetInit();
```

Initialize Inet related modules.

**Returns:** - 0 on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkInetTerm()`

```c
void pspSdkInetTerm();
```

Terminate Inet related modules.

### `pspSdkReferThreadStatusByName()`

```c
int pspSdkReferThreadStatusByName(const char *name, SceUID *pUID, SceKernelThreadInfo *pInfo);
```

Search for a thread with the given name and retrieve it's [SceKernelThreadInfo](../user/pspthreadman.h.md#struct-scekernelthreadinfo) struct.

**Parameters:**

- `name` – The name of the thread to search for.
- `pUID` – If the thread with the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the thread with the given name is found, it's [SceKernelThreadInfo](../user/pspthreadman.h.md#struct-scekernelthreadinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferSemaStatusByName()`

```c
int pspSdkReferSemaStatusByName(const char *name, SceUID *pUID, SceKernelSemaInfo *pInfo);
```

Search for a semaphore with the given name and retrieve it's [SceKernelSemaInfo](../user/pspthreadman.h.md#struct-scekernelsemainfo) struct.

**Parameters:**

- `name` – The name of the sema to search for.
- `pUID` – If the sema with the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the sema with the given name is found, it's [SceKernelSemaInfo](../user/pspthreadman.h.md#struct-scekernelsemainfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferEventFlagStatusByName()`

```c
int pspSdkReferEventFlagStatusByName(const char *name, SceUID *pUID, SceKernelEventFlagInfo *pInfo);
```

Search for an event flag with the given name and retrieve it's [SceKernelEventFlagInfo](../user/pspthreadman.h.md#struct-scekerneleventflaginfo) struct.

**Parameters:**

- `name` – The name of the event flag to search for.
- `pUID` – If the event flag with the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the event flag with the given name is found, it's [SceKernelEventFlagInfo](../user/pspthreadman.h.md#struct-scekerneleventflaginfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferMboxStatusByName()`

```c
int pspSdkReferMboxStatusByName(const char *name, SceUID *pUID, SceKernelMbxInfo *pInfo);
```

Search for a message box with the given name and retrieve it's [SceKernelMbxInfo](../user/pspthreadman.h.md#struct-scekernelmbxinfo) struct.

**Parameters:**

- `name` – The name of the message box to search for.
- `pUID` – If the message box with the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the message box with the given name is found, it's [SceKernelMbxInfo](../user/pspthreadman.h.md#struct-scekernelmbxinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferVplStatusByName()`

```c
int pspSdkReferVplStatusByName(const char *name, SceUID *pUID, SceKernelVplInfo *pInfo);
```

Search for a VPL with the given name and retrieve it's [SceKernelVplInfo](../user/pspthreadman.h.md#struct-scekernelvplinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelVplInfo](../user/pspthreadman.h.md#struct-scekernelvplinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferFplStatusByName()`

```c
int pspSdkReferFplStatusByName(const char *name, SceUID *pUID, SceKernelFplInfo *pInfo);
```

Search for a FPL with the given name and retrieve it's [SceKernelFplInfo](../user/pspthreadman.h.md#struct-scekernelfplinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelFplInfo](../user/pspthreadman.h.md#struct-scekernelfplinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferMppStatusByName()`

```c
int pspSdkReferMppStatusByName(const char *name, SceUID *pUID, SceKernelMppInfo *pInfo);
```

Search for a message pipe with the given name and retrieve it's [SceKernelMppInfo](../user/pspthreadman.h.md#struct-scekernelmppinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelMppInfo](../user/pspthreadman.h.md#struct-scekernelmppinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferCallbackStatusByName()`

```c
int pspSdkReferCallbackStatusByName(const char *name, SceUID *pUID, SceKernelCallbackInfo *pInfo);
```

Search for a callback with the given name and retrieve it's [SceKernelCallbackInfo](../user/pspthreadman.h.md#struct-scekernelcallbackinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelMppInfo](../user/pspthreadman.h.md#struct-scekernelmppinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferVTimerStatusByName()`

```c
int pspSdkReferVTimerStatusByName(const char *name, SceUID *pUID, SceKernelVTimerInfo *pInfo);
```

Search for a vtimer with the given name and retrieve it's [SceKernelVTimerInfo](../user/pspthreadman.h.md#struct-scekernelvtimerinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelVTimerInfo](../user/pspthreadman.h.md#struct-scekernelvtimerinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkReferThreadEventHandlerStatusByName()`

```c
int pspSdkReferThreadEventHandlerStatusByName(const char *name, SceUID *pUID, SceKernelThreadEventHandlerInfo *pInfo);
```

Search for a thread event handler with the given name and retrieve it's [SceKernelThreadEventHandlerInfo](../user/pspthreadman.h.md#struct-scekernelthreadeventhandlerinfo) struct.

**Parameters:**

- `name` – The name of to search for.
- `pUID` – If the given name is found, it's [SceUID](../user/pspkerneltypes.h.md#sceuid) is stored here.
- `pInfo` – If the given name is found, it's [SceKernelThreadEventHandlerInfo](../user/pspthreadman.h.md#struct-scekernelthreadeventhandlerinfo) data is stored here.

**Returns:** 0 if successful, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `pspSdkDisableInterrupts()`

```c
unsigned int pspSdkDisableInterrupts(void);
```

Disable interrupts.

**Note:** Do not disable interrupts for too long otherwise the watchdog will get you.

**Returns:** The previous state of the interrupt enable bit (should be passed back to [pspSdkEnableInterrupts](#pspsdkenableinterrupts))

### `pspSdkEnableInterrupts()`

```c
void pspSdkEnableInterrupts(unsigned int istate);
```

Enable interrupts.

**Parameters:**

- `istate` – The interrupt state as returned from [pspSdkDisableInterrupts](#pspsdkdisableinterrupts)

### `pspSdkSetK1()`

```c
unsigned int pspSdkSetK1(unsigned int k1);
```

Set the processors K1 register to a known value.

**Note:** This function is for use in kernel mode syscall exports. The kernel sets the k1 register to indicate what mode called the function, i.e. whether it was directly called, was called via a syscall from a kernel thread or called via a syscall from a user thread. By setting k1 to 0 before doing anything in your code you can make the other functions think you are calling from a kernel thread and therefore disable numerous protections.

**Parameters:**

- `k1` – The k1 value to set

**Returns:** The previous value of k1

### `pspSdkGetK1()`

```c
unsigned int pspSdkGetK1(void);
```

Get the current value of the processors K1 register.

**Returns:** The current value of K1

### `pspSdkDisableFPUExceptions()`

```c
void pspSdkDisableFPUExceptions(void);
```

Disable the CPUs FPU exceptions.

### `pspSdkTotalFreeUserMemSize()`

```c
SceSize pspSdkTotalFreeUserMemSize(void);
```

Gets the amount of memory available in the user partition(s).

**Note:** This is not to be confused with sceKernelTotalFreeMemSize, which rather contradictorily only returns the amount of memory free in the kernel memory partition.

**Returns:** The amount of user memory available, in bytes.

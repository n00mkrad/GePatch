[PSPSDK documentation](../README.md) › Topics

# PSPSDK Utility Library

Headers: [`sdk/pspsdk.h`](../files/sdk/pspsdk.h.md)

## Functions

- [`pspSdkQueryModuleInfoV1()`](../files/sdk/pspsdk.h.md#pspsdkquerymoduleinfov1) – Query a modules information from its uid.
- [`pspSdkGetModuleIdList()`](../files/sdk/pspsdk.h.md#pspsdkgetmoduleidlist) – Get the list of module IDs.
- [`pspSdkInstallNoDeviceCheckPatch()`](../files/sdk/pspsdk.h.md#pspsdkinstallnodevicecheckpatch) – Patch the sceModuleManager module to nullify LoadDeviceCheck() calls.
- [`pspSdkInstallNoPlainModuleCheckPatch()`](../files/sdk/pspsdk.h.md#pspsdkinstallnoplainmodulecheckpatch) – Patch sceLoadCore module to remove loading plain module checks.
- [`pspSdkInstallKernelLoadModulePatch()`](../files/sdk/pspsdk.h.md#pspsdkinstallkernelloadmodulepatch) – Patch sceLoadModuleWithApiType to remove the kernel check in loadmodule allowing all modules to load.
- [`pspSdkLoadStartModule()`](../files/sdk/pspsdk.h.md#pspsdkloadstartmodule) – Load a module and start it.
- [`pspSdkLoadStartModuleWithArgs()`](../files/sdk/pspsdk.h.md#pspsdkloadstartmodulewithargs) – Load a module and start it with arguments.
- [`pspSdkFixupImports()`](../files/sdk/pspsdk.h.md#pspsdkfixupimports) – Manually fixup library imports for late binding modules.
- [`pspSdkLoadInetModules()`](../files/sdk/pspsdk.h.md#pspsdkloadinetmodules) – Load Inet related modules.
- [`pspSdkInetInit()`](../files/sdk/pspsdk.h.md#pspsdkinetinit) – Initialize Inet related modules.
- [`pspSdkInetTerm()`](../files/sdk/pspsdk.h.md#pspsdkinetterm) – Terminate Inet related modules.
- [`pspSdkReferThreadStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkreferthreadstatusbyname) – Search for a thread with the given name and retrieve it's [SceKernelThreadInfo](../files/user/pspthreadman.h.md#struct-scekernelthreadinfo) struct.
- [`pspSdkReferSemaStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefersemastatusbyname) – Search for a semaphore with the given name and retrieve it's [SceKernelSemaInfo](../files/user/pspthreadman.h.md#struct-scekernelsemainfo) struct.
- [`pspSdkReferEventFlagStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefereventflagstatusbyname) – Search for an event flag with the given name and retrieve it's [SceKernelEventFlagInfo](../files/user/pspthreadman.h.md#struct-scekerneleventflaginfo) struct.
- [`pspSdkReferMboxStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefermboxstatusbyname) – Search for a message box with the given name and retrieve it's [SceKernelMbxInfo](../files/user/pspthreadman.h.md#struct-scekernelmbxinfo) struct.
- [`pspSdkReferVplStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefervplstatusbyname) – Search for a VPL with the given name and retrieve it's [SceKernelVplInfo](../files/user/pspthreadman.h.md#struct-scekernelvplinfo) struct.
- [`pspSdkReferFplStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkreferfplstatusbyname) – Search for a FPL with the given name and retrieve it's [SceKernelFplInfo](../files/user/pspthreadman.h.md#struct-scekernelfplinfo) struct.
- [`pspSdkReferMppStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefermppstatusbyname) – Search for a message pipe with the given name and retrieve it's [SceKernelMppInfo](../files/user/pspthreadman.h.md#struct-scekernelmppinfo) struct.
- [`pspSdkReferCallbackStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefercallbackstatusbyname) – Search for a callback with the given name and retrieve it's [SceKernelCallbackInfo](../files/user/pspthreadman.h.md#struct-scekernelcallbackinfo) struct.
- [`pspSdkReferVTimerStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkrefervtimerstatusbyname) – Search for a vtimer with the given name and retrieve it's [SceKernelVTimerInfo](../files/user/pspthreadman.h.md#struct-scekernelvtimerinfo) struct.
- [`pspSdkReferThreadEventHandlerStatusByName()`](../files/sdk/pspsdk.h.md#pspsdkreferthreadeventhandlerstatusbyname) – Search for a thread event handler with the given name and retrieve it's [SceKernelThreadEventHandlerInfo](../files/user/pspthreadman.h.md#struct-scekernelthreadeventhandlerinfo) struct.
- [`pspSdkDisableInterrupts()`](../files/sdk/pspsdk.h.md#pspsdkdisableinterrupts) – Disable interrupts.
- [`pspSdkEnableInterrupts()`](../files/sdk/pspsdk.h.md#pspsdkenableinterrupts) – Enable interrupts.
- [`pspSdkSetK1()`](../files/sdk/pspsdk.h.md#pspsdksetk1) – Set the processors K1 register to a known value.
- [`pspSdkGetK1()`](../files/sdk/pspsdk.h.md#pspsdkgetk1) – Get the current value of the processors K1 register.
- [`pspSdkDisableFPUExceptions()`](../files/sdk/pspsdk.h.md#pspsdkdisablefpuexceptions) – Disable the CPUs FPU exceptions.
- [`pspSdkTotalFreeUserMemSize()`](../files/sdk/pspsdk.h.md#pspsdktotalfreeusermemsize) – Gets the amount of memory available in the user partition(s).

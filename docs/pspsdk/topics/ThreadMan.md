[PSPSDK documentation](../README.md) › Topics

# Thread Manager Library

Library imports for the kernel threading library.

Headers: [`user/pspthreadman.h`](../files/user/pspthreadman.h.md)

## Data Structures

- [`struct SceKernelSysClock`](../files/user/pspthreadman.h.md#struct-scekernelsysclock) – 64-bit system clock type.
- [`struct SceKernelThreadOptParam`](../files/user/pspthreadman.h.md#struct-scekernelthreadoptparam) – Additional options used when creating threads.
- [`struct SceKernelThreadInfo`](../files/user/pspthreadman.h.md#struct-scekernelthreadinfo) – Structure to hold the status information for a thread.
- [`struct SceKernelThreadRunStatus`](../files/user/pspthreadman.h.md#struct-scekernelthreadrunstatus) – Statistics about a running thread.
- [`struct SceKernelSemaOptParam`](../files/user/pspthreadman.h.md#struct-scekernelsemaoptparam) – Additional options used when creating semaphores.
- [`struct SceKernelSemaInfo`](../files/user/pspthreadman.h.md#struct-scekernelsemainfo) – Current state of a semaphore.
- [`struct SceLwMutexWorkarea`](../files/user/pspthreadman.h.md#struct-scelwmutexworkarea) – Struct as workarea for lightweight mutex.
- [`struct SceKernelEventFlagInfo`](../files/user/pspthreadman.h.md#struct-scekerneleventflaginfo) – Structure to hold the event flag information.
- [`struct SceKernelEventFlagOptParam`](../files/user/pspthreadman.h.md#struct-scekerneleventflagoptparam)
- [`struct SceKernelMbxOptParam`](../files/user/pspthreadman.h.md#struct-scekernelmbxoptparam) – Additional options used when creating messageboxes.
- [`struct SceKernelMbxInfo`](../files/user/pspthreadman.h.md#struct-scekernelmbxinfo) – Current state of a messagebox.
- [`struct SceKernelMsgPacket`](../files/user/pspthreadman.h.md#struct-scekernelmsgpacket) – Header for a message box packet.
- [`struct SceKernelAlarmInfo`](../files/user/pspthreadman.h.md#struct-scekernelalarminfo) – Struct containing alarm info.
- [`struct SceKernelCallbackInfo`](../files/user/pspthreadman.h.md#struct-scekernelcallbackinfo) – Structure to hold the status information for a callback.
- [`struct SceKernelSystemStatus`](../files/user/pspthreadman.h.md#struct-scekernelsystemstatus) – Structure to contain the system status returned by [sceKernelReferSystemStatus](../files/user/pspthreadman.h.md#scekernelrefersystemstatus).
- [`struct SceKernelMppInfo`](../files/user/pspthreadman.h.md#struct-scekernelmppinfo) – Message Pipe status info.
- [`struct SceKernelVplOptParam`](../files/user/pspthreadman.h.md#struct-scekernelvploptparam)
- [`struct SceKernelVplInfo`](../files/user/pspthreadman.h.md#struct-scekernelvplinfo) – Variable pool status info.
- [`struct SceKernelFplOptParam`](../files/user/pspthreadman.h.md#struct-scekernelfploptparam)
- [`struct SceKernelFplInfo`](../files/user/pspthreadman.h.md#struct-scekernelfplinfo) – Fixed pool status information.
- [`struct SceKernelVTimerOptParam`](../files/user/pspthreadman.h.md#struct-scekernelvtimeroptparam)
- [`struct SceKernelVTimerInfo`](../files/user/pspthreadman.h.md#struct-scekernelvtimerinfo)
- [`struct SceKernelThreadEventHandlerInfo`](../files/user/pspthreadman.h.md#struct-scekernelthreadeventhandlerinfo) – Struct for event handler info.

## Macros

- [`THREAD_ATTR_VFPU`](../files/user/pspthreadman.h.md#thread_attr_vfpu)
- [`THREAD_ATTR_USER`](../files/user/pspthreadman.h.md#thread_attr_user)

## Typedefs

- [`SceKernelSysClock`](../files/user/pspthreadman.h.md#scekernelsysclock) – 64-bit system clock type.
- [`SceKernelThreadOptParam`](../files/user/pspthreadman.h.md#scekernelthreadoptparam) – Additional options used when creating threads.
- [`SceKernelThreadInfo`](../files/user/pspthreadman.h.md#scekernelthreadinfo) – Structure to hold the status information for a thread.
- [`SceKernelThreadRunStatus`](../files/user/pspthreadman.h.md#scekernelthreadrunstatus) – Statistics about a running thread.
- [`SceKernelSemaOptParam`](../files/user/pspthreadman.h.md#scekernelsemaoptparam) – Additional options used when creating semaphores.
- [`SceKernelSemaInfo`](../files/user/pspthreadman.h.md#scekernelsemainfo) – Current state of a semaphore.
- [`SceKernelEventFlagInfo`](../files/user/pspthreadman.h.md#scekerneleventflaginfo) – Structure to hold the event flag information.
- [`SceKernelEventFlagOptParam`](../files/user/pspthreadman.h.md#scekerneleventflagoptparam)
- [`SceKernelMbxOptParam`](../files/user/pspthreadman.h.md#scekernelmbxoptparam) – Additional options used when creating messageboxes.
- [`SceKernelMbxInfo`](../files/user/pspthreadman.h.md#scekernelmbxinfo) – Current state of a messagebox.
- [`SceKernelMsgPacket`](../files/user/pspthreadman.h.md#scekernelmsgpacket) – Header for a message box packet.
- [`SceKernelAlarmHandler`](../files/user/pspthreadman.h.md#scekernelalarmhandler) – Prototype for alarm handlers.
- [`SceKernelAlarmInfo`](../files/user/pspthreadman.h.md#scekernelalarminfo) – Struct containing alarm info.
- [`SceKernelCallbackFunction`](../files/user/pspthreadman.h.md#scekernelcallbackfunction) – Callback function prototype.
- [`SceKernelCallbackInfo`](../files/user/pspthreadman.h.md#scekernelcallbackinfo) – Structure to hold the status information for a callback.
- [`SceKernelIdListType`](../files/user/pspthreadman.h.md#scekernelidlisttype) – Threadman types for [sceKernelGetThreadmanIdList](../files/user/pspthreadman.h.md#scekernelgetthreadmanidlist).
- [`SceKernelSystemStatus`](../files/user/pspthreadman.h.md#scekernelsystemstatus) – Structure to contain the system status returned by [sceKernelReferSystemStatus](../files/user/pspthreadman.h.md#scekernelrefersystemstatus).
- [`SceKernelMppInfo`](../files/user/pspthreadman.h.md#scekernelmppinfo) – Message Pipe status info.
- [`SceKernelVplOptParam`](../files/user/pspthreadman.h.md#scekernelvploptparam)
- [`SceKernelVplInfo`](../files/user/pspthreadman.h.md#scekernelvplinfo) – Variable pool status info.
- [`SceKernelFplOptParam`](../files/user/pspthreadman.h.md#scekernelfploptparam)
- [`SceKernelFplInfo`](../files/user/pspthreadman.h.md#scekernelfplinfo) – Fixed pool status information.
- [`SceKernelVTimerOptParam`](../files/user/pspthreadman.h.md#scekernelvtimeroptparam)
- [`SceKernelVTimerHandler`](../files/user/pspthreadman.h.md#scekernelvtimerhandler)
- [`SceKernelVTimerHandlerWide`](../files/user/pspthreadman.h.md#scekernelvtimerhandlerwide)
- [`SceKernelVTimerInfo`](../files/user/pspthreadman.h.md#scekernelvtimerinfo)
- [`SceKernelThreadEventHandler`](../files/user/pspthreadman.h.md#scekernelthreadeventhandler)
- [`SceKernelThreadEventHandlerInfo`](../files/user/pspthreadman.h.md#scekernelthreadeventhandlerinfo) – Struct for event handler info.

## Enumerations

- [`PspThreadAttributes`](../files/user/pspthreadman.h.md#enum-pspthreadattributes) – Attribute for threads.
- [`PspThreadStatus`](../files/user/pspthreadman.h.md#enum-pspthreadstatus)
- [`PspLwMutexAttributes`](../files/user/pspthreadman.h.md#enum-psplwmutexattributes) – Attribute for lightweight mutex.
- [`PspEventFlagAttributes`](../files/user/pspthreadman.h.md#enum-pspeventflagattributes) – Event flag creation attributes.
- [`PspEventFlagWaitTypes`](../files/user/pspthreadman.h.md#enum-pspeventflagwaittypes) – Event flag wait types.
- [`SceKernelIdListType`](../files/user/pspthreadman.h.md#enum-scekernelidlisttype) – Threadman types for [sceKernelGetThreadmanIdList](../files/user/pspthreadman.h.md#scekernelgetthreadmanidlist).
- [`ThreadEventIds`](../files/user/pspthreadman.h.md#enum-threadeventids)
- [`ThreadEvents`](../files/user/pspthreadman.h.md#enum-threadevents)

## Functions

- [`sceKernelCreateThread()`](../files/user/pspthreadman.h.md#scekernelcreatethread) – Create a thread.
- [`sceKernelDeleteThread()`](../files/user/pspthreadman.h.md#scekerneldeletethread) – Delate a thread.
- [`sceKernelStartThread()`](../files/user/pspthreadman.h.md#scekernelstartthread) – Start a created thread.
- [`sceKernelExitThread()`](../files/user/pspthreadman.h.md#scekernelexitthread) – Exit a thread.
- [`sceKernelExitDeleteThread()`](../files/user/pspthreadman.h.md#scekernelexitdeletethread) – Exit a thread and delete itself.
- [`sceKernelTerminateThread()`](../files/user/pspthreadman.h.md#scekernelterminatethread) – Terminate a thread.
- [`sceKernelTerminateDeleteThread()`](../files/user/pspthreadman.h.md#scekernelterminatedeletethread) – Terminate and delete a thread.
- [`sceKernelSuspendDispatchThread()`](../files/user/pspthreadman.h.md#scekernelsuspenddispatchthread) – Suspend the dispatch thread.
- [`sceKernelResumeDispatchThread()`](../files/user/pspthreadman.h.md#scekernelresumedispatchthread) – Resume the dispatch thread.
- [`sceKernelSleepThread()`](../files/user/pspthreadman.h.md#scekernelsleepthread) – Sleep thread.
- [`sceKernelSleepThreadCB()`](../files/user/pspthreadman.h.md#scekernelsleepthreadcb) – Sleep thread but service any callbacks as necessary.
- [`sceKernelWakeupThread()`](../files/user/pspthreadman.h.md#scekernelwakeupthread) – Wake a thread previously put into the sleep state.
- [`sceKernelCancelWakeupThread()`](../files/user/pspthreadman.h.md#scekernelcancelwakeupthread) – Cancel a thread that was to be woken with [sceKernelWakeupThread](../files/user/pspthreadman.h.md#scekernelwakeupthread).
- [`sceKernelSuspendThread()`](../files/user/pspthreadman.h.md#scekernelsuspendthread) – Suspend a thread.
- [`sceKernelResumeThread()`](../files/user/pspthreadman.h.md#scekernelresumethread) – Resume a thread previously put into a suspended state with [sceKernelSuspendThread](../files/user/pspthreadman.h.md#scekernelsuspendthread).
- [`sceKernelWaitThreadEnd()`](../files/user/pspthreadman.h.md#scekernelwaitthreadend) – Wait until a thread has ended.
- [`sceKernelWaitThreadEndCB()`](../files/user/pspthreadman.h.md#scekernelwaitthreadendcb) – Wait until a thread has ended and handle callbacks if necessary.
- [`sceKernelDelayThread()`](../files/user/pspthreadman.h.md#scekerneldelaythread) – Delay the current thread by a specified number of microseconds.
- [`sceKernelDelayThreadCB()`](../files/user/pspthreadman.h.md#scekerneldelaythreadcb) – Delay the current thread by a specified number of microseconds and handle any callbacks.
- [`sceKernelDelaySysClockThread()`](../files/user/pspthreadman.h.md#scekerneldelaysysclockthread) – Delay the current thread by a specified number of sysclocks.
- [`sceKernelDelaySysClockThreadCB()`](../files/user/pspthreadman.h.md#scekerneldelaysysclockthreadcb) – Delay the current thread by a specified number of sysclocks handling callbacks.
- [`sceKernelChangeCurrentThreadAttr()`](../files/user/pspthreadman.h.md#scekernelchangecurrentthreadattr) – Modify the attributes of the current thread.
- [`sceKernelChangeThreadPriority()`](../files/user/pspthreadman.h.md#scekernelchangethreadpriority) – Change the threads current priority.
- [`sceKernelRotateThreadReadyQueue()`](../files/user/pspthreadman.h.md#scekernelrotatethreadreadyqueue) – Rotate thread ready queue at a set priority.
- [`sceKernelReleaseWaitThread()`](../files/user/pspthreadman.h.md#scekernelreleasewaitthread) – Release a thread in the wait state.
- [`sceKernelGetThreadId()`](../files/user/pspthreadman.h.md#scekernelgetthreadid) – Get the current thread Id.
- [`sceKernelGetThreadCurrentPriority()`](../files/user/pspthreadman.h.md#scekernelgetthreadcurrentpriority) – Get the current priority of the thread you are in.
- [`sceKernelGetThreadExitStatus()`](../files/user/pspthreadman.h.md#scekernelgetthreadexitstatus) – Get the exit status of a thread.
- [`sceKernelCheckThreadStack()`](../files/user/pspthreadman.h.md#scekernelcheckthreadstack) – Check the thread stack?
- [`sceKernelGetThreadStackFreeSize()`](../files/user/pspthreadman.h.md#scekernelgetthreadstackfreesize) – Get the free stack size for a thread.
- [`sceKernelReferThreadStatus()`](../files/user/pspthreadman.h.md#scekernelreferthreadstatus) – Get the status information for the specified thread.
- [`sceKernelReferThreadRunStatus()`](../files/user/pspthreadman.h.md#scekernelreferthreadrunstatus) – Retrive the runtime status of a thread.
- [`sceKernelCreateSema()`](../files/user/pspthreadman.h.md#scekernelcreatesema) – Creates a new semaphore.
- [`sceKernelDeleteSema()`](../files/user/pspthreadman.h.md#scekerneldeletesema) – Destroy a semaphore.
- [`sceKernelSignalSema()`](../files/user/pspthreadman.h.md#scekernelsignalsema) – Send a signal to a semaphore.
- [`sceKernelWaitSema()`](../files/user/pspthreadman.h.md#scekernelwaitsema) – Lock a semaphore.
- [`sceKernelWaitSemaCB()`](../files/user/pspthreadman.h.md#scekernelwaitsemacb) – Lock a semaphore a handle callbacks if necessary.
- [`sceKernelPollSema()`](../files/user/pspthreadman.h.md#scekernelpollsema) – Poll a sempahore.
- [`sceKernelReferSemaStatus()`](../files/user/pspthreadman.h.md#scekernelrefersemastatus) – Retrieve information about a semaphore.
- [`sceKernelCreateLwMutex()`](../files/user/pspthreadman.h.md#scekernelcreatelwmutex) – Create a lightweight mutex.
- [`sceKernelDeleteLwMutex()`](../files/user/pspthreadman.h.md#scekerneldeletelwmutex) – Delete a lightweight mutex.
- [`sceKernelTryLockLwMutex()`](../files/user/pspthreadman.h.md#scekerneltrylocklwmutex) – Try to lock a lightweight mutex.
- [`sceKernelLockLwMutex()`](../files/user/pspthreadman.h.md#scekernellocklwmutex) – Lock a lightweight mutex.
- [`sceKernelUnlockLwMutex()`](../files/user/pspthreadman.h.md#scekernelunlocklwmutex) – Lock a lightweight mutex.
- [`sceKernelCreateEventFlag()`](../files/user/pspthreadman.h.md#scekernelcreateeventflag) – Create an event flag.
- [`sceKernelSetEventFlag()`](../files/user/pspthreadman.h.md#scekernelseteventflag) – Set an event flag bit pattern.
- [`sceKernelClearEventFlag()`](../files/user/pspthreadman.h.md#scekernelcleareventflag) – Clear a event flag bit pattern.
- [`sceKernelPollEventFlag()`](../files/user/pspthreadman.h.md#scekernelpolleventflag) – Poll an event flag for a given bit pattern.
- [`sceKernelWaitEventFlag()`](../files/user/pspthreadman.h.md#scekernelwaiteventflag) – Wait for an event flag for a given bit pattern.
- [`sceKernelWaitEventFlagCB()`](../files/user/pspthreadman.h.md#scekernelwaiteventflagcb) – Wait for an event flag for a given bit pattern with callback.
- [`sceKernelDeleteEventFlag()`](../files/user/pspthreadman.h.md#scekerneldeleteeventflag) – Delete an event flag.
- [`sceKernelReferEventFlagStatus()`](../files/user/pspthreadman.h.md#scekernelrefereventflagstatus) – Get the status of an event flag.
- [`sceKernelCreateMbx()`](../files/user/pspthreadman.h.md#scekernelcreatembx) – Creates a new messagebox.
- [`sceKernelDeleteMbx()`](../files/user/pspthreadman.h.md#scekerneldeletembx) – Destroy a messagebox.
- [`sceKernelSendMbx()`](../files/user/pspthreadman.h.md#scekernelsendmbx) – Send a message to a messagebox.
- [`sceKernelReceiveMbx()`](../files/user/pspthreadman.h.md#scekernelreceivembx) – Wait for a message to arrive in a messagebox.
- [`sceKernelReceiveMbxCB()`](../files/user/pspthreadman.h.md#scekernelreceivembxcb) – Wait for a message to arrive in a messagebox and handle callbacks if necessary.
- [`sceKernelPollMbx()`](../files/user/pspthreadman.h.md#scekernelpollmbx) – Check if a message has arrived in a messagebox.
- [`sceKernelCancelReceiveMbx()`](../files/user/pspthreadman.h.md#scekernelcancelreceivembx) – Abort all wait operations on a messagebox.
- [`sceKernelReferMbxStatus()`](../files/user/pspthreadman.h.md#scekernelrefermbxstatus) – Retrieve information about a messagebox.
- [`sceKernelSetAlarm()`](../files/user/pspthreadman.h.md#scekernelsetalarm) – Set an alarm.
- [`sceKernelSetSysClockAlarm()`](../files/user/pspthreadman.h.md#scekernelsetsysclockalarm) – Set an alarm using a [SceKernelSysClock](../files/user/pspthreadman.h.md#struct-scekernelsysclock) structure for the time.
- [`sceKernelCancelAlarm()`](../files/user/pspthreadman.h.md#scekernelcancelalarm) – Cancel a pending alarm.
- [`sceKernelReferAlarmStatus()`](../files/user/pspthreadman.h.md#scekernelreferalarmstatus) – Refer the status of a created alarm.
- [`sceKernelCreateCallback()`](../files/user/pspthreadman.h.md#scekernelcreatecallback) – Create callback.
- [`sceKernelReferCallbackStatus()`](../files/user/pspthreadman.h.md#scekernelrefercallbackstatus) – Gets the status of a specified callback.
- [`sceKernelDeleteCallback()`](../files/user/pspthreadman.h.md#scekerneldeletecallback) – Delete a callback.
- [`sceKernelNotifyCallback()`](../files/user/pspthreadman.h.md#scekernelnotifycallback) – Notify a callback.
- [`sceKernelCancelCallback()`](../files/user/pspthreadman.h.md#scekernelcancelcallback) – Cancel a callback ?
- [`sceKernelGetCallbackCount()`](../files/user/pspthreadman.h.md#scekernelgetcallbackcount) – Get the callback count.
- [`sceKernelCheckCallback()`](../files/user/pspthreadman.h.md#scekernelcheckcallback) – Check callback ?
- [`sceKernelGetThreadmanIdList()`](../files/user/pspthreadman.h.md#scekernelgetthreadmanidlist) – Get a list of UIDs from threadman.
- [`sceKernelReferSystemStatus()`](../files/user/pspthreadman.h.md#scekernelrefersystemstatus) – Get the current system status.
- [`sceKernelCreateMsgPipe()`](../files/user/pspthreadman.h.md#scekernelcreatemsgpipe) – Create a message pipe.
- [`sceKernelDeleteMsgPipe()`](../files/user/pspthreadman.h.md#scekerneldeletemsgpipe) – Delete a message pipe.
- [`sceKernelSendMsgPipe()`](../files/user/pspthreadman.h.md#scekernelsendmsgpipe) – Send a message to a pipe.
- [`sceKernelSendMsgPipeCB()`](../files/user/pspthreadman.h.md#scekernelsendmsgpipecb) – Send a message to a pipe (with callback)
- [`sceKernelTrySendMsgPipe()`](../files/user/pspthreadman.h.md#scekerneltrysendmsgpipe) – Try to send a message to a pipe.
- [`sceKernelReceiveMsgPipe()`](../files/user/pspthreadman.h.md#scekernelreceivemsgpipe) – Receive a message from a pipe.
- [`sceKernelReceiveMsgPipeCB()`](../files/user/pspthreadman.h.md#scekernelreceivemsgpipecb) – Receive a message from a pipe (with callback)
- [`sceKernelTryReceiveMsgPipe()`](../files/user/pspthreadman.h.md#scekerneltryreceivemsgpipe) – Receive a message from a pipe.
- [`sceKernelCancelMsgPipe()`](../files/user/pspthreadman.h.md#scekernelcancelmsgpipe) – Cancel a message pipe.
- [`sceKernelReferMsgPipeStatus()`](../files/user/pspthreadman.h.md#scekernelrefermsgpipestatus) – Get the status of a Message Pipe.
- [`sceKernelCreateVpl()`](../files/user/pspthreadman.h.md#scekernelcreatevpl) – Create a variable pool.
- [`sceKernelDeleteVpl()`](../files/user/pspthreadman.h.md#scekerneldeletevpl) – Delete a variable pool.
- [`sceKernelAllocateVpl()`](../files/user/pspthreadman.h.md#scekernelallocatevpl) – Allocate from the pool.
- [`sceKernelAllocateVplCB()`](../files/user/pspthreadman.h.md#scekernelallocatevplcb) – Allocate from the pool (with callback)
- [`sceKernelTryAllocateVpl()`](../files/user/pspthreadman.h.md#scekerneltryallocatevpl) – Try to allocate from the pool.
- [`sceKernelFreeVpl()`](../files/user/pspthreadman.h.md#scekernelfreevpl) – Free a block.
- [`sceKernelCancelVpl()`](../files/user/pspthreadman.h.md#scekernelcancelvpl) – Cancel a pool.
- [`sceKernelReferVplStatus()`](../files/user/pspthreadman.h.md#scekernelrefervplstatus) – Get the status of an VPL.
- [`sceKernelCreateFpl()`](../files/user/pspthreadman.h.md#scekernelcreatefpl) – Create a fixed pool.
- [`sceKernelDeleteFpl()`](../files/user/pspthreadman.h.md#scekerneldeletefpl) – Delete a fixed pool.
- [`sceKernelAllocateFpl()`](../files/user/pspthreadman.h.md#scekernelallocatefpl) – Allocate from the pool.
- [`sceKernelAllocateFplCB()`](../files/user/pspthreadman.h.md#scekernelallocatefplcb) – Allocate from the pool (with callback)
- [`sceKernelTryAllocateFpl()`](../files/user/pspthreadman.h.md#scekerneltryallocatefpl) – Try to allocate from the pool.
- [`sceKernelFreeFpl()`](../files/user/pspthreadman.h.md#scekernelfreefpl) – Free a block.
- [`sceKernelCancelFpl()`](../files/user/pspthreadman.h.md#scekernelcancelfpl) – Cancel a pool.
- [`sceKernelReferFplStatus()`](../files/user/pspthreadman.h.md#scekernelreferfplstatus) – Get the status of an FPL.
- [`_sceKernelReturnFromTimerHandler()`](../files/user/pspthreadman.h.md#_scekernelreturnfromtimerhandler) – Return from a timer handler (doesn't seem to do alot)
- [`_sceKernelReturnFromCallback()`](../files/user/pspthreadman.h.md#_scekernelreturnfromcallback) – Return from a callback (used as a syscall for the return of the callback function)
- [`sceKernelUSec2SysClock()`](../files/user/pspthreadman.h.md#scekernelusec2sysclock) – Convert a number of microseconds to a [SceKernelSysClock](../files/user/pspthreadman.h.md#struct-scekernelsysclock) structure.
- [`sceKernelUSec2SysClockWide()`](../files/user/pspthreadman.h.md#scekernelusec2sysclockwide) – Convert a number of microseconds to a wide time.
- [`sceKernelSysClock2USec()`](../files/user/pspthreadman.h.md#scekernelsysclock2usec) – Convert a [SceKernelSysClock](../files/user/pspthreadman.h.md#struct-scekernelsysclock) structure to microseconds.
- [`sceKernelSysClock2USecWide()`](../files/user/pspthreadman.h.md#scekernelsysclock2usecwide) – Convert a wide time to microseconds.
- [`sceKernelGetSystemTime()`](../files/user/pspthreadman.h.md#scekernelgetsystemtime) – Get the system time.
- [`sceKernelGetSystemTimeWide()`](../files/user/pspthreadman.h.md#scekernelgetsystemtimewide) – Get the system time (wide version)
- [`sceKernelGetSystemTimeLow()`](../files/user/pspthreadman.h.md#scekernelgetsystemtimelow) – Get the low 32bits of the current system time.
- [`sceKernelCreateVTimer()`](../files/user/pspthreadman.h.md#scekernelcreatevtimer) – Create a virtual timer.
- [`sceKernelDeleteVTimer()`](../files/user/pspthreadman.h.md#scekerneldeletevtimer) – Delete a virtual timer.
- [`sceKernelGetVTimerBase()`](../files/user/pspthreadman.h.md#scekernelgetvtimerbase) – Get the timer base.
- [`sceKernelGetVTimerBaseWide()`](../files/user/pspthreadman.h.md#scekernelgetvtimerbasewide) – Get the timer base (wide format)
- [`sceKernelGetVTimerTime()`](../files/user/pspthreadman.h.md#scekernelgetvtimertime) – Get the timer time.
- [`sceKernelGetVTimerTimeWide()`](../files/user/pspthreadman.h.md#scekernelgetvtimertimewide) – Get the timer time (wide format)
- [`sceKernelSetVTimerTime()`](../files/user/pspthreadman.h.md#scekernelsetvtimertime) – Set the timer time.
- [`sceKernelSetVTimerTimeWide()`](../files/user/pspthreadman.h.md#scekernelsetvtimertimewide) – Set the timer time (wide format)
- [`sceKernelStartVTimer()`](../files/user/pspthreadman.h.md#scekernelstartvtimer) – Start a virtual timer.
- [`sceKernelStopVTimer()`](../files/user/pspthreadman.h.md#scekernelstopvtimer) – Stop a virtual timer.
- [`sceKernelSetVTimerHandler()`](../files/user/pspthreadman.h.md#scekernelsetvtimerhandler) – Set the timer handler.
- [`sceKernelSetVTimerHandlerWide()`](../files/user/pspthreadman.h.md#scekernelsetvtimerhandlerwide) – Set the timer handler (wide mode)
- [`sceKernelCancelVTimerHandler()`](../files/user/pspthreadman.h.md#scekernelcancelvtimerhandler) – Cancel the timer handler.
- [`sceKernelReferVTimerStatus()`](../files/user/pspthreadman.h.md#scekernelrefervtimerstatus) – Get the status of a VTimer.
- [`_sceKernelExitThread()`](../files/user/pspthreadman.h.md#_scekernelexitthread) – Exit the thread (probably used as the syscall when the main thread returns.
- [`sceKernelGetThreadmanIdType()`](../files/user/pspthreadman.h.md#scekernelgetthreadmanidtype) – Get the type of a threadman uid.
- [`sceKernelRegisterThreadEventHandler()`](../files/user/pspthreadman.h.md#scekernelregisterthreadeventhandler) – Register a thread event handler.
- [`sceKernelReleaseThreadEventHandler()`](../files/user/pspthreadman.h.md#scekernelreleasethreadeventhandler) – Release a thread event handler.
- [`sceKernelReferThreadEventHandlerStatus()`](../files/user/pspthreadman.h.md#scekernelreferthreadeventhandlerstatus) – Refer the status of an thread event handler.
- [`sceKernelReferThreadProfiler()`](../files/user/pspthreadman.h.md#scekernelreferthreadprofiler) – Get the thread profiler registers.
- [`sceKernelReferGlobalProfiler()`](../files/user/pspthreadman.h.md#scekernelreferglobalprofiler) – Get the globile profiler registers.

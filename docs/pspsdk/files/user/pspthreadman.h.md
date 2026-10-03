[PSPSDK documentation](../../README.md) › Files

# user/pspthreadman.h

```c
#include <psptypes.h>
#include <pspkerneltypes.h>
#include <pspdebug.h>
```

Topics: [Thread Manager Library](../../topics/ThreadMan.md)

## Data Structures

### `struct SceKernelSysClock`

64-bit system clock type.

```c
struct SceKernelSysClock {
    SceUInt32 low;
    SceUInt32 hi;
};
```

### `struct SceKernelThreadOptParam`

Additional options used when creating threads.

| Field | Description |
|---|---|
| `SceSize size` | Size of the [SceKernelThreadOptParam](#struct-scekernelthreadoptparam) structure. |
| `SceUID stackMpid` | UID of the memory block (?) allocated for the thread's stack. |

### `struct SceKernelThreadInfo`

Structure to hold the status information for a thread.

**See also:** [sceKernelReferThreadStatus](#scekernelreferthreadstatus)

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure. |
| `char name[32]` | Nul terminated name of the thread. |
| `SceUInt attr` | Thread attributes. |
| `int status` | Thread status. |
| `SceKernelThreadEntry entry` | Thread entry point. |
| `void * stack` | Thread stack pointer. |
| `int stackSize` | Thread stack size. |
| `void * gpReg` | Pointer to the gp. |
| `int initPriority` | Initial priority. |
| `int currentPriority` | Current priority. |
| `int waitType` | Wait type. |
| `SceUID waitId` | Wait id. |
| `int wakeupCount` | Wakeup count. |
| `int exitStatus` | Exit status of the thread. |
| `SceKernelSysClock runClocks` | Number of clock cycles run. |
| `SceUInt intrPreemptCount` | Interrupt preemption count. |
| `SceUInt threadPreemptCount` | Thread preemption count. |
| `SceUInt releaseCount` | Release count. |

### `struct SceKernelThreadRunStatus`

Statistics about a running thread.

**See also:** [sceKernelReferThreadRunStatus](#scekernelreferthreadrunstatus).

```c
struct SceKernelThreadRunStatus {
    SceSize size;
    int status;
    int currentPriority;
    int waitType;
    int waitId;
    int wakeupCount;
    SceKernelSysClock runClocks;
    SceUInt intrPreemptCount;
    SceUInt threadPreemptCount;
    SceUInt releaseCount;
};
```

### `struct SceKernelSemaOptParam`

Additional options used when creating semaphores.

| Field | Description |
|---|---|
| `SceSize size` | Size of the [SceKernelSemaOptParam](#struct-scekernelsemaoptparam) structure. |

### `struct SceKernelSemaInfo`

Current state of a semaphore.

**See also:** [sceKernelReferSemaStatus](#scekernelrefersemastatus).

| Field | Description |
|---|---|
| `SceSize size` | Size of the [SceKernelSemaInfo](#struct-scekernelsemainfo) structure. |
| `char name[32]` | NUL-terminated name of the semaphore. |
| `SceUInt attr` | Attributes. |
| `int initCount` | The initial count the semaphore was created with. |
| `int currentCount` | The current count. |
| `int maxCount` | The maximum count. |
| `int numWaitThreads` | The number of threads waiting on the semaphore. |

### `struct SceLwMutexWorkarea`

Struct as workarea for lightweight mutex.

| Field | Description |
|---|---|
| `int lockLevel` | Count. |
| `SceUID lockThread` | Locking thread. |
| `int attr` | Attribute. |
| `int numWaitThreads` | Number of waiting threads. |
| `SceUID uid` | UID. |
| `int pad[3]` | Padding. |

### `struct SceKernelEventFlagInfo`

Structure to hold the event flag information.

```c
struct SceKernelEventFlagInfo {
    SceSize size;
    char name[32];
    SceUInt attr;
    SceUInt initPattern;
    SceUInt currentPattern;
    int numWaitThreads;
};
```

### `struct SceKernelEventFlagOptParam`

```c
struct SceKernelEventFlagOptParam {
    SceSize size;
};
```

### `struct SceKernelMbxOptParam`

Additional options used when creating messageboxes.

| Field | Description |
|---|---|
| `SceSize size` | Size of the [SceKernelMbxOptParam](#struct-scekernelmbxoptparam) structure. |

### `struct SceKernelMbxInfo`

Current state of a messagebox.

**See also:** [sceKernelReferMbxStatus](#scekernelrefermbxstatus).

| Field | Description |
|---|---|
| `SceSize size` | Size of the [SceKernelMbxInfo](#struct-scekernelmbxinfo) structure. |
| `char name[32]` | NUL-terminated name of the messagebox. |
| `SceUInt attr` | Attributes. |
| `int numWaitThreads` | The number of threads waiting on the messagebox. |
| `int numMessages` | Number of messages currently in the messagebox. |
| `void * firstMessage` | The message currently at the head of the queue. |

### `struct SceKernelMsgPacket`

Header for a message box packet.

| Field | Description |
|---|---|
| `struct SceKernelMsgPacket * next` | Pointer to next msg (used by the kernel) |
| `SceUChar msgPriority` | Priority ? |
| `SceUChar dummy[3]` |  |

### `struct SceKernelAlarmInfo`

Struct containing alarm info.

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure (should be set before calling :: sceKernelReferAlarmStatus. |
| `SceKernelSysClock schedule` |  |
| `SceKernelAlarmHandler handler` | Pointer to the alarm handler. |
| `void * common` | Common pointer argument. |

### `struct SceKernelCallbackInfo`

Structure to hold the status information for a callback.

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure (i.e.<br>sizeof(SceKernelCallbackInfo)) |
| `char name[32]` | The name given to the callback. |
| `SceUID threadId` | The thread id associated with the callback. |
| `SceKernelCallbackFunction callback` | Pointer to the callback function. |
| `void * common` | User supplied argument for the callback. |
| `int notifyCount` | Unknown. |
| `int notifyArg` | Unknown. |

### `struct SceKernelSystemStatus`

Structure to contain the system status returned by [sceKernelReferSystemStatus](#scekernelrefersystemstatus).

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure (should be set prior to the call) |
| `SceUInt status` | The status ? |
| `SceKernelSysClock idleClocks` | The number of cpu clocks in the idle thread. |
| `SceUInt comesOutOfIdleCount` | Number of times we resumed from idle. |
| `SceUInt threadSwitchCount` | Number of thread context switches. |
| `SceUInt vfpuSwitchCount` | Number of vfpu switches ? |

### `struct SceKernelMppInfo`

Message Pipe status info.

```c
struct SceKernelMppInfo {
    SceSize size;
    char name[32];
    SceUInt attr;
    int bufSize;
    int freeSize;
    int numSendWaitThreads;
    int numReceiveWaitThreads;
};
```

### `struct SceKernelVplOptParam`

```c
struct SceKernelVplOptParam {
    SceSize size;
};
```

### `struct SceKernelVplInfo`

Variable pool status info.

```c
struct SceKernelVplInfo {
    SceSize size;
    char name[32];
    SceUInt attr;
    int poolSize;
    int freeSize;
    int numWaitThreads;
};
```

### `struct SceKernelFplOptParam`

```c
struct SceKernelFplOptParam {
    SceSize size;
};
```

### `struct SceKernelFplInfo`

Fixed pool status information.

```c
struct SceKernelFplInfo {
    SceSize size;
    char name[32];
    SceUInt attr;
    int blockSize;
    int numBlocks;
    int freeBlocks;
    int numWaitThreads;
};
```

### `struct SceKernelVTimerOptParam`

```c
struct SceKernelVTimerOptParam {
    SceSize size;
};
```

### `struct SceKernelVTimerInfo`

```c
struct SceKernelVTimerInfo {
    SceSize size;
    char name[32];
    int active;
    SceKernelSysClock base;
    SceKernelSysClock current;
    SceKernelSysClock schedule;
    SceKernelVTimerHandler handler;
    void * common;
};
```

### `struct SceKernelThreadEventHandlerInfo`

Struct for event handler info.

```c
struct SceKernelThreadEventHandlerInfo {
    SceSize size;
    char name[32];
    SceUID threadId;
    int mask;
    SceKernelThreadEventHandler handler;
    void * common;
};
```

## Macros

### `THREAD_ATTR_VFPU`

```c
#define THREAD_ATTR_VFPU PSP_THREAD_ATTR_VFPU
```

### `THREAD_ATTR_USER`

```c
#define THREAD_ATTR_USER PSP_THREAD_ATTR_USER
```

## Typedefs

### `SceKernelSysClock`

```c
typedef struct SceKernelSysClock SceKernelSysClock;
```

64-bit system clock type.

### `SceKernelThreadOptParam`

```c
typedef struct SceKernelThreadOptParam SceKernelThreadOptParam;
```

Additional options used when creating threads.

### `SceKernelThreadInfo`

```c
typedef struct SceKernelThreadInfo SceKernelThreadInfo;
```

Structure to hold the status information for a thread.

**See also:** [sceKernelReferThreadStatus](#scekernelreferthreadstatus)

### `SceKernelThreadRunStatus`

```c
typedef struct SceKernelThreadRunStatus SceKernelThreadRunStatus;
```

Statistics about a running thread.

**See also:** [sceKernelReferThreadRunStatus](#scekernelreferthreadrunstatus).

### `SceKernelSemaOptParam`

```c
typedef struct SceKernelSemaOptParam SceKernelSemaOptParam;
```

Additional options used when creating semaphores.

### `SceKernelSemaInfo`

```c
typedef struct SceKernelSemaInfo SceKernelSemaInfo;
```

Current state of a semaphore.

**See also:** [sceKernelReferSemaStatus](#scekernelrefersemastatus).

### `SceKernelEventFlagInfo`

```c
typedef struct SceKernelEventFlagInfo SceKernelEventFlagInfo;
```

Structure to hold the event flag information.

### `SceKernelEventFlagOptParam`

```c
typedef struct SceKernelEventFlagOptParam SceKernelEventFlagOptParam;
```

### `SceKernelMbxOptParam`

```c
typedef struct SceKernelMbxOptParam SceKernelMbxOptParam;
```

Additional options used when creating messageboxes.

### `SceKernelMbxInfo`

```c
typedef struct SceKernelMbxInfo SceKernelMbxInfo;
```

Current state of a messagebox.

**See also:** [sceKernelReferMbxStatus](#scekernelrefermbxstatus).

### `SceKernelMsgPacket`

```c
typedef struct SceKernelMsgPacket SceKernelMsgPacket;
```

Header for a message box packet.

### `SceKernelAlarmHandler`

```c
typedef SceUInt(* SceKernelAlarmHandler) (void *common))(void *common);
```

Prototype for alarm handlers.

### `SceKernelAlarmInfo`

```c
typedef struct SceKernelAlarmInfo SceKernelAlarmInfo;
```

Struct containing alarm info.

### `SceKernelCallbackFunction`

```c
typedef int(* SceKernelCallbackFunction) (int arg1, int arg2, void *arg))(int arg1, int arg2, void *arg);
```

Callback function prototype.

### `SceKernelCallbackInfo`

```c
typedef struct SceKernelCallbackInfo SceKernelCallbackInfo;
```

Structure to hold the status information for a callback.

### `SceKernelIdListType`

```c
typedef enum SceKernelIdListType SceKernelIdListType;
```

Threadman types for [sceKernelGetThreadmanIdList](#scekernelgetthreadmanidlist).

### `SceKernelSystemStatus`

```c
typedef struct SceKernelSystemStatus SceKernelSystemStatus;
```

Structure to contain the system status returned by [sceKernelReferSystemStatus](#scekernelrefersystemstatus).

### `SceKernelMppInfo`

```c
typedef struct SceKernelMppInfo SceKernelMppInfo;
```

Message Pipe status info.

### `SceKernelVplOptParam`

```c
typedef struct SceKernelVplOptParam SceKernelVplOptParam;
```

### `SceKernelVplInfo`

```c
typedef struct SceKernelVplInfo SceKernelVplInfo;
```

Variable pool status info.

### `SceKernelFplOptParam`

```c
typedef struct SceKernelFplOptParam SceKernelFplOptParam;
```

### `SceKernelFplInfo`

```c
typedef struct SceKernelFplInfo SceKernelFplInfo;
```

Fixed pool status information.

### `SceKernelVTimerOptParam`

```c
typedef struct SceKernelVTimerOptParam SceKernelVTimerOptParam;
```

### `SceKernelVTimerHandler`

```c
typedef SceUInt(* SceKernelVTimerHandler) (SceUID uid, SceKernelSysClock *schedule, SceKernelSysClock *current, void *common))(SceUID uid, SceKernelSysClock *schedule, SceKernelSysClock *current, void *common);
```

### `SceKernelVTimerHandlerWide`

```c
typedef SceUInt(* SceKernelVTimerHandlerWide) (SceUID uid, SceInt64 schedule, SceInt64 current, void *common))(SceUID uid, SceInt64 schedule, SceInt64 current, void *common);
```

### `SceKernelVTimerInfo`

```c
typedef struct SceKernelVTimerInfo SceKernelVTimerInfo;
```

### `SceKernelThreadEventHandler`

```c
typedef int(* SceKernelThreadEventHandler) (int mask, SceUID thid, void *common))(int mask, SceUID thid, void *common);
```

### `SceKernelThreadEventHandlerInfo`

```c
typedef struct SceKernelThreadEventHandlerInfo SceKernelThreadEventHandlerInfo;
```

Struct for event handler info.

## Enumerations

### `enum PspThreadAttributes`

Attribute for threads.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_THREAD_ATTR_VFPU` | `0x00004000` | Enable VFPU access for the thread. |
| `PSP_THREAD_ATTR_USER` | `0x80000000` | Start the thread in user mode (done automatically if the thread creating it is in user mode). |
| `PSP_THREAD_ATTR_USBWLAN` | `0xa0000000` | Thread is part of the USB/WLAN API. |
| `PSP_THREAD_ATTR_VSH` | `0xc0000000` | Thread is part of the VSH API. |
| `PSP_THREAD_ATTR_NO_FILLSTACK` | `0x00100000` | Disables filling the stack with 0xFF on creation. |
| `PSP_THREAD_ATTR_CLEAR_STACK` | `0x00200000` | Clear the stack when the thread is deleted. |

### `enum PspThreadStatus`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_THREAD_RUNNING` | `1` |  |
| `PSP_THREAD_READY` | `2` |  |
| `PSP_THREAD_WAITING` | `4` |  |
| `PSP_THREAD_SUSPEND` | `8` |  |
| `PSP_THREAD_STOPPED` | `16` |  |
| `PSP_THREAD_KILLED` | `32` |  |

### `enum PspLwMutexAttributes`

Attribute for lightweight mutex.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_LW_MUTEX_ATTR_THFIFO` | `0x0000U` | The wait thread is queued using FIFO. |
| `PSP_LW_MUTEX_ATTR_THPRI` | `0x0100U` | The wait thread is queued by thread priority . |
| `PSP_LW_MUTEX_ATTR_RECURSIVE` | `0x0200U` | A recursive lock is allowed by the thread that acquired the lightweight mutex. |

### `enum PspEventFlagAttributes`

Event flag creation attributes.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_EVENT_WAITSINGLE` | `0x00` | Allow the event flag to be waited upon by a single thread. |
| `PSP_EVENT_WAITMULTIPLE` | `0x200` | Allow the event flag to be waited upon by multiple threads. |

### `enum PspEventFlagWaitTypes`

Event flag wait types.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_EVENT_WAITAND` | `0` | Wait for all bits in the pattern to be set. |
| `PSP_EVENT_WAITOR` | `1` | Wait for one or more bits in the pattern to be set. |
| `PSP_EVENT_WAITCLEAR` | `0x20` | Clear the wait pattern when it matches. |

### `enum SceKernelIdListType`

Threadman types for [sceKernelGetThreadmanIdList](#scekernelgetthreadmanidlist).

| Enumerator | Value | Description |
|---|---|---|
| `SCE_KERNEL_TMID_Thread` | `1` |  |
| `SCE_KERNEL_TMID_Semaphore` | `2` |  |
| `SCE_KERNEL_TMID_EventFlag` | `3` |  |
| `SCE_KERNEL_TMID_Mbox` | `4` |  |
| `SCE_KERNEL_TMID_Vpl` | `5` |  |
| `SCE_KERNEL_TMID_Fpl` | `6` |  |
| `SCE_KERNEL_TMID_Mpipe` | `7` |  |
| `SCE_KERNEL_TMID_Callback` | `8` |  |
| `SCE_KERNEL_TMID_ThreadEventHandler` | `9` |  |
| `SCE_KERNEL_TMID_Alarm` | `10` |  |
| `SCE_KERNEL_TMID_VTimer` | `11` |  |
| `SCE_KERNEL_TMID_SleepThread` | `64` |  |
| `SCE_KERNEL_TMID_DelayThread` | `65` |  |
| `SCE_KERNEL_TMID_SuspendThread` | `66` |  |
| `SCE_KERNEL_TMID_DormantThread` | `67` |  |

### `enum ThreadEventIds`

| Enumerator | Value | Description |
|---|---|---|
| `THREADEVENT_ALL` | `0xFFFFFFFF` |  |
| `THREADEVENT_KERN` | `0xFFFFFFF8` |  |
| `THREADEVENT_USER` | `0xFFFFFFF0` |  |
| `THREADEVENT_CURRENT` | `0` |  |

### `enum ThreadEvents`

| Enumerator | Value | Description |
|---|---|---|
| `THREAD_CREATE` | `1` |  |
| `THREAD_START` | `2` |  |
| `THREAD_EXIT` | `4` |  |
| `THREAD_DELETE` | `8` |  |

## Functions

### `sceKernelCreateThread()`

```c
SceUID sceKernelCreateThread(const char *name, SceKernelThreadEntry entry, int initPriority, int stackSize, SceUInt attr, SceKernelThreadOptParam *option);
```

Create a thread.

**Example::**

```c
SceUID thid;
thid = sceKernelCreateThread("my_thread", threadFunc, 0x18, 0x10000, 0, NULL);
```

**Parameters:**

- `name` – An arbitrary thread name.
- `entry` – The thread function to run when started.
- `initPriority` – The initial priority of the thread. Less if higher priority.
- `stackSize` – The size of the initial stack.
- `attr` – The thread attributes, zero or more of [PspThreadAttributes](#enum-pspthreadattributes).
- `option` – Additional options specified by [SceKernelThreadOptParam](#struct-scekernelthreadoptparam).

**Returns:** UID of the created thread, or an error code.

### `sceKernelDeleteThread()`

```c
int sceKernelDeleteThread(SceUID thid);
```

Delate a thread.

**Parameters:**

- `thid` – UID of the thread to be deleted.

**Returns:** \< 0 on error.

### `sceKernelStartThread()`

```c
int sceKernelStartThread(SceUID thid, SceSize arglen, void *argp);
```

Start a created thread.

**Parameters:**

- `thid` – Thread id from sceKernelCreateThread
- `arglen` – Length of the data pointed to by argp, in bytes
- `argp` – Pointer to the arguments.

### `sceKernelExitThread()`

```c
int sceKernelExitThread(int status);
```

Exit a thread.

**Parameters:**

- `status` – Exit status.

### `sceKernelExitDeleteThread()`

```c
int sceKernelExitDeleteThread(int status);
```

Exit a thread and delete itself.

**Parameters:**

- `status` – Exit status

### `sceKernelTerminateThread()`

```c
int sceKernelTerminateThread(SceUID thid);
```

Terminate a thread.

**Parameters:**

- `thid` – UID of the thread to terminate.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelTerminateDeleteThread()`

```c
int sceKernelTerminateDeleteThread(SceUID thid);
```

Terminate and delete a thread.

**Parameters:**

- `thid` – UID of the thread to terminate and delete.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelSuspendDispatchThread()`

```c
int sceKernelSuspendDispatchThread(void);
```

Suspend the dispatch thread.

**Returns:** The current state of the dispatch thread, \< 0 on error

### `sceKernelResumeDispatchThread()`

```c
int sceKernelResumeDispatchThread(int state);
```

Resume the dispatch thread.

**Parameters:**

- `state` – The state of the dispatch thread (from [sceKernelSuspendDispatchThread](#scekernelsuspenddispatchthread))

**Returns:** 0 on success, \< 0 on error

### `sceKernelSleepThread()`

```c
int sceKernelSleepThread(void);
```

Sleep thread.

**Returns:** \< 0 on error.

### `sceKernelSleepThreadCB()`

```c
int sceKernelSleepThreadCB(void);
```

Sleep thread but service any callbacks as necessary.

**Example::**

```c
// Once all callbacks have been setup call this function
sceKernelSleepThreadCB();
```

### `sceKernelWakeupThread()`

```c
int sceKernelWakeupThread(SceUID thid);
```

Wake a thread previously put into the sleep state.

**Parameters:**

- `thid` – UID of the thread to wake.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelCancelWakeupThread()`

```c
int sceKernelCancelWakeupThread(SceUID thid);
```

Cancel a thread that was to be woken with [sceKernelWakeupThread](#scekernelwakeupthread).

**Parameters:**

- `thid` – UID of the thread to cancel.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelSuspendThread()`

```c
int sceKernelSuspendThread(SceUID thid);
```

Suspend a thread.

**Parameters:**

- `thid` – UID of the thread to suspend.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelResumeThread()`

```c
int sceKernelResumeThread(SceUID thid);
```

Resume a thread previously put into a suspended state with [sceKernelSuspendThread](#scekernelsuspendthread).

**Parameters:**

- `thid` – UID of the thread to resume.

**Returns:** Success if >= 0, an error if \< 0.

### `sceKernelWaitThreadEnd()`

```c
int sceKernelWaitThreadEnd(SceUID thid, SceUInt *timeout);
```

Wait until a thread has ended.

**Parameters:**

- `thid` – Id of the thread to wait for.
- `timeout` – Timeout in microseconds (assumed).

**Returns:** \< 0 on error.

### `sceKernelWaitThreadEndCB()`

```c
int sceKernelWaitThreadEndCB(SceUID thid, SceUInt *timeout);
```

Wait until a thread has ended and handle callbacks if necessary.

**Parameters:**

- `thid` – Id of the thread to wait for.
- `timeout` – Timeout in microseconds (assumed).

**Returns:** \< 0 on error.

### `sceKernelDelayThread()`

```c
int sceKernelDelayThread(SceUInt delay);
```

Delay the current thread by a specified number of microseconds.

**Parameters:**

- `delay` – Delay in microseconds.

**Example::**

```c
sceKernelDelayThread(1000000); // Delay for a second
```

### `sceKernelDelayThreadCB()`

```c
int sceKernelDelayThreadCB(SceUInt delay);
```

Delay the current thread by a specified number of microseconds and handle any callbacks.

**Parameters:**

- `delay` – Delay in microseconds.

**Example::**

```c
sceKernelDelayThread(1000000); // Delay for a second
```

### `sceKernelDelaySysClockThread()`

```c
int sceKernelDelaySysClockThread(SceKernelSysClock *delay);
```

Delay the current thread by a specified number of sysclocks.

**Parameters:**

- `delay` – Delay in sysclocks

**Returns:** 0 on success, \< 0 on error

### `sceKernelDelaySysClockThreadCB()`

```c
int sceKernelDelaySysClockThreadCB(SceKernelSysClock *delay);
```

Delay the current thread by a specified number of sysclocks handling callbacks.

**Parameters:**

- `delay` – Delay in sysclocks

**Returns:** 0 on success, \< 0 on error

### `sceKernelChangeCurrentThreadAttr()`

```c
int sceKernelChangeCurrentThreadAttr(int unknown, SceUInt attr);
```

Modify the attributes of the current thread.

**Parameters:**

- `unknown` – Set to 0.
- `attr` – The thread attributes to modify. One of [PspThreadAttributes](#enum-pspthreadattributes).

**Returns:** \< 0 on error.

### `sceKernelChangeThreadPriority()`

```c
int sceKernelChangeThreadPriority(SceUID thid, int priority);
```

Change the threads current priority.

**Parameters:**

- `thid` – The ID of the thread (from sceKernelCreateThread or sceKernelGetThreadId)
- `priority` – The new priority (the lower the number the higher the priority)

**Example::**

```c
int thid = sceKernelGetThreadId();
// Change priority of current thread to 16
sceKernelChangeThreadPriority(thid, 16);
```

**Returns:** 0 if successful, otherwise the error code.

### `sceKernelRotateThreadReadyQueue()`

```c
int sceKernelRotateThreadReadyQueue(int priority);
```

Rotate thread ready queue at a set priority.

**Parameters:**

- `priority` – The priority of the queue

**Returns:** 0 on success, \< 0 on error.

### `sceKernelReleaseWaitThread()`

```c
int sceKernelReleaseWaitThread(SceUID thid);
```

Release a thread in the wait state.

**Parameters:**

- `thid` – The UID of the thread.

**Returns:** 0 on success, \< 0 on error

### `sceKernelGetThreadId()`

```c
int sceKernelGetThreadId(void);
```

Get the current thread Id.

**Returns:** The thread id of the calling thread.

### `sceKernelGetThreadCurrentPriority()`

```c
int sceKernelGetThreadCurrentPriority(void);
```

Get the current priority of the thread you are in.

**Returns:** The current thread priority

### `sceKernelGetThreadExitStatus()`

```c
int sceKernelGetThreadExitStatus(SceUID thid);
```

Get the exit status of a thread.

**Parameters:**

- `thid` – The UID of the thread to check.

**Returns:** The exit status

### `sceKernelCheckThreadStack()`

```c
int sceKernelCheckThreadStack(void);
```

Check the thread stack?

**Returns:** Unknown.

### `sceKernelGetThreadStackFreeSize()`

```c
int sceKernelGetThreadStackFreeSize(SceUID thid);
```

Get the free stack size for a thread.

**Parameters:**

- `thid` – The thread ID. Seem to take current thread if set to 0.

**Returns:** The free size.

### `sceKernelReferThreadStatus()`

```c
int sceKernelReferThreadStatus(SceUID thid, SceKernelThreadInfo *info);
```

Get the status information for the specified thread.

**Parameters:**

- `thid` – Id of the thread to get status
- `info` – Pointer to the info structure to receive the data. Note: The structures size field should be set to sizeof(SceKernelThreadInfo) before calling this function.

**Example::**

```c
SceKernelThreadInfo status;
status.size = sizeof(SceKernelThreadInfo);
if(sceKernelReferThreadStatus(thid, &status) == 0)
{ Do something... }
```

**Returns:** 0 if successful, otherwise the error code.

### `sceKernelReferThreadRunStatus()`

```c
int sceKernelReferThreadRunStatus(SceUID thid, SceKernelThreadRunStatus *status);
```

Retrive the runtime status of a thread.

**Parameters:**

- `thid` – UID of the thread to retrive status.
- `status` – Pointer to a [SceKernelThreadRunStatus](#struct-scekernelthreadrunstatus) struct to receive the runtime status.

**Returns:** 0 if successful, otherwise the error code.

### `sceKernelCreateSema()`

```c
SceUID sceKernelCreateSema(const char *name, SceUInt attr, int initVal, int maxVal, SceKernelSemaOptParam *option);
```

Creates a new semaphore.

**Example::**

```c
int semaid;
semaid = sceKernelCreateSema("MyMutex", 0, 1, 1, 0);
```

**Parameters:**

- `name` – Specifies the name of the sema
- `attr` – Sema attribute flags (normally set to 0)
- `initVal` – Sema initial value
- `maxVal` – Sema maximum value
- `option` – Sema options (normally set to 0)

**Returns:** A semaphore id

### `sceKernelDeleteSema()`

```c
int sceKernelDeleteSema(SceUID semaid);
```

Destroy a semaphore.

**Parameters:**

- `semaid` – The semaid returned from a previous create call.

**Returns:** Returns the value 0 if its succesful otherwise -1

### `sceKernelSignalSema()`

```c
int sceKernelSignalSema(SceUID semaid, int signal);
```

Send a signal to a semaphore.

**Example::**

```c
// Signal the sema
sceKernelSignalSema(semaid, 1);
```

**Parameters:**

- `semaid` – The sema id returned from sceKernelCreateSema
- `signal` – The amount to signal the sema (i.e. if 2 then increment the sema by 2)

**Returns:** \< 0 On error.

### `sceKernelWaitSema()`

```c
int sceKernelWaitSema(SceUID semaid, int signal, SceUInt *timeout);
```

Lock a semaphore.

**Example::**

```c
sceKernelWaitSema(semaid, 1, 0);
```

**Parameters:**

- `semaid` – The sema id returned from sceKernelCreateSema
- `signal` – The value to wait for (i.e. if 1 then wait till reaches a signal state of 1)
- `timeout` – Timeout in microseconds (assumed).

**Returns:** \< 0 on error.

### `sceKernelWaitSemaCB()`

```c
int sceKernelWaitSemaCB(SceUID semaid, int signal, SceUInt *timeout);
```

Lock a semaphore a handle callbacks if necessary.

**Example::**

```c
sceKernelWaitSemaCB(semaid, 1, 0);
```

**Parameters:**

- `semaid` – The sema id returned from sceKernelCreateSema
- `signal` – The value to wait for (i.e. if 1 then wait till reaches a signal state of 1)
- `timeout` – Timeout in microseconds (assumed).

**Returns:** \< 0 on error.

### `sceKernelPollSema()`

```c
int sceKernelPollSema(SceUID semaid, int signal);
```

Poll a sempahore.

**Parameters:**

- `semaid` – UID of the semaphore to poll.
- `signal` – The value to test for.

**Returns:** \< 0 on error.

### `sceKernelReferSemaStatus()`

```c
int sceKernelReferSemaStatus(SceUID semaid, SceKernelSemaInfo *info);
```

Retrieve information about a semaphore.

**Parameters:**

- `semaid` – UID of the semaphore to retrieve info for.
- `info` – Pointer to a [SceKernelSemaInfo](#struct-scekernelsemainfo) struct to receive the info.

**Returns:** \< 0 on error.

### `sceKernelCreateLwMutex()`

```c
int sceKernelCreateLwMutex(SceLwMutexWorkarea *workarea, const char *name, SceUInt32 attr, int initialCount, u32 *optionsPtr);
```

Create a lightweight mutex.

**Parameters:**

- `workarea` – The pointer to the workarea
- `name` – The name of the lightweight mutex
- `attr` – The LwMutex attributes, zero or more of [PspLwMutexAttributes](#enum-psplwmutexattributes).
- `initialCount` – THe inital value of the mutex
- `optionsPtr` – Other options for mutex

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

### `sceKernelDeleteLwMutex()`

```c
int sceKernelDeleteLwMutex(SceLwMutexWorkarea *workarea);
```

Delete a lightweight mutex.

**Parameters:**

- `workarea` – The pointer to the workarea

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

### `sceKernelTryLockLwMutex()`

```c
int sceKernelTryLockLwMutex(SceLwMutexWorkarea *workarea, int lockCount);
```

Try to lock a lightweight mutex.

**Parameters:**

- `workarea` – The pointer to the workarea
- `lockCount` – value of increase the lock counter

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

### `sceKernelLockLwMutex()`

```c
int sceKernelLockLwMutex(SceLwMutexWorkarea *workarea, int lockCount, unsigned int *pTimeout);
```

Lock a lightweight mutex.

**Parameters:**

- `workarea` – The pointer to the workarea
- `lockCount` – value of increase the lock counter
- `pTimeout` – The pointer for timeout waiting

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

### `sceKernelUnlockLwMutex()`

```c
int sceKernelUnlockLwMutex(SceLwMutexWorkarea *workarea, int lockCount);
```

Lock a lightweight mutex.

**Parameters:**

- `workarea` – The pointer to the workarea
- `lockCount` – value of decrease the lock counter

**Returns:** 0 on success, otherwise one of [PspKernelErrorCodes](pspkerror.h.md#enum-pspkernelerrorcodes)

### `sceKernelCreateEventFlag()`

```c
SceUID sceKernelCreateEventFlag(const char *name, int attr, int bits, SceKernelEventFlagOptParam *opt);
```

Create an event flag.

**Parameters:**

- `name` – The name of the event flag.
- `attr` – Attributes from [PspEventFlagAttributes](#enum-pspeventflagattributes)
- `bits` – Initial bit pattern.
- `opt` – Options, set to NULL

**Returns:** \< 0 on error. >= 0 event flag id.

**Example::**

```c
int evid;
evid = sceKernelCreateEventFlag("wait_event", 0, 0, 0);
```

### `sceKernelSetEventFlag()`

```c
int sceKernelSetEventFlag(SceUID evid, u32 bits);
```

Set an event flag bit pattern.

**Parameters:**

- `evid` – The event id returned by sceKernelCreateEventFlag.
- `bits` – The bit pattern to set.

**Returns:** \< 0 On error

### `sceKernelClearEventFlag()`

```c
int sceKernelClearEventFlag(SceUID evid, u32 bits);
```

Clear a event flag bit pattern.

**Parameters:**

- `evid` – The event id returned by [sceKernelCreateEventFlag](#scekernelcreateeventflag)
- `bits` – The bits to clean

**Returns:** \< 0 on Error

### `sceKernelPollEventFlag()`

```c
int sceKernelPollEventFlag(int evid, u32 bits, u32 wait, u32 *outBits);
```

Poll an event flag for a given bit pattern.

**Parameters:**

- `evid` – The event id returned by sceKernelCreateEventFlag.
- `bits` – The bit pattern to poll for.
- `wait` – Wait type, one or more of [PspEventFlagWaitTypes](#enum-pspeventflagwaittypes) or'ed together
- `outBits` – The bit pattern that was matched.

**Returns:** \< 0 On error

### `sceKernelWaitEventFlag()`

```c
int sceKernelWaitEventFlag(int evid, u32 bits, u32 wait, u32 *outBits, SceUInt *timeout);
```

Wait for an event flag for a given bit pattern.

**Parameters:**

- `evid` – The event id returned by sceKernelCreateEventFlag.
- `bits` – The bit pattern to poll for.
- `wait` – Wait type, one or more of [PspEventFlagWaitTypes](#enum-pspeventflagwaittypes) or'ed together
- `outBits` – The bit pattern that was matched.
- `timeout` – Timeout in microseconds

**Returns:** \< 0 On error

### `sceKernelWaitEventFlagCB()`

```c
int sceKernelWaitEventFlagCB(int evid, u32 bits, u32 wait, u32 *outBits, SceUInt *timeout);
```

Wait for an event flag for a given bit pattern with callback.

**Parameters:**

- `evid` – The event id returned by sceKernelCreateEventFlag.
- `bits` – The bit pattern to poll for.
- `wait` – Wait type, one or more of [PspEventFlagWaitTypes](#enum-pspeventflagwaittypes) or'ed together
- `outBits` – The bit pattern that was matched.
- `timeout` – Timeout in microseconds

**Returns:** \< 0 On error

### `sceKernelDeleteEventFlag()`

```c
int sceKernelDeleteEventFlag(int evid);
```

Delete an event flag.

**Parameters:**

- `evid` – The event id returned by sceKernelCreateEventFlag.

**Returns:** \< 0 On error

### `sceKernelReferEventFlagStatus()`

```c
int sceKernelReferEventFlagStatus(SceUID event, SceKernelEventFlagInfo *status);
```

Get the status of an event flag.

**Parameters:**

- `event` – The UID of the event.
- `status` – A pointer to a [SceKernelEventFlagInfo](#struct-scekerneleventflaginfo) structure.

**Returns:** \< 0 on error.

### `sceKernelCreateMbx()`

```c
SceUID sceKernelCreateMbx(const char *name, SceUInt attr, SceKernelMbxOptParam *option);
```

Creates a new messagebox.

**Example::**

```c
int mbxid;
mbxid = sceKernelCreateMbx("MyMessagebox", 0, NULL);
```

**Parameters:**

- `name` – Specifies the name of the mbx
- `attr` – Mbx attribute flags (normally set to 0)
- `option` – Mbx options (normally set to NULL)

**Returns:** A messagebox id

### `sceKernelDeleteMbx()`

```c
int sceKernelDeleteMbx(SceUID mbxid);
```

Destroy a messagebox.

**Parameters:**

- `mbxid` – The mbxid returned from a previous create call.

**Returns:** Returns the value 0 if its succesful otherwise an error code

### `sceKernelSendMbx()`

```c
int sceKernelSendMbx(SceUID mbxid, void *message);
```

Send a message to a messagebox.

**Example::**

```c
struct MyMessage {
        SceKernelMsgPacket header;
        char text[8];
};

struct MyMessage msg = { {0}, "Hello" };
// Send the message
sceKernelSendMbx(mbxid, (void*) &msg);
```

**Parameters:**

- `mbxid` – The mbx id returned from sceKernelCreateMbx
- `message` – A message to be forwarded to the receiver. The start of the message should be the [SceKernelMsgPacket](#struct-scekernelmsgpacket) structure, the rest

**Returns:** \< 0 On error.

### `sceKernelReceiveMbx()`

```c
int sceKernelReceiveMbx(SceUID mbxid, void **pmessage, SceUInt *timeout);
```

Wait for a message to arrive in a messagebox.

**Example::**

```c
void *msg;
sceKernelReceiveMbx(mbxid, &msg, NULL);
```

**Parameters:**

- `mbxid` – The mbx id returned from sceKernelCreateMbx
- `pmessage` – A pointer to where a pointer to the received message should be stored
- `timeout` – Timeout in microseconds

**Returns:** \< 0 on error.

### `sceKernelReceiveMbxCB()`

```c
int sceKernelReceiveMbxCB(SceUID mbxid, void **pmessage, SceUInt *timeout);
```

Wait for a message to arrive in a messagebox and handle callbacks if necessary.

**Example::**

```c
void *msg;
sceKernelReceiveMbxCB(mbxid, &msg, NULL);
```

**Parameters:**

- `mbxid` – The mbx id returned from sceKernelCreateMbx
- `pmessage` – A pointer to where a pointer to the received message should be stored
- `timeout` – Timeout in microseconds

**Returns:** \< 0 on error.

### `sceKernelPollMbx()`

```c
int sceKernelPollMbx(SceUID mbxid, void **pmessage);
```

Check if a message has arrived in a messagebox.

**Example::**

```c
void *msg;
sceKernelPollMbx(mbxid, &msg);
```

**Parameters:**

- `mbxid` – The mbx id returned from sceKernelCreateMbx
- `pmessage` – A pointer to where a pointer to the received message should be stored

**Returns:** \< 0 on error (SCE_KERNEL_ERROR_MBOX_NOMSG if the mbx is empty).

### `sceKernelCancelReceiveMbx()`

```c
int sceKernelCancelReceiveMbx(SceUID mbxid, int *pnum);
```

Abort all wait operations on a messagebox.

**Example::**

```c
sceKernelCancelReceiveMbx(mbxid, NULL);
```

**Parameters:**

- `mbxid` – The mbx id returned from sceKernelCreateMbx
- `pnum` – A pointer to where the number of threads which were waiting on the mbx should be stored (NULL if you don't care)

**Returns:** \< 0 on error

### `sceKernelReferMbxStatus()`

```c
int sceKernelReferMbxStatus(SceUID mbxid, SceKernelMbxInfo *info);
```

Retrieve information about a messagebox.

**Parameters:**

- `mbxid` – UID of the messagebox to retrieve info for.
- `info` – Pointer to a [SceKernelMbxInfo](#struct-scekernelmbxinfo) struct to receive the info.

**Returns:** \< 0 on error.

### `sceKernelSetAlarm()`

```c
SceUID sceKernelSetAlarm(SceUInt clock, SceKernelAlarmHandler handler, void *common);
```

Set an alarm.

**Parameters:**

- `clock` – The number of micro seconds till the alarm occurrs.
- `handler` – Pointer to a [SceKernelAlarmHandler](#scekernelalarmhandler)
- `common` – Common pointer for the alarm handler

**Returns:** A UID representing the created alarm, \< 0 on error.

### `sceKernelSetSysClockAlarm()`

```c
SceUID sceKernelSetSysClockAlarm(SceKernelSysClock *clock, SceKernelAlarmHandler handler, void *common);
```

Set an alarm using a [SceKernelSysClock](#struct-scekernelsysclock) structure for the time.

**Parameters:**

- `clock` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure
- `handler` – Pointer to a [SceKernelAlarmHandler](#scekernelalarmhandler)
- `common` – Common pointer for the alarm handler.

**Returns:** A UID representing the created alarm, \< 0 on error.

### `sceKernelCancelAlarm()`

```c
int sceKernelCancelAlarm(SceUID alarmid);
```

Cancel a pending alarm.

**Parameters:**

- `alarmid` – UID of the alarm to cancel.

**Returns:** 0 on success, \< 0 on error.

### `sceKernelReferAlarmStatus()`

```c
int sceKernelReferAlarmStatus(SceUID alarmid, SceKernelAlarmInfo *info);
```

Refer the status of a created alarm.

**Parameters:**

- `alarmid` – UID of the alarm to get the info of
- `info` – Pointer to a [SceKernelAlarmInfo](#struct-scekernelalarminfo) structure

**Returns:** 0 on success, \< 0 on error.

### `sceKernelCreateCallback()`

```c
int sceKernelCreateCallback(const char *name, SceKernelCallbackFunction func, void *arg);
```

Create callback.

**Example::**

```c
int cbid;
cbid = sceKernelCreateCallback("Exit Callback", exit_cb, NULL);
```

**Parameters:**

- `name` – A textual name for the callback
- `func` – A pointer to a function that will be called as the callback
- `arg` – Argument for the callback ?

**Returns:** >= 0 A callback id which can be used in subsequent functions, \< 0 an error.

### `sceKernelReferCallbackStatus()`

```c
int sceKernelReferCallbackStatus(SceUID cb, SceKernelCallbackInfo *status);
```

Gets the status of a specified callback.

**Parameters:**

- `cb` – The UID of the callback to refer.
- `status` – Pointer to a status structure. The size parameter should be initialised before calling.

**Returns:** \< 0 on error.

### `sceKernelDeleteCallback()`

```c
int sceKernelDeleteCallback(SceUID cb);
```

Delete a callback.

**Parameters:**

- `cb` – The UID of the specified callback

**Returns:** 0 on success, \< 0 on error

### `sceKernelNotifyCallback()`

```c
int sceKernelNotifyCallback(SceUID cb, int arg2);
```

Notify a callback.

**Parameters:**

- `cb` – The UID of the specified callback
- `arg2` – Passed as arg2 into the callback function

**Returns:** 0 on success, \< 0 on error

### `sceKernelCancelCallback()`

```c
int sceKernelCancelCallback(SceUID cb);
```

Cancel a callback ?

**Parameters:**

- `cb` – The UID of the specified callback

**Returns:** 0 on succes, \< 0 on error

### `sceKernelGetCallbackCount()`

```c
int sceKernelGetCallbackCount(SceUID cb);
```

Get the callback count.

**Parameters:**

- `cb` – The UID of the specified callback

**Returns:** The callback count, \< 0 on error

### `sceKernelCheckCallback()`

```c
int sceKernelCheckCallback(void);
```

Check callback ?

**Returns:** Something or another

### `sceKernelGetThreadmanIdList()`

```c
int sceKernelGetThreadmanIdList(SceKernelIdListType type, SceUID *readbuf, int readbufsize, int *idcount);
```

Get a list of UIDs from threadman.

Allows you to enumerate resources such as threads or semaphores.

**Parameters:**

- `type` – The type of resource to list, one of [SceKernelIdListType](#enum-scekernelidlisttype).
- `readbuf` – A pointer to a buffer to store the list.
- `readbufsize` – The size of the buffer in SceUID units.
- `idcount` – Pointer to an integer in which to return the number of ids in the list.

**Returns:** \< 0 on error. Either 0 or the same as idcount on success.

### `sceKernelReferSystemStatus()`

```c
int sceKernelReferSystemStatus(SceKernelSystemStatus *status);
```

Get the current system status.

**Parameters:**

- `status` – Pointer to a [SceKernelSystemStatus](#struct-scekernelsystemstatus) structure.

**Returns:** \< 0 on error.

### `sceKernelCreateMsgPipe()`

```c
SceUID sceKernelCreateMsgPipe(const char *name, int part, int attr, void *unk1, void *opt);
```

Create a message pipe.

**Parameters:**

- `name` – Name of the pipe
- `part` – ID of the memory partition
- `attr` – Set to 0?
- `unk1` – Unknown
- `opt` – Message pipe options (set to NULL)

**Returns:** The UID of the created pipe, \< 0 on error

### `sceKernelDeleteMsgPipe()`

```c
int sceKernelDeleteMsgPipe(SceUID uid);
```

Delete a message pipe.

**Parameters:**

- `uid` – The UID of the pipe

**Returns:** 0 on success, \< 0 on error

### `sceKernelSendMsgPipe()`

```c
int sceKernelSendMsgPipe(SceUID uid, void *message, unsigned int size, int unk1, void *unk2, unsigned int *timeout);
```

Send a message to a pipe.

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown
- `timeout` – Timeout for send

**Returns:** 0 on success, \< 0 on error

### `sceKernelSendMsgPipeCB()`

```c
int sceKernelSendMsgPipeCB(SceUID uid, void *message, unsigned int size, int unk1, void *unk2, unsigned int *timeout);
```

Send a message to a pipe (with callback)

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown
- `timeout` – Timeout for send

**Returns:** 0 on success, \< 0 on error

### `sceKernelTrySendMsgPipe()`

```c
int sceKernelTrySendMsgPipe(SceUID uid, void *message, unsigned int size, int unk1, void *unk2);
```

Try to send a message to a pipe.

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown

**Returns:** 0 on success, \< 0 on error

### `sceKernelReceiveMsgPipe()`

```c
int sceKernelReceiveMsgPipe(SceUID uid, void *message, unsigned int size, int unk1, void *unk2, unsigned int *timeout);
```

Receive a message from a pipe.

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown
- `timeout` – Timeout for receive

**Returns:** 0 on success, \< 0 on error

### `sceKernelReceiveMsgPipeCB()`

```c
int sceKernelReceiveMsgPipeCB(SceUID uid, void *message, unsigned int size, int unk1, void *unk2, unsigned int *timeout);
```

Receive a message from a pipe (with callback)

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown
- `timeout` – Timeout for receive

**Returns:** 0 on success, \< 0 on error

### `sceKernelTryReceiveMsgPipe()`

```c
int sceKernelTryReceiveMsgPipe(SceUID uid, void *message, unsigned int size, int unk1, void *unk2);
```

Receive a message from a pipe.

**Parameters:**

- `uid` – The UID of the pipe
- `message` – Pointer to the message
- `size` – Size of the message
- `unk1` – Unknown
- `unk2` – Unknown

**Returns:** 0 on success, \< 0 on error

### `sceKernelCancelMsgPipe()`

```c
int sceKernelCancelMsgPipe(SceUID uid, int *psend, int *precv);
```

Cancel a message pipe.

**Parameters:**

- `uid` – UID of the pipe to cancel
- `psend` – Receive number of sending threads?
- `precv` – Receive number of receiving threads?

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferMsgPipeStatus()`

```c
int sceKernelReferMsgPipeStatus(SceUID uid, SceKernelMppInfo *info);
```

Get the status of a Message Pipe.

**Parameters:**

- `uid` – The uid of the Message Pipe
- `info` – Pointer to a [SceKernelMppInfo](#struct-scekernelmppinfo) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelCreateVpl()`

```c
SceUID sceKernelCreateVpl(const char *name, int part, int attr, unsigned int size, SceKernelVplOptParam *opt);
```

Create a variable pool.

**Parameters:**

- `name` – Name of the pool
- `part` – The memory partition ID
- `attr` – Attributes
- `size` – Size of pool
- `opt` – Options (set to NULL)

**Returns:** The UID of the created pool, \< 0 on error.

### `sceKernelDeleteVpl()`

```c
int sceKernelDeleteVpl(SceUID uid);
```

Delete a variable pool.

**Parameters:**

- `uid` – The UID of the pool

**Returns:** 0 on success, \< 0 on error

### `sceKernelAllocateVpl()`

```c
int sceKernelAllocateVpl(SceUID uid, unsigned int size, void **data, unsigned int *timeout);
```

Allocate from the pool.

**Parameters:**

- `uid` – The UID of the pool
- `size` – The size to allocate
- `data` – Receives the address of the allocated data
- `timeout` – Amount of time to wait for allocation?

**Returns:** 0 on success, \< 0 on error

### `sceKernelAllocateVplCB()`

```c
int sceKernelAllocateVplCB(SceUID uid, unsigned int size, void **data, unsigned int *timeout);
```

Allocate from the pool (with callback)

**Parameters:**

- `uid` – The UID of the pool
- `size` – The size to allocate
- `data` – Receives the address of the allocated data
- `timeout` – Amount of time to wait for allocation?

**Returns:** 0 on success, \< 0 on error

### `sceKernelTryAllocateVpl()`

```c
int sceKernelTryAllocateVpl(SceUID uid, unsigned int size, void **data);
```

Try to allocate from the pool.

**Parameters:**

- `uid` – The UID of the pool
- `size` – The size to allocate
- `data` – Receives the address of the allocated data

**Returns:** 0 on success, \< 0 on error

### `sceKernelFreeVpl()`

```c
int sceKernelFreeVpl(SceUID uid, void *data);
```

Free a block.

**Parameters:**

- `uid` – The UID of the pool
- `data` – The data block to deallocate

**Returns:** 0 on success, \< 0 on error

### `sceKernelCancelVpl()`

```c
int sceKernelCancelVpl(SceUID uid, int *pnum);
```

Cancel a pool.

**Parameters:**

- `uid` – The UID of the pool
- `pnum` – Receives the number of waiting threads

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferVplStatus()`

```c
int sceKernelReferVplStatus(SceUID uid, SceKernelVplInfo *info);
```

Get the status of an VPL.

**Parameters:**

- `uid` – The uid of the VPL
- `info` – Pointer to a [SceKernelVplInfo](#struct-scekernelvplinfo) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelCreateFpl()`

```c
int sceKernelCreateFpl(const char *name, int part, int attr, unsigned int size, unsigned int blocks, SceKernelFplOptParam *opt);
```

Create a fixed pool.

**Parameters:**

- `name` – Name of the pool
- `part` – The memory partition ID
- `attr` – Attributes
- `size` – Size of pool block
- `blocks` – Number of blocks to allocate
- `opt` – Options (set to NULL)

**Returns:** The UID of the created pool, \< 0 on error.

### `sceKernelDeleteFpl()`

```c
int sceKernelDeleteFpl(SceUID uid);
```

Delete a fixed pool.

**Parameters:**

- `uid` – The UID of the pool

**Returns:** 0 on success, \< 0 on error

### `sceKernelAllocateFpl()`

```c
int sceKernelAllocateFpl(SceUID uid, void **data, unsigned int *timeout);
```

Allocate from the pool.

**Parameters:**

- `uid` – The UID of the pool
- `data` – Receives the address of the allocated data
- `timeout` – Amount of time to wait for allocation?

**Returns:** 0 on success, \< 0 on error

### `sceKernelAllocateFplCB()`

```c
int sceKernelAllocateFplCB(SceUID uid, void **data, unsigned int *timeout);
```

Allocate from the pool (with callback)

**Parameters:**

- `uid` – The UID of the pool
- `data` – Receives the address of the allocated data
- `timeout` – Amount of time to wait for allocation?

**Returns:** 0 on success, \< 0 on error

### `sceKernelTryAllocateFpl()`

```c
int sceKernelTryAllocateFpl(SceUID uid, void **data);
```

Try to allocate from the pool.

**Parameters:**

- `uid` – The UID of the pool
- `data` – Receives the address of the allocated data

**Returns:** 0 on success, \< 0 on error

### `sceKernelFreeFpl()`

```c
int sceKernelFreeFpl(SceUID uid, void *data);
```

Free a block.

**Parameters:**

- `uid` – The UID of the pool
- `data` – The data block to deallocate

**Returns:** 0 on success, \< 0 on error

### `sceKernelCancelFpl()`

```c
int sceKernelCancelFpl(SceUID uid, int *pnum);
```

Cancel a pool.

**Parameters:**

- `uid` – The UID of the pool
- `pnum` – Receives the number of waiting threads

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferFplStatus()`

```c
int sceKernelReferFplStatus(SceUID uid, SceKernelFplInfo *info);
```

Get the status of an FPL.

**Parameters:**

- `uid` – The uid of the FPL
- `info` – Pointer to a [SceKernelFplInfo](#struct-scekernelfplinfo) structure

**Returns:** 0 on success, \< 0 on error

### `_sceKernelReturnFromTimerHandler()`

```c
void _sceKernelReturnFromTimerHandler(void);
```

Return from a timer handler (doesn't seem to do alot)

### `_sceKernelReturnFromCallback()`

```c
void _sceKernelReturnFromCallback(void);
```

Return from a callback (used as a syscall for the return of the callback function)

### `sceKernelUSec2SysClock()`

```c
int sceKernelUSec2SysClock(unsigned int usec, SceKernelSysClock *clock);
```

Convert a number of microseconds to a [SceKernelSysClock](#struct-scekernelsysclock) structure.

**Parameters:**

- `usec` – Number of microseconds
- `clock` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelUSec2SysClockWide()`

```c
SceInt64 sceKernelUSec2SysClockWide(unsigned int usec);
```

Convert a number of microseconds to a wide time.

**Parameters:**

- `usec` – Number of microseconds.

**Returns:** The time

### `sceKernelSysClock2USec()`

```c
int sceKernelSysClock2USec(SceKernelSysClock *clock, unsigned int *low, unsigned int *high);
```

Convert a [SceKernelSysClock](#struct-scekernelsysclock) structure to microseconds.

**Parameters:**

- `clock` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure
- `low` – Pointer to the low part of the time
- `high` – Pointer to the high part of the time

**Returns:** 0 on success, \< 0 on error

### `sceKernelSysClock2USecWide()`

```c
int sceKernelSysClock2USecWide(SceInt64 clock, unsigned *low, unsigned int *high);
```

Convert a wide time to microseconds.

**Parameters:**

- `clock` – Wide time
- `low` – Pointer to the low part of the time
- `high` – Pointer to the high part of the time

**Returns:** 0 on success, \< 0 on error

### `sceKernelGetSystemTime()`

```c
int sceKernelGetSystemTime(SceKernelSysClock *time);
```

Get the system time.

**Parameters:**

- `time` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelGetSystemTimeWide()`

```c
SceInt64 sceKernelGetSystemTimeWide(void);
```

Get the system time (wide version)

**Returns:** The system time

### `sceKernelGetSystemTimeLow()`

```c
unsigned int sceKernelGetSystemTimeLow(void);
```

Get the low 32bits of the current system time.

**Returns:** The low 32bits of the system time

### `sceKernelCreateVTimer()`

```c
SceUID sceKernelCreateVTimer(const char *name, SceKernelVTimerOptParam *opt);
```

Create a virtual timer.

**Parameters:**

- `name` – Name for the timer.
- `opt` – Pointer to an [SceKernelVTimerOptParam](#struct-scekernelvtimeroptparam) (pass NULL)

**Returns:** The VTimer's UID or \< 0 on error.

### `sceKernelDeleteVTimer()`

```c
int sceKernelDeleteVTimer(SceUID uid);
```

Delete a virtual timer.

**Parameters:**

- `uid` – The UID of the timer

**Returns:** \< 0 on error.

### `sceKernelGetVTimerBase()`

```c
int sceKernelGetVTimerBase(SceUID uid, SceKernelSysClock *base);
```

Get the timer base.

**Parameters:**

- `uid` – UID of the vtimer
- `base` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelGetVTimerBaseWide()`

```c
SceInt64 sceKernelGetVTimerBaseWide(SceUID uid);
```

Get the timer base (wide format)

**Parameters:**

- `uid` – UID of the vtimer

**Returns:** The 64bit timer base

### `sceKernelGetVTimerTime()`

```c
int sceKernelGetVTimerTime(SceUID uid, SceKernelSysClock *time);
```

Get the timer time.

**Parameters:**

- `uid` – UID of the vtimer
- `time` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelGetVTimerTimeWide()`

```c
SceInt64 sceKernelGetVTimerTimeWide(SceUID uid);
```

Get the timer time (wide format)

**Parameters:**

- `uid` – UID of the vtimer

**Returns:** The 64bit timer time

### `sceKernelSetVTimerTime()`

```c
int sceKernelSetVTimerTime(SceUID uid, SceKernelSysClock *time);
```

Set the timer time.

**Parameters:**

- `uid` – UID of the vtimer
- `time` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelSetVTimerTimeWide()`

```c
SceInt64 sceKernelSetVTimerTimeWide(SceUID uid, SceInt64 time);
```

Set the timer time (wide format)

**Parameters:**

- `uid` – UID of the vtimer
- `time` – Pointer to a [SceKernelSysClock](#struct-scekernelsysclock) structure

**Returns:** Possibly the last time

### `sceKernelStartVTimer()`

```c
int sceKernelStartVTimer(SceUID uid);
```

Start a virtual timer.

**Parameters:**

- `uid` – The UID of the timer

**Returns:** \< 0 on error

### `sceKernelStopVTimer()`

```c
int sceKernelStopVTimer(SceUID uid);
```

Stop a virtual timer.

**Parameters:**

- `uid` – The UID of the timer

**Returns:** \< 0 on error

### `sceKernelSetVTimerHandler()`

```c
int sceKernelSetVTimerHandler(SceUID uid, SceKernelSysClock *time, SceKernelVTimerHandler handler, void *common);
```

Set the timer handler.

**Parameters:**

- `uid` – UID of the vtimer
- `time` – Time to call the handler?
- `handler` – The timer handler
- `common` – Common pointer

**Returns:** 0 on success, \< 0 on error

### `sceKernelSetVTimerHandlerWide()`

```c
int sceKernelSetVTimerHandlerWide(SceUID uid, SceInt64 time, SceKernelVTimerHandlerWide handler, void *common);
```

Set the timer handler (wide mode)

**Parameters:**

- `uid` – UID of the vtimer
- `time` – Time to call the handler?
- `handler` – The timer handler
- `common` – Common pointer

**Returns:** 0 on success, \< 0 on error

### `sceKernelCancelVTimerHandler()`

```c
int sceKernelCancelVTimerHandler(SceUID uid);
```

Cancel the timer handler.

**Parameters:**

- `uid` – The UID of the vtimer

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferVTimerStatus()`

```c
int sceKernelReferVTimerStatus(SceUID uid, SceKernelVTimerInfo *info);
```

Get the status of a VTimer.

**Parameters:**

- `uid` – The uid of the VTimer
- `info` – Pointer to a [SceKernelVTimerInfo](#struct-scekernelvtimerinfo) structure

**Returns:** 0 on success, \< 0 on error

### `_sceKernelExitThread()`

```c
void _sceKernelExitThread(void);
```

Exit the thread (probably used as the syscall when the main thread returns.

### `sceKernelGetThreadmanIdType()`

```c
SceKernelIdListType sceKernelGetThreadmanIdType(SceUID uid);
```

Get the type of a threadman uid.

**Parameters:**

- `uid` – The uid to get the type from

**Returns:** The type, \< 0 on error

### `sceKernelRegisterThreadEventHandler()`

```c
SceUID sceKernelRegisterThreadEventHandler(const char *name, SceUID threadID, int mask, SceKernelThreadEventHandler handler, void *common);
```

Register a thread event handler.

**Parameters:**

- `name` – Name for the thread event handler
- `threadID` – Thread ID to monitor
- `mask` – Bit mask for what events to handle (only lowest 4 bits valid)
- `handler` – Pointer to a [SceKernelThreadEventHandler](#scekernelthreadeventhandler) function
- `common` – Common pointer

**Returns:** The UID of the create event handler, \< 0 on error

### `sceKernelReleaseThreadEventHandler()`

```c
int sceKernelReleaseThreadEventHandler(SceUID uid);
```

Release a thread event handler.

**Parameters:**

- `uid` – The UID of the event handler

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferThreadEventHandlerStatus()`

```c
int sceKernelReferThreadEventHandlerStatus(SceUID uid, SceKernelThreadEventHandlerInfo *info);
```

Refer the status of an thread event handler.

**Parameters:**

- `uid` – The UID of the event handler
- `info` – Pointer to a [SceKernelThreadEventHandlerInfo](#struct-scekernelthreadeventhandlerinfo) structure

**Returns:** 0 on success, \< 0 on error

### `sceKernelReferThreadProfiler()`

```c
PspDebugProfilerRegs * sceKernelReferThreadProfiler(void);
```

Get the thread profiler registers.

**Returns:** Pointer to the registers, NULL on error

### `sceKernelReferGlobalProfiler()`

```c
PspDebugProfilerRegs * sceKernelReferGlobalProfiler(void);
```

Get the globile profiler registers.

**Returns:** Pointer to the registers, NULL on error

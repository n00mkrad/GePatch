[PSPSDK documentation](../../README.md) › Files

# kernel/pspthreadman_kernel.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspthreadman.h>
```

Topics: [Thread Manager kernel functions](../../topics/ThreadmanKern.md)

## Data Structures

### `struct SceThreadContext`

Thread context Structues for the thread context taken from florinsasu's post on the forums.

```c
struct SceThreadContext {
    unsigned int type;
    unsigned int gpr[31];
    unsigned int fpr[32];
    unsigned int fc31;
    unsigned int hi;
    unsigned int lo;
    unsigned int SR;
    unsigned int EPC;
    unsigned int field_114;
    unsigned int field_118;
};
```

### `struct SceSCContext`

```c
struct SceSCContext {
    unsigned int status;
    unsigned int epc;
    unsigned int sp;
    unsigned int ra;
    unsigned int k1;
    unsigned int unk[3];
};
```

### `struct SceKernelThreadKInfo`

Structure to hold the status information for a thread (kernel form) 1.5 form.

| Field | Description |
|---|---|
| `SceSize size` | Size of the structure. |
| `char name[32]` | Nul terminated name of the thread. |
| `SceUInt attr` | Thread attributes. |
| `int status` | Thread status. |
| `SceKernelThreadEntry entry` | Thread entry point. |
| `void * stack` | Thread stack pointer. |
| `int stackSize` | Thread stack size. |
| `void * kstack` | Kernel stack pointer. |
| `void * kstackSize` | Kernel stack size. |
| `void * gpReg` | Pointer to the gp. |
| `SceSize args` | Size of args. |
| `void * argp` | Pointer to args. |
| `int initPriority` | Initial priority. |
| `int currentPriority` | Current priority. |
| `int waitType` | Wait type. |
| `SceUID waitId` | Wait id. |
| `int wakeupCount` | Wakeup count. |
| `SceKernelSysClock runClocks` | Number of clock cycles run. |
| `SceUInt intrPreemptCount` | Interrupt preemption count. |
| `SceUInt threadPreemptCount` | Thread preemption count. |
| `SceUInt releaseCount` | Release count. |
| `struct SceThreadContext * thContext` | Thread Context. |
| `float * vfpuContext` | VFPU Context. |
| `void * retAddr` | Return address from syscall. |
| `SceUInt unknown1` | Unknown, possibly size of SC context. |
| `struct SceSCContext * scContext` | Syscall Context. |

## Typedefs

### `SceKernelThreadKInfo`

```c
typedef struct SceKernelThreadKInfo SceKernelThreadKInfo;
```

Structure to hold the status information for a thread (kernel form) 1.5 form.

## Functions

### `sceKernelSuspendAllUserThreads()`

```c
int sceKernelSuspendAllUserThreads(void);
```

Suspend all user mode threads in the system.

**Returns:** 0 on success, \< 0 on error

### `sceKernelIsUserModeThread()`

```c
int sceKernelIsUserModeThread(void);
```

Checks if the current thread is a usermode thread.

**Returns:** 0 if kernel, 1 if user, \< 0 on error

### `sceKernelGetUserLevel()`

```c
int sceKernelGetUserLevel(void);
```

Get the user level of the current thread.

**Returns:** The user level, \< 0 on error

### `sceKernelGetSyscallRA()`

```c
unsigned int sceKernelGetSyscallRA(void);
```

Get the return address of the current thread's syscall.

**Returns:** The RA, 0 on error

### `sceKernelGetThreadKernelStackFreeSize()`

```c
int sceKernelGetThreadKernelStackFreeSize(SceUID thid);
```

Get the free stack space on the kernel thread.

**Parameters:**

- `thid` – The UID of the thread

**Returns:** The free stack space, \< 0 on error

### `sceKernelCheckThreadKernelStack()`

```c
int sceKernelCheckThreadKernelStack(void);
```

Check the thread kernel stack.

**Returns:** Unknown

### `sceKernelExtendKernelStack()`

```c
int sceKernelExtendKernelStack(int type, void(*cb)(void *), void *arg);
```

Extend the kernel thread stack.

**Parameters:**

- `type` – The type of block allocation. One of [PspSysMemBlockTypes](../user/pspsysmem.h.md#enum-pspsysmemblocktypes)
- `cb` – A pointer to a callback function
- `arg` – A pointer to a user specified argument

**Returns:** \< 0 on error

### `sceKernelGetSystemStatusFlag()`

```c
unsigned int sceKernelGetSystemStatusFlag(void);
```

Get the system status flag.

**Returns:** The system status flag

### `sceKernelAllocateKTLS()`

```c
int sceKernelAllocateKTLS(int id, int(*cb)(unsigned int *size, void *arg), void *arg);
```

Setup the KTLS allocator.

**Parameters:**

- `id` – The ID of the allocator
- `cb` – The allocator callback
- `arg` – User specified arg passed to the callback

**Returns:** \< 0 on error, allocation id on success

### `sceKernelFreeKTLS()`

```c
int sceKernelFreeKTLS(int id);
```

Free the KTLS allocator.

**Parameters:**

- `id` – The allocation id returned from AllocateKTLS

**Returns:** \< 0 on error

### `sceKernelGetKTLS()`

```c
void * sceKernelGetKTLS(int id);
```

Get the KTLS of the current thread.

**Parameters:**

- `id` – The allocation id returned from AllocateKTLS

**Returns:** The current KTLS, NULL on error

### `sceKernelGetThreadKTLS()`

```c
void * sceKernelGetThreadKTLS(int id, SceUID thid, int mode);
```

Get the KTLS of a thread.

**Parameters:**

- `id` – The allocation id returned from AllocateKTLS
- `thid` – The thread is, 0 for current thread
- `mode` – Perhaps? Sees to be set to 0 or 1

**Returns:** The current KTLS, NULL on error

### `sceKernelReferThreadDebugStatus()`

```c
int sceKernelReferThreadDebugStatus(SceUID uid, SceKernelThreadKInfo *info);
```

Refer kernel version of thread information.

**Parameters:**

- `uid` – UID to find
- `info` – Pointer to info structure, ensure size is set before calling

**Returns:** 0 on success

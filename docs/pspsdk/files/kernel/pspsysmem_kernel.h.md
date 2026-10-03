[PSPSDK documentation](../../README.md) › Files

# kernel/pspsysmem_kernel.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspsysmem.h>
```

Topics: [System Memory Manager Kernel](../../topics/SysMemKern.md)

## Data Structures

### `struct _PspSysmemPartitionInfo`

```c
struct _PspSysmemPartitionInfo {
    SceSize size;
    unsigned int startaddr;
    unsigned int memsize;
    unsigned int attr;
};
```

### `struct SceGameInfo`

```c
struct SceGameInfo {
    u32 size;
    u32 flags;
    char umd_data_string[16];
    char expect_umd_data[16];
    char qtgp2[8];
    char qtgp3[16];
    u32 allow_replace_umd;
    char title_id[16];
    u32 parental_level;
    char vsh_version[8];
    u32 umd_cache_on;
    u32 compiled_sdk_version;
    u32 compiler_version;
    u32 dnas;
    u32 utility_location;
    char vsh_bootfilename[64];
    char gamedata_id[16];
    char app_ver[8];
    char subscription_validity[8];
    int bootable;
    int opnssmp_ver;
};
```

### `struct _uidControlBlock`

Structure of a UID control block.

```c
struct _uidControlBlock {
    struct _uidControlBlock * parent;
    struct _uidControlBlock * nextChild;
    struct _uidControlBlock * type;
    u32 UID;
    char * name;
    unsigned char unk;
    unsigned char size;
    short attribute;
    struct _uidControlBlock * nextEntry;
};
```

### `struct SceSysmemPartInfo`

```c
struct SceSysmemPartInfo {
    u32 addr;
    u32 size;
};
```

### `struct SceSysmemPartTable`

```c
struct SceSysmemPartTable {
    u32 memSize;
    u32 unk4;
    u32 unk8;
    SceSysmemPartInfo other1;
    SceSysmemPartInfo other2;
    SceSysmemPartInfo vshell;
    SceSysmemPartInfo scUser;
    SceSysmemPartInfo meUser;
    SceSysmemPartInfo extSc2Kernel;
    SceSysmemPartInfo extScKernel;
    SceSysmemPartInfo extMeKernel;
    SceSysmemPartInfo extVshell;
};
```

### `struct PspPartitionData`

```c
struct PspPartitionData {
    u32 unk[5];
    u32 size;
};
```

### `struct PspSysMemPartition`

```c
struct PspSysMemPartition {
    struct PspSysMemPartition * next;
    u32 address;
    u32 size;
    u32 attributes;
    PspPartitionData * data;
};
```

## Typedefs

### `PspSysmemPartitionInfo`

```c
typedef struct _PspSysmemPartitionInfo PspSysmemPartitionInfo;
```

### `SceGameInfo`

```c
typedef struct SceGameInfo SceGameInfo;
```

### `SceUidControlBlock`

```c
typedef struct _uidControlBlock SceUidControlBlock;
```

### `uidControlBlock`

```c
typedef struct _uidControlBlock uidControlBlock;
```

### `PspPartitionData`

```c
typedef struct PspPartitionData PspPartitionData;
```

### `PspSysMemPartition`

```c
typedef struct PspSysMemPartition PspSysMemPartition;
```

## Functions

### `sceKernelQueryMemoryPartitionInfo()`

```c
int sceKernelQueryMemoryPartitionInfo(int pid, PspSysmemPartitionInfo *info);
```

Query the parition information.

**Parameters:**

- `pid` – The partition id
- `info` – Pointer to the [PspSysmemPartitionInfo](#pspsysmempartitioninfo) structure

**Returns:** 0 on success.

### `sceKernelPartitionTotalFreeMemSize()`

```c
SceSize sceKernelPartitionTotalFreeMemSize(int pid);
```

Get the total amount of free memory.

**Parameters:**

- `pid` – The partition id

**Returns:** The total amount of free memory, in bytes.

### `sceKernelPartitionMaxFreeMemSize()`

```c
SceSize sceKernelPartitionMaxFreeMemSize(int pid);
```

Get the size of the largest free memory block.

**Parameters:**

- `pid` – The partition id

**Returns:** The size of the largest free memory block, in bytes.

### `sceKernelSysMemDump()`

```c
void sceKernelSysMemDump(void);
```

Get the kernel to dump the internal memory table to Kprintf.

### `sceKernelSysMemDumpBlock()`

```c
void sceKernelSysMemDumpBlock(void);
```

Dump the list of memory blocks.

### `sceKernelSysMemDumpTail()`

```c
void sceKernelSysMemDumpTail(void);
```

Dump the tail blocks.

### `sceKernelSetDdrMemoryProtection()`

```c
int sceKernelSetDdrMemoryProtection(void *addr, int size, int prot);
```

Set the protection of a block of ddr memory.

**Parameters:**

- `addr` – Address to set protection on
- `size` – Size of block
- `prot` – Protection bitmask

**Returns:** \< 0 on error

### `sceKernelCreateHeap()`

```c
SceUID sceKernelCreateHeap(SceUID partitionid, SceSize size, int unk, const char *name);
```

Create a heap.

**Parameters:**

- `partitionid` – The UID of the partition where allocate the heap.
- `size` – The size in bytes of the heap.
- `unk` – Unknown, probably some flag or type, pass 1.
- `name` – Name assigned to the new heap.

**Returns:** The UID of the new heap, or if less than 0 an error.

### `sceKernelAllocHeapMemory()`

```c
void * sceKernelAllocHeapMemory(SceUID heapid, SceSize size);
```

Allocate a memory block from a heap.

**Parameters:**

- `heapid` – The UID of the heap to allocate from.
- `size` – The number of bytes to allocate.

**Returns:** The address of the allocated memory block, or NULL on error.

### `sceKernelFreeHeapMemory()`

```c
int sceKernelFreeHeapMemory(SceUID heapid, void *block);
```

Free a memory block allocated from a heap.

**Parameters:**

- `heapid` – The UID of the heap where block belongs.
- `block` – The block of memory to free from the heap.

**Returns:** 0 on success, \< 0 on error.

### `sceKernelDeleteHeap()`

```c
int sceKernelDeleteHeap(SceUID heapid);
```

Delete a heap.

**Parameters:**

- `heapid` – The UID of the heap to delete.

**Returns:** 0 on success, \< 0 on error.

### `sceKernelHeapTotalFreeSize()`

```c
SceSize sceKernelHeapTotalFreeSize(SceUID heapid);
```

Get the amount of free size of a heap, in bytes.

**Parameters:**

- `heapid` – The UID of the heap

**Returns:** the free size of the heap, in bytes. \< 0 on error.

### `sceKernelGetSceUidControlBlock()`

```c
int sceKernelGetSceUidControlBlock(SceUID uid, SceUidControlBlock **block);
```

Get a UID control block.

**Parameters:**

- `uid` – The UID to find
- `block` – Pointer to hold the pointer to the block

**Returns:** 0 on success

### `sceKernelGetSceUidControlBlockWithType()`

```c
int sceKernelGetSceUidControlBlockWithType(SceUID uid, SceUidControlBlock *type, SceUidControlBlock **block);
```

Get a UID control block on a particular type.

**Parameters:**

- `uid` – The UID to find
- `type` – Pointer to the type UID block
- `block` – Pointer to hold the pointer to the block

**Returns:** 0 on success

### `sceKernelGetUidmanCB()`

```c
SceUidControlBlock * sceKernelGetUidmanCB(void);
```

Get the root of the UID tree (1.5+ only)

**Returns:** Pointer to the UID tree root

### `sceKernelDeleteUID()`

```c
int sceKernelDeleteUID(SceUID uid);
```

Delete a UID.

**Parameters:**

- `uid` – The UID to delete

**Returns:** 0 on success

### `sceKernelGetModel()`

```c
int sceKernelGetModel(void);
```

Get the model of PSP.

**Returns:** \<= 0 original, 1 slim

### `sceKernelSetCompiledSdkVersion()`

```c
int sceKernelSetCompiledSdkVersion(int version);
```

Set the version of the SDK with which the caller was compiled.

Version numbers are as for [sceKernelDevkitVersion()](../user/pspsysmem.h.md#scekerneldevkitversion).

**Returns:** 0 on success, \< 0 on error.

### `sceKernelGetCompiledSdkVersion()`

```c
int sceKernelGetCompiledSdkVersion(void);
```

Get the SDK version set with [sceKernelSetCompiledSdkVersion()](#scekernelsetcompiledsdkversion).

**Returns:** Version number, or 0 if unset.

### `sceKernelGetGameInfo()`

```c
SceGameInfo * sceKernelGetGameInfo();
```

Gets the information of the game.

(2.00+ ?)

**Returns:** Pointer to the game information on success. NULL otherwise.

**Attention:** Needs to link to `pspsysmem_kernel` stub.

### `sceKernelGetSystemStatus()`

```c
int sceKernelGetSystemStatus(void);
```

Gets the current status of the system.

**Returns:** The status of the system.

**Attention:** Needs to link to `pspsysmem_kernel` stub.

### `sceKernelGetUIDcontrolBlock()`

```c
int sceKernelGetUIDcontrolBlock(SceUID uid, SceUidControlBlock **block);
```

Get a UID control block.

**Parameters:**

- `uid` – The UID to find
- `block` – Pointer to hold the pointer to the block

**Returns:** 0 on success

**Attention:** Needs to link to `pspsysmem_kernel` stub.

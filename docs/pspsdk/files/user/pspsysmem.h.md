[PSPSDK documentation](../../README.md) › Files

# user/pspsysmem.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
```

Topics: [System Memory Manager](../../topics/SysMem.md)

## Typedefs

### `SceKernelSysMemAlloc_t`

```c
typedef int SceKernelSysMemAlloc_t;
```

## Enumerations

### `enum PspSysMemBlockTypes`

Specifies the type of allocation used for memory blocks.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SMEM_Low` | `0` | Allocate from the lowest available address. |
| `PSP_SMEM_High` |  | Allocate from the highest available address. |
| `PSP_SMEM_Addr` |  | Allocate from the specified address. |

## Functions

### `sceKernelAllocPartitionMemory()`

```c
SceUID sceKernelAllocPartitionMemory(SceUID partitionid, const char *name, int type, SceSize size, void *addr);
```

Allocate a memory block from a memory partition.

**Parameters:**

- `partitionid` – The UID of the partition to allocate from.
- `name` – Name assigned to the new block.
- `type` – Specifies how the block is allocated within the partition. One of [PspSysMemBlockTypes](#enum-pspsysmemblocktypes).
- `size` – Size of the memory block, in bytes.
- `addr` – If type is PSP_SMEM_Addr, then addr specifies the lowest address allocate the block from.

**Returns:** The UID of the new block, or if less than 0 an error.

### `sceKernelFreePartitionMemory()`

```c
int sceKernelFreePartitionMemory(SceUID blockid);
```

Free a memory block allocated with [sceKernelAllocPartitionMemory](#scekernelallocpartitionmemory).

**Parameters:**

- `blockid` – UID of the block to free.

**Returns:** ? on success, less than 0 on error.

### `sceKernelGetBlockHeadAddr()`

```c
void * sceKernelGetBlockHeadAddr(SceUID blockid);
```

Get the address of a memory block.

**Parameters:**

- `blockid` – UID of the memory block.

**Returns:** The lowest address belonging to the memory block.

### `sceKernelTotalFreeMemSize()`

```c
SceSize sceKernelTotalFreeMemSize(void);
```

Get the total amount of free memory.

**Returns:** The total amount of free memory, in bytes.

### `sceKernelMaxFreeMemSize()`

```c
SceSize sceKernelMaxFreeMemSize(void);
```

Get the size of the largest free memory block.

**Returns:** The size of the largest free memory block, in bytes.

### `sceKernelDevkitVersion()`

```c
int sceKernelDevkitVersion(void);
```

Get the firmware version.

**Returns:** The firmware version. 0x01000300 on v1.00 unit, 0x01050001 on v1.50 unit, 0x01050100 on v1.51 unit, 0x01050200 on v1.52 unit, 0x02000010 on v2.00/v2.01 unit, 0x02050010 on v2.50 unit, 0x02060010 on v2.60 unit, 0x02070010 on v2.70 unit, 0x02070110 on v2.71 unit.

### `sceKernelSetCompiledSdkVersion()`

```c
int sceKernelSetCompiledSdkVersion(int version);
```

Set the version of the SDK with which the caller was compiled.

Version numbers are as for [sceKernelDevkitVersion()](#scekerneldevkitversion).

**Returns:** 0 on success, \< 0 on error.

### `sceKernelGetCompiledSdkVersion()`

```c
int sceKernelGetCompiledSdkVersion(void);
```

Get the SDK version set with [sceKernelSetCompiledSdkVersion()](#scekernelsetcompiledsdkversion).

**Returns:** Version number, or 0 if unset.

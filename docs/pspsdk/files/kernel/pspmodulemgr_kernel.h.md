[PSPSDK documentation](../../README.md) › Files

# kernel/pspmodulemgr_kernel.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspmodulemgr.h>
```

Topics: [Kernel Module Manager Library](../../topics/ModuleMgrKern.md)

## Data Structures

### `struct SceModuleMgrParam`

Structure used internally for many `sceModuleManager` module functions.

Also seems to be passed to `sceKernelStartThread` eventually by those internal functions.

| Field | Description |
|---|---|
| `u8 mode_start` | The Operation to start on.<br>One of the `SceModuleMgrExecModes` modes. |
| `u8 mode_finish` | The Operation to finish on.<br>One of the `SceModuleMgrExecModes` modes. |
| `u8 position` | The module placement policy in memory.<br>One of `PspSysMemBlockTypes`. |
| `u8 access` |  |
| `SceUID * result` |  |
| `SceUID * new_block_id` |  |
| `SceModule * mod` | The module in memory. |
| `SceLoadCoreExecFileInfo * exec_info` | The executable information of the module. |
| `u32 api_type` | The API type of the module. |
| `SceUID fd` | The file ID for module file. |
| `s32 thread_priority` | The module thread priority. |
| `u32 thread_attr` | The module thread attributes. |
| `SceUID mpid_text` | The memory partition where the program of the module will be stored. |
| `SceUID mpid_data` | The memory partition where the data of the module will be stored. |
| `SceUID thread_mpid_stack` |  |
| `SceSize stack_size` |  |
| `SceUID mod_id` | The module ID. |
| `SceUID caller_mod_id` |  |
| `SceSize mod_size` |  |
| `void * file_base` |  |
| `SceSize arg_size` |  |
| `void * argp` |  |
| `u32 unk1` |  |
| `u32 unk2` |  |
| `s32 * status` |  |
| `SceUID event_id` |  |
| `u32 unk3` |  |
| `u32 unk4` |  |
| `u32 unk5` |  |
| `SceUID extern_mem_block_id_kernel` |  |
| `SceUID extern_mem_block_partition_id` |  |
| `SceSize extern_mem_block_size` |  |
| `u32 unk6` |  |
| `void * block_gzip` |  |
| `u32 unk7` |  |
| `char secure_install_id[SCE_SECURE_INSTALL_ID_LEN]` |  |
| `SceUID extern_mem_block_id_user` |  |
| `u32 unk8` |  |
| `SceOff mem_block_offset` |  |

## Enumerations

### `enum SceModuleMgrExecModes`

| Enumerator | Description |
|---|---|
| `MODULE_EXEC_CMD_LOAD` |  |
| `MODULE_EXEC_CMD_RELOCATE` |  |
| `MODULE_EXEC_CMD_START` |  |
| `MODULE_EXEC_CMD_STOP` |  |
| `MODULE_EXEC_CMD_UNLOAD` |  |

## Functions

### `sceKernelLoadModuleBuffer()`

```c
SceUID sceKernelLoadModuleBuffer(void *buf, SceSize bufsize, int flags, SceKernelLMOption *option);
```

Load a module from a buffer.

**Parameters:**

- `buf` – Pointer to a buffer containing the module to load. The buffer must reside at an address that is a multiple to 64 bytes.
- `bufsize` – Size (in bytes) of the buffer pointed to by buf.
- `flags` – Unused, always 0.
- `option` – Pointer to an optional [SceKernelLMOption](../user/pspmodulemgr.h.md#struct-scekernellmoption) structure.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

### `sceKernelLoadModuleWithApitype2()`

```c
SceUID sceKernelLoadModuleWithApitype2(int apitype, const char *path, int flags, SceKernelLMOption *option);
```

Alias for `sceKernelLoadModuleForLoadExecForUser`

**Attention:** Needs to link to `pspmodulemgr_kernel` stub.

### `sceKernelLoadModuleBufferBootInitBtcnf()`

```c
SceUID sceKernelLoadModuleBufferBootInitBtcnf(int bufsize, void *buf, int flags, SceKernelLMOption *option);
```

Load a module from a buffer with the Boot Init BTCNF apitype (0x051).

**Parameters:**

- `bufsize` – Size (in bytes) of the buffer pointed to by buf.
- `buf` – Pointer to a buffer containing the module to load. The buffer must reside at an address that is a multiple to 64 bytes.
- `flags` – Unused, always 0.
- `option` – Pointer to an optional [SceKernelLMOption](../user/pspmodulemgr.h.md#struct-scekernellmoption) structure.

**Returns:** The UID of the loaded module on success, otherwise one of [PspKernelErrorCodes](../user/pspkerror.h.md#enum-pspkernelerrorcodes).

**Attention:** Needs to link to `pspmodulemgr_kernel` stub.

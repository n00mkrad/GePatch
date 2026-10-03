[PSPSDK documentation](../../README.md) › Files

# kernel/psploadcore.h

```c
#include <pspkerneltypes.h>
#include <pspmoduleinfo.h>
```

Topics: [Interface to the LoadCoreForKernel library.](../../topics/LoadCore.md)

## Data Structures

### `struct SceModule`

Describes a loaded module in memory.

This structure could change in future firmware revisions.

| Field | Description |
|---|---|
| `struct SceModule * next` | Pointer to the next registered module.<br>Modules are connected via a linked list. |
| `u16 attribute` | The attributes of a module.<br>One or more of [SceModuleAttribute](#enum-scemoduleattribute) and [SceModulePrivilegeLevel](#enum-scemoduleprivilegelevel). |
| `u8 version[2]` | The version of the module.<br>Consists of a major and minor part. There can be several modules loaded with the same name and version. |
| `char modname[27]` | The module's name.<br>There can be several modules loaded with the same name. |
| `char terminal` | String terminator (always '\\0'). |
| `u16 mod_state` | The status of the module.<br>Contains information whether the module has been started, stopped, is a user module, etc. |
| `char padding[2]` |  |
| `SceUID sec_id` | A secondary ID for the module. |
| `SceUID modid` | The module's UID. |
| `SceUID user_mod_thid` | The thread ID of a user module. |
| `SceUID mem_id` | The ID of the memory block belonging to the module. |
| `u32 mpid_text` | The ID of the TEXT segment's memory partition. |
| `u32 mpid_data` | The ID of the DATA segment's memory partition. |
| `void * ent_top` | Pointer to the first resident library entry table of the module. |
| `SceSize ent_size` | The size of all resident library entry tables of the module. |
| `void * stub_top` | Pointer to the first stub library entry table of the module. |
| `SceSize stub_size` | The size of all stub library entry tables of the module. |
| `SceKernelThreadEntry module_start` | A pointer to the (required) module's start entry function.<br>This function is executed during the module's startup. |
| `SceKernelThreadEntry module_stop` | A pointer to the (required) module's stop entry function.<br>This function is executed during the module's stopping phase. |
| `SceKernelThreadEntry module_bootstart` | A pointer to a module's Bootstart entry function.<br>This function is probably executed after a reboot. |
| `SceKernelRebootBeforeForKernel module_reboot_before` | A pointer to a module's rebootBefore entry function.<br>This function is probably executed before a reboot. |
| `SceKernelRebootPhaseForKernel module_reboot_phase` | A pointer to a module's rebootPhase entry function.<br>This function is probably executed during a reboot. |
| `u32 entry_addr` | The entry address of the module.<br>It is the offset from the start of the TEXT segment to the program's entry point. |
| `u32 gp_value` | Contains the offset from the start of the TEXT segment of the program's GP register value. |
| `u32 text_addr` | The start address of the TEXT segment. |
| `u32 text_size` | The size of the TEXT segment. |
| `u32 data_size` | The size of the DATA segment. |
| `u32 bss_size` | The size of the BSS segment. |
| `u8 nsegment` | The number of segments the module consists of. |
| `u8 padding2[3]` | Reserved. |
| `u32 segmentaddr[4]` | An array containing the start address of each segment. |
| `SceSize segmentsize[4]` | An array containing the size of each segment. |
| `u32 segmentalign[4]` | An array containing the alignment information of each segment. |
| `s32 module_start_thread_priority` | The priority of the module start thread. |
| `SceSize module_start_thread_stacksize` | The stack size of the module start thread. |
| `SceUInt module_start_thread_attr` | The attributes of the module start thread. |
| `s32 module_stop_thread_priority` | The priority of the module stop thread. |
| `SceSize module_stop_thread_stacksize` | The stack size of the module stop thread. |
| `SceUInt module_stop_thread_attr` | The attributes of the module stop thread. |
| `s32 module_reboot_before_thread_priority` | The priority of the module reboot before thread. |
| `SceSize module_reboot_before_thread_stacksize` | The stack size of the module reboot before thread. |
| `SceUInt module_reboot_before_thread_attr` | The attributes of the module reboot before thread. |
| `u32 count_reg_val` | The value of the coprocessor 0's count register when the module is created. |
| `u32 segment_checksum` | The segment checksum of the module's segments. |
| `u32 text_segment_checksum` | TEXT segment checksum of the module. |
| `u32 compute_text_segment_checksum` | Whether to compute the text segment checksum before starting the module (see prologue).<br>If non-zero, the text segment checksum will be computed after the module's resident libraries have been registered, and its stub libraries have been linked. |

### `struct SceLoadCoreBootModuleInfo`

```c
struct SceLoadCoreBootModuleInfo {
    char * name;
    void * buf;
    int size;
    int unk_12;
    int attr;
    int unk_20;
    int argSize;
    int argPartId;
};
```

### `struct SceLibraryEntryTable`

Defines a library and its exported functions and variables.

Use the len member to determine the real size of the table (size = len \* 4).

| Field | Description |
|---|---|
| `const char * libname` | The library's name. |
| `unsigned char version[2]` | Library version. |
| `unsigned short attribute` | Library attributes. |
| `unsigned char len` | Length of this entry table in 32-bit WORDs. |
| `unsigned char vstubcount` | The number of variables exported by the library. |
| `unsigned short stubcount` | The number of functions exported by the library. |
| `void * entrytable` | Pointer to the entry table; an array of NIDs followed by pointers to functions and variables. |

### `struct SceLibraryStubTable`

Specifies a library and a set of imports from that library.

Use the len member to determine the real size of the table (size = len \* 4).

| Field | Description |
|---|---|
| `const char * libname` |  |
| `unsigned char version[2]` | Minimum required version of the library we want to import. |
| `unsigned short attribute` |  |
| `unsigned char len` | Length of this stub table in 32-bit WORDs. |
| `unsigned char vstubcount` | The number of variables imported from the library. |
| `unsigned short stubcount` | The number of functions imported from the library. |
| `unsigned int * nidtable` | Pointer to an array of NIDs. |
| `void * stubtable` | Pointer to the imported function stubs. |
| `void * vstubtable` | Pointer to the imported variable stubs. |

### `struct SceLoadCoreExecFileInfo`

| Field | Description |
|---|---|
| `u32 unk0` | Unknown. |
| `u32 mode_attr` | The mode attribute of the executable file.<br>One of ::SceExecFileModeAttr. |
| `u32 api_type` | The API type. |
| `u32 unk12` | Unknown. |
| `SceSize exec_size` | The size of the executable, including the ~PSP header. |
| `SceSize max_alloc_size` | The maximum size needed for the decompression. |
| `SceUID decompression_mem_id` | The memory ID of the decompression buffer. |
| `void * file_base` | Pointer to the compressed module data. |
| `u32 elf_type` | Indicates the ELF type of the executable.<br>One of ::SceExecFileElfType. |
| `void * top_addr` | The start address of the TEXT segment of the executable in memory. |
| `u32 entry_addr` | The entry address of the module.<br>It is the offset from the start of the TEXT segment to the program's entry point. |
| `u32 unk44` | Unknown. |
| `SceSize largest_seg_size` | The size of the largest module segment.<br>Should normally be "textSize", but technically can be any other segment. |
| `SceSize text_size` | The size of the TEXT segment. |
| `SceSize data_size` | The size of the DATA segment. |
| `SceSize bss_size` | The size of the BSS segment. |
| `u32 partition_id` | The memory partition of the executable. |
| `u32 is_kernel_mod` | Indicates whether the executable is a kernel module or not.<br>Set to 1 for kernel module, 0 for user module. |
| `u32 is_decrypted` | Indicates whether the executable is decrypted or not.<br>Set to 1 if it is successfully decrypted, 0 for encrypted. |
| `u32 module_info_offset` | The offset from the start address of the TEXT segment to the SceModuleInfo section. |
| `SceModuleInfo * module_info` | The pointer to the module's SceModuleInfo section. |
| `u32 is_compressed` | Indicates whether the module is compressed or not.<br>Set to 1 if it is compressed, otherwise 0. |
| `u16 mod_info_attribute` | The module's attributes.<br>One or more of [SceModuleAttribute](#enum-scemoduleattribute) and [SceModulePrivilegeLevel](#enum-scemoduleprivilegelevel). |
| `u16 exec_attribute` | The attributes of the executable file.<br>One of ::SceExecFileAttr. |
| `SceSize dec_size` | The size of the decompressed module, including its headers. |
| `u32 is_decompressed` | Indicates whether the module is decompressed or not.<br>Set to 1 for decompressed, otherwise 0. |
| `u32 is_sign_checked` | Indicates whether the module was signChecked or not.<br>Set to 1 for signChecked, otherwise 0. A signed module has a "mangled" executable header, in other words, the "~PSP" signature can't be seen. |
| `u32 unk104` | Unknown. |
| `SceSize overlap_size` | The size of the GZIP compression overlap. |
| `void * exports_info` | Pointer to the first resident library entry table of the module. |
| `SceSize exports_size` | The size of all resident library entry tables of the module. |
| `void * imports_info` | Pointer to the first stub library entry table of the module. |
| `SceSize imports_size` | The size of all stub library entry tables of the module. |
| `void * strtab_offset` | Pointer to the string table section. |
| `u8 num_segments` | The number of segments in the executable. |
| `u8 padding[3]` | Reserved. |
| `u32 segment_addr[(4)]` | An array containing the start address of each segment. |
| `u32 segment_size[(4)]` | An array containing the size of each segment. |
| `SceUID mem_block_id` | The ID of the ELF memory block containing the TEXT, DATA and BSS segment. |
| `u32 segment_align[(4)]` | An array containing the alignment information of each segment. |
| `u32 max_seg_align` | The largest value of the segment_align array. |

## Macros

### `SCE_KERNEL_MAX_MODULE_SEGMENT`

```c
#define SCE_KERNEL_MAX_MODULE_SEGMENT (4)
```

## Typedefs

### `SceKernelRebootBeforeForKernel`

```c
typedef s32(* SceKernelRebootBeforeForKernel) (void *arg1, s32 arg2, s32 arg3, s32 arg4))(void *arg1, s32 arg2, s32 arg3, s32 arg4);
```

Reboot preparation functions.

### `SceKernelRebootPhaseForKernel`

```c
typedef s32(* SceKernelRebootPhaseForKernel) (s32 arg1, void *arg2, s32 arg3, s32 arg4))(s32 arg1, void *arg2, s32 arg3, s32 arg4);
```

### `SceModule`

```c
typedef struct SceModule SceModule;
```

Describes a loaded module in memory.

This structure could change in future firmware revisions.

### `SceLibraryEntryTable`

```c
typedef struct SceLibraryEntryTable SceLibraryEntryTable;
```

Defines a library and its exported functions and variables.

Use the len member to determine the real size of the table (size = len \* 4).

### `SceLibraryStubTable`

```c
typedef struct SceLibraryStubTable SceLibraryStubTable;
```

Specifies a library and a set of imports from that library.

Use the len member to determine the real size of the table (size = len \* 4).

### `SceLoadCoreExecFileInfo`

```c
typedef struct SceLoadCoreExecFileInfo SceLoadCoreExecFileInfo;
```

## Enumerations

### `enum SceModuleAttribute`

Module type attributes.

| Enumerator | Value | Description |
|---|---|---|
| `SCE_MODULE_ATTR_NONE` | `0x0000` | No module attributes. |
| `SCE_MODULE_ATTR_CANT_STOP` | `0x0001` | Resident module - stays in memory.<br>You cannot unload such a module. |
| `SCE_MODULE_ATTR_EXCLUSIVE_LOAD` | `0x0002` | Only one instance of the module (one version) can be loaded into the system.<br>If you want to load another version of that module, you have to delete the loaded version first. |
| `SCE_MODULE_ATTR_EXCLUSIVE_START` | `0x0004` | Only one instance of the module (one version) can be started.<br>If you want to start another version of that module, you have to stop the currently running version first. |

### `enum SceModulePrivilegeLevel`

Module Privilege Levels - These levels define the permissions a module can have.

| Enumerator | Value | Description |
|---|---|---|
| `SCE_MODULE_USER` | `0x0000` | Lowest permission. |
| `SCE_MODULE_MS` | `0x0200` | POPS/Demo. |
| `SCE_MODULE_USB_WLAN` | `0x0400` | Module Gamesharing. |
| `SCE_MODULE_APP` | `0x0600` | Application module. |
| `SCE_MODULE_VSH` | `0x0800` | VSH module. |
| `SCE_MODULE_KERNEL` | `0x1000` | Highest permission. |
| `SCE_MODULE_KIRK_MEMLMD_LIB` | `0x2000` | The module uses KIRK's memlmd resident library. |
| `SCE_MODULE_KIRK_SEMAPHORE_LIB` | `0x4000` | The module uses KIRK's semaphore resident library. |

## Functions

### `sceKernelGetModuleList()`

```c
int sceKernelGetModuleList(int readbufsize, SceUID *readbuf);
```

Gets the current module list.

**Parameters:**

- `readbufsize` – The size of the read buffer.
- `readbuf` – Pointer to a buffer to store the IDs

**Returns:** \< 0 on error.

### `sceKernelModuleCount()`

```c
int sceKernelModuleCount(void);
```

Get the number of loaded modules.

Return the count of loaded modules.

**Returns:**

- The number of loaded modules.
- The count of loaded modules.

### `sceKernelFindModuleByName()`

```c
SceModule * sceKernelFindModuleByName(const char *modname);
```

Find a module by it's name.

**Parameters:**

- `modname` – The name of the module.

**Returns:** Pointer to the [SceModule](#struct-scemodule) structure if found, otherwise NULL.

### `sceKernelFindModuleByAddress()`

```c
SceModule * sceKernelFindModuleByAddress(unsigned int addr);
```

Find a module from an address.

**Parameters:**

- `addr` – Address somewhere within the module.

**Returns:** Pointer to the [SceModule](#struct-scemodule) structure if found, otherwise NULL.

### `sceKernelFindModuleByUID()`

```c
SceModule * sceKernelFindModuleByUID(SceUID modid);
```

Find a module by it's UID.

**Parameters:**

- `modid` – The UID of the module.

**Returns:** Pointer to the [SceModule](#struct-scemodule) structure if found, otherwise NULL.

### `sceKernelIcacheClearAll()`

```c
void sceKernelIcacheClearAll(void);
```

Invalidate the CPU's instruction cache.

### `sceKernelCheckExecFile()`

```c
int sceKernelCheckExecFile(void *buf, SceLoadCoreExecFileInfo *execInfo);
```

Check an executable file.

This contains scanning its ELF header and ~PSP header (if it has one) and filling the execInfo structure with basic information, like the ELF type, segment information, the size of the executable. The file is also uncompressed, if it was compressed before.

**Parameters:**

- `buf` – Pointer to the file's contents.
- `execInfo` – Pointer to the executionInfo belonging to that executable.

**Returns:** 0 on success.

### `sceKernelProbeExecutableObject()`

```c
int sceKernelProbeExecutableObject(void *buf, SceLoadCoreExecFileInfo *execInfo);
```

Probe an executable file.

This contains calculating the sizes for the three segments TEXT, DATA and BSS, filling the execInfo structure with information about the location and sizes of the resident/stub library entry tables.

Furthermore, it is checked whether the executable has valid API type or not.

**Parameters:**

- `buf` – Pointer to the file's contents.
- `execInfo` – Pointer to the executionInfo belonging to that executable.

**Returns:** 0 on success.

### `sceKernelGetModuleIdListForKernel()`

```c
int sceKernelGetModuleIdListForKernel(SceUID *mod_id_list, u32 size, u32 *mod_count, u32 user_mods_only);
```

Receive a list of UIDs of loaded modules.

**Parameters:**

- `mod_id_list` – Pointer to a SceUID array which will receive the UIDs of the loaded modules.
- `size` – Size of mod_id_list. Specifies the number of entries that can be stored into mod_id_list.
- `mod_count` – A pointer which will receive the total number of loaded modules.
- `user_mods_only` – Set to 1 to only receive UIDs from user mode modules. Set to 0 to receive UIDs from all loaded modules.

**Returns:** 0 on success.

### `sceKernelCheckPspConfig()`

```c
int sceKernelCheckPspConfig(void *buf, int size, int flag);
```

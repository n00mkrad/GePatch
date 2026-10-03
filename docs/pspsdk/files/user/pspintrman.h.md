[PSPSDK documentation](../../README.md) › Files

# user/pspintrman.h

```c
#include <pspkerneltypes.h>
```

Topics: [Interrupt Manager](../../topics/IntrMan.md)

## Data Structures

### `struct tag_IntrHandlerOptionParam`

```c
struct tag_IntrHandlerOptionParam {
    int size;
    u32 entry;
    u32 common;
    u32 gp;
    u16 intr_code;
    u16 sub_count;
    u16 intr_level;
    u16 enabled;
    u32 calls;
    u32 field_1C;
    u32 total_clock_lo;
    u32 total_clock_hi;
    u32 min_clock_lo;
    u32 min_clock_hi;
    u32 max_clock_lo;
    u32 max_clock_hi;
};
```

## Typedefs

### `PspIntrHandlerOptionParam`

```c
typedef struct tag_IntrHandlerOptionParam PspIntrHandlerOptionParam;
```

## Enumerations

### `enum PspInterrupts`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_GPIO_INT` | `4` |  |
| `PSP_ATA_INT` | `5` |  |
| `PSP_UMD_INT` | `6` |  |
| `PSP_MSCM0_INT` | `7` |  |
| `PSP_WLAN_INT` | `8` |  |
| `PSP_AUDIO_INT` | `10` |  |
| `PSP_I2C_INT` | `12` |  |
| `PSP_SIRCS_INT` | `14` |  |
| `PSP_SYSTIMER0_INT` | `15` |  |
| `PSP_SYSTIMER1_INT` | `16` |  |
| `PSP_SYSTIMER2_INT` | `17` |  |
| `PSP_SYSTIMER3_INT` | `18` |  |
| `PSP_THREAD0_INT` | `19` |  |
| `PSP_NAND_INT` | `20` |  |
| `PSP_DMACPLUS_INT` | `21` |  |
| `PSP_DMA0_INT` | `22` |  |
| `PSP_DMA1_INT` | `23` |  |
| `PSP_MEMLMD_INT` | `24` |  |
| `PSP_GE_INT` | `25` |  |
| `PSP_VBLANK_INT` | `30` |  |
| `PSP_MECODEC_INT` | `31` |  |
| `PSP_HPREMOTE_INT` | `36` |  |
| `PSP_MSCM1_INT` | `60` |  |
| `PSP_MSCM2_INT` | `61` |  |
| `PSP_THREAD1_INT` | `65` |  |
| `PSP_INTERRUPT_INT` | `66` |  |

### `enum PspSubInterrupts`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_GPIO_SUBINT` | `PSP_GPIO_INT` |  |
| `PSP_ATA_SUBINT` | `PSP_ATA_INT` |  |
| `PSP_UMD_SUBINT` | `PSP_UMD_INT` |  |
| `PSP_DMACPLUS_SUBINT` | `PSP_DMACPLUS_INT` |  |
| `PSP_GE_SUBINT` | `PSP_GE_INT` |  |
| `PSP_DISPLAY_SUBINT` | `PSP_VBLANK_INT` |  |

## Functions

### `sceKernelCpuSuspendIntr()`

```c
unsigned int sceKernelCpuSuspendIntr(void);
```

Suspend all interrupts.

**Returns:** The current state of the interrupt controller, to be used with [sceKernelCpuResumeIntr()](#scekernelcpuresumeintr).

### `sceKernelCpuResumeIntr()`

```c
void sceKernelCpuResumeIntr(unsigned int flags);
```

Resume all interrupts.

**Parameters:**

- `flags` – The value returned from [sceKernelCpuSuspendIntr()](#scekernelcpususpendintr).

### `sceKernelCpuResumeIntrWithSync()`

```c
void sceKernelCpuResumeIntrWithSync(unsigned int flags);
```

Resume all interrupts (using sync instructions).

**Parameters:**

- `flags` – The value returned from [sceKernelCpuSuspendIntr()](#scekernelcpususpendintr)

### `sceKernelIsCpuIntrSuspended()`

```c
int sceKernelIsCpuIntrSuspended(unsigned int flags);
```

Determine if interrupts are suspended or active, based on the given flags.

**Parameters:**

- `flags` – The value returned from [sceKernelCpuSuspendIntr()](#scekernelcpususpendintr).

**Returns:** 1 if flags indicate that interrupts were not suspended, 0 otherwise.

### `sceKernelIsCpuIntrEnable()`

```c
int sceKernelIsCpuIntrEnable(void);
```

Determine if interrupts are enabled or disabled.

**Returns:** 1 if interrupts are currently enabled.

### `sceKernelRegisterSubIntrHandler()`

```c
int sceKernelRegisterSubIntrHandler(int intno, int no, void *handler, void *arg);
```

Register a sub interrupt handler.

**Parameters:**

- `intno` – The interrupt number to register.
- `no` – The sub interrupt handler number (user controlled)
- `handler` – The interrupt handler
- `arg` – An argument passed to the interrupt handler

**Returns:** \< 0 on error.

### `sceKernelReleaseSubIntrHandler()`

```c
int sceKernelReleaseSubIntrHandler(int intno, int no);
```

Release a sub interrupt handler.

**Parameters:**

- `intno` – The interrupt number to register.
- `no` – The sub interrupt handler number

**Returns:** \< 0 on error.

### `sceKernelEnableSubIntr()`

```c
int sceKernelEnableSubIntr(int intno, int no);
```

Enable a sub interrupt.

**Parameters:**

- `intno` – The sub interrupt to enable.
- `no` – The sub interrupt handler number

**Returns:** \< 0 on error.

### `sceKernelDisableSubIntr()`

```c
int sceKernelDisableSubIntr(int intno, int no);
```

Disable a sub interrupt handler.

**Parameters:**

- `intno` – The sub interrupt to disable.
- `no` – The sub interrupt handler number

**Returns:** \< 0 on error.

### `QueryIntrHandlerInfo()`

```c
int QueryIntrHandlerInfo(SceUID intr_code, SceUID sub_intr_code, PspIntrHandlerOptionParam *data);
```

## Variables

### `PspInterruptNames`

```c
const char* PspInterruptNames[67][67];
```

[PSPSDK documentation](../../README.md) › Files

# kermit/pspkermit.h

```c
#include <pspsdk.h>
```

## Data Structures

### `struct SceKermitRequest`

```c
struct SceKermitRequest {
    uint32_t cmd;
    SceUID sema_id;
    uint64_t * response;
    uint32_t padding;
    uint64_t args[14];
};
```

### `struct SceKermitCommand`

```c
struct SceKermitCommand {
    uint32_t cmd;
    SceKermitRequest * request;
};
```

### `struct SceKermitResponse`

```c
struct SceKermitResponse {
    uint64_t result;
    SceUID sema_id;
    int32_t unk_C;
    uint64_t * response;
    uint64_t unk_1C;
};
```

### `struct SceKermitInterrupt`

```c
struct SceKermitInterrupt {
    int32_t unk_0;
    int32_t unk_4;
};
```

### `struct KermitPacket_`

```c
struct KermitPacket_ {
    u32 cmd;
    SceUID sema;
    struct KermitPacket_ * self;
    u32 unk_C;
};
```

## Macros

### `KERMIT_MAX_ARGC`

```c
#define KERMIT_MAX_ARGC (14)
```

### `KERMIT_CMD_RTC_GET_CURRENT_TICK`

```c
#define KERMIT_CMD_RTC_GET_CURRENT_TICK (0x0)
```

### `KERMIT_CMD_ID_STORAGE_LOOKUP`

```c
#define KERMIT_CMD_ID_STORAGE_LOOKUP (0x1)
```

### `KERMIT_CMD_POWER_FREQUENCY`

```c
#define KERMIT_CMD_POWER_FREQUENCY (0x2)
```

### `KERMIT_CMD_AUDIO_ROUTING`

```c
#define KERMIT_CMD_AUDIO_ROUTING (0x3)
```

### `KERMIT_CMD_GET_CAMERA_DIRECTION`

```c
#define KERMIT_CMD_GET_CAMERA_DIRECTION (0x5)
```

### `KERMIT_CMD_GET_IDPSC_ENABLE`

```c
#define KERMIT_CMD_GET_IDPSC_ENABLE (0x6)
```

### `KERMIT_CMD_DISABLE_MULTITASKING`

```c
#define KERMIT_CMD_DISABLE_MULTITASKING (0x7)
```

### `KERMIT_CMD_ERROR_EXIT`

```c
#define KERMIT_CMD_ERROR_EXIT (0x8)
```

### `KERMIT_CMD_ERROR_EXIT_2`

```c
#define KERMIT_CMD_ERROR_EXIT_2 (0x422)
```

### `KERMIT_CMD_ENABLE_MULTITASKING`

```c
#define KERMIT_CMD_ENABLE_MULTITASKING (0x9)
```

### `KERMIT_CMD_RESUME_DEVICE`

```c
#define KERMIT_CMD_RESUME_DEVICE (0xA)
```

### `KERMIT_CMD_REQUEST_SUSPEND`

```c
#define KERMIT_CMD_REQUEST_SUSPEND (0xB)
```

### `KERMIT_CMD_IS_FIRST_BOOT`

```c
#define KERMIT_CMD_IS_FIRST_BOOT (0xC)
```

### `KERMIT_CMD_GET_PREFIX_SSID`

```c
#define KERMIT_CMD_GET_PREFIX_SSID (0xD)
```

### `KERMIT_CMD_SET_PS_BUTTON_STATE`

```c
#define KERMIT_CMD_SET_PS_BUTTON_STATE (0x10)
```

### `KERMIT_CMD_INIT_MS`

```c
#define KERMIT_CMD_INIT_MS (0x0)
```

### `KERMIT_CMD_EXIT_MS`

```c
#define KERMIT_CMD_EXIT_MS (0x1)
```

### `KERMIT_CMD_OPEN_MS`

```c
#define KERMIT_CMD_OPEN_MS (0x2)
```

### `KERMIT_CMD_CLOSE_MS`

```c
#define KERMIT_CMD_CLOSE_MS (0x3)
```

### `KERMIT_CMD_READ_MS`

```c
#define KERMIT_CMD_READ_MS (0x4)
```

### `KERMIT_CMD_WRITE_MS`

```c
#define KERMIT_CMD_WRITE_MS (0x5)
```

### `KERMIT_CMD_SEEK_MS`

```c
#define KERMIT_CMD_SEEK_MS (0x6)
```

### `KERMIT_CMD_IOCTL_MS`

```c
#define KERMIT_CMD_IOCTL_MS (0x7)
```

### `KERMIT_CMD_REMOVE_MS`

```c
#define KERMIT_CMD_REMOVE_MS (0x8)
```

### `KERMIT_CMD_MKDIR_MS`

```c
#define KERMIT_CMD_MKDIR_MS (0x9)
```

### `KERMIT_CMD_RMDIR_MS`

```c
#define KERMIT_CMD_RMDIR_MS (0xA)
```

### `KERMIT_CMD_DOPEN_MS`

```c
#define KERMIT_CMD_DOPEN_MS (0xB)
```

### `KERMIT_CMD_DCLOSE_MS`

```c
#define KERMIT_CMD_DCLOSE_MS (0xC)
```

### `KERMIT_CMD_DREAD_MS`

```c
#define KERMIT_CMD_DREAD_MS (0xD)
```

### `KERMIT_CMD_GETSTAT_MS`

```c
#define KERMIT_CMD_GETSTAT_MS (0xE)
```

### `KERMIT_CMD_CHSTAT_MS`

```c
#define KERMIT_CMD_CHSTAT_MS (0xF)
```

### `KERMIT_CMD_RENAME_MS`

```c
#define KERMIT_CMD_RENAME_MS (0x10)
```

### `KERMIT_CMD_CHDIR_MS`

```c
#define KERMIT_CMD_CHDIR_MS (0x11)
```

### `KERMIT_CMD_DEVCTL`

```c
#define KERMIT_CMD_DEVCTL (0x14)
```

### `KERMIT_CMD_INIT_AUDIO_IN`

```c
#define KERMIT_CMD_INIT_AUDIO_IN 0x0
```

### `KERMIT_CMD_OUTPUT_1`

```c
#define KERMIT_CMD_OUTPUT_1 0x1
```

### `KERMIT_CMD_OUTPUT_2`

```c
#define KERMIT_CMD_OUTPUT_2 0x2
```

### `KERMIT_CMD_SUSPEND_AUDIO`

```c
#define KERMIT_CMD_SUSPEND_AUDIO 0x3
```

### `KERMIT_CMD_RESUME`

```c
#define KERMIT_CMD_RESUME 0x4
```

### `KERMIT_CMD_UNK0`

```c
#define KERMIT_CMD_UNK0 0x0
```

### `KERMIT_CMD_SETAVC_TIMESTAMPINTERNAL`

```c
#define KERMIT_CMD_SETAVC_TIMESTAMPINTERNAL 0x1
```

### `KERMIT_CMD_BOOT_START`

```c
#define KERMIT_CMD_BOOT_START 0x2
```

### `KERMIT_CMD_UNK9`

```c
#define KERMIT_CMD_UNK9 0x9
```

### `KERMIT_CMD_UNKA`

```c
#define KERMIT_CMD_UNKA 0xA
```

### `KERMIT_CMD_UNKB`

```c
#define KERMIT_CMD_UNKB 0xB
```

### `KERMIT_CMD_UNKC`

```c
#define KERMIT_CMD_UNKC 0xC
```

### `KERMIT_CMD_INIT`

```c
#define KERMIT_CMD_INIT 0x0
```

### `KERMIT_CMD_GET_SWITCH_INTERNAL_STATE`

```c
#define KERMIT_CMD_GET_SWITCH_INTERNAL_STATE 0x2
```

### `KERMIT_CMD_GET_ETHER_ADDR`

```c
#define KERMIT_CMD_GET_ETHER_ADDR 0x3
```

### `KERMIT_CMD_ADHOC_CTL_INIT`

```c
#define KERMIT_CMD_ADHOC_CTL_INIT 0x6
```

### `KERMIT_CMD_ADHOC_CTL_TERM`

```c
#define KERMIT_CMD_ADHOC_CTL_TERM 0x7
```

### `KERMIT_CMD_ADHOC_SCAN`

```c
#define KERMIT_CMD_ADHOC_SCAN 0x8
```

### `KERMIT_CMD_ADHOC_JOIN`

```c
#define KERMIT_CMD_ADHOC_JOIN 0x9
```

### `KERMIT_CMD_ADHOC_CREATE`

```c
#define KERMIT_CMD_ADHOC_CREATE 0xA
```

### `KERMIT_CMD_ADHOC_LEAVE`

```c
#define KERMIT_CMD_ADHOC_LEAVE 0xB
```

### `KERMIT_CMD_ADHOC_TX_DATA`

```c
#define KERMIT_CMD_ADHOC_TX_DATA 0xC
```

### `KERMIT_CMD_ADHOC_RX_DATA`

```c
#define KERMIT_CMD_ADHOC_RX_DATA 0xD
```

### `KERMIT_CMD_INET_INIT`

```c
#define KERMIT_CMD_INET_INIT 0xE
```

### `KERMIT_CMD_INET_START`

```c
#define KERMIT_CMD_INET_START 0xF
```

### `KERMIT_CMD_INET_TERM`

```c
#define KERMIT_CMD_INET_TERM 0x10
```

### `KERMIT_CMD_INET_SOCKET`

```c
#define KERMIT_CMD_INET_SOCKET 0x11
```

### `KERMIT_CMD_INET_CLOSE`

```c
#define KERMIT_CMD_INET_CLOSE 0x12
```

### `KERMIT_CMD_INET_BIND`

```c
#define KERMIT_CMD_INET_BIND 0x13
```

### `KERMIT_CMD_INET_LISTEN`

```c
#define KERMIT_CMD_INET_LISTEN 0x14
```

### `KERMIT_CMD_INET_CONNECT`

```c
#define KERMIT_CMD_INET_CONNECT 0x15
```

### `KERMIT_CMD_INET_SHUTDOWN`

```c
#define KERMIT_CMD_INET_SHUTDOWN 0x16
```

### `KERMIT_CMD_INET_POLL`

```c
#define KERMIT_CMD_INET_POLL 0x17
```

### `KERMIT_CMD_INET_ACCEPT`

```c
#define KERMIT_CMD_INET_ACCEPT 0x18
```

### `KERMIT_CMD_INET_GET_PEER_NAME`

```c
#define KERMIT_CMD_INET_GET_PEER_NAME 0x19
```

### `KERMIT_CMD_INET_GET_SOCK_NAME`

```c
#define KERMIT_CMD_INET_GET_SOCK_NAME 0x1A
```

### `KERMIT_CMD_INET_GET_OPT`

```c
#define KERMIT_CMD_INET_GET_OPT 0x1B
```

### `KERMIT_CMD_INET_SET_OPT`

```c
#define KERMIT_CMD_INET_SET_OPT 0x1C
```

### `KERMIT_CMD_INET_RECV_FROM`

```c
#define KERMIT_CMD_INET_RECV_FROM 0x1D
```

### `KERMIT_CMD_INET_SENDTO_INTERNAL`

```c
#define KERMIT_CMD_INET_SENDTO_INTERNAL 0x1E
```

### `KERMIT_CMD_INET_SOIOCTL`

```c
#define KERMIT_CMD_INET_SOIOCTL 0x1F
```

### `KERMIT_CMD_SUSPEND_WLAN`

```c
#define KERMIT_CMD_SUSPEND_WLAN 0x20
```

### `KERMIT_CMD_SET_WOL_PARAM`

```c
#define KERMIT_CMD_SET_WOL_PARAM 0x22
```

### `KERMIT_CMD_GET_WOL_INFO`

```c
#define KERMIT_CMD_GET_WOL_INFO 0x23
```

### `KERMIT_CMD_SET_HOST_DISCOVER`

```c
#define KERMIT_CMD_SET_HOST_DISCOVER 0x24
```

### `KERMIT_CMD_OSK_START`

```c
#define KERMIT_CMD_OSK_START (0x0)
```

### `KERMIT_CMD_OSK_SHUTDOWN`

```c
#define KERMIT_CMD_OSK_SHUTDOWN (0x1)
```

### `KERMIT_CMD_OSK_UPDATE`

```c
#define KERMIT_CMD_OSK_UPDATE (0x3)
```

### `KERMIT_CMD_ACTIVATE`

```c
#define KERMIT_CMD_ACTIVATE 0x15
```

### `KERMIT_CMD_DEACTIVATE`

```c
#define KERMIT_CMD_DEACTIVATE 0x16
```

### `KERMIT_CMD_SET_OP`

```c
#define KERMIT_CMD_SET_OP 0x19
```

### `KERMIT_CMD_SET_OP_BIS`

```c
#define KERMIT_CMD_SET_OP_BIS 0x1A
```

### `KERMIT_CMD_UNK1B`

```c
#define KERMIT_CMD_UNK1B 0x1B
```

### `KERNEL()`

```c
#define KERNEL(x) ((x & 0x80000000)? 1:0)
```

### `KERMIT_PACKET()`

```c
#define KERMIT_PACKET(x) (x | (2-KERNEL(x))*0x20000000)
```

### `ALIGN_64()`

```c
#define ALIGN_64(x) ((x) & -64)
```

### `KERMIT_CALLBACK_DISABLE`

```c
#define KERMIT_CALLBACK_DISABLE 0
```

## Typedefs

### `KermitPacket`

```c
typedef struct KermitPacket_ KermitPacket;
```

## Enumerations

### `enum KermitModes`

| Enumerator | Description |
|---|---|
| `KERMIT_MODE_NONE` |  |
| `KERMIT_MODE_UNK_1` |  |
| `KERMIT_MODE_UNK_2` |  |
| `KERMIT_MODE_MSFS` |  |
| `KERMIT_MODE_FLASHFS` |  |
| `KERMIT_MODE_AUDIOOUT` |  |
| `KERMIT_MODE_ME` |  |
| `KERMIT_MODE_LOWIO` |  |
| `KERMIT_MODE_POCS_USBPSPCM` |  |
| `KERMIT_MODE_PERIPHERAL` |  |
| `KERMIT_MODE_WLAN` |  |
| `KERMIT_MODE_AUDIOIN` |  |
| `KERMIT_MODE_USB` |  |
| `KERMIT_MODE_UTILITY` |  |
| `KERMIT_MODE_EXTRA_1` |  |
| `KERMIT_MODE_EXTRA_2` |  |

### `enum KermitVirtualInterrupts`

| Enumerator | Description |
|---|---|
| `KERMIT_VIRTUAL_INTR_NONE` |  |
| `KERMIT_VIRTUAL_INTR_AUDIO_CH1` |  |
| `KERMIT_VIRTUAL_INTR_AUDIO_CH2` |  |
| `KERMIT_VIRTUAL_INTR_AUDIO_CH3` |  |
| `KERMIT_VIRTUAL_INTR_ME_DMA_CH1` |  |
| `KERMIT_VIRTUAL_INTR_ME_DMA_CH2` |  |
| `KERMIT_VIRTUAL_INTR_ME_DMA_CH3` |  |
| `KERMIT_VIRTUAL_INTR_WLAN_CH1` |  |
| `KERMIT_VIRTUAL_INTR_WLAN_CH2` |  |
| `KERMIT_VIRTUAL_INTR_IMPOSE_CH1` |  |
| `KERMIT_VIRTUAL_INTR_POWER_CH1` |  |
| `KERMIT_VIRTUAL_INTR_UNKNOWN_CH1` |  |
| `KERMIT_VIRTUAL_INTR_USBGPS_CH1` |  |
| `KERMIT_VIRTUAL_INTR_USBPSPCM_CH1` |  |

### `enum KermitArgumentModes`

| Enumerator | Value | Description |
|---|---|---|
| `KERMIT_INPUT_MODE` | `0x1` |  |
| `KERMIT_OUTPUT_MODE` | `0x2` |  |

## Functions

### `sceKermit_driver_4F75AA05()`

```c
int sceKermit_driver_4F75AA05(KermitPacket *packet, u32 cmd_mode, u32 cmd, u32 argc, u32 allow_callback, u64 *resp);
```

### `sceKermitMemorySetArgument()`

```c
void sceKermitMemorySetArgument(KermitPacket *packet, u32 argc, u8 *buffer, u32 buffer_size, u32 io_mode);
```

### `sceKermitMemory_driver_80E1240A()`

```c
void sceKermitMemory_driver_80E1240A(u8 *data, u32 len);
```

### `sceKermitMemory_driver_90B662D0()`

```c
void sceKermitMemory_driver_90B662D0(u8 *data, u32 data_size);
```

### `sceKermitRegisterVirtualIntrHandler()`

```c
int sceKermitRegisterVirtualIntrHandler(u32 interrupt, void *handler);
```

### `sceKermitSendRequest()`

```c
int sceKermitSendRequest(SceKermitRequest *request, u32 mode, u32 cmd, int argc, u32 callback, u64 *response);
```

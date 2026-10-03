[PSPSDK documentation](../../README.md) › Files

# hprm/psphprm.h

```c
#include <psptypes.h>
```

Topics: [Hprm Remote](../../topics/Hprm.md)

## Enumerations

### `enum PspHprmKeys`

Enumeration of the remote keys.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_HPRM_PLAYPAUSE` | `0x1` |  |
| `PSP_HPRM_FORWARD` | `0x4` |  |
| `PSP_HPRM_BACK` | `0x8` |  |
| `PSP_HPRM_VOL_UP` | `0x10` |  |
| `PSP_HPRM_VOL_DOWN` | `0x20` |  |
| `PSP_HPRM_HOLD` | `0x80` |  |

## Functions

### `sceHprmPeekCurrentKey()`

```c
int sceHprmPeekCurrentKey(u32 *key);
```

Peek at the current being pressed on the remote.

**Parameters:**

- `key` – Pointer to the u32 to receive the key bitmap, should be one or more of [PspHprmKeys](#enum-psphprmkeys)

**Returns:** \< 0 on error

### `sceHprmPeekLatch()`

```c
int sceHprmPeekLatch(u32 *latch);
```

Peek at the current latch data.

**Parameters:**

- `latch` – Pointer a to a 4 dword array to contain the latch data.

**Returns:** \< 0 on error.

### `sceHprmReadLatch()`

```c
int sceHprmReadLatch(u32 *latch);
```

Read the current latch data.

**Parameters:**

- `latch` – Pointer a to a 4 dword array to contain the latch data.

**Returns:** \< 0 on error.

### `sceHprmIsHeadphoneExist()`

```c
int sceHprmIsHeadphoneExist(void);
```

Determines whether the headphones are plugged in.

**Returns:** 1 if the headphones are plugged in, else 0.

### `sceHprmIsRemoteExist()`

```c
int sceHprmIsRemoteExist(void);
```

Determines whether the remote is plugged in.

**Returns:** 1 if the remote is plugged in, else 0.

### `sceHprmIsMicrophoneExist()`

```c
int sceHprmIsMicrophoneExist(void);
```

Determines whether the microphone is plugged in.

**Returns:** 1 if the microphone is plugged in, else 0.

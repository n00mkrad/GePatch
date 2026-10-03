[PSPSDK documentation](../../README.md) › Files

# kernel/pspamctrl.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct SceMacKey`

```c
struct SceMacKey {
    int type;
    u8 key[16];
    u8 pad[16];
    int pad_size;
};
```

### `struct SceCipherKey`

```c
struct SceCipherKey {
    u32 type;
    u32 seed;
    u8 key[16];
};
```

## Typedefs

### `SceMacKey`

```c
typedef struct SceMacKey SceMacKey;
```

### `SceCipherKey`

```c
typedef struct SceCipherKey SceCipherKey;
```

## Enumerations

### `enum SceMacKeyType`

| Enumerator | Value | Description |
|---|---|---|
| `MAC_KEY_TYPE_UNK0` | `0` |  |
| `MAC_KEY_TYPE_UNK1` | `1` |  |
| `MAC_KEY_TYPE_FUSE_ID` | `2` | Use fuse ID. |
| `MAC_KEY_TYPE_FIXED` | `3` | Use fixed key.<br>MAC will need to encrypt again. |
| `MAC_KEY_TYPE_UNK6` | `6` |  |

### `enum SceCipherKeyType`

| Enumerator | Value | Description |
|---|---|---|
| `CIPHER_KEY_TYPE_FIXED` | `1` | Use fixed key. |
| `CIPHER_KEY_TYPE_FUSE_ID` | `2` | Use fuse ID. |

### `enum SceCipherKeyMode`

| Enumerator | Value | Description |
|---|---|---|
| `CIPHER_KEY_MODE_ENCRYPT` | `1` |  |
| `CIPHER_KEY_MODE_DECRYPT` | `2` |  |

## Functions

### `sceDrmBBMacInit()`

```c
int sceDrmBBMacInit(SceMacKey *mac_key, int type);
```

### `sceDrmBBMacUpdate()`

```c
int sceDrmBBMacUpdate(SceMacKey *mac_key, u8 *buf, int size);
```

### `sceAmctrl_driver_9227EA79()`

```c
int sceAmctrl_driver_9227EA79(SceMacKey *mac_key, u8 *buf, int size);
```

### `sceDrmBBMacFinal()`

```c
int sceDrmBBMacFinal(SceMacKey *mac_key, u8 *buf, u8 *version_key);
```

### `sceDrmBBMacFinal2()`

```c
int sceDrmBBMacFinal2(SceMacKey *mac_key, u8 *buf, u8 *version_key);
```

### `sceDrmBBCipherInit()`

```c
int sceDrmBBCipherInit(SceCipherKey *cipher_key, int type, int mode, u8 *header_key, u8 *version_key, int seed);
```

### `sceDrmBBCipherUpdate()`

```c
int sceDrmBBCipherUpdate(SceCipherKey *cipher_key, u8 *buf, int size);
```

### `sceAmctrl_driver_E04ADD4C()`

```c
int sceAmctrl_driver_E04ADD4C(SceCipherKey *cipher_key, u8 *buf, int size);
```

### `sceDrmBBCipherFinal()`

```c
int sceDrmBBCipherFinal(SceCipherKey *cipher_key);
```

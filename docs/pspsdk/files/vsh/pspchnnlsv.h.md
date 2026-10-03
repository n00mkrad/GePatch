[PSPSDK documentation](../../README.md) › Files

# vsh/pspchnnlsv.h

```c
#include <psptypes.h>
```

Topics: [Chnnlsv Library](../../topics/Chnnlsv.md)

## Data Structures

### `struct _pspChnnlsvContext1`

| Field | Description |
|---|---|
| `int mode` | Cipher mode. |
| `u8 data[16]` | Context data. |
| `u8 key[16]` | Context key. |
| `u32 size` | Data size. |

### `struct _pspChnnlsvContext2`

| Field | Description |
|---|---|
| `u32 mode` | Cipher mode. |
| `u32 unk4` |  |
| `u8 data[16]` |  |

## Macros

### `sceChnnlsv_E7833020`

```c
#define sceChnnlsv_E7833020 sceSdSetIndex
```

### `sceChnnlsv_F21A1FCA`

```c
#define sceChnnlsv_F21A1FCA sceSdRemoveValue
```

### `sceChnnlsv_C4C494F8`

```c
#define sceChnnlsv_C4C494F8 sceSdGetLastIndex
```

### `sceChnnlsv_ABFDFC8B`

```c
#define sceChnnlsv_ABFDFC8B sceSdCreateList
```

### `sceChnnlsv_850A7FA1`

```c
#define sceChnnlsv_850A7FA1 sceSdSetMember
```

### `sceChnnlsv_21BE78B4`

```c
#define sceChnnlsv_21BE78B4 sceSdCleanList
```

## Typedefs

### `SceSdContext1`

```c
typedef struct _pspChnnlsvContext1 SceSdContext1;
```

### `SceSdContext2`

```c
typedef struct _pspChnnlsvContext2 SceSdContext2;
```

### `pspChnnlsvContext1`

```c
typedef SceSdContext1 pspChnnlsvContext1;
```

### `pspChnnlsvContext2`

```c
typedef SceSdContext2 pspChnnlsvContext2;
```

## Functions

### `sceSdSetIndex()`

```c
int sceSdSetIndex(SceSdContext1 *ctx, int mode);
```

Initialize context.

**Parameters:**

- `ctx` – Context
- `mode` – Cipher mode

**Returns:** \< 0 on error

### `sceSdRemoveValue()`

```c
int sceSdRemoveValue(SceSdContext1 *ctx, unsigned char *data, int len);
```

Process data.

**Parameters:**

- `ctx` – Context
- `data` – Data (aligned to 0x10)
- `len` – Length (aligned to 0x10)

**Returns:** \< 0 on error

### `sceSdGetLastIndex()`

```c
int sceSdGetLastIndex(SceSdContext1 *ctx, unsigned char *hash, unsigned char *cryptkey);
```

Finalize hash.

**Parameters:**

- `ctx` – Context
- `hash` – Hash output (aligned to 0x10, 0x10 bytes long)
- `cryptkey` – Crypt key or NULL.

**Returns:** \< 0 on error

### `sceSdCreateList()`

```c
int sceSdCreateList(SceSdContext2 *ctx, int mode1, int mode2, unsigned char *hashkey, unsigned char *cipherkey);
```

Prepare a key, and set up integrity check.

**Parameters:**

- `ctx` – Context
- `mode1` – Cipher mode
- `mode2` – Encrypt mode (1 = encrypting, 2 = decrypting)
- `hashkey` – Key out
- `cipherkey` – Key in

**Returns:** \< 0 on error

### `sceSdSetMember()`

```c
int sceSdSetMember(SceSdContext2 *ctx, unsigned char *data, int len);
```

Process data for integrity check.

**Parameters:**

- `ctx` – Context
- `data` – Data (aligned to 0x10)
- `len` – Length (aligned to 0x10)

**Returns:** \< 0 on error

### `sceSdCleanList()`

```c
int sceSdCleanList(SceSdContext2 *ctx);
```

Check integrity.

**Parameters:**

- `ctx` – Context

**Returns:** \< 0 on error

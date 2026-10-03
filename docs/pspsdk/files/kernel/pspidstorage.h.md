[PSPSDK documentation](../../README.md) › Files

# kernel/pspidstorage.h

```c
#include <psptypes.h>
```

Topics: [Interface to the sceIdStorage_driver library.](../../topics/IdStorage.md)

## Functions

### `sceIdStorageLookup()`

```c
int sceIdStorageLookup(u16 key, u32 offset, void *buf, u32 len);
```

Retrieves the value associated with a key.

**Parameters:**

- `key` – idstorage key
- `offset` – offset within the 512 byte leaf
- `buf` – buffer with enough storage
- `len` – amount of data to retrieve (offset + len must be \<= 512 bytes)

### `sceIdStorageReadLeaf()`

```c
int sceIdStorageReadLeaf(u16 key, void *buf);
```

Retrieves the whole 512 byte container for the key.

**Parameters:**

- `key` – idstorage key
- `buf` – buffer with at last 512 bytes of storage

### `sceIdStorageWriteLeaf()`

```c
int sceIdStorageWriteLeaf(u16 key, void *buf);
```

[sceIdStorageWriteLeaf()](#sceidstoragewriteleaf) - Writes 512-bytes to idstorage key

**Parameters:**

- `key` – idstorage key
- `buf` – buffer with 512-btes of data

### `sceIdStorageIsReadOnly()`

```c
int sceIdStorageIsReadOnly(void);
```

[sceIdStorageIsReadOnly()](#sceidstorageisreadonly) - Checks idstorage for readonly status

### `sceIdStorageFlush()`

```c
int sceIdStorageFlush(void);
```

[sceIdStorageFlush()](#sceidstorageflush) - Finalizes a write

### `sceIdStorageCreateLeaf()`

```c
int sceIdStorageCreateLeaf(unsigned int leafid);
```

### `sceIdStorageCreateAtomicLeaves()`

```c
int sceIdStorageCreateAtomicLeaves(u16 *leaves, int n);
```

### `sceIdStorageFormat()`

```c
int sceIdStorageFormat(void);
```

### `sceIdStorageUnformat()`

```c
int sceIdStorageUnformat(void);
```

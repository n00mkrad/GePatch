[PSPSDK documentation](../../README.md) › Files

# net/pspssl.h

## Functions

### `sceSslInit()`

```c
int sceSslInit(int unknown1);
```

Init the ssl library.

**Parameters:**

- `unknown1` – Memory size? Pass 0x28000

**Returns:** 0 on success

### `sceSslEnd()`

```c
int sceSslEnd(void);
```

Terminate the ssl library.

**Returns:** 0 on success

### `sceSslGetUsedMemoryMax()`

```c
int sceSslGetUsedMemoryMax(unsigned int *memory);
```

Get the maximum memory size used by ssl.

**Parameters:**

- `memory` – Pointer where the maximum memory used value will be stored.

**Returns:** 0 on success

### `sceSslGetUsedMemoryCurrent()`

```c
int sceSslGetUsedMemoryCurrent(unsigned int *memory);
```

Get the current memory size used by ssl.

**Parameters:**

- `memory` – Pointer where the current memory used value will be stored.

**Returns:** 0 on success

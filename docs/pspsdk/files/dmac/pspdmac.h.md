[PSPSDK documentation](../../README.md) › Files

# dmac/pspdmac.h

```c
#include <psptypes.h>
```

## Functions

### `sceDmacMemcpy()`

```c
int sceDmacMemcpy(void *dst, const void *src, SceSize n);
```

Copy data in memory using DMAC.

**Parameters:**

- `dst` – The pointer to the destination
- `src` – The pointer to the source
- `n` – The size of data

**Returns:** 0 on success; otherwise an error code

### `sceDmacTryMemcpy()`

```c
int sceDmacTryMemcpy(void *dst, const void *src, SceSize n);
```

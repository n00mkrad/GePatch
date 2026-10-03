[PSPSDK documentation](../../README.md) › Files

# user/pspsuspend.h

```c
#include <psptypes.h>
```

## Functions

### `sceKernelVolatileMemLock()`

```c
int sceKernelVolatileMemLock(int unk, void **ptr, int *size);
```

Allocate the extra 4megs of RAM.

**Parameters:**

- `unk` – No idea as it is never used, set to anything
- `ptr` – Pointer to a pointer to hold the address of the memory
- `size` – Pointer to an int which will hold the size of the memory

**Returns:** 0 on success

### `sceKernelVolatileMemTryLock()`

```c
int sceKernelVolatileMemTryLock(int unk, void **ptr, int *size);
```

Try and allocate the extra 4megs of RAM, will return an error if something has already allocated it.

**Parameters:**

- `unk` – No idea as it is never used, set to anything
- `ptr` – Pointer to a pointer to hold the address of the memory
- `size` – Pointer to an int which will hold the size of the memory

**Returns:** 0 on success

### `sceKernelVolatileMemUnlock()`

```c
int sceKernelVolatileMemUnlock(int unk);
```

Deallocate the extra 4 megs of RAM.

**Parameters:**

- `unk` – Set to 0, otherwise it fails in 3.52+, possibly earlier

**Returns:** 0 on success

[PSPSDK documentation](../../README.md) › Files

# nand/pspnand_driver.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
```

## Functions

### `sceNandSetWriteProtect()`

```c
int sceNandSetWriteProtect(int protectFlag);
```

### `sceNandLock()`

```c
int sceNandLock(int writeFlag);
```

### `sceNandUnlock()`

```c
void sceNandUnlock(void);
```

### `sceNandReadStatus()`

```c
int sceNandReadStatus(void);
```

### `sceNandReset()`

```c
int sceNandReset(int flag);
```

### `sceNandReadId()`

```c
int sceNandReadId(void *buf, SceSize size);
```

### `sceNandReadPages()`

```c
int sceNandReadPages(u32 ppn, void *buf, void *buf2, u32 count);
```

### `sceNandReadPagesRawAll()`

```c
int sceNandReadPagesRawAll(u32 ppn, void *buf, void *spare, u32 count);
```

### `sceNandEraseBlock()`

```c
int sceNandEraseBlock(u32 ppn);
```

### `sceNandWriteAccess()`

```c
int sceNandWriteAccess(u32 ppn, void *buf, void *spare, int, unsigned int);
```

### `sceNandReadExtraOnly()`

```c
int sceNandReadExtraOnly(u32 ppn, void *buf, int);
```

### `sceNandGetPageSize()`

```c
int sceNandGetPageSize(void);
```

### `sceNandGetPagesPerBlock()`

```c
int sceNandGetPagesPerBlock(void);
```

### `sceNandGetTotalBlocks()`

```c
int sceNandGetTotalBlocks(void);
```

### `sceNandWriteBlockWithVerify()`

```c
int sceNandWriteBlockWithVerify(u32 ppn, void *buf, void *spare);
```

### `sceNandReadBlockWithRetry()`

```c
int sceNandReadBlockWithRetry(u32 ppn, void *buf, void *buf2);
```

### `sceNandEraseBlockWithRetry()`

```c
int sceNandEraseBlockWithRetry(u32 ppn);
```

### `sceNandIsBadBlock()`

```c
int sceNandIsBadBlock(u32 ppn);
```

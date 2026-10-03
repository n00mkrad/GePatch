[PSPSDK documentation](../../README.md) › Files

# user/psputils.h

```c
#include <psptypes.h>
#include <sys/time.h>
#include <time.h>
```

Topics: [Utils Library](../../topics/Utils.md)

## Data Structures

### `struct SceKernelTimeval`

This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.

```c
struct SceKernelTimeval {
    uint32_t tv_sec;
    uint32_t tv_usec;
};
```

### `struct _SceKernelUtilsMt19937Context`

Structure for holding a mersenne twister context.

```c
struct _SceKernelUtilsMt19937Context {
    unsigned int count;
    unsigned int state[624];
};
```

### `struct _SceKernelUtilsMd5Context`

Structure to hold the MD5 context.

```c
struct _SceKernelUtilsMd5Context {
    unsigned int h[4];
    unsigned int pad;
    SceUShort16 usRemains;
    SceUShort16 usComputed;
    SceULong64 ullTotalLen;
    unsigned char buf[64];
};
```

### `struct _SceKernelUtilsSha1Context`

Type to hold a sha1 context.

```c
struct _SceKernelUtilsSha1Context {
    unsigned int h[5];
    SceUShort16 usRemains;
    SceUShort16 usComputed;
    SceULong64 ullTotalLen;
    unsigned char buf[64];
};
```

## Typedefs

### `SceKernelTimeval`

```c
typedef struct SceKernelTimeval SceKernelTimeval;
```

This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.

### `SceKernelUtilsMt19937Context`

```c
typedef struct _SceKernelUtilsMt19937Context SceKernelUtilsMt19937Context;
```

Structure for holding a mersenne twister context.

### `SceKernelUtilsMd5Context`

```c
typedef struct _SceKernelUtilsMd5Context SceKernelUtilsMd5Context;
```

Structure to hold the MD5 context.

### `SceKernelUtilsSha1Context`

```c
typedef struct _SceKernelUtilsSha1Context SceKernelUtilsSha1Context;
```

Type to hold a sha1 context.

## Functions

### `sceKernelLibcTime()`

```c
time_t sceKernelLibcTime(time_t *t);
```

Get the time in seconds since the epoc (1st Jan 1970)

### `sceKernelLibcClock()`

```c
clock_t sceKernelLibcClock(void);
```

Get the processor clock used since the start of the process.

### `sceKernelLibcGettimeofday()`

```c
int sceKernelLibcGettimeofday(SceKernelTimeval *tp, struct timezone *tzp);
```

Get the current time of time and time zone information.

### `sceKernelDcacheWritebackAll()`

```c
void sceKernelDcacheWritebackAll(void);
```

Write back the data cache to memory.

### `sceKernelDcacheWritebackInvalidateAll()`

```c
void sceKernelDcacheWritebackInvalidateAll(void);
```

Write back and invalidate the data cache.

### `sceKernelDcacheWritebackRange()`

```c
void sceKernelDcacheWritebackRange(const void *p, unsigned int size);
```

Write back a range of addresses from the data cache to memory.

### `sceKernelDcacheWritebackInvalidateRange()`

```c
void sceKernelDcacheWritebackInvalidateRange(const void *p, unsigned int size);
```

Write back and invalidate a range of addresses in the data cache.

### `sceKernelDcacheInvalidateRange()`

```c
void sceKernelDcacheInvalidateRange(const void *p, unsigned int size);
```

Invalidate a range of addresses in data cache.

### `sceKernelIcacheInvalidateAll()`

```c
void sceKernelIcacheInvalidateAll(void);
```

Invalidate the instruction cache.

### `sceKernelIcacheInvalidateRange()`

```c
void sceKernelIcacheInvalidateRange(const void *p, unsigned int size);
```

Invalidate a range of addresses in the instruction cache.

### `sceKernelUtilsMt19937Init()`

```c
int sceKernelUtilsMt19937Init(SceKernelUtilsMt19937Context *ctx, u32 seed);
```

Function to initialise a mersenne twister context.

**Parameters:**

- `ctx` – Pointer to a context
- `seed` – A seed for the random function.

**Example::**

```c
SceKernelUtilsMt19937Context ctx;
sceKernelUtilsMt19937Init(&ctx, time(NULL));
u23 rand_val = sceKernelUtilsMt19937UInt(&ctx);
```

**Returns:** \< 0 on error.

### `sceKernelUtilsMt19937UInt()`

```c
u32 sceKernelUtilsMt19937UInt(SceKernelUtilsMt19937Context *ctx);
```

Function to return a new psuedo random number.

**Parameters:**

- `ctx` – Pointer to a pre-initialised context.

**Returns:** A pseudo random number (between 0 and MAX_INT).

### `sceKernelUtilsMd5Digest()`

```c
int sceKernelUtilsMd5Digest(u8 *data, u32 size, u8 *digest);
```

Function to perform an MD5 digest of a data block.

**Parameters:**

- `data` – Pointer to a data block to make a digest of.
- `size` – Size of the data block.
- `digest` – Pointer to a 16byte buffer to store the resulting digest

**Returns:** \< 0 on error.

### `sceKernelUtilsMd5BlockInit()`

```c
int sceKernelUtilsMd5BlockInit(SceKernelUtilsMd5Context *ctx);
```

Function to initialise a MD5 digest context.

**Parameters:**

- `ctx` – A context block to initialise

**Returns:** \< 0 on error.

**Example::**

```c
SceKernelUtilsMd5Context ctx;
u8 digest[16];
sceKernelUtilsMd5BlockInit(&ctx);
sceKernelUtilsMd5BlockUpdate(&ctx, (u8*) "Hello", 5);
sceKernelUtilsMd5BlockResult(&ctx, digest);
```

### `sceKernelUtilsMd5BlockUpdate()`

```c
int sceKernelUtilsMd5BlockUpdate(SceKernelUtilsMd5Context *ctx, u8 *data, u32 size);
```

Function to update the MD5 digest with a block of data.

**Parameters:**

- `ctx` – A filled in context block.
- `data` – The data block to hash.
- `size` – The size of the data to hash

**Returns:** \< 0 on error.

### `sceKernelUtilsMd5BlockResult()`

```c
int sceKernelUtilsMd5BlockResult(SceKernelUtilsMd5Context *ctx, u8 *digest);
```

Function to get the digest result of the MD5 hash.

**Parameters:**

- `ctx` – A filled in context block.
- `digest` – A 16 byte array to hold the digest.

**Returns:** \< 0 on error.

### `sceKernelUtilsSha1Digest()`

```c
int sceKernelUtilsSha1Digest(u8 *data, u32 size, u8 *digest);
```

Function to SHA1 hash a data block.

**Parameters:**

- `data` – The data to hash.
- `size` – The size of the data.
- `digest` – Pointer to a 20 byte array for storing the digest

**Returns:** \< 0 on error.

### `sceKernelUtilsSha1BlockInit()`

```c
int sceKernelUtilsSha1BlockInit(SceKernelUtilsSha1Context *ctx);
```

Function to initialise a context for SHA1 hashing.

**Parameters:**

- `ctx` – Pointer to a context.

**Returns:** \< 0 on error.

**Example::**

```c
SceKernelUtilsSha1Context ctx;
u8 digest[20];
sceKernelUtilsSha1BlockInit(&ctx);
sceKernelUtilsSha1BlockUpdate(&ctx, (u8*) "Hello", 5);
sceKernelUtilsSha1BlockResult(&ctx, digest);
```

### `sceKernelUtilsSha1BlockUpdate()`

```c
int sceKernelUtilsSha1BlockUpdate(SceKernelUtilsSha1Context *ctx, u8 *data, u32 size);
```

Function to update the current hash.

**Parameters:**

- `ctx` – Pointer to a prefilled context.
- `data` – The data block to hash.
- `size` – The size of the data block

**Returns:** \< 0 on error.

### `sceKernelUtilsSha1BlockResult()`

```c
int sceKernelUtilsSha1BlockResult(SceKernelUtilsSha1Context *ctx, u8 *digest);
```

Function to get the result of the SHA1 hash.

**Parameters:**

- `ctx` – Pointer to a prefilled context.
- `digest` – A pointer to a 20 byte array to contain the digest.

**Returns:** \< 0 on error.

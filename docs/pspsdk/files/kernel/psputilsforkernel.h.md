[PSPSDK documentation](../../README.md) › Files

# kernel/psputilsforkernel.h

## Functions

### `sceKernelGzipDecompress()`

```c
int sceKernelGzipDecompress(u8 *dest, u32 destSize, const u8 *src, u8 **src_out);
```

Decompress gzip'd data (requires kernel mode)

**Parameters:**

- `dest` – pointer to destination buffer
- `destSize` – size of destination buffer
- `src` – pointer to source (compressed) data
- `src_out` – if not NULL, it will store the pointer to src + compressed_bytes_processed

**Returns:** size decompressed on success, \< 0 on error

### `sceKernelDeflateDecompress()`

```c
int sceKernelDeflateDecompress(u8 *dest, u32 destSize, const u8 *src, u8 **src_out);
```

Decompress deflate'd data (requires kernel mode)

**Parameters:**

- `dest` – pointer to destination buffer
- `destSize` – size of destination buffer
- `src` – pointer to source (compressed) data
- `src_out` – if not NULL, it will store the pointer to src + compressed_bytes_processed

**Returns:** size decompressed on success, \< 0 on error

### `sceKernelDcacheInvalidateAll()`

```c
void sceKernelDcacheInvalidateAll(void);
```

Invalidate the entire data cache.

### `sceKernelDcacheProbe()`

```c
int sceKernelDcacheProbe(void *addr);
```

Check whether the specified address is in the data cache.

**Parameters:**

- `addr` – The address to check

**Returns:** 0 = not cached, 1 = cache

### `sceKernelIcacheInvalidateAll()`

```c
void sceKernelIcacheInvalidateAll(void);
```

Invalidate the entire instruction cache.

### `sceKernelIcacheInvalidateRange()`

```c
void sceKernelIcacheInvalidateRange(const void *addr, unsigned int size);
```

Invalidate a instruction cache range.

**Parameters:**

- `addr` – The start address of the range.
- `size` – The size in bytes

### `sceKernelIcacheProbe()`

```c
int sceKernelIcacheProbe(const void *addr);
```

Check whether the specified address is in the instruction cache.

**Parameters:**

- `addr` – The address to check

**Returns:** 0 = not cached, 1 = cache

[PSPSDK documentation](../../README.md) › Files

# net/pspnet_resolver.h

```c
#include <netinet/in.h>
#include <pspkerneltypes.h>
#include <psptypes.h>
```

## Functions

### `sceNetResolverInit()`

```c
int sceNetResolverInit(void);
```

Inititalise the resolver library.

**Returns:** 0 on sucess, \< 0 on error.

### `sceNetResolverCreate()`

```c
int sceNetResolverCreate(int *rid, void *buf, SceSize buflen);
```

Create a resolver object.

**Parameters:**

- `rid` – Pointer to receive the resolver id
- `buf` – Temporary buffer
- `buflen` – Length of the temporary buffer

**Returns:** 0 on success, \< 0 on error

### `sceNetResolverDelete()`

```c
int sceNetResolverDelete(int rid);
```

Delete a resolver.

**Parameters:**

- `rid` – The resolver to delete

**Returns:** 0 on success, \< 0 on error

### `sceNetResolverStartNtoA()`

```c
int sceNetResolverStartNtoA(int rid, const char *hostname, struct in_addr *addr, unsigned int timeout, int retry);
```

Begin a name to address lookup.

**Parameters:**

- `rid` – Resolver id
- `hostname` – Name to resolve
- `addr` – Pointer to [in_addr](../libcglue/netinet/in.h.md#struct-in_addr) structure to receive the address
- `timeout` – Number of seconds before timeout
- `retry` – Number of retires

**Returns:** 0 on success, \< 0 on error

### `sceNetResolverStartAtoN()`

```c
int sceNetResolverStartAtoN(int rid, const struct in_addr *addr, char *hostname, SceSize hostname_len, unsigned int timeout, int retry);
```

Begin a address to name lookup.

**Parameters:**

- `rid` – -Resolver id
- `addr` – Pointer to the address to resolve
- `hostname` – Buffer to receive the name
- `hostname_len` – Length of the buffer
- `timeout` – Number of seconds before timeout
- `retry` – Number of retries

**Returns:** 0 on success, \< 0 on error

### `sceNetResolverStop()`

```c
int sceNetResolverStop(int rid);
```

Stop a resolver operation.

**Parameters:**

- `rid` – Resolver id

**Returns:** 0 on success, \< 0 on error

### `sceNetResolverTerm()`

```c
int sceNetResolverTerm(void);
```

Terminate the resolver library.

**Returns:** 0 on success, \< 0 on error

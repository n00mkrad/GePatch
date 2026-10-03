[PSPSDK documentation](../../README.md) › Files

# net/pspnet.h

## Data Structures

### `struct SceNetMallocStat`

```c
struct SceNetMallocStat {
    int pool;
    int maximum;
    int free;
};
```

## Typedefs

### `SceNetMallocStat`

```c
typedef struct SceNetMallocStat SceNetMallocStat;
```

## Functions

### `sceNetInit()`

```c
int sceNetInit(int poolsize, int calloutprio, int calloutstack, int netintrprio, int netintrstack);
```

Initialise the networking library.

**Parameters:**

- `poolsize` – Memory pool size (appears to be for the whole of the networking library).
- `calloutprio` – Priority of the SceNetCallout thread.
- `calloutstack` – Stack size of the SceNetCallout thread (defaults to 4096 on non 1.5 firmware regardless of what value is passed).
- `netintrprio` – Priority of the SceNetNetintr thread.
- `netintrstack` – Stack size of the SceNetNetintr thread (defaults to 4096 on non 1.5 firmware regardless of what value is passed).

**Returns:** 0 on success, \< 0 on error

### `sceNetTerm()`

```c
int sceNetTerm(void);
```

Terminate the networking library.

**Returns:** 0 on success, \< 0 on error

### `sceNetFreeThreadinfo()`

```c
int sceNetFreeThreadinfo(int thid);
```

Free (delete) thread info/data.

**Parameters:**

- `thid` – The thread id.

**Returns:** 0 on success, \< 0 on error

### `sceNetThreadAbort()`

```c
int sceNetThreadAbort(int thid);
```

Abort a thread.

**Parameters:**

- `thid` – The thread id.

**Returns:** 0 on success, \< 0 on error

### `sceNetEtherStrton()`

```c
void sceNetEtherStrton(char *name, unsigned char *mac);
```

Convert string to a Mac address.

**Parameters:**

- `name` – The string to convert.
- `mac` – Pointer to a buffer to store the result.

### `sceNetEtherNtostr()`

```c
void sceNetEtherNtostr(unsigned char *mac, char *name);
```

Convert Mac address to a string.

**Parameters:**

- `mac` – The Mac address to convert.
- `name` – Pointer to a buffer to store the result.

### `sceNetGetLocalEtherAddr()`

```c
int sceNetGetLocalEtherAddr(unsigned char *mac);
```

Retrieve the local Mac address.

**Parameters:**

- `mac` – Pointer to a buffer to store the result.

**Returns:** 0 on success, \< 0 on error

### `sceNetGetMallocStat()`

```c
int sceNetGetMallocStat(SceNetMallocStat *stat);
```

Retrieve the networking library memory usage.

**Parameters:**

- `stat` – Pointer to a [SceNetMallocStat](#struct-scenetmallocstat) type to store the result.

**Returns:** 0 on success, \< 0 on error

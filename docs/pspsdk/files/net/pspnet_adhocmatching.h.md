[PSPSDK documentation](../../README.md) › Files

# net/pspnet_adhocmatching.h

## Data Structures

### `struct pspAdhocMatchingMember`

Linked list for sceNetAdhocMatchingGetMembers.

```c
struct pspAdhocMatchingMember {
    struct pspAdhocMatchingMember * next;
    unsigned char mac[6];
    char unknown[2];
};
```

### `struct pspAdhocPoolStat`

Linked list for sceNetAdhocMatchingGetMembers.

| Field | Description |
|---|---|
| `int size` | Size of the pool. |
| `int maxsize` | Maximum size of the pool. |
| `int freesize` | Unused memory in the pool. |

## Typedefs

### `pspAdhocMatchingCallback`

```c
typedef void(* pspAdhocMatchingCallback) (int matchingid, int event, unsigned char *mac, int optlen, void *optdata))(int matchingid, int event, unsigned char *mac, int optlen, void *optdata);
```

Matching callback.

## Enumerations

### `enum pspAdhocMatchingEvents`

Matching events used in pspAdhocMatchingCallback.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_ADHOC_MATCHING_EVENT_HELLO` | `1` | Hello event.<br>optdata contains data if optlen > 0. |
| `PSP_ADHOC_MATCHING_EVENT_JOIN` | `2` | Join request.<br>optdata contains data if optlen > 0. |
| `PSP_ADHOC_MATCHING_EVENT_LEFT` | `3` | Target left matching. |
| `PSP_ADHOC_MATCHING_EVENT_REJECT` | `4` | Join request rejected. |
| `PSP_ADHOC_MATCHING_EVENT_CANCEL` | `5` | Join request cancelled. |
| `PSP_ADHOC_MATCHING_EVENT_ACCEPT` | `6` | Join request accepted.<br>optdata contains data if optlen > 0. |
| `PSP_ADHOC_MATCHING_EVENT_COMPLETE` | `7` | Matching is complete. |
| `PSP_ADHOC_MATCHING_EVENT_TIMEOUT` | `8` | Ping timeout event. |
| `PSP_ADHOC_MATCHING_EVENT_ERROR` | `9` | Error event. |
| `PSP_ADHOC_MATCHING_EVENT_DISCONNECT` | `10` | Peer disconnect event. |
| `PSP_ADHOC_MATCHING_EVENT_DATA` | `11` | Data received event.<br>optdata contains data if optlen > 0. |
| `PSP_ADHOC_MATCHING_EVENT_DATA_CONFIRM` | `12` | Data acknowledged event. |
| `PSP_ADHOC_MATCHING_EVENT_DATA_TIMEOUT` | `13` | Data timeout event. |

### `enum pspAdhocMatchingModes`

Matching modes used in sceNetAdhocMatchingCreate.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_ADHOC_MATCHING_MODE_HOST` | `1` | Host. |
| `PSP_ADHOC_MATCHING_MODE_CLIENT` | `2` | Client. |
| `PSP_ADHOC_MATCHING_MODE_PTP` | `3` | Peer to peer. |

## Functions

### `sceNetAdhocMatchingInit()`

```c
int sceNetAdhocMatchingInit(int memsize);
```

Initialise the Adhoc matching library.

**Parameters:**

- `memsize` – Internal memory pool size. Lumines uses 0x20000

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocMatchingTerm()`

```c
int sceNetAdhocMatchingTerm(void);
```

Terminate the Adhoc matching library.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocMatchingCreate()`

```c
int sceNetAdhocMatchingCreate(int mode, int maxpeers, unsigned short port, int bufsize, unsigned int hellodelay, unsigned int pingdelay, int initcount, unsigned int msgdelay, pspAdhocMatchingCallback callback);
```

Create an Adhoc matching object.

**Parameters:**

- `mode` – One of [pspAdhocMatchingModes](#enum-pspadhocmatchingmodes)
- `maxpeers` – Maximum number of peers to match (only used when mode is PSP_ADHOC_MATCHING_MODE_HOST)
- `port` – Port. Lumines uses 0x22B
- `bufsize` – Receiving buffer size
- `hellodelay` – Hello message send delay in microseconds (only used when mode is PSP_ADHOC_MATCHING_MODE_HOST or PSP_ADHOC_MATCHING_MODE_PTP)
- `pingdelay` – Ping send delay in microseconds. Lumines uses 0x5B8D80 (only used when mode is PSP_ADHOC_MATCHING_MODE_HOST or PSP_ADHOC_MATCHING_MODE_PTP)
- `initcount` – Initial count of the of the resend counter. Lumines uses 3
- `msgdelay` – Message send delay in microseconds
- `callback` – Callback to be called for matching

**Returns:** ID of object on success, \< 0 on error.

### `sceNetAdhocMatchingDelete()`

```c
int sceNetAdhocMatchingDelete(int matchingid);
```

Delete an Adhoc matching object.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingStart()`

```c
int sceNetAdhocMatchingStart(int matchingid, int evthpri, int evthstack, int inthpri, int inthstack, int optlen, void *optdata);
```

Start a matching object.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `evthpri` – Priority of the event handler thread. Lumines uses 0x10
- `evthstack` – Stack size of the event handler thread. Lumines uses 0x2000
- `inthpri` – Priority of the input handler thread. Lumines uses 0x10
- `inthstack` – Stack size of the input handler thread. Lumines uses 0x2000
- `optlen` – Size of hellodata
- `optdata` – Pointer to block of data passed to callback

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocMatchingStop()`

```c
int sceNetAdhocMatchingStop(int matchingid);
```

Stop a matching object.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingSelectTarget()`

```c
int sceNetAdhocMatchingSelectTarget(int matchingid, unsigned char *mac, int optlen, void *optdata);
```

Select a matching target.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `mac` – MAC address to select
- `optlen` – Optional data length
- `optdata` – Pointer to the optional data

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingCancelTarget()`

```c
int sceNetAdhocMatchingCancelTarget(int matchingid, unsigned char *mac);
```

Cancel a matching target.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `mac` – The MAC address to cancel

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingCancelTargetWithOpt()`

```c
int sceNetAdhocMatchingCancelTargetWithOpt(int matchingid, unsigned char *mac, int optlen, void *optdata);
```

Cancel a matching target (with optional data)

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `mac` – The MAC address to cancel
- `optlen` – Optional data length
- `optdata` – Pointer to the optional data

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingSendData()`

```c
int sceNetAdhocMatchingSendData(int matchingid, unsigned char *mac, int datalen, void *data);
```

Send data to a matching target.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `mac` – The MAC address to send the data to
- `datalen` – Length of the data
- `data` – Pointer to the data

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingAbortSendData()`

```c
int sceNetAdhocMatchingAbortSendData(int matchingid, unsigned char *mac);
```

Abort a data send to a matching target.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `mac` – The MAC address to send the data to

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingSetHelloOpt()`

```c
int sceNetAdhocMatchingSetHelloOpt(int matchingid, int optlen, void *optdata);
```

Set the optional hello message.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `optlen` – Length of the hello data
- `optdata` – Pointer to the hello data

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingGetHelloOpt()`

```c
int sceNetAdhocMatchingGetHelloOpt(int matchingid, int *optlen, void *optdata);
```

Get the optional hello message.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `optlen` – Length of the hello data
- `optdata` – Pointer to the hello data

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingGetMembers()`

```c
int sceNetAdhocMatchingGetMembers(int matchingid, int *length, void *buf);
```

Get a list of matching members.

**Parameters:**

- `matchingid` – The ID returned from [sceNetAdhocMatchingCreate](#scenetadhocmatchingcreate)
- `length` – The length of the list.
- `buf` – An allocated area of size length.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocMatchingGetPoolMaxAlloc()`

```c
int sceNetAdhocMatchingGetPoolMaxAlloc(void);
```

Get the maximum memory usage by the matching library.

**Returns:** The memory usage on success, \< 0 on error.

### `sceNetAdhocMatchingGetPoolStat()`

```c
int sceNetAdhocMatchingGetPoolStat(struct pspAdhocPoolStat *poolstat);
```

Get the status of the memory pool used by the matching library.

**Parameters:**

- `poolstat` – A [pspAdhocPoolStat](#struct-pspadhocpoolstat).

**Returns:** 0 on success, \< 0 on error.

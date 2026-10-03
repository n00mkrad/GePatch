[PSPSDK documentation](../../README.md) › Files

# net/pspnet_adhoc.h

## Data Structures

### `struct pdpStatStruct`

PDP status structure.

| Field | Description |
|---|---|
| `struct pdpStatStruct * next` | Pointer to next PDP structure in list. |
| `int pdpId` | pdp ID |
| `unsigned char mac[6]` | MAC address. |
| `unsigned short port` | Port. |
| `unsigned int rcvdData` | Bytes received. |

### `struct ptpStatStruct`

PTP status structure.

| Field | Description |
|---|---|
| `struct ptpStatStruct * next` | Pointer to next PTP structure in list. |
| `int ptpId` | ptp ID |
| `unsigned char mac[6]` | MAC address. |
| `unsigned char peermac[6]` | Peer MAC address. |
| `unsigned short port` | Port. |
| `unsigned short peerport` | Peer Port. |
| `unsigned int sentData` | Bytes sent. |
| `unsigned int rcvdData` | Bytes received. |
| `int unk1` | Unknown. |

## Typedefs

### `pdpStatStruct`

```c
typedef struct pdpStatStruct pdpStatStruct;
```

PDP status structure.

### `ptpStatStruct`

```c
typedef struct ptpStatStruct ptpStatStruct;
```

PTP status structure.

## Functions

### `sceNetAdhocInit()`

```c
int sceNetAdhocInit(void);
```

Initialise the adhoc library.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocTerm()`

```c
int sceNetAdhocTerm(void);
```

Terminate the adhoc library.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocPdpCreate()`

```c
int sceNetAdhocPdpCreate(unsigned char *mac, unsigned short port, unsigned int bufsize, int unk1);
```

Create a PDP object.

**Parameters:**

- `mac` – Your MAC address (from sceWlanGetEtherAddr)
- `port` – Port to use, lumines uses 0x309
- `bufsize` – Socket buffer size, lumines sets to 0x400
- `unk1` – Unknown, lumines sets to 0

**Returns:** The ID of the PDP object (\< 0 on error)

### `sceNetAdhocPdpDelete()`

```c
int sceNetAdhocPdpDelete(int id, int unk1);
```

Delete a PDP object.

**Parameters:**

- `id` – The ID returned from [sceNetAdhocPdpCreate](#scenetadhocpdpcreate)
- `unk1` – Unknown, set to 0

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocPdpSend()`

```c
int sceNetAdhocPdpSend(int id, unsigned char *destMacAddr, unsigned short port, void *data, unsigned int len, unsigned int timeout, int nonblock);
```

Set a PDP packet to a destination.

**Parameters:**

- `id` – The ID as returned by [sceNetAdhocPdpCreate](#scenetadhocpdpcreate)
- `destMacAddr` – The destination MAC address, can be set to all 0xFF for broadcast
- `port` – The port to send to
- `data` – The data to send
- `len` – The length of the data.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** Bytes sent, \< 0 on error

### `sceNetAdhocPdpRecv()`

```c
int sceNetAdhocPdpRecv(int id, unsigned char *srcMacAddr, unsigned short *port, void *data, void *dataLength, unsigned int timeout, int nonblock);
```

Receive a PDP packet.

**Parameters:**

- `id` – The ID of the PDP object, as returned by [sceNetAdhocPdpCreate](#scenetadhocpdpcreate)
- `srcMacAddr` – Buffer to hold the source mac address of the sender
- `port` – Buffer to hold the port number of he received data
- `data` – Data buffer
- `dataLength` – The length of the data buffer
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** Number of bytes received, \< 0 on error.

### `sceNetAdhocGetPdpStat()`

```c
int sceNetAdhocGetPdpStat(int *size, pdpStatStruct *stat);
```

Get the status of all PDP objects.

**Parameters:**

- `size` – Pointer to the size of the stat array (e.g 20 for one structure)
- `stat` – Pointer to a list of [pdpStatStruct](#struct-pdpstatstruct) structures.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocGameModeCreateMaster()`

```c
int sceNetAdhocGameModeCreateMaster(void *data, int size);
```

Create own game object type data.

**Parameters:**

- `data` – A pointer to the game object data.
- `size` – Size of the game data.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocGameModeCreateReplica()`

```c
int sceNetAdhocGameModeCreateReplica(unsigned char *mac, void *data, int size);
```

Create peer game object type data.

**Parameters:**

- `mac` – The mac address of the peer.
- `data` – A pointer to the game object data.
- `size` – Size of the game data.

**Returns:** The id of the replica on success, \< 0 on error.

### `sceNetAdhocGameModeUpdateMaster()`

```c
int sceNetAdhocGameModeUpdateMaster(void);
```

Update own game object type data.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocGameModeUpdateReplica()`

```c
int sceNetAdhocGameModeUpdateReplica(int id, int unk1);
```

Update peer game object type data.

**Parameters:**

- `id` – The id of the replica returned by sceNetAdhocGameModeCreateReplica.
- `unk1` – Pass 0.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocGameModeDeleteMaster()`

```c
int sceNetAdhocGameModeDeleteMaster(void);
```

Delete own game object type data.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocGameModeDeleteReplica()`

```c
int sceNetAdhocGameModeDeleteReplica(int id);
```

Delete peer game object type data.

**Parameters:**

- `id` – The id of the replica.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocPtpOpen()`

```c
int sceNetAdhocPtpOpen(unsigned char *srcmac, unsigned short srcport, unsigned char *destmac, unsigned short destport, unsigned int bufsize, unsigned int delay, int count, int unk1);
```

Open a PTP connection.

**Parameters:**

- `srcmac` – Local mac address.
- `srcport` – Local port.
- `destmac` – Destination mac.
- `destport` – Destination port
- `bufsize` – Socket buffer size
- `delay` – Interval between retrying (microseconds).
- `count` – Number of retries.
- `unk1` – Pass 0.

**Returns:** A socket ID on success, \< 0 on error.

### `sceNetAdhocPtpConnect()`

```c
int sceNetAdhocPtpConnect(int id, unsigned int timeout, int nonblock);
```

Wait for connection created by [sceNetAdhocPtpOpen()](#scenetadhocptpopen)

**Parameters:**

- `id` – A socket ID.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocPtpListen()`

```c
int sceNetAdhocPtpListen(unsigned char *srcmac, unsigned short srcport, unsigned int bufsize, unsigned int delay, int count, int queue, int unk1);
```

Wait for an incoming PTP connection.

**Parameters:**

- `srcmac` – Local mac address.
- `srcport` – Local port.
- `bufsize` – Socket buffer size
- `delay` – Interval between retrying (microseconds).
- `count` – Number of retries.
- `queue` – Connection queue length.
- `unk1` – Pass 0.

**Returns:** A socket ID on success, \< 0 on error.

### `sceNetAdhocPtpAccept()`

```c
int sceNetAdhocPtpAccept(int id, unsigned char *mac, unsigned short *port, unsigned int timeout, int nonblock);
```

Accept an incoming PTP connection.

**Parameters:**

- `id` – A socket ID.
- `mac` – Connecting peers mac.
- `port` – Connecting peers port.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocPtpSend()`

```c
int sceNetAdhocPtpSend(int id, void *data, int *datasize, unsigned int timeout, int nonblock);
```

Send data.

**Parameters:**

- `id` – A socket ID.
- `data` – Data to send.
- `datasize` – Size of the data.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** 0 success, \< 0 on error.

### `sceNetAdhocPtpRecv()`

```c
int sceNetAdhocPtpRecv(int id, void *data, int *datasize, unsigned int timeout, int nonblock);
```

Receive data.

**Parameters:**

- `id` – A socket ID.
- `data` – Buffer for the received data.
- `datasize` – Size of the data received.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocPtpFlush()`

```c
int sceNetAdhocPtpFlush(int id, unsigned int timeout, int nonblock);
```

Wait for data in the buffer to be sent.

**Parameters:**

- `id` – A socket ID.
- `timeout` – Timeout in microseconds.
- `nonblock` – Set to 0 to block, 1 for non-blocking.

**Returns:** A socket ID on success, \< 0 on error.

### `sceNetAdhocPtpClose()`

```c
int sceNetAdhocPtpClose(int id, int unk1);
```

Close a socket.

**Parameters:**

- `id` – A socket ID.
- `unk1` – Pass 0.

**Returns:** A socket ID on success, \< 0 on error.

### `sceNetAdhocGetPtpStat()`

```c
int sceNetAdhocGetPtpStat(int *size, ptpStatStruct *stat);
```

Get the status of all PTP objects.

**Parameters:**

- `size` – Pointer to the size of the stat array (e.g 20 for one structure)
- `stat` – Pointer to a list of [ptpStatStruct](#struct-ptpstatstruct) structures.

**Returns:** 0 on success, \< 0 on error

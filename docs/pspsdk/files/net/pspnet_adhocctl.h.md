[PSPSDK documentation](../../README.md) › Files

# net/pspnet_adhocctl.h

## Data Structures

### `struct productStruct`

Product structure.

| Field | Description |
|---|---|
| `int unknown` | Unknown, set to 0, other values used are 1 and 2.<br>Not sure on what they represent |
| `char product[9]` | The product ID string. |
| `char unk[3]` |  |

### `struct SceNetAdhocctlPeerInfo`

Peer info structure.

| Field | Description |
|---|---|
| `struct SceNetAdhocctlPeerInfo * next` |  |
| `char nickname[128]` | Nickname. |
| `unsigned char mac[6]` | Mac address. |
| `unsigned char unknown[6]` | Unknown. |
| `unsigned long timestamp` | Time stamp. |

### `struct SceNetAdhocctlScanInfo`

Scan info structure.

| Field | Description |
|---|---|
| `struct SceNetAdhocctlScanInfo * next` |  |
| `int channel` | Channel number. |
| `char name[8]` | Name of the connection (alphanumeric characters only) |
| `unsigned char bssid[6]` | The BSSID. |
| `unsigned char unknown[2]` | Unknown. |
| `int unknown2` | Unknown. |

### `struct SceNetAdhocctlGameModeInfo`

| Field | Description |
|---|---|
| `int count` | Number of peers (including self) |
| `unsigned char macs[16][6]` | MAC addresses of peers (including self) |

### `struct SceNetAdhocctlParams`

Params structure.

| Field | Description |
|---|---|
| `int channel` | Channel number. |
| `char name[8]` | Name of the connection. |
| `char nickname[128]` | Nickname. |
| `unsigned char bssid[6]` | The BSSID. |

## Typedefs

### `SceNetAdhocctlPeerInfo`

```c
typedef struct SceNetAdhocctlPeerInfo SceNetAdhocctlPeerInfo;
```

Peer info structure.

### `SceNetAdhocctlScanInfo`

```c
typedef struct SceNetAdhocctlScanInfo SceNetAdhocctlScanInfo;
```

Scan info structure.

### `SceNetAdhocctlGameModeInfo`

```c
typedef struct SceNetAdhocctlGameModeInfo SceNetAdhocctlGameModeInfo;
```

### `SceNetAdhocctlParams`

```c
typedef struct SceNetAdhocctlParams SceNetAdhocctlParams;
```

Params structure.

### `sceNetAdhocctlHandler`

```c
typedef void(* sceNetAdhocctlHandler) (int flag, int error, void *unknown))(int flag, int error, void *unknown);
```

## Functions

### `sceNetAdhocctlInit()`

```c
int sceNetAdhocctlInit(int stacksize, int priority, struct productStruct *product);
```

Initialise the Adhoc control library.

**Parameters:**

- `stacksize` – Stack size of the adhocctl thread. Set to 0x2000
- `priority` – Priority of the adhocctl thread. Set to 0x30
- `product` – Pass a filled in [productStruct](#struct-productstruct)

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocctlTerm()`

```c
int sceNetAdhocctlTerm(void);
```

Terminate the Adhoc control library.

**Returns:** 0 on success, \< on error.

### `sceNetAdhocctlConnect()`

```c
int sceNetAdhocctlConnect(const char *name);
```

Connect to the Adhoc control.

**Parameters:**

- `name` – The name of the connection (maximum 8 alphanumeric characters).

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlDisconnect()`

```c
int sceNetAdhocctlDisconnect(void);
```

Disconnect from the Adhoc control.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocctlGetState()`

```c
int sceNetAdhocctlGetState(int *event);
```

Get the state of the Adhoc control.

**Parameters:**

- `event` – Pointer to an integer to receive the status. Can continue when it becomes 1.

**Returns:** 0 on success, \< 0 on error

### `sceNetAdhocctlCreate()`

```c
int sceNetAdhocctlCreate(const char *name);
```

Connect to the Adhoc control (as a host)

**Parameters:**

- `name` – The name of the connection (maximum 8 alphanumeric characters).

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlJoin()`

```c
int sceNetAdhocctlJoin(SceNetAdhocctlScanInfo *scaninfo);
```

Connect to the Adhoc control (as a client)

**Parameters:**

- `scaninfo` – A valid [SceNetAdhocctlScanInfo](#struct-scenetadhocctlscaninfo) struct that has been filled by sceNetAchocctlGetScanInfo

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetAdhocId()`

```c
int sceNetAdhocctlGetAdhocId(struct productStruct *product);
```

Get the adhoc ID.

**Parameters:**

- `product` – A pointer to a [productStruct](#struct-productstruct)

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlCreateEnterGameMode()`

```c
int sceNetAdhocctlCreateEnterGameMode(const char *name, int unknown, int num, unsigned char *macs, unsigned int timeout, int unknown2);
```

Connect to the Adhoc control game mode (as a host)

**Parameters:**

- `name` – The name of the connection (maximum 8 alphanumeric characters).
- `unknown` – Pass 1.
- `num` – The total number of players (including the host).
- `macs` – A pointer to a list of the participating mac addresses, host first, then clients.
- `timeout` – Timeout in microseconds.
- `unknown2` – pass 0.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlJoinEnterGameMode()`

```c
int sceNetAdhocctlJoinEnterGameMode(const char *name, unsigned char *hostmac, unsigned int timeout, int unknown);
```

Connect to the Adhoc control game mode (as a client)

**Parameters:**

- `name` – The name of the connection (maximum 8 alphanumeric characters).
- `hostmac` – The mac address of the host.
- `timeout` – Timeout in microseconds.
- `unknown` – pass 0.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetGameModeInfo()`

```c
int sceNetAdhocctlGetGameModeInfo(SceNetAdhocctlGameModeInfo *gamemodeinfo);
```

Get game mode information.

**Parameters:**

- `gamemodeinfo` – Pointer to store the info.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlExitGameMode()`

```c
int sceNetAdhocctlExitGameMode(void);
```

Exit game mode.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetPeerList()`

```c
int sceNetAdhocctlGetPeerList(int *length, void *buf);
```

Get a list of peers.

**Parameters:**

- `length` – The length of the list.
- `buf` – An allocated area of size length.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetPeerInfo()`

```c
int sceNetAdhocctlGetPeerInfo(unsigned char *mac, int size, SceNetAdhocctlPeerInfo *peerinfo);
```

Get peer information.

**Parameters:**

- `mac` – The mac address of the peer.
- `size` – Size of peerinfo.
- `peerinfo` – Pointer to store the information.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlScan()`

```c
int sceNetAdhocctlScan(void);
```

Scan the adhoc channels.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetScanInfo()`

```c
int sceNetAdhocctlGetScanInfo(int *length, void *buf);
```

Get the results of a scan.

**Parameters:**

- `length` – The length of the list.
- `buf` – An allocated area of size length.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlAddHandler()`

```c
int sceNetAdhocctlAddHandler(sceNetAdhocctlHandler handler, void *unknown);
```

Register an adhoc event handler.

**Parameters:**

- `handler` – The event handler.
- `unknown` – Pass NULL.

**Returns:** Handler id on success, \< 0 on error.

### `sceNetAdhocctlDelHandler()`

```c
int sceNetAdhocctlDelHandler(int id);
```

Delete an adhoc event handler.

**Parameters:**

- `id` – The handler id as returned by sceNetAdhocctlAddHandler.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetNameByAddr()`

```c
int sceNetAdhocctlGetNameByAddr(unsigned char *mac, char *nickname);
```

Get nickname from a mac address.

**Parameters:**

- `mac` – The mac address.
- `nickname` – Pointer to a char buffer where the nickname will be stored.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetAddrByName()`

```c
int sceNetAdhocctlGetAddrByName(char *nickname, int *length, void *buf);
```

Get mac address from nickname.

**Parameters:**

- `nickname` – The nickname.
- `length` – The length of the list.
- `buf` – An allocated area of size length.

**Returns:** 0 on success, \< 0 on error.

### `sceNetAdhocctlGetParameter()`

```c
int sceNetAdhocctlGetParameter(SceNetAdhocctlParams *params);
```

Get Adhocctl parameter.

**Parameters:**

- `params` – Pointer to a [SceNetAdhocctlParams](#struct-scenetadhocctlparams)

**Returns:** 0 on success, \< 0 on error.

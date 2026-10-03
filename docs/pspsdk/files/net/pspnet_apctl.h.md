[PSPSDK documentation](../../README.md) › Files

# net/pspnet_apctl.h

## Data Structures

### `union SceNetApctlInfo`

```c
union SceNetApctlInfo {
    char name[64];
    unsigned char bssid[6];
    unsigned char ssid[32];
    unsigned int ssidLength;
    unsigned int securityType;
    unsigned char strength;
    unsigned char channel;
    unsigned char powerSave;
    char ip[16];
    char subNetMask[16];
    char gateway[16];
    char primaryDns[16];
    char secondaryDns[16];
    unsigned int useProxy;
    char proxyUrl[128];
    unsigned short proxyPort;
    unsigned int eapType;
    unsigned int startBrowser;
    unsigned int wifisp;
};
```

## Macros

### `PSP_NET_APCTL_STATE_DISCONNECTED`

```c
#define PSP_NET_APCTL_STATE_DISCONNECTED 0
```

### `PSP_NET_APCTL_STATE_SCANNING`

```c
#define PSP_NET_APCTL_STATE_SCANNING 1
```

### `PSP_NET_APCTL_STATE_JOINING`

```c
#define PSP_NET_APCTL_STATE_JOINING 2
```

### `PSP_NET_APCTL_STATE_GETTING_IP`

```c
#define PSP_NET_APCTL_STATE_GETTING_IP 3
```

### `PSP_NET_APCTL_STATE_GOT_IP`

```c
#define PSP_NET_APCTL_STATE_GOT_IP 4
```

### `PSP_NET_APCTL_STATE_EAP_AUTH`

```c
#define PSP_NET_APCTL_STATE_EAP_AUTH 5
```

### `PSP_NET_APCTL_STATE_KEY_EXCHANGE`

```c
#define PSP_NET_APCTL_STATE_KEY_EXCHANGE 6
```

### `PSP_NET_APCTL_EVENT_CONNECT_REQUEST`

```c
#define PSP_NET_APCTL_EVENT_CONNECT_REQUEST 0
```

### `PSP_NET_APCTL_EVENT_SCAN_REQUEST`

```c
#define PSP_NET_APCTL_EVENT_SCAN_REQUEST 1
```

### `PSP_NET_APCTL_EVENT_SCAN_COMPLETE`

```c
#define PSP_NET_APCTL_EVENT_SCAN_COMPLETE 2
```

### `PSP_NET_APCTL_EVENT_ESTABLISHED`

```c
#define PSP_NET_APCTL_EVENT_ESTABLISHED 3
```

### `PSP_NET_APCTL_EVENT_GET_IP`

```c
#define PSP_NET_APCTL_EVENT_GET_IP 4
```

### `PSP_NET_APCTL_EVENT_DISCONNECT_REQUEST`

```c
#define PSP_NET_APCTL_EVENT_DISCONNECT_REQUEST 5
```

### `PSP_NET_APCTL_EVENT_ERROR`

```c
#define PSP_NET_APCTL_EVENT_ERROR 6
```

### `PSP_NET_APCTL_EVENT_INFO`

```c
#define PSP_NET_APCTL_EVENT_INFO 7
```

### `PSP_NET_APCTL_EVENT_EAP_AUTH`

```c
#define PSP_NET_APCTL_EVENT_EAP_AUTH 8
```

### `PSP_NET_APCTL_EVENT_KEY_EXCHANGE`

```c
#define PSP_NET_APCTL_EVENT_KEY_EXCHANGE 9
```

### `PSP_NET_APCTL_EVENT_RECONNECT`

```c
#define PSP_NET_APCTL_EVENT_RECONNECT 10
```

### `PSP_NET_APCTL_INFO_PROFILE_NAME`

```c
#define PSP_NET_APCTL_INFO_PROFILE_NAME 0
```

### `PSP_NET_APCTL_INFO_BSSID`

```c
#define PSP_NET_APCTL_INFO_BSSID 1
```

### `PSP_NET_APCTL_INFO_SSID`

```c
#define PSP_NET_APCTL_INFO_SSID 2
```

### `PSP_NET_APCTL_INFO_SSID_LENGTH`

```c
#define PSP_NET_APCTL_INFO_SSID_LENGTH 3
```

### `PSP_NET_APCTL_INFO_SECURITY_TYPE`

```c
#define PSP_NET_APCTL_INFO_SECURITY_TYPE 4
```

### `PSP_NET_APCTL_INFO_STRENGTH`

```c
#define PSP_NET_APCTL_INFO_STRENGTH 5
```

### `PSP_NET_APCTL_INFO_CHANNEL`

```c
#define PSP_NET_APCTL_INFO_CHANNEL 6
```

### `PSP_NET_APCTL_INFO_POWER_SAVE`

```c
#define PSP_NET_APCTL_INFO_POWER_SAVE 7
```

### `PSP_NET_APCTL_INFO_IP`

```c
#define PSP_NET_APCTL_INFO_IP 8
```

### `PSP_NET_APCTL_INFO_SUBNETMASK`

```c
#define PSP_NET_APCTL_INFO_SUBNETMASK 9
```

### `PSP_NET_APCTL_INFO_GATEWAY`

```c
#define PSP_NET_APCTL_INFO_GATEWAY 10
```

### `PSP_NET_APCTL_INFO_PRIMDNS`

```c
#define PSP_NET_APCTL_INFO_PRIMDNS 11
```

### `PSP_NET_APCTL_INFO_SECDNS`

```c
#define PSP_NET_APCTL_INFO_SECDNS 12
```

### `PSP_NET_APCTL_INFO_USE_PROXY`

```c
#define PSP_NET_APCTL_INFO_USE_PROXY 13
```

### `PSP_NET_APCTL_INFO_PROXY_URL`

```c
#define PSP_NET_APCTL_INFO_PROXY_URL 14
```

### `PSP_NET_APCTL_INFO_PROXY_PORT`

```c
#define PSP_NET_APCTL_INFO_PROXY_PORT 15
```

### `PSP_NET_APCTL_INFO_8021_EAP_TYPE`

```c
#define PSP_NET_APCTL_INFO_8021_EAP_TYPE 16
```

### `PSP_NET_APCTL_INFO_START_BROWSER`

```c
#define PSP_NET_APCTL_INFO_START_BROWSER 17
```

### `PSP_NET_APCTL_INFO_WIFISP`

```c
#define PSP_NET_APCTL_INFO_WIFISP 18
```

### `PSP_NET_APCTL_INFO_SECURITY_TYPE_NONE`

```c
#define PSP_NET_APCTL_INFO_SECURITY_TYPE_NONE 0
```

### `PSP_NET_APCTL_INFO_SECURITY_TYPE_WEP`

```c
#define PSP_NET_APCTL_INFO_SECURITY_TYPE_WEP 1
```

### `PSP_NET_APCTL_INFO_SECURITY_TYPE_WPA`

```c
#define PSP_NET_APCTL_INFO_SECURITY_TYPE_WPA 2
```

## Typedefs

### `SceNetApctlInfo`

```c
typedef union SceNetApctlInfo SceNetApctlInfo;
```

### `sceNetApctlHandler`

```c
typedef void(* sceNetApctlHandler) (int oldState, int newState, int event, int error, void *pArg))(int oldState, int newState, int event, int error, void *pArg);
```

## Functions

### `sceNetApctlInit()`

```c
int sceNetApctlInit(int stackSize, int initPriority);
```

Init the apctl.

**Parameters:**

- `stackSize` – The stack size of the internal thread.
- `initPriority` – The priority of the internal thread.

**Returns:** \< 0 on error.

### `sceNetApctlTerm()`

```c
int sceNetApctlTerm(void);
```

Terminate the apctl.

**Returns:** \< 0 on error.

### `sceNetApctlGetInfo()`

```c
int sceNetApctlGetInfo(int code, SceNetApctlInfo *pInfo);
```

Get the apctl information.

**Parameters:**

- `code` – One of the PSP_NET_APCTL_INFO\_\* defines.
- `pInfo` – Pointer to a [SceNetApctlInfo](#union-scenetapctlinfo).

**Returns:** \< 0 on error.

### `sceNetApctlAddHandler()`

```c
int sceNetApctlAddHandler(sceNetApctlHandler handler, void *pArg);
```

Add an apctl event handler.

**Parameters:**

- `handler` – Pointer to the event handler function.
- `pArg` – Value to be passed to the pArg parameter of the handler function.

**Returns:** A handler id or \< 0 on error.

### `sceNetApctlDelHandler()`

```c
int sceNetApctlDelHandler(int handlerId);
```

Delete an apctl event handler.

**Parameters:**

- `handlerId` – A handler as created returned from sceNetApctlAddHandler.

**Returns:** \< 0 on error.

### `sceNetApctlConnect()`

```c
int sceNetApctlConnect(int connIndex);
```

Connect to an access point.

**Parameters:**

- `connIndex` – The index of the connection.

**Returns:** \< 0 on error.

### `sceNetApctlDisconnect()`

```c
int sceNetApctlDisconnect(void);
```

Disconnect from an access point.

**Returns:** \< 0 on error.

### `sceNetApctlGetState()`

```c
int sceNetApctlGetState(int *pState);
```

Get the state of the access point connection.

**Parameters:**

- `pState` – Pointer to receive the current state (one of the PSP_NET_APCTL_STATE\_\* defines).

**Returns:** \< 0 on error.

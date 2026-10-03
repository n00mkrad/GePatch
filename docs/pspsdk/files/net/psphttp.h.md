[PSPSDK documentation](../../README.md) › Files

# net/psphttp.h

```c
#include <pspkerneltypes.h>
#include <psptypes.h>
```

## Typedefs

### `PspHttpMallocFunction`

```c
typedef void *(* PspHttpMallocFunction) (SceSize size))(SceSize size);
```

### `PspHttpReallocFunction`

```c
typedef void *(* PspHttpReallocFunction) (void *p, SceSize size))(void *p, SceSize size);
```

### `PspHttpFreeFunction`

```c
typedef void(* PspHttpFreeFunction) (void *p))(void *p);
```

### `PspHttpPasswordCB`

```c
typedef int(* PspHttpPasswordCB) (int request, PspHttpAuthType auth_type, const unsigned char *realm, unsigned char *username, unsigned char *password, SceBool need_entity, unsigned char **entity_body, SceSize *entity_size, SceBool *save))(int request, PspHttpAuthType auth_type, const unsigned char *realm, unsigned char *username, unsigned char *password, SceBool need_entity, unsigned char **entity_body, SceSize *entity_size, SceBool *save);
```

## Enumerations

### `enum PspHttpHttpVersion`

| Enumerator | Description |
|---|---|
| `PSP_HTTP_VERSION_1_0` |  |
| `PSP_HTTP_VERSION_1_1` |  |

### `enum PspHttpMethod`

| Enumerator | Description |
|---|---|
| `PSP_HTTP_METHOD_GET` |  |
| `PSP_HTTP_METHOD_POST` |  |
| `PSP_HTTP_METHOD_HEAD` |  |

### `enum PspHttpAuthType`

| Enumerator | Description |
|---|---|
| `PSP_HTTP_AUTH_BASIC` |  |
| `PSP_HTTP_AUTH_DIGEST` |  |

### `enum PspHttpProxyMode`

| Enumerator | Description |
|---|---|
| `PSP_HTTP_PROXY_AUTO` |  |
| `PSP_HTTP_PROXY_MANUAL` |  |

### `enum PspHttpAddHeaderMode`

| Enumerator | Description |
|---|---|
| `PSP_HTTP_HEADER_OVERWRITE` |  |
| `PSP_HTTP_HEADER_ADD` |  |

## Functions

### `sceHttpInit()`

```c
int sceHttpInit(unsigned int unknown1);
```

Init the http library.

**Parameters:**

- `unknown1` – Memory pool size? Pass 20000

**Returns:** 0 on success, \< 0 on error.

### `sceHttpEnd()`

```c
int sceHttpEnd(void);
```

Terminate the http library.

**Returns:** 0 on success, \< 0 on error.

### `sceHttpCreateTemplate()`

```c
int sceHttpCreateTemplate(char *agent, int unknown1, int unknown2);
```

Create a http template.

**Parameters:**

- `agent` – User agent
- `unknown1` – Pass 1
- `unknown2` – Pass 0

**Returns:** A template ID on success, \< 0 on error.

### `sceHttpDeleteTemplate()`

```c
int sceHttpDeleteTemplate(int templateid);
```

Delete a http template.

**Parameters:**

- `templateid` – ID of the template created by sceHttpCreateTemplate

**Returns:** 0 on success, \< 0 on error.

### `sceHttpCreateConnection()`

```c
int sceHttpCreateConnection(int templateid, char *host, char *unknown1, unsigned short port, int unknown2);
```

Create a http connection.

**Parameters:**

- `templateid` – ID of the template created by sceHttpCreateTemplate
- `host` – Host to connect to
- `unknown1` – Pass "http"
- `port` – Port to connect on
- `unknown2` – Pass 0

**Returns:** A connection ID on success, \< 0 on error.

### `sceHttpCreateConnectionWithURL()`

```c
int sceHttpCreateConnectionWithURL(int templateid, const char *url, int unknown1);
```

Create a http connection to a url.

**Parameters:**

- `templateid` – ID of the template created by sceHttpCreateTemplate
- `url` – url to connect to
- `unknown1` – Pass 0

**Returns:** A connection ID on success, \< 0 on error.

### `sceHttpDeleteConnection()`

```c
int sceHttpDeleteConnection(int connectionid);
```

Delete a http connection.

**Parameters:**

- `connectionid` – ID of the connection created by sceHttpCreateConnection or sceHttpCreateConnectionWithURL

**Returns:** 0 on success, \< 0 on error.

### `sceHttpCreateRequest()`

```c
int sceHttpCreateRequest(int connectionid, PspHttpMethod method, char *path, SceULong64 contentlength);
```

Create a http request.

**Parameters:**

- `connectionid` – ID of the connection created by sceHttpCreateConnection or sceHttpCreateConnectionWithURL
- `method` – One of [PspHttpMethod](#enum-psphttpmethod)
- `path` – Path to access
- `contentlength` – Length of the content (POST method only)

**Returns:** A request ID on success, \< 0 on error.

### `sceHttpCreateRequestWithURL()`

```c
int sceHttpCreateRequestWithURL(int connectionid, PspHttpMethod method, char *url, SceULong64 contentlength);
```

Create a http request with url.

**Parameters:**

- `connectionid` – ID of the connection created by sceHttpCreateConnection or sceHttpCreateConnectionWithURL
- `method` – One of [PspHttpMethod](#enum-psphttpmethod)
- `url` – url to access
- `contentlength` – Length of the content (POST method only)

**Returns:** A request ID on success, \< 0 on error.

### `sceHttpDeleteRequest()`

```c
int sceHttpDeleteRequest(int requestid);
```

Delete a http request.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSendRequest()`

```c
int sceHttpSendRequest(int requestid, void *data, unsigned int datasize);
```

Send a http request.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL
- `data` – For POST methods specify a pointer to the post data, otherwise pass NULL
- `datasize` – For POST methods specify the size of the post data, otherwise pass 0

**Returns:** 0 on success, \< 0 on error.

### `sceHttpAbortRequest()`

```c
int sceHttpAbortRequest(int requestid);
```

Abort a http request.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL

**Returns:** 0 on success, \< 0 on error.

### `sceHttpReadData()`

```c
int sceHttpReadData(int requestid, void *data, unsigned int datasize);
```

Read a http request response.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL
- `data` – Buffer for the response data to be stored
- `datasize` – Size of the buffer

**Returns:** The size read into the data buffer, 0 if there is no more data, \< 0 on error.

### `sceHttpGetContentLength()`

```c
int sceHttpGetContentLength(int requestid, SceULong64 *contentlength);
```

Get http request response length.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL
- `contentlength` – The size of the content

**Returns:** 0 on success, \< 0 on error.

### `sceHttpGetStatusCode()`

```c
int sceHttpGetStatusCode(int requestid, int *statuscode);
```

Get http request status code.

**Parameters:**

- `requestid` – ID of the request created by sceHttpCreateRequest or sceHttpCreateRequestWithURL
- `statuscode` – The status code from the host (200 is ok, 404 is not found etc)

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSetResolveTimeOut()`

```c
int sceHttpSetResolveTimeOut(int id, unsigned int timeout);
```

Set resolver timeout.

**Parameters:**

- `id` – ID of the template or connection
- `timeout` – Timeout value in microseconds

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSetResolveRetry()`

```c
int sceHttpSetResolveRetry(int id, int count);
```

Set resolver retry.

**Parameters:**

- `id` – ID of the template or connection
- `count` – Number of retries

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSetConnectTimeOut()`

```c
int sceHttpSetConnectTimeOut(int id, unsigned int timeout);
```

Set connect timeout.

**Parameters:**

- `id` – ID of the template, connection or request
- `timeout` – Timeout value in microseconds

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSetSendTimeOut()`

```c
int sceHttpSetSendTimeOut(int id, unsigned int timeout);
```

Set send timeout.

**Parameters:**

- `id` – ID of the template, connection or request
- `timeout` – Timeout value in microseconds

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSetRecvTimeOut()`

```c
int sceHttpSetRecvTimeOut(int id, unsigned int timeout);
```

Set receive timeout.

**Parameters:**

- `id` – ID of the template or connection
- `timeout` – Timeout value in microseconds

**Returns:** 0 on success, \< 0 on error.

### `sceHttpEnableKeepAlive()`

```c
int sceHttpEnableKeepAlive(int id);
```

Enable keep alive.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpDisableKeepAlive()`

```c
int sceHttpDisableKeepAlive(int id);
```

Disable keep alive.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpEnableRedirect()`

```c
int sceHttpEnableRedirect(int id);
```

Enable redirect.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpDisableRedirect()`

```c
int sceHttpDisableRedirect(int id);
```

Disable redirect.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpEnableCookie()`

```c
int sceHttpEnableCookie(int id);
```

Enable cookie.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpDisableCookie()`

```c
int sceHttpDisableCookie(int id);
```

Disable cookie.

**Parameters:**

- `id` – ID of the template or connection

**Returns:** 0 on success, \< 0 on error.

### `sceHttpSaveSystemCookie()`

```c
int sceHttpSaveSystemCookie(void);
```

Save cookie.

**Returns:** 0 on success, \< 0 on error.

### `sceHttpLoadSystemCookie()`

```c
int sceHttpLoadSystemCookie(void);
```

Load cookie.

**Returns:** 0 on success, \< 0 on error.

### `sceHttpAddExtraHeader()`

```c
int sceHttpAddExtraHeader(int id, char *name, char *value, int unknown1);
```

Add content header.

**Parameters:**

- `id` – ID of the template, connection or request
- `name` – Name of the content
- `value` – Value of the content
- `unknown1` – Pass 0

**Returns:** 0 on success, \< 0 on error.

### `sceHttpDeleteHeader()`

```c
int sceHttpDeleteHeader(int id, const char *name);
```

Delete content header.

**Parameters:**

- `id` – ID of the template, connection or request
- `name` – Name of the content

**Returns:** 0 on success, \< 0 on error.

### `sceHttpsInit()`

```c
int sceHttpsInit(int unknown1, int unknown2, int unknown3, int unknown4);
```

Init the https library.

**Parameters:**

- `unknown1` – Pass 0
- `unknown2` – Pass 0
- `unknown3` – Pass 0
- `unknown4` – Pass 0

**Returns:** 0 on success, \< 0 on error.

### `sceHttpsEnd()`

```c
int sceHttpsEnd(void);
```

Terminate the https library.

**Returns:** 0 on success, \< 0 on error.

### `sceHttpsLoadDefaultCert()`

```c
int sceHttpsLoadDefaultCert(int unknown1, int unknown2);
```

Load default certificate.

**Parameters:**

- `unknown1` – Pass 0
- `unknown2` – Pass 0

**Returns:** 0 on success, \< 0 on error.

### `sceHttpDisableAuth()`

```c
int sceHttpDisableAuth(int id);
```

### `sceHttpDisableCache()`

```c
int sceHttpDisableCache(int id);
```

### `sceHttpEnableAuth()`

```c
int sceHttpEnableAuth(int id);
```

### `sceHttpEnableCache()`

```c
int sceHttpEnableCache(int id);
```

### `sceHttpEndCache()`

```c
int sceHttpEndCache(void);
```

### `sceHttpGetAllHeader()`

```c
int sceHttpGetAllHeader(int request, unsigned char **header, unsigned int *header_size);
```

### `sceHttpGetNetworkErrno()`

```c
int sceHttpGetNetworkErrno(int request, int *err_num);
```

### `sceHttpGetProxy()`

```c
int sceHttpGetProxy(int id, int *activate_flag, int *mode, unsigned char *proxy_host, SceSize len, unsigned short *proxy_port);
```

### `sceHttpInitCache()`

```c
int sceHttpInitCache(SceSize max_size);
```

### `sceHttpSetAuthInfoCB()`

```c
int sceHttpSetAuthInfoCB(int id, PspHttpPasswordCB cbfunc);
```

### `sceHttpSetProxy()`

```c
int sceHttpSetProxy(int id, int activate_flag, int mode, const unsigned char *new_proxy_host, unsigned short new_proxy_port);
```

### `sceHttpSetResHeaderMaxSize()`

```c
int sceHttpSetResHeaderMaxSize(int id, unsigned int header_size);
```

### `sceHttpSetMallocFunction()`

```c
int sceHttpSetMallocFunction(PspHttpMallocFunction malloc_func, PspHttpFreeFunction free_func, PspHttpReallocFunction realloc_func);
```

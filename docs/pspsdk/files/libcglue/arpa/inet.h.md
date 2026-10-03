[PSPSDK documentation](../../../README.md) › Files

# libcglue/arpa/inet.h

```c
#include <netinet/in.h>
```

## Macros

### `inet_addr`

```c
#define inet_addr sceNetInetInetAddr
```

### `inet_aton`

```c
#define inet_aton sceNetInetInetAton
```

### `inet_ntop`

```c
#define inet_ntop sceNetInetInetNtop
```

### `inet_pton`

```c
#define inet_pton sceNetInetInetPton
```

## Functions

### `sceNetInetInetAddr()`

```c
in_addr_t sceNetInetInetAddr(const char *ip);
```

### `sceNetInetInetAton()`

```c
int sceNetInetInetAton(const char *ip, struct in_addr *in);
```

### `sceNetInetInetNtop()`

```c
const char * sceNetInetInetNtop(int af, const void *src, char *dst, socklen_t cnt);
```

### `sceNetInetInetPton()`

```c
int sceNetInetInetPton(int af, const char *src, void *dst);
```

### `inet_ntoa()`

```c
char * inet_ntoa(struct in_addr in);
```

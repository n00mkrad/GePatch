[PSPSDK documentation](../../README.md) › Files

# net/pspnet_inet.h

```c
#include <sys/socket.h>
#include <sys/select.h>
```

## Data Structures

### `struct SceNetInetTimeval`

This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.

```c
struct SceNetInetTimeval {
    uint32_t tv_sec;
    uint32_t tv_usec;
};
```

### `struct SceNetInetPollfd`

```c
struct SceNetInetPollfd {
    int fd;
    short events;
    short revents;
};
```

## Macros

### `SCE_NET_INET_POLLIN`

```c
#define SCE_NET_INET_POLLIN 0x0001
```

### `SCE_NET_INET_POLLPRI`

```c
#define SCE_NET_INET_POLLPRI 0x0002
```

### `SCE_NET_INET_POLLOUT`

```c
#define SCE_NET_INET_POLLOUT 0x0004
```

### `SCE_NET_INET_POLLERR`

```c
#define SCE_NET_INET_POLLERR 0x0008
```

### `SCE_NET_INET_POLLHUP`

```c
#define SCE_NET_INET_POLLHUP 0x0010
```

### `SCE_NET_INET_POLLNVAL`

```c
#define SCE_NET_INET_POLLNVAL 0x0020
```

### `SCE_NET_INET_POLLRDNORM`

```c
#define SCE_NET_INET_POLLRDNORM 0x0040
```

### `SCE_NET_INET_POLLRDBAND`

```c
#define SCE_NET_INET_POLLRDBAND 0x0080
```

### `SCE_NET_INET_POLLWRBAND`

```c
#define SCE_NET_INET_POLLWRBAND 0x0100
```

### `SCE_NET_INET_POLLWRNORM`

```c
#define SCE_NET_INET_POLLWRNORM SCE_NET_INET_POLLOUT
```

## Typedefs

### `SceNetInetTimeval`

```c
typedef struct SceNetInetTimeval SceNetInetTimeval;
```

This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.

### `SceNetInetPollfd`

```c
typedef struct SceNetInetPollfd SceNetInetPollfd;
```

## Functions

### `sceNetInetInit()`

```c
int sceNetInetInit(void);
```

### `sceNetInetSelect()`

```c
int sceNetInetSelect(int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, SceNetInetTimeval *timeout);
```

### `sceNetInetTerm()`

```c
int sceNetInetTerm(void);
```

### `sceNetInetGetErrno()`

```c
int sceNetInetGetErrno(void);
```

### `sceNetInetAccept()`

```c
int sceNetInetAccept(int s, struct sockaddr *addr, socklen_t *addrlen);
```

### `sceNetInetBind()`

```c
int sceNetInetBind(int s, const struct sockaddr *my_addr, socklen_t addrlen);
```

### `sceNetInetConnect()`

```c
int sceNetInetConnect(int s, const struct sockaddr *serv_addr, socklen_t addrlen);
```

### `sceNetInetGetsockopt()`

```c
int sceNetInetGetsockopt(int s, int level, int optname, void *optval, socklen_t *optlen);
```

### `sceNetInetListen()`

```c
int sceNetInetListen(int s, int backlog);
```

### `sceNetInetRecv()`

```c
size_t sceNetInetRecv(int s, void *buf, size_t len, int flags);
```

### `sceNetInetRecvfrom()`

```c
size_t sceNetInetRecvfrom(int s, void *buf, size_t len, int flags, struct sockaddr *from, socklen_t *fromlen);
```

### `sceNetInetSend()`

```c
size_t sceNetInetSend(int s, const void *buf, size_t len, int flags);
```

### `sceNetInetSendto()`

```c
size_t sceNetInetSendto(int s, const void *buf, size_t len, int flags, const struct sockaddr *to, socklen_t tolen);
```

### `sceNetInetSetsockopt()`

```c
int sceNetInetSetsockopt(int s, int level, int optname, const void *optval, socklen_t optlen);
```

### `sceNetInetShutdown()`

```c
int sceNetInetShutdown(int s, int how);
```

### `sceNetInetSocket()`

```c
int sceNetInetSocket(int domain, int type, int protocol);
```

### `sceNetInetClose()`

```c
int sceNetInetClose(int s);
```

### `sceNetInetGetpeername()`

```c
int sceNetInetGetpeername(int s, struct sockaddr *name, socklen_t *namelen);
```

### `sceNetInetGetsockname()`

```c
int sceNetInetGetsockname(int s, struct sockaddr *name, socklen_t *namelen);
```

### `sceNetInetSendmsg()`

```c
ssize_t sceNetInetSendmsg(int s, const struct msghdr *msg, int flags);
```

### `sceNetInetRecvmsg()`

```c
ssize_t sceNetInetRecvmsg(int s, struct msghdr *msg, int flags);
```

### `sceNetInetPoll()`

```c
int sceNetInetPoll(SceNetInetPollfd *fds, size_t nfds, int timeout);
```

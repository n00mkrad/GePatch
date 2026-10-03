[PSPSDK documentation](../../../README.md) › Files

# libcglue/sys/socket.h

```c
#include <stdint.h>
#include <stddef.h>
#include <sys/types.h>
```

## Data Structures

### `struct linger`

```c
struct linger {
    int l_onoff;
    int l_linger;
};
```

### `struct sockaddr`

```c
struct sockaddr {
    uint8_t sa_len;
    sa_family_t sa_family;
    char sa_data[14];
};
```

### `struct sockaddr_storage`

```c
struct sockaddr_storage {
    uint8_t ss_len;
    sa_family_t ss_family;
    char __ss_pad1[((sizeof(int64_t)) - 2)];
    int64_t __ss_align;
    char __ss_pad2[(128 - 2 -((sizeof(int64_t)) - 2) -(sizeof(int64_t)))];
};
```

### `struct iovec`

```c
struct iovec {
    void * iov_base;
    size_t iov_len;
};
```

### `struct msghdr`

```c
struct msghdr {
    void * msg_name;
    socklen_t msg_namelen;
    struct iovec * msg_iov;
    int msg_iovlen;
    void * msg_control;
    socklen_t msg_controllen;
    int msg_flags;
};
```

## Macros

### `SOCK_STREAM`

```c
#define SOCK_STREAM 1		/* stream socket */
```

### `SOCK_DGRAM`

```c
#define SOCK_DGRAM 2		/* datagram socket */
```

### `SOCK_RAW`

```c
#define SOCK_RAW 3		/* raw-protocol interface */
```

### `SOCK_RDM`

```c
#define SOCK_RDM 4		/* reliably-delivered message */
```

### `SOCK_SEQPACKET`

```c
#define SOCK_SEQPACKET 5		/* sequenced packet stream */
```

### `SO_DEBUG`

```c
#define SO_DEBUG 0x0001		/* turn on debugging info recording */
```

### `SO_ACCEPTCONN`

```c
#define SO_ACCEPTCONN 0x0002		/* socket has had listen() */
```

### `SO_REUSEADDR`

```c
#define SO_REUSEADDR 0x0004		/* allow local address reuse */
```

### `SO_KEEPALIVE`

```c
#define SO_KEEPALIVE 0x0008		/* keep connections alive */
```

### `SO_DONTROUTE`

```c
#define SO_DONTROUTE 0x0010		/* just use interface addresses */
```

### `SO_BROADCAST`

```c
#define SO_BROADCAST 0x0020		/* permit sending of broadcast msgs */
```

### `SO_USELOOPBACK`

```c
#define SO_USELOOPBACK 0x0040		/* bypass hardware when possible */
```

### `SO_LINGER`

```c
#define SO_LINGER 0x0080		/* linger on close if data present */
```

### `SO_OOBINLINE`

```c
#define SO_OOBINLINE 0x0100		/* leave received OOB data in line */
```

### `SO_REUSEPORT`

```c
#define SO_REUSEPORT 0x0200		/* allow local address & port reuse */
```

### `SO_TIMESTAMP`

```c
#define SO_TIMESTAMP 0x0400		/* timestamp received dgram traffic */
```

### `SO_SNDBUF`

```c
#define SO_SNDBUF 0x1001		/* send buffer size */
```

### `SO_RCVBUF`

```c
#define SO_RCVBUF 0x1002		/* receive buffer size */
```

### `SO_SNDLOWAT`

```c
#define SO_SNDLOWAT 0x1003		/* send low-water mark */
```

### `SO_RCVLOWAT`

```c
#define SO_RCVLOWAT 0x1004		/* receive low-water mark */
```

### `SO_SNDTIMEO`

```c
#define SO_SNDTIMEO 0x1005		/* send timeout */
```

### `SO_RCVTIMEO`

```c
#define SO_RCVTIMEO 0x1006		/* receive timeout */
```

### `SO_ERROR`

```c
#define SO_ERROR 0x1007		/* get error status and clear */
```

### `SO_TYPE`

```c
#define SO_TYPE 0x1008		/* get socket type */
```

### `SO_OVERFLOWED`

```c
#define SO_OVERFLOWED 0x1009		/* datagrams: return packets dropped */
```

### `SO_NONBLOCK`

```c
#define SO_NONBLOCK 0x1009		/* non-blocking I/O */
```

### `SOL_SOCKET`

```c
#define SOL_SOCKET 0xffff		/* options for socket level */
```

### `AF_UNSPEC`

```c
#define AF_UNSPEC 0		/* unspecified */
```

### `AF_LOCAL`

```c
#define AF_LOCAL 1		/* local to host (pipes, portals) */
```

### `AF_UNIX`

```c
#define AF_UNIX AF_LOCAL	/* backward compatibility */
```

### `AF_INET`

```c
#define AF_INET 2		/* internetwork: UDP, TCP, etc. */
```

### `AF_IMPLINK`

```c
#define AF_IMPLINK 3		/* arpanet imp addresses */
```

### `AF_PUP`

```c
#define AF_PUP 4		/* pup protocols: e.g. BSP */
```

### `AF_CHAOS`

```c
#define AF_CHAOS 5		/* mit CHAOS protocols */
```

### `AF_NS`

```c
#define AF_NS 6		/* XEROX NS protocols */
```

### `AF_ISO`

```c
#define AF_ISO 7		/* ISO protocols */
```

### `AF_OSI`

```c
#define AF_OSI AF_ISO
```

### `AF_ECMA`

```c
#define AF_ECMA 8		/* european computer manufacturers */
```

### `AF_DATAKIT`

```c
#define AF_DATAKIT 9		/* datakit protocols */
```

### `AF_CCITT`

```c
#define AF_CCITT 10		/* CCITT protocols, X.25 etc */
```

### `AF_SNA`

```c
#define AF_SNA 11		/* IBM SNA */
```

### `AF_DECnet`

```c
#define AF_DECnet 12		/* DECnet */
```

### `AF_DLI`

```c
#define AF_DLI 13		/* DEC Direct data link interface */
```

### `AF_LAT`

```c
#define AF_LAT 14		/* LAT */
```

### `AF_HYLINK`

```c
#define AF_HYLINK 15		/* NSC Hyperchannel */
```

### `AF_APPLETALK`

```c
#define AF_APPLETALK 16		/* Apple Talk */
```

### `AF_ROUTE`

```c
#define AF_ROUTE 17		/* Internal Routing Protocol */
```

### `AF_LINK`

```c
#define AF_LINK 18		/* Link layer interface */
```

### `AF_COIP`

```c
#define AF_COIP 20		/* connection-oriented IP, aka ST II */
```

### `AF_CNT`

```c
#define AF_CNT 21		/* Computer Network Technology */
```

### `AF_IPX`

```c
#define AF_IPX 23		/* Novell Internet Protocol */
```

### `AF_INET6`

```c
#define AF_INET6 24		/* IP version 6 */
```

### `AF_ISDN`

```c
#define AF_ISDN 26		/* Integrated Services Digital Network*/
```

### `AF_E164`

```c
#define AF_E164 AF_ISDN		/* CCITT E.164 recommendation */
```

### `AF_NATM`

```c
#define AF_NATM 27		/* native ATM access */
```

### `AF_ARP`

```c
#define AF_ARP 28		/* (rev.) addr. res. prot. (RFC 826) */
```

### `AF_MAX`

```c
#define AF_MAX 31
```

### `_SS_MAXSIZE`

```c
#define _SS_MAXSIZE 128
```

### `_SS_ALIGNSIZE`

```c
#define _SS_ALIGNSIZE (sizeof(int64_t))
```

### `_SS_PAD1SIZE`

```c
#define _SS_PAD1SIZE (_SS_ALIGNSIZE - 2)
```

### `_SS_PAD2SIZE`

```c
#define _SS_PAD2SIZE (_SS_MAXSIZE - 2 - _SS_PAD1SIZE - _SS_ALIGNSIZE)
```

### `PF_UNSPEC`

```c
#define PF_UNSPEC AF_UNSPEC
```

### `PF_LOCAL`

```c
#define PF_LOCAL AF_LOCAL
```

### `PF_UNIX`

```c
#define PF_UNIX PF_LOCAL	/* backward compatibility */
```

### `PF_INET`

```c
#define PF_INET AF_INET
```

### `PF_IMPLINK`

```c
#define PF_IMPLINK AF_IMPLINK
```

### `PF_PUP`

```c
#define PF_PUP AF_PUP
```

### `PF_CHAOS`

```c
#define PF_CHAOS AF_CHAOS
```

### `PF_NS`

```c
#define PF_NS AF_NS
```

### `PF_ISO`

```c
#define PF_ISO AF_ISO
```

### `PF_OSI`

```c
#define PF_OSI AF_ISO
```

### `PF_ECMA`

```c
#define PF_ECMA AF_ECMA
```

### `PF_DATAKIT`

```c
#define PF_DATAKIT AF_DATAKIT
```

### `PF_CCITT`

```c
#define PF_CCITT AF_CCITT
```

### `PF_SNA`

```c
#define PF_SNA AF_SNA
```

### `PF_DECnet`

```c
#define PF_DECnet AF_DECnet
```

### `PF_DLI`

```c
#define PF_DLI AF_DLI
```

### `PF_LAT`

```c
#define PF_LAT AF_LAT
```

### `PF_HYLINK`

```c
#define PF_HYLINK AF_HYLINK
```

### `PF_APPLETALK`

```c
#define PF_APPLETALK AF_APPLETALK
```

### `PF_ROUTE`

```c
#define PF_ROUTE AF_ROUTE
```

### `PF_LINK`

```c
#define PF_LINK AF_LINK
```

### `PF_COIP`

```c
#define PF_COIP AF_COIP
```

### `PF_CNT`

```c
#define PF_CNT AF_CNT
```

### `PF_INET6`

```c
#define PF_INET6 AF_INET6
```

### `PF_IPX`

```c
#define PF_IPX AF_IPX		/* same format as AF_NS */
```

### `PF_ISDN`

```c
#define PF_ISDN AF_ISDN		/* same as E164 */
```

### `PF_E164`

```c
#define PF_E164 AF_E164
```

### `PF_NATM`

```c
#define PF_NATM AF_NATM
```

### `PF_ARP`

```c
#define PF_ARP AF_ARP
```

### `PF_MAX`

```c
#define PF_MAX AF_MAX
```

### `MSG_OOB`

```c
#define MSG_OOB 0x1		/* process out-of-band data */
```

### `MSG_PEEK`

```c
#define MSG_PEEK 0x2		/* peek at incoming message */
```

### `MSG_DONTROUTE`

```c
#define MSG_DONTROUTE 0x4		/* send without using routing tables */
```

### `MSG_EOR`

```c
#define MSG_EOR 0x8		/* data completes record */
```

### `MSG_TRUNC`

```c
#define MSG_TRUNC 0x10		/* data discarded before delivery */
```

### `MSG_CTRUNC`

```c
#define MSG_CTRUNC 0x20		/* control data lost before delivery */
```

### `MSG_WAITALL`

```c
#define MSG_WAITALL 0x40		/* wait for full request or error */
```

### `MSG_DONTWAIT`

```c
#define MSG_DONTWAIT 0x80		/* this message should be nonblocking */
```

### `MSG_BCAST`

```c
#define MSG_BCAST 0x100		/* this message was rcvd using link-level brdcst */
```

### `MSG_MCAST`

```c
#define MSG_MCAST 0x200		/* this message was rcvd using link-level mcast */
```

### `SHUT_RD`

```c
#define SHUT_RD 0		/* Disallow further receives. */
```

### `SHUT_WR`

```c
#define SHUT_WR 1		/* Disallow further sends. */
```

### `SHUT_RDWR`

```c
#define SHUT_RDWR 2		/* Disallow further sends/receives. */
```

### `SOMAXCONN`

```c
#define SOMAXCONN 128
```

## Typedefs

### `sa_family_t`

```c
typedef uint8_t sa_family_t;
```

### `socklen_t`

```c
typedef uint32_t socklen_t;
```

## Functions

### `accept()`

```c
int accept(int, struct sockaddr *__restrict, socklen_t *__restrict);
```

### `bind()`

```c
int bind(int, const struct sockaddr *, socklen_t);
```

### `connect()`

```c
int connect(int, const struct sockaddr *, socklen_t);
```

### `getpeername()`

```c
int getpeername(int, struct sockaddr *__restrict, socklen_t *__restrict);
```

### `getsockname()`

```c
int getsockname(int, struct sockaddr *__restrict, socklen_t *__restrict);
```

### `getsockopt()`

```c
int getsockopt(int, int, int, void *__restrict, socklen_t *__restrict);
```

### `listen()`

```c
int listen(int, int);
```

### `recv()`

```c
ssize_t recv(int, void *, size_t, int);
```

### `recvfrom()`

```c
ssize_t recvfrom(int, void *__restrict, size_t, int, struct sockaddr *__restrict, socklen_t *__restrict);
```

### `recvmsg()`

```c
ssize_t recvmsg(int s, struct msghdr *msg, int flags);
```

### `send()`

```c
ssize_t send(int, const void *, size_t, int);
```

### `sendto()`

```c
ssize_t sendto(int, const void *, size_t, int, const struct sockaddr *, socklen_t);
```

### `sendmsg()`

```c
ssize_t sendmsg(int s, const struct msghdr *msg, int flags);
```

### `setsockopt()`

```c
int setsockopt(int, int, int, const void *, socklen_t);
```

### `shutdown()`

```c
int shutdown(int, int);
```

### `socket()`

```c
int socket(int, int, int);
```

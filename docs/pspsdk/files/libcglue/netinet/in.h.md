[PSPSDK documentation](../../../README.md) › Files

# libcglue/netinet/in.h

```c
#include <sys/socket.h>
```

## Data Structures

### `struct in_addr`

```c
struct in_addr {
    in_addr_t s_addr;
};
```

### `struct sockaddr_in`

```c
struct sockaddr_in {
    uint8_t sin_len;
    sa_family_t sin_family;
    in_port_t sin_port;
    struct in_addr sin_addr;
    int8_t sin_zero[8];
};
```

### `struct ip_opts`

```c
struct ip_opts {
    struct in_addr ip_dst;
    int8_t ip_opts[40];
};
```

### `struct ip_mreq`

```c
struct ip_mreq {
    struct in_addr imr_multiaddr;
    struct in_addr imr_interface;
};
```

## Macros

### `IPPROTO_IP`

```c
#define IPPROTO_IP 0		/* dummy for IP */
```

### `IPPROTO_HOPOPTS`

```c
#define IPPROTO_HOPOPTS 0		/* IP6 hop-by-hop options */
```

### `IPPROTO_ICMP`

```c
#define IPPROTO_ICMP 1		/* control message protocol */
```

### `IPPROTO_IGMP`

```c
#define IPPROTO_IGMP 2		/* group mgmt protocol */
```

### `IPPROTO_GGP`

```c
#define IPPROTO_GGP 3		/* gateway^2 (deprecated) */
```

### `IPPROTO_IPV4`

```c
#define IPPROTO_IPV4 4 		/* IP header */
```

### `IPPROTO_IPIP`

```c
#define IPPROTO_IPIP 4		/* IP inside IP */
```

### `IPPROTO_TCP`

```c
#define IPPROTO_TCP 6		/* tcp */
```

### `IPPROTO_EGP`

```c
#define IPPROTO_EGP 8		/* exterior gateway protocol */
```

### `IPPROTO_PUP`

```c
#define IPPROTO_PUP 12		/* pup */
```

### `IPPROTO_UDP`

```c
#define IPPROTO_UDP 17		/* user datagram protocol */
```

### `IPPROTO_IDP`

```c
#define IPPROTO_IDP 22		/* xns idp */
```

### `IPPROTO_TP`

```c
#define IPPROTO_TP 29 		/* tp-4 w/ class negotiation */
```

### `IPPROTO_IPV6`

```c
#define IPPROTO_IPV6 41		/* IP6 header */
```

### `IPPROTO_ROUTING`

```c
#define IPPROTO_ROUTING 43		/* IP6 routing header */
```

### `IPPROTO_FRAGMENT`

```c
#define IPPROTO_FRAGMENT 44		/* IP6 fragmentation header */
```

### `IPPROTO_RSVP`

```c
#define IPPROTO_RSVP 46		/* resource reservation */
```

### `IPPROTO_GRE`

```c
#define IPPROTO_GRE 47		/* GRE encaps RFC 1701 */
```

### `IPPROTO_ESP`

```c
#define IPPROTO_ESP 50 		/* encap. security payload */
```

### `IPPROTO_AH`

```c
#define IPPROTO_AH 51 		/* authentication header */
```

### `IPPROTO_MOBILE`

```c
#define IPPROTO_MOBILE 55		/* IP Mobility RFC 2004 */
```

### `IPPROTO_IPV6_ICMP`

```c
#define IPPROTO_IPV6_ICMP 58		/* IPv6 ICMP */
```

### `IPPROTO_ICMPV6`

```c
#define IPPROTO_ICMPV6 58		/* ICMP6 */
```

### `IPPROTO_NONE`

```c
#define IPPROTO_NONE 59		/* IP6 no next header */
```

### `IPPROTO_DSTOPTS`

```c
#define IPPROTO_DSTOPTS 60		/* IP6 destination option */
```

### `IPPROTO_EON`

```c
#define IPPROTO_EON 80		/* ISO cnlp */
```

### `IPPROTO_ETHERIP`

```c
#define IPPROTO_ETHERIP 97		/* Ethernet-in-IP */
```

### `IPPROTO_ENCAP`

```c
#define IPPROTO_ENCAP 98		/* encapsulation header */
```

### `IPPROTO_PIM`

```c
#define IPPROTO_PIM 103		/* Protocol indep. multicast */
```

### `IPPROTO_IPCOMP`

```c
#define IPPROTO_IPCOMP 108		/* IP Payload Comp. Protocol */
```

### `IPPROTO_VRRP`

```c
#define IPPROTO_VRRP 112		/* VRRP RFC 2338 */
```

### `IPPROTO_RAW`

```c
#define IPPROTO_RAW 255		/* raw IP packet */
```

### `IPPROTO_MAX`

```c
#define IPPROTO_MAX 256
```

### `IPPROTO_DONE`

```c
#define IPPROTO_DONE 257
```

### `CTL_IPPROTO_IPSEC`

```c
#define CTL_IPPROTO_IPSEC 258
```

### `IPPORT_RESERVED`

```c
#define IPPORT_RESERVED 1024
```

### `IPPORT_ANONMIN`

```c
#define IPPORT_ANONMIN 49152
```

### `IPPORT_ANONMAX`

```c
#define IPPORT_ANONMAX 65535
```

### `IPPORT_RESERVEDMIN`

```c
#define IPPORT_RESERVEDMIN 600
```

### `IPPORT_RESERVEDMAX`

```c
#define IPPORT_RESERVEDMAX (IPPORT_RESERVED-1)
```

### `__IPADDR()`

```c
#define __IPADDR(x) ((uint32_t)(x))
```

### `IN_CLASSA()`

```c
#define IN_CLASSA(i) (((uint32_t)(i) & __IPADDR(0x80000000)) == \
				 __IPADDR(0x00000000))
```

### `IN_CLASSA_NET`

```c
#define IN_CLASSA_NET __IPADDR(0xff000000)
```

### `IN_CLASSA_NSHIFT`

```c
#define IN_CLASSA_NSHIFT 24
```

### `IN_CLASSA_HOST`

```c
#define IN_CLASSA_HOST __IPADDR(0x00ffffff)
```

### `IN_CLASSA_MAX`

```c
#define IN_CLASSA_MAX 128
```

### `IN_CLASSB()`

```c
#define IN_CLASSB(i) (((uint32_t)(i) & __IPADDR(0xc0000000)) == \
				 __IPADDR(0x80000000))
```

### `IN_CLASSB_NET`

```c
#define IN_CLASSB_NET __IPADDR(0xffff0000)
```

### `IN_CLASSB_NSHIFT`

```c
#define IN_CLASSB_NSHIFT 16
```

### `IN_CLASSB_HOST`

```c
#define IN_CLASSB_HOST __IPADDR(0x0000ffff)
```

### `IN_CLASSB_MAX`

```c
#define IN_CLASSB_MAX 65536
```

### `IN_CLASSC()`

```c
#define IN_CLASSC(i) (((uint32_t)(i) & __IPADDR(0xe0000000)) == \
				 __IPADDR(0xc0000000))
```

### `IN_CLASSC_NET`

```c
#define IN_CLASSC_NET __IPADDR(0xffffff00)
```

### `IN_CLASSC_NSHIFT`

```c
#define IN_CLASSC_NSHIFT 8
```

### `IN_CLASSC_HOST`

```c
#define IN_CLASSC_HOST __IPADDR(0x000000ff)
```

### `IN_CLASSD()`

```c
#define IN_CLASSD(i) (((uint32_t)(i) & __IPADDR(0xf0000000)) == \
				 __IPADDR(0xe0000000))
```

### `IN_CLASSD_NET`

```c
#define IN_CLASSD_NET __IPADDR(0xf0000000)
```

### `IN_CLASSD_NSHIFT`

```c
#define IN_CLASSD_NSHIFT 28
```

### `IN_CLASSD_HOST`

```c
#define IN_CLASSD_HOST __IPADDR(0x0fffffff)
```

### `IN_MULTICAST()`

```c
#define IN_MULTICAST(i) IN_CLASSD(i)
```

### `IN_EXPERIMENTAL()`

```c
#define IN_EXPERIMENTAL(i) (((uint32_t)(i) & __IPADDR(0xf0000000)) == \
				 __IPADDR(0xf0000000))
```

### `IN_BADCLASS()`

```c
#define IN_BADCLASS(i) (((uint32_t)(i) & __IPADDR(0xf0000000)) == \
				 __IPADDR(0xf0000000))
```

### `IN_LOCAL_GROUP()`

```c
#define IN_LOCAL_GROUP(i) (((uint32_t)(i) & __IPADDR(0xffffff00)) == \
				 __IPADDR(0xe0000000))
```

### `INADDR_ANY`

```c
#define INADDR_ANY __IPADDR(0x00000000)
```

### `INADDR_LOOPBACK`

```c
#define INADDR_LOOPBACK __IPADDR(0x7f000001)
```

### `INADDR_BROADCAST`

```c
#define INADDR_BROADCAST __IPADDR(0xffffffff)	/* must be masked */
```

### `INADDR_UNSPEC_GROUP`

```c
#define INADDR_UNSPEC_GROUP __IPADDR(0xe0000000)	/* 224.0.0.0 */
```

### `INADDR_ALLHOSTS_GROUP`

```c
#define INADDR_ALLHOSTS_GROUP __IPADDR(0xe0000001)	/* 224.0.0.1 */
```

### `INADDR_ALLRTRS_GROUP`

```c
#define INADDR_ALLRTRS_GROUP __IPADDR(0xe0000002)	/* 224.0.0.2 */
```

### `INADDR_MAX_LOCAL_GROUP`

```c
#define INADDR_MAX_LOCAL_GROUP __IPADDR(0xe00000ff)	/* 224.0.0.255 */
```

### `IN_LOOPBACKNET`

```c
#define IN_LOOPBACKNET 127			/* official! */
```

### `INET_ADDRSTRLEN`

```c
#define INET_ADDRSTRLEN 16
```

### `IP_OPTIONS`

```c
#define IP_OPTIONS 1    /* buf/ip_opts; set/get IP options */
```

### `IP_HDRINCL`

```c
#define IP_HDRINCL 2    /* int; header is included with data */
```

### `IP_TOS`

```c
#define IP_TOS 3    /* int; IP type of service and preced. */
```

### `IP_TTL`

```c
#define IP_TTL 4    /* int; IP time to live */
```

### `IP_RECVOPTS`

```c
#define IP_RECVOPTS 5    /* bool; receive all IP opts w/dgram */
```

### `IP_RECVRETOPTS`

```c
#define IP_RECVRETOPTS 6    /* bool; receive IP opts for response */
```

### `IP_RECVDSTADDR`

```c
#define IP_RECVDSTADDR 7    /* bool; receive IP dst addr w/dgram */
```

### `IP_RETOPTS`

```c
#define IP_RETOPTS 8    /* ip_opts; set/get IP options */
```

### `IP_MULTICAST_IF`

```c
#define IP_MULTICAST_IF 9    /* in_addr; set/get IP multicast i/f  */
```

### `IP_MULTICAST_TTL`

```c
#define IP_MULTICAST_TTL 10   /* u_char; set/get IP multicast ttl */
```

### `IP_MULTICAST_LOOP`

```c
#define IP_MULTICAST_LOOP 11   /* u_char; set/get IP multicast loopback */
```

### `IP_ADD_MEMBERSHIP`

```c
#define IP_ADD_MEMBERSHIP 12   /* ip_mreq; add an IP group membership */
```

### `IP_DROP_MEMBERSHIP`

```c
#define IP_DROP_MEMBERSHIP 13   /* ip_mreq; drop an IP group membership */
```

### `IP_PORTRANGE`

```c
#define IP_PORTRANGE 19   /* int; range to use for ephemeral port */
```

### `IP_RECVIF`

```c
#define IP_RECVIF 20   /* bool; receive reception if w/dgram */
```

### `IP_ERRORMTU`

```c
#define IP_ERRORMTU 21   /* int; get MTU of last xmit = EMSGSIZE */
```

### `IP_IPSEC_POLICY`

```c
#define IP_IPSEC_POLICY 22 /* struct; get/set security policy */
```

### `IP_DEFAULT_MULTICAST_TTL`

```c
#define IP_DEFAULT_MULTICAST_TTL 1	/* normally limit m'casts to 1 hop  */
```

### `IP_DEFAULT_MULTICAST_LOOP`

```c
#define IP_DEFAULT_MULTICAST_LOOP 1	/* normally hear sends if a member  */
```

### `IP_MAX_MEMBERSHIPS`

```c
#define IP_MAX_MEMBERSHIPS 20	/* per socket; must fit in one mbuf */
```

### `IP_PORTRANGE_DEFAULT`

```c
#define IP_PORTRANGE_DEFAULT 0	/* default range */
```

### `IP_PORTRANGE_HIGH`

```c
#define IP_PORTRANGE_HIGH 1	/* same as DEFAULT (FreeBSD compat) */
```

### `IP_PORTRANGE_LOW`

```c
#define IP_PORTRANGE_LOW 2	/* use privileged range */
```

### `ntohs()`

```c
#define ntohs(x) __builtin_bswap16(x)
```

### `ntohl()`

```c
#define ntohl(x) __builtin_bswap32(x)
```

### `htons()`

```c
#define htons(x) __builtin_bswap16(x)
```

### `htonl()`

```c
#define htonl(x) __builtin_bswap32(x)
```

## Typedefs

### `in_addr_t`

```c
typedef uint32_t in_addr_t;
```

### `in_port_t`

```c
typedef uint16_t in_port_t;
```

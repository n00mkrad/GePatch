[PSPSDK documentation](../../README.md) › Files

# libcglue/netdb.h

## Data Structures

### `struct hostent`

```c
struct hostent {
    char * h_name;
    char ** h_aliases;
    int h_addrtype;
    int h_length;
    char ** h_addr_list;
    char * h_addr;
};
```

## Macros

### `NETDB_INTERNAL`

```c
#define NETDB_INTERNAL -1	/* see errno */
```

### `NETDB_SUCCESS`

```c
#define NETDB_SUCCESS 0	/* no problem */
```

### `HOST_NOT_FOUND`

```c
#define HOST_NOT_FOUND 1 /* Authoritative Answer Host not found */
```

### `TRY_AGAIN`

```c
#define TRY_AGAIN 2 /* Non-Authoritative Host not found, or SERVERFAIL */
```

### `NO_RECOVERY`

```c
#define NO_RECOVERY 3 /* Non recoverable errors, FORMERR, REFUSED, NOTIMP */
```

### `NO_DATA`

```c
#define NO_DATA 4 /* Valid name, no data record of requested type */
```

### `NO_ADDRESS`

```c
#define NO_ADDRESS NO_DATA		/* no address, look for MX record */
```

## Functions

### `gethostbyaddr()`

```c
struct hostent * gethostbyaddr(const void *addr, int len, int type);
```

### `gethostbyname()`

```c
struct hostent * gethostbyname(const char *name);
```

## Variables

### `h_errno`

```c
int h_errno;
```

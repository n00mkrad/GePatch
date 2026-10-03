[PSPSDK documentation](../../README.md) › Files

# libcglue/select.c

```c
#include <fcntl.h>
#include <errno.h>
#include <sys/select.h>
#include <psptypes.h>
#include <pspthreadman.h>
#include <pspnet_inet.h>
#include "fdman.h"
```

## Macros

### `SELECT_POLLING_DELAY_IN_us`

```c
#define SELECT_POLLING_DELAY_IN_us 100
```

### `SCE_FD_SET()`

```c
#define SCE_FD_SET(n, p) ((p)->fds_bits[((n) & 0xFF) /_NFDBITS] |= (1 << ((n) % _NFDBITS)))
```

[PSPSDK documentation](../../README.md) › Files

# libcglue/fdman.c

```c
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <pspstdio.h>
#include <psptypes.h>
#include <pspsdk.h>
#include "fdman.h"
```

## Variables

### `__fdman_mutex`

```c
SceLwMutexWorkarea __fdman_mutex;
```

### `__descriptor_data_pool`

```c
__descriptormap_type __descriptor_data_pool[1024][1024];
```

### `__descriptormap`

```c
__descriptormap_type* __descriptormap[1024][1024];
```

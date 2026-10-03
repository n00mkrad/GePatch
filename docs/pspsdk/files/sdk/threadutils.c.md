[PSPSDK documentation](../../README.md) › Files

# sdk/threadutils.c

```c
#include <string.h>
#include "pspthreadman.h"
#include "pspsdk.h"
#include "psptypes.h"
```

## Data Structures

### `struct _ThreadInfoSkel`

```c
struct _ThreadInfoSkel {
    SceSize size;
    char name[32];
};
```

## Macros

### `MAX_UIDS`

```c
#define MAX_UIDS 256
```

## Typedefs

### `ReferFunc`

```c
typedef int(* ReferFunc) (SceUID, struct _ThreadInfoSkel *))(SceUID, struct _ThreadInfoSkel *);
```

## Functions

### `_pspSdkReferInternal()`

```c
static int _pspSdkReferInternal(const char *name, enum SceKernelIdListType type, struct _ThreadInfoSkel *pInfo, int size, ReferFunc pRefer);
```

**Also defined in this file** (documented with the declaration):

- [`pspSdkReferSemaStatusByName`](pspsdk.h.md#pspsdkrefersemastatusbyname)
- [`pspSdkReferEventFlagStatusByName`](pspsdk.h.md#pspsdkrefereventflagstatusbyname)
- [`pspSdkReferThreadStatusByName`](pspsdk.h.md#pspsdkreferthreadstatusbyname)
- [`pspSdkReferMboxStatusByName`](pspsdk.h.md#pspsdkrefermboxstatusbyname)
- [`pspSdkReferVplStatusByName`](pspsdk.h.md#pspsdkrefervplstatusbyname)
- [`pspSdkReferFplStatusByName`](pspsdk.h.md#pspsdkreferfplstatusbyname)
- [`pspSdkReferMppStatusByName`](pspsdk.h.md#pspsdkrefermppstatusbyname)
- [`pspSdkReferCallbackStatusByName`](pspsdk.h.md#pspsdkrefercallbackstatusbyname)
- [`pspSdkReferVTimerStatusByName`](pspsdk.h.md#pspsdkrefervtimerstatusbyname)
- [`pspSdkReferThreadEventHandlerStatusByName`](pspsdk.h.md#pspsdkreferthreadeventhandlerstatusbyname)

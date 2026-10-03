[PSPSDK documentation](../../README.md) › Files

# libpthreadglue/osal.c

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pspkerror.h>
#include <pspthreadman.h>
#include <pspsdk.h>
#include <sys/pte_generic_osal.h>
```

## Data Structures

### `struct pspThreadData`

```c
struct pspThreadData {
    pte_osThreadEntryPoint entryPoint;
    void * argv;
    SceUID cancelSem;
};
```

## Macros

### `MAX_PSP_UID`

```c
#define MAX_PSP_UID 2048
```

### `DEFAULT_STACK_SIZE_BYTES`

```c
#define DEFAULT_STACK_SIZE_BYTES 4096
```

### `PSP_MAX_TLS`

```c
#define PSP_MAX_TLS 32
```

### `PSP_DEBUG()`

```c
#define PSP_DEBUG(x)
```

### `POLLING_DELAY_IN_us`

```c
#define POLLING_DELAY_IN_us 100
```

## Typedefs

### `pte_osThreadHandle`

```c
typedef int pte_osThreadHandle;
```

### `pte_osSemaphoreHandle`

```c
typedef int pte_osSemaphoreHandle;
```

### `pte_osMutexHandle`

```c
typedef int pte_osMutexHandle;
```

### `pspThreadData`

```c
typedef struct pspThreadData pspThreadData;
```

## Functions

### `pteTlsGlobalInit()`

```c
pte_osResult pteTlsGlobalInit(int maxEntries);
```

### `pteTlsThreadInit()`

```c
void * pteTlsThreadInit(void);
```

### `__pteTlsAlloc()`

```c
pte_osResult __pteTlsAlloc(unsigned int *pKey);
```

### `pteTlsGetValue()`

```c
void * pteTlsGetValue(void *pTlsThreadStruct, unsigned int index);
```

### `__pteTlsSetValue()`

```c
pte_osResult __pteTlsSetValue(void *pTlsThreadStruct, unsigned int index, void *value);
```

### `__getTlsStructFromThread()`

```c
void * __getTlsStructFromThread(SceUID thid);
```

### `pteTlsFree()`

```c
pte_osResult pteTlsFree(unsigned int index);
```

### `pteTlsThreadDestroy()`

```c
void pteTlsThreadDestroy(void *pTlsThreadStruct);
```

### `pteTlsGlobalDestroy()`

```c
void pteTlsGlobalDestroy(void);
```

### `__getThreadData()`

```c
pspThreadData * __getThreadData(SceUID threadHandle);
```

### `__pspStubThreadEntry()`

```c
int __pspStubThreadEntry(unsigned int argc, void *argv);
```

### `invert_priority()`

```c
static int invert_priority(int priority);
```

## Variables

### `__threadDataKey`

```c
unsigned int __threadDataKey;
```

### `__globalTls`

```c
void* __globalTls;
```

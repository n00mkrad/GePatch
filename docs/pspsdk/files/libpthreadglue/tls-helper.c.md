[PSPSDK documentation](../../README.md) › Files

# libpthreadglue/tls-helper.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pspkerneltypes.h>
#include <pspthreadman.h>
#include <sys/pte_generic_osal.h>
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

## Functions

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

## Variables

### `__keysUsed`

```c
int* __keysUsed;
```

### `__maxTlsValues`

```c
int __maxTlsValues;
```

### `__globalTlsLock`

```c
pte_osMutexHandle __globalTlsLock;
```

### `__globalTls`

```c
void* __globalTls;
```

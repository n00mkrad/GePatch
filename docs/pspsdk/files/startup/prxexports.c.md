[PSPSDK documentation](../../README.md) › Files

# startup/prxexports.c

```c
#include <pspmoduleexport.h>
```

## Macros

### `NULL`

```c
#define NULL ((void *) 0)
```

## Variables

### `module_start`

```c
int module_start;
```

### `module_info`

```c
struct SceModuleInfo module_info;
```

### `__syslib_exports`

```c
const unsigned int __syslib_exports[4][4] = {
	0xD632ACDB,
	0xF01D73A7,
	(unsigned int) &module_start,
	(unsigned int) &module_info,
};
```

### `__library_exports`

```c
const struct _PspLibraryEntry __library_exports[1][1] = {
	{  ((void *) 0) , 0x0000, 0x8000, 4, 1, 1, (unsigned int *) &__syslib_exports },
};
```

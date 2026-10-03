[PSPSDK documentation](../../README.md) › Files

# startup/crt0.c

```c
#include <stdlib.h>
#include <string.h>
#include <pspkerneltypes.h>
#include <psptypes.h>
#include <pspmoduleinfo.h>
#include <pspthreadman.h>
#include <psploadexec.h>
#include <pspmodulemgr.h>
```

## Data Structures

### `struct _library_entry`

```c
struct _library_entry {
    const char * name;
    unsigned short version;
    unsigned short attribute;
    unsigned char entLen;
    unsigned char varCount;
    unsigned short funcCount;
    void * entrytable;
};
```

## Macros

### `ARG_MAX`

```c
#define ARG_MAX 19
```

### `DEFAULT_THREAD_PRIORITY`

```c
#define DEFAULT_THREAD_PRIORITY 32
```

### `DEFAULT_THREAD_ATTRIBUTE`

```c
#define DEFAULT_THREAD_ATTRIBUTE PSP_THREAD_ATTR_USER
```

### `DEFAULT_THREAD_STACK_KB_SIZE`

```c
#define DEFAULT_THREAD_STACK_KB_SIZE 256
```

### `DEFAULT_MAIN_THREAD_NAME`

```c
#define DEFAULT_MAIN_THREAD_NAME "user_main"
```

## Functions

### `__libcglue_init()`

```c
void __libcglue_init(int argc, char *argv[]);
```

### `__libcglue_deinit()`

```c
void __libcglue_deinit();
```

### `_init()`

```c
void _init(void);
```

### `_fini()`

```c
void _fini(void);
```

### `main()`

```c
int main(int argc, char *argv[]);
```

### `_main()`

```c
void _main(SceSize args, void *argp);
```

Main program thread.

Initializes runtime parameters and calls the program's [main()](../debug/callstack.c.md#main).

**Parameters:**

- `args` – Size (in bytes) of the argp parameter.
- `argp` – Pointer to program arguments. Each argument is a NUL-terminated string.

### `_exit()`

```c
void _exit(int status);
```

### `_start()`

```c
int _start(SceSize args, void *argp);
```

Startup thread.

Creates the main program thread based on variables defined by the program.

**Parameters:**

- `args` – Size (in bytes) of arguments passed to the program by the kernel.
- `argp` – Pointer to arguments passed by the kernel.

## Variables

### `sce_newlib_nocreate_thread_in_start`

```c
int sce_newlib_nocreate_thread_in_start;
```

### `sce_newlib_priority`

```c
unsigned int sce_newlib_priority;
```

### `sce_newlib_attribute`

```c
unsigned int sce_newlib_attribute;
```

### `sce_newlib_stack_kb_size`

```c
unsigned int sce_newlib_stack_kb_size;
```

### `sce_newlib_main_thread_name`

```c
const char* sce_newlib_main_thread_name;
```

### `module_info`

```c
SceModuleInfo module_info;
```

### `__entrytable`

```c
const unsigned int __entrytable[4][4] = {
	0xD632ACDB, 0xF01D73A7, (unsigned int) &_start, (unsigned int) &module_info
};
```

### `_library_entry`

```c
const struct _library_entry _library_entry = {
	NULL, 0, 0x8000, 4, 1, 1, (unsigned int *) &__entrytable
};
```

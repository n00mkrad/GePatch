[PSPSDK documentation](../../README.md) › Files

# prof/prof.c

```c
#include <stdlib.h>
#include <malloc.h>
#include <stdio.h>
#include <string.h>
#include <pspprof.h>
#include <pspthreadman.h>
```

## Data Structures

### `struct gmonhdr`

gmon.out file header

```c
struct gmonhdr {
    int lpc;
    int hpc;
    int ncnt;
    int version;
    int profrate;
    int resv[3];
};
```

### `struct rawarc`

frompc -> selfpc graph

```c
struct rawarc {
    unsigned int frompc;
    unsigned int selfpc;
    unsigned int count;
};
```

### `struct gmonparam`

context

```c
struct gmonparam {
    int state;
    unsigned int lowpc;
    unsigned int highpc;
    unsigned int lowpc_link;
    unsigned int highpc_link;
    unsigned int textsize;
    unsigned int hashfraction;
    int narcs;
    struct rawarc * arcs;
    int nsamples;
    unsigned int * samples;
    int timer;
    unsigned int pc;
};
```

## Macros

### `GMON_PROF_ON`

```c
#define GMON_PROF_ON 0
```

### `GMON_PROF_BUSY`

```c
#define GMON_PROF_BUSY 1
```

### `GMON_PROF_ERROR`

```c
#define GMON_PROF_ERROR 2
```

### `GMON_PROF_OFF`

```c
#define GMON_PROF_OFF 3
```

### `GMONVERSION`

```c
#define GMONVERSION 0x00051879
```

### `HISTFRACTION`

```c
#define HISTFRACTION 4
```

one histogram per four bytes of text space

### `SAMPLE_FREQ`

```c
#define SAMPLE_FREQ 1000
```

define sample frequency - 1000 hz = 1ms

## Functions

### `__gprof_cleanup()`

```c
void __gprof_cleanup();
```

Writes gmon.out dump file and stops profiling Called from atexit() handler; will dump out a gmon.out file at cwd with all collected information.

### `__mcount()`

```c
void __mcount(unsigned int frompc, unsigned int selfpc);
```

Internal C handler for \_mcount()

**Parameters:**

- `frompc` – pc address of caller
- `selfpc` – pc address of current function

Called from mcount.S to make life a bit easier. \_\_mcount is called right before a function starts. GCC generates a tiny stub at the very beginning of each compiled routine, which eventually brings the control to here.

### `timer_handler()`

```c
static SceUInt timer_handler(SceUID uid, SceKernelSysClock *requested, SceKernelSysClock *actual, void *common);
```

Internal timer handler.

### `initialize()`

```c
static void initialize();
```

Initializes pg library.

After calculating the text size, initialize() allocates enough memory to allow fastest access to arc structures, and some more for sampling statistics. Note that this also installs a timer that runs at 1000 hert.

### `gprof_start()`

```c
void gprof_start(void);
```

Start the profiler.

If the profiler is already running, this function stop previous one, and ignore the result. Finally, it initializes a new profiler session.

### `gprof_stop()`

```c
void gprof_stop(const char *filename, int should_dump);
```

Stop the profiler.

If the profiler is not running, this function does nothing.

**Parameters:**

- `filename` – The name of the file to write the profiling data to.
- `should_dump` – If 1, the profiling data will be written to the file. If 0, the profiling data will be discarded.

## Variables

### `gp`

```c
struct gmonparam gp;
```

holds context statistics

### `initialized`

```c
int initialized = 0;
```

have we allocated memory and registered already

### `_ftext`

```c
int _ftext;
```

defined by linker

### `_etext`

```c
int _etext;
```

### `_start`

```c
int _start;
```

\_start is the entry point defined in both [crt0.c](../startup/crt0.c.md) and [crt0_prx.c](../startup/crt0_prx.c.md)

### `module_start`

```c
int module_start;
```

module_start is only defined in PRX startup code ([crt0_prx.c](../startup/crt0_prx.c.md)) as an alias for \_start Using weak reference allows us to detect PRX vs PBP at runtime We also verify module_start == \_start to handle the case where a PBP defines its own module_start

### `reloc_offset`

```c
unsigned int reloc_offset;
```

relocation offset: runtime_address - link_address (for PRX)

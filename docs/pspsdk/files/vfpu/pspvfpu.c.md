[PSPSDK documentation](../../README.md) › Files

# vfpu/pspvfpu.c

```c
#include <malloc.h>
#include <string.h>
#include "pspthreadman.h"
#include "pspvfpu.h"
```

## Data Structures

### `struct pspvfpu_context`

```c
struct pspvfpu_context {
    float fpregs[4 *4 *8];
    vfpumatrixset_t valid;
    vfpumatrixset_t owned;
};
```

## Macros

### `NMAT`

```c
#define NMAT 8
```

### `SV()`

```c
#define SV(N) asm("sv.q	c"#N"00,  0 + %0, wt\n" \
	    "sv.q	c"#N"10, 16 + %0, wt\n" \
	    "sv.q	c"#N"20, 32 + %0, wt\n" \
	    "sv.q	c"#N"30, 48 + %0, wt\n" \
	    : "=m" (c->fpregs[N * 4*4]) \
	    : : "memory")
```

### `LV()`

```c
#define LV(N) asm("lv.q	c"#N"00,  0 + %0\n" \
	    "lv.q	c"#N"10, 16 + %0\n" \
	    "lv.q	c"#N"20, 32 + %0\n" \
	    "lv.q	c"#N"30, 48 + %0\n" \
	    : : "m" (c->fpregs[N * 4*4]) \
	    : "memory")
```

## Functions

### `save_matrix()`

```c
static void save_matrix(struct pspvfpu_context *c, int mat);
```

### `load_matrix()`

```c
static void load_matrix(const struct pspvfpu_context *c, int mat);
```

### `pspvfpu_use_matrices()`

```c
void pspvfpu_use_matrices(struct pspvfpu_context *c, vfpumatrixset_t keepset, vfpumatrixset_t tempset);
```

Use a set of VFPU matrices.

This restores the parts of the VFPU state the caller wants restored (if necessary). If the caller was the previous user of the the matrix set, then this call is effectively a no-op. If a matrix has never been used by this context before, then it will initially have an undefined value.

**Parameters:**

- `context` – The VFPU context the caller wants to restore from. It is valid to pass NULL as a context. This means the caller wants to reserve a temporary matrix without affecting other VFPU users, but doesn't want any long-term matrices itself.
- `keepset` – The set of matrices the caller wants to use, and keep the values persistently.<br>
- `tempset` – A set of matrices the callers wants to use temporarily, but doesn't care about the values in the long-term.

### `pspvfpu_initcontext()`

```c
struct pspvfpu_context * pspvfpu_initcontext(void);
```

Prepare to use the VFPU.

This set's the calling thread's VFPU attribute, and returns a pointer to some VFPU state storage. The initial value all all VFPU matrix registers is undefined.

**Returns:** A VFPU context

### `pspvfpu_deletecontext()`

```c
void pspvfpu_deletecontext(struct pspvfpu_context *c);
```

Delete a VFPU context.

This frees the resources used by the VFPU context.

**Parameters:**

- `context` – The VFPU context to be deleted.

## Variables

### `users`

```c
struct pspvfpu_context* users[8][8];
```

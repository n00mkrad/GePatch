[PSPSDK documentation](../../README.md) › Files

# vfpu/pspvfpu.h

## Macros

### `VMAT0`

```c
#define VMAT0 (1<<0)
```

### `VMAT1`

```c
#define VMAT1 (1<<1)
```

### `VMAT2`

```c
#define VMAT2 (1<<2)
```

### `VMAT3`

```c
#define VMAT3 (1<<3)
```

### `VMAT4`

```c
#define VMAT4 (1<<4)
```

### `VMAT5`

```c
#define VMAT5 (1<<5)
```

### `VMAT6`

```c
#define VMAT6 (1<<6)
```

### `VMAT7`

```c
#define VMAT7 (1<<7)
```

### `VFPU_ALIGNMENT`

```c
#define VFPU_ALIGNMENT (sizeof(float) * 4)	/* alignment required for VFPU matrix loads and stores */
```

## Typedefs

### `vfpumatrixset_t`

```c
typedef unsigned char vfpumatrixset_t;
```

## Functions

### `pspvfpu_initcontext()`

```c
struct pspvfpu_context * pspvfpu_initcontext(void);
```

Prepare to use the VFPU.

This set's the calling thread's VFPU attribute, and returns a pointer to some VFPU state storage. The initial value all all VFPU matrix registers is undefined.

**Returns:** A VFPU context

### `pspvfpu_deletecontext()`

```c
void pspvfpu_deletecontext(struct pspvfpu_context *context);
```

Delete a VFPU context.

This frees the resources used by the VFPU context.

**Parameters:**

- `context` – The VFPU context to be deleted.

### `pspvfpu_use_matrices()`

```c
void pspvfpu_use_matrices(struct pspvfpu_context *context, vfpumatrixset_t keepset, vfpumatrixset_t tempset);
```

Use a set of VFPU matrices.

This restores the parts of the VFPU state the caller wants restored (if necessary). If the caller was the previous user of the the matrix set, then this call is effectively a no-op. If a matrix has never been used by this context before, then it will initially have an undefined value.

**Parameters:**

- `context` – The VFPU context the caller wants to restore from. It is valid to pass NULL as a context. This means the caller wants to reserve a temporary matrix without affecting other VFPU users, but doesn't want any long-term matrices itself.
- `keepset` – The set of matrices the caller wants to use, and keep the values persistently.<br>
- `tempset` – A set of matrices the callers wants to use temporarily, but doesn't care about the values in the long-term.

[PSPSDK documentation](../../README.md) › Files

# gum/gumInternal.h

```c
#include <alloca.h>
#include "pspgum.h"
#include "../gu/pspgu.h"
```

## Macros

### `GUM_EPSILON`

```c
#define GUM_EPSILON 0.00001f
```

### `GUM_ALIGNED_MATRIX()`

```c
#define GUM_ALIGNED_MATRIX() (ScePspFMatrix4*)((((unsigned int)alloca(sizeof(ScePspFMatrix4)+64)) + 63) & ~63)
```

### `GUM_ALIGNED_VECTOR()`

```c
#define GUM_ALIGNED_VECTOR() (ScePspFVector4*)((((unsigned int)alloca(sizeof(ScePspFVector4)+64)) + 63) & ~63)
```

## Variables

### `gum_current_mode`

```c
int gum_current_mode;
```

### `gum_matrix_update`

```c
int gum_matrix_update[4][4];
```

### `gum_current_matrix_update`

```c
int gum_current_matrix_update;
```

### `gum_current_matrix`

```c
ScePspFMatrix4* gum_current_matrix;
```

### `gum_stack_depth`

```c
ScePspFMatrix4* gum_stack_depth[4][4];
```

### `gum_matrix_stack`

```c
ScePspFMatrix4 gum_matrix_stack[4][32][4][32];
```

### `gum_vfpucontext`

```c
struct pspvfpu_context* gum_vfpucontext;
```

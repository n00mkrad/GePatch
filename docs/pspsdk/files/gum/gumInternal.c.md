[PSPSDK documentation](../../README.md) › Files

# gum/gumInternal.c

```c
#include "gumInternal.h"
#include <math.h>
#include <string.h>
```

## Variables

### `gum_current_mode`

```c
int gum_current_mode =  (0);
```

### `gum_matrix_update`

```c
int gum_matrix_update[4][4] = { 0 };
```

### `gum_current_matrix_update`

```c
int gum_current_matrix_update = 0;
```

### `gum_current_matrix`

```c
ScePspFMatrix4* gum_current_matrix = gum_matrix_stack[ (0) ];
```

### `gum_stack_depth`

```c
ScePspFMatrix4* gum_stack_depth[4][4] =
{
  gum_matrix_stack[ (0) ],
  gum_matrix_stack[ (1) ],
  gum_matrix_stack[ (2) ],
  gum_matrix_stack[ (3) ]
};
```

### `gum_matrix_stack`

```c
ScePspFMatrix4 gum_matrix_stack[4][32][4][32];
```

### `gum_vfpucontext`

```c
struct pspvfpu_context* gum_vfpucontext;
```

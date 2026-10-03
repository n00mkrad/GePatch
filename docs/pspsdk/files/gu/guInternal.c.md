[PSPSDK documentation](../../README.md) › Files

# gu/guInternal.c

```c
#include "guInternal.h"
```

## Variables

### `gu_contexts`

```c
GuContext gu_contexts[3][3];
```

### `ge_list_executed`

```c
int ge_list_executed[2][2];
```

### `ge_edram_address`

```c
void* ge_edram_address;
```

### `gu_settings`

```c
GuSettings gu_settings;
```

### `gu_list`

```c
GuDisplayList* gu_list;
```

### `gu_curr_context`

```c
int gu_curr_context;
```

### `gu_init`

```c
int gu_init;
```

### `gu_first_start`

```c
int gu_first_start;
```

### `gu_display_on`

```c
int gu_display_on;
```

### `gu_call_mode`

```c
int gu_call_mode;
```

### `gu_states`

```c
int gu_states;
```

### `gu_draw_buffer`

```c
GuDrawBuffer gu_draw_buffer;
```

### `gu_object_stack`

```c
unsigned int* gu_object_stack[32][32];
```

### `gu_object_stack_depth`

```c
int gu_object_stack_depth;
```

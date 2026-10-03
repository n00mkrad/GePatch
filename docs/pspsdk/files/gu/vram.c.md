[PSPSDK documentation](../../README.md) › Files

# gu/vram.c

```c
#include <pspge.h>
#include <pspgu.h>
```

## Macros

### `ALIGNMENT`

```c
#define ALIGNMENT 16
```

## Functions

### `getMemorySize()`

```c
static unsigned int getMemorySize(unsigned int width, unsigned int height, unsigned int psm);
```

## Variables

### `staticOffset`

```c
unsigned int staticOffset = 0;
```

**Also defined in this file** (documented with the declaration):

- [`guGetStaticVramBuffer`](pspgu.h.md#gugetstaticvrambuffer)
- [`guGetStaticVramTexture`](pspgu.h.md#gugetstaticvramtexture)

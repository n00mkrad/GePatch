[PSPSDK documentation](../../README.md) › Files

# debug/screenshot.c

```c
#include "pspdebug.h"
#include "pspdisplay.h"
#include "pspuser.h"
```

## Macros

### `PSP_SCREEN_HEIGHT`

```c
#define PSP_SCREEN_HEIGHT 272
```

## Functions

### `bitmapWrite()`

```c
int bitmapWrite(void *frame_addr, int format, const char *file);
```

**Also defined in this file** (documented with the declaration):

- [`pspScreenshotSave`](pspdebug.h.md#pspscreenshotsave)

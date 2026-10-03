[PSPSDK documentation](../../README.md) › Files

# kernel/pspsysclib.h

```c
#include <pspkerneltypes.h>
#include <stdarg.h>
```

## Typedefs

### `prnt_callback`

```c
typedef void(* prnt_callback) (void *ctx, int ch))(void *ctx, int ch);
```

Callback type, ch is 0x200 on start of string, 0x201 on end.

## Functions

### `prnt()`

```c
void prnt(prnt_callback cb, void *ctx, const char *fmt, va_list args);
```

Generic print routine.

**Parameters:**

- `cb` – Callback, called for every character printed
- `ctx` – Context parameter passed to the callback
- `fmt` – Format data
- `args` – Arguments for format

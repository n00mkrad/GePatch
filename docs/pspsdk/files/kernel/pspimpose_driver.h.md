[PSPSDK documentation](../../README.md) › Files

# kernel/pspimpose_driver.h

```c
#include <pspimpose.h>
```

## Macros

### `PSP_IMPOSE_MAIN_VOLUME`

```c
#define PSP_IMPOSE_MAIN_VOLUME 0x1
```

These values have been found in the 3.52 kernel.

Therefore, they might not be supported by previous ones.

### `PSP_IMPOSE_BACKLIGHT_BRIGHTNESS`

```c
#define PSP_IMPOSE_BACKLIGHT_BRIGHTNESS 0x2
```

### `PSP_IMPOSE_EQUALIZER_MODE`

```c
#define PSP_IMPOSE_EQUALIZER_MODE 0x4
```

### `PSP_IMPOSE_MUTE`

```c
#define PSP_IMPOSE_MUTE 0x8
```

### `PSP_IMPOSE_AVLS`

```c
#define PSP_IMPOSE_AVLS 0x10
```

### `PSP_IMPOSE_TIME_FORMAT`

```c
#define PSP_IMPOSE_TIME_FORMAT 0x20
```

### `PSP_IMPOSE_DATE_FORMAT`

```c
#define PSP_IMPOSE_DATE_FORMAT 0x40
```

### `PSP_IMPOSE_LANGUAGE`

```c
#define PSP_IMPOSE_LANGUAGE 0x80
```

### `PSP_IMPOSE_BACKLIGHT_OFF_INTERVAL`

```c
#define PSP_IMPOSE_BACKLIGHT_OFF_INTERVAL 0x200
```

### `PSP_IMPOSE_SOUND_REDUCTION`

```c
#define PSP_IMPOSE_SOUND_REDUCTION 0x400
```

## Typedefs

### `SceImposeParam`

```c
typedef int SceImposeParam;
```

## Functions

### `sceImposeGetParam()`

```c
int sceImposeGetParam(SceImposeParam param);
```

Fetch the value of an Impose parameter.

**Returns:** value of the parameter on success, \< 0 on error

### `sceImposeSetParam()`

```c
int sceImposeSetParam(SceImposeParam param, int value);
```

Change the value of an Impose parameter.

**Parameters:**

- `param` – The parameter to change.
- `value` – The value to set the parameter to.

**Returns:** \< 0 on error

### `sceImposeCheckVideoOut()`

```c
int sceImposeCheckVideoOut(int *value);
```

Check the video out.

(for psp slim?)

**Parameters:**

- `value` – video out mode/status(?)

**Returns:** \< 0 on error

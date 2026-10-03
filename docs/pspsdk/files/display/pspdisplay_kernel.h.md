[PSPSDK documentation](../../README.md) › Files

# display/pspdisplay_kernel.h

## Macros

### `sceDisplaySetFrameBufferInternal`

```c
#define sceDisplaySetFrameBufferInternal sceDisplay_driver_63E22A26
```

### `sceDisplayGetFrameBufferInternal`

```c
#define sceDisplayGetFrameBufferInternal sceDisplay_driver_5B5AEFAD
```

## Functions

### `sceDisplay_driver_63E22A26()`

```c
int sceDisplay_driver_63E22A26(int pri, void *topaddr, int bufferwidth, int pixelformat, int sync);
```

Display set framebuf.

**Parameters:**

- `pri` – Priority
- `topaddr` – address of start of framebuffer
- `bufferwidth` – buffer width (must be power of 2)
- `pixelformat` – One of [PspDisplayPixelFormats](pspdisplay.h.md#enum-pspdisplaypixelformats).
- `sync` – One of [PspDisplaySetBufSync](pspdisplay.h.md#enum-pspdisplaysetbufsync)

**Returns:** 0 on success

### `sceDisplay_driver_5B5AEFAD()`

```c
int sceDisplay_driver_5B5AEFAD(int pri, void **topaddr, int *bufferwidth, int *pixelformat, int *sync);
```

Get Display Framebuffer information.

**Parameters:**

- `pri` – Priority
- `topaddr` – pointer to void\* to receive address of start of framebuffer
- `bufferwidth` – pointer to int to receive buffer width (must be power of 2)
- `pixelformat` – pointer to int to receive one of [PspDisplayPixelFormats](pspdisplay.h.md#enum-pspdisplaypixelformats).
- `sync` – pointer to int to receive one of [PspDisplaySetBufSync](pspdisplay.h.md#enum-pspdisplaysetbufsync)

**Returns:** 0 on success

### `sceDisplaySetBrightness()`

```c
void sceDisplaySetBrightness(int level, int unk1);
```

Set Display brightness to a particular level.

**Parameters:**

- `level` – Level of the brightness. it goes from 0 (black screen) to 100 (max brightness)
- `unk1` – Unknown can be 0 or 1 (pass 0)

### `sceDisplayGetBrightness()`

```c
void sceDisplayGetBrightness(int *level, int *unk1);
```

Get current display brightness.

**Parameters:**

- `level` – Pointer to int to receive the current brightness level (0-100)
- `unk1` – Pointer to int, receives unknown, it's 1 or 0

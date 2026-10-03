[PSPSDK documentation](../../README.md) › Files

# display/pspdisplay.h

## Macros

### `PSP_DISPLAY_SETBUF_IMMEDIATE`

```c
#define PSP_DISPLAY_SETBUF_IMMEDIATE PSP_DISPLAY_SETBUF_NEXTHSYNC
```

Values for retro compatibility.

### `PSP_DISPLAY_SETBUF_NEXTFRAME`

```c
#define PSP_DISPLAY_SETBUF_NEXTFRAME PSP_DISPLAY_SETBUF_NEXTVSYNC
```

## Enumerations

### `enum PspDisplayPixelFormats`

Framebuffer pixel formats.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_DISPLAY_PIXEL_FORMAT_565` | `0` | 16-bit RGB 5:6:5. |
| `PSP_DISPLAY_PIXEL_FORMAT_5551` |  | 16-bit RGBA 5:5:5:1. |
| `PSP_DISPLAY_PIXEL_FORMAT_4444` |  |  |
| `PSP_DISPLAY_PIXEL_FORMAT_8888` |  |  |

### `enum PspDisplaySetBufSync`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_DISPLAY_SETBUF_NEXTHSYNC` | `0` | Buffer change effective next hsync. |
| `PSP_DISPLAY_SETBUF_NEXTVSYNC` | `1` | Buffer change effective next vsync. |

### `enum PspDisplayMode`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_DISPLAY_MODE_LCD` | `0` | LCD MAX 480x272 at 59.94005995 Hz. |
| `PSP_DISPLAY_MODE_VESA1A` | `0x1A` | VESA VGA MAX 640x480 at 59.94047618Hz. |
| `PSP_DISPLAY_MODE_PSEUDO_VGA` | `0x60` | PSEUDO VGA MAX 640x480 at 59.94005995Hz. |

### `enum PspDisplayErrorCodes`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_DISPLAY_ERROR_OK` | `0` |  |
| `SCE_DISPLAY_ERROR_POINTER` | `0x80000103` |  |
| `SCE_DISPLAY_ERROR_ARGUMENT` | `0x80000107` |  |

## Functions

### `sceDisplaySetMode()`

```c
int sceDisplaySetMode(int mode, int width, int height);
```

Set display mode.

**Example1::**

```c
int mode = PSP_DISPLAY_MODE_LCD;
int width = 480;
int height = 272;
sceDisplaySetMode(mode, width, height);
```

**Parameters:**

- `mode` – One of [PspDisplayMode](#enum-pspdisplaymode)
- `width` – Width of screen in pixels.
- `height` – Height of screen in pixels.

**Returns:** when error, a negative value is returned.

### `sceDisplayGetMode()`

```c
int sceDisplayGetMode(int *pmode, int *pwidth, int *pheight);
```

Get display mode.

**Parameters:**

- `pmode` – Pointer to an integer to receive the current mode.
- `pwidth` – Pointer to an integer to receive the current width.
- `pheight` – Pointer to an integer to receive the current height,

**Returns:** 0 on success

### `sceDisplaySetFrameBuf()`

```c
int sceDisplaySetFrameBuf(void *topaddr, int bufferwidth, int pixelformat, int sync);
```

Display set framebuf.

**Parameters:**

- `topaddr` – address of start of framebuffer
- `bufferwidth` – buffer width (must be power of 2)
- `pixelformat` – One of [PspDisplayPixelFormats](#enum-pspdisplaypixelformats).
- `sync` – One of [PspDisplaySetBufSync](#enum-pspdisplaysetbufsync)

**Returns:** 0 on success

### `sceDisplayGetFrameBuf()`

```c
int sceDisplayGetFrameBuf(void **topaddr, int *bufferwidth, int *pixelformat, int sync);
```

Get Display Framebuffer information.

**Parameters:**

- `topaddr` – pointer to void\* to receive address of start of framebuffer
- `bufferwidth` – pointer to int to receive buffer width (must be power of 2)
- `pixelformat` – pointer to int to receive one of [PspDisplayPixelFormats](#enum-pspdisplaypixelformats).
- `sync` – One of [PspDisplaySetBufSync](#enum-pspdisplaysetbufsync)

**Returns:** 0 on success

### `sceDisplayGetVcount()`

```c
unsigned int sceDisplayGetVcount(void);
```

Number of vertical blank pulses up to now.

### `sceDisplayWaitVblankStart()`

```c
int sceDisplayWaitVblankStart(void);
```

Wait for vertical blank start.

### `sceDisplayWaitVblankStartCB()`

```c
int sceDisplayWaitVblankStartCB(void);
```

Wait for vertical blank start with callback.

### `sceDisplayWaitVblank()`

```c
int sceDisplayWaitVblank(void);
```

Wait for vertical blank.

### `sceDisplayWaitVblankCB()`

```c
int sceDisplayWaitVblankCB(void);
```

Wait for vertical blank with callback.

### `sceDisplayGetAccumulatedHcount()`

```c
int sceDisplayGetAccumulatedHcount(void);
```

Get accumlated HSYNC count.

### `sceDisplayGetCurrentHcount()`

```c
int sceDisplayGetCurrentHcount(void);
```

Get current HSYNC count.

### `sceDisplayGetFramePerSec()`

```c
float sceDisplayGetFramePerSec(void);
```

Get number of frames per second.

### `sceDisplayIsForeground()`

```c
int sceDisplayIsForeground(void);
```

Get whether or not frame buffer is being displayed.

### `sceDisplayIsVblank()`

```c
int sceDisplayIsVblank(void);
```

Test whether VBLANK is active.

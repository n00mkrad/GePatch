[PSPSDK documentation](../../README.md) › Files

# mpeg/pspjpeg.h

```c
#include <psptypes.h>
```

## Macros

### `SCE_JPEG_ERROR_BAD_MARKER_LENGTH`

```c
#define SCE_JPEG_ERROR_BAD_MARKER_LENGTH (0x80650004)
```

### `SCE_JPEG_ERROR_INVALID_POINTER`

```c
#define SCE_JPEG_ERROR_INVALID_POINTER (0x80650010)
```

### `SCE_JPEG_ERROR_UNSUPPORT_COLORSPACE`

```c
#define SCE_JPEG_ERROR_UNSUPPORT_COLORSPACE (0x80650013)
```

### `SCE_JPEG_ERROR_UNSUPPORT_SAMPLING`

```c
#define SCE_JPEG_ERROR_UNSUPPORT_SAMPLING (0x80650016)
```

### `SCE_JPEG_ERROR_UNSUPPORT_IMAGE_SIZE`

```c
#define SCE_JPEG_ERROR_UNSUPPORT_IMAGE_SIZE (0x80650020)
```

### `SCE_JPEG_ERROR_UNKNOWN_MARKER`

```c
#define SCE_JPEG_ERROR_UNKNOWN_MARKER (0x80650035)
```

## Functions

### `sceJpegInitMJpeg()`

```c
int sceJpegInitMJpeg(void);
```

Inits the MJpeg library.

**Returns:** 0 on success, \< 0 on error

### `sceJpegFinishMJpeg()`

```c
int sceJpegFinishMJpeg(void);
```

Finishes the MJpeg library.

**Returns:** 0 on success, \< 0 on error

### `sceJpegCreateMJpeg()`

```c
int sceJpegCreateMJpeg(int width, int height);
```

Creates the decoder context.

**Parameters:**

- `width` – The width of the frame
- `height` – The height of the frame

**Returns:** 0 on success, \< 0 on error

### `sceJpegDeleteMJpeg()`

```c
int sceJpegDeleteMJpeg(void);
```

Deletes the current decoder context.

**Returns:** 0 on success, \< 0 on error

### `sceJpegDecodeMJpeg()`

```c
int sceJpegDecodeMJpeg(u8 *jpegbuf, SceSize size, u8 *rgba, u32 unk);
```

Decodes a mjpeg frame to RGBA encoding.

**Note:** Input frame should be encoded as either yuv420p or yuvj420p, returns SCE_JPEG_ERROR_UNSUPPORT_SAMPLING otherwise

**Parameters:**

- `jpegbuf` – the buffer with the mjpeg frame
- `size` – size of the buffer pointed by jpegbuf
- `rgba` – buffer where the decoded data in RGBA format will be stored. It should have a size of (width \* height \* 4).
- `unk` – Unknown, pass 0

**Returns:** (width \* 65536) + height on success, \< 0 on error

### `sceJpegGetOutputInfo()`

```c
int sceJpegGetOutputInfo(u8 *jpegbuf, SceSize size, int *colourInfo, int unk);
```

Reads information from mjpeg frame.

**Parameters:**

- `jpegbuf` – the buffer with the mjpeg frame
- `size` – size of the mjpeg frame
- `colourInfo` – address where the mjpeg chroma information will be stored
- `unk` – Unknown, pass 0

**Returns:** number of bytes needed in the buffer that will be used for YCbCr decoding, \<= 0 on error

### `sceJpegDecodeMJpegYCbCr()`

```c
int sceJpegDecodeMJpegYCbCr(u8 *jpegbuf, SceSize size, u8 *yCbCr, SceSize yCbCrSize, u32 unk);
```

Decodes a mjpeg frame to YCbCr encoding.

**Note:** Input frame should be encoded as either yuv420p or yuvj420p, returns SCE_JPEG_ERROR_UNSUPPORT_SAMPLING otherwise

**Parameters:**

- `jpegbuf` – the buffer with the mjpeg frame
- `size` – size of the buffer pointed by jpegbuf
- `yCbCr` – buffer where the decoded data in YCbCr format will be stored
- `yCbCrSize` – size of the buffer pointed by yCbCr (see [sceJpegGetOutputInfo()](#scejpeggetoutputinfo))
- `unk` – Unknown, pass 0

**Returns:** (width \* 65536) + height on success, \< 0 on error

### `sceJpegCsc()`

```c
int sceJpegCsc(u8 *imageAddr, u8 *yCbCrAddr, int widthHeight, int bufferWidth, int colourInfo);
```

Converts a frame from YCbCr to RGBA.

**Parameters:**

- `imageAddr` – buffer where the converted data in RGBA format will be stored.
- `yCbCrAddr` – the buffer with the YCbCr data
- `widthHeight` – width and height of the frame (width \* 65536) + height, as returned by [sceJpegDecodeMJpegYCbCr()](#scejpegdecodemjpegycbcr) or [sceJpegDecodeMJpeg()](#scejpegdecodemjpeg)
- `bufferWidth` – number of pixels per row of the buffer
- `colourInfo` – chroma subsampling mode, as provided by [sceJpegGetOutputInfo()](#scejpeggetoutputinfo)

**Returns:** 0 on success, \< 0 on error

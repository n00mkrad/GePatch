[PSPSDK documentation](../../README.md) › Files

# mpeg/pspmpegbase.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct SceMpegLLI`

```c
struct SceMpegLLI {
    ScePVoid pSrc;
    ScePVoid pDst;
    ScePVoid Next;
    SceInt32 iSize;
};
```

### `struct SceMpegYCrCbBuffer`

```c
struct SceMpegYCrCbBuffer {
    SceInt32 iFrameBufferHeight16;
    SceInt32 iFrameBufferWidth16;
    SceInt32 iUnknown;
    SceInt32 iUnknown2;
    ScePVoid pYBuffer;
    ScePVoid pYBuffer2;
    ScePVoid pCrBuffer;
    ScePVoid pCbBuffer;
    ScePVoid pCrBuffer2;
    ScePVoid pCbBuffer2;
    SceInt32 iFrameHeight;
    SceInt32 iFrameWidth;
    SceInt32 iFrameBufferWidth;
    SceInt32 iUnknown3[11];
};
```

## Typedefs

### `SceMpegLLI`

```c
typedef struct SceMpegLLI SceMpegLLI;
```

### `SceMpegYCrCbBuffer`

```c
typedef struct SceMpegYCrCbBuffer SceMpegYCrCbBuffer;
```

## Functions

### `sceMpegBaseYCrCbCopyVme()`

```c
SceInt32 sceMpegBaseYCrCbCopyVme(ScePVoid YUVBuffer, SceInt32 *Buffer, SceInt32 Type);
```

### `sceMpegBaseCscInit()`

```c
SceInt32 sceMpegBaseCscInit(SceInt32 width);
```

### `sceMpegBaseCscVme()`

```c
SceInt32 sceMpegBaseCscVme(ScePVoid pRGBbuffer, ScePVoid pRGBbuffer2, SceInt32 width, SceMpegYCrCbBuffer *pYCrCbBuffer);
```

### `sceMpegBasePESpacketCopy()`

```c
SceInt32 sceMpegBasePESpacketCopy(SceMpegLLI *pLLI);
```

[PSPSDK documentation](../../README.md) › Files

# mpeg/pspmpeg.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct SceMpegRingbuffer`

| Field | Description |
|---|---|
| `SceInt32 iPackets` | packets |
| `SceUInt32 iUnk0` | unknown |
| `SceUInt32 iUnk1` | unknown |
| `SceUInt32 iUnk2` | unknown |
| `SceUInt32 iUnk3` | unknown |
| `ScePVoid pData` | pointer to data |
| `sceMpegRingbufferCB Callback` | ringbuffer callback |
| `ScePVoid pCBparam` | callback param |
| `SceUInt32 iUnk4` | unknown |
| `SceUInt32 iUnk5` | unknown |
| `SceMpeg pSceMpeg` | mpeg id |

### `struct SceMpegAu`

| Field | Description |
|---|---|
| `SceUInt32 iPtsMSB` | presentation timestamp MSB |
| `SceUInt32 iPts` | presentation timestamp LSB |
| `SceUInt32 iDtsMSB` | decode timestamp MSB |
| `SceUInt32 iDts` | decode timestamp LSB |
| `SceUInt32 iEsBuffer` | Es buffer handle. |
| `SceUInt32 iAuSize` | Au size. |

### `struct SceMpegAvcMode`

| Field | Description |
|---|---|
| `SceInt32 iUnk0` | unknown, set to -1 |
| `SceInt32 iPixelFormat` | Decode pixelformat. |

## Macros

### `SCE_MPEG_AVC_FORMAT_DEFAULT`

```c
#define SCE_MPEG_AVC_FORMAT_DEFAULT -1
```

### `SCE_MPEG_AVC_FORMAT_5650`

```c
#define SCE_MPEG_AVC_FORMAT_5650 0
```

### `SCE_MPEG_AVC_FORMAT_5551`

```c
#define SCE_MPEG_AVC_FORMAT_5551 1
```

### `SCE_MPEG_AVC_FORMAT_4444`

```c
#define SCE_MPEG_AVC_FORMAT_4444 2
```

### `SCE_MPEG_AVC_FORMAT_8888`

```c
#define SCE_MPEG_AVC_FORMAT_8888 3
```

## Typedefs

### `SceMpeg`

```c
typedef ScePVoid SceMpeg;
```

points to "LIBMPEG"

### `SceMpegStream`

```c
typedef SceVoid SceMpegStream;
```

some structure

### `sceMpegRingbufferCB`

```c
typedef SceInt32(* sceMpegRingbufferCB) (ScePVoid pData, SceInt32 iNumPackets, ScePVoid pParam))(ScePVoid pData, SceInt32 iNumPackets, ScePVoid pParam);
```

Ringbuffer callback.

### `SceMpegRingbuffer`

```c
typedef struct SceMpegRingbuffer SceMpegRingbuffer;
```

### `SceMpegAu`

```c
typedef struct SceMpegAu SceMpegAu;
```

### `SceMpegAvcMode`

```c
typedef struct SceMpegAvcMode SceMpegAvcMode;
```

## Functions

### `sceMpegInit()`

```c
SceInt32 sceMpegInit(void);
```

sceMpegInit

**Returns:** 0 if success.

### `sceMpegFinish()`

```c
SceVoid sceMpegFinish(void);
```

sceMpegFinish

### `sceMpegRingbufferQueryMemSize()`

```c
SceInt32 sceMpegRingbufferQueryMemSize(SceInt32 iPackets);
```

sceMpegRingbufferQueryMemSize

**Parameters:**

- `iPackets` – number of packets in the ringbuffer

**Returns:** \< 0 if error else ringbuffer data size.

### `sceMpegRingbufferConstruct()`

```c
SceInt32 sceMpegRingbufferConstruct(SceMpegRingbuffer *Ringbuffer, SceInt32 iPackets, ScePVoid pData, SceInt32 iSize, sceMpegRingbufferCB Callback, ScePVoid pCBparam);
```

sceMpegRingbufferConstruct

**Parameters:**

- `Ringbuffer` – pointer to a sceMpegRingbuffer struct
- `iPackets` – number of packets in the ringbuffer
- `pData` – pointer to allocated memory
- `iSize` – size of allocated memory, shoud be sceMpegRingbufferQueryMemSize(iPackets)
- `Callback` – ringbuffer callback
- `pCBparam` – param passed to callback

**Returns:** 0 if success.

### `sceMpegRingbufferDestruct()`

```c
SceVoid sceMpegRingbufferDestruct(SceMpegRingbuffer *Ringbuffer);
```

sceMpegRingbufferDestruct

**Parameters:**

- `Ringbuffer` – pointer to a sceMpegRingbuffer struct

### `sceMpegRingbufferAvailableSize()`

```c
SceInt32 sceMpegRingbufferAvailableSize(SceMpegRingbuffer *Ringbuffer);
```

sceMpegQueryMemSize

**Parameters:**

- `Ringbuffer` – pointer to a sceMpegRingbuffer struct

**Returns:** \< 0 if error else number of free packets in the ringbuffer.

### `sceMpegRingbufferPut()`

```c
SceInt32 sceMpegRingbufferPut(SceMpegRingbuffer *Ringbuffer, SceInt32 iNumPackets, SceInt32 iAvailable);
```

sceMpegRingbufferPut

**Parameters:**

- `Ringbuffer` – pointer to a sceMpegRingbuffer struct
- `iNumPackets` – num packets to put into the ringbuffer
- `iAvailable` – free packets in the ringbuffer, should be [sceMpegRingbufferAvailableSize()](#scempegringbufferavailablesize)

**Returns:** \< 0 if error else number of packets.

### `sceMpegQueryMemSize()`

```c
SceInt32 sceMpegQueryMemSize(int iUnk);
```

sceMpegQueryMemSize

**Parameters:**

- `iUnk` – Unknown, set to 0

**Returns:** \< 0 if error else decoder data size.

### `sceMpegCreate()`

```c
SceInt32 sceMpegCreate(SceMpeg *Mpeg, ScePVoid pData, SceInt32 iSize, SceMpegRingbuffer *Ringbuffer, SceInt32 iFrameWidth, SceInt32 iUnk1, SceInt32 iUnk2);
```

sceMpegCreate

**Parameters:**

- `Mpeg` – will be filled
- `pData` – pointer to allocated memory of size = [sceMpegQueryMemSize()](#scempegquerymemsize)
- `iSize` – size of data, should be = [sceMpegQueryMemSize()](#scempegquerymemsize)
- `Ringbuffer` – a ringbuffer
- `iFrameWidth` – display buffer width, set to 512 if writing to framebuffer
- `iUnk1` – unknown, set to 0
- `iUnk2` – unknown, set to 0

**Returns:** 0 if success.

### `sceMpegDelete()`

```c
SceVoid sceMpegDelete(SceMpeg *Mpeg);
```

sceMpegDelete

**Parameters:**

- `Mpeg` – SceMpeg handle

### `sceMpegQueryStreamOffset()`

```c
SceInt32 sceMpegQueryStreamOffset(SceMpeg *Mpeg, ScePVoid pBuffer, SceInt32 *iOffset);
```

sceMpegQueryStreamOffset

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pBuffer` – pointer to file header
- `iOffset` – will contain stream offset in bytes, usually 2048

**Returns:** 0 if success.

### `sceMpegQueryStreamSize()`

```c
SceInt32 sceMpegQueryStreamSize(ScePVoid pBuffer, SceInt32 *iSize);
```

sceMpegQueryStreamSize

**Parameters:**

- `pBuffer` – pointer to file header
- `iSize` – will contain stream size in bytes

**Returns:** 0 if success.

### `sceMpegRegistStream()`

```c
SceMpegStream * sceMpegRegistStream(SceMpeg *Mpeg, SceInt32 iStreamID, SceInt32 iUnk);
```

sceMpegRegistStream

**Parameters:**

- `Mpeg` – SceMpeg handle
- `iStreamID` – stream id, 0 for video, 1 for audio
- `iUnk` – unknown, set to 0

**Returns:** 0 if error.

### `sceMpegUnRegistStream()`

```c
SceVoid sceMpegUnRegistStream(SceMpeg Mpeg, SceMpegStream *pStream);
```

sceMpegUnRegistStream

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pStream` – pointer to stream

### `sceMpegFlushAllStream()`

```c
SceInt32 sceMpegFlushAllStream(SceMpeg *Mpeg);
```

sceMpegFlushAllStreams

**Returns:** 0 if success.

### `sceMpegMallocAvcEsBuf()`

```c
ScePVoid sceMpegMallocAvcEsBuf(SceMpeg *Mpeg);
```

sceMpegMallocAvcEsBuf

**Returns:** 0 if error else pointer to buffer.

### `sceMpegFreeAvcEsBuf()`

```c
SceVoid sceMpegFreeAvcEsBuf(SceMpeg *Mpeg, ScePVoid pBuf);
```

sceMpegFreeAvcEsBuf

### `sceMpegQueryAtracEsSize()`

```c
SceInt32 sceMpegQueryAtracEsSize(SceMpeg *Mpeg, SceInt32 *iEsSize, SceInt32 *iOutSize);
```

sceMpegQueryAtracEsSize

**Parameters:**

- `Mpeg` – SceMpeg handle
- `iEsSize` – will contain size of Es
- `iOutSize` – will contain size of decoded data

**Returns:** 0 if success.

### `sceMpegInitAu()`

```c
SceInt32 sceMpegInitAu(SceMpeg *Mpeg, ScePVoid pEsBuffer, SceMpegAu *pAu);
```

sceMpegInitAu

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pEsBuffer` – prevously allocated Es buffer
- `pAu` – will contain pointer to Au

**Returns:** 0 if success.

### `sceMpegGetAvcAu()`

```c
SceInt32 sceMpegGetAvcAu(SceMpeg *Mpeg, SceMpegStream *pStream, SceMpegAu *pAu, SceInt32 *iUnk);
```

sceMpegGetAvcAu

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pStream` – associated stream
- `pAu` – will contain pointer to Au
- `iUnk` – unknown

**Returns:** 0 if success.

### `sceMpegAvcDecodeMode()`

```c
SceInt32 sceMpegAvcDecodeMode(SceMpeg *Mpeg, SceMpegAvcMode *pMode);
```

sceMpegAvcDecodeMode

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pMode` – pointer to [SceMpegAvcMode](#struct-scempegavcmode) struct defining the decode mode (pixelformat)

**Returns:** 0 if success.

### `sceMpegAvcDecode()`

```c
SceInt32 sceMpegAvcDecode(SceMpeg *Mpeg, SceMpegAu *pAu, SceInt32 iFrameWidth, ScePVoid pBuffer, SceInt32 *iInit);
```

sceMpegAvcDecode

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pAu` – video Au
- `iFrameWidth` – output buffer width, set to 512 if writing to framebuffer
- `pBuffer` – buffer that will contain the decoded frame
- `iInit` – will be set to 0 on first call, then 1

**Returns:** 0 if success.

### `sceMpegAvcDecodeStop()`

```c
SceInt32 sceMpegAvcDecodeStop(SceMpeg *Mpeg, SceInt32 iFrameWidth, ScePVoid pBuffer, SceInt32 *iStatus);
```

sceMpegAvcDecodeStop

**Parameters:**

- `Mpeg` – SceMpeg handle
- `iFrameWidth` – output buffer width, set to 512 if writing to framebuffer
- `pBuffer` – buffer that will contain the decoded frame
- `iStatus` – frame number

**Returns:** 0 if success.

### `sceMpegGetAtracAu()`

```c
SceInt32 sceMpegGetAtracAu(SceMpeg *Mpeg, SceMpegStream *pStream, SceMpegAu *pAu, ScePVoid pUnk);
```

sceMpegGetAtracAu

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pStream` – associated stream
- `pAu` – will contain pointer to Au
- `pUnk` – unknown

**Returns:** 0 if success.

### `sceMpegAtracDecode()`

```c
SceInt32 sceMpegAtracDecode(SceMpeg *Mpeg, SceMpegAu *pAu, ScePVoid pBuffer, SceInt32 iInit);
```

sceMpegAtracDecode

**Parameters:**

- `Mpeg` – SceMpeg handle
- `pAu` – video Au
- `pBuffer` – buffer that will contain the decoded frame
- `iInit` – set this to 1 on first call

**Returns:** 0 if success.

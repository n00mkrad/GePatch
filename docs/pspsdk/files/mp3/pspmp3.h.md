[PSPSDK documentation](../../README.md) › Files

# mp3/pspmp3.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct SceMp3InitArg`

| Field | Description |
|---|---|
| `SceOff mp3StreamStart` | Stream start position. |
| `SceOff mp3StreamEnd` | Stream end position. |
| `SceUChar8 * mp3Buf` | Pointer to a buffer to contain raw mp3 stream data (+1472 bytes workspace) |
| `SceInt32 mp3BufSize` | Size of mp3Buf buffer (must be >= 8192) |
| `SceUChar8 * pcmBuf` | Pointer to decoded pcm samples buffer. |
| `SceInt32 pcmBufSize` | Size of pcmBuf buffer (must be >= 9216) |

## Typedefs

### `SceMp3InitArg`

```c
typedef struct SceMp3InitArg SceMp3InitArg;
```

## Functions

### `sceMp3ReserveMp3Handle()`

```c
SceInt32 sceMp3ReserveMp3Handle(SceMp3InitArg *args);
```

sceMp3ReserveMp3Handle

**Parameters:**

- `args` – Pointer to [SceMp3InitArg](#struct-scemp3initarg) structure

**Returns:** sceMp3 handle on success, \< 0 on error.

### `sceMp3ReleaseMp3Handle()`

```c
SceInt32 sceMp3ReleaseMp3Handle(SceInt32 handle);
```

sceMp3ReleaseMp3Handle

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** 0 if success, \< 0 on error.

### `sceMp3InitResource()`

```c
SceInt32 sceMp3InitResource(void);
```

sceMp3InitResource

**Returns:** 0 if success, \< 0 on error.

### `sceMp3TermResource()`

```c
SceInt32 sceMp3TermResource(void);
```

sceMp3TermResource

**Returns:** 0 if success, \< 0 on error.

### `sceMp3Init()`

```c
SceInt32 sceMp3Init(SceInt32 handle);
```

sceMp3Init

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** 0 if success, \< 0 on error.

### `sceMp3Decode()`

```c
SceInt32 sceMp3Decode(SceInt32 handle, SceShort16 **dst);
```

sceMp3Decode

**Parameters:**

- `handle` – sceMp3 handle
- `dst` – Pointer to destination pcm samples buffer

**Returns:** number of bytes in decoded pcm buffer, \< 0 on error.

### `sceMp3GetInfoToAddStreamData()`

```c
SceInt32 sceMp3GetInfoToAddStreamData(SceInt32 handle, SceUChar8 **dst, SceInt32 *towrite, SceInt32 *srcpos);
```

sceMp3GetInfoToAddStreamData

**Parameters:**

- `handle` – sceMp3 handle
- `dst` – Pointer to stream data buffer
- `towrite` – Space remaining in stream data buffer
- `srcpos` – Position in source stream to start reading from

**Returns:** 0 if success, \< 0 on error.

### `sceMp3NotifyAddStreamData()`

```c
SceInt32 sceMp3NotifyAddStreamData(SceInt32 handle, SceInt32 size);
```

sceMp3NotifyAddStreamData

**Parameters:**

- `handle` – sceMp3 handle
- `size` – number of bytes added to the stream data buffer

**Returns:** 0 if success, \< 0 on error.

### `sceMp3CheckStreamDataNeeded()`

```c
SceInt32 sceMp3CheckStreamDataNeeded(SceInt32 handle);
```

sceMp3CheckStreamDataNeeded

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** 1 if more stream data is needed, \< 0 on error.

### `sceMp3SetLoopNum()`

```c
SceInt32 sceMp3SetLoopNum(SceInt32 handle, SceInt32 loop);
```

sceMp3SetLoopNum

**Parameters:**

- `handle` – sceMp3 handle
- `loop` – Number of loops

**Returns:** 0 if success, \< 0 on error.

### `sceMp3GetLoopNum()`

```c
SceInt32 sceMp3GetLoopNum(SceInt32 handle);
```

sceMp3GetLoopNum

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Number of loops, \< 0 on error.

### `sceMp3GetSumDecodedSample()`

```c
SceInt32 sceMp3GetSumDecodedSample(SceInt32 handle);
```

sceMp3GetSumDecodedSample

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Number of decoded samples, \< 0 on error.

### `sceMp3GetMaxOutputSample()`

```c
SceInt32 sceMp3GetMaxOutputSample(SceInt32 handle);
```

sceMp3GetMaxOutputSample

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Number of max samples to output, \< 0 on error.

### `sceMp3GetSamplingRate()`

```c
SceInt32 sceMp3GetSamplingRate(SceInt32 handle);
```

sceMp3GetSamplingRate

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Sampling rate of the mp3, \< 0 on error.

### `sceMp3GetBitRate()`

```c
SceInt32 sceMp3GetBitRate(SceInt32 handle);
```

sceMp3GetBitRate

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Bitrate of the mp3, \< 0 on error.

### `sceMp3GetMp3ChannelNum()`

```c
SceInt32 sceMp3GetMp3ChannelNum(SceInt32 handle);
```

sceMp3GetMp3ChannelNum

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Number of channels of the mp3, \< 0 on error.

### `sceMp3ResetPlayPosition()`

```c
SceInt32 sceMp3ResetPlayPosition(SceInt32 handle);
```

sceMp3ResetPlayPosition

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** 0 if success, \< 0 on error.

### `sceMp3GetFrameNum()`

```c
SceInt32 sceMp3GetFrameNum(SceInt32 handle);
```

sceMp3GetFrameNum

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** Number of audio frames, \< 0 on error

### `sceMp3ResetPlayPositionByFrame()`

```c
SceInt32 sceMp3ResetPlayPositionByFrame(SceInt32 handle, SceUInt32 frame);
```

sceMp3ResetPlayPositionByFrame

**Parameters:**

- `handle` – sceMp3 handle
- `frame` – frame

**Returns:** 0 if success, \< 0 on error.

### `sceMp3GetMPEGVersion()`

```c
SceInt32 sceMp3GetMPEGVersion(SceInt32 handle);
```

sceMp3GetMPEGVersion

**Parameters:**

- `handle` – sceMp3 handle

**Returns:** MPEG Version, \< 0 on error

### `sceMp3LowLevelInit()`

```c
SceInt32 sceMp3LowLevelInit(SceInt32 handle, SceUChar8 *src);
```

sceMp3LowLevelInit

**Parameters:**

- `handle` – sceMp3 handle
- `src` – Pointer to a buffer to contain raw mp3 stream data

**Returns:** 0 if success, \< 0 on error.

### `sceMp3LowLevelDecode()`

```c
SceInt32 sceMp3LowLevelDecode(SceInt32 handle, SceUChar8 *mp3src, SceUInt32 *mp3srcused, SceShort16 *pcmdst, SceUInt32 *pcmdstoutsz);
```

sceMp3LowLevelDecode

**Parameters:**

- `handle` – sceMp3 handle
- `mp3src` – Pointer to a buffer to contain raw mp3 stream data
- `mp3srcused` – mp3 data size consumed by decoding
- `pcmdst` – Pointer to destination pcm samples buffer
- `pcmdstoutsz` – Size of pcm data output by decoding

**Returns:** 0 if success, \< 0 on error.

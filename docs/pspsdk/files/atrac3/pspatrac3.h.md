[PSPSDK documentation](../../README.md) › Files

# atrac3/pspatrac3.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct PspBufferInfo`

```c
struct PspBufferInfo {
    u8 * pucWritePositionFirstBuf;
    u32 uiWritableByteFirstBuf;
    u32 uiMinWriteByteFirstBuf;
    u32 uiReadPositionFirstBuf;
    u8 * pucWritePositionSecondBuf;
    u32 uiWritableByteSecondBuf;
    u32 uiMinWriteByteSecondBuf;
    u32 uiReadPositionSecondBuf;
};
```

## Macros

### `PSP_ATRAC_SUCCESS`

```c
#define PSP_ATRAC_SUCCESS SCE_OK
```

### `PSP_ATRAC_ERROR_PARAM_FAIL`

```c
#define PSP_ATRAC_ERROR_PARAM_FAIL (0x80630001)
```

### `PSP_ATRAC_ERROR_API_FAIL`

```c
#define PSP_ATRAC_ERROR_API_FAIL (0x80630002)
```

### `PSP_ATRAC_ERROR_NO_ATRACID`

```c
#define PSP_ATRAC_ERROR_NO_ATRACID (0x80630003)
```

### `PSP_ATRAC_ERROR_BAD_CODECTYPE`

```c
#define PSP_ATRAC_ERROR_BAD_CODECTYPE (0x80630004)
```

### `PSP_ATRAC_ERROR_BAD_ATRACID`

```c
#define PSP_ATRAC_ERROR_BAD_ATRACID (0x80630005)
```

### `PSP_ATRAC_ERROR_UNKNOWN_FORMAT`

```c
#define PSP_ATRAC_ERROR_UNKNOWN_FORMAT (0x80630006)
```

### `PSP_ATRAC_ERROR_UNMATCH_FORMAT`

```c
#define PSP_ATRAC_ERROR_UNMATCH_FORMAT (0x80630007)
```

### `PSP_ATRAC_ERROR_BAD_DATA`

```c
#define PSP_ATRAC_ERROR_BAD_DATA (0x80630008)
```

### `PSP_ATRAC_ERROR_ALLDATA_IS_ONMEMORY`

```c
#define PSP_ATRAC_ERROR_ALLDATA_IS_ONMEMORY (0x80630009)
```

### `PSP_ATRAC_ERROR_UNSET_DATA`

```c
#define PSP_ATRAC_ERROR_UNSET_DATA (0x80630010)
```

### `PSP_ATRAC_ERROR_READSIZE_IS_TOO_SMALL`

```c
#define PSP_ATRAC_ERROR_READSIZE_IS_TOO_SMALL (0x80630011)
```

### `PSP_ATRAC_ERROR_NEED_SECOND_BUFFER`

```c
#define PSP_ATRAC_ERROR_NEED_SECOND_BUFFER (0x80630012)
```

### `PSP_ATRAC_ERROR_READSIZE_OVER_BUFFER`

```c
#define PSP_ATRAC_ERROR_READSIZE_OVER_BUFFER (0x80630013)
```

### `PSP_ATRAC_ERROR_NOT_4BYTE_ALIGNMENT`

```c
#define PSP_ATRAC_ERROR_NOT_4BYTE_ALIGNMENT (0x80630014)
```

### `PSP_ATRAC_ERROR_BAD_SAMPLE`

```c
#define PSP_ATRAC_ERROR_BAD_SAMPLE (0x80630015)
```

### `PSP_ATRAC_ERROR_WRITEBYTE_FIRST_BUFFER`

```c
#define PSP_ATRAC_ERROR_WRITEBYTE_FIRST_BUFFER (0x80630016)
```

### `PSP_ATRAC_ERROR_WRITEBYTE_SECOND_BUFFER`

```c
#define PSP_ATRAC_ERROR_WRITEBYTE_SECOND_BUFFER (0x80630017)
```

### `PSP_ATRAC_ERROR_ADD_DATA_IS_TOO_BIG`

```c
#define PSP_ATRAC_ERROR_ADD_DATA_IS_TOO_BIG (0x80630018)
```

### `PSP_ATRAC_ERROR_UNSET_PARAM`

```c
#define PSP_ATRAC_ERROR_UNSET_PARAM (0x80630021)
```

### `PSP_ATRAC_ERROR_NONEED_SECOND_BUFFER`

```c
#define PSP_ATRAC_ERROR_NONEED_SECOND_BUFFER (0x80630022)
```

### `PSP_ATRAC_ERROR_NODATA_IN_BUFFER`

```c
#define PSP_ATRAC_ERROR_NODATA_IN_BUFFER (0x80630023)
```

### `PSP_ATRAC_ERROR_ALLDATA_WAS_DECODED`

```c
#define PSP_ATRAC_ERROR_ALLDATA_WAS_DECODED (0x80630024)
```

### `PSP_ATRAC_AT3PLUS`

```c
#define PSP_ATRAC_AT3PLUS (0x00001000)
```

### `PSP_ATRAC_AT3`

```c
#define PSP_ATRAC_AT3 (0x00001001)
```

### `PSP_ATRAC_ALLDATA_IS_ON_MEMORY`

```c
#define PSP_ATRAC_ALLDATA_IS_ON_MEMORY (-1)
```

### `PSP_ATRAC_NONLOOP_STREAM_DATA_IS_ON_MEMORY`

```c
#define PSP_ATRAC_NONLOOP_STREAM_DATA_IS_ON_MEMORY (-2)
```

### `PSP_ATRAC_LOOP_STREAM_DATA_IS_ON_MEMORY`

```c
#define PSP_ATRAC_LOOP_STREAM_DATA_IS_ON_MEMORY (-3)
```

## Functions

### `sceAtracGetAtracID()`

```c
int sceAtracGetAtracID(u32 uiCodecType);
```

### `sceAtracSetDataAndGetID()`

```c
int sceAtracSetDataAndGetID(void *buf, SceSize bufsize);
```

Creates a new Atrac ID from the specified data.

**Parameters:**

- `buf` – the buffer holding the atrac3 data, including the RIFF/WAVE header.
- `bufsize` – the size of the buffer pointed by buf

**Returns:** the new atrac ID, or \< 0 on error

### `sceAtracDecodeData()`

```c
int sceAtracDecodeData(int atracID, u16 *outSamples, int *outN, int *outEnd, int *outRemainFrame);
```

Decode a frame of data.

**Parameters:**

- `atracID` – the atrac ID
- `outSamples` – pointer to a buffer that receives the decoded data of the current frame
- `outN` – pointer to a integer that receives the number of audio samples of the decoded frame
- `outEnd` – pointer to a integer that receives a boolean value indicating if the decoded frame is the last one
- `outRemainFrame` – pointer to a integer that receives either -1 if all at3 data is already on memory, or the remaining (not decoded yet) frames at memory if not all at3 data is on memory

**Returns:** \< 0 on error, otherwise 0

### `sceAtracGetRemainFrame()`

```c
int sceAtracGetRemainFrame(int atracID, int *outRemainFrame);
```

Gets the remaining (not decoded) number of frames.

**Parameters:**

- `atracID` – the atrac ID
- `outRemainFrame` – pointer to a integer that receives either -1 if all at3 data is already on memory, or the remaining (not decoded yet) frames at memory if not all at3 data is on memory

**Returns:** \< 0 on error, otherwise 0

### `sceAtracGetStreamDataInfo()`

```c
int sceAtracGetStreamDataInfo(int atracID, u8 **writePointer, u32 *availableBytes, u32 *readOffset);
```

**Parameters:**

- `atracID` – the atrac ID
- `writePointer` – Pointer to where to read the atrac data
- `availableBytes` – Number of bytes available at the writePointer location
- `readOffset` – Offset where to seek into the atrac file before reading

**Returns:** \< 0 on error, otherwise 0

### `sceAtracAddStreamData()`

```c
int sceAtracAddStreamData(int atracID, unsigned int bytesToAdd);
```

**Parameters:**

- `atracID` – the atrac ID
- `bytesToAdd` – Number of bytes read into location given by [sceAtracGetStreamDataInfo()](#sceatracgetstreamdatainfo).

**Returns:** \< 0 on error, otherwise 0

### `sceAtracGetBitrate()`

```c
int sceAtracGetBitrate(int atracID, int *outBitrate);
```

Gets the bitrate.

**Parameters:**

- `atracID` – the atracID
- `outBitrate` – pointer to a integer that receives the bitrate in kbps

**Returns:** \< 0 on error, otherwise 0

### `sceAtracSetLoopNum()`

```c
int sceAtracSetLoopNum(int atracID, int nloops);
```

Sets the number of loops for this atrac ID.

**Parameters:**

- `atracID` – the atracID
- `nloops` – the number of loops to set

**Returns:** \< 0 on error, otherwise 0

### `sceAtracReleaseAtracID()`

```c
int sceAtracReleaseAtracID(int atracID);
```

It releases an atrac ID.

**Parameters:**

- `atracID` – the atrac ID to release

**Returns:** \< 0 on error

### `sceAtracGetNextSample()`

```c
int sceAtracGetNextSample(int atracID, int *outN);
```

Gets the number of samples of the next frame to be decoded.

**Parameters:**

- `atracID` – the atrac ID
- `outN` – pointer to receives the number of samples of the next frame.

**Returns:** \< 0 on error, otherwise 0

### `sceAtracGetMaxSample()`

```c
int sceAtracGetMaxSample(int atracID, int *outMax);
```

Gets the maximum number of samples of the atrac3 stream.

**Parameters:**

- `atracID` – the atrac ID
- `outMax` – pointer to a integer that receives the maximum number of samples.

**Returns:** \< 0 on error, otherwise 0

### `sceAtracGetBufferInfoForReseting()`

```c
int sceAtracGetBufferInfoForReseting(int atracID, u32 uiSample, PspBufferInfo *pBufferInfo);
```

### `sceAtracGetChannel()`

```c
int sceAtracGetChannel(int atracID, u32 *puiChannel);
```

### `sceAtracGetInternalErrorInfo()`

```c
int sceAtracGetInternalErrorInfo(int atracID, int *piResult);
```

### `sceAtracGetLoopStatus()`

```c
int sceAtracGetLoopStatus(int atracID, int *piLoopNum, u32 *puiLoopStatus);
```

### `sceAtracGetNextDecodePosition()`

```c
int sceAtracGetNextDecodePosition(int atracID, u32 *puiSamplePosition);
```

### `sceAtracGetSecondBufferInfo()`

```c
int sceAtracGetSecondBufferInfo(int atracID, u32 *puiPosition, u32 *puiDataByte);
```

### `sceAtracGetSoundSample()`

```c
int sceAtracGetSoundSample(int atracID, int *piEndSample, int *piLoopStartSample, int *piLoopEndSample);
```

### `sceAtracResetPlayPosition()`

```c
int sceAtracResetPlayPosition(int atracID, u32 uiSample, u32 uiWriteByteFirstBuf, u32 uiWriteByteSecondBuf);
```

### `sceAtracSetData()`

```c
int sceAtracSetData(int atracID, u8 *pucBufferAddr, u32 uiBufferByte);
```

### `sceAtracSetHalfwayBuffer()`

```c
int sceAtracSetHalfwayBuffer(int atracID, u8 *pucBufferAddr, u32 uiReadByte, u32 uiBufferByte);
```

### `sceAtracSetHalfwayBufferAndGetID()`

```c
int sceAtracSetHalfwayBufferAndGetID(u8 *pucBufferAddr, u32 uiReadByte, u32 uiBufferByte);
```

### `sceAtracSetSecondBuffer()`

```c
int sceAtracSetSecondBuffer(int atracID, u8 *pucSecondBufferAddr, u32 uiSecondBufferByte);
```

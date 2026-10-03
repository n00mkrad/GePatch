[PSPSDK documentation](../../README.md) › Files

# audio/pspaudiocodec.h

## Macros

### `PSP_CODEC_AT3PLUS`

```c
#define PSP_CODEC_AT3PLUS (0x00001000)
```

### `PSP_CODEC_AT3`

```c
#define PSP_CODEC_AT3 (0x00001001)
```

### `PSP_CODEC_MP3`

```c
#define PSP_CODEC_MP3 (0x00001002)
```

### `PSP_CODEC_AAC`

```c
#define PSP_CODEC_AAC (0x00001003)
```

## Functions

### `sceAudiocodecCheckNeedMem()`

```c
int sceAudiocodecCheckNeedMem(unsigned long *Buffer, int Type);
```

### `sceAudiocodecInit()`

```c
int sceAudiocodecInit(unsigned long *Buffer, int Type);
```

### `sceAudiocodecDecode()`

```c
int sceAudiocodecDecode(unsigned long *Buffer, int Type);
```

### `sceAudiocodecGetEDRAM()`

```c
int sceAudiocodecGetEDRAM(unsigned long *Buffer, int Type);
```

### `sceAudiocodecReleaseEDRAM()`

```c
int sceAudiocodecReleaseEDRAM(unsigned long *Buffer);
```

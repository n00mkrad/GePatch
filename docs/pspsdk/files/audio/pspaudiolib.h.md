[PSPSDK documentation](../../README.md) › Files

# audio/pspaudiolib.h

## Data Structures

### `struct psp_audio_channelinfo`

```c
struct psp_audio_channelinfo {
    int threadhandle;
    int handle;
    int volumeleft;
    int volumeright;
    pspAudioCallback_t callback;
    void * pdata;
};
```

## Macros

### `PSP_NUM_AUDIO_CHANNELS`

```c
#define PSP_NUM_AUDIO_CHANNELS 4
```

### `PSP_NUM_AUDIO_SAMPLES`

```c
#define PSP_NUM_AUDIO_SAMPLES 1024
```

This is the number of frames you can update per callback, a frame being 1 sample for mono, 2 samples for stereo etc.

### `PSP_VOLUME_MAX`

```c
#define PSP_VOLUME_MAX 0x8000
```

## Typedefs

### `pspAudioCallback_t`

```c
typedef void(* pspAudioCallback_t) (void *buf, unsigned int reqn, void *pdata))(void *buf, unsigned int reqn, void *pdata);
```

### `pspAudioThreadfunc_t`

```c
typedef int(* pspAudioThreadfunc_t) (int args, void *argp))(int args, void *argp);
```

## Functions

### `pspAudioInit()`

```c
int pspAudioInit();
```

### `pspAudioEndPre()`

```c
void pspAudioEndPre();
```

### `pspAudioEnd()`

```c
void pspAudioEnd();
```

### `pspAudioSetVolume()`

```c
void pspAudioSetVolume(int channel, int left, int right);
```

### `pspAudioGetVolume()`

```c
void pspAudioGetVolume(int channel, int *left, int *right);
```

### `pspAudioSetChannelCallback()`

```c
void pspAudioSetChannelCallback(int channel, pspAudioCallback_t callback, void *pdata);
```

### `pspAudioGetChannelCallback()`

```c
void pspAudioGetChannelCallback(int channel, pspAudioCallback_t *callback, void **pdata);
```

### `pspAudioOutBlocking()`

```c
int pspAudioOutBlocking(unsigned int channel, unsigned int vol1, unsigned int vol2, void *buf);
```

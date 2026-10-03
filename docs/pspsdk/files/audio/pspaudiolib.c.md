[PSPSDK documentation](../../README.md) › Files

# audio/pspaudiolib.c

```c
#include <stdlib.h>
#include <string.h>
#include <pspthreadman.h>
#include <pspaudio.h>
#include "pspaudiolib.h"
```

## Functions

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

### `AudioChannelThread()`

```c
static int AudioChannelThread(int args, void *argp);
```

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

## Variables

### `audio_ready`

```c
int audio_ready =0;
```

### `audio_sndbuf`

```c
short audio_sndbuf[4][2][1024][2][4][2][1024][2];
```

### `AudioStatus`

```c
psp_audio_channelinfo AudioStatus[4][4];
```

### `audio_terminate`

```c
volatile int audio_terminate =0;
```

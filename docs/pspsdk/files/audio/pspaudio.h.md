[PSPSDK documentation](../../README.md) › Files

# audio/pspaudio.h

## Data Structures

### `struct pspAudioInputParams`

| Field | Description |
|---|---|
| `int unknown1` | Unknown.<br>Pass 0 |
| `int gain` |  |
| `int unknown2` | Unknown.<br>Pass 0 |
| `int unknown3` | Unknown.<br>Pass 0 |
| `int unknown4` | Unknown.<br>Pass 0 |
| `int unknown5` | Unknown.<br>Pass 0 |

## Macros

### `PSP_AUDIO_VOLUME_MAX`

```c
#define PSP_AUDIO_VOLUME_MAX 0x8000
```

The maximum output volume.

### `PSP_AUDIO_CHANNEL_MAX`

```c
#define PSP_AUDIO_CHANNEL_MAX 8
```

The maximum number of hardware channels.

### `PSP_AUDIO_NEXT_CHANNEL`

```c
#define PSP_AUDIO_NEXT_CHANNEL (-1)
```

Used to request the next available hardware channel.

### `SCE_AUDIO_ERROR_NOT_INITIALIZED`

```c
#define SCE_AUDIO_ERROR_NOT_INITIALIZED (0x80260001)
```

Error codes used as return values for the Audio Driver.

### `SCE_AUDIO_ERROR_OUTPUT_BUSY`

```c
#define SCE_AUDIO_ERROR_OUTPUT_BUSY (0x80260002)
```

### `SCE_AUDIO_ERROR_INVALID_CH`

```c
#define SCE_AUDIO_ERROR_INVALID_CH (0x80260003)
```

### `SCE_AUDIO_ERROR_PRIV_REQUIRED`

```c
#define SCE_AUDIO_ERROR_PRIV_REQUIRED (0x80260004)
```

### `SCE_AUDIO_ERROR_NOT_FOUND`

```c
#define SCE_AUDIO_ERROR_NOT_FOUND (0x80260005)
```

### `SCE_AUDIO_ERROR_INVALID_SIZE`

```c
#define SCE_AUDIO_ERROR_INVALID_SIZE (0x80260006)
```

### `SCE_AUDIO_ERROR_INVALID_FORMAT`

```c
#define SCE_AUDIO_ERROR_INVALID_FORMAT (0x80260007)
```

### `SCE_AUDIO_ERROR_NOT_RESERVED`

```c
#define SCE_AUDIO_ERROR_NOT_RESERVED (0x80260008)
```

### `SCE_AUDIO_ERROR_NOT_OUTPUT`

```c
#define SCE_AUDIO_ERROR_NOT_OUTPUT (0x80260009)
```

### `SCE_AUDIO_ERROR_INVALID_FREQUENCY`

```c
#define SCE_AUDIO_ERROR_INVALID_FREQUENCY (0x8026000A)
```

### `SCE_AUDIO_ERROR_INVALID_VOLUME`

```c
#define SCE_AUDIO_ERROR_INVALID_VOLUME (0x8026000B)
```

### `SCE_AUDIO_ERROR_INPUT_BUSY`

```c
#define SCE_AUDIO_ERROR_INPUT_BUSY (0x80260010)
```

### `PSP_AUDIO_SAMPLE_MIN`

```c
#define PSP_AUDIO_SAMPLE_MIN 64
```

The minimum number of samples that can be allocated to a channel.

### `PSP_AUDIO_SAMPLE_MAX`

```c
#define PSP_AUDIO_SAMPLE_MAX 65472
```

The maximum number of samples that can be allocated to a channel.

### `PSP_AUDIO_SAMPLE_ALIGN()`

```c
#define PSP_AUDIO_SAMPLE_ALIGN(s) (((s) + 63) & ~63)
```

Make the given sample count a multiple of 64.

## Enumerations

### `enum PspAudioFormats`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_AUDIO_FORMAT_STEREO` | `0` | Channel is set to stereo output. |
| `PSP_AUDIO_FORMAT_MONO` | `0x10` | Channel is set to mono output. |

## Functions

### `sceAudioChReserve()`

```c
int sceAudioChReserve(int channel, int samplecount, int format);
```

Allocate and initialize a hardware output channel.

**Parameters:**

- `channel` – Use a value between 0 - 7 to reserve a specific channel. Pass PSP_AUDIO_NEXT_CHANNEL to get the first available channel.
- `samplecount` – The number of samples that can be output on the channel per output call. It must be a value between [PSP_AUDIO_SAMPLE_MIN](#psp_audio_sample_min) and [PSP_AUDIO_SAMPLE_MAX](#psp_audio_sample_max), and it must be aligned to 64 bytes (use the [PSP_AUDIO_SAMPLE_ALIGN](#psp_audio_sample_align) macro to align it).
- `format` – The output format to use for the channel. One of [PspAudioFormats](#enum-pspaudioformats).

**Returns:** The channel number on success, an error code if less than 0.

### `sceAudioChRelease()`

```c
int sceAudioChRelease(int channel);
```

Release a hardware output channel.

**Parameters:**

- `channel` – The channel to release.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput()`

```c
int sceAudioOutput(int channel, int vol, void *buf);
```

Output audio of the specified channel.

**Parameters:**

- `channel` – The channel number.
- `vol` – The volume.
- `buf` – Pointer to the PCM data to output.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutputBlocking()`

```c
int sceAudioOutputBlocking(int channel, int vol, void *buf);
```

Output audio of the specified channel (blocking)

**Parameters:**

- `channel` – The channel number.
- `vol` – The volume.
- `buf` – Pointer to the PCM data to output.

**Returns:** number of queued samples on success, an error if less than 0.

### `sceAudioOutputPanned()`

```c
int sceAudioOutputPanned(int channel, int leftvol, int rightvol, void *buf);
```

Output panned audio of the specified channel.

**Parameters:**

- `channel` – The channel number.
- `leftvol` – The left volume.
- `rightvol` – The right volume.
- `buf` – Pointer to the PCM data to output.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutputPannedBlocking()`

```c
int sceAudioOutputPannedBlocking(int channel, int leftvol, int rightvol, void *buf);
```

Output panned audio of the specified channel (blocking)

**Parameters:**

- `channel` – The channel number.
- `leftvol` – The left volume.
- `rightvol` – The right volume.
- `buf` – Pointer to the PCM data to output.

**Returns:** number of queued samples on success, an error if less than 0.

### `sceAudioGetChannelRestLen()`

```c
int sceAudioGetChannelRestLen(int channel);
```

Get count of unplayed samples remaining.

**Parameters:**

- `channel` – The channel number.

**Returns:** Number of samples to be played, an error if less than 0.

### `sceAudioGetChannelRestLength()`

```c
int sceAudioGetChannelRestLength(int channel);
```

Get count of unplayed samples remaining.

**Parameters:**

- `channel` – The channel number.

**Returns:** Number of samples to be played, an error if less than 0.

### `sceAudioSetChannelDataLen()`

```c
int sceAudioSetChannelDataLen(int channel, int samplecount);
```

Change the output sample count, after it's already been reserved.

**Parameters:**

- `channel` – The channel number.
- `samplecount` – The number of samples to output in one output call.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioChangeChannelConfig()`

```c
int sceAudioChangeChannelConfig(int channel, int format);
```

Change the format of a channel.

**Parameters:**

- `channel` – The channel number.
- `format` – One of [PspAudioFormats](#enum-pspaudioformats)

**Returns:** 0 on success, an error if less than 0.

### `sceAudioChangeChannelVolume()`

```c
int sceAudioChangeChannelVolume(int channel, int leftvol, int rightvol);
```

Change the volume of a channel.

**Parameters:**

- `channel` – The channel number.
- `leftvol` – The left volume.
- `rightvol` – The right volume.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput2Reserve()`

```c
int sceAudioOutput2Reserve(int samplecount);
```

Reserve the audio output and set the output sample count.

**Parameters:**

- `samplecount` – The number of samples to output in one output call (min 17, max 4111).

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput2Release()`

```c
int sceAudioOutput2Release(void);
```

Release the audio output.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput2ChangeLength()`

```c
int sceAudioOutput2ChangeLength(int samplecount);
```

Change the output sample count, after it's already been reserved.

**Parameters:**

- `samplecount` – The number of samples to output in one output call (min 17, max 4111).

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput2OutputBlocking()`

```c
int sceAudioOutput2OutputBlocking(int vol, void *buf);
```

Output audio (blocking)

**Parameters:**

- `vol` – The volume.
- `buf` – Pointer to the PCM data.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioOutput2GetRestSample()`

```c
int sceAudioOutput2GetRestSample(void);
```

Get count of unplayed samples remaining.

**Returns:** Number of samples to be played, an error if less than 0.

### `sceAudioSRCChReserve()`

```c
int sceAudioSRCChReserve(int samplecount, int freq, int channels);
```

Reserve the audio output.

**Parameters:**

- `samplecount` – The number of samples to output in one output call (min 17, max 4111).
- `freq` – The frequency. One of 48000, 44100, 32000, 24000, 22050, 16000, 12000, 11050, 8000.
- `channels` – Number of channels. Pass 2 (stereo).

**Returns:** 0 on success, an error if less than 0.

### `sceAudioSRCChRelease()`

```c
int sceAudioSRCChRelease(void);
```

Release the audio output.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioSRCOutputBlocking()`

```c
int sceAudioSRCOutputBlocking(int vol, void *buf);
```

Output audio.

**Parameters:**

- `vol` – The volume.
- `buf` – Pointer to the PCM data to output.

**Returns:** number of queued samples on success, an error if less than 0.

### `sceAudioInputInit()`

```c
int sceAudioInputInit(int unknown1, int gain, int unknown2);
```

Init audio input.

**Parameters:**

- `unknown1` – Unknown. Pass 0.
- `gain` – Gain.
- `unknown2` – Unknown. Pass 0.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioInputInitEx()`

```c
int sceAudioInputInitEx(pspAudioInputParams *params);
```

Init audio input (with extra arguments)

**Parameters:**

- `params` – A pointer to a [pspAudioInputParams](#struct-pspaudioinputparams) struct.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioInputBlocking()`

```c
int sceAudioInputBlocking(int samplecount, int freq, void *buf);
```

Perform audio input (blocking)

**Parameters:**

- `samplecount` – Number of samples.
- `freq` – Either 44100, 22050 or 11025.
- `buf` – Pointer to where the audio data will be stored.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioInput()`

```c
int sceAudioInput(int samplecount, int freq, void *buf);
```

Perform audio input.

**Parameters:**

- `samplecount` – Number of samples.
- `freq` – Either 44100, 22050 or 11025.
- `buf` – Pointer to where the audio data will be stored.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioGetInputLength()`

```c
int sceAudioGetInputLength(void);
```

Get the number of samples that were acquired.

**Returns:** Number of samples acquired, an error if less than 0.

### `sceAudioWaitInputEnd()`

```c
int sceAudioWaitInputEnd(void);
```

Wait for non-blocking audio input to complete.

**Returns:** 0 on success, an error if less than 0.

### `sceAudioPollInputEnd()`

```c
int sceAudioPollInputEnd(void);
```

Poll for non-blocking audio input status.

**Returns:** 0 if input has completed, 1 if not completed or an error if less than 0.

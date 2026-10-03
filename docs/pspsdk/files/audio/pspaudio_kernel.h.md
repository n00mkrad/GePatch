[PSPSDK documentation](../../README.md) › Files

# audio/pspaudio_kernel.h

Topics: [User Audio Library](../../topics/Audio.md)

## Enumerations

### `enum PspAudioFrequencies`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_AUDIO_FREQ_44K` | `44100` | Sampling frequency set to 44100Hz. |
| `PSP_AUDIO_FREQ_48K` | `48000` | Sampling frequency set to 48000Hz. |

## Functions

### `sceAudioSetFrequency()`

```c
int sceAudioSetFrequency(int frequency);
```

Set audio sampling frequency.

**Parameters:**

- `frequency` – Sampling frequency to set audio output to - either 44100 or 48000.

**Returns:** 0 on success, an error if less than 0.

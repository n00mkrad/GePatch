[PSPSDK documentation](../../README.md) › Files

# vaudio/pspvaudio.h

## Macros

### `PSP_VAUDIO_VOLUME_MAX`

```c
#define PSP_VAUDIO_VOLUME_MAX 0x8000
```

The maximum output volume.

### `PSP_VAUDIO_SAMPLE_MAX`

```c
#define PSP_VAUDIO_SAMPLE_MAX 2048
```

The maximum number of samples that can be allocated to a channel.

### `PSP_VAUDIO_SAMPLE_MIN`

```c
#define PSP_VAUDIO_SAMPLE_MIN 256
```

The minimum number of samples that can be allocated to a channel.

### `PSP_VAUDIO_FORMAT_MONO`

```c
#define PSP_VAUDIO_FORMAT_MONO 1
```

Channel is set to mono output.

### `PSP_VAUDIO_FORMAT_STEREO`

```c
#define PSP_VAUDIO_FORMAT_STEREO 2
```

Channel is set to stereo output.

### `PSP_VAUDIO_EFFECT_OFF`

```c
#define PSP_VAUDIO_EFFECT_OFF 0
```

Effect type<br>

### `PSP_VAUDIO_EFFECT_HEAVY`

```c
#define PSP_VAUDIO_EFFECT_HEAVY 1
```

### `PSP_VAUDIO_EFFECT_POPS`

```c
#define PSP_VAUDIO_EFFECT_POPS 2
```

### `PSP_VAUDIO_EFFECT_JAZZ`

```c
#define PSP_VAUDIO_EFFECT_JAZZ 3
```

### `PSP_VAUDIO_EFFECT_UNIQUE`

```c
#define PSP_VAUDIO_EFFECT_UNIQUE 4
```

### `PSP_VAUDIO_EFFECT_MAX`

```c
#define PSP_VAUDIO_EFFECT_MAX 5
```

### `PSP_VAUDIO_ALC_OFF`

```c
#define PSP_VAUDIO_ALC_OFF 0
```

Alc mode<br>

### `PSP_VAUDIO_ALC_MODE1`

```c
#define PSP_VAUDIO_ALC_MODE1 1
```

### `PSP_VAUDIO_ALC_MODE_MAX`

```c
#define PSP_VAUDIO_ALC_MODE_MAX 2
```

## Functions

### `sceVaudioOutputBlocking()`

```c
int sceVaudioOutputBlocking(int volume, void *buffer);
```

Output audio (blocking)

**Parameters:**

- `volume` – It must be a value between 0 and [PSP_VAUDIO_VOLUME_MAX](#psp_vaudio_volume_max)
- `buffer` – Pointer to the PCM data to output.

**Returns:** 0 on success, an error if less than 0.

### `sceVaudioChReserve()`

```c
int sceVaudioChReserve(int samplecount, int frequency, int format);
```

Allocate and initialize a virtual output channel.

**Parameters:**

- `samplecount` – The number of samples that can be output on the channel per output call. One of 256, 576, 1024, 1152, 2048. It must be a value between [PSP_VAUDIO_SAMPLE_MIN](#psp_vaudio_sample_min) and [PSP_VAUDIO_SAMPLE_MAX](#psp_vaudio_sample_max).
- `frequency` – The frequency. One of 48000, 44100, 32000, 24000, 22050, 16000, 12000, 11050, 8000.
- `format` – The output format to use for the channel. One of [PSP_VAUDIO_FORMAT_MONO](#psp_vaudio_format_mono) or [PSP_VAUDIO_FORMAT_STEREO](#psp_vaudio_format_stereo)

**Returns:** 0 if success, \< 0 on error.

### `sceVaudioChRelease()`

```c
int sceVaudioChRelease(void);
```

Release a virtual output channel.

**Returns:** 0 if success, \< 0 on error.

### `sceVaudioSetEffectType()`

```c
int sceVaudioSetEffectType(int effect, int volume);
```

Set effect type.

**Parameters:**

- `effect` – The effect type. One of [PSP_VAUDIO_EFFECT_OFF](#psp_vaudio_effect_off) or [PSP_VAUDIO_EFFECT_HEAVY](#psp_vaudio_effect_heavy) or [PSP_VAUDIO_EFFECT_POPS](#psp_vaudio_effect_pops) or [PSP_VAUDIO_EFFECT_JAZZ](#psp_vaudio_effect_jazz) or [PSP_VAUDIO_EFFECT_UNIQUE](#psp_vaudio_effect_unique) or [PSP_VAUDIO_EFFECT_MAX](#psp_vaudio_effect_max)
- `volume` – The volume. It must be a value between 0 and [PSP_VAUDIO_VOLUME_MAX](#psp_vaudio_volume_max)

**Returns:** The volume value on success, \< 0 on error.

### `sceVaudioSetAlcMode()`

```c
int sceVaudioSetAlcMode(int mode);
```

Set ALC(dynamic normalizer)

**Parameters:**

- `mode` – The mode. One of [PSP_VAUDIO_ALC_OFF](#psp_vaudio_alc_off) or [PSP_VAUDIO_ALC_MODE1](#psp_vaudio_alc_mode1) or [PSP_VAUDIO_ALC_MODE_MAX](#psp_vaudio_alc_mode_max)

**Returns:** 0 if success, \< 0 on error.

[PSPSDK documentation](../../README.md) › Files

# sascore/pspsascore.h

```c
#include <psptypes.h>
```

Topics: [SAS Core Audio Library](../../topics/SAS.md)

## Data Structures

### `struct SceSasCore`

Contains all data related to a sceSasCore state.

Developers are not meant to interact with this structure directly. Always prefer to use the public functions over reading/writing values from here.

```c
struct SceSasCore {
    u8 pad[3616];
};
```

## Macros

### `PSP_SAS_GET_VOICE_BIT()`

```c
#define PSP_SAS_GET_VOICE_BIT(voice) (1u << (voice % 32))
```

Macro utility to obtain the corresponding bit of a voice index.

**Parameters:**

- `voice` – The voice index, ranging from 0 to [PSP_SAS_VOICES_MAX](#psp_sas_voices_max)-1

### `PSP_SAS_GET_FLAG_AT()`

```c
#define PSP_SAS_GET_FLAG_AT(flags, voice) (((flags) & (PSP_SAS_GET_VOICE_BIT(voice))) != 0)
```

Macro utility for reading voice bitfield flags.

**Parameters:**

- `flags` – The 32-bit bitfield representing each voice.
- `voice` – The voice index, ranging from 0 to [PSP_SAS_VOICES_MAX](#psp_sas_voices_max)-1

### `PSP_SAS_GRAIN_SIZE`

```c
#define PSP_SAS_GRAIN_SIZE (256)
```

The recommended sceSasCore grain size that's used by most games.

### `PSP_SAS_GRAIN_SIZE_MIN`

```c
#define PSP_SAS_GRAIN_SIZE_MIN (64)
```

The minimum sceSasCore grain size.

### `PSP_SAS_GRAIN_SIZE_MAX`

```c
#define PSP_SAS_GRAIN_SIZE_MAX (2048)
```

The maximum sceSasCore grain size.

### `PSP_SAS_VOICES_MAX`

```c
#define PSP_SAS_VOICES_MAX (32)
```

The maximum number of voices that sceSas can playback all at once.

### `PSP_SAS_SAMPLE_RATE`

```c
#define PSP_SAS_SAMPLE_RATE (44100)
```

The sample rate of sceSasCore mixer.

### `PSP_SAS_VOLUME_MAX`

```c
#define PSP_SAS_VOLUME_MAX (0x1000)
```

The maximum output volume of sceSas voices.

### `PSP_SAS_PITCH_BASE`

```c
#define PSP_SAS_PITCH_BASE (0x1000)
```

Represents 1x voice pitch.

### `PSP_SAS_PITCH_MIN`

```c
#define PSP_SAS_PITCH_MIN (0x1)
```

The minimum supported voice pitch.

### `PSP_SAS_PITCH_MAX`

```c
#define PSP_SAS_PITCH_MAX (0x4000)
```

The maximum supported voice pitch.

### `PSP_SAS_NOISE_FREQ_MAX`

```c
#define PSP_SAS_NOISE_FREQ_MAX (0x3F)
```

The maximum noise frequency.

### `PSP_SAS_ENVELOPE_HEIGHT_MAX`

```c
#define PSP_SAS_ENVELOPE_HEIGHT_MAX (0x40000000)
```

Represents maximum ADSR envelope height.

### `PSP_SAS_ENVELOPE_FREQ_MAX`

```c
#define PSP_SAS_ENVELOPE_FREQ_MAX (0x7FFFFFFF)
```

Represents maximum ADSR envelope frequency.

### `PSP_SAS_ADSR_EVERYTHING`

```c
#define PSP_SAS_ADSR_EVERYTHING (PSP_SAS_ADSR_ATTACK | PSP_SAS_ADSR_DECAY | PSP_SAS_ADSR_SUSTAIN | PSP_SAS_ADSR_RELEASE)
```

## Enumerations

### `enum PspSasOutputModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SAS_OUTPUTMODE_STEREO` | `0` | Interleaved stereo output (L/R), with dry + send already mixed together. |
| `PSP_SAS_OUTPUTMODE_MULTICHANNEL` | `1` | 4 separate output buffers: L, R, Send-L, Send-R (each planar, not interleaved). |

### `enum PspSasEffectTypes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SAS_EFFECT_TYPE_OFF` | `-1` |  |
| `PSP_SAS_EFFECT_TYPE_ROOM` | `0` |  |
| `PSP_SAS_EFFECT_TYPE_SMALL` | `1` |  |
| `PSP_SAS_EFFECT_TYPE_MEDIUM` | `2` |  |
| `PSP_SAS_EFFECT_TYPE_LARGE` | `3` |  |
| `PSP_SAS_EFFECT_TYPE_HALL` | `4` |  |
| `PSP_SAS_EFFECT_TYPE_SPACE` | `5` |  |
| `PSP_SAS_EFFECT_TYPE_ECHO` | `6` |  |
| `PSP_SAS_EFFECT_TYPE_DELAY` | `7` |  |
| `PSP_SAS_EFFECT_TYPE_PIPE` | `8` |  |

### `enum PspSasADSRCurveModes`

ADSR envelope curve modes.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SAS_ADSR_CURVE_MODE_LINEAR_INCREASE` | `0` | Equivalent to `height += rate` |
| `PSP_SAS_ADSR_CURVE_MODE_LINEAR_DECREASE` | `1` | Equivalent to `height -= rate` |
| `PSP_SAS_ADSR_CURVE_MODE_LINEAR_BENT` | `2` |  |
| `PSP_SAS_ADSR_CURVE_MODE_EXPONENT_REV` | `3` |  |
| `PSP_SAS_ADSR_CURVE_MODE_EXPONENT` | `4` |  |
| `PSP_SAS_ADSR_CURVE_MODE_DIRECT` | `5` | Equivalent to `height = rate` |

### `enum PspSasErrorCodes`

Error codes used as return values by sceSasCore.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SAS_ERROR_ADDRESS` | `0x80420005` |  |
| `PSP_SAS_ERROR_VOICE_INDEX` | `0x80420010` |  |
| `PSP_SAS_ERROR_NOISE_CLOCK` | `0x80420011` |  |
| `PSP_SAS_ERROR_PITCH_VAL` | `0x80420012` |  |
| `PSP_SAS_ERROR_ADSR_MODE` | `0x80420013` |  |
| `PSP_SAS_ERROR_ADPCM_SIZE` | `0x80420014` |  |
| `PSP_SAS_ERROR_LOOP_MODE` | `0x80420015` |  |
| `PSP_SAS_ERROR_INVALID_STATE` | `0x80420016` |  |
| `PSP_SAS_ERROR_VOLUME_VAL` | `0x80420018` |  |
| `PSP_SAS_ERROR_ADSR_VAL` | `0x80420019` |  |
| `PSP_SAS_ERROR_FX_TYPE` | `0x80420020` |  |
| `PSP_SAS_ERROR_FX_FEEDBACK` | `0x80420021` |  |
| `PSP_SAS_ERROR_FX_DELAY` | `0x80420022` |  |
| `PSP_SAS_ERROR_FX_VOLUME_VAL` | `0x80420023` |  |
| `PSP_SAS_ERROR_BUSY` | `0x80420030` |  |
| `PSP_SAS_ERROR_NOTINIT` | `0x80420100` |  |
| `PSP_SAS_ERROR_ALRDYINIT` | `0x80420101` |  |

### `enum PspSasADSRFlags`

ADSR envelope flags.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_SAS_ADSR_ATTACK` | `1` |  |
| `PSP_SAS_ADSR_DECAY` | `2` |  |
| `PSP_SAS_ADSR_SUSTAIN` | `4` |  |
| `PSP_SAS_ADSR_RELEASE` | `8` |  |

## Functions

### `__sceSasInit()`

```c
int __sceSasInit(SceSasCore *core, int grainsize, int maxvoices, PspSasOutputModes outputmode, int samplerate);
```

Initializes a [SceSasCore](#struct-scesascore) instance.

Make sure to load [PSP_MODULE_AV_AVCODEC](../utility/psputility_modules.h.md#psp_module_av_avcodec) and [PSP_MODULE_AV_SASCORE](../utility/psputility_modules.h.md#psp_module_av_sascore) with [sceUtilityLoadModule](../utility/psputility_modules.h.md#sceutilityloadmodule) or [sceUtilityLoadAvModule](../utility/psputility_avmodules.h.md#sceutilityloadavmodule) before calling this function.

**Parameters:**

- `core` – Pointer to [SceSasCore](#struct-scesascore) for initialization. Must be 64-byte aligned.
- `grainsize` – Tells how many frames (samples per channel) the mixer will process and output per iteration. It must be a value between [PSP_SAS_GRAIN_SIZE_MIN](#psp_sas_grain_size_min) and [PSP_SAS_GRAIN_SIZE_MAX](#psp_sas_grain_size_max), and it must be a multiple of 64.
- `maxvoices` – The maximum number of voices [SceSasCore](#struct-scesascore) will process. It must be a number between 1 and [PSP_SAS_VOICES_MAX](#psp_sas_voices_max).
- `outputmode` – The output mode to use. One of [PspSasOutputModes](#enum-pspsasoutputmodes).
- `samplerate` – Must be [PSP_SAS_SAMPLE_RATE](#psp_sas_sample_rate) (44100). Any other value will result in an error.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasGetOutputmode()`

```c
int __sceSasGetOutputmode(SceSasCore *core);
```

Gets the current output mode from the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.

**Returns:** One of [PspSasOutputModes](#enum-pspsasoutputmodes) on success, an error code if less than 0.

### `__sceSasSetOutputmode()`

```c
int __sceSasSetOutputmode(SceSasCore *core, PspSasOutputModes outputmode);
```

Sets the current output mode of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `outputmode` – The output mode to use. One of [PspSasOutputModes](#enum-pspsasoutputmodes).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasRevType()`

```c
int __sceSasRevType(SceSasCore *core, PspSasEffectTypes type);
```

Sets the reverb effect of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `type` – The reverb effect to use. One of [PspSasEffectTypes](#enum-pspsaseffecttypes).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasRevEVOL()`

```c
int __sceSasRevEVOL(SceSasCore *core, int leftvol, int rightvol);
```

Sets the effect volume of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `leftvol` – Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).
- `rightvol` – Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasRevVON()`

```c
int __sceSasRevVON(SceSasCore *core, int dry, int wet);
```

Toggles dry and wet audio signals of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – A valid sceSas instance.
- `dry` – Enable/disable dry signal.
- `wet` – Enable/disable wet/send signal.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasRevParam()`

```c
int __sceSasRevParam(SceSasCore *core, int delay, int feedback);
```

Sets the effect delay and feedback parameters of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `delay` – Must be a number between 0 and 128.
- `feedback` – Must be a number between 0 and 128.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasGetGrain()`

```c
int __sceSasGetGrain(SceSasCore *core);
```

Gets the grain size of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.

**Returns:** The grain size on success, an error code if less than 0.

### `__sceSasSetGrain()`

```c
int __sceSasSetGrain(SceSasCore *core, int grainsize);
```

Sets the grain size of the [SceSasCore](#struct-scesascore) instance.

**Parameters:**

- `core` – A valid sceSas instance.
- `grainsize` – The new grain size to set. It must be a value between [PSP_SAS_GRAIN_SIZE_MIN](#psp_sas_grain_size_min) and [PSP_SAS_GRAIN_SIZE_MAX](#psp_sas_grain_size_max), and it must be a multiple of 64.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasGetEndFlag()`

```c
u32 __sceSasGetEndFlag(SceSasCore *core);
```

Gets the end status of the voices from an [SceSasCore](#struct-scesascore) nstance.

Each bit corresponds to a voice index:

- Bit N == 1 -> voice N has ended.
- Bit N == 0 -> voice N is currently playing.

**Note:** On real hardware, the end flags are refreshed only *AFTER* [\_\_sceSasCore](#__scesascore) is called.

**Parameters:**

- `core` – Pointer to a valid Sas instance

**Returns:** 32-bit bitmask of voice end flags. To read a specific voice bit, use [PSP_SAS_GET_FLAG_AT](#psp_sas_get_flag_at).

### `__sceSasSetVoice()`

```c
int __sceSasSetVoice(SceSasCore *core, int voice, void *vag, int size, int loop);
```

Sets PlayStation VAG data for a given sceSas voice.

- For raw PCM playback, see [\_\_sceSasSetVoicePCM](#__scesassetvoicepcm).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `vag` – A stable pointer to VAG ADPCM data.
- `size` – The size in bytes of the VAG ADPCM data.
- `loop` – Whether this voice should loop or not. The VAG file itself has to contain the end loop flag in its data in order for looping to work. Must be 0 or 1.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetVoicePCM()`

```c
int __sceSasSetVoicePCM(SceSasCore *core, int voice, void *pcm, int samplecount, int loopstart);
```

Sets PCM data for the given sceSas voice.

- For PlayStation VAG playback, see [\_\_sceSasSetVoice](#__scesassetvoice).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `pcm` – A stable pointer to the audio PCM data. The audio *MUST* be mono and its format *HAS* to be in 16-bit signed integer (little-endian).
- `samplecount` – The amount of samples the voice will play.
- `loopstart` – The sample position the loop will start from. Pass -1 to disable looping.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetKeyOn()`

```c
int __sceSasSetKeyOn(SceSasCore *core, int voice);
```

Plays the voice (starts Attack phase).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetKeyOff()`

```c
int __sceSasSetKeyOff(SceSasCore *core, int voice);
```

Stops the voice (starts Release phase).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetPitch()`

```c
int __sceSasSetPitch(SceSasCore *core, int voice, int pitch);
```

Sets the pitch value of a voice.

Can be used to set the playback speed of the voice. For waveform voices (such as steep/triangular/noise waves), this value gets treated as the tonal frequency (in hertz).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `pitch` – Fixed-point ratio where [PSP_SAS_PITCH_BASE](#psp_sas_pitch_base) means 1x in pitch-scale, or the tonal frequency (in hertz) of waveform voices. It must be a number between [PSP_SAS_PITCH_MIN](#psp_sas_pitch_min) ad [PSP_SAS_PITCH_MAX](#psp_sas_pitch_max).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetADSRmode()`

```c
int __sceSasSetADSRmode(SceSasCore *core, int voice, u32 mask, PspSasADSRCurveModes attackcurve, PspSasADSRCurveModes decaycurve, PspSasADSRCurveModes sustaincurve, PspSasADSRCurveModes releasecurve);
```

Sets the voice ADSR envelope curves.

Configures "how" the envelope progresses through its Attack, Decay, Sustain, and Release phases. Often used alongside [\_\_sceSasSetADSR](#__scesassetadsr) to set the envelope rates.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `mask` – Bitmask selecting which ADSR parameters to update. Use [PspSasADSRFlags](#enum-pspsasadsrflags) values or [PSP_SAS_ADSR_EVERYTHING](#psp_sas_adsr_everything).
- `attackcurve` – Attack step curve. One of [PspSasADSRCurveModes](#enum-pspsasadsrcurvemodes)
- `decaycurve` – Decay step curve. One of [PspSasADSRCurveModes](#enum-pspsasadsrcurvemodes)
- `sustaincurve` – Sustain step curve. One of [PspSasADSRCurveModes](#enum-pspsasadsrcurvemodes)
- `releasecurve` – Release step curve. One of [PspSasADSRCurveModes](#enum-pspsasadsrcurvemodes)

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetADSR()`

```c
int __sceSasSetADSR(SceSasCore *core, int voice, u32 mask, int attackrate, int decayrate, int sustainrate, int releaserate);
```

Sets the voice ADSR envelope rates for a voice.

Configures how fast the envelope progresses through its Attack, Decay, Sustain, and Release phases.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `mask` – Bitmask selecting which ADSR parameters to update. Use [PspSasADSRFlags](#enum-pspsasadsrflags) values or [PSP_SAS_ADSR_EVERYTHING](#psp_sas_adsr_everything).
- `attackrate` – Attack step rate (rise towards [PSP_SAS_ENVELOPE_HEIGHT_MAX](#psp_sas_envelope_height_max)).
- `decayrate` – Decay step rate (fall towards sustain level).
- `sustainrate` – Sustain phase rate (envelope change while key is held)
- `releaserate` – Release step rate (fall toward 0 after key is off).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetSimpleADSR()`

```c
int __sceSasSetSimpleADSR(SceSasCore *core, int voice, u32 envelope1, u32 envelope2);
```

Configures the entire voice ADSR envelope (rates & curves).

**Todo:** Explain how to set ADSR parameters via `envelope1` and `envelope2`.

This is used to set the entire ADSR envelope in a single call, acting as a replacement to [\_\_sceSasSetADSR](#__scesassetadsr) and [\_\_sceSasSetADSRmode](#__scesassetadsrmode).

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `envelope1` – First envelope config value.
- `envelope2` – Second envelope config value.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetSL()`

```c
int __sceSasSetSL(SceSasCore *core, int voice, int level);
```

Sets the voice ADSR envelope sustain level height.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `level` – A number between 0 and [PSP_SAS_ENVELOPE_HEIGHT_MAX](#psp_sas_envelope_height_max)

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetVolume()`

```c
int __sceSasSetVolume(SceSasCore *core, int voice, int leftvol, int rightvol, int sendleftvol, int sendrightvol);
```

Sets the output volume of the voice.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index.
- `leftvol` – Left dry channel volume. Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).
- `rightvol` – Right dry channel volume. Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).
- `sendleftvol` – Send-Left channel volume. Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).
- `sendrightvol` – Send-Right channel volume. Must be a number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasCore()`

```c
int __sceSasCore(SceSasCore *core, void *dst);
```

Runs a sceSas cycle iteration and outputs samples onto destination buffer.

This is the heart of sceSasCore, hence its name. Processes and updates voices, mixes them together and updates end/pause flags.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `dst` – A destination buffer of N bytes, where `N == (grainSize * 4 * sizeof(int16_t))`. The data layout gets decided from the current output mode, which is one of [PspSasOutputModes](#enum-pspsasoutputmodes).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasCoreWithMix()`

```c
int __sceSasCoreWithMix(SceSasCore *core, void *dst, int leftvol, int rightvol);
```

Runs a sceSas cycle iteration and mixes samples onto destination buffer.

This is similar to [\_\_sceSasCore](#__scesascore), except that the destination buffer does not get cleared.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `dst` – A destination buffer of N bytes, where `N == (grainSize * 4 * sizeof(int16_t))`. The data layout gets decided from the current output mode, which is one of [PspSasOutputModes](#enum-pspsasoutputmodes).
- `leftvol` – A number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).
- `rightvol` – A number between 0 and [PSP_SAS_VOLUME_MAX](#psp_sas_volume_max).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasGetPauseFlag()`

```c
int __sceSasGetPauseFlag(SceSasCore *core);
```

Get the pause status of every voice in a bitfield.

Each bit corresponds to a voice index:

- Bit N == 1 -> voice N is paused.
- Bit N == 0 -> voice N is currently playing.

**Parameters:**

- `core` – Pointer to a valid Sas instance

**Returns:** 32-bit bitmask of voice pause flags. To read a specific voice bit, use [PSP_SAS_GET_FLAG_AT](#psp_sas_get_flag_at).

### `__sceSasGetEnvelopeHeight()`

```c
int __sceSasGetEnvelopeHeight(SceSasCore *core, int voice);
```

Gets the current envelope height of a voice.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The voice index to read from.

**Returns:** The voice height, ranging from 0 and [PSP_SAS_ENVELOPE_HEIGHT_MAX](#psp_sas_envelope_height_max) on success, an error code if less than 0.

### `__sceSasGetAllEnvelopeHeights()`

```c
int __sceSasGetAllEnvelopeHeights(SceSasCore *core, int heights[32]);
```

Gets the current envelope height of all voices.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `heights` – An `int` array of 32 indices where the results will be inserted into.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetPause()`

```c
int __sceSasSetPause(SceSasCore *core, u32 voicebit, int pause);
```

Pauses/unpauses voice playback using a bitmask.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voicebit` – 32-bit bitmask selecting which voices to update. Each bit corresponds to a voice index. You can use [PSP_SAS_GET_VOICE_BIT](#psp_sas_get_voice_bit) to convert a voice index into a proper bitmask.
- `pause` – Whether to pause or unpause the selected voices

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetNoise()`

```c
int __sceSasSetNoise(SceSasCore *core, int voice, int freq);
```

Configures the voice to play a noise waveform.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index
- `freq` – How often the wave will randomly alternate? Must be a number from 0 to [PSP_SAS_NOISE_FREQ_MAX](#psp_sas_noise_freq_max).

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetTrianglarWave()`

```c
int __sceSasSetTrianglarWave(SceSasCore *core, int voice, int unk);
```

Configures the voice to play a triangular waveform.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index
- `unk` – Unsure. Probably duty cycle + some other thing that gets packed into 7 bits? Apparently it must be a number from 0 to 100.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetTriangularWave()`

```c
int __sceSasSetTriangularWave(SceSasCore *core, int voice, int unk);
```

A function alias of [\_\_sceSasSetTrianglarWave](#__scesassettrianglarwave).

### `__sceSasSetSteepWave()`

```c
int __sceSasSetSteepWave(SceSasCore *core, int voice, int duty);
```

Configures the voice to play a square waveform.

**Parameters:**

- `core` – Pointer to a valid sceSas instance.
- `voice` – The target voice index
- `duty` – The percentage of the square's duty cycle (e.g. a value of 50 means a symmetrical 50% duty cycle). Must be a number from 0 to 100.

**Returns:** 0 on success, an error code if less than 0.

### `__sceSasSetVoiceATRAC3()`

```c
int __sceSasSetVoiceATRAC3(SceSasCore *core, int voice, void *atrac3ctx);
```

### `__sceSasConcatenateATRAC3()`

```c
int __sceSasConcatenateATRAC3(SceSasCore *core, int voice, void *data, int size);
```

### `__sceSasUnsetATRAC3()`

```c
int __sceSasUnsetATRAC3(SceSasCore *core, int voice);
```

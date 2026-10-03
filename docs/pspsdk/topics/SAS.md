[PSPSDK documentation](../README.md) › Topics

# SAS Core Audio Library

This module contains the imports for sceSasCore, the PSP's audio software mixer.

Headers: [`sascore/pspsascore.h`](../files/sascore/pspsascore.h.md)

## Data Structures

- [`struct SceSasCore`](../files/sascore/pspsascore.h.md#struct-scesascore) – Contains all data related to a sceSasCore state.

## Macros

- [`PSP_SAS_GET_VOICE_BIT`](../files/sascore/pspsascore.h.md#psp_sas_get_voice_bit) – Macro utility to obtain the corresponding bit of a voice index.
- [`PSP_SAS_GET_FLAG_AT`](../files/sascore/pspsascore.h.md#psp_sas_get_flag_at) – Macro utility for reading voice bitfield flags.
- [`PSP_SAS_GRAIN_SIZE`](../files/sascore/pspsascore.h.md#psp_sas_grain_size) – The recommended sceSasCore grain size that's used by most games.
- [`PSP_SAS_GRAIN_SIZE_MIN`](../files/sascore/pspsascore.h.md#psp_sas_grain_size_min) – The minimum sceSasCore grain size.
- [`PSP_SAS_GRAIN_SIZE_MAX`](../files/sascore/pspsascore.h.md#psp_sas_grain_size_max) – The maximum sceSasCore grain size.
- [`PSP_SAS_VOICES_MAX`](../files/sascore/pspsascore.h.md#psp_sas_voices_max) – The maximum number of voices that sceSas can playback all at once.
- [`PSP_SAS_SAMPLE_RATE`](../files/sascore/pspsascore.h.md#psp_sas_sample_rate) – The sample rate of sceSasCore mixer.
- [`PSP_SAS_VOLUME_MAX`](../files/sascore/pspsascore.h.md#psp_sas_volume_max) – The maximum output volume of sceSas voices.
- [`PSP_SAS_PITCH_BASE`](../files/sascore/pspsascore.h.md#psp_sas_pitch_base) – Represents 1x voice pitch.
- [`PSP_SAS_PITCH_MIN`](../files/sascore/pspsascore.h.md#psp_sas_pitch_min) – The minimum supported voice pitch.
- [`PSP_SAS_PITCH_MAX`](../files/sascore/pspsascore.h.md#psp_sas_pitch_max) – The maximum supported voice pitch.
- [`PSP_SAS_NOISE_FREQ_MAX`](../files/sascore/pspsascore.h.md#psp_sas_noise_freq_max) – The maximum noise frequency.
- [`PSP_SAS_ENVELOPE_HEIGHT_MAX`](../files/sascore/pspsascore.h.md#psp_sas_envelope_height_max) – Represents maximum ADSR envelope height.
- [`PSP_SAS_ENVELOPE_FREQ_MAX`](../files/sascore/pspsascore.h.md#psp_sas_envelope_freq_max) – Represents maximum ADSR envelope frequency.
- [`PSP_SAS_ADSR_EVERYTHING`](../files/sascore/pspsascore.h.md#psp_sas_adsr_everything)

## Enumerations

- [`PspSasOutputModes`](../files/sascore/pspsascore.h.md#enum-pspsasoutputmodes)
- [`PspSasEffectTypes`](../files/sascore/pspsascore.h.md#enum-pspsaseffecttypes)
- [`PspSasADSRCurveModes`](../files/sascore/pspsascore.h.md#enum-pspsasadsrcurvemodes) – ADSR envelope curve modes.
- [`PspSasErrorCodes`](../files/sascore/pspsascore.h.md#enum-pspsaserrorcodes) – Error codes used as return values by sceSasCore.
- [`PspSasADSRFlags`](../files/sascore/pspsascore.h.md#enum-pspsasadsrflags) – ADSR envelope flags.

## Functions

- [`__sceSasInit()`](../files/sascore/pspsascore.h.md#__scesasinit) – Initializes a [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasGetOutputmode()`](../files/sascore/pspsascore.h.md#__scesasgetoutputmode) – Gets the current output mode from the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasSetOutputmode()`](../files/sascore/pspsascore.h.md#__scesassetoutputmode) – Sets the current output mode of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasRevType()`](../files/sascore/pspsascore.h.md#__scesasrevtype) – Sets the reverb effect of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasRevEVOL()`](../files/sascore/pspsascore.h.md#__scesasrevevol) – Sets the effect volume of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasRevVON()`](../files/sascore/pspsascore.h.md#__scesasrevvon) – Toggles dry and wet audio signals of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasRevParam()`](../files/sascore/pspsascore.h.md#__scesasrevparam) – Sets the effect delay and feedback parameters of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasGetGrain()`](../files/sascore/pspsascore.h.md#__scesasgetgrain) – Gets the grain size of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasSetGrain()`](../files/sascore/pspsascore.h.md#__scesassetgrain) – Sets the grain size of the [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) instance.
- [`__sceSasGetEndFlag()`](../files/sascore/pspsascore.h.md#__scesasgetendflag) – Gets the end status of the voices from an [SceSasCore](../files/sascore/pspsascore.h.md#struct-scesascore) nstance.
- [`__sceSasSetVoice()`](../files/sascore/pspsascore.h.md#__scesassetvoice) – Sets PlayStation VAG data for a given sceSas voice.
- [`__sceSasSetVoicePCM()`](../files/sascore/pspsascore.h.md#__scesassetvoicepcm) – Sets PCM data for the given sceSas voice.
- [`__sceSasSetKeyOn()`](../files/sascore/pspsascore.h.md#__scesassetkeyon) – Plays the voice (starts Attack phase).
- [`__sceSasSetKeyOff()`](../files/sascore/pspsascore.h.md#__scesassetkeyoff) – Stops the voice (starts Release phase).
- [`__sceSasSetPitch()`](../files/sascore/pspsascore.h.md#__scesassetpitch) – Sets the pitch value of a voice.
- [`__sceSasSetADSRmode()`](../files/sascore/pspsascore.h.md#__scesassetadsrmode) – Sets the voice ADSR envelope curves.
- [`__sceSasSetADSR()`](../files/sascore/pspsascore.h.md#__scesassetadsr) – Sets the voice ADSR envelope rates for a voice.
- [`__sceSasSetSimpleADSR()`](../files/sascore/pspsascore.h.md#__scesassetsimpleadsr) – Configures the entire voice ADSR envelope (rates & curves).
- [`__sceSasSetSL()`](../files/sascore/pspsascore.h.md#__scesassetsl) – Sets the voice ADSR envelope sustain level height.
- [`__sceSasSetVolume()`](../files/sascore/pspsascore.h.md#__scesassetvolume) – Sets the output volume of the voice.
- [`__sceSasCore()`](../files/sascore/pspsascore.h.md#__scesascore) – Runs a sceSas cycle iteration and outputs samples onto destination buffer.
- [`__sceSasCoreWithMix()`](../files/sascore/pspsascore.h.md#__scesascorewithmix) – Runs a sceSas cycle iteration and mixes samples onto destination buffer.
- [`__sceSasGetPauseFlag()`](../files/sascore/pspsascore.h.md#__scesasgetpauseflag) – Get the pause status of every voice in a bitfield.
- [`__sceSasGetEnvelopeHeight()`](../files/sascore/pspsascore.h.md#__scesasgetenvelopeheight) – Gets the current envelope height of a voice.
- [`__sceSasGetAllEnvelopeHeights()`](../files/sascore/pspsascore.h.md#__scesasgetallenvelopeheights) – Gets the current envelope height of all voices.
- [`__sceSasSetPause()`](../files/sascore/pspsascore.h.md#__scesassetpause) – Pauses/unpauses voice playback using a bitmask.
- [`__sceSasSetNoise()`](../files/sascore/pspsascore.h.md#__scesassetnoise) – Configures the voice to play a noise waveform.
- [`__sceSasSetTrianglarWave()`](../files/sascore/pspsascore.h.md#__scesassettrianglarwave) – Configures the voice to play a triangular waveform.
- [`__sceSasSetTriangularWave()`](../files/sascore/pspsascore.h.md#__scesassettriangularwave) – A function alias of [\_\_sceSasSetTrianglarWave](../files/sascore/pspsascore.h.md#__scesassettrianglarwave).
- [`__sceSasSetSteepWave()`](../files/sascore/pspsascore.h.md#__scesassetsteepwave) – Configures the voice to play a square waveform.
- [`__sceSasSetVoiceATRAC3()`](../files/sascore/pspsascore.h.md#__scesassetvoiceatrac3)
- [`__sceSasConcatenateATRAC3()`](../files/sascore/pspsascore.h.md#__scesasconcatenateatrac3)
- [`__sceSasUnsetATRAC3()`](../files/sascore/pspsascore.h.md#__scesasunsetatrac3)

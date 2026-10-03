[PSPSDK documentation](../../README.md) › Files

# usb/pspusbcam.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct PspUsbCamSetupStillParam`

Structure for sceUsbCamSetupStill.

| Field | Description |
|---|---|
| `int size` | Size of the [PspUsbCamSetupStillParam](#struct-pspusbcamsetupstillparam) structure. |
| `int resolution` | Resolution.<br>One of [PspUsbCamResolution](#enum-pspusbcamresolution) |
| `int jpegsize` | Size of the jpeg image. |
| `int reverseflags` | Reverse effect to apply.<br>Zero or more of [PspUsbCamReverseFlags](#enum-pspusbcamreverseflags) |
| `int delay` | Delay to apply to take the picture.<br>One of [PspUsbCamDelay](#enum-pspusbcamdelay) |
| `int complevel` | JPEG compression level, a value from 1-63.<br>1 -> less compression, better quality; 63 -> max compression, worse quality |

### `struct PspUsbCamSetupStillExParam`

Structure for sceUsbCamSetupStillEx.

| Field | Description |
|---|---|
| `int size` | Size of the [PspUsbCamSetupStillExParam](#struct-pspusbcamsetupstillexparam) structure. |
| `u32 unk` | Unknown, set it to 9 at the moment. |
| `int resolution` | Resolution.<br>One of [PspUsbCamResolutionEx](#enum-pspusbcamresolutionex) |
| `int jpegsize` | Size of the jpeg image. |
| `int complevel` | JPEG compression level, a value from 1-63.<br>1 -> less compression, better quality; 63 -> max compression, worse quality |
| `u32 unk2` | Unknown, set it to 0 at the moment. |
| `u32 unk3` | Unknown, set it to 1 at the moment. |
| `int flip` | Flag that indicates whether to flip the image. |
| `int mirror` | Flag that indicates whether to mirror the image. |
| `int delay` | Delay to apply to take the picture.<br>One of [PspUsbCamDelay](#enum-pspusbcamdelay) |
| `u32 unk4[5]` | Unknown, set it to 0 at the moment. |

### `struct PspUsbCamSetupVideoParam`

| Field | Description |
|---|---|
| `int size` | Size of the [PspUsbCamSetupVideoParam](#struct-pspusbcamsetupvideoparam) structure. |
| `int resolution` | Resolution.<br>One of [PspUsbCamResolution](#enum-pspusbcamresolution) |
| `int framerate` | Framerate.<br>One of [PspUsbCamFrameRate](#enum-pspusbcamframerate) |
| `int wb` | White balance.<br>One of [PspUsbCamWB](#enum-pspusbcamwb) |
| `int saturation` | Saturarion (0-255) |
| `int brightness` | Brightness (0-255) |
| `int contrast` | Contrast (0-255) |
| `int sharpness` | Sharpness (0-255) |
| `int effectmode` | Effect mode.<br>One of [PspUsbCamEffectMode](#enum-pspusbcameffectmode) |
| `int framesize` | Size of jpeg video frame. |
| `u32 unk` | Unknown.<br>Set it to 0 at the moment. |
| `int evlevel` | Exposure value.<br>One of [PspUsbCamEVLevel](#enum-pspusbcamevlevel) |

### `struct PspUsbCamSetupVideoExParam`

| Field | Description |
|---|---|
| `int size` | Size of the [PspUsbCamSetupVideoParam](#struct-pspusbcamsetupvideoparam) structure. |
| `u32 unk` |  |
| `int resolution` | Resolution.<br>One of [PspUsbCamResolutionEx](#enum-pspusbcamresolutionex) |
| `int framerate` | Framerate.<br>One of [PspUsbCamFrameRate](#enum-pspusbcamframerate) |
| `u32 unk2` | Unknown.<br>Set it to 2 at the moment |
| `u32 unk3` | Unknown.<br>Set it to 3 at the moment |
| `int wb` | White balance.<br>One of [PspUsbCamWB](#enum-pspusbcamwb) |
| `int saturation` | Saturarion (0-255) |
| `int brightness` | Brightness (0-255) |
| `int contrast` | Contrast (0-255) |
| `int sharpness` | Sharpness (0-255) |
| `u32 unk4` | Unknown.<br>Set it to 0 at the moment |
| `u32 unk5` | Unknown.<br>Set it to 1 at the moment |
| `u32 unk6[3]` | Unknown.<br>Set it to 0 at the moment |
| `int effectmode` | Effect mode.<br>One of [PspUsbCamEffectMode](#enum-pspusbcameffectmode) |
| `u32 unk7` | Unknown.<br>Set it to 1 at the moment |
| `u32 unk8` | Unknown.<br>Set it to 10 at the moment |
| `u32 unk9` | Unknown.<br>Set it to 2 at the moment |
| `u32 unk10` | Unknown.<br>Set it to 500 at the moment |
| `u32 unk11` | Unknown.<br>Set it to 1000 at the moment |
| `int framesize` | Size of jpeg video frame. |
| `u32 unk12` | Unknown.<br>Set it to 0 at the moment |
| `int evlevel` | Exposure value.<br>One of [PspUsbCamEVLevel](#enum-pspusbcamevlevel) |

### `struct PspUsbCamSetupMicParam`

```c
struct PspUsbCamSetupMicParam {
    int size;
    int alc;
    int gain;
    int noize;
    int freq;
};
```

### `struct PspUsbCamSetupMicExParam`

```c
struct PspUsbCamSetupMicExParam {
    int size;
    int alc;
    int gain;
    u32 unk2[4];
    int freq;
    int unk3;
};
```

## Macros

### `PSP_USBCAM_PID`

```c
#define PSP_USBCAM_PID (0x282)
```

### `PSP_USBCAM_DRIVERNAME`

```c
#define PSP_USBCAM_DRIVERNAME "USBCamDriver"
```

### `PSP_USBCAMMIC_DRIVERNAME`

```c
#define PSP_USBCAMMIC_DRIVERNAME "USBCamMicDriver"
```

## Typedefs

### `PspUsbCamSetupStillParam`

```c
typedef struct PspUsbCamSetupStillParam PspUsbCamSetupStillParam;
```

Structure for sceUsbCamSetupStill.

### `PspUsbCamSetupStillExParam`

```c
typedef struct PspUsbCamSetupStillExParam PspUsbCamSetupStillExParam;
```

Structure for sceUsbCamSetupStillEx.

### `PspUsbCamSetupVideoParam`

```c
typedef struct PspUsbCamSetupVideoParam PspUsbCamSetupVideoParam;
```

### `PspUsbCamSetupVideoExParam`

```c
typedef struct PspUsbCamSetupVideoExParam PspUsbCamSetupVideoExParam;
```

### `PspUsbCamSetupMicParam`

```c
typedef struct PspUsbCamSetupMicParam PspUsbCamSetupMicParam;
```

### `PspUsbCamSetupMicExParam`

```c
typedef struct PspUsbCamSetupMicExParam PspUsbCamSetupMicExParam;
```

## Enumerations

### `enum PspUsbCamResolution`

Resolutions for sceUsbCamSetupStill & sceUsbCamSetupVideo DO NOT use on sceUsbCamSetupStillEx & sceUsbCamSetupVideoEx.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_RESOLUTION_160_120` | `0` |  |
| `PSP_USBCAM_RESOLUTION_176_144` | `1` |  |
| `PSP_USBCAM_RESOLUTION_320_240` | `2` |  |
| `PSP_USBCAM_RESOLUTION_352_288` | `3` |  |
| `PSP_USBCAM_RESOLUTION_640_480` | `4` |  |
| `PSP_USBCAM_RESOLUTION_1024_768` | `5` |  |
| `PSP_USBCAM_RESOLUTION_1280_960` | `6` |  |
| `PSP_USBCAM_RESOLUTION_480_272` | `7` |  |
| `PSP_USBCAM_RESOLUTION_360_272` | `8` |  |

### `enum PspUsbCamResolutionEx`

Resolutions for sceUsbCamSetupStillEx & sceUsbCamSetupVideoEx DO NOT use on sceUsbCamSetupStill & sceUsbCamSetupVideo.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_RESOLUTION_EX_160_120` | `0` |  |
| `PSP_USBCAM_RESOLUTION_EX_176_144` | `1` |  |
| `PSP_USBCAM_RESOLUTION_EX_320_240` | `2` |  |
| `PSP_USBCAM_RESOLUTION_EX_352_288` | `3` |  |
| `PSP_USBCAM_RESOLUTION_EX_360_272` | `4` |  |
| `PSP_USBCAM_RESOLUTION_EX_480_272` | `5` |  |
| `PSP_USBCAM_RESOLUTION_EX_640_480` | `6` |  |
| `PSP_USBCAM_RESOLUTION_EX_1024_768` | `7` |  |
| `PSP_USBCAM_RESOLUTION_EX_1280_960` | `8` |  |

### `enum PspUsbCamReverseFlags`

Flags for reverse effects.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_FLIP` | `1` |  |
| `PSP_USBCAM_MIRROR` | `0x100` |  |

### `enum PspUsbCamDelay`

Delay to take pictures.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_NODELAY` | `0` |  |
| `PSP_USBCAM_DELAY_10SEC` | `1` |  |
| `PSP_USBCAM_DELAY_20SEC` | `2` |  |
| `PSP_USBCAM_DELAY_30SEC` | `3` |  |

### `enum PspUsbCamFrameRate`

Usbcam framerates.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_FRAMERATE_3_75_FPS` | `0` |  |
| `PSP_USBCAM_FRAMERATE_5_FPS` | `1` |  |
| `PSP_USBCAM_FRAMERATE_7_5_FPS` | `2` |  |
| `PSP_USBCAM_FRAMERATE_10_FPS` | `3` |  |
| `PSP_USBCAM_FRAMERATE_15_FPS` | `4` |  |
| `PSP_USBCAM_FRAMERATE_20_FPS` | `5` |  |
| `PSP_USBCAM_FRAMERATE_30_FPS` | `6` |  |
| `PSP_USBCAM_FRAMERATE_60_FPS` | `7` |  |

### `enum PspUsbCamWB`

White balance values.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_WB_AUTO` | `0` |  |
| `PSP_USBCAM_WB_DAYLIGHT` | `1` |  |
| `PSP_USBCAM_WB_FLUORESCENT` | `2` |  |
| `PSP_USBCAM_WB_INCADESCENT` | `3` |  |

### `enum PspUsbCamEffectMode`

Effect modes.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_EFFECTMODE_NORMAL` | `0` |  |
| `PSP_USBCAM_EFFECTMODE_NEGATIVE` | `1` |  |
| `PSP_USBCAM_EFFECTMODE_BLACKWHITE` | `2` |  |
| `PSP_USBCAM_EFFECTMODE_SEPIA` | `3` |  |
| `PSP_USBCAM_EFFECTMODE_BLUE` | `4` |  |
| `PSP_USBCAM_EFFECTMODE_RED` | `5` |  |
| `PSP_USBCAM_EFFECTMODE_GREEN` | `6` |  |

### `enum PspUsbCamEVLevel`

Exposure levels.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_USBCAM_EVLEVEL_2_0_POSITIVE` | `0` |  |
| `PSP_USBCAM_EVLEVEL_1_7_POSITIVE` | `1` |  |
| `PSP_USBCAM_EVLEVEL_1_5_POSITIVE` | `2` |  |
| `PSP_USBCAM_EVLEVEL_1_3_POSITIVE` | `3` |  |
| `PSP_USBCAM_EVLEVEL_1_0_POSITIVE` | `4` |  |
| `PSP_USBCAM_EVLEVEL_0_7_POSITIVE` | `5` |  |
| `PSP_USBCAM_EVLEVEL_0_5_POSITIVE` | `6` |  |
| `PSP_USBCAM_EVLEVEL_0_3_POSITIVE` | `7` |  |
| `PSP_USBCAM_EVLEVEL_0_0` | `8` |  |
| `PSP_USBCAM_EVLEVEL_0_3_NEGATIVE` | `9` |  |
| `PSP_USBCAM_EVLEVEL_0_5_NEGATIVE` | `10` |  |
| `PSP_USBCAM_EVLEVEL_0_7_NEGATIVE` | `11` |  |
| `PSP_USBCAM_EVLEVEL_1_0_NEGATIVE` | `12` |  |
| `PSP_USBCAM_EVLEVEL_1_3_NEGATIVE` | `13` |  |
| `PSP_USBCAM_EVLEVEL_1_5_NEGATIVE` | `14` |  |
| `PSP_USBCAM_EVLEVEL_1_7_NEGATIVE` | `15` |  |
| `PSP_USBCAM_EVLEVEL_2_0_NEGATIVE` | `16` |  |

## Functions

### `sceUsbCamSetupStill()`

```c
int sceUsbCamSetupStill(PspUsbCamSetupStillParam *param);
```

Setups the parameters to take a still image.

**Parameters:**

- `param` – pointer to a [PspUsbCamSetupStillParam](#struct-pspusbcamsetupstillparam)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetupStillEx()`

```c
int sceUsbCamSetupStillEx(PspUsbCamSetupStillExParam *param);
```

Setups the parameters to take a still image (with more options)

**Parameters:**

- `param` – pointer to a [PspUsbCamSetupStillExParam](#struct-pspusbcamsetupstillexparam)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamStillInputBlocking()`

```c
int sceUsbCamStillInputBlocking(u8 *buf, SceSize size);
```

Gets a still image.

The function doesn't return until the image has been acquired.

**Parameters:**

- `buf` – The buffer that receives the image jpeg data
- `size` – The size of the buffer.

**Returns:** size of acquired image on success, \< 0 on error

### `sceUsbCamStillInput()`

```c
int sceUsbCamStillInput(u8 *buf, SceSize size);
```

Gets a still image.

The function returns inmediately, and the completion has to be handled by calling [sceUsbCamStillWaitInputEnd](#sceusbcamstillwaitinputend) or [sceUsbCamStillPollInputEnd](#sceusbcamstillpollinputend).

**Parameters:**

- `buf` – The buffer that receives the image jpeg data
- `size` – The size of the buffer.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamStillWaitInputEnd()`

```c
int sceUsbCamStillWaitInputEnd(void);
```

Waits untils still input has been finished.

**Returns:** the size of the acquired image on sucess, \< 0 on error

### `sceUsbCamStillPollInputEnd()`

```c
int sceUsbCamStillPollInputEnd(void);
```

Polls the status of still input completion.

**Returns:** the size of the acquired image if still input has ended, 0 if the input has not ended, \< 0 on error.

### `sceUsbCamStillCancelInput()`

```c
int sceUsbCamStillCancelInput(void);
```

Cancels the still input.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamStillGetInputLength()`

```c
int sceUsbCamStillGetInputLength(void);
```

Gets the size of the acquired still image.

**Returns:** the size of the acquired image on success, \< 0 on error

### `sceUsbCamSetupVideo()`

```c
int sceUsbCamSetupVideo(PspUsbCamSetupVideoParam *param, void *workarea, int wasize);
```

Set ups the parameters for video capture.

**Parameters:**

- `param` – Pointer to a [PspUsbCamSetupVideoParam](#struct-pspusbcamsetupvideoparam) structure.
- `workarea` – Pointer to a buffer used as work area by the driver.
- `wasize` – Size of the work area.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetupVideoEx()`

```c
int sceUsbCamSetupVideoEx(PspUsbCamSetupVideoExParam *param, void *workarea, int wasize);
```

Set ups the parameters for video capture (with more options)

**Parameters:**

- `param` – Pointer to a [PspUsbCamSetupVideoExParam](#struct-pspusbcamsetupvideoexparam) structure.
- `workarea` – Pointer to a buffer used as work area by the driver.
- `wasize` – Size of the work area.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamStartVideo()`

```c
int sceUsbCamStartVideo(void);
```

Starts video input from the camera.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamStopVideo()`

```c
int sceUsbCamStopVideo(void);
```

Stops video input from the camera.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamReadVideoFrameBlocking()`

```c
int sceUsbCamReadVideoFrameBlocking(u8 *buf, SceSize size);
```

Reads a video frame.

The function doesn't return until the frame has been acquired.

**Parameters:**

- `buf` – The buffer that receives the frame jpeg data
- `size` – The size of the buffer.

**Returns:** size of acquired frame on success, \< 0 on error

### `sceUsbCamReadVideoFrame()`

```c
int sceUsbCamReadVideoFrame(u8 *buf, SceSize size);
```

Reads a video frame.

The function returns inmediately, and the completion has to be handled by calling [sceUsbCamWaitReadVideoFrameEnd](#sceusbcamwaitreadvideoframeend) or [sceUsbCamPollReadVideoFrameEnd](#sceusbcampollreadvideoframeend).

**Parameters:**

- `buf` – The buffer that receives the frame jpeg data
- `size` – The size of the buffer.

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamWaitReadVideoFrameEnd()`

```c
int sceUsbCamWaitReadVideoFrameEnd(void);
```

Waits untils the current frame has been read.

**Returns:** the size of the acquired frame on sucess, \< 0 on error

### `sceUsbCamPollReadVideoFrameEnd()`

```c
int sceUsbCamPollReadVideoFrameEnd(void);
```

Polls the status of video frame read completion.

**Returns:** the size of the acquired frame if it has been read, 0 if the frame has not yet been read, \< 0 on error.

### `sceUsbCamGetReadVideoFrameSize()`

```c
int sceUsbCamGetReadVideoFrameSize(void);
```

Gets the size of the acquired frame.

**Returns:** the size of the acquired frame on success, \< 0 on error

### `sceUsbCamSetSaturation()`

```c
int sceUsbCamSetSaturation(int saturation);
```

Sets the saturation.

**Parameters:**

- `saturation` – The saturation (0-255)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetBrightness()`

```c
int sceUsbCamSetBrightness(int brightness);
```

Sets the brightness.

**Parameters:**

- `brightness` – The brightness (0-255)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetContrast()`

```c
int sceUsbCamSetContrast(int contrast);
```

Sets the contrast.

**Parameters:**

- `contrast` – The contrast (0-255)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetSharpness()`

```c
int sceUsbCamSetSharpness(int sharpness);
```

Sets the sharpness.

**Parameters:**

- `sharpness` – The sharpness (0-255)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetImageEffectMode()`

```c
int sceUsbCamSetImageEffectMode(int effectmode);
```

Sets the image effect mode.

**Parameters:**

- `effectmode` – The effect mode, one of [PspUsbCamEffectMode](#enum-pspusbcameffectmode)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetEvLevel()`

```c
int sceUsbCamSetEvLevel(int ev);
```

Sets the exposure level.

**Parameters:**

- `ev` – The exposure level, one of [PspUsbCamEVLevel](#enum-pspusbcamevlevel)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetReverseMode()`

```c
int sceUsbCamSetReverseMode(int reverseflags);
```

Sets the reverse mode.

**Parameters:**

- `reverseflags` – The reverse flags, zero or more of [PspUsbCamReverseFlags](#enum-pspusbcamreverseflags)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamSetZoom()`

```c
int sceUsbCamSetZoom(int zoom);
```

Sets the zoom.

**Parameters:**

- `zoom` – The zoom level starting by 10. (10 = 1X, 11 = 1.1X, etc)

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetSaturation()`

```c
int sceUsbCamGetSaturation(int *saturation);
```

Gets the current saturation.

**Parameters:**

- `saturation` – pointer to a variable that receives the current saturation

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetBrightness()`

```c
int sceUsbCamGetBrightness(int *brightness);
```

Gets the current brightness.

**Parameters:**

- `brightness` – pointer to a variable that receives the current brightness

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetContrast()`

```c
int sceUsbCamGetContrast(int *contrast);
```

Gets the current contrast.

**Parameters:**

- `contrast` – pointer to a variable that receives the current contrast

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetSharpness()`

```c
int sceUsbCamGetSharpness(int *sharpness);
```

Gets the current sharpness.

**Parameters:**

- `sharpness` – pointer to a variable that receives the current sharpness

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetImageEffectMode()`

```c
int sceUsbCamGetImageEffectMode(int *effectmode);
```

Gets the current image efect mode.

**Parameters:**

- `effectmode` – pointer to a variable that receives the current effect mode

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetEvLevel()`

```c
int sceUsbCamGetEvLevel(int *ev);
```

Gets the current exposure level.

**Parameters:**

- `ev` – pointer to a variable that receives the current exposure level

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetReverseMode()`

```c
int sceUsbCamGetReverseMode(int *reverseflags);
```

Gets the current reverse mode.

**Parameters:**

- `reverseflags` – pointer to a variable that receives the current reverse mode flags

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetZoom()`

```c
int sceUsbCamGetZoom(int *zoom);
```

Gets the current zoom.

**Parameters:**

- `zoom` – pointer to a variable that receives the current zoom

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamAutoImageReverseSW()`

```c
int sceUsbCamAutoImageReverseSW(int on);
```

Sets if the image should be automatically reversed, depending of the position of the camera.

**Parameters:**

- `on` – 1 to set the automatical reversal of the image, 0 to set it off

**Returns:** 0 on success, \< 0 on error

### `sceUsbCamGetAutoImageReverseState()`

```c
int sceUsbCamGetAutoImageReverseState(void);
```

Gets the state of the autoreversal of the image.

**Returns:** 1 if it is set to automatic, 0 otherwise

### `sceUsbCamGetLensDirection()`

```c
int sceUsbCamGetLensDirection(void);
```

Gets the direction of the camera lens.

**Returns:** 1 if the camera is "looking to you", 0 if the camera is "looking to the other side".

### `sceUsbCamSetupMic()`

```c
int sceUsbCamSetupMic(void *param, void *workarea, int wasize);
```

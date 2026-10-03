[PSPSDK documentation](../../README.md) › Files

# utility/psputility_osk.h

```c
#include <psptypes.h>
```

## Data Structures

### `struct _SceUtilityOskData`

OSK Field data.

| Field | Description |
|---|---|
| `int unk_00` | Unknown.<br>Pass 0. |
| `int unk_04` | Unknown.<br>Pass 0. |
| `int language` | One of [SceUtilityOskInputLanguage](#enum-sceutilityoskinputlanguage). |
| `int unk_12` | Unknown.<br>Pass 0. |
| `int inputtype` | One or more of [SceUtilityOskInputType](#enum-sceutilityoskinputtype) (types that are selectable by pressing SELECT) |
| `int lines` | Number of lines. |
| `int unk_24` | Unknown.<br>Pass 0. |
| `unsigned short * desc` | Description text. |
| `unsigned short * intext` | Initial text. |
| `int outtextlength` | Length of output text. |
| `unsigned short * outtext` | Pointer to the output text. |
| `int result` | Result.<br>One of [SceUtilityOskResult](#enum-sceutilityoskresult) |
| `int outtextlimit` | The max text that can be input. |

### `struct _SceUtilityOskParams`

OSK parameters.

| Field | Description |
|---|---|
| `pspUtilityDialogCommon base` |  |
| `int datacount` | Number of input fields. |
| `SceUtilityOskData * data` | Pointer to the start of the data for the input fields. |
| `int state` | The local OSK state, one of [SceUtilityOskState](#enum-sceutilityoskstate). |
| `int unk_60` | Unknown.<br>Pass 0 |

## Typedefs

### `SceUtilityOskData`

```c
typedef struct _SceUtilityOskData SceUtilityOskData;
```

OSK Field data.

### `SceUtilityOskParams`

```c
typedef struct _SceUtilityOskParams SceUtilityOskParams;
```

OSK parameters.

## Enumerations

### `enum SceUtilityOskInputLanguage`

Enumeration for input language.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_OSK_LANGUAGE_DEFAULT` | `0x00` |  |
| `PSP_UTILITY_OSK_LANGUAGE_JAPANESE` | `0x01` |  |
| `PSP_UTILITY_OSK_LANGUAGE_ENGLISH` | `0x02` |  |
| `PSP_UTILITY_OSK_LANGUAGE_FRENCH` | `0x03` |  |
| `PSP_UTILITY_OSK_LANGUAGE_SPANISH` | `0x04` |  |
| `PSP_UTILITY_OSK_LANGUAGE_GERMAN` | `0x05` |  |
| `PSP_UTILITY_OSK_LANGUAGE_ITALIAN` | `0x06` |  |
| `PSP_UTILITY_OSK_LANGUAGE_DUTCH` | `0x07` |  |
| `PSP_UTILITY_OSK_LANGUAGE_PORTUGESE` | `0x08` |  |
| `PSP_UTILITY_OSK_LANGUAGE_RUSSIAN` | `0x09` |  |
| `PSP_UTILITY_OSK_LANGUAGE_KOREAN` | `0x0a` |  |

### `enum SceUtilityOskState`

Enumeration for OSK internal state.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_OSK_DIALOG_NONE` | `0` | No OSK is currently active. |
| `PSP_UTILITY_OSK_DIALOG_INITING` |  | The OSK is currently being initialized. |
| `PSP_UTILITY_OSK_DIALOG_INITED` |  | The OSK is initialised. |
| `PSP_UTILITY_OSK_DIALOG_VISIBLE` |  | The OSK is visible and ready for use. |
| `PSP_UTILITY_OSK_DIALOG_QUIT` |  | The OSK has been cancelled and should be shut down. |
| `PSP_UTILITY_OSK_DIALOG_FINISHED` |  | The OSK has successfully shut down. |

### `enum SceUtilityOskResult`

Enumeration for OSK field results.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_OSK_RESULT_UNCHANGED` | `0` |  |
| `PSP_UTILITY_OSK_RESULT_CANCELLED` |  |  |
| `PSP_UTILITY_OSK_RESULT_CHANGED` |  |  |

### `enum SceUtilityOskInputType`

Enumeration for input types (these are limited by initial choice of language)

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_OSK_INPUTTYPE_ALL` | `0x00000000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_LATIN_DIGIT` | `0x00000001` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_LATIN_SYMBOL` | `0x00000002` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_LATIN_LOWERCASE` | `0x00000004` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_LATIN_UPPERCASE` | `0x00000008` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_DIGIT` | `0x00000100` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_SYMBOL` | `0x00000200` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_LOWERCASE` | `0x00000400` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_UPPERCASE` | `0x00000800` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_HIRAGANA` | `0x00001000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_HALF_KATAKANA` | `0x00002000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_KATAKANA` | `0x00004000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_JAPANESE_KANJI` | `0x00008000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_RUSSIAN_LOWERCASE` | `0x00010000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_RUSSIAN_UPPERCASE` | `0x00020000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_KOREAN` | `0x00040000` |  |
| `PSP_UTILITY_OSK_INPUTTYPE_URL` | `0x00080000` |  |

## Functions

### `sceUtilityOskInitStart()`

```c
int sceUtilityOskInitStart(SceUtilityOskParams *params);
```

Create an on-screen keyboard.

**Parameters:**

- `params` – OSK parameters.

**Returns:** \< 0 on error.

### `sceUtilityOskShutdownStart()`

```c
int sceUtilityOskShutdownStart(void);
```

Remove a currently active keyboard.

After calling this function you must

poll [sceUtilityOskGetStatus()](#sceutilityoskgetstatus) until it returns PSP_UTILITY_DIALOG_NONE.

**Returns:** \< 0 on error.

### `sceUtilityOskUpdate()`

```c
int sceUtilityOskUpdate(int n);
```

Refresh the GUI for a keyboard currently active.

**Parameters:**

- `n` – Unknown, pass 1.

**Returns:** \< 0 on error.

### `sceUtilityOskGetStatus()`

```c
int sceUtilityOskGetStatus(void);
```

Get the status of a on-screen keyboard currently active.

**Returns:** the current status of the keyboard. See [pspUtilityDialogState](psputility.h.md#enum-psputilitydialogstate) for details.

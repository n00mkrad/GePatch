[PSPSDK documentation](../../README.md) › Files

# ctrl/pspctrl_kernel.h

```c
#include <psptypes.h>
```

## Macros

### `sceCtrlSetButtonMasks`

```c
#define sceCtrlSetButtonMasks sceCtrlSetButtonIntercept
```

### `sceCtrlGetButtonMask`

```c
#define sceCtrlGetButtonMask sceCtrlGetButtonIntercept
```

### `sceCtrlRegisterButtonCallback`

```c
#define sceCtrlRegisterButtonCallback sceCtrlSetSpecialButtonCallback
```

## Typedefs

### `SceKernelButtonCallbackFunction`

```c
typedef void(* SceKernelButtonCallbackFunction) (u32 cur_buttons, u32 last_buttons, void *opt))(u32 cur_buttons, u32 last_buttons, void *opt);
```

The callback function used by [sceCtrlSetSpecialButtonCallback()](#scectrlsetspecialbuttoncallback).

### `SceCtrlButtonMaskMode`

```c
typedef enum SceCtrlButtonMaskMode SceCtrlButtonMaskMode;
```

Button mask settings.

## Enumerations

### `enum SceCtrlButtonMaskMode`

Button mask settings.

| Enumerator | Value | Description |
|---|---|---|
| `SCE_CTRL_MASK_NO_MASK` | `0` | No mask for the specified buttons.<br>Button input is normally recognized. |
| `SCE_CTRL_MASK_IGNORE_BUTTONS` | `1` | The specified buttons are ignored, that means even if these buttons are pressed by the user they won't be shown as pressed internally.<br>```<br>You can only block user buttons for applications running in User Mode.<br>``` |
| `SCE_CTRL_MASK_APPLY_BUTTONS` | `2` | The specified buttons show up as being pressed, even if the user does not press them.<br>```<br>You can only turn ON user buttons for applications running in User Mode.<br>``` |

## Functions

### `sceCtrlSetButtonIntercept()`

```c
u32 sceCtrlSetButtonIntercept(u32 buttons, u32 mask_mode);
```

Sets a button mask mode for one or more buttons.

You can only mask user mode buttons in user applications. Masking of kernel mode buttons is ignored as well as buttons used in kernel mode applications.

**Parameters:**

- `buttons` – The button value for which the button mask mode will be applied for. One or more buttons of `SceCtrlButtons`.
- `mask_mode` – Specifies the type of the button mask. One of `SceCtrlButtonMaskMode`.

**Returns:** The previous button mask type for the given buttons. One of `SceCtrlButtonMaskMode`.

```c
sceCtrlSetButtonIntercept(0xFFFF, 1);  // Mask lower 16bits
sceCtrlSetButtonIntercept(0x10000, 2); // Always return HOME key
// Do something
sceCtrlSetButtonIntercept(0x10000, 0); // Unset HOME key
sceCtrlSetButtonIntercept(0xFFFF, 0);  // Unset mask
```

### `sceCtrlGetButtonIntercept()`

```c
u32 sceCtrlGetButtonIntercept(u32 buttons);
```

Get button mask mode.

**Parameters:**

- `buttons` – The buttons to check for. One or more buttons of `SceCtrlButtons`.

**Returns:** The button mask mode for the given buttons. One of `SceCtrlButtonMaskMode`.

### `sceCtrlSetSpecialButtonCallback()`

```c
int sceCtrlSetSpecialButtonCallback(u32 slot, u32 button_mask, SceKernelButtonCallbackFunction callback, void *opt);
```

Registers a button callback.

**Parameters:**

- `slot` – The slot used to register the callback. Between 0 - 3.
- `button_mask` – Bitwise OR'ed button values which will be checked for being pressed. One or more buttons of `SceCtrlButtons`.
- `callback` – A pointer to the callback function handling the button callbacks.
- `opt` – Optional user argument. Passed to the callback function as its third argument.

**Returns:** 0 on success, \< 0 on error.

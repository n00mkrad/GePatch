[PSPSDK documentation](../../README.md) › Files

# user/pspimpose.h

## Macros

### `PSP_IMPOSE_UMD_POPUP_ENABLED`

```c
#define PSP_IMPOSE_UMD_POPUP_ENABLED 1
```

### `PSP_IMPOSE_UMD_POPUP_DISABLED`

```c
#define PSP_IMPOSE_UMD_POPUP_DISABLED 0
```

## Functions

### `sceImposeGetBacklightOffTime()`

```c
int sceImposeGetBacklightOffTime(void);
```

Get the value of the backlight timer.

**Returns:** backlight timer in seconds or \< 0 on error

### `sceImposeSetBacklightOffTime()`

```c
int sceImposeSetBacklightOffTime(int value);
```

Set the value of the backlight timer.

**Parameters:**

- `value` – The backlight timer. (30 to a lot of seconds)

**Returns:** \< 0 on error

### `sceImposeGetLanguageMode()`

```c
int sceImposeGetLanguageMode(int *lang, int *button);
```

Get the language and button assignment parameters.

**Returns:** \< 0 on error

### `sceImposeSetLanguageMode()`

```c
int sceImposeSetLanguageMode(int lang, int button);
```

Set the language and button assignment parameters.

/!\\ parameter values not known.

**Parameters:**

- `lang` – Language
- `button` – Button assignment

**Returns:** \< 0 on error

### `sceImposeGetUMDPopup()`

```c
int sceImposeGetUMDPopup(void);
```

Get the value of the UMD popup.

**Returns:** umd popup state or \< 0 on error

### `sceImposeSetUMDPopup()`

```c
int sceImposeSetUMDPopup(int value);
```

Set the value of the UMD popup.

**Parameters:**

- `value` – The popup mode.

**Returns:** \< 0 on error

### `sceImposeGetHomePopup()`

```c
int sceImposeGetHomePopup(void);
```

Get the value of the Home popup.

**Returns:** home popup state or \< 0 on error

### `sceImposeSetHomePopup()`

```c
int sceImposeSetHomePopup(int value);
```

Set the value of the Home popup.

**Parameters:**

- `value` – The popup mode.

**Returns:** \< 0 on error

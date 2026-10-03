[PSPSDK documentation](../../README.md) › Files

# utility/psputility_sysparam.h

```c
#include <psptypes.h>
```

## Macros

### `PSP_SYSTEMPARAM_ID_STRING_NICKNAME`

```c
#define PSP_SYSTEMPARAM_ID_STRING_NICKNAME 1
```

IDs for use inSystemParam functions PSP_SYSTEMPARAM_ID_INT are for use with SystemParamInt funcs PSP_SYSTEMPARAM_ID_STRING are for use with SystemParamString funcs.

### `PSP_SYSTEMPARAM_ID_INT_ADHOC_CHANNEL`

```c
#define PSP_SYSTEMPARAM_ID_INT_ADHOC_CHANNEL 2
```

### `PSP_SYSTEMPARAM_ID_INT_WLAN_POWERSAVE`

```c
#define PSP_SYSTEMPARAM_ID_INT_WLAN_POWERSAVE 3
```

### `PSP_SYSTEMPARAM_ID_INT_DATE_FORMAT`

```c
#define PSP_SYSTEMPARAM_ID_INT_DATE_FORMAT 4
```

### `PSP_SYSTEMPARAM_ID_INT_TIME_FORMAT`

```c
#define PSP_SYSTEMPARAM_ID_INT_TIME_FORMAT 5
```

### `PSP_SYSTEMPARAM_ID_INT_TIMEZONE`

```c
#define PSP_SYSTEMPARAM_ID_INT_TIMEZONE 6
```

### `PSP_SYSTEMPARAM_ID_INT_DAYLIGHTSAVINGS`

```c
#define PSP_SYSTEMPARAM_ID_INT_DAYLIGHTSAVINGS 7
```

### `PSP_SYSTEMPARAM_ID_INT_LANGUAGE`

```c
#define PSP_SYSTEMPARAM_ID_INT_LANGUAGE 8
```

### `PSP_SYSTEMPARAM_ID_INT_BUTTON_SWAP`

```c
#define PSP_SYSTEMPARAM_ID_INT_BUTTON_SWAP 9
```

Whether to swap X and O depends on region 0 for O as confirm 1 for X as confirm.

### `PSP_SYSTEMPARAM_ID_INT_UNKNOWN`

```c
#define PSP_SYSTEMPARAM_ID_INT_UNKNOWN PSP_SYSTEMPARAM_ID_INT_BUTTON_SWAP
```

Old name of PSP_SYSTEMPARAM_ID_INT_BUTTON_SWAP for legacy compatibility.

### `PSP_SYSTEMPARAM_RETVAL_OK`

```c
#define PSP_SYSTEMPARAM_RETVAL_OK 0
```

Return values for the SystemParam functions.

### `PSP_SYSTEMPARAM_RETVAL_FAIL`

```c
#define PSP_SYSTEMPARAM_RETVAL_FAIL 0x80110103
```

### `PSP_SYSTEMPARAM_ADHOC_CHANNEL_AUTOMATIC`

```c
#define PSP_SYSTEMPARAM_ADHOC_CHANNEL_AUTOMATIC 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_ADHOC_CHANNEL.

### `PSP_SYSTEMPARAM_ADHOC_CHANNEL_1`

```c
#define PSP_SYSTEMPARAM_ADHOC_CHANNEL_1 1
```

### `PSP_SYSTEMPARAM_ADHOC_CHANNEL_6`

```c
#define PSP_SYSTEMPARAM_ADHOC_CHANNEL_6 6
```

### `PSP_SYSTEMPARAM_ADHOC_CHANNEL_11`

```c
#define PSP_SYSTEMPARAM_ADHOC_CHANNEL_11 11
```

### `PSP_SYSTEMPARAM_WLAN_POWERSAVE_OFF`

```c
#define PSP_SYSTEMPARAM_WLAN_POWERSAVE_OFF 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_WLAN_POWERSAVE.

### `PSP_SYSTEMPARAM_WLAN_POWERSAVE_ON`

```c
#define PSP_SYSTEMPARAM_WLAN_POWERSAVE_ON 1
```

### `PSP_SYSTEMPARAM_DATE_FORMAT_YYYYMMDD`

```c
#define PSP_SYSTEMPARAM_DATE_FORMAT_YYYYMMDD 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_DATE_FORMAT.

### `PSP_SYSTEMPARAM_DATE_FORMAT_MMDDYYYY`

```c
#define PSP_SYSTEMPARAM_DATE_FORMAT_MMDDYYYY 1
```

### `PSP_SYSTEMPARAM_DATE_FORMAT_DDMMYYYY`

```c
#define PSP_SYSTEMPARAM_DATE_FORMAT_DDMMYYYY 2
```

### `PSP_SYSTEMPARAM_TIME_FORMAT_24HR`

```c
#define PSP_SYSTEMPARAM_TIME_FORMAT_24HR 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_TIME_FORMAT.

### `PSP_SYSTEMPARAM_TIME_FORMAT_12HR`

```c
#define PSP_SYSTEMPARAM_TIME_FORMAT_12HR 1
```

### `PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_STD`

```c
#define PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_STD 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_DAYLIGHTSAVINGS.

### `PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_SAVING`

```c
#define PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_SAVING 1
```

### `PSP_SYSTEMPARAM_LANGUAGE_JAPANESE`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_JAPANESE 0
```

Valid values for PSP_SYSTEMPARAM_ID_INT_LANGUAGE.

### `PSP_SYSTEMPARAM_LANGUAGE_ENGLISH`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_ENGLISH 1
```

### `PSP_SYSTEMPARAM_LANGUAGE_FRENCH`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_FRENCH 2
```

### `PSP_SYSTEMPARAM_LANGUAGE_SPANISH`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_SPANISH 3
```

### `PSP_SYSTEMPARAM_LANGUAGE_GERMAN`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_GERMAN 4
```

### `PSP_SYSTEMPARAM_LANGUAGE_ITALIAN`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_ITALIAN 5
```

### `PSP_SYSTEMPARAM_LANGUAGE_DUTCH`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_DUTCH 6
```

### `PSP_SYSTEMPARAM_LANGUAGE_PORTUGUESE`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_PORTUGUESE 7
```

### `PSP_SYSTEMPARAM_LANGUAGE_RUSSIAN`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_RUSSIAN 8
```

### `PSP_SYSTEMPARAM_LANGUAGE_KOREAN`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_KOREAN 9
```

### `PSP_SYSTEMPARAM_LANGUAGE_CHINESE_TRADITIONAL`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_CHINESE_TRADITIONAL 10
```

### `PSP_SYSTEMPARAM_LANGUAGE_CHINESE_SIMPLIFIED`

```c
#define PSP_SYSTEMPARAM_LANGUAGE_CHINESE_SIMPLIFIED 11
```

## Functions

### `sceUtilitySetSystemParamInt()`

```c
int sceUtilitySetSystemParamInt(int id, int value);
```

Set Integer System Parameter.

**Parameters:**

- `id` – which parameter to set
- `value` – integer value to set

**Returns:** 0 on success, PSP_SYSTEMPARAM_RETVAL_FAIL on failure

### `sceUtilitySetSystemParamString()`

```c
int sceUtilitySetSystemParamString(int id, const char *str);
```

Set String System Parameter.

**Parameters:**

- `id` – which parameter to set
- `str` – char \* value to set

**Returns:** 0 on success, PSP_SYSTEMPARAM_RETVAL_FAIL on failure

### `sceUtilityGetSystemParamInt()`

```c
int sceUtilityGetSystemParamInt(int id, int *value);
```

Get Integer System Parameter.

**Parameters:**

- `id` – which parameter to get
- `value` – pointer to integer value to place result in

**Returns:** 0 on success, PSP_SYSTEMPARAM_RETVAL_FAIL on failure

### `sceUtilityGetSystemParamString()`

```c
int sceUtilityGetSystemParamString(int id, char *str, int len);
```

Get String System Parameter.

**Parameters:**

- `id` – which parameter to get
- `str` – char \* buffer to place result in
- `len` – length of str buffer

**Returns:** 0 on success, PSP_SYSTEMPARAM_RETVAL_FAIL on failure

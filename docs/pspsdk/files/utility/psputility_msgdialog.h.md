[PSPSDK documentation](../../README.md) › Files

# utility/psputility_msgdialog.h

## Data Structures

### `struct _pspUtilityMsgDialogParams`

Structure to hold the parameters for a message dialog.

| Field | Description |
|---|---|
| `pspUtilityDialogCommon base` |  |
| `int unknown` |  |
| `pspUtilityMsgDialogMode mode` |  |
| `unsigned int errorValue` |  |
| `char message[512]` | The message to display (may contain embedded linefeeds) |
| `int options` |  |
| `pspUtilityMsgDialogPressed buttonPressed` |  |

## Typedefs

### `pspUtilityMsgDialogParams`

```c
typedef struct _pspUtilityMsgDialogParams pspUtilityMsgDialogParams;
```

Structure to hold the parameters for a message dialog.

## Enumerations

### `enum pspUtilityMsgDialogMode`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_MSGDIALOG_MODE_ERROR` | `0` |  |
| `PSP_UTILITY_MSGDIALOG_MODE_TEXT` |  |  |

### `enum pspUtilityMsgDialogOption`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_MSGDIALOG_OPTION_ERROR` | `0` |  |
| `PSP_UTILITY_MSGDIALOG_OPTION_TEXT` | `0x00000001` |  |
| `PSP_UTILITY_MSGDIALOG_OPTION_YESNO_BUTTONS` | `0x00000010` |  |
| `PSP_UTILITY_MSGDIALOG_OPTION_DEFAULT_NO` | `0x00000100` |  |

### `enum pspUtilityMsgDialogPressed`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_MSGDIALOG_RESULT_UNKNOWN1` | `0` |  |
| `PSP_UTILITY_MSGDIALOG_RESULT_YES` |  |  |
| `PSP_UTILITY_MSGDIALOG_RESULT_NO` |  |  |
| `PSP_UTILITY_MSGDIALOG_RESULT_BACK` |  |  |

## Functions

### `sceUtilityMsgDialogInitStart()`

```c
int sceUtilityMsgDialogInitStart(pspUtilityMsgDialogParams *params);
```

Create a message dialog.

**Parameters:**

- `params` – dialog parameters

**Returns:** 0 on success

### `sceUtilityMsgDialogShutdownStart()`

```c
void sceUtilityMsgDialogShutdownStart(void);
```

Remove a message dialog currently active.

After calling this function you need to keep calling GetStatus and Update until you get a status of 4.

### `sceUtilityMsgDialogGetStatus()`

```c
int sceUtilityMsgDialogGetStatus(void);
```

Get the current status of a message dialog currently active.

**Returns:** 2 if the GUI is visible (you need to call sceUtilityMsgDialogGetStatus). 3 if the user cancelled the dialog, and you need to call sceUtilityMsgDialogShutdownStart. 4 if the dialog has been successfully shut down.

### `sceUtilityMsgDialogUpdate()`

```c
void sceUtilityMsgDialogUpdate(int n);
```

Refresh the GUI for a message dialog currently active.

**Parameters:**

- `n` – unknown, pass 1

### `sceUtilityMsgDialogAbort()`

```c
int sceUtilityMsgDialogAbort(void);
```

Abort a message dialog currently active.

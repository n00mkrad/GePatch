[PSPSDK documentation](../../README.md) › Files

# utility/psputility_htmlviewer.h

## Data Structures

### `struct pspUtilityHtmlViewerParam`

| Field | Description |
|---|---|
| `pspUtilityDialogCommon base` |  |
| `void * memaddr` | Pointer to the memory pool to be used. |
| `unsigned int memsize` | Size of the memory pool. |
| `int unknown1` | Unknown.<br>Pass 0 |
| `int unknown2` | Unknown.<br>Pass 0 |
| `char * initialurl` | URL to be opened initially. |
| `unsigned int numtabs` | Number of tabs (maximum of 3) |
| `unsigned int interfacemode` | One of [pspUtilityHtmlViewerInterfaceModes](#enum-psputilityhtmlviewerinterfacemodes). |
| `unsigned int options` | Values from [pspUtilityHtmlViewerOptions](#enum-psputilityhtmlvieweroptions).<br>Bitwise OR together |
| `char * dldirname` | Directory to be used for downloading. |
| `char * dlfilename` | Filename to be used for downloading. |
| `char * uldirname` | Directory to be used for uploading. |
| `char * ulfilename` | Filename to be used for uploading. |
| `unsigned int cookiemode` | One of [pspUtilityHtmlViewerCookieModes](#enum-psputilityhtmlviewercookiemodes). |
| `unsigned int unknown3` | Unknown.<br>Pass 0 |
| `char * homeurl` | URL to set the home page to. |
| `unsigned int textsize` | One of [pspUtilityHtmlViewerTextSizes](#enum-psputilityhtmlviewertextsizes). |
| `unsigned int displaymode` | One of [pspUtilityHtmlViewerDisplayModes](#enum-psputilityhtmlviewerdisplaymodes). |
| `unsigned int connectmode` | One of [pspUtilityHtmlViewerConnectModes](#enum-psputilityhtmlviewerconnectmodes). |
| `unsigned int disconnectmode` | One of [pspUtilityHtmlViewerDisconnectModes](#enum-psputilityhtmlviewerdisconnectmodes). |
| `unsigned int memused` | The maximum amount of memory the browser used. |
| `int unknown4[10]` | Unknown.<br>Pass 0 |

## Typedefs

### `pspUtilityHtmlViewerParam`

```c
typedef struct pspUtilityHtmlViewerParam pspUtilityHtmlViewerParam;
```

## Enumerations

### `enum pspUtilityHtmlViewerDisconnectModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_DISCONNECTMODE_ENABLE` | `0` | Enable automatic disconnect. |
| `PSP_UTILITY_HTMLVIEWER_DISCONNECTMODE_DISABLE` |  | Disable automatic disconnect. |
| `PSP_UTILITY_HTMLVIEWER_DISCONNECTMODE_CONFIRM` |  | Confirm disconnection. |

### `enum pspUtilityHtmlViewerInterfaceModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_INTERFACEMODE_FULL` | `0` | Full user interface. |
| `PSP_UTILITY_HTMLVIEWER_INTERFACEMODE_LIMITED` |  | Limited user interface. |
| `PSP_UTILITY_HTMLVIEWER_INTERFACEMODE_NONE` |  | No user interface. |

### `enum pspUtilityHtmlViewerCookieModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_COOKIEMODE_DISABLED` | `0` | Disable accepting cookies. |
| `PSP_UTILITY_HTMLVIEWER_COOKIEMODE_ENABLED` |  | Enable accepting cookies. |
| `PSP_UTILITY_HTMLVIEWER_COOKIEMODE_CONFIRM` |  | Confirm accepting a cookie every time. |
| `PSP_UTILITY_HTMLVIEWER_COOKIEMODE_DEFAULT` |  | Use the system default for accepting cookies. |

### `enum pspUtilityHtmlViewerTextSizes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_TEXTSIZE_LARGE` | `0` | Large text size. |
| `PSP_UTILITY_HTMLVIEWER_TEXTSIZE_NORMAL` |  | Normal text size. |
| `PSP_UTILITY_HTMLVIEWER_TEXTSIZE_SMALL` |  | Small text size. |

### `enum pspUtilityHtmlViewerDisplayModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_DISPLAYMODE_NORMAL` | `0` | Normal display. |
| `PSP_UTILITY_HTMLVIEWER_DISPLAYMODE_FIT` |  | Fit display. |
| `PSP_UTILITY_HTMLVIEWER_DISPLAYMODE_SMART_FIT` |  | Smart fit display. |

### `enum pspUtilityHtmlViewerConnectModes`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_CONNECTMODE_LAST` | `0` | Auto connect to last used connection. |
| `PSP_UTILITY_HTMLVIEWER_CONNECTMODE_MANUAL_ONCE` |  | Manually select the connection (once) |
| `PSP_UTILITY_HTMLVIEWER_CONNECTMODE_MANUAL_ALL` |  | Manually select the connection (every time) |

### `enum pspUtilityHtmlViewerOptions`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_HTMLVIEWER_OPEN_SCE_START_PAGE` | `0x000001` | Open SCE net start page. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_STARTUP_LIMITS` | `0x000002` | Disable startup limitations. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_EXIT_DIALOG` | `0x000004` | Disable exit confirmation dialog. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_CURSOR` | `0x000008` | Disable cursor. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_DOWNLOAD_COMPLETE_DIALOG` | `0x000010` | Disable download completion confirmation dialog. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_DOWNLOAD_START_DIALOG` | `0x000020` | Disable download confirmation dialog. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_DOWNLOAD_DESTINATION_DIALOG` | `0x000040` | Disable save destination confirmation dialog. |
| `PSP_UTILITY_HTMLVIEWER_LOCK_DOWNLOAD_DESTINATION_DIALOG` | `0x000080` | Disable modification of the download destination. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_TAB_DISPLAY` | `0x000100` | Disable tab display. |
| `PSP_UTILITY_HTMLVIEWER_ENABLE_ANALOG_HOLD` | `0x000200` | Hold analog controller when HOLD button is down. |
| `PSP_UTILITY_HTMLVIEWER_ENABLE_FLASH` | `0x000400` | Enable Flash Player. |
| `PSP_UTILITY_HTMLVIEWER_DISABLE_LRTRIGGER` | `0x000800` | Disable L/R triggers for back/forward. |

## Functions

### `sceUtilityHtmlViewerInitStart()`

```c
int sceUtilityHtmlViewerInitStart(pspUtilityHtmlViewerParam *params);
```

Init the html viewer.

**Parameters:**

- `params` – html viewer parameters

**Returns:** 0 on success, \< 0 on error.

### `sceUtilityHtmlViewerShutdownStart()`

```c
int sceUtilityHtmlViewerShutdownStart(void);
```

Shutdown html viewer.

### `sceUtilityHtmlViewerUpdate()`

```c
int sceUtilityHtmlViewerUpdate(int n);
```

Refresh the GUI for html viewer.

**Parameters:**

- `n` – unknown, pass 1

### `sceUtilityHtmlViewerGetStatus()`

```c
int sceUtilityHtmlViewerGetStatus(void);
```

Get the current status of the html viewer.

**Returns:** 2 if the GUI is visible (you need to call sceUtilityHtmlViewerGetStatus). 3 if the user cancelled the dialog, and you need to call sceUtilityHtmlViewerShutdownStart. 4 if the dialog has been successfully shut down.

[PSPSDK documentation](../../README.md) › Files

# utility/psputility_gamesharing.h

## Data Structures

### `struct _pspUtilityGameSharingParams`

Structure to hold the parameters for Game Sharing.

```c
struct _pspUtilityGameSharingParams {
    pspUtilityDialogCommon base;
    int unknown1;
    int unknown2;
    char name[8];
    int unknown3;
    int unknown4;
    int unknown5;
    int result;
    char * filepath;
    pspUtilityGameSharingMode mode;
    pspUtilityGameSharingDataType datatype;
    void * data;
    unsigned int datasize;
};
```

## Typedefs

### `pspUtilityGameSharingParams`

```c
typedef struct _pspUtilityGameSharingParams pspUtilityGameSharingParams;
```

Structure to hold the parameters for Game Sharing.

## Enumerations

### `enum pspUtilityGameSharingMode`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_GAMESHARING_MODE_SINGLE` | `1` |  |
| `PSP_UTILITY_GAMESHARING_MODE_MULTIPLE` | `2` |  |

### `enum pspUtilityGameSharingDataType`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_GAMESHARING_DATA_TYPE_FILE` | `1` |  |
| `PSP_UTILITY_GAMESHARING_DATA_TYPE_MEMORY` | `2` |  |

## Functions

### `sceUtilityGameSharingInitStart()`

```c
int sceUtilityGameSharingInitStart(pspUtilityGameSharingParams *params);
```

Init the game sharing.

**Parameters:**

- `params` – game sharing parameters

**Returns:** 0 on success, \< 0 on error.

### `sceUtilityGameSharingShutdownStart()`

```c
void sceUtilityGameSharingShutdownStart(void);
```

Shutdown game sharing.

### `sceUtilityGameSharingGetStatus()`

```c
int sceUtilityGameSharingGetStatus(void);
```

Get the current status of game sharing.

**Returns:** 2 if the GUI is visible (you need to call sceUtilityGameSharingGetStatus). 3 if the user cancelled the dialog, and you need to call sceUtilityGameSharingShutdownStart. 4 if the dialog has been successfully shut down.

### `sceUtilityGameSharingUpdate()`

```c
void sceUtilityGameSharingUpdate(int n);
```

Refresh the GUI for game sharing.

**Parameters:**

- `n` – unknown, pass 1

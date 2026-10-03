[PSPSDK documentation](../../README.md) › Files

# utility/psputility_savedata.h

```c
#include <psptypes.h>
#include <pspkerneltypes.h>
```

## Data Structures

### `struct PspUtilitySavedataSFOParam`

title, savedataTitle, detail: parts of the unencrypted SFO data, it contains what the VSH and standard load screen shows

```c
struct PspUtilitySavedataSFOParam {
    char title[0x80];
    char savedataTitle[0x80];
    char detail[0x400];
    unsigned char parentalLevel;
    unsigned char unknown[3];
};
```

### `struct PspUtilitySavedataFileData`

```c
struct PspUtilitySavedataFileData {
    void * buf;
    SceSize bufSize;
    SceSize size;
    int unknown;
};
```

### `struct PspUtilitySavedataSizeEntry`

```c
struct PspUtilitySavedataSizeEntry {
    uint64_t size;
    char name[16];
};
```

### `struct PspUtilitySavedataSizeInfo`

```c
struct PspUtilitySavedataSizeInfo {
    int numSecureEntries;
    int numNormalEntries;
    PspUtilitySavedataSizeEntry * secureEntries;
    PspUtilitySavedataSizeEntry * normalEntries;
    int sectorSize;
    int freeSectors;
    int freeKB;
    char freeString[8];
    int neededKB;
    char neededString[8];
    int overwriteKB;
    char overwriteString[8];
};
```

### `struct SceUtilitySavedataIdListEntry`

```c
struct SceUtilitySavedataIdListEntry {
    int st_mode;
    ScePspDateTime sce_st_ctime;
    ScePspDateTime sce_st_atime;
    ScePspDateTime sce_st_mtime;
    char name[20];
};
```

### `struct SceUtilitySavedataIdListInfo`

```c
struct SceUtilitySavedataIdListInfo {
    int maxCount;
    int resultCount;
    SceUtilitySavedataIdListEntry * entries;
};
```

### `struct SceUtilitySavedataFileListEntry`

```c
struct SceUtilitySavedataFileListEntry {
    int st_mode;
    uint32_t st_unk0;
    uint64_t st_size;
    ScePspDateTime sce_st_ctime;
    ScePspDateTime sce_st_atime;
    ScePspDateTime sce_st_mtime;
    char name[16];
};
```

### `struct SceUtilitySavedataFileListInfo`

```c
struct SceUtilitySavedataFileListInfo {
    uint32_t maxSecureEntries;
    uint32_t maxNormalEntries;
    uint32_t maxSystemEntries;
    uint32_t resultNumSecureEntries;
    uint32_t resultNumNormalEntries;
    uint32_t resultNumSystemEntries;
    SceUtilitySavedataFileListEntry * secureEntries;
    SceUtilitySavedataFileListEntry * normalEntries;
    SceUtilitySavedataFileListEntry * systemEntries;
};
```

### `struct SceUtilitySavedataMsFreeInfo`

```c
struct SceUtilitySavedataMsFreeInfo {
    int clusterSize;
    int freeClusters;
    int freeSpaceKB;
    char freeSpaceStr[8];
};
```

### `struct SceUtilitySavedataUsedDataInfo`

```c
struct SceUtilitySavedataUsedDataInfo {
    int usedClusters;
    int usedSpaceKB;
    char usedSpaceStr[8];
    int usedSpace32KB;
    char usedSpace32Str[8];
};
```

### `struct SceUtilitySavedataMsDataInfo`

```c
struct SceUtilitySavedataMsDataInfo {
    char gameName[13];
    char pad[3];
    char saveName[20];
    SceUtilitySavedataUsedDataInfo info;
};
```

### `struct PspUtilitySavedataListSaveNewData`

```c
struct PspUtilitySavedataListSaveNewData {
    PspUtilitySavedataFileData icon0;
    char * title;
};
```

### `struct SceUtilitySavedataParam`

Structure to hold the parameters for the [sceUtilitySavedataInitStart](#sceutilitysavedatainitstart) function.

| Field | Description |
|---|---|
| `pspUtilityDialogCommon base` |  |
| `PspUtilitySavedataMode mode` |  |
| `int bind` |  |
| `int overwrite` |  |
| `char gameName[13]` | gameName: name used from the game for saves, equal for all saves |
| `char reserved[3]` |  |
| `char saveName[20]` | saveName: name of the particular save, normally a number |
| `char(* saveNameList)[20]` | saveNameList: used by multiple modes |
| `char fileName[13]` | fileName: name of the data file of the game for example DATA.BIN |
| `char reserved1[3]` |  |
| `void * dataBuf` | pointer to a buffer that will contain data file unencrypted data |
| `SceSize dataBufSize` | size of allocated space to dataBuf |
| `SceSize dataSize` |  |
| `PspUtilitySavedataSFOParam sfoParam` |  |
| `PspUtilitySavedataFileData icon0FileData` |  |
| `PspUtilitySavedataFileData icon1FileData` |  |
| `PspUtilitySavedataFileData pic1FileData` |  |
| `PspUtilitySavedataFileData snd0FileData` |  |
| `PspUtilitySavedataListSaveNewData * newData` | Pointer to an [PspUtilitySavedataListSaveNewData](#struct-psputilitysavedatalistsavenewdata) structure. |
| `PspUtilitySavedataFocus focus` | Initial focus for lists. |
| `int abortStatus` |  |
| `SceUtilitySavedataMsFreeInfo * msFree` |  |
| `SceUtilitySavedataMsDataInfo * msData` |  |
| `SceUtilitySavedataUsedDataInfo * utilityData` |  |

## Typedefs

### `PspUtilitySavedataSFOParam`

```c
typedef struct PspUtilitySavedataSFOParam PspUtilitySavedataSFOParam;
```

title, savedataTitle, detail: parts of the unencrypted SFO data, it contains what the VSH and standard load screen shows

### `PspUtilitySavedataFileData`

```c
typedef struct PspUtilitySavedataFileData PspUtilitySavedataFileData;
```

### `PspUtilitySavedataSizeEntry`

```c
typedef struct PspUtilitySavedataSizeEntry PspUtilitySavedataSizeEntry;
```

### `PspUtilitySavedataSizeInfo`

```c
typedef struct PspUtilitySavedataSizeInfo PspUtilitySavedataSizeInfo;
```

### `SceUtilitySavedataIdListEntry`

```c
typedef struct SceUtilitySavedataIdListEntry SceUtilitySavedataIdListEntry;
```

### `SceUtilitySavedataIdListInfo`

```c
typedef struct SceUtilitySavedataIdListInfo SceUtilitySavedataIdListInfo;
```

### `SceUtilitySavedataFileListEntry`

```c
typedef struct SceUtilitySavedataFileListEntry SceUtilitySavedataFileListEntry;
```

### `SceUtilitySavedataFileListInfo`

```c
typedef struct SceUtilitySavedataFileListInfo SceUtilitySavedataFileListInfo;
```

### `SceUtilitySavedataMsFreeInfo`

```c
typedef struct SceUtilitySavedataMsFreeInfo SceUtilitySavedataMsFreeInfo;
```

### `SceUtilitySavedataUsedDataInfo`

```c
typedef struct SceUtilitySavedataUsedDataInfo SceUtilitySavedataUsedDataInfo;
```

### `SceUtilitySavedataMsDataInfo`

```c
typedef struct SceUtilitySavedataMsDataInfo SceUtilitySavedataMsDataInfo;
```

### `PspUtilitySavedataListSaveNewData`

```c
typedef struct PspUtilitySavedataListSaveNewData PspUtilitySavedataListSaveNewData;
```

### `SceUtilitySavedataParam`

```c
typedef struct SceUtilitySavedataParam SceUtilitySavedataParam;
```

Structure to hold the parameters for the [sceUtilitySavedataInitStart](#sceutilitysavedatainitstart) function.

## Enumerations

### `enum PspUtilitySavedataMode`

Save data utility modes.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_SAVEDATA_AUTOLOAD` | `0` |  |
| `PSP_UTILITY_SAVEDATA_AUTOSAVE` |  |  |
| `PSP_UTILITY_SAVEDATA_LOAD` |  |  |
| `PSP_UTILITY_SAVEDATA_SAVE` |  |  |
| `PSP_UTILITY_SAVEDATA_LISTLOAD` |  |  |
| `PSP_UTILITY_SAVEDATA_LISTSAVE` |  |  |
| `PSP_UTILITY_SAVEDATA_LISTDELETE` |  |  |
| `PSP_UTILITY_SAVEDATA_LISTALLDELETE` |  |  |
| `SCE_UTILITY_SAVEDATA_SIZES` |  |  |
| `SCE_UTILITY_SAVEDATA_AUTODELETE` |  |  |
| `SCE_UTILITY_SAVEDATA_DELETE` |  |  |
| `SCE_UTILITY_SAVEDATA_LIST` |  |  |
| `SCE_UTILITY_SAVEDATA_FILES` |  |  |
| `SCE_UTILITY_SAVEDATA_MAKEDATASECURE` |  |  |
| `SCE_UTILITY_SAVEDATA_MAKEDATA` |  |  |
| `SCE_UTILITY_SAVEDATA_READDATASECURE` |  |  |
| `SCE_UTILITY_SAVEDATA_READDATA` |  |  |
| `SCE_UTILITY_SAVEDATA_WRITEDATASECURE` |  |  |
| `SCE_UTILITY_SAVEDATA_WRITEDATA` |  |  |
| `SCE_UTILITY_SAVEDATA_ERASESECURE` |  |  |
| `SCE_UTILITY_SAVEDATA_ERASE` |  |  |
| `SCE_UTILITY_SAVEDATA_DELETEDATA` |  |  |
| `SCE_UTILITY_SAVEDATA_GETSIZE` |  |  |

### `enum PspUtilitySavedataFocus`

Initial focus position for list selection types.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_UTILITY_SAVEDATA_FOCUS_UNKNOWN` | `0` |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_FIRSTLIST` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_LASTLIST` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_LATEST` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_OLDEST` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_FIRSTDATA` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_LASTDATA` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_FIRSTEMPTY` |  |  |
| `PSP_UTILITY_SAVEDATA_FOCUS_LASTEMPTY` |  |  |

## Functions

### `sceUtilitySavedataInitStart()`

```c
int sceUtilitySavedataInitStart(SceUtilitySavedataParam *params);
```

Saves or Load savedata to/from the passed structure After having called this continue calling sceUtilitySavedataGetStatus to check if the operation is completed.

**Parameters:**

- `params` – savedata parameters

**Returns:** 0 on success

### `sceUtilitySavedataGetStatus()`

```c
int sceUtilitySavedataGetStatus(void);
```

Check the current status of the saving/loading/shutdown process Continue calling this to check current status of the process before calling this call also sceUtilitySavedataUpdate.

**Returns:** 2 if the process is still being processed. 3 on save/load success, then you can call sceUtilitySavedataShutdownStart. 4 on complete shutdown.

### `sceUtilitySavedataShutdownStart()`

```c
int sceUtilitySavedataShutdownStart(void);
```

Shutdown the savedata utility.

after calling this continue calling [sceUtilitySavedataGetStatus](#sceutilitysavedatagetstatus) to check when it has shutdown

**Returns:** 0 on success

### `sceUtilitySavedataUpdate()`

```c
void sceUtilitySavedataUpdate(int unknown);
```

Refresh status of the savedata function.

**Parameters:**

- `unknown` – unknown, pass 1

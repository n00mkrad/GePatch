[PSPSDK documentation](../../README.md) › Files

# user/pspmoduleexport.h

## Data Structures

### `struct _PspLibraryEntry`

Structure to hold a single export entry.

```c
struct _PspLibraryEntry {
    const char * name;
    unsigned short version;
    unsigned short attribute;
    unsigned char entLen;
    unsigned char varCount;
    unsigned short funcCount;
    void * entrytable;
};
```

[PSPSDK documentation](../../README.md) › Files

# openpsid/pspopenpsid.h

## Data Structures

### `struct PspOpenPSID`

```c
struct PspOpenPSID {
    unsigned char data[16];
};
```

## Typedefs

### `PspOpenPSID`

```c
typedef struct PspOpenPSID PspOpenPSID;
```

## Functions

### `sceOpenPSIDGetOpenPSID()`

```c
int sceOpenPSIDGetOpenPSID(PspOpenPSID *openpsid);
```

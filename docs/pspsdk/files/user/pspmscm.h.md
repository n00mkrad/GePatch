[PSPSDK documentation](../../README.md) › Files

# user/pspmscm.h

## Macros

### `MS_CB_EVENT_INSERTED`

```c
#define MS_CB_EVENT_INSERTED 1
```

### `MS_CB_EVENT_EJECTED`

```c
#define MS_CB_EVENT_EJECTED 2
```

## Functions

### `MScmIsMediumInserted()`

```c
static __inline__ int MScmIsMediumInserted(void);
```

Returns whether a memory stick is current inserted.

**Returns:** 1 if memory stick inserted, 0 if not or if \< 0 on error

### `MScmRegisterMSInsertEjectCallback()`

```c
static __inline__ int MScmRegisterMSInsertEjectCallback(SceUID cbid);
```

Registers a memory stick ejection callback.

**Parameters:**

- `cbid` – The uid of an allocated callback

**Returns:** 0 on success, \< 0 on error

### `MScmUnregisterMSInsertEjectCallback()`

```c
static __inline__ int MScmUnregisterMSInsertEjectCallback(SceUID cbid);
```

Unregister a memory stick ejection callback.

**Parameters:**

- `cbid` – The uid of an allocated callback

**Returns:** 0 on success, \< 0 on error

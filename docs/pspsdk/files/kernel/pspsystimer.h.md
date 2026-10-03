[PSPSDK documentation](../../README.md) › Files

# kernel/pspsystimer.h

## Typedefs

### `SceSysTimerId`

```c
typedef int SceSysTimerId;
```

## Functions

### `sceSTimerAlloc()`

```c
SceSysTimerId sceSTimerAlloc(void);
```

Allocate a new SysTimer timer instance.

**Returns:** SysTimerId on success, \< 0 on error

### `sceSTimerFree()`

```c
void sceSTimerFree(SceSysTimerId timer);
```

Free an instance of a SysTimer timer.

**Parameters:**

- `timer` – The timer id.

### `sceSTimerStartCount()`

```c
void sceSTimerStartCount(SceSysTimerId timer);
```

Start the SysTimer timer count.

**Parameters:**

- `timer` – The timer id.

### `sceSTimerStopCount()`

```c
void sceSTimerStopCount(SceSysTimerId timer);
```

Stop the current SysTimer timer count.

**Parameters:**

- `timer` – The timer id.

### `sceSTimerResetCount()`

```c
void sceSTimerResetCount(SceSysTimerId timer);
```

Reset the current SysTimer timer count.

**Parameters:**

- `timer` – The timer id.

### `sceSTimerGetCount()`

```c
void sceSTimerGetCount(SceSysTimerId timer, int *count);
```

Get the current SysTimer timer count.

**Parameters:**

- `timer` – The timer id.
- `count` – The pointer to an integer into which the count will be written.

### `sceSTimerSetHandler()`

```c
void sceSTimerSetHandler(SceSysTimerId timer, int cycle, int(*handler)(void), int unk1);
```

Setup a SysTimer handler.

**Parameters:**

- `timer` – The timer id.
- `cycle` – The timer cycle in microseconds (???). Maximum: 4194303 which represents ~1/10 seconds.
- `handler` – The handler function. Has to return -1.
- `unk1` – Unknown. Pass 0.

### `sceSTimerSetTMCY()`

```c
void sceSTimerSetTMCY(SceSysTimerId timer, int unk1);
```

Unknown purpose.

Probably something to set the cycle of an active timer.

**Parameters:**

- `timer` – The ID of the timer.
- `unk1` – Unknown. Should not be less than `0` and greater `4194304`.

**Returns:** `0` on success.

### `sceSTimerSetPrscl()`

```c
void sceSTimerSetPrscl(SceSysTimerId timer, int unk1, int unk2);
```

Set the prescale of a hardware timer.

It can be only set on timers which are in the "not in use" state.

The input signal is divided into the resulting ratio. The ratio has to be less than 1/11.

**Parameters:**

- `timer` – The ID of the timer to set the prescale.
- `numerator` – The numerator of the prescale. Must not be `0`.
- `denominator` – The denominator of the prescale. Must not be `0`.

**Returns:** `0` on success.

[PSPSDK documentation](../../README.md) › Files

# rtc/psprtc.h

```c
#include <time.h>
#include <psptypes.h>
```

## Enumerations

### `enum pspRtcCheckValidErrors`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_TIME_INVALID_YEAR` | `-1` |  |
| `PSP_TIME_INVALID_MONTH` | `-2` |  |
| `PSP_TIME_INVALID_DAY` | `-3` |  |
| `PSP_TIME_INVALID_HOUR` | `-4` |  |
| `PSP_TIME_INVALID_MINUTES` | `-5` |  |
| `PSP_TIME_INVALID_SECONDS` | `-6` |  |
| `PSP_TIME_INVALID_MICROSECONDS` | `-7` |  |

## Functions

### `sceRtcGetTickResolution()`

```c
u32 sceRtcGetTickResolution(void);
```

Get the resolution of the tick counter.

**Returns:** # of ticks per second

### `sceRtcGetCurrentTick()`

```c
int sceRtcGetCurrentTick(u64 *tick);
```

Get current tick count.

**Parameters:**

- `tick` – pointer to u64 to receive tick count

**Returns:** 0 on success, \< 0 on error

### `sceRtcGetCurrentClock()`

```c
int sceRtcGetCurrentClock(ScePspDateTime *time, int tz);
```

Get current tick count, adjusted for local time zone.

**Parameters:**

- `time` – pointer to [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct to receive time
- `tz` – time zone to adjust to (minutes from UTC)

**Returns:** 0 on success, \< 0 on error

### `sceRtcGetCurrentClockLocalTime()`

```c
int sceRtcGetCurrentClockLocalTime(ScePspDateTime *time);
```

Get current local time into a [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct.

**Parameters:**

- `time` – pointer to [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct to receive time

**Returns:** 0 on success, \< 0 on error

### `sceRtcConvertUtcToLocalTime()`

```c
int sceRtcConvertUtcToLocalTime(const u64 *tickUTC, u64 *tickLocal);
```

Convert a UTC-based tickcount into a local time tick count.

**Parameters:**

- `tickUTC` – pointer to u64 tick in UTC time
- `tickLocal` – pointer to u64 to receive tick in local time

**Returns:** 0 on success, \< 0 on error

### `sceRtcConvertLocalTimeToUTC()`

```c
int sceRtcConvertLocalTimeToUTC(const u64 *tickLocal, u64 *tickUTC);
```

Convert a local time based tickcount into a UTC-based tick count.

**Parameters:**

- `tickLocal` – pointer to u64 tick in local time
- `tickUTC` – pointer to u64 to receive tick in UTC based time

**Returns:** 0 on success, \< 0 on error

### `sceRtcIsLeapYear()`

```c
int sceRtcIsLeapYear(int year);
```

Check if a year is a leap year.

**Parameters:**

- `year` – year to check if is a leap year

**Returns:** 1 on leapyear, 0 if not

### `sceRtcGetDaysInMonth()`

```c
int sceRtcGetDaysInMonth(int year, int month);
```

Get number of days in a specific month.

**Parameters:**

- `year` – year in which to check (accounts for leap year)
- `month` – month to get number of days for

**Returns:** # of days in month, \<0 on error (?)

### `sceRtcGetDayOfWeek()`

```c
int sceRtcGetDayOfWeek(int year, int month, int day);
```

Get day of the week for a date.

**Parameters:**

- `year` – year in which to check (accounts for leap year)
- `month` – month that day is in
- `day` – day to get day of week for

**Returns:** day of week with 0 representing Monday

### `sceRtcCheckValid()`

```c
int sceRtcCheckValid(const ScePspDateTime *date);
```

Validate pspDate component ranges.

**Parameters:**

- `date` – pointer to pspDate struct to be checked

**Returns:** 0 on success, one of [pspRtcCheckValidErrors](#enum-psprtccheckvaliderrors) on error

### `sceRtcSetTick()`

```c
int sceRtcSetTick(ScePspDateTime *date, const u64 *tick);
```

Set a [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct based on ticks.

**Parameters:**

- `date` – pointer to [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct to set
- `tick` – pointer to ticks to convert

**Returns:** 0 on success, \< 0 on error

### `sceRtcGetTick()`

```c
int sceRtcGetTick(const ScePspDateTime *date, u64 *tick);
```

Set ticks based on a [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) struct.

**Parameters:**

- `date` – pointer to [ScePspDateTime](../base/psptypes.h.md#struct-scepspdatetime) to convert
- `tick` – pointer to tick to set

**Returns:** 0 on success, \< 0 on error

### `sceRtcCompareTick()`

```c
int sceRtcCompareTick(const u64 *tick1, const u64 *tick2);
```

Compare two ticks.

**Parameters:**

- `tick1` – pointer to first tick
- `tick2` – poiinter to second tick

**Returns:** 0 on equal, \<0 when tick1 \< tick2, >0 when tick1 > tick2

### `sceRtcTickAddTicks()`

```c
int sceRtcTickAddTicks(u64 *destTick, const u64 *srcTick, u64 numTicks);
```

Add two ticks.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numTicks` – number of ticks to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddMicroseconds()`

```c
int sceRtcTickAddMicroseconds(u64 *destTick, const u64 *srcTick, u64 numMS);
```

Add an amount of ms to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numMS` – number of ms to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddSeconds()`

```c
int sceRtcTickAddSeconds(u64 *destTick, const u64 *srcTick, u64 numSecs);
```

Add an amount of seconds to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numSecs` – number of seconds to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddMinutes()`

```c
int sceRtcTickAddMinutes(u64 *destTick, const u64 *srcTick, u64 numMins);
```

Add an amount of minutes to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numMins` – number of minutes to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddHours()`

```c
int sceRtcTickAddHours(u64 *destTick, const u64 *srcTick, int numHours);
```

Add an amount of hours to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numHours` – number of hours to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddDays()`

```c
int sceRtcTickAddDays(u64 *destTick, const u64 *srcTick, int numDays);
```

Add an amount of days to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numDays` – number of days to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddWeeks()`

```c
int sceRtcTickAddWeeks(u64 *destTick, const u64 *srcTick, int numWeeks);
```

Add an amount of weeks to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numWeeks` – number of weeks to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddMonths()`

```c
int sceRtcTickAddMonths(u64 *destTick, const u64 *srcTick, int numMonths);
```

Add an amount of months to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numMonths` – number of months to add

**Returns:** 0 on success, \<0 on error

### `sceRtcTickAddYears()`

```c
int sceRtcTickAddYears(u64 *destTick, const u64 *srcTick, int numYears);
```

Add an amount of years to a tick.

**Parameters:**

- `destTick` – pointer to tick to hold result
- `srcTick` – pointer to source tick
- `numYears` – number of years to add

**Returns:** 0 on success, \<0 on error

### `sceRtcSetTime_t()`

```c
int sceRtcSetTime_t(ScePspDateTime *date, const time_t time);
```

### `sceRtcGetTime_t()`

```c
int sceRtcGetTime_t(const ScePspDateTime *date, time_t *time);
```

### `sceRtcSetDosTime()`

```c
int sceRtcSetDosTime(ScePspDateTime *date, u32 dosTime);
```

### `sceRtcGetDosTime()`

```c
int sceRtcGetDosTime(ScePspDateTime *date, u32 dosTime);
```

### `sceRtcSetWin32FileTime()`

```c
int sceRtcSetWin32FileTime(ScePspDateTime *date, u64 *win32Time);
```

### `sceRtcGetWin32FileTime()`

```c
int sceRtcGetWin32FileTime(ScePspDateTime *date, u64 *win32Time);
```

### `sceRtcParseDateTime()`

```c
int sceRtcParseDateTime(u64 *destTick, const char *dateString);
```

### `sceRtcFormatRFC2822()`

```c
int sceRtcFormatRFC2822(char *pszDateTime, const u64 *pUtc, int iTimeZoneMinutes);
```

Format Tick-representation UTC time in RFC2822 format.

### `sceRtcFormatRFC2822LocalTime()`

```c
int sceRtcFormatRFC2822LocalTime(char *pszDateTime, const u64 *pUtc);
```

Format Tick-representation UTC time in RFC2822 format.

### `sceRtcFormatRFC3339()`

```c
int sceRtcFormatRFC3339(char *pszDateTime, const u64 *pUtc, int iTimeZoneMinutes);
```

Format Tick-representation UTC time in RFC3339(ISO8601) format.

### `sceRtcFormatRFC3339LocalTime()`

```c
int sceRtcFormatRFC3339LocalTime(char *pszDateTime, const u64 *pUtc);
```

Format Tick-representation UTC time in RFC3339(ISO8601) format.

### `sceRtcParseRFC3339()`

```c
int sceRtcParseRFC3339(u64 *pUtc, const char *pszDateTime);
```

Parse time information represented in RFC3339 format.

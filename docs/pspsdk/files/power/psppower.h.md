[PSPSDK documentation](../../README.md) › Files

# power/psppower.h

```c
#include <pspkerneltypes.h>
```

## Macros

### `PSP_POWER_CB_POWER_SWITCH`

```c
#define PSP_POWER_CB_POWER_SWITCH 0x80000000
```

Power callback flags.

### `PSP_POWER_CB_HOLD_SWITCH`

```c
#define PSP_POWER_CB_HOLD_SWITCH 0x40000000
```

### `PSP_POWER_CB_STANDBY`

```c
#define PSP_POWER_CB_STANDBY 0x00080000
```

### `PSP_POWER_CB_RESUME_COMPLETE`

```c
#define PSP_POWER_CB_RESUME_COMPLETE 0x00040000
```

### `PSP_POWER_CB_RESUMING`

```c
#define PSP_POWER_CB_RESUMING 0x00020000
```

### `PSP_POWER_CB_SUSPENDING`

```c
#define PSP_POWER_CB_SUSPENDING 0x00010000
```

### `PSP_POWER_CB_AC_POWER`

```c
#define PSP_POWER_CB_AC_POWER 0x00001000
```

### `PSP_POWER_CB_BATTERY_LOW`

```c
#define PSP_POWER_CB_BATTERY_LOW 0x00000100
```

### `PSP_POWER_CB_BATTERY_EXIST`

```c
#define PSP_POWER_CB_BATTERY_EXIST 0x00000080
```

### `PSP_POWER_CB_BATTPOWER`

```c
#define PSP_POWER_CB_BATTPOWER 0x0000007F
```

### `PSP_POWER_TICK_ALL`

```c
#define PSP_POWER_TICK_ALL 0
```

Power tick flags.

### `PSP_POWER_TICK_SUSPEND`

```c
#define PSP_POWER_TICK_SUSPEND 1
```

### `PSP_POWER_TICK_DISPLAY`

```c
#define PSP_POWER_TICK_DISPLAY 6
```

## Typedefs

### `powerCallback_t`

```c
typedef void(* powerCallback_t) (int unknown, int powerInfo))(int unknown, int powerInfo);
```

Power Callback Function Definition.

**Parameters:**

- `unknown` – unknown function, appears to cycle between 1,2 and 3
- `powerInfo` – combination of PSP_POWER_CB\_ flags

## Functions

### `scePowerRegisterCallback()`

```c
int scePowerRegisterCallback(int slot, SceUID cbid);
```

Register Power Callback Function.

**Parameters:**

- `slot` – slot of the callback in the list, 0 to 15, pass -1 to get an auto assignment.
- `cbid` – callback id from calling sceKernelCreateCallback

**Returns:** 0 on success, the slot number if -1 is passed, \< 0 on error.

### `scePowerUnregisterCallback()`

```c
int scePowerUnregisterCallback(int slot);
```

Unregister Power Callback Function.

**Parameters:**

- `slot` – slot of the callback

**Returns:** 0 on success, \< 0 on error.

### `scePowerIsPowerOnline()`

```c
int scePowerIsPowerOnline(void);
```

Check if unit is plugged in.

**Returns:** 1 if plugged in, 0 if not plugged in, \< 0 on error.

### `scePowerIsBatteryExist()`

```c
int scePowerIsBatteryExist(void);
```

Check if a battery is present.

**Returns:** 1 if battery present, 0 if battery not present, \< 0 on error.

### `scePowerIsBatteryCharging()`

```c
int scePowerIsBatteryCharging(void);
```

Check if the battery is charging.

**Returns:** 1 if battery charging, 0 if battery not charging, \< 0 on error.

### `scePowerGetBatteryChargingStatus()`

```c
int scePowerGetBatteryChargingStatus(void);
```

Get the status of the battery charging.

### `scePowerIsLowBattery()`

```c
int scePowerIsLowBattery(void);
```

Check if the battery is low.

**Returns:** 1 if the battery is low, 0 if the battery is not low, \< 0 on error.

### `scePowerIsSuspendRequired()`

```c
int scePowerIsSuspendRequired(void);
```

Check if a suspend is required.

**Returns:** 1 if suspend is required, 0 otherwise

### `scePowerGetBatteryRemainCapacity()`

```c
int scePowerGetBatteryRemainCapacity(void);
```

Returns battery remaining capacity.

**Returns:** battery remaining capacity in mAh (milliampere hour)

### `scePowerGetBatteryFullCapacity()`

```c
int scePowerGetBatteryFullCapacity(void);
```

Returns battery full capacity.

**Returns:** battery full capacity in mAh (milliampere hour)

### `scePowerGetBatteryLifePercent()`

```c
int scePowerGetBatteryLifePercent(void);
```

Get battery life as integer percent.

**Returns:** Battery charge percentage (0-100), \< 0 on error.

### `scePowerGetBatteryLifeTime()`

```c
int scePowerGetBatteryLifeTime(void);
```

Get battery life as time.

**Returns:** Battery life in minutes, \< 0 on error.

### `scePowerGetBatteryTemp()`

```c
int scePowerGetBatteryTemp(void);
```

Get temperature of the battery.

### `scePowerGetBatteryElec()`

```c
int scePowerGetBatteryElec(void);
```

unknown? - crashes PSP in usermode

### `scePowerGetBatteryVolt()`

```c
int scePowerGetBatteryVolt(void);
```

Get battery volt level.

### `scePowerSetCpuClockFrequency()`

```c
int scePowerSetCpuClockFrequency(int cpufreq);
```

Set CPU Frequency.

**Parameters:**

- `cpufreq` – new CPU frequency, valid values are 1 - 333

### `scePowerSetBusClockFrequency()`

```c
int scePowerSetBusClockFrequency(int busfreq);
```

Set Bus Frequency.

**Parameters:**

- `busfreq` – new BUS frequency, valid values are 1 - 167

### `scePowerGetCpuClockFrequency()`

```c
int scePowerGetCpuClockFrequency(void);
```

Alias for scePowerGetCpuClockFrequencyInt.

**Returns:** frequency as int

### `scePowerGetCpuClockFrequencyInt()`

```c
int scePowerGetCpuClockFrequencyInt(void);
```

Get CPU Frequency as Integer.

**Returns:** frequency as int

### `scePowerGetCpuClockFrequencyFloat()`

```c
float scePowerGetCpuClockFrequencyFloat(void);
```

Get CPU Frequency as Float.

**Returns:** frequency as float

### `scePowerGetBusClockFrequency()`

```c
int scePowerGetBusClockFrequency(void);
```

Alias for scePowerGetBusClockFrequencyInt.

**Returns:** frequency as int

### `scePowerGetBusClockFrequencyInt()`

```c
int scePowerGetBusClockFrequencyInt(void);
```

Get Bus fequency as Integer.

**Returns:** frequency as int

### `scePowerGetBusClockFrequencyFloat()`

```c
float scePowerGetBusClockFrequencyFloat(void);
```

Get Bus frequency as Float.

**Returns:** frequency as float

### `scePowerSetClockFrequency()`

```c
int scePowerSetClockFrequency(int pllfreq, int cpufreq, int busfreq);
```

Set Clock Frequencies.

**Parameters:**

- `pllfreq` – pll frequency, valid from 19-333
- `cpufreq` – cpu frequency, valid from 1-333
- `busfreq` – bus frequency, valid from 1-167

and:

cpufreq \<= pllfreq busfreq\*2 \<= pllfreq

### `scePowerLock()`

```c
int scePowerLock(int unknown);
```

Lock power switch.

Note: if the power switch is toggled while locked it will fire immediately after being unlocked.

**Parameters:**

- `unknown` – pass 0

**Returns:** 0 on success, \< 0 on error.

### `scePowerUnlock()`

```c
int scePowerUnlock(int unknown);
```

Unlock power switch.

**Parameters:**

- `unknown` – pass 0

**Returns:** 0 on success, \< 0 on error.

### `scePowerTick()`

```c
int scePowerTick(int type);
```

Generate a power tick, preventing unit from powering off and turning off display.

**Parameters:**

- `type` – Either PSP_POWER_TICK_ALL, PSP_POWER_TICK_SUSPEND or PSP_POWER_TICK_DISPLAY

**Returns:** 0 on success, \< 0 on error.

### `scePowerGetIdleTimer()`

```c
int scePowerGetIdleTimer(void);
```

Get Idle timer.

### `scePowerIdleTimerEnable()`

```c
int scePowerIdleTimerEnable(int unknown);
```

Enable Idle timer.

**Parameters:**

- `unknown` – pass 0

### `scePowerIdleTimerDisable()`

```c
int scePowerIdleTimerDisable(int unknown);
```

Disable Idle timer.

**Parameters:**

- `unknown` – pass 0

### `scePowerRequestStandby()`

```c
int scePowerRequestStandby(void);
```

Request the PSP to go into standby.

**Returns:** 0 always

### `scePowerRequestSuspend()`

```c
int scePowerRequestSuspend(void);
```

Request the PSP to go into suspend.

**Returns:** 0 always

### `scePowerRequestColdReset()`

```c
int scePowerRequestColdReset(int exitcode);
```

Request the PSP to do a cold reboot.

**Parameters:**

- `exitcode` – pass 0

**Returns:** 0 always

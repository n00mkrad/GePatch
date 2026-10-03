[PSPSDK documentation](../../README.md) › Files

# ctrl/pspctrl.h

Topics: [Controller Kernel Library](../../topics/Ctrl.md)

## Data Structures

### `struct SceCtrlData`

Controller data.

Contains current button and axis state.

**Note:** Axis state is present only in [PSP_CTRL_MODE_ANALOG](#enum-pspctrlmode) controller mode.

**See also:** [sceCtrlPeekBufferPositive()](#scectrlpeekbufferpositive), [sceCtrlPeekBufferNegative()](#scectrlpeekbuffernegative), [sceCtrlReadBufferPositive()](#scectrlreadbufferpositive), [sceCtrlReadBufferNegative()](#scectrlreadbuffernegative), [PspCtrlMode](#enum-pspctrlmode)

| Field | Description |
|---|---|
| `unsigned int TimeStamp` | Current read frame. |
| `unsigned int Buttons` | Buttons in pressed state.<br>Mask the value with one or more [PspCtrlButtons](#enum-pspctrlbuttons) flags to access specific buttons. |
| `unsigned char Lx` | X-axis value of the Analog Stick. |
| `unsigned char Ly` | Y-axis value of the Analog Stick. |
| `unsigned char Rx` | X-axis value of the right Analog Stick, valid when using DualShock 3 on PSP GO, a PS VITA system, through hardware/software hacking, or system emulation. |
| `unsigned char Ry` | Y-axis value of the right Analog Stick, valid when using DualShock 3 on PSP GO, a PS VITA system, through hardware/software hacking, or system emulation. |
| `unsigned char Reserved[4]` | Reserved bytes unused by the firmware. |

### `struct SceCtrlLatch`

Controller latch data.

Contains information about button state changes between two controller service sampling cycles. With each sampling cycle, the controller service compares the new pressed & releasedbutton states with the previously collected pressed button states. This comparison will result in the following possible states for each button:

- **Make** - The button has just been pressed with its prior state being the released state. Transition from 'released' state to 'pressed' state.
- **Press** - The button is currently in the 'pressed' state.
- **Break** - The button has just been released with its prior state being the 'pressed' state. Transition from 'pressed' state to 'release' state.
- **Release** - The button is currently in the 'released' state.

It is possible for a button to (briefly) be in two states at the same time. Valid combinations are as follows:

- **Make** & **Press**
- **Break** & **Release**

In other words, if a button is in the **Make** state, then it is also in the **Press** state. However, this is not the case for the inverse. A button in the **Press** state does not need to be in the **Make** state.

Mask the values with one or more [PspCtrlButtons](#enum-pspctrlbuttons) flags to access specific buttons.

These comparison results are stored internally as latch data and can be retrieved using the APIs [sceCtrlPeekLatch()](#scectrlpeeklatch) and [sceCtrlReadLatch()](#scectrlreadlatch).

**Remarks:** The same can be accomplished by using the different sceCtrl\[Read/Peek\]Buffer\[Positive/Negative\]() APIs and comparing the currently collected button sampling data with the previously collected one.

**See also:** [PspCtrlButtons](#enum-pspctrlbuttons), [sceCtrlPeekLatch()](#scectrlpeeklatch), [sceCtrlReadLatch()](#scectrlreadlatch)

| Field | Description |
|---|---|
| `unsigned int uiMake` | Button transitioned to pressed state. |
| `unsigned int uiBreak` | Button transitioned to released state. |
| `unsigned int uiPress` | Button is in the pressed state. |
| `unsigned int uiRelease` | Button is in the released state. |

## Typedefs

### `SceCtrlLatch`

```c
typedef struct SceCtrlLatch SceCtrlLatch;
```

Controller latch data.

Contains information about button state changes between two controller service sampling cycles. With each sampling cycle, the controller service compares the new pressed & releasedbutton states with the previously collected pressed button states. This comparison will result in the following possible states for each button:

- **Make** - The button has just been pressed with its prior state being the released state. Transition from 'released' state to 'pressed' state.
- **Press** - The button is currently in the 'pressed' state.
- **Break** - The button has just been released with its prior state being the 'pressed' state. Transition from 'pressed' state to 'release' state.
- **Release** - The button is currently in the 'released' state.

It is possible for a button to (briefly) be in two states at the same time. Valid combinations are as follows:

- **Make** & **Press**
- **Break** & **Release**

In other words, if a button is in the **Make** state, then it is also in the **Press** state. However, this is not the case for the inverse. A button in the **Press** state does not need to be in the **Make** state.

Mask the values with one or more [PspCtrlButtons](#enum-pspctrlbuttons) flags to access specific buttons.

These comparison results are stored internally as latch data and can be retrieved using the APIs [sceCtrlPeekLatch()](#scectrlpeeklatch) and [sceCtrlReadLatch()](#scectrlreadlatch).

**Remarks:** The same can be accomplished by using the different sceCtrl\[Read/Peek\]Buffer\[Positive/Negative\]() APIs and comparing the currently collected button sampling data with the previously collected one.

**See also:** [PspCtrlButtons](#enum-pspctrlbuttons), [sceCtrlPeekLatch()](#scectrlpeeklatch), [sceCtrlReadLatch()](#scectrlreadlatch)

## Enumerations

### `enum PspCtrlButtons`

Enumeration representing digital controller button flags.

Each flag corresponds to a different button and can be used to extract button states from [SceCtrlData](#struct-scectrldata) and [SceCtrlLatch](#struct-scectrllatch) structures. Flags can be combined using bitwise OR operation to check for mutliple key states at once.

**Note:** Some button states are available only in kernel mode.

**See also:** [SceCtrlData](#struct-scectrldata), [SceCtrlLatch](#struct-scectrllatch)

| Enumerator | Value | Description |
|---|---|---|
| `PSP_CTRL_SELECT` | `0x000001` | Select button. |
| `PSP_CTRL_L3` | `0x000002` | L3 button. |
| `PSP_CTRL_R3` | `0x000004` | R3 button. |
| `PSP_CTRL_START` | `0x000008` | Start button. |
| `PSP_CTRL_UP` | `0x000010` | Up D-Pad button. |
| `PSP_CTRL_RIGHT` | `0x000020` | Right D-Pad button. |
| `PSP_CTRL_DOWN` | `0x000040` | Down D-Pad button. |
| `PSP_CTRL_LEFT` | `0x000080` | Left D-Pad button. |
| `PSP_CTRL_LTRIGGER` | `0x000100` | Left trigger. |
| `PSP_CTRL_RTRIGGER` | `0x000200` | Right trigger. |
| `PSP_CTRL_L2` | `0x000100` | L2 button. |
| `PSP_CTRL_R2` | `0x000200` | R2 button. |
| `PSP_CTRL_L1` | `0x000400` | L1 button. |
| `PSP_CTRL_R1` | `0x000800` | R1 button. |
| `PSP_CTRL_TRIANGLE` | `0x001000` | Triangle button. |
| `PSP_CTRL_CIRCLE` | `0x002000` | Circle button. |
| `PSP_CTRL_CROSS` | `0x004000` | Cross button. |
| `PSP_CTRL_SQUARE` | `0x008000` | Square button. |
| `PSP_CTRL_HOME` | `0x010000` | Home button.<br>In user mode this bit is set if the exit dialog is visible. |
| `PSP_CTRL_HOLD` | `0x020000` | Hold button. |
| `PSP_CTRL_NOTE` | `0x800000` | Music Note button. |
| `PSP_CTRL_SCREEN` | `0x400000` | Screen button. |
| `PSP_CTRL_VOLUP` | `0x100000` | Volume up button. |
| `PSP_CTRL_VOLDOWN` | `0x200000` | Volume down button. |
| `PSP_CTRL_WLAN_UP` | `0x040000` | Wlan switch up. |
| `PSP_CTRL_REMOTE` | `0x080000` | Remote hold position. |
| `PSP_CTRL_DISC` | `0x1000000` | Disc present. |
| `PSP_CTRL_MS` | `0x2000000` | Memory stick present. |

### `enum PspCtrlMode`

Controller mode.

Specifies if analog data should be included in [SceCtrlData](#struct-scectrldata).

**See also:** [sceCtrlSetSamplingMode()](#scectrlsetsamplingmode), [sceCtrlGetSamplingMode()](#scectrlgetsamplingmode), [SceCtrlData](#struct-scectrldata)

| Enumerator | Value | Description |
|---|---|---|
| `PSP_CTRL_MODE_DIGITAL` | `0` |  |
| `PSP_CTRL_MODE_ANALOG` | `1` |  |

## Functions

### `sceCtrlSetSamplingCycle()`

```c
int sceCtrlSetSamplingCycle(int cycle);
```

Set the controller cycle setting.

**Parameters:**

- `cycle` – Cycle. Normally set to 0.

**Returns:** The previous cycle setting.

### `sceCtrlGetSamplingCycle()`

```c
int sceCtrlGetSamplingCycle(int *pcycle);
```

Get the controller current cycle setting.

**Parameters:**

- `pcycle` – Return value.

**Returns:** 0.

### `sceCtrlSetSamplingMode()`

```c
int sceCtrlSetSamplingMode(int mode);
```

Set the controller mode.

**Parameters:**

- `mode` – One of [PspCtrlMode](#enum-pspctrlmode). If this is [PSP_CTRL_MODE_DIGITAL](#enum-pspctrlmode), no data about the analog stick will be present in the [SceCtrlData](#struct-scectrldata) struct read by SceCtrlReadBuffer.

**Returns:** The previous mode.

### `sceCtrlGetSamplingMode()`

```c
int sceCtrlGetSamplingMode(int *pmode);
```

Get the current controller mode.

**Parameters:**

- `pmode` – Return value.

**Returns:** 0.

### `sceCtrlPeekBufferPositive()`

```c
int sceCtrlPeekBufferPositive(SceCtrlData *pad_data, int count);
```

Read latest controller data from the controller service.

Controller data contains current button and axis state.

**Note:** Axis state is present only in [PSP_CTRL_MODE_ANALOG](#enum-pspctrlmode) controller mode.

**Parameters:**

- `pad_data` – A pointer to [SceCtrlData](#struct-scectrldata) structure that receives controller data.
- `count` – Number of [SceCtrlData](#struct-scectrldata) structures to read.

**See also:** [SceCtrlData](#struct-scectrldata), [sceCtrlPeekBufferNegative()](#scectrlpeekbuffernegative), [sceCtrlReadBufferPositive()](#scectrlreadbufferpositive)

### `sceCtrlPeekBufferNegative()`

```c
int sceCtrlPeekBufferNegative(SceCtrlData *pad_data, int count);
```

### `sceCtrlReadBufferPositive()`

```c
int sceCtrlReadBufferPositive(SceCtrlData *pad_data, int count);
```

Read new controller data from the controller service.

Controller data contains current button and axis state.

**Example:**

```c
SceCtrlData pad;
sceCtrlSetSamplingCycle(0);
sceCtrlSetSamplingMode(1);
sceCtrlReadBufferPositive(&pad, 1);
// Do something with the read controller data
```

**Note:** Axis state is present only in [PSP_CTRL_MODE_ANALOG](#enum-pspctrlmode) controller mode.

**Warning:** Controller data is collected once every controller sampling cycle. If controller data was already read during a cycle, trying to read it again will block the execution until the next one.

**Parameters:**

- `pad_data` – A pointer to [SceCtrlData](#struct-scectrldata) structure that receives controller data.
- `count` – Number of [SceCtrlData](#struct-scectrldata) structures to read.

**See also:** [SceCtrlData](#struct-scectrldata), [sceCtrlReadBufferNegative()](#scectrlreadbuffernegative), [sceCtrlPeekBufferPositive()](#scectrlpeekbufferpositive)

### `sceCtrlReadBufferNegative()`

```c
int sceCtrlReadBufferNegative(SceCtrlData *pad_data, int count);
```

### `sceCtrlPeekLatch()`

```c
int sceCtrlPeekLatch(SceCtrlLatch *latch_data);
```

Read latest latch data from the controller service.

Latch data contains information about button state changes between two controller service sampling cycles.

**Parameters:**

- `latch_data` – A pointer to [SceCtrlLatch](#struct-scectrllatch) structure that receives latch data.

**Returns:**

- On success, the number of times the controller service performed sampling since the last time [sceCtrlReadLatch()](#scectrlreadlatch) was called.
- \< 0 on error.

**See also:** [SceCtrlLatch](#struct-scectrllatch), [sceCtrlReadLatch()](#scectrlreadlatch)

### `sceCtrlReadLatch()`

```c
int sceCtrlReadLatch(SceCtrlLatch *latch_data);
```

Read new latch data from the controller service.

Latch data contains information about button state changes between two controller service sampling cycles.

**Example:**

```c
SceCtrlLatch latchData;

while (1) {
    // Obtain latch data
    sceCtrlReadLatch(&latchData);

    if (latchData.uiMake & PSP_CTRL_CROSS)
    {
        // The Cross button has just been pressed (transition from 'released' state to 'pressed' state)
    }

    if (latchData.uiPress & PSP_CTRL_SQUARE)
    {
        // The Square button is currently in the 'pressed' state
    }

   if (latchData.uiBreak & PSP_CTRL_TRIANGLE)
   {
       // The Triangle button has just been released (transition from 'pressed' state to 'released' state)
   }

   if (latchData.uiRelease & PSP_CTRL_CIRCLE)
   {
       // The Circle button is currently in the 'released' state
   }

   // As we clear the internal latch data with the ReadLatch() call, we can explicitly wait for the VBLANK interval
   // to give the controller service the time it needs to collect new latch data again. This guarantees the next call
   // to sceCtrlReadLatch() will return collected data again.
   //
   // Note: The sceCtrlReadBuffer*() APIs are implicitly waiting for a VBLANK interval if necessary.
   sceDisplayWaitVBlank();
}
```

**Warning:** Latch data is produced once every controller sampling cycle. If latch data was already read during a cycle, trying to read it again will block the execution until the next one.

**Parameters:**

- `latch_data` – A pointer to [SceCtrlLatch](#struct-scectrllatch) structure that receives latch data.

**Returns:**

- On success, the number of times the controller service performed sampling since the last time [sceCtrlReadLatch()](#scectrlreadlatch) was called.
- \< 0 on error.

**See also:** [SceCtrlLatch](#struct-scectrllatch), [sceCtrlPeekLatch()](#scectrlpeeklatch)

### `sceCtrlSetIdleCancelThreshold()`

```c
int sceCtrlSetIdleCancelThreshold(int idlereset, int idleback);
```

Set analog threshold relating to the idle timer.

**Parameters:**

- `idlereset` – Movement needed by the analog to reset the idle timer.
- `idleback` – Movement needed by the analog to bring the PSP back from an idle state.

Set to -1 for analog to not cancel idle timer. Set to 0 for idle timer to be cancelled even if the analog is not moved. Set between 1 - 128 to specify the movement on either axis needed by the analog to fire the event.

**Returns:** \< 0 on error.

### `sceCtrlGetIdleCancelThreshold()`

```c
int sceCtrlGetIdleCancelThreshold(int *idlerest, int *idleback);
```

Get the idle threshold values.

**Parameters:**

- `idlerest` – Movement needed by the analog to reset the idle timer.
- `idleback` – Movement needed by the analog to bring the PSP back from an idle state.

**Returns:** \< 0 on error.

## Variables

### `Rsrv`

```c
unsigned char Rsrv[6][6];
```

Reserved bytes.

This is deprecated with the implementation of Rx and Ry and only here for backwards compatibility.

### `SceCtrlData`

```c
SceCtrlData;
```

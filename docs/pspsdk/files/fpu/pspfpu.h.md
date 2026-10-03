[PSPSDK documentation](../../README.md) › Files

# fpu/pspfpu.h

```c
#include <stdint.h>
```

## Macros

### `PSP_FPU_RM_MASK`

```c
#define PSP_FPU_RM_MASK 0x03
```

Mask value for rounding mode.

### `PSP_FPU_FLAGS_POS`

```c
#define PSP_FPU_FLAGS_POS 2
```

Bit position of the flag bits.

### `PSP_FPU_ENABLE_POS`

```c
#define PSP_FPU_ENABLE_POS 7
```

Bit position of the enable bits.

### `PSP_FPU_CAUSE_POS`

```c
#define PSP_FPU_CAUSE_POS 12
```

Bit position of the cause bits.

### `PSP_FPU_CC0_POS`

```c
#define PSP_FPU_CC0_POS 23
```

Bit position of the cc0 bit.

### `PSP_FPU_FS_POS`

```c
#define PSP_FPU_FS_POS 24
```

Bit position of the fs bit.

### `PSP_FPU_CC17_POS`

```c
#define PSP_FPU_CC17_POS 25
```

Bit position of the cc1->7 bits.

### `PSP_FPU_FLAGS_MASK`

```c
#define PSP_FPU_FLAGS_MASK (0x1F << PSP_FPU_FLAGS_POS)
```

### `PSP_FPU_ENABLE_MASK`

```c
#define PSP_FPU_ENABLE_MASK (0x1F << PSP_FPU_ENABLE_POS)
```

### `PSP_FPU_CAUSE_MASK`

```c
#define PSP_FPU_CAUSE_MASK (0x3F << PSP_FPU_CAUSE_POS)
```

### `PSP_FPU_CC0_MASK`

```c
#define PSP_FPU_CC0_MASK (1 << PSP_FPU_CC0_POS)
```

### `PSP_FPU_FS_MASK`

```c
#define PSP_FPU_FS_MASK (1 << PSP_FPU_FS_POS)
```

### `PSP_FPU_CC17_MASK`

```c
#define PSP_FPU_CC17_MASK (0x7F << PSP_FPU_CC17_POS)
```

## Enumerations

### `enum PspFpuRoundMode`

Enumeration for FPU rounding modes.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_FPU_RN` | `0` | Round to nearest representable value. |
| `PSP_FPU_RZ` | `1` | Round towards zero. |
| `PSP_FPU_RP` | `2` | Round towards plus infinity. |
| `PSP_FPU_RM` | `3` | Round towards minus infinity. |

### `enum PspFpuExceptions`

Enumeration for FPU exceptions.

| Enumerator | Value | Description |
|---|---|---|
| `PSP_FPU_EXCEPTION_INEXACT` | `0x01` | Inexact operation exception. |
| `PSP_FPU_EXCEPTION_UNDERFLOW` | `0x02` | Underflow exception. |
| `PSP_FPU_EXCEPTION_OVERFLOW` | `0x04` | Overflow exception. |
| `PSP_FPU_EXCEPTION_DIVBYZERO` | `0x08` | Division by zero exception. |
| `PSP_FPU_EXCEPTION_INVALIDOP` | `0x10` | Invalid operation exception. |
| `PSP_FPU_EXCEPTION_UNIMPOP` | `0x20` | Unimplemented operation exception (only supported in the cause bits) |
| `PSP_FPU_EXCEPTION_ALL` | `0x3F` | All exceptions. |

## Functions

### `pspFpuGetFCR31()`

```c
uint32_t pspFpuGetFCR31(void);
```

Get the current value of the control/status register.

**Returns:** The value of the control/status register

### `pspFpuSetFCR31()`

```c
void pspFpuSetFCR31(uint32_t var);
```

Set the current value of the control/status register.

**Parameters:**

- `var` – The value to set.

### `pspFpuSetRoundmode()`

```c
void pspFpuSetRoundmode(enum PspFpuRoundMode mode);
```

Set the current round mode.

**Parameters:**

- `mode` – The rounding mode to set, one of [PspFpuRoundMode](#enum-pspfpuroundmode)

### `pspFpuGetRoundmode()`

```c
enum PspFpuRoundMode pspFpuGetRoundmode(void);
```

Get the current round mode.

**Returns:** The round mode, one of [PspFpuRoundMode](#enum-pspfpuroundmode)

### `pspFpuGetFlags()`

```c
uint32_t pspFpuGetFlags(void);
```

Get the exception flags (set when an exception occurs but the actual exception bit is not enabled)

**Returns:** Bitmask of the flags, zero or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuClearFlags()`

```c
void pspFpuClearFlags(uint32_t clear);
```

Clear the flags bits.

**Parameters:**

- `clear` – Bitmask of the bits to clear, one or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuGetEnable()`

```c
uint32_t pspFpuGetEnable(void);
```

Get the exception enable flags.

**Returns:** Bitmask of the flags, zero or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuSetEnable()`

```c
void pspFpuSetEnable(uint32_t enable);
```

Set the enable flags bits.

**Parameters:**

- `enable` – Bitmask of exceptions to enable, zero or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuGetCause()`

```c
uint32_t pspFpuGetCause(void);
```

Get the cause bits (only useful if you installed your own exception handler)

**Returns:** Bitmask of flags, zero or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuClearCause()`

```c
void pspFpuClearCause(uint32_t clear);
```

Clear the cause bits.

**Parameters:**

- `clear` – Bitmask of the bits to clear, one or more of [PspFpuExceptions](#enum-pspfpuexceptions)

### `pspFpuGetFS()`

```c
uint32_t pspFpuGetFS(void);
```

Get the current value of the FS bit (if FS is 0 then an exception occurs with denormalized values, if 1 then they are rewritten as 0.

**Returns:** The current state of the FS bit (0 or 1)

### `pspFpuSetFS()`

```c
void pspFpuSetFS(uint32_t fs);
```

Set the FS bit.

**Parameters:**

- `fs` – 0 or 1 to unset or set fs

### `pspFpuGetCondbits()`

```c
uint32_t pspFpuGetCondbits(void);
```

Get the condition flags (8 bits)

**Returns:** The current condition flags

### `pspFpuClearCondbits()`

```c
void pspFpuClearCondbits(uint32_t clear);
```

Clear the condition bits.

**Parameters:**

- `clear` – Bitmask of the bits to clear

### `pspFpuAbs()`

```c
float pspFpuAbs(float f);
```

returns absolute value

### `pspFpuCeil()`

```c
int pspFpuCeil(float f);
```

Round up.

### `pspFpuFloor()`

```c
int pspFpuFloor(float f);
```

Truncate.

### `pspFpuMax()`

```c
float pspFpuMax(float f1, float f2);
```

select maximum value

### `pspFpuMin()`

```c
float pspFpuMin(float f1, float f2);
```

select minimum value

### `pspFpuNeg()`

```c
float pspFpuNeg(float f);
```

Sign reversal.

### `pspFpuRound()`

```c
int pspFpuRound(float f);
```

Round to nearest.

### `pspFpuRsqrt()`

```c
float pspFpuRsqrt(float f);
```

### `pspFpuSqrt()`

```c
float pspFpuSqrt(float f);
```

Square root.

### `pspFpuTrunc()`

```c
int pspFpuTrunc(float f);
```

Round towards zero.

### `pspFpuFmod()`

```c
float pspFpuFmod(float fs, float fd);
```

### `pspFpuFrac()`

```c
float pspFpuFrac(float f);
```

### `pspFpuReinterpretFloat()`

```c
float pspFpuReinterpretFloat(uint32_t ui);
```

### `pspFpuReinterpretUint()`

```c
uint32_t pspFpuReinterpretUint(float f);
```

### `pspFpuIsEqual()`

```c
int pspFpuIsEqual(float f1, float f2);
```

### `pspFpuSignFloat()`

```c
float pspFpuSignFloat(float f);
```

### `pspFpuSignInt()`

```c
int pspFpuSignInt(float f);
```

### `pspFpuPositiveZero()`

```c
float pspFpuPositiveZero(void);
```

Positive zero.

### `pspFpuNegativeZero()`

```c
float pspFpuNegativeZero(void);
```

Negative zero.

### `pspFpuIsZero()`

```c
int pspFpuIsZero(float f);
```

Test for zero value.

### `pspFpuIsPositiveZero()`

```c
int pspFpuIsPositiveZero(float f);
```

Test for positive zero.

### `pspFpuIsNegativeZero()`

```c
int pspFpuIsNegativeZero(float f);
```

Test for negative zero.

### `pspFpuIsDenormal()`

```c
int pspFpuIsDenormal(float f);
```

Test for denormalized number.

### `pspFpuIsZeroOrDenormal()`

```c
int pspFpuIsZeroOrDenormal(float f);
```

Test for zero or denormalized number.

### `pspFpuPositiveInf()`

```c
float pspFpuPositiveInf(void);
```

Positive infinity.

### `pspFpuNegativeInf()`

```c
float pspFpuNegativeInf(void);
```

Negative infinity.

### `pspFpuIsInf()`

```c
int pspFpuIsInf(float f);
```

Test for infinity.

### `pspFpuPositiveNaN()`

```c
float pspFpuPositiveNaN(void);
```

NaN (positive SNaN)

### `pspFpuNegativeNaN()`

```c
float pspFpuNegativeNaN(void);
```

NaN (negative SNaN)

### `pspFpuPositiveQNaN()`

```c
float pspFpuPositiveQNaN(void);
```

Quiet NaN (positive QNaN)

### `pspFpuNegativeQNaN()`

```c
float pspFpuNegativeQNaN(void);
```

Quiet NaN (positive QNaN)

### `pspFpuPositiveSNaN()`

```c
float pspFpuPositiveSNaN(unsigned int uiSignal);
```

Signaling NaN (positive SNaN)

### `pspFpuNegativeSNaN()`

```c
float pspFpuNegativeSNaN(unsigned int uiSignal);
```

Signaling NaN (negative SNaN)

### `pspFpuIsNaN()`

```c
int pspFpuIsNaN(float f);
```

Test for NaN.

### `pspFpuIsInfOrNaN()`

```c
int pspFpuIsInfOrNaN(float f);
```

Test for infinity or NaN.

### `pspFpuNormalizePhase()`

```c
float pspFpuNormalizePhase(float f);
```

### `pspFpuSin()`

```c
float pspFpuSin(float x);
```

Sine.

### `pspFpuCos()`

```c
float pspFpuCos(float x);
```

Cosine.

### `pspFpuAtan()`

```c
float pspFpuAtan(float x);
```

Arc tangent.

### `pspFpuLog()`

```c
float pspFpuLog(float x);
```

Natural Logarithm.

### `pspFpuExp()`

```c
float pspFpuExp(float x);
```

Exponential.

### `pspFpuAsin()`

```c
float pspFpuAsin(float x);
```

ArcSin.

### `pspFpuAcos()`

```c
float pspFpuAcos(float x);
```

ArcCos.

### `pspFpuFloatToDouble()`

```c
double pspFpuFloatToDouble(float a);
```

convert float to double

### `pspFpuDoubleToFloat()`

```c
float pspFpuDoubleToFloat(double a);
```

convert double to float

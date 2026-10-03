[PSPSDK documentation](../../README.md) › Files

# fpu/pspfpu.c

```c
#include "pspfpu.h"
```

## Macros

### `PSP_MATH_PI`

```c
#define PSP_MATH_PI 3.14159265358979323846
```

### `PSP_MATH_TWOPI`

```c
#define PSP_MATH_TWOPI (PSP_MATH_PI * 2.0)
```

### `PSP_MATH_SQRT2`

```c
#define PSP_MATH_SQRT2 1.41421356237309504880
```

### `PSP_MATH_LN2`

```c
#define PSP_MATH_LN2 0.69314718055994530942
```

### `PSP_MATH_LOG2E`

```c
#define PSP_MATH_LOG2E 1.4426950408889634074
```

### `COS_SIN_DIV`

```c
#define COS_SIN_DIV 0.208
```

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

- `mode` – The rounding mode to set, one of [PspFpuRoundMode](pspfpu.h.md#enum-pspfpuroundmode)

### `pspFpuGetRoundmode()`

```c
enum PspFpuRoundMode pspFpuGetRoundmode(void);
```

Get the current round mode.

**Returns:** The round mode, one of [PspFpuRoundMode](pspfpu.h.md#enum-pspfpuroundmode)

### `pspFpuGetFlags()`

```c
uint32_t pspFpuGetFlags(void);
```

Get the exception flags (set when an exception occurs but the actual exception bit is not enabled)

**Returns:** Bitmask of the flags, zero or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

### `pspFpuClearFlags()`

```c
void pspFpuClearFlags(uint32_t clear);
```

Clear the flags bits.

**Parameters:**

- `clear` – Bitmask of the bits to clear, one or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

### `pspFpuGetEnable()`

```c
uint32_t pspFpuGetEnable(void);
```

Get the exception enable flags.

**Returns:** Bitmask of the flags, zero or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

### `pspFpuSetEnable()`

```c
void pspFpuSetEnable(uint32_t enable);
```

Set the enable flags bits.

**Parameters:**

- `enable` – Bitmask of exceptions to enable, zero or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

### `pspFpuGetCause()`

```c
uint32_t pspFpuGetCause(void);
```

Get the cause bits (only useful if you installed your own exception handler)

**Returns:** Bitmask of flags, zero or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

### `pspFpuClearCause()`

```c
void pspFpuClearCause(uint32_t clear);
```

Clear the cause bits.

**Parameters:**

- `clear` – Bitmask of the bits to clear, one or more of [PspFpuExceptions](pspfpu.h.md#enum-pspfpuexceptions)

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
float pspFpuAbs(float fs);
```

returns absolute value

### `pspFpuCeil()`

```c
int pspFpuCeil(float fs);
```

Round up.

### `pspFpuFloor()`

```c
int pspFpuFloor(float fs);
```

Truncate.

### `pspFpuMax()`

```c
float pspFpuMax(float fs1, float fs2);
```

select maximum value

### `pspFpuMin()`

```c
float pspFpuMin(float fs1, float fs2);
```

select minimum value

### `pspFpuNeg()`

```c
float pspFpuNeg(float fs);
```

Sign reversal.

### `pspFpuRound()`

```c
int pspFpuRound(float fs);
```

Round to nearest.

### `pspFpuRsqrt()`

```c
float pspFpuRsqrt(float fs);
```

### `pspFpuSqrt()`

```c
float pspFpuSqrt(float fs);
```

Square root.

### `pspFpuTrunc()`

```c
int pspFpuTrunc(float fs);
```

Round towards zero.

### `pspFpuFmod()`

```c
float pspFpuFmod(float fs, float fd);
```

### `pspFpuFrac()`

```c
float pspFpuFrac(float fs);
```

### `pspFpuReinterpretFloat()`

```c
float pspFpuReinterpretFloat(uint32_t ui);
```

### `pspFpuReinterpretUint()`

```c
uint32_t pspFpuReinterpretUint(float fs);
```

### `pspFpuIsEqual()`

```c
int pspFpuIsEqual(float fs1, float fs2);
```

### `pspFpuSignFloat()`

```c
float pspFpuSignFloat(float fs);
```

### `pspFpuSignInt()`

```c
int pspFpuSignInt(float fs);
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
float pspFpuNormalizePhase(float fs);
```

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

### `_pspFpuSinMain()`

```c
static float _pspFpuSinMain(float x);
```

### `_pspFpuCosMain()`

```c
static float _pspFpuCosMain(float x);
```

### `_pspFpuAtanMain()`

```c
static float _pspFpuAtanMain(float x);
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

### `_atanf()`

```c
static float _atanf(float x);
```

### `pspFpuAtan()`

```c
float pspFpuAtan(float x);
```

Arc tangent.

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

## Variables

### `logPoly`

```c
const float logPoly[][] = {
	 4194305.0 / (1024.0 * 1024.0 *  2.0),
	 5590817.0 / (1024.0 * 1024.0 *  8.0),
	13890687.0 / (1024.0 * 1024.0 * 32.0),
};
```

### `triPoly`

```c
const float triPoly[][] = {
	(float)(2.0* 3.14159265358979323846 ),
	(float)(1.0),
	(float)(-0xAAAA98/(1024.0*1024*64)),
	(float)( 0x88801C/(1024.0*1024*1024)),
	(float)(-0xCB9F27/(1024.0*1024*1024*64)),

	(float)(-0xFFFFF9/(1024.0*1024*32)),
	(float)( 0xAAA6FB/(1024.0*1024*256)),
	(float)(-0xB3D431/(1024.0*1024*1024*8)),

	(float)(-0xAAAAAA/(1024.0*1024*32)),
	(float)( 0xCCCCCD/(1024.0*1024*64)),
	(float)(-0x8F5C29/(1024.0*1024*64)),
};
```

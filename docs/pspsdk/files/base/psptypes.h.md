[PSPSDK documentation](../../README.md) › Files

# base/psptypes.h

```c
#include <stdint.h>
```

## Data Structures

### `struct ScePspSRect`

```c
struct ScePspSRect {
    short int x;
    short int y;
    short int w;
    short int h;
};
```

### `struct ScePspIRect`

```c
struct ScePspIRect {
    int x;
    int y;
    int w;
    int h;
};
```

### `struct ScePspL64Rect`

```c
struct ScePspL64Rect {
    SceLong64 x;
    SceLong64 y;
    SceLong64 w;
    SceLong64 h;
};
```

### `struct ScePspFRect`

```c
struct ScePspFRect {
    float x;
    float y;
    float w;
    float h;
};
```

### `struct ScePspSVector2`

```c
struct ScePspSVector2 {
    short int x;
    short int y;
};
```

### `struct ScePspIVector2`

```c
struct ScePspIVector2 {
    int x;
    int y;
};
```

### `struct ScePspL64Vector2`

```c
struct ScePspL64Vector2 {
    SceLong64 x;
    SceLong64 y;
};
```

### `struct ScePspFVector2`

```c
struct ScePspFVector2 {
    float x;
    float y;
};
```

### `union ScePspVector2`

```c
union ScePspVector2 {
    ScePspFVector2 fv;
    ScePspIVector2 iv;
    float f[2];
    int i[2];
};
```

### `struct ScePspSVector3`

```c
struct ScePspSVector3 {
    short int x;
    short int y;
    short int z;
};
```

### `struct ScePspIVector3`

```c
struct ScePspIVector3 {
    int x;
    int y;
    int z;
};
```

### `struct ScePspL64Vector3`

```c
struct ScePspL64Vector3 {
    SceLong64 x;
    SceLong64 y;
    SceLong64 z;
};
```

### `struct ScePspFVector3`

```c
struct ScePspFVector3 {
    float x;
    float y;
    float z;
};
```

### `union ScePspVector3`

```c
union ScePspVector3 {
    ScePspFVector3 fv;
    ScePspIVector3 iv;
    float f[3];
    int i[3];
};
```

### `struct ScePspSVector4`

```c
struct ScePspSVector4 {
    short int x;
    short int y;
    short int z;
    short int w;
};
```

### `struct ScePspIVector4`

```c
struct ScePspIVector4 {
    int x;
    int y;
    int z;
    int w;
};
```

### `struct ScePspL64Vector4`

```c
struct ScePspL64Vector4 {
    SceLong64 x;
    SceLong64 y;
    SceLong64 z;
    SceLong64 w;
};
```

### `struct ScePspFVector4`

```c
struct ScePspFVector4 {
    float x;
    float y;
    float z;
    float w;
};
```

### `struct ScePspFVector4Unaligned`

```c
struct ScePspFVector4Unaligned {
    float x;
    float y;
    float z;
    float w;
};
```

### `union ScePspVector4`

```c
union ScePspVector4 {
    ScePspFVector4 fv;
    ScePspIVector4 iv;
    float f[4];
    int i[4];
};
```

### `struct ScePspIMatrix2`

```c
struct ScePspIMatrix2 {
    ScePspIVector2 x;
    ScePspIVector2 y;
};
```

### `struct ScePspFMatrix2`

```c
struct ScePspFMatrix2 {
    ScePspFVector2 x;
    ScePspFVector2 y;
};
```

### `union ScePspMatrix2`

```c
union ScePspMatrix2 {
    ScePspFMatrix2 fm;
    ScePspIMatrix2 im;
    ScePspFVector2 fv[2];
    ScePspIVector2 iv[2];
    ScePspVector2 v[2];
    float f[2][2];
    int i[2][2];
};
```

### `struct ScePspIMatrix3`

```c
struct ScePspIMatrix3 {
    ScePspIVector3 x;
    ScePspIVector3 y;
    ScePspIVector3 z;
};
```

### `struct ScePspFMatrix3`

```c
struct ScePspFMatrix3 {
    ScePspFVector3 x;
    ScePspFVector3 y;
    ScePspFVector3 z;
};
```

### `union ScePspMatrix3`

```c
union ScePspMatrix3 {
    ScePspFMatrix3 fm;
    ScePspIMatrix3 im;
    ScePspFVector3 fv[3];
    ScePspIVector3 iv[3];
    ScePspVector3 v[3];
    float f[3][3];
    int i[3][3];
};
```

### `struct ScePspIMatrix4`

```c
struct ScePspIMatrix4 {
    ScePspIVector4 x;
    ScePspIVector4 y;
    ScePspIVector4 z;
    ScePspIVector4 w;
};
```

### `struct ScePspIMatrix4Unaligned`

```c
struct ScePspIMatrix4Unaligned {
    ScePspIVector4 x;
    ScePspIVector4 y;
    ScePspIVector4 z;
    ScePspIVector4 w;
};
```

### `struct ScePspFMatrix4`

```c
struct ScePspFMatrix4 {
    ScePspFVector4 x;
    ScePspFVector4 y;
    ScePspFVector4 z;
    ScePspFVector4 w;
};
```

### `struct ScePspFMatrix4Unaligned`

```c
struct ScePspFMatrix4Unaligned {
    ScePspFVector4 x;
    ScePspFVector4 y;
    ScePspFVector4 z;
    ScePspFVector4 w;
};
```

### `union ScePspMatrix4`

```c
union ScePspMatrix4 {
    ScePspFMatrix4 fm;
    ScePspIMatrix4 im;
    ScePspFVector4 fv[4];
    ScePspIVector4 iv[4];
    ScePspVector4 v[4];
    float f[4][4];
    int i[4][4];
};
```

### `struct ScePspFQuaternion`

```c
struct ScePspFQuaternion {
    float x;
    float y;
    float z;
    float w;
};
```

### `struct ScePspFQuaternionUnaligned`

```c
struct ScePspFQuaternionUnaligned {
    float x;
    float y;
    float z;
    float w;
};
```

### `struct ScePspFColor`

```c
struct ScePspFColor {
    float r;
    float g;
    float b;
    float a;
};
```

### `struct ScePspFColorUnaligned`

```c
struct ScePspFColorUnaligned {
    float r;
    float g;
    float b;
    float a;
};
```

### `union ScePspUnion32`

```c
union ScePspUnion32 {
    unsigned int ui;
    int i;
    unsigned short us[2];
    short int s[2];
    unsigned char uc[4];
    char c[4];
    float f;
    ScePspRGBA8888 rgba8888;
    ScePspRGBA4444 rgba4444[2];
    ScePspRGBA5551 rgba5551[2];
    ScePspRGB565 rgb565[2];
};
```

### `union ScePspUnion64`

```c
union ScePspUnion64 {
    SceULong64 ul;
    SceLong64 l;
    unsigned int ui[2];
    int i[2];
    unsigned short us[4];
    short int s[4];
    unsigned char uc[8];
    char c[8];
    float f[2];
    ScePspSRect sr;
    ScePspSVector4 sv;
    ScePspRGBA8888 rgba8888[2];
    ScePspRGBA4444 rgba4444[4];
    ScePspRGBA5551 rgba5551[4];
    ScePspRGB565 rgb565[4];
};
```

### `union ScePspUnion128`

```c
union ScePspUnion128 {
    SceULong64 ul[2];
    SceLong64 l[2];
    unsigned int ui[4];
    int i[4];
    unsigned short us[8];
    short int s[8];
    unsigned char uc[16];
    char c[16];
    float f[4];
    ScePspFRect fr;
    ScePspIRect ir;
    ScePspFVector4 fv;
    ScePspIVector4 iv;
    ScePspFQuaternion fq;
    ScePspFColor fc;
    ScePspRGBA8888 rgba8888[4];
    ScePspRGBA4444 rgba4444[8];
    ScePspRGBA5551 rgba5551[8];
    ScePspRGB565 rgb565[8];
};
```

### `struct ScePspDateTime`

```c
struct ScePspDateTime {
    unsigned short year;
    unsigned short month;
    unsigned short day;
    unsigned short hour;
    unsigned short minute;
    unsigned short second;
    unsigned int microsecond;
};
```

## Macros

### `NULL`

```c
#define NULL ((void *) 0)
```

### `PSP_LEGACY_TYPES_DEFINED`

```c
#define PSP_LEGACY_TYPES_DEFINED
```

### `PSP_LEGACY_VOLATILE_TYPES_DEFINED`

```c
#define PSP_LEGACY_VOLATILE_TYPES_DEFINED
```

## Typedefs

### `u8`

```c
typedef uint8_t u8;
```

### `u16`

```c
typedef uint16_t u16;
```

### `u32`

```c
typedef uint32_t u32;
```

### `u64`

```c
typedef uint64_t u64;
```

### `s8`

```c
typedef int8_t s8;
```

### `s16`

```c
typedef int16_t s16;
```

### `s32`

```c
typedef int32_t s32;
```

### `s64`

```c
typedef int64_t s64;
```

### `vu8`

```c
typedef volatile uint8_t vu8;
```

### `vu16`

```c
typedef volatile uint16_t vu16;
```

### `vu32`

```c
typedef volatile uint32_t vu32;
```

### `vu64`

```c
typedef volatile uint64_t vu64;
```

### `vs8`

```c
typedef volatile int8_t vs8;
```

### `vs16`

```c
typedef volatile int16_t vs16;
```

### `vs32`

```c
typedef volatile int32_t vs32;
```

### `vs64`

```c
typedef volatile int64_t vs64;
```

### `SceUChar8`

```c
typedef unsigned char SceUChar8;
```

### `SceUShort16`

```c
typedef uint16_t SceUShort16;
```

### `SceUInt32`

```c
typedef uint32_t SceUInt32;
```

### `SceUInt64`

```c
typedef uint64_t SceUInt64;
```

### `SceULong64`

```c
typedef uint64_t SceULong64;
```

### `SceChar8`

```c
typedef char SceChar8;
```

### `SceShort16`

```c
typedef int16_t SceShort16;
```

### `SceInt32`

```c
typedef int32_t SceInt32;
```

### `SceInt64`

```c
typedef int64_t SceInt64;
```

### `SceLong64`

```c
typedef int64_t SceLong64;
```

### `SceFloat`

```c
typedef float SceFloat;
```

### `SceFloat32`

```c
typedef float SceFloat32;
```

### `SceWChar16`

```c
typedef short unsigned int SceWChar16;
```

### `SceWChar32`

```c
typedef unsigned int SceWChar32;
```

### `SceBool`

```c
typedef int SceBool;
```

### `SceVoid`

```c
typedef void SceVoid;
```

### `ScePVoid`

```c
typedef void* ScePVoid;
```

### `SceSize`

```c
typedef unsigned int SceSize;
```

### `ScePspSRect`

```c
typedef struct ScePspSRect ScePspSRect;
```

### `ScePspIRect`

```c
typedef struct ScePspIRect ScePspIRect;
```

### `ScePspL64Rect`

```c
typedef struct ScePspL64Rect ScePspL64Rect;
```

### `ScePspFRect`

```c
typedef struct ScePspFRect ScePspFRect;
```

### `ScePspSVector2`

```c
typedef struct ScePspSVector2 ScePspSVector2;
```

### `ScePspIVector2`

```c
typedef struct ScePspIVector2 ScePspIVector2;
```

### `ScePspL64Vector2`

```c
typedef struct ScePspL64Vector2 ScePspL64Vector2;
```

### `ScePspFVector2`

```c
typedef struct ScePspFVector2 ScePspFVector2;
```

### `ScePspVector2`

```c
typedef union ScePspVector2 ScePspVector2;
```

### `ScePspSVector3`

```c
typedef struct ScePspSVector3 ScePspSVector3;
```

### `ScePspIVector3`

```c
typedef struct ScePspIVector3 ScePspIVector3;
```

### `ScePspL64Vector3`

```c
typedef struct ScePspL64Vector3 ScePspL64Vector3;
```

### `ScePspFVector3`

```c
typedef struct ScePspFVector3 ScePspFVector3;
```

### `ScePspVector3`

```c
typedef union ScePspVector3 ScePspVector3;
```

### `ScePspSVector4`

```c
typedef struct ScePspSVector4 ScePspSVector4;
```

### `ScePspIVector4`

```c
typedef struct ScePspIVector4 ScePspIVector4;
```

### `ScePspL64Vector4`

```c
typedef struct ScePspL64Vector4 ScePspL64Vector4;
```

### `ScePspFVector4`

```c
typedef struct ScePspFVector4 ScePspFVector4;
```

### `ScePspFVector4Unaligned`

```c
typedef struct ScePspFVector4Unaligned ScePspFVector4Unaligned;
```

### `ScePspVector4`

```c
typedef union ScePspVector4 ScePspVector4;
```

### `ScePspIMatrix2`

```c
typedef struct ScePspIMatrix2 ScePspIMatrix2;
```

### `ScePspFMatrix2`

```c
typedef struct ScePspFMatrix2 ScePspFMatrix2;
```

### `ScePspMatrix2`

```c
typedef union ScePspMatrix2 ScePspMatrix2;
```

### `ScePspIMatrix3`

```c
typedef struct ScePspIMatrix3 ScePspIMatrix3;
```

### `ScePspFMatrix3`

```c
typedef struct ScePspFMatrix3 ScePspFMatrix3;
```

### `ScePspMatrix3`

```c
typedef union ScePspMatrix3 ScePspMatrix3;
```

### `ScePspIMatrix4`

```c
typedef struct ScePspIMatrix4 ScePspIMatrix4;
```

### `ScePspIMatrix4Unaligned`

```c
typedef struct ScePspIMatrix4Unaligned ScePspIMatrix4Unaligned;
```

### `ScePspFMatrix4`

```c
typedef struct ScePspFMatrix4 ScePspFMatrix4;
```

### `ScePspFMatrix4Unaligned`

```c
typedef struct ScePspFMatrix4Unaligned ScePspFMatrix4Unaligned;
```

### `ScePspMatrix4`

```c
typedef union ScePspMatrix4 ScePspMatrix4;
```

### `ScePspFQuaternion`

```c
typedef struct ScePspFQuaternion ScePspFQuaternion;
```

### `ScePspFQuaternionUnaligned`

```c
typedef struct ScePspFQuaternionUnaligned ScePspFQuaternionUnaligned;
```

### `ScePspFColor`

```c
typedef struct ScePspFColor ScePspFColor;
```

### `ScePspFColorUnaligned`

```c
typedef struct ScePspFColorUnaligned ScePspFColorUnaligned;
```

### `ScePspRGBA8888`

```c
typedef unsigned int ScePspRGBA8888;
```

### `ScePspRGBA4444`

```c
typedef unsigned short ScePspRGBA4444;
```

### `ScePspRGBA5551`

```c
typedef unsigned short ScePspRGBA5551;
```

### `ScePspRGB565`

```c
typedef unsigned short ScePspRGB565;
```

### `ScePspUnion32`

```c
typedef union ScePspUnion32 ScePspUnion32;
```

### `ScePspUnion64`

```c
typedef union ScePspUnion64 ScePspUnion64;
```

### `ScePspUnion128`

```c
typedef union ScePspUnion128 ScePspUnion128;
```

### `ScePspDateTime`

```c
typedef struct ScePspDateTime ScePspDateTime;
```

### `SceKernelThreadEntry`

```c
typedef int(* SceKernelThreadEntry) (SceSize args, void *argp))(SceSize args, void *argp);
```

## Functions

### `_lb()`

```c
static __inline__ u8 _lb(u32 addr);
```

### `_lh()`

```c
static __inline__ u16 _lh(u32 addr);
```

### `_lw()`

```c
static __inline__ u32 _lw(u32 addr);
```

### `_ld()`

```c
static __inline__ u64 _ld(u32 addr);
```

### `_sb()`

```c
static __inline__ void _sb(u8 val, u32 addr);
```

### `_sh()`

```c
static __inline__ void _sh(u16 val, u32 addr);
```

### `_sw()`

```c
static __inline__ void _sw(u32 val, u32 addr);
```

### `_sd()`

```c
static __inline__ void _sd(u64 val, u32 addr);
```

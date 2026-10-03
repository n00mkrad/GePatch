[PSPSDK documentation](../../README.md) › Files

# gu/guInternal.h

```c
#include "pspgu.h"
```

## Data Structures

### `struct GuSettings`

```c
struct GuSettings {
    GuCallback sig;
    GuCallback fin;
    short signal_history[16];
    int signal_offset;
    int kernel_event_flag;
    int ge_callback_id;
    GuSwapBuffersCallback swapBuffersCallback;
    int swapBuffersBehaviour;
};
```

### `struct GuDisplayList`

```c
struct GuDisplayList {
    unsigned int * start;
    unsigned int * current;
    int parent_context;
};
```

### `struct GuContext`

```c
struct GuContext {
    GuDisplayList list;
    int scissor_enable;
    int scissor_start[2];
    int scissor_end[2];
    int near_plane;
    int far_plane;
    int depth_offset;
    int fragment_2x;
    int texture_function;
    int texture_proj_map_mode;
    int texture_map_mode;
    int sprite_mode[4];
    unsigned int clear_color;
    unsigned int clear_stencil;
    unsigned int clear_depth;
    int texture_mode;
};
```

### `struct GuDrawBuffer`

```c
struct GuDrawBuffer {
    int pixel_size;
    int frame_width;
    void * frame_buffer;
    void * disp_buffer;
    void * depth_buffer;
    int depth_width;
    int width;
    int height;
};
```

## Macros

### `GU_OBJECT_STACK_SIZE`

```c
#define GU_OBJECT_STACK_SIZE 32
```

## Typedefs

### `GECommand`

```c
typedef enum GECommand GECommand;
```

## Enumerations

### `enum GECommand`

| Enumerator | Value | Description |
|---|---|---|
| `NOP` | `0x0` |  |
| `VADDR` | `0x1` |  |
| `IADDR` | `0x2` |  |
| `PRIM` | `0x4` |  |
| `BEZIER` | `0x5` |  |
| `SPLINE` | `0x6` |  |
| `BOUNDING_BOX` | `0x7` |  |
| `JUMP` | `0x8` |  |
| `BJUMP` | `0x9` |  |
| `CALL` | `0xa` |  |
| `RET` | `0xb` |  |
| `END` | `0xc` |  |
| `SIGNAL` | `0xe` |  |
| `FINISH` | `0xf` |  |
| `BASE` | `0x10` |  |
| `VERTEX_TYPE` | `0x12` |  |
| `OFFSET_ADDR` | `0x13` |  |
| `ORIGIN` | `0x14` |  |
| `REGION1` | `0x15` |  |
| `REGION2` | `0x16` |  |
| `LIGHTING_ENABLE` | `0x17` |  |
| `LIGHT_ENABLE0` | `0x18` |  |
| `LIGHT_ENABLE1` | `0x19` |  |
| `LIGHT_ENABLE2` | `0x1a` |  |
| `LIGHT_ENABLE3` | `0x1b` |  |
| `DEPTH_CLIP_ENABLE` | `0x1c` |  |
| `CULL_FACE_ENABLE` | `0x1d` |  |
| `TEXTURE_ENABLE` | `0x1e` |  |
| `FOG_ENABLE` | `0x1f` |  |
| `DITHER_ENABLE` | `0x20` |  |
| `ALPHA_BLEND_ENABLE` | `0x21` |  |
| `ALPHA_TEST_ENABLE` | `0x22` |  |
| `Z_TEST_ENABLE` | `0x23` |  |
| `STENCIL_TEST_ENABLE` | `0x24` |  |
| `ANTI_ALIAS_ENABLE` | `0x25` |  |
| `PATCH_CULL_ENABLE` | `0x26` |  |
| `COLOR_TEST_ENABLE` | `0x27` |  |
| `LOGIC_OP_ENABLE` | `0x28` |  |
| `BONE_MATRIX_NUMBER` | `0x2a` |  |
| `BONE_MATRIX_DATA` | `0x2b` |  |
| `MORPH_WEIGHT0` | `0x2c` |  |
| `MORPH_WEIGHT1` | `0x2d` |  |
| `MORPH_WEIGHT2` | `0x2e` |  |
| `MORPH_WEIGHT3` | `0x2f` |  |
| `MORPH_WEIGHT4` | `0x30` |  |
| `MORPH_WEIGHT5` | `0x31` |  |
| `MORPH_WEIGHT6` | `0x32` |  |
| `MORPH_WEIGHT7` | `0x33` |  |
| `PATCH_DIVISION` | `0x36` |  |
| `PATCH_PRIMITIVE` | `0x37` |  |
| `PATCH_FACING` | `0x38` |  |
| `WORLD_MATRIX_NUMBER` | `0x3a` |  |
| `WORLD_MATRIX_DATA` | `0x3b` |  |
| `VIEW_MATRIX_NUMBER` | `0x3c` |  |
| `VIEW_MATRIX_DATA` | `0x3d` |  |
| `PROJ_MATRIX_NUMBER` | `0x3e` |  |
| `PROJ_MATRIX_DATA` | `0x3f` |  |
| `TGEN_MATRIX_NUMBER` | `0x40` |  |
| `TGEN_MATRIX_DATA` | `0x41` |  |
| `VIEWPORT_X_SCALE` | `0x42` |  |
| `VIEWPORT_Y_SCALE` | `0x43` |  |
| `VIEWPORT_Z_SCALE` | `0x44` |  |
| `VIEWPORT_X_CENTER` | `0x45` |  |
| `VIEWPORT_Y_CENTER` | `0x46` |  |
| `VIEWPORT_Z_CENTER` | `0x47` |  |
| `TEX_SCALE_U` | `0x48` |  |
| `TEX_SCALE_V` | `0x49` |  |
| `TEX_OFFSET_U` | `0x4a` |  |
| `TEX_OFFSET_V` | `0x4b` |  |
| `OFFSET_X` | `0x4c` |  |
| `OFFSET_Y` | `0x4d` |  |
| `SHADE_MODE` | `0x50` |  |
| `NORMAL_REVERSE` | `0x51` |  |
| `MATERIAL_COLOR` | `0x53` |  |
| `MATERIAL_EMISSIVE` | `0x54` |  |
| `AMBIENT_COLOR` | `0x55` |  |
| `MATERIAL_DIFFUSE` | `0x56` |  |
| `MATERIAL_SPECULAR` | `0x57` |  |
| `AMBIENT_ALPHA` | `0x58` |  |
| `MATERIAL_SPECULAR_COEF` | `0x5b` |  |
| `AMBIENT_LIGHT_COLOR` | `0x5c` |  |
| `AMBIENT_LIGHT_ALPHA` | `0x5d` |  |
| `LIGHT_MODE` | `0x5e` |  |
| `LIGHT_TYPE0` | `0x5f` |  |
| `LIGHT_TYPE1` | `0x60` |  |
| `LIGHT_TYPE2` | `0x61` |  |
| `LIGHT_TYPE3` | `0x62` |  |
| `LIGHT0_X` | `0x63` |  |
| `LIGHT0_Y` | `0x64` |  |
| `LIGHT0_Z` | `0x65` |  |
| `LIGHT1_X` | `0x66` |  |
| `LIGHT1_Y` | `0x67` |  |
| `LIGHT1_Z` | `0x68` |  |
| `LIGHT2_X` | `0x69` |  |
| `LIGHT2_Y` | `0x6a` |  |
| `LIGHT2_Z` | `0x6b` |  |
| `LIGHT3_X` | `0x6c` |  |
| `LIGHT3_Y` | `0x6d` |  |
| `LIGHT3_Z` | `0x6e` |  |
| `LIGHT0_DIRECTION_X` | `0x6f` |  |
| `LIGHT0_DIRECTION_Y` | `0x70` |  |
| `LIGHT0_DIRECTION_Z` | `0x71` |  |
| `LIGHT1_DIRECTION_X` | `0x72` |  |
| `LIGHT1_DIRECTION_Y` | `0x73` |  |
| `LIGHT1_DIRECTION_Z` | `0x74` |  |
| `LIGHT2_DIRECTION_X` | `0x75` |  |
| `LIGHT2_DIRECTION_Y` | `0x76` |  |
| `LIGHT2_DIRECTION_Z` | `0x77` |  |
| `LIGHT3_DIRECTION_X` | `0x78` |  |
| `LIGHT3_DIRECTION_Y` | `0x79` |  |
| `LIGHT3_DIRECTION_Z` | `0x7a` |  |
| `LIGHT0_CONSTANT_ATTEN` | `0x7b` |  |
| `LIGHT0_LINEAR_ATTEN` | `0x7c` |  |
| `LIGHT0_QUADRATIC_ATTEN` | `0x7d` |  |
| `LIGHT1_CONSTANT_ATTEN` | `0x7e` |  |
| `LIGHT1_LINEAR_ATTEN` | `0x7f` |  |
| `LIGHT1_QUADRATIC_ATTEN` | `0x80` |  |
| `LIGHT2_CONSTANT_ATTEN` | `0x81` |  |
| `LIGHT2_LINEAR_ATTEN` | `0x82` |  |
| `LIGHT2_QUADRATIC_ATTEN` | `0x83` |  |
| `LIGHT3_CONSTANT_ATTEN` | `0x84` |  |
| `LIGHT3_LINEAR_ATTEN` | `0x85` |  |
| `LIGHT3_QUADRATIC_ATTEN` | `0x86` |  |
| `LIGHT0_EXPONENT_ATTEN` | `0x87` |  |
| `LIGHT1_EXPONENT_ATTEN` | `0x88` |  |
| `LIGHT2_EXPONENT_ATTEN` | `0x89` |  |
| `LIGHT3_EXPONENT_ATTEN` | `0x8a` |  |
| `LIGHT0_CUTOFF_ATTEN` | `0x8b` |  |
| `LIGHT1_CUTOFF_ATTEN` | `0x8c` |  |
| `LIGHT2_CUTOFF_ATTEN` | `0x8d` |  |
| `LIGHT3_CUTOFF_ATTEN` | `0x8e` |  |
| `LIGHT0_AMBIENT` | `0x8f` |  |
| `LIGHT0_DIFFUSE` | `0x90` |  |
| `LIGHT0_SPECULAR` | `0x91` |  |
| `LIGHT1_AMBIENT` | `0x92` |  |
| `LIGHT1_DIFFUSE` | `0x93` |  |
| `LIGHT1_SPECULAR` | `0x94` |  |
| `LIGHT2_AMBIENT` | `0x95` |  |
| `LIGHT2_DIFFUSE` | `0x96` |  |
| `LIGHT2_SPECULAR` | `0x97` |  |
| `LIGHT3_AMBIENT` | `0x98` |  |
| `LIGHT3_DIFFUSE` | `0x99` |  |
| `LIGHT3_SPECULAR` | `0x9a` |  |
| `CULL` | `0x9b` |  |
| `FRAME_BUF_PTR` | `0x9c` |  |
| `FRAME_BUF_WIDTH` | `0x9d` |  |
| `Z_BUF_PTR` | `0x9e` |  |
| `Z_BUF_WIDTH` | `0x9f` |  |
| `TEX_ADDR0` | `0xa0` |  |
| `TEX_ADDR1` | `0xa1` |  |
| `TEX_ADDR2` | `0xa2` |  |
| `TEX_ADDR3` | `0xa3` |  |
| `TEX_ADDR4` | `0xa4` |  |
| `TEX_ADDR5` | `0xa5` |  |
| `TEX_ADDR6` | `0xa6` |  |
| `TEX_ADDR7` | `0xa7` |  |
| `TEX_BUF_WIDTH0` | `0xa8` |  |
| `TEX_BUF_WIDTH1` | `0xa9` |  |
| `TEX_BUF_WIDTH2` | `0xaa` |  |
| `TEX_BUF_WIDTH3` | `0xab` |  |
| `TEX_BUF_WIDTH4` | `0xac` |  |
| `TEX_BUF_WIDTH5` | `0xad` |  |
| `TEX_BUF_WIDTH6` | `0xae` |  |
| `TEX_BUF_WIDTH7` | `0xaf` |  |
| `CLUT_BUF_PTR` | `0xb0` |  |
| `CLUT_BUF_WIDTH` | `0xb1` |  |
| `TRANSFER_SRC` | `0xb2` |  |
| `TRANSFER_SRC_W` | `0xb3` |  |
| `TRANSFER_DST` | `0xb4` |  |
| `TRANSFER_DST_W` | `0xb5` |  |
| `TEX_SIZE0` | `0xb8` |  |
| `TEX_SIZE1` | `0xb9` |  |
| `TEX_SIZE2` | `0xba` |  |
| `TEX_SIZE3` | `0xbb` |  |
| `TEX_SIZE4` | `0xbc` |  |
| `TEX_SIZE5` | `0xbd` |  |
| `TEX_SIZE6` | `0xbe` |  |
| `TEX_SIZE7` | `0xbf` |  |
| `TEX_MAP_MODE` | `0xc0` |  |
| `TEX_SHADE_MAPPING` | `0xc1` |  |
| `TEX_MODE` | `0xc2` |  |
| `TEX_FORMAT` | `0xc3` |  |
| `CLUT_LOAD` | `0xc4` |  |
| `CLUT_FORMAT` | `0xc5` |  |
| `TEX_FILTER` | `0xc6` |  |
| `TEX_WRAP` | `0xc7` |  |
| `TEX_LEVEL` | `0xc8` |  |
| `TEX_FUNC` | `0xc9` |  |
| `TEX_ENV_COLOR` | `0xca` |  |
| `TEX_FLUSH` | `0xcb` |  |
| `TEX_SYNC` | `0xcc` |  |
| `FOG1` | `0xcd` |  |
| `FOG2` | `0xce` |  |
| `FOG_COLOR` | `0xcf` |  |
| `TEX_LOD_SLOPE` | `0xd0` |  |
| `FRAMEBUF_PIX_FORMAT` | `0xd2` |  |
| `CLEAR_MODE` | `0xd3` |  |
| `SCISSOR1` | `0xd4` |  |
| `SCISSOR2` | `0xd5` |  |
| `MIN_Z` | `0xd6` |  |
| `MAX_Z` | `0xd7` |  |
| `COLOR_TEST` | `0xd8` |  |
| `COLOR_REF` | `0xd9` |  |
| `COLOR_TESTMASK` | `0xda` |  |
| `ALPHA_TEST` | `0xdb` |  |
| `STENCIL_TEST` | `0xdc` |  |
| `STENCIL_OP` | `0xdd` |  |
| `Z_TEST` | `0xde` |  |
| `BLEND_MODE` | `0xdf` |  |
| `BLEND_FIXED_A` | `0xe0` |  |
| `BLEND_FIXED_B` | `0xe1` |  |
| `DITH0` | `0xe2` |  |
| `DITH1` | `0xe3` |  |
| `DITH2` | `0xe4` |  |
| `DITH3` | `0xe5` |  |
| `LOGIC_OP` | `0xe6` |  |
| `Z_MASK` | `0xe7` |  |
| `MASK_COLOR` | `0xe8` |  |
| `MASK_ALPHA` | `0xe9` |  |
| `TRANSFER_START` | `0xea` |  |
| `TRANSFER_SRC_OFFSET` | `0xeb` |  |
| `TRANSFER_DST_OFFSET` | `0xec` |  |
| `TRANSFER_FORMAT` | `0xed` |  |
| `TRANSFER_SIZE` | `0xee` |  |
| `TRANSFER_FLIP` | `0xef` |  |
| `TRANSFER_OUT_SIZE` | `0xf0` |  |
| `TRANSFER_OUT_FORMAT` | `0xf1` |  |
| `VERTEX_WEIGHT` | `0xf2` |  |
| `VERTEX_WEIGHT_ADDR` | `0xf3` |  |
| `VERTEX_WEIGHT_SIZE` | `0xf4` |  |
| `VERTEX_WEIGHT_TYPE` | `0xf5` |  |
| `VERTEX_WEIGHT_MODEL` | `0xf6` |  |
| `VERTEX_WEIGHT_NORMALIZE` | `0xf7` |  |
| `VERTEX_WEIGHT_OFFSET` | `0xf8` |  |
| `VERTEX_WEIGHT_SCALE` | `0xf9` |  |
| `VERTEX_WEIGHT_MATRIX` | `0xfa` |  |
| `VERTEX_WEIGHT_MATRIX_ADDR` | `0xfb` |  |
| `VERTEX_WEIGHT_MATRIX_SIZE` | `0xfc` |  |
| `VERTEX_WEIGHT_MATRIX_TYPE` | `0xfd` |  |
| `VERTEX_WEIGHT_MATRIX_MODEL` | `0xfe` |  |
| `VERTEX_WEIGHT_MATRIX_NORMALIZE` | `0xff` |  |

## Functions

### `callbackSig()`

```c
void callbackSig(int id, void *arg);
```

### `callbackFin()`

```c
void callbackFin(int id, void *arg);
```

### `sendCommandi()`

```c
static void sendCommandi(GECommand cmd, int argument);
```

### `sendCommandf()`

```c
static void sendCommandf(GECommand cmd, float argument);
```

### `_sceGuUpdateStallAddr()`

```c
static int _sceGuUpdateStallAddr(void);
```

## Variables

### `gu_contexts`

```c
GuContext gu_contexts[3][3];
```

### `ge_list_executed`

```c
int ge_list_executed[2][2];
```

### `ge_edram_address`

```c
void* ge_edram_address;
```

### `gu_settings`

```c
GuSettings gu_settings;
```

### `gu_list`

```c
GuDisplayList* gu_list;
```

### `gu_curr_context`

```c
int gu_curr_context;
```

### `gu_init`

```c
int gu_init;
```

### `gu_first_start`

```c
int gu_first_start;
```

### `gu_display_on`

```c
int gu_display_on;
```

### `gu_call_mode`

```c
int gu_call_mode;
```

### `gu_states`

```c
int gu_states;
```

### `gu_draw_buffer`

```c
GuDrawBuffer gu_draw_buffer;
```

### `gu_object_stack`

```c
unsigned int* gu_object_stack[][];
```

### `gu_object_stack_depth`

```c
int gu_object_stack_depth;
```

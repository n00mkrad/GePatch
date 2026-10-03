[PSPSDK documentation](../../README.md) › Files

# gu/pspgu.h

```c
#include <psptypes.h>
#include <pspge.h>
```

Topics: [Graphics Utility Library](../../topics/GU.md)

## Macros

### `GU_PI`

```c
#define GU_PI (3.141593f)
```

### `GU_FALSE`

```c
#define GU_FALSE (0)
```

### `GU_TRUE`

```c
#define GU_TRUE (1)
```

### `GU_POINTS`

```c
#define GU_POINTS (0)
```

### `GU_LINES`

```c
#define GU_LINES (1)
```

### `GU_LINE_STRIP`

```c
#define GU_LINE_STRIP (2)
```

### `GU_TRIANGLES`

```c
#define GU_TRIANGLES (3)
```

### `GU_TRIANGLE_STRIP`

```c
#define GU_TRIANGLE_STRIP (4)
```

### `GU_TRIANGLE_FAN`

```c
#define GU_TRIANGLE_FAN (5)
```

### `GU_SPRITES`

```c
#define GU_SPRITES (6)
```

### `GU_ALPHA_TEST`

```c
#define GU_ALPHA_TEST (0)
```

### `GU_DEPTH_TEST`

```c
#define GU_DEPTH_TEST (1)
```

### `GU_SCISSOR_TEST`

```c
#define GU_SCISSOR_TEST (2)
```

### `GU_STENCIL_TEST`

```c
#define GU_STENCIL_TEST (3)
```

### `GU_BLEND`

```c
#define GU_BLEND (4)
```

### `GU_CULL_FACE`

```c
#define GU_CULL_FACE (5)
```

### `GU_DITHER`

```c
#define GU_DITHER (6)
```

### `GU_FOG`

```c
#define GU_FOG (7)
```

### `GU_CLIP_PLANES`

```c
#define GU_CLIP_PLANES (8)
```

### `GU_TEXTURE_2D`

```c
#define GU_TEXTURE_2D (9)
```

### `GU_LIGHTING`

```c
#define GU_LIGHTING (10)
```

### `GU_LIGHT0`

```c
#define GU_LIGHT0 (11)
```

### `GU_LIGHT1`

```c
#define GU_LIGHT1 (12)
```

### `GU_LIGHT2`

```c
#define GU_LIGHT2 (13)
```

### `GU_LIGHT3`

```c
#define GU_LIGHT3 (14)
```

### `GU_LINE_SMOOTH`

```c
#define GU_LINE_SMOOTH (15)
```

### `GU_PATCH_CULL_FACE`

```c
#define GU_PATCH_CULL_FACE (16)
```

### `GU_COLOR_TEST`

```c
#define GU_COLOR_TEST (17)
```

### `GU_COLOR_LOGIC_OP`

```c
#define GU_COLOR_LOGIC_OP (18)
```

### `GU_FACE_NORMAL_REVERSE`

```c
#define GU_FACE_NORMAL_REVERSE (19)
```

### `GU_PATCH_FACE`

```c
#define GU_PATCH_FACE (20)
```

### `GU_FRAGMENT_2X`

```c
#define GU_FRAGMENT_2X (21)
```

### `GU_MAX_STATUS`

```c
#define GU_MAX_STATUS (22)
```

### `GU_PROJECTION`

```c
#define GU_PROJECTION (0)
```

### `GU_VIEW`

```c
#define GU_VIEW (1)
```

### `GU_MODEL`

```c
#define GU_MODEL (2)
```

### `GU_TEXTURE`

```c
#define GU_TEXTURE (3)
```

### `GU_TEXTURE_SHIFT()`

```c
#define GU_TEXTURE_SHIFT(n) ((n)<<0)
```

### `GU_TEXTURE_8BIT`

```c
#define GU_TEXTURE_8BIT GU_TEXTURE_SHIFT(1)
```

### `GU_TEXTURE_16BIT`

```c
#define GU_TEXTURE_16BIT GU_TEXTURE_SHIFT(2)
```

### `GU_TEXTURE_32BITF`

```c
#define GU_TEXTURE_32BITF GU_TEXTURE_SHIFT(3)
```

### `GU_TEXTURE_BITS`

```c
#define GU_TEXTURE_BITS GU_TEXTURE_SHIFT(3)
```

### `GU_COLOR_SHIFT()`

```c
#define GU_COLOR_SHIFT(n) ((n)<<2)
```

### `GU_COLOR_5650`

```c
#define GU_COLOR_5650 GU_COLOR_SHIFT(4)
```

### `GU_COLOR_5551`

```c
#define GU_COLOR_5551 GU_COLOR_SHIFT(5)
```

### `GU_COLOR_4444`

```c
#define GU_COLOR_4444 GU_COLOR_SHIFT(6)
```

### `GU_COLOR_8888`

```c
#define GU_COLOR_8888 GU_COLOR_SHIFT(7)
```

### `GU_COLOR_BITS`

```c
#define GU_COLOR_BITS GU_COLOR_SHIFT(7)
```

### `GU_NORMAL_SHIFT()`

```c
#define GU_NORMAL_SHIFT(n) ((n)<<5)
```

### `GU_NORMAL_8BIT`

```c
#define GU_NORMAL_8BIT GU_NORMAL_SHIFT(1)
```

### `GU_NORMAL_16BIT`

```c
#define GU_NORMAL_16BIT GU_NORMAL_SHIFT(2)
```

### `GU_NORMAL_32BITF`

```c
#define GU_NORMAL_32BITF GU_NORMAL_SHIFT(3)
```

### `GU_NORMAL_BITS`

```c
#define GU_NORMAL_BITS GU_NORMAL_SHIFT(3)
```

### `GU_VERTEX_SHIFT()`

```c
#define GU_VERTEX_SHIFT(n) ((n)<<7)
```

### `GU_VERTEX_8BIT`

```c
#define GU_VERTEX_8BIT GU_VERTEX_SHIFT(1)
```

### `GU_VERTEX_16BIT`

```c
#define GU_VERTEX_16BIT GU_VERTEX_SHIFT(2)
```

### `GU_VERTEX_32BITF`

```c
#define GU_VERTEX_32BITF GU_VERTEX_SHIFT(3)
```

### `GU_VERTEX_BITS`

```c
#define GU_VERTEX_BITS GU_VERTEX_SHIFT(3)
```

### `GU_WEIGHT_SHIFT()`

```c
#define GU_WEIGHT_SHIFT(n) ((n)<<9)
```

### `GU_WEIGHT_8BIT`

```c
#define GU_WEIGHT_8BIT GU_WEIGHT_SHIFT(1)
```

### `GU_WEIGHT_16BIT`

```c
#define GU_WEIGHT_16BIT GU_WEIGHT_SHIFT(2)
```

### `GU_WEIGHT_32BITF`

```c
#define GU_WEIGHT_32BITF GU_WEIGHT_SHIFT(3)
```

### `GU_WEIGHT_BITS`

```c
#define GU_WEIGHT_BITS GU_WEIGHT_SHIFT(3)
```

### `GU_INDEX_SHIFT()`

```c
#define GU_INDEX_SHIFT(n) ((n)<<11)
```

### `GU_INDEX_8BIT`

```c
#define GU_INDEX_8BIT GU_INDEX_SHIFT(1)
```

### `GU_INDEX_16BIT`

```c
#define GU_INDEX_16BIT GU_INDEX_SHIFT(2)
```

### `GU_INDEX_BITS`

```c
#define GU_INDEX_BITS GU_INDEX_SHIFT(3)
```

### `GU_WEIGHTS()`

```c
#define GU_WEIGHTS(n) ((((n)-1)&7)<<14)
```

### `GU_WEIGHTS_BITS`

```c
#define GU_WEIGHTS_BITS GU_WEIGHTS(8)
```

### `GU_VERTICES()`

```c
#define GU_VERTICES(n) ((((n)-1)&7)<<18)
```

### `GU_VERTICES_BITS`

```c
#define GU_VERTICES_BITS GU_VERTICES(8)
```

### `GU_TRANSFORM_SHIFT()`

```c
#define GU_TRANSFORM_SHIFT(n) ((n)<<23)
```

### `GU_TRANSFORM_3D`

```c
#define GU_TRANSFORM_3D GU_TRANSFORM_SHIFT(0)
```

### `GU_TRANSFORM_2D`

```c
#define GU_TRANSFORM_2D GU_TRANSFORM_SHIFT(1)
```

### `GU_TRANSFORM_BITS`

```c
#define GU_TRANSFORM_BITS GU_TRANSFORM_SHIFT(1)
```

### `GU_DISPLAY_OFF`

```c
#define GU_DISPLAY_OFF 0
```

### `GU_DISPLAY_ON`

```c
#define GU_DISPLAY_ON 1
```

### `GU_SCR_WIDTH`

```c
#define GU_SCR_WIDTH 480
```

### `GU_SCR_HEIGHT`

```c
#define GU_SCR_HEIGHT 272
```

### `GU_SCR_ASPECT`

```c
#define GU_SCR_ASPECT ((float)GU_SCR_WIDTH / (float)GU_SCR_HEIGHT)
```

### `GU_SCR_OFFSETX`

```c
#define GU_SCR_OFFSETX ((4096 - GU_SCR_WIDTH) / 2)
```

### `GU_SCR_OFFSETY`

```c
#define GU_SCR_OFFSETY ((4096 - GU_SCR_HEIGHT) / 2)
```

### `GU_VRAM_TOP`

```c
#define GU_VRAM_TOP 0x00000000
```

### `GU_VRAM_WIDTH`

```c
#define GU_VRAM_WIDTH 512
```

### `GU_VRAM_BUFSIZE`

```c
#define GU_VRAM_BUFSIZE (GU_VRAM_WIDTH*GU_SCR_HEIGHT*2)
```

### `GU_VRAM_BP_0`

```c
#define GU_VRAM_BP_0 (void *)(GU_VRAM_TOP)
```

### `GU_VRAM_BP_1`

```c
#define GU_VRAM_BP_1 (void *)(GU_VRAM_TOP+GU_VRAM_BUFSIZE)
```

### `GU_VRAM_BP_2`

```c
#define GU_VRAM_BP_2 (void *)(GU_VRAM_TOP+(GU_VRAM_BUFSIZE*2))
```

### `GU_VRAM_BUFSIZE32`

```c
#define GU_VRAM_BUFSIZE32 (GU_VRAM_WIDTH*GU_SCR_HEIGHT*4)
```

### `GU_VRAM_BP32_0`

```c
#define GU_VRAM_BP32_0 (void *)(GU_VRAM_TOP)
```

### `GU_VRAM_BP32_1`

```c
#define GU_VRAM_BP32_1 (void *)(GU_VRAM_TOP+GU_VRAM_BUFSIZE32)
```

### `GU_VRAM_BP32_2`

```c
#define GU_VRAM_BP32_2 (void *)(GU_VRAM_TOP+(GU_VRAM_BUFSIZE32*2))
```

### `GU_PSM_5650`

```c
#define GU_PSM_5650 (0) /* Display, Texture, Palette */
```

### `GU_PSM_5551`

```c
#define GU_PSM_5551 (1) /* Display, Texture, Palette */
```

### `GU_PSM_4444`

```c
#define GU_PSM_4444 (2) /* Display, Texture, Palette */
```

### `GU_PSM_8888`

```c
#define GU_PSM_8888 (3) /* Display, Texture, Palette */
```

### `GU_PSM_T4`

```c
#define GU_PSM_T4 (4) /* Texture */
```

### `GU_PSM_T8`

```c
#define GU_PSM_T8 (5) /* Texture */
```

### `GU_PSM_T16`

```c
#define GU_PSM_T16 (6) /* Texture */
```

### `GU_PSM_T32`

```c
#define GU_PSM_T32 (7) /* Texture */
```

### `GU_PSM_DXT1`

```c
#define GU_PSM_DXT1 (8) /* Texture */
```

### `GU_PSM_DXT3`

```c
#define GU_PSM_DXT3 (9) /* Texture */
```

### `GU_PSM_DXT5`

```c
#define GU_PSM_DXT5 (10) /* Texture */
```

### `GU_FILL_FILL`

```c
#define GU_FILL_FILL (0)
```

### `GU_OPEN_FILL`

```c
#define GU_OPEN_FILL (1)
```

### `GU_FILL_OPEN`

```c
#define GU_FILL_OPEN (2)
```

### `GU_OPEN_OPEN`

```c
#define GU_OPEN_OPEN (3)
```

### `GU_FLAT`

```c
#define GU_FLAT (0)
```

### `GU_SMOOTH`

```c
#define GU_SMOOTH (1)
```

### `GU_CLEAR`

```c
#define GU_CLEAR (0)
```

### `GU_AND`

```c
#define GU_AND (1)
```

### `GU_AND_REVERSE`

```c
#define GU_AND_REVERSE (2)
```

### `GU_COPY`

```c
#define GU_COPY (3)
```

### `GU_AND_INVERTED`

```c
#define GU_AND_INVERTED (4)
```

### `GU_NOOP`

```c
#define GU_NOOP (5)
```

### `GU_XOR`

```c
#define GU_XOR (6)
```

### `GU_OR`

```c
#define GU_OR (7)
```

### `GU_NOR`

```c
#define GU_NOR (8)
```

### `GU_EQUIV`

```c
#define GU_EQUIV (9)
```

### `GU_INVERTED`

```c
#define GU_INVERTED (10)
```

### `GU_OR_REVERSE`

```c
#define GU_OR_REVERSE (11)
```

### `GU_COPY_INVERTED`

```c
#define GU_COPY_INVERTED (12)
```

### `GU_OR_INVERTED`

```c
#define GU_OR_INVERTED (13)
```

### `GU_NAND`

```c
#define GU_NAND (14)
```

### `GU_SET`

```c
#define GU_SET (15)
```

### `GU_NEAREST`

```c
#define GU_NEAREST (0)
```

### `GU_LINEAR`

```c
#define GU_LINEAR (1)
```

### `GU_NEAREST_MIPMAP_NEAREST`

```c
#define GU_NEAREST_MIPMAP_NEAREST (4)
```

### `GU_LINEAR_MIPMAP_NEAREST`

```c
#define GU_LINEAR_MIPMAP_NEAREST (5)
```

### `GU_NEAREST_MIPMAP_LINEAR`

```c
#define GU_NEAREST_MIPMAP_LINEAR (6)
```

### `GU_LINEAR_MIPMAP_LINEAR`

```c
#define GU_LINEAR_MIPMAP_LINEAR (7)
```

### `GU_TEXTURE_COORDS`

```c
#define GU_TEXTURE_COORDS (0)
```

### `GU_TEXTURE_MATRIX`

```c
#define GU_TEXTURE_MATRIX (1)
```

### `GU_ENVIRONMENT_MAP`

```c
#define GU_ENVIRONMENT_MAP (2)
```

### `GU_TEXTURE_AUTO`

```c
#define GU_TEXTURE_AUTO (0)
```

### `GU_TEXTURE_CONST`

```c
#define GU_TEXTURE_CONST (1)
```

### `GU_TEXTURE_SLOPE`

```c
#define GU_TEXTURE_SLOPE (2)
```

### `GU_POSITION`

```c
#define GU_POSITION (0)
```

### `GU_UV`

```c
#define GU_UV (1)
```

### `GU_NORMALIZED_NORMAL`

```c
#define GU_NORMALIZED_NORMAL (2)
```

### `GU_NORMAL`

```c
#define GU_NORMAL (3)
```

### `GU_REPEAT`

```c
#define GU_REPEAT (0)
```

### `GU_CLAMP`

```c
#define GU_CLAMP (1)
```

### `GU_CW`

```c
#define GU_CW (0)
```

### `GU_CCW`

```c
#define GU_CCW (1)
```

### `GU_NEVER`

```c
#define GU_NEVER (0)
```

### `GU_ALWAYS`

```c
#define GU_ALWAYS (1)
```

### `GU_EQUAL`

```c
#define GU_EQUAL (2)
```

### `GU_NOTEQUAL`

```c
#define GU_NOTEQUAL (3)
```

### `GU_LESS`

```c
#define GU_LESS (4)
```

### `GU_LEQUAL`

```c
#define GU_LEQUAL (5)
```

### `GU_GREATER`

```c
#define GU_GREATER (6)
```

### `GU_GEQUAL`

```c
#define GU_GEQUAL (7)
```

### `GU_COLOR_BUFFER_BIT`

```c
#define GU_COLOR_BUFFER_BIT (1)
```

### `GU_STENCIL_BUFFER_BIT`

```c
#define GU_STENCIL_BUFFER_BIT (2)
```

### `GU_DEPTH_BUFFER_BIT`

```c
#define GU_DEPTH_BUFFER_BIT (4)
```

### `GU_FAST_CLEAR_BIT`

```c
#define GU_FAST_CLEAR_BIT (16)
```

### `GU_TFX_MODULATE`

```c
#define GU_TFX_MODULATE (0)
```

### `GU_TFX_DECAL`

```c
#define GU_TFX_DECAL (1)
```

### `GU_TFX_BLEND`

```c
#define GU_TFX_BLEND (2)
```

### `GU_TFX_REPLACE`

```c
#define GU_TFX_REPLACE (3)
```

### `GU_TFX_ADD`

```c
#define GU_TFX_ADD (4)
```

### `GU_TCC_RGB`

```c
#define GU_TCC_RGB (0)
```

### `GU_TCC_RGBA`

```c
#define GU_TCC_RGBA (1)
```

### `GU_ADD`

```c
#define GU_ADD (0)
```

### `GU_SUBTRACT`

```c
#define GU_SUBTRACT (1)
```

### `GU_REVERSE_SUBTRACT`

```c
#define GU_REVERSE_SUBTRACT (2)
```

### `GU_MIN`

```c
#define GU_MIN (3)
```

### `GU_MAX`

```c
#define GU_MAX (4)
```

### `GU_ABS`

```c
#define GU_ABS (5)
```

### `GU_OTHER_COLOR`

```c
#define GU_OTHER_COLOR (0)
```

### `GU_ONE_MINUS_OTHER_COLOR`

```c
#define GU_ONE_MINUS_OTHER_COLOR (1)
```

### `GU_SRC_ALPHA`

```c
#define GU_SRC_ALPHA (2)
```

### `GU_ONE_MINUS_SRC_ALPHA`

```c
#define GU_ONE_MINUS_SRC_ALPHA (3)
```

### `GU_DST_ALPHA`

```c
#define GU_DST_ALPHA (4)
```

### `GU_ONE_MINUS_DST_ALPHA`

```c
#define GU_ONE_MINUS_DST_ALPHA (5)
```

### `GU_DOUBLE_SRC_ALPHA`

```c
#define GU_DOUBLE_SRC_ALPHA (6)
```

### `GU_ONE_MINUS_DOUBLE_SRC_ALPHA`

```c
#define GU_ONE_MINUS_DOUBLE_SRC_ALPHA (7)
```

### `GU_DOUBLE_DST_ALPHA`

```c
#define GU_DOUBLE_DST_ALPHA (8)
```

### `GU_ONE_MINUS_DOUBLE_DST_ALPHA`

```c
#define GU_ONE_MINUS_DOUBLE_DST_ALPHA (9)
```

### `GU_FIX`

```c
#define GU_FIX (10) /* Note: behavior of 11-15 blend factors is identical to GU_FIX */
```

### `GU_SRC_COLOR`

```c
#define GU_SRC_COLOR (0) /* Deprecated */
```

### `GU_ONE_MINUS_SRC_COLOR`

```c
#define GU_ONE_MINUS_SRC_COLOR (1) /* Deprecated */
```

### `GU_DST_COLOR`

```c
#define GU_DST_COLOR (0) /* Deprecated */
```

### `GU_ONE_MINUS_DST_COLOR`

```c
#define GU_ONE_MINUS_DST_COLOR (1) /* Deprecated */
```

### `GU_KEEP`

```c
#define GU_KEEP (0)
```

### `GU_ZERO`

```c
#define GU_ZERO (1)
```

### `GU_REPLACE`

```c
#define GU_REPLACE (2)
```

### `GU_INVERT`

```c
#define GU_INVERT (3)
```

### `GU_INCR`

```c
#define GU_INCR (4)
```

### `GU_DECR`

```c
#define GU_DECR (5)
```

### `GU_AMBIENT`

```c
#define GU_AMBIENT (1)
```

### `GU_DIFFUSE`

```c
#define GU_DIFFUSE (2)
```

### `GU_SPECULAR`

```c
#define GU_SPECULAR (4)
```

### `GU_AMBIENT_AND_DIFFUSE`

```c
#define GU_AMBIENT_AND_DIFFUSE (GU_AMBIENT|GU_DIFFUSE)
```

### `GU_DIFFUSE_AND_SPECULAR`

```c
#define GU_DIFFUSE_AND_SPECULAR (GU_DIFFUSE|GU_SPECULAR)
```

### `GU_POWERED_DIFFUSE`

```c
#define GU_POWERED_DIFFUSE (8)
```

### `GU_SINGLE_COLOR`

```c
#define GU_SINGLE_COLOR (0)
```

### `GU_SEPARATE_SPECULAR_COLOR`

```c
#define GU_SEPARATE_SPECULAR_COLOR (1)
```

### `GU_DIRECTIONAL`

```c
#define GU_DIRECTIONAL (0)
```

### `GU_POINTLIGHT`

```c
#define GU_POINTLIGHT (1)
```

### `GU_SPOTLIGHT`

```c
#define GU_SPOTLIGHT (2)
```

### `GU_DIRECT`

```c
#define GU_DIRECT (0)
```

### `GU_CALL`

```c
#define GU_CALL (1)
```

### `GU_SEND`

```c
#define GU_SEND (2)
```

### `GU_TAIL`

```c
#define GU_TAIL (0)
```

### `GU_HEAD`

```c
#define GU_HEAD (1)
```

### `GU_SYNC_FINISH`

```c
#define GU_SYNC_FINISH (0)
```

### `GU_SYNC_SIGNAL`

```c
#define GU_SYNC_SIGNAL (1)
```

### `GU_SYNC_DONE`

```c
#define GU_SYNC_DONE (2)
```

### `GU_SYNC_LIST`

```c
#define GU_SYNC_LIST (3)
```

### `GU_SYNC_SEND`

```c
#define GU_SYNC_SEND (4)
```

### `GU_SYNC_WAIT`

```c
#define GU_SYNC_WAIT (0)
```

### `GU_SYNC_NOWAIT`

```c
#define GU_SYNC_NOWAIT (1)
```

### `GU_SYNC_WHAT_DONE`

```c
#define GU_SYNC_WHAT_DONE (0)
```

### `GU_SYNC_WHAT_QUEUED`

```c
#define GU_SYNC_WHAT_QUEUED (1)
```

### `GU_SYNC_WHAT_DRAW`

```c
#define GU_SYNC_WHAT_DRAW (2)
```

### `GU_SYNC_WHAT_STALL`

```c
#define GU_SYNC_WHAT_STALL (3)
```

### `GU_SYNC_WHAT_CANCEL`

```c
#define GU_SYNC_WHAT_CANCEL (4)
```

### `GU_CALL_NORMAL`

```c
#define GU_CALL_NORMAL (0)
```

### `GU_CALL_SIGNAL`

```c
#define GU_CALL_SIGNAL (1)
```

### `GU_SIGNAL_WAIT`

```c
#define GU_SIGNAL_WAIT (1)
```

### `GU_SIGNAL_NOWAIT`

```c
#define GU_SIGNAL_NOWAIT (2)
```

### `GU_SIGNAL_PAUSE`

```c
#define GU_SIGNAL_PAUSE (3)
```

### `GU_CALLBACK_SIGNAL`

```c
#define GU_CALLBACK_SIGNAL (1)
```

### `GU_CALLBACK_FINISH`

```c
#define GU_CALLBACK_FINISH (4)
```

### `GU_BEHAVIOR_SUSPEND`

```c
#define GU_BEHAVIOR_SUSPEND (1)
```

### `GU_BEHAVIOR_CONTINUE`

```c
#define GU_BEHAVIOR_CONTINUE (2)
```

### `GU_BREAK_PAUSE`

```c
#define GU_BREAK_PAUSE (0)
```

### `GU_BREAK_CANCEL`

```c
#define GU_BREAK_CANCEL (1)
```

### `GU_ABGR()`

```c
#define GU_ABGR(a, b, g, r) (((a) << 24)|((b) << 16)|((g) << 8)|(r))
```

### `GU_ARGB()`

```c
#define GU_ARGB(a, r, g, b) GU_ABGR((a),(b),(g),(r))
```

### `GU_RGBA()`

```c
#define GU_RGBA(r, g, b, a) GU_ARGB((a),(r),(g),(b))
```

### `GU_COLOR()`

```c
#define GU_COLOR(r, g, b, a) GU_RGBA((u32)((r) * 255.0f),(u32)((g) * 255.0f),(u32)((b) * 255.0f),(u32)((a) * 255.0f))
```

## Typedefs

### `GuCallback`

```c
typedef void(* GuCallback) (int id))(int id);
```

Callback for signal and finish events.

### `GuSwapBuffersCallback`

```c
typedef void(* GuSwapBuffersCallback) (void **display, void **render))(void **display, void **render);
```

Callback for the framebuffer swap.

## Functions

### `sceGuDepthBuffer()`

```c
void sceGuDepthBuffer(void *zbp, int zbw);
```

Set depth buffer parameters.

**Parameters:**

- `zbp` – VRAM pointer where the depthbuffer should start
- `zbw` – The width of the depth-buffer (block-aligned)

### `sceGuDispBuffer()`

```c
void sceGuDispBuffer(int width, int height, void *dispbp, int dispbw);
```

Set display buffer parameters.

**Example: Setup a standard 16-bit display buffer:**

```c
sceGuDispBuffer(480,272,(void*)512*272*2,512); // 480*272, skipping the draw buffer located at address 0
```

**Parameters:**

- `width` – Width of the display buffer in pixels
- `height` – Width of the display buffer in pixels
- `dispbp` – VRAM pointer to where the display-buffer starts
- `dispbw` – Display buffer width (block aligned)

### `sceGuDrawBuffer()`

```c
void sceGuDrawBuffer(int psm, void *fbp, int fbw);
```

Set draw buffer parameters (and store in context for buffer-swap)

Available pixel formats are:

- GU_PSM_5650
- GU_PSM_5551
- GU_PSM_4444
- GU_PSM_8888

**Example: Setup a standard 16-bit draw buffer:**

```c
sceGuDrawBuffer(GU_PSM_5551,(void*)0,512);
```

**Parameters:**

- `psm` – Pixel format to use for rendering (and display)
- `fbp` – VRAM pointer to where the draw buffer starts
- `fbw` – Frame buffer width (block aligned)

### `sceGuDrawBufferList()`

```c
void sceGuDrawBufferList(int psm, void *fbp, int fbw);
```

Set draw buffer directly, not storing parameters in the context.

**Parameters:**

- `psm` – Pixel format to use for rendering
- `fbp` – VRAM pointer to where the draw buffer starts
- `fbw` – Frame buffer width (block aligned)

### `sceGuDisplay()`

```c
int sceGuDisplay(int state);
```

Turn display on or off.

Available states are:

- GU_DISPLAY_ON (1) - Turns display on
- GU_DISPLAY_OFF (0) - Turns display off

**Parameters:**

- `state` – Turn display on or off

**Returns:** State of the display prior to this call

### `sceGuDepthFunc()`

```c
void sceGuDepthFunc(int function);
```

Select which depth-test function to use.

Valid choices for the depth-test are:

- GU_NEVER - No pixels pass the depth-test
- GU_ALWAYS - All pixels pass the depth-test
- GU_EQUAL - Pixels that match the depth-test pass
- GU_NOTEQUAL - Pixels that doesn't match the depth-test pass
- GU_LESS - Pixels that are less in depth passes
- GU_LEQUAL - Pixels that are less or equal in depth passes
- GU_GREATER - Pixels that are greater in depth passes
- GU_GEQUAL - Pixels that are greater or equal passes

**Parameters:**

- `function` – Depth test function to use

### `sceGuDepthMask()`

```c
void sceGuDepthMask(int mask);
```

Mask depth buffer writes.

**Parameters:**

- `mask` – [GU_TRUE(1)](#gu_true) to disable Z writes, [GU_FALSE(0)](#gu_false) to enable

### `sceGuDepthOffset()`

```c
void sceGuDepthOffset(unsigned int offset);
```

### `sceGuDepthRange()`

```c
void sceGuDepthRange(int near, int far);
```

Set which range to use for depth calculations.

**Note:** The depth buffer is inversed, and takes values from 65535 to 0.

Example: Use the entire depth-range for calculations:

```c
sceGuDepthRange(65535,0);
```

**Parameters:**

- `near` – Value to use for the near plane
- `far` – Value to use for the far plane

### `sceGuFog()`

```c
void sceGuFog(float near, float far, unsigned int color);
```

### `sceGuInit()`

```c
int sceGuInit(void);
```

Initalize the GU system.

This function MUST be called as the first function, otherwise state is undetermined.

**Returns:** 0 for success, \< 0 for failure

### `sceGuTerm()`

```c
void sceGuTerm(void);
```

Shutdown the GU system.

Called when GU is no longer needed

### `guGetInit()`

```c
int guGetInit();
```

Get if the GU system has been initialized.

Returns 1 after [sceGuInit()](#sceguinit) has been called, returns 0 otherwise or after [sceGuTerm()](#sceguterm) has been called.

**Returns:** Whether the GU system has been initialized or not

### `sceGuBreak()`

```c
int sceGuBreak(int mode);
```

Break the display list.

**Parameters:**

- `mode` – Mode to break the display list. Valid modes are:

  - GU_BREAK_PAUSE - Pause the display list
  - GU_BREAK_CANCEL - Cancel drawing queue

**Returns:** 0 for success, \< 0 for failure

### `sceGuContinue()`

```c
int sceGuContinue(void);
```

Continue the display list.

**Returns:** 0 for success, \< 0 for failure

### `sceGuSetCallback()`

```c
void * sceGuSetCallback(int signal, GuCallback callback);
```

Setup signal handler.

Available signals are:

- GU_CALLBACK_SIGNAL - Called when sceGuSignal is used
- GU_CALLBACK_FINISH - Called when display list is finished

**Parameters:**

- `signal` – Signal index to install a handler for
- `callback` – Callback to call when signal index is triggered

**Returns:** The old callback handler

### `sceGuSignal()`

```c
void sceGuSignal(int mode, int id);
```

Trigger signal to call code from the command stream.

Available signal interrupt modes are:

- GU_SIGNAL_WAIT - Wait for callback to finish
- GU_SIGNAL_NOWAIT - Do not wait for callback to finish
- GU_SIGNAL_PAUSE - Pause execution until callback is finished

**Parameters:**

- `mode` – Signal interrupt mode
- `id` – Signal id

### `sceGuSendCommandf()`

```c
void sceGuSendCommandf(int cmd, float argument);
```

Send raw float-command to the GE.

The argument is converted into a 24-bit float before transfer.

**Parameters:**

- `cmd` – Which command to send
- `argument` – Argument to pass along

### `sceGuSendCommandi()`

```c
void sceGuSendCommandi(int cmd, int argument);
```

Send raw command to the GE.

Only the 24 lower bits of the argument is passed along.

**Parameters:**

- `cmd` – Which command to send
- `argument` – Argument to pass along

### `sceGuGetMemory()`

```c
void * sceGuGetMemory(int size);
```

Allocate memory on the current display list for temporary storage.

**Note:** This function is NOT for permanent memory allocation, the memory will be invalid as soon as you start filling the same display list again.

**Parameters:**

- `size` – How much memory to allocate

**Returns:** Memory-block ready for use

### `sceGuStart()`

```c
int sceGuStart(int ctype, void *list);
```

Start filling a new display-context.

Contexts available are:

- GU_DIRECT - Rendering is performed as list is filled
- GU_CALL - List is setup to be called from the main list
- GU_SEND - List is buffered for a later call to [sceGuSendList()](#scegusendlist)

The previous context-type is stored so that it can be restored at [sceGuFinish()](#scegufinish).

**Parameters:**

- `ctype` – Context Type
- `list` – Pointer to display-list (16 byte aligned)

**Returns:** 0 for success, \< 0 for failure

### `sceGuFinish()`

```c
int sceGuFinish(void);
```

Finish current display list and go back to the parent context.

If the context is GU_DIRECT, the stall-address is updated so that the entire list will execute. Otherwise, only the terminating action is written to the list, depending on context-type.

The finish-callback will get a zero as argument when using this function.

This also restores control back to whatever context that was active prior to this call.

**Returns:** Size of finished display list

### `sceGuFinishId()`

```c
int sceGuFinishId(unsigned int id);
```

Finish current display list and go back to the parent context, sending argument id for the finish callback.

If the context is GU_DIRECT, the stall-address is updated so that the entire list will execute. Otherwise, only the terminating action is written to the list, depending on context-type.

**Parameters:**

- `id` – Finish callback id (16-bit)

**Returns:** Size of finished display list

### `sceGuCallList()`

```c
int sceGuCallList(const void *list);
```

Call previously generated display-list.

**Parameters:**

- `list` – Display list to call

**Returns:** 0 for success, \< 0 for failure

### `sceGuCallMode()`

```c
void sceGuCallMode(int mode);
```

Set wether to use stack-based calls or signals to handle execution of called lists.

**Parameters:**

- `mode` – [GU_CALL_SIGNAL(1)](#gu_call_signal) to enable signals, [GU_CALL_NORMAL(0)](#gu_call_normal) to disable signals and use normal calls instead.

### `sceGuCheckList()`

```c
int sceGuCheckList(void);
```

Check how large the current display-list is.

**Returns:** The size of the current display list

### `sceGuSendList()`

```c
int sceGuSendList(int mode, const void *list, PspGeContext *context);
```

Send a list to the GE directly.

Available modes are:

- GU_TAIL - Place list last in the queue, so it executes in-order
- GU_HEAD - Place list first in queue so that it executes as soon as possible

**Parameters:**

- `mode` – Whether to place the list first or last in queue
- `list` – List to send
- `context` – Temporary storage for the GE context

**Returns:** 0 for success, \< 0 for failure

### `sceGuSwapBuffers()`

```c
void * sceGuSwapBuffers(void);
```

Swap display and draw buffer.

**Returns:** Pointer to the new drawbuffer

### `sceGuSync()`

```c
int sceGuSync(int mode, int what);
```

Wait until display list has finished executing.

**Example: Wait for the currently executing display list:**

```c
sceGuSync(GU_SYNC_FINISH, GU_SYNC_WHAT_DONE);
```

Available what are:

- GU_SYNC_WHAT_DONE
- GU_SYNC_WHAT_QUEUED
- GU_SYNC_WHAT_DRAW
- GU_SYNC_WHAT_STALL
- GU_SYNC_WHAT_CANCEL

Available mode are:

- GU_SYNC_FINISH - Wait until the last sceGuFinish command is reached
- GU_SYNC_SIGNAL - Wait until the last (?) signal is executed
- GU_SYNC_DONE - Wait until all commands currently in list are executed
- GU_SYNC_LIST - Wait for the currently executed display list (GU_DIRECT)
- GU_SYNC_SEND - Wait for the last send list

**Parameters:**

- `mode` – What to wait for
- `what` – What to sync to

**Returns:** Unknown at this time

### `sceGuDrawArray()`

```c
void sceGuDrawArray(int prim, int vtype, int count, const void *indices, const void *vertices);
```

Draw array of vertices forming primitives.

Available primitive-types are:

- GU_POINTS - Single pixel points (1 vertex per primitive)
- GU_LINES - Single pixel lines (2 vertices per primitive)
- GU_LINE_STRIP - Single pixel line-strip (2 vertices for the first primitive, 1 for every following)
- GU_TRIANGLES - Filled triangles (3 vertices per primitive)
- GU_TRIANGLE_STRIP - Filled triangles-strip (3 vertices for the first primitive, 1 for every following)
- GU_TRIANGLE_FAN - Filled triangle-fan (3 vertices for the first primitive, 1 for every following)
- GU_SPRITES - Filled blocks (2 vertices per primitive)

The vertex-type decides how the vertices align and what kind of information they contain.<br>The following flags are ORed together to compose the final vertex format:

- GU_TEXTURE_8BIT - 8-bit texture coordinates
- GU_TEXTURE_16BIT - 16-bit texture coordinates
- GU_TEXTURE_32BITF - 32-bit texture coordinates (float)
- GU_COLOR_5650 - 16-bit color (R5G6B5A0)
- GU_COLOR_5551 - 16-bit color (R5G5B5A1)
- GU_COLOR_4444 - 16-bit color (R4G4B4A4)
- GU_COLOR_8888 - 32-bit color (R8G8B8A8)
- GU_NORMAL_8BIT - 8-bit normals
- GU_NORMAL_16BIT - 16-bit normals
- GU_NORMAL_32BITF - 32-bit normals (float)
- GU_VERTEX_8BIT - 8-bit vertex position
- GU_VERTEX_16BIT - 16-bit vertex position
- GU_VERTEX_32BITF - 32-bit vertex position (float)
- GU_WEIGHT_8BIT - 8-bit weights
- GU_WEIGHT_16BIT - 16-bit weights
- GU_WEIGHT_32BITF - 32-bit weights (float)
- GU_INDEX_8BIT - 8-bit vertex index
- GU_INDEX_16BIT - 16-bit vertex index
- [GU_WEIGHTS(n)](#gu_weights) - Number of weights (1-8)
- [GU_VERTICES(n)](#gu_vertices) - Number of vertices (1-8)
- GU_TRANSFORM_2D - Coordinate is passed directly to the rasterizer
- GU_TRANSFORM_3D - Coordinate is transformed before passed to rasterizer

Data members inside a vertex are laid out in the following order:

- Weights - if [GU_WEIGHTS(n)](#gu_weights) is used N weights are present
- Texture Coordinates
- Color
- Normal
- Position

If [GU_VERTICES(n)](#gu_vertices) is used the entire vertex structure is repeated N-times.<br>A member is only present if related type flag has been used (look at examples below).

**Note:** Every member making up a vertex must be aligned to 16 bits.

**Notes on 16 bit vertex/texture/normal formats::**

- Values are stored as 16-bit signed integers, with a range of -32768 to 32767
- In the floating point coordinate space this is mapped as -1.0 to 1.0
- To scale this to be such that the value 1 in 16 bit space is 1 unit in floating point space, use [sceGumScale()](../gum/pspgum.h.md#scegumscale) for vertices; (see [pspgum.h](../gum/pspgum.h.md))

  - You can technically use this to create whatever fixed-point space you want (a common one is 5 bits for the decimals)
  - Caveat: you need to use the sceGumDrawArray method to apply the affine transform to the vertices.
  - [sceGuDrawArray()](#scegudrawarray) will not apply the affine transform to the vertices.
- To scale this for texture coordinates use [sceGuTexOffset()](#scegutexoffset) and [sceGuTexScale()](#scegutexscale) (see below)
- You can't scale the normals with any functions, which is expected since normals by definition are unit vectors.

```c
sceGumScale(32768.0f, 32768.0f, 32768.0f); // This is an identity mapping -- 1 unit in floating point space is 1 unit in 16-bit space
sceGumDrawArray(GU_TRIANGLES, GU_TEXTURE_32BITF|GU_VERTEX_16BIT, 3, 0, vertices);
```

**Notes on 8 bit vertex/texture/normal formats::**

- Values are stored as 8-bit signed integers with a range of -128 to 127
- In the floating point coordinate space this is mapped as -1.0 to 1.0
- To scale this to be such that the value 1 in 8 bit space is 1 unit in floating point space, use [sceGumScale()](../gum/pspgum.h.md#scegumscale) for vertices; (see above).
- The scaling factor as demonstrated will be 128.0f.
- See above for notes on texture and normals.

**Example: Render 400 triangles, with floating-point texture coordinates, and floating-point position, no indices:**

```c
sceGuDrawArray(GU_TRIANGLES,GU_TEXTURE_32BITF|GU_VERTEX_32BITF,400*3,0,vertices);
```

**Parameters:**

- `prim` – What kind of primitives to render
- `vtype` – Vertex type to process
- `count` – How many vertices to process
- `indices` – Optional pointer to an index-list
- `vertices` – Pointer to a vertex-list

### `sceGuBeginObject()`

```c
void sceGuBeginObject(int vtype, int count, const void *indices, const void *vertices);
```

Begin conditional rendering of object.

If no vertices passed into this function are inside the scissor region, it will skip rendering the object. There can be up to 32 levels of conditional testing, and all levels HAVE to be terminated by [sceGuEndObject()](#sceguendobject).

**Example: test a boundingbox against the frustum, and if visible, render object:**

```c
sceGuBeginObject(GU_VERTEX_32BITF,8,0,boundingBox);
  sceGuDrawArray(GU_TRIANGLES,GU_TEXTURE_32BITF|GU_VERTEX_32BITF,vertexCount,0,vertices);
sceGuEndObject();
```

**Parameters:**

- `vtype` – Vertex type to process
- `count` – Number of vertices to test
- `indices` – Optional list to an index-list
- `vertices` – Pointer to a vertex-list

### `sceGuEndObject()`

```c
int sceGuEndObject(void);
```

End conditional rendering of object.

**Returns:** 0 for success, \< 0 for failure

### `sceGuSetStatus()`

```c
void sceGuSetStatus(int state, int status);
```

Enable or disable GE state.

Look at [sceGuEnable()](#sceguenable) for a list of states

**Parameters:**

- `state` – Which state to change
- `status` – Wether to enable or disable the state

### `sceGuGetStatus()`

```c
int sceGuGetStatus(int state);
```

Get if state is currently enabled or disabled.

Look at [sceGuEnable()](#sceguenable) for a list of states

**Parameters:**

- `state` – Which state to query about

**Returns:** Wether state is enabled or not

### `sceGuSetAllStatus()`

```c
void sceGuSetAllStatus(int status);
```

Set the status on all 22 available states.

Look at [sceGuEnable()](#sceguenable) for a list of states

**Parameters:**

- `status` – Bit-mask (0-21) containing the status of all 22 states

### `sceGuGetAllStatus()`

```c
int sceGuGetAllStatus(void);
```

Query status on all 22 available states.

Look at [sceGuEnable()](#sceguenable) for a list of states

**Returns:** Status of all 22 states as a bitmask (0-21)

### `sceGuEnable()`

```c
void sceGuEnable(int state);
```

Enable GE state.

The currently available states are:

- GU_ALPHA_TEST
- GU_DEPTH_TEST
- GU_SCISSOR_TEST
- GU_BLEND
- GU_CULL_FACE
- GU_DITHER
- GU_CLIP_PLANES
- GU_TEXTURE_2D
- GU_LIGHTING
- GU_LIGHT0
- GU_LIGHT1
- GU_LIGHT2
- GU_LIGHT3
- GU_COLOR_LOGIC_OP

**Parameters:**

- `state` – Which state to enable

### `sceGuDisable()`

```c
void sceGuDisable(int state);
```

Disable GE state.

Look at [sceGuEnable()](#sceguenable) for a list of states

**Parameters:**

- `state` – Which state to disable

### `sceGuLight()`

```c
void sceGuLight(int light, int type, int components, const ScePspFVector3 *position);
```

Set light parameters.

Available light types are:

- GU_DIRECTIONAL - Directional light
- GU_POINTLIGHT - Single point of light
- GU_SPOTLIGHT - Point-light with a cone

Available light components are:

- GU_AMBIENT_AND_DIFFUSE
- GU_DIFFUSE_AND_SPECULAR
- GU_POWERED_DIFFUSE

**Parameters:**

- `light` – Light index
- `type` – Light type
- `components` – Light components
- `position` – Light position

### `sceGuLightAtt()`

```c
void sceGuLightAtt(int light, float atten0, float atten1, float atten2);
```

Set light attenuation.

**Parameters:**

- `light` – Light index
- `atten0` – Constant attenuation factor
- `atten1` – Linear attenuation factor
- `atten2` – Quadratic attenuation factor

### `sceGuLightColor()`

```c
void sceGuLightColor(int light, int component, unsigned int color);
```

Set light color.

Available light components are:

- GU_AMBIENT
- GU_DIFFUSE
- GU_SPECULAR
- GU_AMBIENT_AND_DIFFUSE
- GU_DIFFUSE_AND_SPECULAR

**Parameters:**

- `light` – Light index
- `component` – Which component to set
- `color` – Which color to use

### `sceGuLightMode()`

```c
void sceGuLightMode(int mode);
```

Set light mode.

Available light modes are:

- GU_SINGLE_COLOR
- GU_SEPARATE_SPECULAR_COLOR

Separate specular colors are used to interpolate the specular component independently, so that it can be added to the fragment after the texture color.

**Parameters:**

- `mode` – Light mode to use

### `sceGuLightSpot()`

```c
void sceGuLightSpot(int light, const ScePspFVector3 *direction, float exponent, float cutoff);
```

Set spotlight parameters.

**Parameters:**

- `light` – Light index
- `direction` – Spotlight direction
- `exponent` – Spotlight exponent
- `cutoff` – Spotlight cutoff angle (in radians)

### `sceGuClear()`

```c
void sceGuClear(int flags);
```

Clear current drawbuffer.

Available clear-flags are (OR them together to get final clear-mode):

- GU_COLOR_BUFFER_BIT - Clears the color-buffer
- GU_STENCIL_BUFFER_BIT - Clears the stencil-buffer
- GU_DEPTH_BUFFER_BIT - Clears the depth-buffer

**Parameters:**

- `flags` – Which part of the buffer to clear

### `sceGuClearColor()`

```c
void sceGuClearColor(unsigned int color);
```

Set the current clear-color.

**Parameters:**

- `color` – Color to clear with

### `sceGuClearDepth()`

```c
void sceGuClearDepth(unsigned int depth);
```

Set the current clear-depth.

**Parameters:**

- `depth` – Set which depth to clear with (0x0000-0xffff)

### `sceGuClearStencil()`

```c
void sceGuClearStencil(unsigned int stencil);
```

Set the current stencil clear value.

**Parameters:**

- `stencil` – Set which stencil value to clear with (0-255)

### `sceGuPixelMask()`

```c
void sceGuPixelMask(unsigned int mask);
```

Set mask for which bits of the pixels to write.

**Parameters:**

- `mask` – Which bits to filter against writes

**Note:**

- The representation of the mask is in the format 0xAABBGGRR: 1-bits prevent writes to that bit, 0-bits allow writes.
- If you have a draw format using less than 8 bits per channel, you need to mask the higher bits as less significant bits aren't used. a draw format of GU_PSM_5650: sceGuPixelMask(0x00000000); // All channels writable sceGuPixelMask(0x0000FCF8); // Only Blue (+Alpha) writable sceGuPixelMask(0x00F800F8); // Only Green (+Alpha) writable sceGuPixelMask(0x00F8FC00); // Only Red (+Alpha) writable

### `sceGuColor()`

```c
void sceGuColor(unsigned int color);
```

Set current primitive color.

**Parameters:**

- `color` – Which color to use (overriden by vertex-colors)

### `sceGuColorFunc()`

```c
void sceGuColorFunc(int func, unsigned int color, unsigned int mask);
```

Set the color test function.

The color test is only performed while GU_COLOR_TEST is enabled.

Available functions are:

- GU_NEVER
- GU_ALWAYS
- GU_EQUAL
- GU_NOTEQUAL

**Example: Reject any pixel that does not have 0 as the blue channel:**

```c
sceGuColorFunc(GU_EQUAL,0,0xff0000);
```

**Parameters:**

- `func` – Color test function
- `color` – Color to test against
- `mask` – Mask ANDed against both source and destination when testing

### `sceGuColorMaterial()`

```c
void sceGuColorMaterial(int components);
```

Set which color components that the material will receive.

The components are ORed together from the following values:

- GU_AMBIENT
- GU_DIFFUSE
- GU_SPECULAR

**Parameters:**

- `components` – Which components to receive

### `sceGuAlphaFunc()`

```c
void sceGuAlphaFunc(int func, int value, int mask);
```

Set the alpha test parameters.

Available comparison functions are:

- GU_NEVER
- GU_ALWAYS
- GU_EQUAL
- GU_NOTEQUAL
- GU_LESS
- GU_LEQUAL
- GU_GREATER
- GU_GEQUAL

**Parameters:**

- `func` – Specifies the alpha comparison function.
- `value` – Specifies the reference value that incoming alpha values are compared to.
- `mask` – Specifies the mask that both values are ANDed with before comparison.

### `sceGuAmbient()`

```c
void sceGuAmbient(unsigned int color);
```

Set the ambient light color.

**Parameters:**

- `color` – The light color to set

### `sceGuAmbientColor()`

```c
void sceGuAmbientColor(unsigned int color);
```

Set the ambient color.

**Parameters:**

- `color` – The color to set

### `sceGuBlendFunc()`

```c
void sceGuBlendFunc(int op, int src, int dest, unsigned int srcfix, unsigned int destfix);
```

Set the blending-mode.

Keys for the blending operations:

- Cs - Source color
- Cd - Destination color
- Bs - Blend function for source fragment
- Bd - Blend function for destination fragment

Available blending-operations are:

- GU_ADD - (Cs\*Bs) + (Cd\*Bd)
- GU_SUBTRACT - (Cs\*Bs) - (Cd\*Bd)
- GU_REVERSE_SUBTRACT - (Cd\*Bd) - (Cs\*Bs)
- GU_MIN - Cs \< Cd ? Cs : Cd
- GU_MAX - Cs \< Cd ? Cd : Cs
- GU_ABS - |Cs-Cd|

Available blending-functions are:

- GU_OTHER_COLOR - dstColor if used for source operand; srcColor if used for destination operand
- GU_ONE_MINUS_OTHER_COLOR - 1-dstColor if used for source operand; 1-srcColor if used for destination operand
- GU_SRC_ALPHA - srcAlpha
- GU_ONE_MINUS_SRC_ALPHA - 1-srcAlpha
- GU_DST_ALPHA - dstAlpha
- GU_ONE_MINUS_DST_ALPHA - 1-dstAlpha
- GU_DOUBLE_SRC_ALPHA - 2\*srcAlpha
- GU_ONE_MINUS_DOUBLE_SRC_ALPHA - 1-2\*srcAlpha
- GU_DOUBLE_DST_ALPHA - 2\*dstAlpha
- GU_ONE_MINUS_DOUBLE_DST_ALPHA - 1-2\*dstAlpha
- GU_FIX - srcFix if used for source operand; dstFix if used for destination operand

**Parameters:**

- `op` – Blending Operation
- `src` – Blending function for source operand
- `dest` – Blending function for dest operand
- `srcfix` – Fix value for GU_FIX (source operand)
- `destfix` – Fix value for GU_FIX (dest operand)

### `sceGuMaterial()`

```c
void sceGuMaterial(int mode, int color);
```

### `sceGuModelColor()`

```c
void sceGuModelColor(unsigned int emissive, unsigned int ambient, unsigned int diffuse, unsigned int specular);
```

### `sceGuStencilFunc()`

```c
void sceGuStencilFunc(int func, int ref, int mask);
```

Set stencil function and reference value for stencil testing.

Available functions are:

- GU_NEVER
- GU_ALWAYS
- GU_EQUAL
- GU_NOTEQUAL
- GU_LESS
- GU_LEQUAL
- GU_GREATER
- GU_GEQUAL

**Parameters:**

- `func` – Test function
- `ref` – The reference value for the stencil test
- `mask` – Mask that is ANDed with both the reference value and stored stencil value when the test is done

### `sceGuStencilOp()`

```c
void sceGuStencilOp(int fail, int zfail, int zpass);
```

Set the stencil test actions.

Available actions are:

- GU_KEEP - Keeps the current value
- GU_ZERO - Sets the stencil buffer value to zero
- GU_REPLACE - Sets the stencil buffer value to ref, as specified by [sceGuStencilFunc()](#scegustencilfunc)
- GU_INCR - Increments the current stencil buffer value
- GU_DECR - Decrease the current stencil buffer value
- GU_INVERT - Bitwise invert the current stencil buffer value

As stencil buffer shares memory with framebuffer alpha, resolution of the buffer is directly in relation.

**Parameters:**

- `fail` – The action to take when the stencil test fails
- `zfail` – The action to take when stencil test passes, but the depth test fails
- `zpass` – The action to take when both stencil test and depth test passes

### `sceGuSpecular()`

```c
void sceGuSpecular(float power);
```

Set the specular power for the material.

**Parameters:**

- `power` – Specular power

### `sceGuFrontFace()`

```c
void sceGuFrontFace(int order);
```

Set the current face-order (for culling)

This only has effect when culling is enabled (GU_CULL_FACE)

Culling order can be:

- GU_CW - Clockwise primitives are not culled
- GU_CCW - Counter-clockwise are not culled

**Parameters:**

- `order` – Which order to use

### `sceGuLogicalOp()`

```c
void sceGuLogicalOp(int op);
```

Set color logical operation.

Available operations are:

- GU_CLEAR
- GU_AND
- GU_AND_REVERSE
- GU_COPY
- GU_AND_INVERTED
- GU_NOOP
- GU_XOR
- GU_OR
- GU_NOR
- GU_EQUIV
- GU_INVERTED
- GU_OR_REVERSE
- GU_COPY_INVERTED
- GU_OR_INVERTED
- GU_NAND
- GU_SET

This operation only has effect if GU_COLOR_LOGIC_OP is enabled.

**Note:** Unlike OpenGL, GE allows to enable both blending and color logic operations at the same time, in which case color blending will be computed as usual but stored in framebuffer using specified logical operation

**Parameters:**

- `op` – Operation to execute

### `sceGuSetDither()`

```c
void sceGuSetDither(const ScePspIMatrix4 *matrix);
```

Set ordered pixel dither matrix.

This dither matrix is only applied if GU_DITHER is enabled.

**Parameters:**

- `matrix` – Dither matrix

### `sceGuShadeModel()`

```c
void sceGuShadeModel(int mode);
```

Set how primitives are shaded.

The available shading-methods are:

- GU_FLAT - Primitives are flatshaded, the last vertex-color takes effet
- GU_SMOOTH - Primtives are gouraud-shaded, all vertex-colors take effect

**Parameters:**

- `mode` – Which mode to use

### `sceGuCopyImage()`

```c
void sceGuCopyImage(int psm, int sx, int sy, int width, int height, int srcw, void *src, int dx, int dy, int destw, void *dest);
```

Image transfer using the GE.

**Note:** Data must be aligned to 1 quad word (16 bytes)

**Example: Copy a fullscreen 32-bit image from RAM to VRAM:**

```c
sceGuCopyImage(GU_PSM_8888,0,0,480,272,512,pixels,0,0,512,(void*)(((unsigned int)framebuffer)+0x4000000));
```

**Parameters:**

- `psm` – Pixel format for buffer
- `sx` – Source X
- `sy` – Source Y
- `width` – Image width
- `height` – Image height
- `srcw` – Source buffer width (block aligned)
- `src` – Source pointer
- `dx` – Destination X
- `dy` – Destination Y
- `destw` – Destination buffer width (block aligned)
- `dest` – Destination pointer

### `sceGuTexEnvColor()`

```c
void sceGuTexEnvColor(unsigned int color);
```

Specify the texture environment color.

This is used in the texture function when a constant color is needed.

See [sceGuTexFunc()](#scegutexfunc) for more information.

**Parameters:**

- `color` – Constant color (0x00BBGGRR)

### `sceGuTexFilter()`

```c
void sceGuTexFilter(int min, int mag);
```

Set how the texture is filtered.

Available filters are:

- GU_NEAREST
- GU_LINEAR
- GU_NEAREST_MIPMAP_NEAREST
- GU_LINEAR_MIPMAP_NEAREST
- GU_NEAREST_MIPMAP_LINEAR
- GU_LINEAR_MIPMAP_LINEAR

**Parameters:**

- `min` – Minimizing filter
- `mag` – Magnifying filter

### `sceGuTexFlush()`

```c
void sceGuTexFlush(void);
```

Flush texture page-cache.

Do this if you have copied/rendered into an area currently in the texture-cache

### `sceGuTexFunc()`

```c
void sceGuTexFunc(int tfx, int tcc);
```

Set how textures are applied.

Key for the apply-modes:

- Cv - Color value result
- Ct - Texture color
- Cf - Fragment color
- Cc - Constant color (specified by [sceGuTexEnvColor()](#scegutexenvcolor))

Available apply-modes are: (TFX)

- GU_TFX_MODULATE - Cv=Ct\*Cf TCC_RGB: Av=Af TCC_RGBA: Av=At\*Af
- GU_TFX_DECAL - TCC_RGB: Cv=Ct,Av=Af TCC_RGBA: Cv=Cf\*(1-At)+Ct\*At Av=Af
- GU_TFX_BLEND - Cv=(Cf\*(1-Ct))+(Cc\*Ct) TCC_RGB: Av=Af TCC_RGBA: Av=At\*Af
- GU_TFX_REPLACE - Cv=Ct TCC_RGB: Av=Af TCC_RGBA: Av=At
- GU_TFX_ADD - Cv=Cf+Ct TCC_RGB: Av=Af TCC_RGBA: Av=At\*Af

The fields TCC_RGB and TCC_RGBA specify components that differ between the two different component modes.

- GU_TFX_MODULATE - The texture is multiplied with the current diffuse fragment
- GU_TFX_REPLACE - The texture replaces the fragment
- GU_TFX_ADD - The texture is added on-top of the diffuse fragment

Available component-modes are: (TCC)

- GU_TCC_RGB - The texture alpha does not have any effect
- GU_TCC_RGBA - The texture alpha is taken into account

**Parameters:**

- `tfx` – Which apply-mode to use
- `tcc` – Which component-mode to use

### `sceGuTexImage()`

```c
void sceGuTexImage(int mipmap, int width, int height, int tbw, const void *tbp);
```

Set current texturemap.

Textures may reside in main RAM, but it has a huge speed-penalty. Swizzle textures to get maximum speed.

**Note:** Data must be aligned to 1 quad word (16 bytes)

**Parameters:**

- `mipmap` – Mipmap level
- `width` – Width of texture (must be a power of 2)
- `height` – Height of texture (must be a power of 2)
- `tbw` – Texture Buffer Width (block-aligned)
- `tbp` – Texture buffer pointer (16 byte aligned)

### `sceGuTexLevelMode()`

```c
void sceGuTexLevelMode(unsigned int mode, float bias);
```

Set texture-level mode (mipmapping)

Available modes are:

- GU_TEXTURE_AUTO
- GU_TEXTURE_CONST
- GU_TEXTURE_SLOPE

**Parameters:**

- `mode` – Which mode to use
- `bias` – Which mipmap bias to use

### `sceGuTexMapMode()`

```c
void sceGuTexMapMode(int mode, unsigned int lu, unsigned int lv);
```

Set the texture-mapping mode.

Available modes are:

- GU_TEXTURE_COORDS
- GU_TEXTURE_MATRIX
- GU_ENVIRONMENT_MAP

**Parameters:**

- `mode` – Which mode to use
- `lu` – Light U
- `lv` – Light V

### `sceGuTexMode()`

```c
void sceGuTexMode(int tpsm, int maxmips, int mc, int swizzle);
```

Set texture-mode parameters.

Available texture-formats are:

- GU_PSM_5650 - Hicolor, 16-bit
- GU_PSM_5551 - Hicolor, 16-bit
- GU_PSM_4444 - Hicolor, 16-bit
- GU_PSM_8888 - Truecolor, 32-bit
- GU_PSM_T4 - Indexed, 4-bit (2 pixels per byte)
- GU_PSM_T8 - Indexed, 8-bit

**Parameters:**

- `tpsm` – Which texture format to use
- `maxmips` – Index of the maximum mip level to use (NOT THE NUMBER OF MIPS). Range is 0-7.
- `mc` – Multiclut on/off (0/1)
- `swizzle` – [GU_TRUE(1)](#gu_true) to swizzle texture-reads

### `sceGuTexOffset()`

```c
void sceGuTexOffset(float u, float v);
```

Set texture offset.

**Note:** Only used by the 3D T&L pipe, renders done with GU_TRANSFORM_2D are not affected by this.

**Parameters:**

- `u` – Offset to add to the U coordinate
- `v` – Offset to add to the V coordinate

### `sceGuTexProjMapMode()`

```c
void sceGuTexProjMapMode(int mode);
```

Set texture projection-map mode.

Available modes are:

- GU_POSITION
- GU_UV
- GU_NORMALIZED_NORMAL
- GU_NORMAL

**Parameters:**

- `mode` – Which mode to use

### `sceGuTexScale()`

```c
void sceGuTexScale(float u, float v);
```

Set texture scale.

**Note:** Only used by the 3D T&L pipe, renders ton with GU_TRANSFORM_2D are not affected by this.

**Parameters:**

- `u` – Scalar to multiply U coordinate with
- `v` – Scalar to multiply V coordinate with

### `sceGuTexSlope()`

```c
void sceGuTexSlope(float slope);
```

### `sceGuTexSync()`

```c
void sceGuTexSync();
```

Synchronize rendering pipeline with image upload.

This will stall the rendering pipeline until the current image upload initiated by [sceGuCopyImage()](#scegucopyimage) has completed.

### `sceGuTexWrap()`

```c
void sceGuTexWrap(int u, int v);
```

Set if the texture should repeat or clamp.

Available modes are:

- GU_REPEAT - The texture repeats after crossing the border
- GU_CLAMP - Texture clamps at the border

**Parameters:**

- `u` – Wrap-mode for the U direction
- `v` – Wrap-mode for the V direction

### `sceGuClutLoad()`

```c
void sceGuClutLoad(int num_blocks, const void *cbp);
```

Upload CLUT (Color Lookup Table)

**Note:** Data must be aligned to 1 quad word (16 bytes)

**Parameters:**

- `num_blocks` – How many blocks of 8 entries to upload (32\*8 is 256 colors)
- `cbp` – Pointer to palette (16 byte aligned)

### `sceGuClutMode()`

```c
void sceGuClutMode(unsigned int cpsm, unsigned int shift, unsigned int mask, unsigned int csa);
```

Set current CLUT mode.

Available pixel formats for palettes are:

- GU_PSM_5650
- GU_PSM_5551
- GU_PSM_4444
- GU_PSM_8888

**Note:** Final color index is computed by GE in the following way: `((pixelValue >> shift) & mask) | (csa << 4)`

**Parameters:**

- `cpsm` – Which pixel format to use for the palette
- `shift` – Shifts color index by that many bits to the right
- `mask` – Masks the color index with this bitmask after the shift (0-0xFF)
- `csa` – This value is shifted to the left by 4 bits and bitwise ORed with color index after applying mask

### `sceGuOffset()`

```c
void sceGuOffset(unsigned int x, unsigned int y);
```

Set virtual coordinate offset.

The PSP has a virtual coordinate-space of 4096x4096, this controls where rendering is performed

**Example: Center the virtual coordinate range:**

```c
sceGuOffset(2048-(480/2),2048-(480/2));
```

**Parameters:**

- `x` – Offset (0-4095)
- `y` – Offset (0-4095)

### `sceGuScissor()`

```c
void sceGuScissor(int x, int y, int w, int h);
```

Set what to scissor within the current viewport.

Note that scissoring is only performed if the custom scissoring is enabled (GU_SCISSOR_TEST)

**Parameters:**

- `x` – Left of scissor region
- `y` – Top of scissor region
- `w` – Width of scissor region
- `h` – Height of scissor region

### `sceGuViewport()`

```c
void sceGuViewport(int cx, int cy, int width, int height);
```

Set current viewport.

**Example: Setup a viewport of size (480,272) with origo at (2048,2048):**

```c
sceGuViewport(2048,2048,480,272);
```

**Parameters:**

- `cx` – Center for horizontal viewport
- `cy` – Center for vertical viewport
- `width` – Width of viewport
- `height` – Height of viewport

### `sceGuDrawBezier()`

```c
void sceGuDrawBezier(int vtype, int ucount, int vcount, const void *indices, const void *vertices);
```

Draw bezier surface.

**Parameters:**

- `vtype` – Vertex type, look at [sceGuDrawArray()](#scegudrawarray) for vertex definition
- `ucount` – Number of vertices used in the U direction
- `vcount` – Number of vertices used in the V direction
- `indices` – Pointer to index buffer
- `vertices` – Pointer to vertex buffer

### `sceGuPatchDivide()`

```c
void sceGuPatchDivide(unsigned int ulevel, unsigned int vlevel);
```

Set dividing for patches (beziers and splines)

**Parameters:**

- `ulevel` – Number of division on u direction
- `vlevel` – Number of division on v direction

### `sceGuPatchFrontFace()`

```c
void sceGuPatchFrontFace(unsigned int mode);
```

Set front face for patches (beziers and splines)

**Parameters:**

- `mode` – Desired front face mode (GU_CW | GU_CCW)

### `sceGuPatchPrim()`

```c
void sceGuPatchPrim(int prim);
```

Set primitive for patches (beziers and splines)

**Parameters:**

- `prim` – Desired primitive type (GU_POINTS | GU_LINE_STRIP | GU_TRIANGLE_STRIP)

### `sceGuDrawSpline()`

```c
void sceGuDrawSpline(int vtype, int ucount, int vcount, int uedge, int vedge, const void *indices, const void *vertices);
```

### `sceGuSetMatrix()`

```c
void sceGuSetMatrix(int type, const ScePspFMatrix4 *matrix);
```

Set transform matrices.

Available matrices are:

- GU_PROJECTION - View->Projection matrix
- GU_VIEW - World->View matrix
- GU_MODEL - Model->World matrix
- GU_TEXTURE - Texture matrix

**Parameters:**

- `type` – Which matrix-type to set
- `matrix` – Matrix to load

### `sceGuBoneMatrix()`

```c
void sceGuBoneMatrix(unsigned int index, const ScePspFMatrix4 *matrix);
```

Specify skinning matrix entry.

To enable vertex skinning, pass [GU_WEIGHTS(n)](#gu_weights), where n is between 1-8, and pass available GU_WEIGHT\_??? declaration. This will change the amount of weights passed in the vertex araay, and by setting the skinning, matrices, you will multiply each vertex every weight and vertex passed.

Please see [sceGuDrawArray()](#scegudrawarray) for vertex format information.

**Parameters:**

- `index` – Skinning matrix index (0-7)
- `matrix` – Matrix to set

### `sceGuMorphWeight()`

```c
void sceGuMorphWeight(int index, float weight);
```

Specify morph weight entry.

To enable vertex morphing, pass [GU_VERTICES(n)](#gu_vertices), where n is between 1-8. This will change the amount of vertices passed in the vertex array, and by setting the morph weights for every vertex entry in the array, you can blend between them.

Please see [sceGuDrawArray()](#scegudrawarray) for vertex format information.

**Parameters:**

- `index` – Morph weight index (0-7)
- `weight` – Weight to set

### `sceGuDrawArrayN()`

```c
void sceGuDrawArrayN(int primitive_type, int vertex_type, int vcount, int primcount, const void *indices, const void *vertices);
```

Draw an array of primitives.

**Parameters:**

- `primitive_type` – Type of primitive to draw
- `vertex_type` – Type of vertex to draw
- `vcount` – Number of vertices to draw
- `primcount` – Number of primitives to draw
- `indices` – Pointer to index buffer
- `vertices` – Pointer to vertex buffer

### `guSwapBuffersBehaviour()`

```c
void guSwapBuffersBehaviour(int behaviour);
```

Set how the display should be set.

Available behaviours are:

- PSP_DISPLAY_SETBUF_NEXTHSYNC - Display is swapped on the next hsync
- PSP_DISPLAY_SETBUF_NEXTVSYNC - Display is swapped on the next vsync

Do remember that this swaps the pointers internally, regardless of setting, so be careful to wait until the next vertical blank or use another buffering algorithm (see [guSwapBuffersCallback()](#guswapbufferscallback-1)).

### `guSwapBuffersCallback()`

```c
void guSwapBuffersCallback(GuSwapBuffersCallback callback);
```

Set a buffer swap callback to allow for more advanced buffer methods without hacking the library.

The GuSwapBuffersCallback is defined like this:

```c
void swapBuffersCallback(void** display, void** render);
```

and on entry they contain the variables that are to be set. To change the pointers that will be used, just write the new pointers. Example of a triple-buffering algorithm:

```c
void* doneBuffer;
void swapBuffersCallback(void** display, void** render)
{
 void* active = doneBuffer;
 doneBuffer = *display;
 *display = active;
}
```

**Parameters:**

- `callback` – Callback to access when buffers are swapped. Pass 0 to disable.

### `guGetStaticVramBuffer()`

```c
void * guGetStaticVramBuffer(unsigned int width, unsigned int height, unsigned int psm);
```

Allocate a draw buffer in vram.

Available pixel formats are:

- GU_PSM_5650 - Hicolor, 16-bit
- GU_PSM_5551 - Hicolor, 16-bit
- GU_PSM_4444 - Hicolor, 16-bit
- GU_PSM_8888 - Truecolor, 32-bit

**Parameters:**

- `width` – Width of the buffer, usually 512 (must be a power of 2)
- `height` – Height of the buffer, normally the height of the screen 272
- `psm` – Which pixel format to use

**Returns:** A pointer to the buffer's relative to vram start (as required by sceGuDispBuffer, sceGuDrawBuffer, sceGuDepthBuffer and sceGuDrawBufferList)

### `guGetStaticVramTexture()`

```c
void * guGetStaticVramTexture(unsigned int width, unsigned int height, unsigned int psm);
```

Allocate a texture in vram.

Available texture-formats are:

- GU_PSM_5650 - Hicolor, 16-bit
- GU_PSM_5551 - Hicolor, 16-bit
- GU_PSM_4444 - Hicolor, 16-bit
- GU_PSM_8888 - Truecolor, 32-bit
- GU_PSM_T4 - Indexed, 4-bit (2 pixels per byte)
- GU_PSM_T8 - Indexed, 8-bit

**Parameters:**

- `width` – Width of the texture (must be a power of 2)
- `height` – Height of the texture (must be a power of 2)
- `psm` – Which pixel format to use

**Returns:** A pointer to the texture

### `guGetDisplayState()`

```c
int guGetDisplayState();
```

Get state of display.

Available states are:

- GU_TRUE (1) - Display is turned on
- GU_FALSE (0) - Display is turned off

**Returns:** State of the display

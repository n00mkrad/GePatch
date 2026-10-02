# How GePatch Works

GePatch is a kernel plugin for Adrenaline that makes PSP games render at 960x544 (the PS Vita's native resolution) instead of 480x272. It does this without touching game code: it intercepts the display lists that games submit to the PSP's graphics engine (GE), rewrites the resolution-dependent commands and vertex data in place, and redirects all rendering into a single 960x544 buffer that Adrenaline then shows on screen.

## Overview

A PSP game draws by building a display list - an array of 32-bit GE commands - and submitting it with `sceGeListEnQueue`. Each command has an 8-bit opcode in the top byte and 24 bits of data. The commands set state (framebuffer address and stride, viewport, scissor, texture addresses, vertex format) and issue draws (`PRIM`, `BEZIER`, `SPLINE`).

GePatch sits between the game and the GE driver:

```
game -> sceGeListEnQueue -> [GePatch walks + rewrites list] -> real GE driver -> GE renders at 960x544 into VRAM
game -> sceDisplaySetFrameBuf -> [GePatch copies VRAM result to display buffer] -> Adrenaline presents it
```

The plugin is made up of three source files:

| File | Purpose |
|---|---|
| `main.c` | Hooks, display list walker and all patching logic |
| `gu.c` | Minimal reimplementation of a few `sceGu*` functions, used to build the plugin's own small display list |
| `ge_constants.h` | GE opcode and vertex type constants |

## Startup

`module_start` first reads the controller. If L is held, the plugin returns without installing anything, which allows a game to be started unpatched.

Otherwise it resolves the following driver functions by NID with `sctrlHENFindFunction` and replaces their syscall entries with `sctrlHENPatchSyscall`:

| Function | Replacement behavior |
|---|---|
| `sceGeEdramGetAddr` | Returns the fake VRAM address `0x0A000000` |
| `sceGeEdramGetSize` | Returns 4 MB |
| `sceGeListEnQueue` | Copies the previous frame if needed, resets state, patches the list, then enqueues it |
| `sceGeListEnQueueHead` | Resets state, patches the list, then enqueues it |
| `sceGeListUpdateStallAddr` | Patches the newly appended part of a list before moving the stall address |
| `sceDisplaySetFrameBuf` | Copies the rendered frame to the display buffer before the flip |

Because only syscalls are patched, calls from games (user mode) are intercepted, while the plugin itself can still call the original functions.

## Memory Layout

The real PSP VRAM is 2 MB at `0x04000000`, which is too small for 960x544 color and depth buffers alongside the game's own data. GePatch therefore gives the game a fake VRAM in main RAM and takes over the real VRAM for itself.

| Address | Size | Use |
|---|---|---|
| `0x04000000` | ~1 MB | Real VRAM: 960x544 RGB565 color buffer that all game rendering is redirected to |
| `0x04100000` | ~1 MB | Real VRAM: 960x544 depth buffer |
| `0x041FF000` | small | Real VRAM: dummy target for framebuffers that are ignored (see below) |
| `0x0A000000` | 4 MB | Fake VRAM reported to the game. Game framebuffers and textures "in VRAM" actually live here |
| `0x0A400000` | ~1 MB | Display buffer: the final 960x544 frame that Adrenaline presents |
| `0x0A800000` | small | Plugin's own display list for the frame copy |
| `0xABCDEF00` | 4 bytes | Flag written on every frame copy to signal native-resolution output to Adrenaline |

Since the fake VRAM is twice the size of the real VRAM, games also have more room for textures.

## Display List Walking

`patchGeList` interprets a display list in software, starting at the submitted address and stopping at the stall address or at a `FINISH` + `END` pair. It does not execute anything on the GE; it only follows the list the same way the GE would, so it can find and rewrite every relevant command.

It tracks the state needed to compute addresses (`BASE`, `OFFSETADDR`, `ORIGIN`) and follows control flow:

- `CALL` pushes the return position onto a 64-entry stack and jumps; `RET` pops it. Calls into small subroutines that only upload bone matrices are skipped.
- `JUMP` and `BJUMP` are always taken (the condition of a conditional jump cannot be known ahead of time).
- `SIGNAL` + `END` pairs are handled for the sync, jump, call and return signal behaviors.

The value of every opcode is also recorded in `state.ge_cmd`, so later commands can check the current GE state (for example, whether texturing is enabled).

Lists are not always submitted complete. Many games enqueue a list with a stall address and keep appending commands, moving the stall address forward with `sceGeListUpdateStallAddr`. The hook asks the driver for the list's current position via `sceGeGetList` and patches only the range between the previous stall address and the new one, keeping the walker state from earlier segments.

After patching, the data cache is written back so the GE (which reads memory directly) sees the modified commands and vertices.

## Command Patching

The following commands are rewritten in place:

| Command | Rewritten to |
|---|---|
| `FRAMEBUFPTR`, `FRAMEBUFWIDTH` | The real VRAM color buffer at `0x04000000`. A stride of 512 is changed to 960 |
| `FRAMEBUFPIXFORMAT` | RGB565 |
| `ZBUFPTR`, `ZBUFWIDTH` | The real VRAM depth buffer at `0x04100000` with a stride of 960 |
| `VIEWPORTXSCALE`, `VIEWPORTYSCALE` | ±480 and ±272 (half of 960x544), keeping the original sign |
| `VIEWPORTXCENTER`, `VIEWPORTYCENTER` | 2048 |
| `OFFSETX`, `OFFSETY` | `2048 - 480` and `2048 - 272` |
| `REGION2`, `SCISSOR2` | Full 960x544 area |

The viewport changes are enough to make transformed 3D geometry fill the larger buffer, since the GE maps clip space to screen coordinates using these values. Games may render to several framebuffers, but all of them are redirected to the same 960x544 buffer.

### Ignored Framebuffers and Textures

Every framebuffer address the game sets is recorded (up to 16). This is used for two heuristics that skip draws which cannot work at the higher resolution:

- A framebuffer with a stride other than 512 or 960 is usually an offscreen render target (for example a small buffer for effects). Its width command is replaced with a stride of 0 at the dummy address `0x041FF000`, and all draws while it is bound are replaced with NOPs.
- When a texture address points into a recorded framebuffer other than the current one, the game is sampling an earlier render target (render-to-texture). That framebuffer was never rendered at the address the game expects, so textured draws using it are replaced with NOPs.

These heuristics are the main reason some games lose effects, show black screens or miss cutscenes.

## Vertex Patching

3D vertices are transformed by the GE and scaled through the viewport, so they need no changes. 2D "through mode" vertices, however, carry final screen coordinates and bypass the viewport. For each `PRIM` draw in through mode, GePatch edits the X and Y position of each vertex in memory:

- 480 or 960 becomes 960, and 272 or 544 becomes 544 (full-screen edges).
- Any other value between -2048 and 2048 is doubled.

The vertex format from `VERTEXTYPE` is decoded by `getVertexInfo` to get the vertex size and position offset. For indexed draws, the index buffer is scanned to find which range of vertices is used. After each draw, the vertex or index pointer is advanced the same way the GE would, so following draws without a new address read the right data. `BEZIER`, `SPLINE` and `BOUNDINGBOX` only advance the pointer.

Since vertex data is modified in memory and games often reuse it, the same vertices could be doubled again in a later frame. To prevent this, GePatch looks for unused padding bytes in the vertex format (`visit_off`) and stores the bytes of the first patched coordinate there, spread over the first few vertices. When the same vertices are seen again and these bytes match, the draw is skipped. Vertex formats without padding cannot be marked this way.

## Presenting the Frame

The final image is in real VRAM at 960x544, but the game's display calls still refer to 480x272 buffers in fake VRAM. `copyFrameBuffer` handles this:

1. It writes `1` to the `0xABCDEF00` flag.
2. It builds a short display list at `0x0A800000` using the functions in `gu.c`, containing a single block transfer (`sceGuCopyImage`) from the VRAM color buffer to the display buffer at `0x0A400000`.
3. It enqueues that list with the original `sceGeListEnQueue`, so the copy runs on the GE after the game's rendering.

The copy is triggered on every `sceDisplaySetFrameBuf` call, and also when a new list is enqueued after a list that contained draws. The game's `sceDisplaySetFrameBuf` call is then passed through unchanged.

## Limitations

The approach depends on heuristics that work for many, but not all, games:

- Render-to-texture effects are dropped rather than upscaled.
- Through-mode vertex doubling is based on value ranges, so 2D coordinates that are not screen positions can be distorted, and data reused in ways the marker does not catch can be doubled twice.
- Display lists are modified in place, so a game that reuses a list keeps the NOPs from a previous pass.
- Anything drawn directly into the framebuffer by the CPU (including some plugins' on-screen output) is not visible, as the displayed image comes from the redirected buffer.

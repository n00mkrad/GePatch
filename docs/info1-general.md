# PSP rendering hand-off: initialization and presentation

## Instructions

Keep this step's instructions, open questions, and answers/findings in this document. Do not create a separate findings document for this step. Broader storage-ownership, renderer-lifetime, and effect questions belong in [handoff2-buffer-ownership.md](handoff2-buffer-ownership.md).

Preserve every research question after it is answered. Move the original question unchanged from `Open questions` to `Answers and findings`, together with its answer and supporting evidence; never delete or replace the question with an answer-only summary. Keep partially answered or blocked questions in `Open questions` with their current evidence and remaining checks. The `Answers and findings` list was empty when this handoff was created and is populated as questions are answered.

Keep the scope finite: verify initialization, the first valid displayed image, and representative consecutive presentations. Record game-visible addresses, strides, formats, translation settings, and justified address envelopes; do not reverse-engineer the physical eDRAM transform or chase whole-pipeline ownership to complete this step. Move out-of-scope questions with their existing evidence to the follow-up document and leave a link here. Consolidate new evidence into the existing answer instead of appending repeated investigation summaries.

### Q: What is this session responsible for?

A: Research and document the framebuffer setup and presentation path of Silent Hill: Origins on PSP. Establish initialization and presentation before investigating individual offscreen effects.

Trace `0x0017B440`, `0x0017DC2C`, the recorded presentation lists, `0x0017EFCC`, and the display thread at `0x0017F0B8`. Always use `GHIDRA-WRAPPER-NOTES.md` for binary tracing. Follow their immediate callers, buffer setup helpers, and synchronization code only as needed to explain the path end to end.

The result should answer where the baseline buffers live, how they are laid out, which image is actually displayed, and how completed scene rendering becomes safe scanout. This is a research/documentation task, not a request to patch the game, change PPSSPP, or implement rendering in Unity.

### Q: What approach should I use?

A: Use existing reverse engineering to build a provisional memory map, verify the relevant code in the binary, then corroborate the effective bindings and presentation behavior with PPSSPP if a research instance is available.

Keep three kinds of evidence distinct: prior claims, independently verified binary behavior, and observed runtime behavior. A current factbook claim is a starting point, not proof. If runtime access is unavailable, complete the static investigation and explicitly identify the remaining runtime checks.

Do not start by treating PPSSPP's framebuffer inventory or host GPU resources as the game's resource model. Document PSP memory and its views first.

### Q: What should I read before tracing?

A: Read the repository instructions and these references, narrowing to the relevant sections rather than loading unrelated dossiers:

- `GHIDRA-WRAPPER-NOTES.md`: required for all binary tracing.
- `GHIDRA-NOTES.md`: maintained Allegrex project, address conversions, relocation caveats, and parallel-safe project access.
- `docs/re/AGENT.md`: atlas evidence and editing rules, if using or updating atlas material.
- `docs/re/tools/factbook.md`: claim lifecycle, binary scoping, and address conventions.
- `docs/PSP-GE-research.md`: framebuffer/depth/texture command state, address formation, synchronization, and alpha/stencil storage.
- `src/tools/ppsspp/ge_dump.md`: capture procedure and parser limitations.

Read current factbook entries in the contexts `Retail buffer swap trace` and `GE dithering cheat research`. Also inspect framebuffer/depth/context entries in `Inventory item preview transform research`, including their corrected addresses. Review full-word, case-sensitive `GE` matches in the ledger for additional relevant pointers; do not limit the investigation to those matches, since several presentation claims do not contain that word.

`docs/re/tools/factbook.md` is the guide; `docs/re/factbook.tsv` contains the entries. Use claim status and the selected binary identity, not file order alone, to choose evidence.

### Q: Which functions are the primary anchors?

A: The following are existing interpretations to verify, not newly established findings:

| Image address | Starting interpretation | Factbook anchor |
| --- | --- | --- |
| `0x0017AF5C` / `0x0017ADA8` | Device-start dispatch and one-time setup | `FB001271` |
| `0x0017B440` | Initializes the fixed scene draw buffer and display dimensions | `FB001272` |
| `0x0017FE9C` | Initializes GE context, callbacks, display pool, and display thread | `FB001276` |
| `0x0017DC2C` | Creates two RGB565 display entries in an interleaved stride-1024 layout | `FB000161` |
| `0x0017FFF4` | Builds each entry's reusable presentation list during initialization | `FB001287` |
| `0x0017EFCC` | Selects a reusable display entry, emits a GE CALL, updates its stamp | `FB001277` |
| `0x0017F0B8` | Vblank thread selecting a display entry through `sceDisplaySetFrameBuf` | `FB001278` |
| `0x0017D7CC` | Presentation orchestration: finish/sync, start list, select display entry | `FB001286` |
| `0x0017F830` / `0x0017F7A8` | Persistent GU draw-buffer setup / current GE target binding | `FB001273` / `FB000160` |
| `0x0017EC74` | Emits BASE and CALL for a recorded list | `FB001282` |

Also inspect `0x0017F918` for display setup, `0x0017F96C` for depth binding, and `0x0017F1CC` / `0x0017F3E4` for list start/finish when needed. Verify names and argument interpretation from the implementation and emitted commands.

### Q: What is already suspected about the memory layout?

A: Seed the investigation with these claims, then recover exact extents and views:

- Scene target: RGBA8888 at VRAM offset `0x4C000`, ordinarily absolute address `0x0404C000`, stride 512 pixels, with a 480x272 scene/display area.
- Display pool: two RGB565 images interleaved in a shared stride-1024 eDRAM surface. Exact bases, row ranges, padding, and allocation extent still need to be established here.
- Shared depth: the earlier render-state claim reports ZBP offset 0 and ZBW 512; confirm the actual setup and storage extent rather than assuming conventional double-buffer allocation.
- Presentation: a recorded list blits the 8888 scene into the selected 5650 display image using 15 textured sprites with dithering, then restores the scene target.

Useful relocated image-address globals are `0x00587A38` (GU context), `0x00587A44` (VRAM base), `0x00587A60` (persistent scene draw-buffer offset), `0x00587A68` / `0x00587A6C` (cached depth pointer/stride), and `0x00587A88` (cached frame format).

The display-pool globals are `0x00587B58` (entry count), `0x00587B5C` (displayed stamp), `0x00587B60` (frame counter), and `0x00587B64` (entry-array pointer). Existing evidence describes 0x24-byte entries. Recover their fields from accesses rather than inventing a complete struct.

### Q: What known traps or conflicting claims need attention?

A: `FB000159` is superseded by `FB001287`. `0x0017FFF4` is an init-time list builder, not a CPU helper called on every frame. Its recorded commands execute later through GE CALL. A CPU breakpoint only on the builder will miss steady-state presentation.

`FB000016` still describes four render-state initialization call sites, whereas the newer `FB001272` says `0x0017B440` has only the device-start caller. Resolve this discrepancy against current binary evidence; do not silently combine the two claims.

The persistent GU draw-buffer field is not necessarily the current GE render target. Offscreen binds can change effective framebuffer state without changing the fixed scene pointer used by presentation.

Older `.bss` aliases, such as `0x000873B0` for the GU context, were rejected and replaced with relocated image addresses. Do not reuse them as valid memory locations.

### Q: How should I begin the static trace?

A: Follow `GHIDRA-WRAPPER-NOTES.md` for all binary tracing. Use that guide directly for query commands and project-access instructions.

Inspect signatures, callers, and data references first. Select individual bodies and bounded assembly slices where they answer a question, especially selection predicates, argument construction, delay slots, and synchronization order. Preserve enough surrounding logic to verify signedness and comparison behavior.

Reconstruct the actual initialization call order, then the ordinary presentation call order. Recover display-entry fields, how reusable lists are allocated and addressed, which commands they contain, and whether their contents are later rewritten. Distinguish initialization clears/copies from steady-state conversion.

For each shared global, inspect relevant writers as well as readers. A lack of direct references is not proof that indirect access or recorded GE execution cannot affect the underlying memory.

### Q: How do I handle addresses correctly?

A: Record image addresses, CPU runtime addresses, VRAM offsets, and absolute GE memory addresses in separate fields.

Ghidra queries use zero-based image addresses. For the documented PSP image, CPU runtime addresses are image addresses plus `0x08804000`; verify the loaded module base before placing runtime breakpoints. This conversion does not apply to VRAM offsets.

Unrelocated segment-1 references in Ghidra need the documented `0x00500688` correction before CPU runtime conversion. The wrapper helps translate these references. Avoid both omitting the correction and applying it twice to already corrected globals.

Keep raw cached/uncached pointers alongside canonical storage addresses. Decode split GE pointer/stride commands correctly; do not interpret each command operand as an independent flat address. Follow the documented raw-file mapping only if a raw-file read is actually necessary.

### Q: How should I handle incomplete evidence?

A: Address each research question explicitly, using UNKNOWN where evidence is incomplete. Keep unresolved questions in `Open questions`; do not move them to the answered list merely because the current session cannot investigate further.

Do not equate a timestamp written by the CPU with completed GPU work. Likewise, a bound depth pointer does not mean a presentation sprite actually tests or writes depth.

### Q: What runtime evidence should I collect?

A: Ask the user to provide a PPSSPP debugger instance. Coordinate before pausing, resuming, restarting, or installing breakpoints in a shared instance. Do not replace a user's running state or restart from boot without agreement.

If runtime work is available, record game/build identity, module base, emulator version/backend, relevant graphics settings and active cheats, and the capture scenario. Keep native PSP dimensions separate from host upscaling. Reuse the established local debugger tooling instead of guessing endpoints or event capabilities.

For initialization, capture buffer setup and the resulting display entries if a fresh boot is available. For ordinary gameplay, observe several consecutive presentations: entry selected, stamp/counter values, recorded-list execution and effective source/destination bindings, completion boundary, and actual display API arguments. Correlate CPU observations with GE execution; a GE frame dump alone does not document the display thread.

`src/tools/ppsspp/ge_dump.md` documents `gpu.record.dump` and the need to resume the CPU after that request pauses it. Resume only as part of the coordinated capture, not an unrelated paused session.

The parser snapshots state at PRIM, but its CLI `--state` reports only the first selected draw. Inspect selected draws individually or use the existing replay data through a narrowly scoped analysis helper if necessary. Confirm dump-version compatibility and what the recording preserves. A missing initialization event, CALL boundary, or display API event in a dump is not proof that it never occurred.

Retain inherited initial state. Inspect the list's final restoration commands as well as its draw snapshots. Do not infer allocation height from texture size, scissor, or a host framebuffer's inferred dimensions.

### Q: What is outside this session's scope?

A: Do not expand into bloom, shadow-map generation, preview rendering, loading effects, a complete frame graph, renderer shutdown/reinitialization, whole-camera clear policy, scratch-view ownership, or physical eDRAM translation internals. Record any relevant boundary or overlap here, but move further questions and supporting evidence to [handoff2-buffer-ownership.md](handoff2-buffer-ownership.md).

### Q: What does a useful result look like?

A: Use this structure, replacing placeholders only with supported answers:

```text
Baseline views
  scene: address, format, stride, dimensions, extent, lifetime
  depth: address, 16-bit layout, stride, extent, sharing
  display entry 0/1: bases, interleaving, RGB565 layout, scanout

Initialization
  device start -> buffer/context setup -> recorded copy lists -> display thread
  Actual order and synchronization: <verified sequence>

Presentation
  producer selects reusable entry -> GE executes conversion list
  completion/ordering boundary: <verified mechanism>
  display thread selects entry -> display switch takes effect

Evidence and limits
  <binary locations, fact IDs, capture references, unresolved checks>
```

### Q: When is the first step complete?

A: The baseline game-visible memory/view map and presentation mechanism are documented with traceable evidence, including the reusable-list distinction, initial-image validity, and buffer-reuse/completion rules. Resolve code-level questions by static tracing first; use a coordinated boot/presentation capture to validate the three remaining open questions and the answered first-image path. Document limitations if capture capabilities cannot establish a particular boundary. Deferred physical-storage, whole-renderer lifetime, and effect-ownership questions do not block completion. If runtime access is blocked, deliver the static findings and this bounded runtime checklist rather than declaring the whole path runtime-verified. Do not expand the checklist into an exhaustive audit of every scene or device mode.

End with a concise summary of established facts, corrected interpretations, remaining blockers, and the next buffer-related investigation this foundation enables. Follow the user's required action/assumption tables in the session's final response.

## Established / Unresolved / Next check

Established (static): the mode-0 scene is RGBA8888 at offset `0x4C000`; two RGB565 display views at `0xD4000` and `0xD43C0` share stride-1024 rows. Init-time recorded lists later convert the completed scene through GE CALL before retained scene rendering. Initialization has one recorded caller, not four; cached depth can diverge from the emitted depth binding. Before two early presentation pumps, the successful splash-load path CPU-writes the 480x272 splash into the scene with alpha `0xFF`; it does not depend on a first camera clear.

Established (PPSSPP, one zone per shipped zone render mode): device mode 0, `B=0x04000000`, translation `0x1000`, and the effective scene/depth/display bindings match the static map. The conversion is the first draw of each frame and inherits no masks, fog, colour test, logic op, alpha/stencil test, or depth test, with the default dither matrix. The display thread requested the newly stamped entry before the GE FINISH callback of the list converting into it in 62% of observed presentations. See "Runtime observations" below.

Established (PPSSPP fresh boot, software renderer): the splash is CPU-copied into the scene exactly, the display surface is still empty before the first presentation, and the two early presentations convert it into both RGB565 views, with entry 1 last requested.

Not established, and not measurable in PPSSPP: hardware conversion-to-scanout latency and firmware latch timing. Physical depth storage and further scratch/effect ownership remain in [handoff2-buffer-ownership.md](handoff2-buffer-ownership.md). This step's questions are answered below.

## Open questions

None remain within this step. Hardware display timing would need PSP hardware; it is recorded as a limit in the completion answer.

## Answers and findings

### Runtime observations

Capture identity: PPSSPP `v1.20.4-1414-g38ed1be64b` (user build with extended debugging and shadow-mapping changes), D3D11, 1x, 60 FPS, no cheats, WebSocket debugger. Game `ULUS10285` 1.00 from `build/SHO_PSP_bootmenu_v2.iso`; its runtime code in `0x0017A000..0x00188000`, `0x000D7800..0x000D8700`, `0x000F0400..0x000F0E80`, and `0x0007B400..0x0007CA00` equals retail `BOOT.BIN` except for relocation-shaped words. Active module `SilentHillOrigins` at `0x08804000`, confirming the image-to-runtime conversion. Scenario: zone `HO_2_ElevatorHallway` (zone render mode 2), torch on, ordinary gameplay. Zone render mode (CZone attribute 9, see `docs/zone-render-modes.md`) is distinct from the device mode at `0x00589488` and from FX worker modes.

Memory reads while running: device mode 0; `B=0x04000000`; scene offset `0x4C000`; cached depth 0/512 (the initialization-time `0xD4000` divergence was already repaired); entry count 2. Entry 0: view `0x040D43C0`, stride 1024, format 0, list `0x08E505C0`, raw allocation `0x08E50590`. Entry 1: view `0x040D4000`, list and raw allocation `0x08E52400`. The cached framebuffer format `0x00587A88` read 0 although the effective scene format is 8888; the dump below shows several 565 binds earlier in the frame, so this cache is not effective state.

GE dump `G:\Emulation\PPSSPP\memstick\PSP\SYSTEM\DUMP\handoff1-20261002-ho2-elevatorhallway-d3d11.ppdmp` (version 6, 224 draws; `ge_dump.py --timeline`). Its translation record is `0x1000`. Its display records show entry 0 at the start and entry 1 at the end of the frame. Draw 0 is the conversion: framebuffer `0x040D4000`, stride 1024, 5650, texture `0x0404C000` stride 512 8888, 30 sprite vertices covering x 0..480, y 0..272, depth bound at 0/512 with depth test off. Scene draws use framebuffer `0x0404C000` stride 512 8888 and depth 0/512. The full-scene camera clear is draw 41, after effect passes that reuse scene storage; see handoff 2.

Further GE dumps under the same settings, each in ordinary gameplay: `handoff1-20261002-ho1-lobby-d3d11.ppdmp` (`HO_1_Lobby`, zone render mode 0), `handoff1-20261002-introroad-d3d11.ppdmp` (`IntroRoad`, mode 3, torch on), and `handoff1-20261002-dh1-hallway-d3d11.ppdmp` (`DH_1_Hallway`, mode 4, bloom enabled). Each begins with the same conversion draw and ends with a display record for the entry it converted into.

- What are the presentation-list source and destination rectangles, texture layout, filtering, dithering, write masks, and relevant alpha/stencil behavior?

Answered. "Recorded conversion list" below gives the exact geometry and explicitly emitted state. In all four shipped zone render modes, the captured conversion draw inherits pixel masks `0x000000` (all channels written), fog, colour test, logic op, alpha test, stencil test, and depth test all disabled, region `(0,0)..(1023,1023)`, clamp wrap, and the default dither matrix, so it fully overwrites the 480x272 RGB of the selected entry. Across the four zones, the inherited state differs only in fog colour and range, CLUT address, and colour-test function, none of which is active for the conversion. Vertices (x 0..480, y 0..272) and UVs match the static trace. This covers ordinary gameplay frames; effects that end a frame with other state (menus, movies, transitions) were not captured.

Fresh boot, software renderer, emulation slowed to 20%: a pausing breakpoint at runtime `0x088DBB34` (image `0x000D7B34`, after the splash copy and before the first presentation call) hit on the second of two resets; PPSSPP log-only events from that boot were lost to its log stream re-sending older lines. At that stop, D=0, C=1, both entry stamps -1, and the entry lists were reallocated at `0x08E585C0`/`0x08E5A400`. All 130560 visible scene pixels equalled a PIL decode of the unsuffixed `splash272.jpg` (mean absolute difference 0.00) with alpha `0xFF`, the 32 padding pixels per row were zero, and the whole `[0x040D4000,0x0415C000)` display surface was zero. A later manual break while the splash was on screen read D=2, C=3, entry 0 stamp 1, entry 1 stamp 2: both early presentations ran, entry 1 was the last requested, and no further presentation had run. Both views decoded to the splash within RGB565 quantization and dither (mean absolute difference 2.19 per channel); the 64 padding pixels per shared row stayed zero. The user's framebuffer viewer listed both 480x272 stride-1024 565 views with identical splash previews.

- What establishes completion between GE writes and display use? Separate CPU stamp updates, GE completion, list ordering, callback/semaphore behavior, and vblank timing.

Answered: nothing establishes it. The preceding direct work is completed through blocking `sceGeDrawSync(0)`, and GE list order protects scene-source consumption before the next scene rendering. The display thread has no completion wait, and the CPU stamp is published before the direct list's stall release; the SIGNAL semaphore and FINISH callback do not gate selection. At runtime the display thread requested the new entry before the list's FINISH callback in most frames (counts below). This is a missing safety proof, not an observed tear or demonstrated defect.

The reuse rule protects every requested entry, including the first deferred request. The producer reuses only an entry whose stamp is below D, and D only rises when the display thread requests a newer entry. So an entry becomes writable only after a later request has replaced it, and after the first request every later one is immediate. The first deferred request therefore cannot still be the latest request when its entry is overwritten. This is derived from the verified predicates in "Producer selection and reuse" and "Display-thread selection"; it assumes that a later immediate request supersedes a pending deferred one, as the PSP API contract describes. The boot capture is consistent with it: after the two early presentations, entry 0 (stamp 1) was below D=2 and therefore reusable, while entry 1 was the latest request. Limit: PPSSPP's GE and display timing is approximate, so hardware conversion-to-scanout latency and latch timing are not established.

Presentation ordering, from `src/tools/ppsspp/sho_present_trace.py` (log-only breakpoints, three runs, 31 + 126 + 130 consecutive presentations, contiguous stamps): every presentation runs `DrawSync(0)`, enqueue with initial stall, entry stamp, FINISH emission, and stall release, in that order. Stamps alternated strictly between the entries, the producer never waited in selection, and each new entry was requested once with sync 0. The display thread requested the new entry before the list's FINISH callback in 179 of 285 presentations and after it in 106. About 5% of display-thread vblank waits found no newer stamp. Host timestamps are not emulated time; only ordering is used. PPSSPP's log stream re-sends earlier lines after a few seconds, so the script discards events from the first backwards timestamp.

- What are each view's base address, format, pixel stride, byte stride, logical dimensions, and backed or reserved extent?

Answered for device mode 0 by the baseline view table below and confirmed at runtime: the observed `B`, translation value, framebuffer/depth bindings, and display requests match it. The setup uses fixed VRAM addresses, not three allocator-returned VRAM blocks. Backed/reserved extent is not established by this step: independently reserved boundaries and the physical depth transform are deferred to [handoff2-buffer-ownership.md](handoff2-buffer-ownership.md), which also records runtime scratch reuse of scene and depth address space. Do not derive scene allocation height from its 512x512 texture declaration.

### Evidence scope and address conventions

Static investigation completed on 2026-10-02 using `docs/re/tools/ghidra_query.py` against the maintained Allegrex analysis's existing read-only snapshot:

```text
ghidra_tmp/wrapper/allegrex/20260923T094309Z-24c1b263d2ae40f0b132ef9aa5bd30e0/BOOT.BIN_allegrex_ghidra/
program: BOOT.BIN; Allegrex:LE:32:default; image base 0; 7351 functions
binary identity reported by wrapper:
0803dbfc05cdf9e46530e1dcc42d2e2430eee5ffa2f23ffe02abc1c8f5fe7006
project classification: UNCHANGED
```

The snapshot was reused, not refreshed; canonical analysis may have changed since its creation. No canonical or copied Ghidra annotations were edited. Decompilation was checked against bounded/full assembly for argument construction, delay slots, signed predicates, and ordering. Raw-reference queries corroborated selected global writers, but do not prove whole-program completeness or exclude computed/indirect writes.

Evidence labels used here: "prior claim" means an existing factbook entry; "static" means independently queried binary behavior; "derived" means arithmetic or a consequence of that behavior plus the documented GE command model; "observed" means a PPSSPP capture recorded under "Runtime observations".

All function/instruction references below are zero-based image addresses. Corrected segment-1 globals already include `0x00500688`; never add it again. CPU runtime conversion is `image + 0x08804000`, observed as the module base in PPSSPP. VRAM offsets do not receive that conversion. The binary obtains the eDRAM base `B` with the import at `0x001D6670` and stores it at `0x00587A44`; PPSSPP returned `0x04000000`.

The scene map below is for device mode 0 at `0x00589488`. `0x0017AF5C` case 0 initializes that mode to 0, but case 7 / `0x0017AE44` can select other modes before start. `0x0017B440` selects RGBA8888 and offset `0x4C000` only for mode 0; other branches choose other formats and offset 0. The reusable conversion lists nevertheless hardcode their 8888 source at `0x0404C000`. Do not generalize the mode-0 map to every selectable mode without runtime evidence. [Static: `0x0017AF5C`, `0x0017AE44`, `0x0017B604..0x0017B684`, `0x0017B8B4..0x0017B90C`, `0x0018019C..0x001801B8`; prior anchors `FB001271`, `FB001272`, `FB001287`.]

### Baseline buffer/view table

All intervals are half-open. "Pitch envelope" includes row padding and is derived from the logical row count, not proof of an allocator reservation. Display active bytes are interleaved; overlapping view envelopes do not mean overlapping visible pixels.

| View | VRAM offset / expected canonical address | Format | Pixel / byte stride | Logical area | Address envelope and storage qualification | Role |
| --- | --- | --- | --- | --- | --- | --- |
| Fixed scene, mode 0 | `0x4C000` / `0x0404C000` | RGBA8888, 4 bytes/pixel | 512 / `0x800` | 480x272 | 272-row pitch envelope `[0x4C000,0xD4000)`, `0x88000` bytes; last visible row ends at `0xD3F80`; independent reserved extent UNKNOWN | Scene target and conversion texture source; not passed to scanout by this path |
| Shared depth, explicit GE view | ZBP operand 0 / expected eDRAM view at `0x04000000` | 16-bit depth; no separate format register | 512 / `0x400` | Baseline scene rectangle 480x272 | Linear 272-row envelope would be `[0,0x44000)`, `0x44000` bytes; physical translation/backing/reservation UNKNOWN | Scene depth only; not a displayed colour image |
| Display entry 0 | `0xD43C0` / `0x040D43C0` | RGB565 (`5650`, format 0), 2 bytes/pixel | 1024 / `0x800` | 480x272 | Visible-row hull `[0xD43C0,0x15BF80)`; shares `[0xD4000,0x15C000)` with entry 1 | Conversion destination; directly supplied to display API |
| Display entry 1 | `0xD4000` / `0x040D4000` | RGB565 (`5650`, format 0), 2 bytes/pixel | 1024 / `0x800` | 480x272 | Visible-row hull `[0xD4000,0x15BBC0)`; shared 272-row pitch envelope is `0x88000` bytes total, not twice that | Conversion destination; directly supplied to display API |
| Presentation texture declaration | `0x4C000` / `0x0404C000` | Linear, unswizzled RGBA8888; level 0 only | 512 / `0x800` | Declared 512x512; sampled rectangle 480x272 | Declaration's nominal span `[0x4C000,0x14C000)` overlaps display storage, but the recorded source coordinates do not sample those extra rows | A view of scene memory, not a separately allocated texture |

Evidence: `0x0017B8C0..0x0017B90C`, `0x0017F830`, `0x0017F918`, `0x0017F96C`, `0x0017DCD4..0x0017DD0C`, `0x00180030..0x00180070`, `0x0018019C..0x001801B8`; prior `FB000022`, `FB000160`, `FB000161`, `FB001272..FB001275`, `FB001287`. The pixel-pipeline model and split pointer/stride encoding are from the local GE reference, not PPSSPP host framebuffer inventory.

```text
VRAM offsets, mode-0 linear address-space map (not translated-depth allocation proof)

000000 +---------------------------------------+
       | depth view: hypothetical linear rows  |
044000 +---------------------------------------+
       | 08000-byte gap in this linear map     | ownership UNKNOWN
04C000 +---------------------------------------+
       | scene: 272 rows, 0800 bytes/row        |
       | each row: 480 RGBA pixels | 32 pad     |
0D4000 +---------------------------------------+
       | shared RGB565 display surface         |
       | 272 rows, 0800 bytes/row               |
       | [entry 1: 480][entry 0: 480][pad: 64] |
15C000 +---------------------------------------+
       | remaining baseline ownership UNKNOWN  |
200000 +---------------------------------------+ expected 2 MiB boundary

The 512x512 scene texture declaration extends to 14C000.
Its rows beyond the actual source rectangle are not proof of scene backing.
The cached depth pointer can transiently equal D4000 without a GE depth rebind.
```

Important cache distinction: explicit `sceGuDepthBuffer(0,512)` emits `0x9E000000`, `0x9F000200` and caches 0/512. Later `0x0017F830` treats cached pointer 0 as unset and writes `0x4C000 + 272*512*4 = 0xD4000` to `0x00587A68`, without emitting another ZBP/ZBW pair. Thus the setup's cached depth pointer no longer mirrors effective GE depth state, and it numerically coincides with the display pool base. This is not evidence of GE depth writes into display storage. The baseline restore at `0x001873E0` explicitly rebinds depth 0/512. [Static: `0x0017B624/0x0017B650/0x0017B668/0x0017B680`, `0x0017F86C..0x0017F8A8`, `0x0017F9C4..0x0017F9CC`, `0x001873BC..0x001873E4`; qualifies the unconditional "mirroring" wording of `FB000901`.]

Mode 0 additionally calls the GE import at `0x001D6680` with `0x1000`; nonzero modes pass `0x800`. Its NID is `0xB77905EA`, the eDRAM-address-translation API. The local GE reference explicitly leaves the physical transform incompletely specified. The diagram therefore does not establish physical depth placement or the ownership of the apparent gap. [Static: `0x0017B8CC..0x0017B8E8`; import descriptor/NID evidence below.]

### Initialization sequence

- What initializes the scene, depth, and display buffers, and in what order?

Static answer: the display pool and its recorded lists are created before the device render-state setup, not after it. Recording a list is not executing its conversion.

```text
0017AF5C device-system case 2
  -> 0017ADA8 device start
       if one-time flag 004F48A8 != 0:
         -> 0017FE9C
              CPU interrupt guard; obtain eDRAM base/size
              -> 0017DB54 reset GU context and pool counters
              create RwPspDLSignal semaphore; register GE callbacks
              enqueue/reset list at 004F4A80; ListSync(id,0); DrawSync(0)
              -> 0017DC2C allocate 2 RAM entries, initialise stamps to -1
                   -> 0017FFF4(entry 0, B+D43C0): record callable conversion
                   -> 0017FFF4(entry 1, B+D4000): record callable conversion
              create/start RwClimaxVBL thread at 0017F0B8
         clear one-time flag
       -> 0017B440 device-state initialization
            start direct initialization list
            choose format; emit depth bind 0/512 in one of four branches
            seed viewport/scissor/render state and cached clear values
            mode 0: set translation width 1000, draw buffer 3/4C000/512
            set display mode/dimensions 480x272 (not display framebuffer)
            finish direct list; DrawSync(0)
            start/finish second direct state list (no local sync afterwards)
       -> 0017D5AC allocate separate scene-command ring; begin context-1 list
       -> remaining device-start helpers (not traced beyond baseline scope)
```

`0x004F48A8` contains initialized value 1. The one-time guarded call is `0x0017ADC4`, followed by clearing the flag at `0x0017ADCC`; `0x0017B440` is called at `0x0017ADD0` outside the guard. Do not describe every future device-start invocation as recreating the pool. Thread creation uses priority `0x10`, stack size `0x400`, and no arguments; it starts at `0x0017FFA4`. Its initial displayed stamp is 0, so it does not select either -1-stamped entry before a producer publishes one. [Static: `0x0017ADA8`, `0x0017FE9C`, `0x0017DB54`, `0x0017DC2C`, `0x0017D5AC`; prior `FB001271`, `FB001276`, `FB001279`.]

`0x0017F918 -> 0x0017F8C4 -> 0x001D6688` sets display mode 0 and 480x272 dimensions. It also stores the same scene offset/stride again in the GU context. `0x0017FE84(1)` at `0x0017B910` only changes the software flag at `0x00587A3C`; its body does not call `sceDisplaySetFrameBuf`. No inspected initialization helper clears the images or executes the recorded conversion list. The pool's zeroing call at `0x0017DC88` covers the 0x48-byte RAM entry array only.

### First-image initialization path

- What image contents are established during initialization and before the first display request?

Static answer: the successful boot path initializes scene color by CPU copying the decoded splash, before camera-director creation and before the two explicit early render/present pumps. Device setup itself initializes metadata/state, not image bytes.

```text
device/RenderWare start succeeds -> 000D88E4 -> 000D7A00
  000D7A20: create main camera through 000DAC88; publish it via 000D81DC
  000D7AC0: 000D7864 resolves splash272.jpg and opens/decodes it
    000D78EC..000D7954: write decoded RGB and FF alpha into B + scene offset
    000D7958..000D7964: repeat the same scene copy, not a second buffer
  000D7B24: register render/preshow messages
  000D7B34 / 000D7B3C: two 000D8644 render pumps
    000D8508 -> 000D84DC -> 000D8478 -> RwCameraShowRaster -> 0017D7CC
      ordinary selection records conversion CALL and publishes its entry stamp
  000D7C2C: create camera director later
```

`0x000D7864` uses the decoded image's width/height and advances destination rows by 512 RGBA pixels. Destination bytes are `(B + sceneOffset) + y*0x800 + x*4`; alpha is explicitly `0xFF`. The extracted retail `splash272.jpg` and all five localized variants in `gamedata/SHO_PSP/PSP_GAME/USRDIR/SH_ARC` have 480x272 dimensions, checked by reading image metadata. Thus those assets populate every visible scene pixel but not the 32 padding pixels per row; depth and RGB565 display bytes are not initialized by this copy. `0x00111D68` creates a 32-bit image and decodes scanlines before returning it. The two-pass loop reloads the same B/offset each time; describing it as CPU initialization of two scene buffers would be incorrect. [Static: `0x000D7864` full assembly, `0x00111D68`, `0x000D7A00`, `0x000D88E4`; asset metadata is corroboration, not an observed loaded resource.]

The render gates at `0x001EC910` and `0x001EC918` are initialized to 1, and the flag-2 override at `0x001EC919` to 0. The camera director and its subscriptions do not exist at the two early calls; the first source therefore does not require the director's later `RwCameraClear`. Each enabled pump reaches the ordinary conversion machinery described below. The first bundle's negative scene-ring gate suppresses the retained scene CALL, while its conversion still reads the already populated fixed scene. This identifies the programmed source of the initial display image, not the exact vblank at which either display entry becomes active. [Static: bytes at `0x001EC910`, `0x000D7B24..0x000D7C30`, `0x000D8508`, `0x000D84DC`, `0x000D8478`, `0x0017D7CC`.]

Runtime validation (see "Runtime observations"): in PPSSPP the splash was copied exactly, and both early presentations converted it into the two RGB565 views. Limits: stream-open or decoded-image failure returns without clearing the scene, and the caller still reaches the early pumps; no initialized-image guarantee is established for that failure branch. `0x000D7864` has no local cache-writeback call and `0x0017D7CC`'s writeback is conditional; PPSSPP does not model the PSP data cache, so the observed visibility does not establish hardware cache behavior. Baseline camera clears after director creation and the bounded teardown/restore findings are in `handoff2-buffer-ownership.md`.

### Display interleaving

- How are the two display views interleaved? Show row-address formulas or a small layout diagram, including padding and any overlaps with other baseline storage.

Derived from verified bases, stride, and sprite vertices, for `0 <= x < 480`, `0 <= y < 272`:

```text
scene(x,y)   = B + 04C000 + y*0800 + x*4
entry1(x,y)  = B + 0D4000 + y*0800 + x*2
entry0(x,y)  = B + 0D4000 + y*0800 + 03C0 + x*2

one shared display row, relative to B+0D4000+y*0800:
0000                         03C0                         0780       0800
| entry 1: 480 RGB565 pixels  | entry 0: 480 RGB565 pixels  | 64 pad  |
```

These are side-by-side views within each row, not alternating whole rows. The builder rounds both render-target bases down to the same 8192-byte-aligned `B+0xD4000`, then implements the entry displacement in destination vertex coordinates. Entry 0 draws at x=480..960, entry 1 at x=0..480; both use y=0..272. `sceDisplaySetFrameBuf` instead receives each unrounded view pointer. The 64 trailing RGB565 pixels per shared row and 32 trailing RGBA8888 scene pixels per row are outside the conversion rectangles. Actual visible scene and display bytes are disjoint; the scene's 272-row pitch envelope ends exactly where the display surface begins. Only the oversized texture declaration and the transient cached-depth value produce the baseline overlaps described above. [Static: `0x00180040..0x00180070`, `0x001800FC..0x0018015C`, `0x00180180`, `0x0017F170..0x0017F19C`; prior `FB000161`, `FB000170`, `FB001287`.]

### Displayed and non-displayed roles

- Which buffers are directly scanned out, indirectly visible, or only used for depth? Does that role change during initialization?

Static answer: the thread supplies only entry 0/1's RGB565 pointers to the display API. The scene is indirectly visible through textured conversion, and the explicit depth view is never supplied as a colour scanout image. Before the first stamped entry, the thread does not request a framebuffer switch. Setting display dimensions or the software display flag does not make the scene an initialization scanout buffer. What the firmware/emulator was showing before the first request is UNKNOWN; no observed boot image is claimed. [Static: `0x0017F0B8`, `0x0017F918`, `0x0017FE84`, `0x0017DB54`, `0x0017DC2C`; prior `FB001278`, `FB001287`.]

### Recorded conversion list

The following establishes the explicitly recorded portion of the source/destination/state answer. At width 480, `N = (480+31)/32 = 15`. The builder allocates `N*N*0x20 + 0x240 = 0x1E60` RAM bytes per entry, stores the raw allocation, aligns the callable list up to 64 bytes, and places the 30 vertices at aligned-list+`0x200` (also 64-byte aligned). Each vertex is 16 bytes: short UV, packed colour, short XYZ, and padding. Only 480 bytes of vertices are initialized for the 15 sprite pairs. The squared allocation formula is present in the binary; it is not a necessary framebuffer footprint. [Static: `0x00180074..0x0018015C`.]

Keep RAM pointer views distinct: if the allocation pointer is P, entry+8 stores P and entry+4 stores `L=(P+0x3F)&~0x3F`. Context-1 list recording writes through uncached alias `(L&0x1FFFFFFF)|0x40000000`; vertices are prepared through the allocation-derived pointer at L+`0x200`. GE CALL/vertex BASE words use the pointer masked with `0x1FFFFFFF`, while low-address words carry the low 24 bits. CPU data-cache writeback-all calls bracket list recording at `0x00180160` and `0x00180294`, making the cached vertex writes visible without copying the image/list into a separate host resource. Actual P/L values are UNKNOWN without runtime memory. [Static: `0x001800B8..0x001800D8`, `0x0017F230..0x0017F298`, `0x0017EC74`, `0x0017EE6C`.]

For strip `j=0..14`, UV endpoints are `(32*j,0)` and `(32*(j+1),272)`. Destination endpoints are `(X+32*j,0,0)` and `(X+32*(j+1),272,0)`, where X=480 for entry 0 and 0 for entry 1. Edge coordinates denote the rectangle edges, not an extra rendered pixel at x=480 or y=272. Colours are diagnostic packed values `0xFFFFFF00 | (20*j)`, not uniformly white; RGB REPLACE ignores their RGB for conversion. The builder submits one `PRIM SPRITES` with 30 vertices, not 15 separate PRIM commands. Raw call argument `0x1280011E` is masked by `0x0017EE6C` to GE `VTYPE=0x80011E`: through mode, short UV/XYZ, RGBA8888 colour, no weights/indices. [Static: `0x001800FC..0x0018015C`, `0x00180220..0x00180238`, `0x0017EE6C`; prior `FB000805`.]

| Explicit recorded state | Conversion setting | Evidence |
| --- | --- | --- |
| Framebuffer | Format 0, pointer `B+0xD4000`, stride 1024 | `0x00180180 -> 0x0017F7A8` |
| Texture | Format 3; mode word 0: linear/unswizzled, no mip levels; address `0x0404C000`, stride 512, size exponents 9/9 | `0x00180194`, `0x001801B4`; `FB000806`, `FB000807` |
| Texture coherency | TEXFLUSH emitted before sampling | `0x001801BC`; `FB000804` |
| Combiner | REPLACE, RGB-only (`tfx=3,tcc=0`); colour-double bit captured from GU context at build time, initially 0 | `0x001801C8 -> 0x0017E928`, `0x0017DBD4` |
| Filter | Nearest min/mag, `TEXFILTER=0` | `0x001801D4`; `FB000798` |
| Tests/blend | Alpha test, depth test, stencil test, blend disabled; texture enabled | `0x001801DC..0x00180200 -> 0x0017E3C4` |
| Region/scissor | `(0,0)..(1023,1023)` inclusive | `0x00180210 -> 0x0017DF28` |
| Dither | Enabled for the sprite draw; matrix not uploaded by this recorded list | `0x00180218`, `0x0018025C`; `FB000169` |
| Masks/depth state | No MASKRGB, MASKALPHA, ZWRITEDISABLE, or ZBP/ZBW update in the recorded list | Complete builder/emitter trace; `FB001287` |

Normal one-time `sceGuStart` setup uploads the matrix at `0x001E8DF0`, verified as `-4 0 -3 1 / 2 -2 3 -1 / -3 1 -4 0 / 3 -1 2 -2`. The pool temporarily sets the initialized flag while recording, suppressing that setup within each conversion list; the subsequent first direct device-state list uploads it through `0x0017F2F4`. Thus this is the statically established default, not proof that every future runtime draw inherits it unchanged. [Static: `0x0017DCCC..0x0017DD10`, `0x0017F2E4..0x0017F324`, bytes at `0x001E8DF0`; prior `FB002513`, `FB002514`.]

Alpha/stencil: source alpha is ignored by the RGB-only replacement combiner, alpha/stencil tests and blending are disabled, and RGB565 has no alpha/stencil storage under the documented GE model. Conversion does not preserve scene alpha/stencil into a separate display plane. The source image itself is sampled, not intentionally modified. Depth remains bound but its test is disabled; the list does not issue a depth clear or a new depth bind. The inherited masks and other inherited state observed at runtime are in the answer under "Runtime observations".

### Restoration and inherited state

- Which state is restored by the recorded list, and which state is inherited or left changed?

Static answer: the tail installs a fixed baseline, not a saved-state restore. It binds RGBA8888 scene `0x0404C000` at stride 512, enables texture and blend, disables dither, enables depth test, sets texture combiner MODULATE/RGBA, and restores region/scissor to `(0,0)..(479,271)`. It ends in RET because it was recorded in context 1, not FINISH/END. [Static: `0x0018023C..0x00180290`, `0x0017F3E4`; prior `FB000170`, `FB001281`, `FB001287`.]

Alpha and stencil tests remain disabled. Nearest filtering and the scene texture binding/mode remain installed. VTYPE, vertex/index pointers, and BASE have been changed by the draw emitter; these are not restored. The list does not write fog, lighting, colour-test, logic-op, wrap, coordinate mapping/scale/offset, viewport/offset, blend equation/factors, masks, depth pointer/stride/write-disable, or the dither matrix. They remain inherited from execution-time state, except that the combiner colour-double bit is baked into the recorded words from initialization-time GU state. Texture/depth/blend enables restored by the tail are fixed values, regardless of their entry values.

The global engine dirty mask is ORed with `0x7AF` after selection (`0x0017F070..0x0017F09C`) so later engine state flushing can re-emit its tracked groups. This CPU bookkeeping is separate from the GE's effective state; executing CALL/RET does not itself update the cached GU fields. `0x0017F7A8` emits a current target but does not replace the persistent scene offset at `0x00587A60`. [Static: `0x0017F7A8`, `0x0017F830`, `0x0017EFCC`; prior `FB000160`, `FB001273`, `FB001274`.]

With aligned list start and the initialized guard set, the explicit emitter sequence derives to 40 words (`0xA0` bytes), including the final RET, inside the reserved `0x200`-byte command prefix. There is no per-frame rebuild or patch of these words in the inspected presentation path: it reads entry+4 and emits BASE/CALL. The exact RAM allocation addresses and a runtime no-rewrite observation are UNKNOWN. [Static/derived: full `0x0017FFF4` assembly and selected emitters; `0x0017F05C`; prior `FB001282`, `FB001287`.]

### Entry fields and globals

Only fields actually accessed by this path are named; entry size is 0x24, not an inferred complete structure.

| Entry displacement | Verified access/meaning |
| --- | --- |
| `+0x00` | Signed stamp; initialized -1; producer writes frame counter; thread reads it |
| `+0x04` | 64-byte-aligned callable conversion-list address |
| `+0x08` | Raw list/vertex allocation address before alignment |
| `+0x0C` | Display view pointer `B+0xD43C0` or `B+0xD4000` |
| `+0x10` | Scanout pixel stride 1024 |
| `+0x14` | Scanout pixel format 0 |
| `+0x18..+0x23` | Zeroed by entry initialization; no semantic field recovered here |

Evidence: `0x0017DC58..0x0017DCBC`, `0x00180030..0x001800C8`, `0x0017F060..0x0017F068`, `0x0017F170..0x0017F1AC`.

| Corrected image global | Expected CPU runtime address | Meaning in this trace |
| --- | --- | --- |
| `0x00587A38` | `0x08D8BA38` | GU context / initialized flag at +0 |
| `0x00587A44` | `0x08D8BA44` | API-returned eDRAM base |
| `0x00587A60` | `0x08D8BA60` | Persistent scene offset, mode 0: `0x4C000` |
| `0x00587A68` / `0x00587A6C` | `0x08D8BA68` / `0x08D8BA6C` | Cached depth pointer/stride; pointer can diverge from emitted state |
| `0x00587A88` | `0x08D8BA88` | Cached emitted framebuffer format; not proof of current GE state |
| `0x00587B58` | `0x08D8BB58` | Entry count 2 |
| `0x00587B5C` | `0x08D8BB5C` | Last requested display stamp D, initially 0 |
| `0x00587B60` | `0x08D8BB60` | Producer frame counter C, initially 1 |
| `0x00587B64` | `0x08D8BB64` | Pointer to 0x48-byte entry array |

Depth/frame cache claims start from `FB000899..FB000903`; pool globals from `FB001279`. Independent raw-reference queries covered scene-offset, eDRAM-base, depth-cache, count, stamp, counter, and entry-array accesses. The scene-offset writers recovered are context reset, draw-buffer setup, and display-mode setup, not ordinary offscreen target binds. The display-mode helper writes the same offset during initialization, so "never rewritten" in `FB001272` should mean stable after initialization, not literally a single store.

### Producer selection and reuse

- How does the producer choose an entry, update its stamp, and avoid writing an image still needed by display?

Static answer, with signed 32-bit comparisons:

```text
candidate = null
repeat:
    bound = D
    scan entries in ascending index order:
        if entry.stamp < bound:
            bound = entry.stamp
            candidate = entry
    if candidate == null: wait for vblank start
until candidate != null

if selection_argument == 0:
    emit BASE/CALL(candidate.list)
    candidate.stamp = C
mark tracked render state dirty (mask |= 7AF)
```

It chooses the minimum stamp strictly below D. Equal minimum stamps retain the first encountered entry. Stamps equal to D are not reusable; in the ordinary immediate-switch steady state this excludes the currently requested image. There is no modulo-entry index or unconditional alternation. With D=0, C=1 and both stamps=-1, entry 0 wins the initial tie. A flag-2 presentation calls selection with argument 1: it still waits for an eligible entry, but emits no conversion CALL and writes no stamp. [Static: `0x0017F000..0x0017F068`, signed `slt` at `0x0017F014`, `0x0017D8E0..0x0017D904`; prior `FB001277`, `FB001286`.]

The reuse rule is against the last requested display stamp, not a queried active framebuffer or GPU completion stamp. The completion answer under "Runtime observations" shows that this rule also covers the first deferred request. A normal producer cannot distinguish an actually scanned-out image from a pending first request by this bookkeeping alone. The stamp store at `0x0017F068` follows CPU command recording, not completion of the recorded GE conversion.

### Display-thread selection, counters, and wraparound

- How does the display thread choose an entry? Recover exact predicates, tie handling, counter initialization, and meaningful wraparound behavior rather than describing this as simple alternation.

Static answer:

```text
first_request = true
forever:
    wait for vblank start
    candidate = null
    bound = D
    scan entries in ascending index order:
        if bound < entry.stamp:
            bound = entry.stamp
            candidate = entry
    if candidate != null:
        SetFrameBuf(candidate.base, 1024, 0, first_request ? 1 : 0)
        first_request = false
        D = candidate.stamp
```

The thread chooses the greatest stamp strictly above D, skipping stale/equal entries; equal greatest stamps retain the first encountered entry. If no newer stamp exists it repeats the vblank wait without issuing a switch. Both comparisons are signed `slt`, not unsigned or modular sequence comparisons. D is written by the thread after the display call; the API's return value is not checked. The final store rereads the candidate stamp at `0x0017F1A0`. [Static: `0x0017F0CC..0x0017F1AC`, especially `0x0017F114`; prior `FB001278`.]

`0x0017DB54` initializes D=0 and C=1 at `0x0017DC1C/0x0017DC20`; pool initialization sets both entry stamps=-1 at `0x0017DCB0`. `0x0017D7CC` increments C at `0x0017D978` after finishing the direct bundle, including flag-2 calls that do not stamp a new image. It does not increment in the display thread or in selection itself.

Wrap is not handled correctly as a modular clock: the instruction is non-trapping `addiu`, but comparisons remain signed. If D reaches `0x7FFFFFFF`, a new `0x80000000` stamp is negative and is not newer. Even an older positive entry can be repeatedly reused/stamped negative without advancing D; selection cannot make D cross that boundary. A hypothetical uninterrupted 60/30 presentations per second reaches the boundary after roughly 414/829 days; these are arithmetic examples, not observed game rates. No reset-on-wrap was found among the traced writers. This qualifies "newest" and "lowest" in `FB001277/FB001278` as signed ordering within the normal counter range.

### Steady-state presentation and completion boundary

This is the verified ordering behind the still-open completion question:

```text
CPU, 0017D7CC (scene-command ring active):
  finish current recorded scene list with RET                 0017D864
  blocking DrawSync(0) for previously submitted direct work  0017D870
  optional callback; flags&3==1: wait for vblank start         0017D890 / 0017D8A8
  conditional CPU data-cache writeback-all                   0017D8C4
  start direct scratch list, initially stalled               0017D8D8
  select reusable display entry                             0017D900 (normal path)
    append BASE/CALL of conversion; publish CPU stamp        0017F05C / 0017F068
  if scene-ring gate >= 0, append retained scene-list CALL   0017D91C
  append FINISH/END; update GE stall address                 0017D924 -> 0017F3E4
  update scene-ring bookkeeping; increment C                 0017D92C..0017D97C
  start context-1 recording in next scene-command slot       0017D988

GE, once the direct-list stall is advanced:
  bind persistent scene target at direct-list start
  CALL conversion: read completed scene -> selected RGB565; restore scene; RET
  CALL retained scene list, when gate permits: render subsequent scene; RET
  FINISH / END

display thread, independent of this GE completion:
  vblank-start wait -> choose highest stamp > D
  SetFrameBuf(entry+0C, entry+10, entry+14, first ? 1 : 0)
  D = entry.stamp
```

The conversion precedes the retained scene CALL in the same direct list. It consumes scene contents produced by preceding submitted work, not necessarily the scene list the CPU just finished recording. The first scene-ring gate is -1 and suppresses that retained CALL on the first bundle. The command-ring selector toggles independently of the display pool; do not confuse these two rings or infer which image is displayed from its parity. [Static: `0x0017D5AC`, `0x0017D7F4..0x0017D82C`, `0x0017D8D8..0x0017D988`; prior `FB001286`.]

`0x0017F1CC` context 0 enqueues a direct list with its initial stall at the current write pointer. It writes subsequent target words without releasing that stall. `0x0017EC74` only appends BASE/CALL and does not update the stall. Thus the normal stamp publication occurs before the direct list's `0x0017F3E4` FINISH/END and stall update; those commands are not made executable by the stamp store. Context 1 lists end in RET and are callable recordings, not separately enqueued work. The third start argument is a word capacity: `0x0017F1FC` shifts it left by 2; its name "size" must not imply bytes. [Static: `0x0017F1CC`, `0x0017F3E4`, `0x0017EC74`, `0x0017EE6C`; prior `FB001280..FB001282`.]

Completion mechanisms are distinct:

| Mechanism | Established role | Does it prove the currently selected display image is complete before display selection? |
| --- | --- | --- |
| CPU entry stamp | Publishes selection/frame counter immediately after recording CALL | No |
| `sceGeDrawSync(0)` before the new direct bundle | Waits for previously submitted work, including prior conversion/scene work | Not for the conversion appended afterwards |
| GE CALL/RET and list ordering | Conversion reads previous scene before retained scene list overwrites it | Protects producer/source ordering, not independent display-thread timing |
| FINISH/END plus stall update | Releases direct work and provides a completion event | Display thread does not wait for it |
| SIGNAL callback `0x0017DAA4` | Records 16-bit signal IDs, invokes optional hook, signals semaphore at context+0x2C | No wait on this semaphore in display selection/thread |
| FINISH callback `0x0017DB20` | Invokes optional context+4 hook; that field is reset to zero | Does not update entry stamp/D or gate the thread in the inspected path |
| Vblank-start waits | Pace selection/display and optional producer synchronization | Timing opportunity, not a GE completion fence |

The callback context is corrected image address `0x005866C0`; semaphore slot is `0x005866EC`. This callback/semaphore family is distinct from the display stamp/counter family at `0x00587B58..0x00587B64`. [Static: `0x0017FEF8..0x0017FF2C`, `0x0017DAA4`, `0x0017DB20`, `0x0017EF34`, `0x0017F0B8`; prior `FB001276`.]

### Display request timing

- Does `sceDisplaySetFrameBuf` request an immediate or deferred switch, and when does the selected image become active?

Static answer: the first successful selection uses sync argument 1 at `0x0017F17C/0x0017F180`; every subsequent selection uses argument 0 at `0x0017F198/0x0017F19C`. Under the PSP API contract these mean next-frame/deferred and immediate respectively. The first-request flag changes after issuing the API request, not after checking success or observing active scanout. D is then updated for either form. Consequently D denotes last requested stamp, not a guaranteed active-image stamp. The boot capture under "Runtime observations" shows both early presentations completed before the splash was on screen. Exact latch time relative to the preceding vblank-start wait and actual API success are not observed; no active-frame event is claimed. [Static: full `0x0017F0B8` assembly; import NID `0x289D82FE` at `0x001D6FA0`; qualifies `FB001278`.]

### Main-camera and FX-worker connection

- How do the main camera path and the FX worker reach this same presentation machinery? Trace only their connection, not the effects themselves.

Static answer:

```text
main camera:
  000D8478 -> 001704C8(camera,0,flags)
             -> 00174E4C(camera.frameRaster at +60,0,flags)
                -> device raster-show slot -> 0017ACEC -> 0017D7CC(flags)

FX worker:
  000F0DAC worker loop -> 0017D7CC(0) at 000F0E28
```

`0x000D8478` uses flag 1 when `0x00010018` returns nonzero, otherwise 0; override byte `0x001EC919` forces flag 2 and is cleared. Assembly verifies that `0x001704C8` changes only a0 to the camera frame raster and preserves a1/a2, despite its decompiled single-argument signature. `0x00174E4C` dispatches through device+`0x98`. Device-system case `0xB` calls `0x0017AD1C` to install indexed handlers; the pair at `0x004F48F8` is slot `0x14` -> `0x0017ACEC`, corroborating the driver endpoint. The driver forwards the third argument and returns 1 regardless of the present helper's return. Worker message/effect handling is outside this trace. [Static: `0x000D8478`, `0x001704C8`, `0x00174E4C`, `0x0017AF5C`, `0x0017AD1C`, bytes at `0x004F48E0`, `0x0017ACEC`, `0x000F0DAC`; prior `FB001283`, `FB001284`, `FB001286`.]

### Evidence index and proposed ledger corrections

These are reproducible wrapper queries, not runtime captures. All follow-up commands use `--followup`. For independent verification use `--no-factbook` on supported subcommands so prior annotations are not mistaken for new evidence.

| Evidence group | Selected binary locations / query | Supports |
| --- | --- | --- |
| Initialization | `fn 0x0017ADA8 0x0017FE9C 0x0017DB54 0x0017B440 0x0017DC2C --only c`; selected `--only asm --limit 0` | Actual call order, guards, reset counters, mode branches, metadata versus image initialization |
| Fixed buffer setup | `fn 0x0017F830 0x0017F8C4 0x0017F918 0x0017F96C 0x0017F7A8 --only c`; `slice 0x0017B8F4 --before 18 --after 20 --limit 0` | Persistent pointer, command operands, dimensions, depth-cache divergence |
| Conversion recording | `fn 0x0017FFF4 --only c,asm --limit 0`; `fn 0x0017ED04 0x0017EE10 0x0017E928 0x0017EE6C 0x0017DF28 --only c` | Allocation formula, exact vertices, 40-word derived list, explicit/inherited state |
| Producer/consumer predicates | `fn 0x0017EFCC 0x0017F0B8 --only asm --limit 0` | Signed comparisons, first-index ties, stamp publication, switch arguments |
| Ordering/completion | `fn 0x0017D7CC 0x0017F1CC 0x0017F3E4 0x0017EF34 0x0017EC74 0x0017DAA4 0x0017DB20 --only c`; assembly for start/present | Conversion-before-scene order, initial stall, prior-work sync, callback separation |
| Global writers | `xrefs 0x00587A44 0x00587A60 0x00587A68 0x00587A6C 0x00587B58 0x00587B5C 0x00587B60 0x00587B64 --raw --limit 0` plus context reset body | Writers/readers within the raw-reference method's limits; computed stores in reset must be read in context |
| Caller conflict | `fn 0x0017B440 --only xrefs --limit 0`; `xrefs 0x0017B440 --raw`; `slice 0x0017B604 --before 4 --after 32 --limit 0`; `fn 0x0017F96C --only xrefs --limit 0` | One recorded initialization caller versus four depth-bind sites inside that caller's callee |
| API import identity | `memory --limit 0`; `bytes 0x001D6AC4 --length 460 --limit 0`; `bytes 0x001D6F6C --length 96`; `bytes 0x001D6FCC --length 28`; `strings sceDisplay` | GE/display/Utils library ranges, descriptor pointers, API NIDs below |
| Default/reset state | `bytes 0x004F48A8 --length 32`; `bytes 0x004F4A80 --length 32`; `bytes 0x004F4DA8 --length 40`; `bytes 0x001E8DF0 --length 64` | One-time flag, reset-list state writes/FINISH/END, dither matrix |
| Caller connection | `fn 0x000D8478 0x001704C8 0x00174E4C 0x0017ACEC 0x000F0DAC --only c`; `bytes 0x004F48E0 --length 144` | Main-camera/worker routes into common helper |
| First-image source | `fn 0x000D7A00 0x000D7864 0x00111D68 0x000D88E4 --only c --no-factbook`; full splash-copy assembly; startup call-site slices; `bytes 0x001EC910 --length 16` | CPU splash population precedes early pumps and director creation; failure path has no fallback clear |

Import descriptor `0x001D6BD8` connects `sceGe_user` stubs beginning `0x001D6628` to NIDs at `0x001D6F6C`; descriptor `0x001D6BC4` connects `sceDisplay` stubs beginning `0x001D6688` to `0x001D6F9C`. The UtilsForUser descriptor at `0x001D6B8C` connects stubs beginning `0x001D66E8` to NIDs at `0x001D6FCC`. Each stub is 8 bytes and each NID is 4 bytes. Binary-verified stub/NID pairs, with API names interpreted under the established PSP interface model:

| Stub image address | NID | API interpretation |
| --- | --- | --- |
| `0x001D6628` | `0x03444EB4` | `sceGeListSync` |
| `0x001D6648` | `0xA4FC06A4` | `sceGeSetCallback` |
| `0x001D6650` | `0xAB49E76A` | `sceGeListEnQueue` |
| `0x001D6658` | `0xB287BD61` | `sceGeDrawSync` |
| `0x001D6668` | `0xE0D68148` | `sceGeListUpdateStallAddr` |
| `0x001D6670` | `0xE47E40E4` | `sceGeEdramGetAddr` |
| `0x001D6678` | `0x1F6752AD` | `sceGeEdramGetSize` |
| `0x001D6680` | `0xB77905EA` | `sceGeEdramSetAddrTranslation` |
| `0x001D6688` | `0x0E20F177` | `sceDisplaySetMode` |
| `0x001D6690` | `0x289D82FE` | `sceDisplaySetFrameBuf` |
| `0x001D6698` | `0x984C27E7` | `sceDisplayWaitVblankStart` |
| `0x001D66F0` | `0x79D1C3FA` | `sceKernelDcacheWritebackAll`; not writeback/invalidate-all (that NID is `0xB435DEC5` at stub `0x001D6700`) |

The import/NID bytes are static evidence; firmware-internal latch timing and physical eDRAM translation are not recovered by reading an import stub. API names/semantics are interpreted using the existing PSP research model and calling shapes, not execution of firmware in Ghidra.

Shared-ledger writes were not coordinated, so `factbook.tsv` was not edited. Proposed durable updates for later use through `factbook.py`:

| Existing anchor | Proposed correction/addition | Confidence |
| --- | --- | --- |
| `FB000016` | Replace "all four of its call sites" with one recorded caller `0x0017ADA8`, and four mutually exclusive depth-bind calls within `0x0017B440`; all emit 0/512 | HIGH static |
| `FB001287` / superseded `FB000159` | Preserve init-time-builder interpretation; add one PRIM/30 vertices, entry-specific x offset, callable RET, and no per-frame rebuild | HIGH static |
| `FB000161` / `FB001279` | Add exact entry bases, fields, shared-row formula and `0x88000` derived 272-row envelope; do not label it allocator-proven reservation | HIGH static/derived |
| `FB000901` / `FB001273` | Cached depth pointer can become `0xD4000` in draw-buffer setup without a new GE bind; it does not always mirror ZBP | HIGH static |
| `FB001272` / `FB001274` | Mode-0 scene offset is stable after initialization, with an additional same-value store through display setup; other selectable device modes exist | HIGH static |
| `FB001277` / `FB001278` | Add strict signed predicates, first-index tie retention, D=0/C=1/stamps=-1, argument-1 no-stamp path, and first deferred/subsequent immediate requests | HIGH static |
| `FB001286` | Prior-work DrawSync precedes current conversion; current stamp is published before stall release; conversion CALL precedes retained scene CALL | HIGH static |
| New completion claim | No display-thread GE/semaphore completion gate found in inspected path; safe current-image scanout is not established by CPU stamps | HIGH for static ordering; runtime safety UNKNOWN |

### Runtime verification coverage

The checks are recorded under "Runtime observations". Not covered: the init-time call order and list contents at runtime (boot log events were lost), the display API return value, the splash-failure branch, menus/movies/transitions, the final restoration commands of the conversion list as separate events (GE dumps flatten CALL/RET), and hardware timing. A GE dump does not preserve CPU display events or original CALL boundaries, so missing events in one are not negative evidence.

### Established foundation and next investigation

Static evidence establishes a mode-0 8888 scene, an explicit shared 16-bit depth view, and two side-by-side-per-row RGB565 scanout views. Presentation is recorded at initialization and later CALLed, converts the prior completed scene before the retained scene list, and restores a fixed subset of baseline state. The four-caller interpretation is incorrect; four branch-local depth binds explain the count. Cached depth and CPU presentation stamps must not be mistaken for effective depth state or GPU completion.

PPSSPP captures confirm the device-mode-0 bindings in one zone per shipped zone render mode, the conversion's inherited state, the absence of a GPU-completion gate before display requests, and the first-image path: successful splash decoding CPU-populates the fixed scene, and the two early presentations convert it into both views. Failed loading has no fallback clear in that path. Hardware display timing is not established. The bounded baseline storage/lifetime and one scratch-to-scene restoration trace are recorded in [handoff2-buffer-ownership.md](handoff2-buffer-ownership.md); physical storage and further scratch/effect ownership remain separate work.

[PSPSDK documentation](../../README.md) › Files

# debug/pspdebugkb.h

## Enumerations

### `enum PspDebugKbSettings`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_DEBUG_KB_MAXLEN` | `40` | Maximum string length. |
| `PSP_DEBUG_KB_BOX_X` | `6` | Place the box' upper-left corner at this location. |
| `PSP_DEBUG_KB_BOX_Y` | `8` |  |
| `PSP_DEBUG_KB_CHAR_COLOUR` | `0xffffffff` | FG and BG colour of unhighlighted characters. |
| `PSP_DEBUG_KB_BACK_COLOUR` | `0xff000000` |  |
| `PSP_DEBUG_KB_CHAR_HIGHLIGHT` | `0xff00ff00` | FG and BG colour of highlighted character. |
| `PSP_DEBUG_KB_BACK_HIGHLIGHT` | `0xff101010` |  |
| `PSP_DEBUG_KB_OFFSET_X` | `6` | Indent the printed characters by (X_OFFSET,Y_OFFSET) |
| `PSP_DEBUG_KB_OFFSET_Y` | `4` |  |
| `PSP_DEBUG_KB_SPACING_X` | `3` | Distance from one character to the next. |
| `PSP_DEBUG_KB_SPACING_Y` | `2` |  |
| `PSP_DEBUG_KB_NUM_CHARS` | `13` | Number of columns/rows (respectively) in [charTable(s)](pspdebugkb.c.md#chartable) |
| `PSP_DEBUG_KB_NUM_ROWS` | `4` |  |
| `PSP_DEBUG_KB_BOX_WIDTH` | `(PSP_DEBUG_KB_NUM_CHARS * PSP_DEBUG_KB_SPACING_X) + (2 * PSP_DEBUG_KB_OFFSET_X)` | Box width and height. |
| `PSP_DEBUG_KB_BOX_HEIGHT` | `((PSP_DEBUG_KB_NUM_ROWS + 1) * PSP_DEBUG_KB_SPACING_Y) + PSP_DEBUG_KB_OFFSET_Y` |  |
| `PSP_DEBUG_KB_COMMAND_ROW` | `4` | Array index of commandRow. |
| `PSP_DEBUG_KB_NUM_COMMANDS` | `5` | Number of commands on bottom row. |

## Functions

### `pspDebugKbShift()`

```c
void pspDebugKbShift(int *shiftState);
```

Switch charTable when SHIFT is pressed.

**Parameters:**

- `shiftState` – Pointer to an int indicating Caps Lock

### `pspDebugKbDrawKey()`

```c
void pspDebugKbDrawKey(int row, int col, int highlight);
```

Draw the specified key on the keyboard.

**Parameters:**

- `row` – The row of the character to print (in charTable)
- `col` – The column of the character to print (in charTable)
- `highlight` – 0 for plain; otherwise highlighted

### `pspDebugKbDrawString()`

```c
void pspDebugKbDrawString(char *str);
```

Draw the string at the top of the box.

**Parameters:**

- `str` – The string to print

### `pspDebugKbClearBox()`

```c
void pspDebugKbClearBox();
```

Clear the area where the box resides.

Called from pspDebugKbDrawBox and pspDebugKbInit (on exit).

### `pspDebugKbDrawBox()`

```c
void pspDebugKbDrawBox();
```

Draw the entire box on the desbug screen.

Called from shift() and doInputBox(char\*)

### `pspDebugKbInit()`

```c
void pspDebugKbInit(char *str);
```

Make the text box happen.

**Parameters:**

- `str` – The string to edit

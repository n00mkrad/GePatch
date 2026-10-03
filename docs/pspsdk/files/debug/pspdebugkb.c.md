[PSPSDK documentation](../../README.md) › Files

# debug/pspdebugkb.c

```c
#include <pspdebug.h>
#include <pspctrl.h>
#include <stdio.h>
#include <string.h>
#include "pspdebugkb.h"
```

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

### `pspDebugKbDrawString()`

```c
void pspDebugKbDrawString(char *str);
```

Draw the string at the top of the box.

**Parameters:**

- `str` – The string to print

### `pspDebugKbInit()`

```c
void pspDebugKbInit(char *str);
```

Make the text box happen.

**Parameters:**

- `str` – The string to edit

## Variables

### `loCharTable`

```c
char loCharTable[PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS][PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS] = {
  { '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=' },
  { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\' },
  { '\0', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '\0' },
  { '\0', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\0', '\0' }
};
```

### `hiCharTable`

```c
char hiCharTable[PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS][PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS] = {
  { '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+' },
  { 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|' },
  { '\0', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', '\0' },
  { '\0', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', '\0', '\0' }
};
```

### `commandRow`

```c
char* commandRow[][] = { "Shift", "[    ]", "Back", "Clear", "Done" };
```

### `charTable`

```c
char charTable[PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS][PSP_DEBUG_KB_NUM_ROWS][PSP_DEBUG_KB_NUM_CHARS];
```

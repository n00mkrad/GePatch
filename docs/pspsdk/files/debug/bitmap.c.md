[PSPSDK documentation](../../README.md) › Files

# debug/bitmap.c

```c
#include <pspuser.h>
#include <pspdisplay.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
```

## Data Structures

### `struct BitmapHeader`

```c
struct BitmapHeader {
    char id[2];
    uint32_t filesize;
    uint32_t reserved;
    uint32_t offset;
    uint32_t headsize;
    uint32_t width;
    uint32_t height;
    uint16_t planes;
    uint16_t bpp;
    uint32_t comp;
    uint32_t bitmapsize;
    uint32_t hres;
    uint32_t vres;
    uint32_t colors;
    uint32_t impcolors;
};
```

## Macros

### `BMP_ID`

```c
#define BMP_ID "BM"
```

### `PSP_SCREEN_WIDTH`

```c
#define PSP_SCREEN_WIDTH 480
```

### `PSP_SCREEN_HEIGHT`

```c
#define PSP_SCREEN_HEIGHT 272
```

### `PSP_LINE_SIZE`

```c
#define PSP_LINE_SIZE 512
```

### `BMP_RGB_BYTES_PER_PIXEL`

```c
#define BMP_RGB_BYTES_PER_PIXEL 3
```

## Functions

### `get_pixel_depth()`

```c
static int get_pixel_depth(int format);
```

### `fixed_write()`

```c
static int fixed_write(int fd, void *data, int len);
```

### `write_8888_line()`

```c
void write_8888_line(void *frame, void *line_buf, int line);
```

### `write_5551_line()`

```c
void write_5551_line(void *frame, void *line_buf, int line);
```

### `write_565_line()`

```c
void write_565_line(void *frame, void *line_buf, int line);
```

### `write_4444_line()`

```c
void write_4444_line(void *frame, void *line_buf, int line);
```

### `bitmapWrite()`

```c
int bitmapWrite(void *frame_addr, int format, const char *file);
```

[PSPSDK documentation](../../README.md) › Files

# font/pspfont.h

```c
#include <malloc.h>
```

Topics: [Fonts Library](../../topics/LibFont.md)

## Data Structures

### `struct SceFontStyle`

Font style info.

**See also:** [sceFontFindOptimumFont()](#scefontfindoptimumfont), [sceFontCalcMemorySize()](#scefontcalcmemorysize), [sceFontGetFontInfoByIndexNumber()](#scefontgetfontinfobyindexnumber), [sceFontFindFont()](#scefontfindfont), [sceFontGetFontList()](#scefontgetfontlist)

| Field | Description |
|---|---|
| `float width` | Width in points (1/72 inch), where 0 is system standard. |
| `float height` | Height in points (1/72 inch), where 0 is system standard. |
| `float xResolution` | Resolution, where 0 is system standard. |
| `float yResolution` | Resolution, where 0 is system standard. |
| `float weight` |  |
| `unsigned short family` |  |
| `unsigned short style` |  |
| `unsigned short subStyle` |  |
| `unsigned short language` | Language code (leave 0 if not specified) |
| `unsigned short region` | Region code (leave 0 if not specified) |
| `unsigned short country` | Country code (leave 0 if not specified) |
| `unsigned char fontName[64]` |  |
| `unsigned char fileName[64]` |  |
| `unsigned int extra` |  |
| `unsigned int expiration` | Expiration (leave 0 if not specified) |

### `struct SceFontCharacterData`

Fixed-point info about singular characters.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontCharacterDataFloat](#struct-scefontcharacterdatafloat), [SceFontInfo](#struct-scefontinfo), [SceFontCharacterInfo](#struct-scefontcharacterinfo)

```c
struct SceFontCharacterData {
    unsigned int width;
    unsigned int height;
    int top;
    int bottom;
    int shiftX;
    int shiftY;
    int shiftVertX;
    int shiftVertY;
    int hShift;
    int vShift;
};
```

### `struct SceFontCharacterDataFloat`

Floating-point info about singular characters.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontInfo](#struct-scefontinfo)

```c
struct SceFontCharacterDataFloat {
    float width;
    float height;
    float top;
    float bottom;
    float shiftX;
    float shiftY;
    float shiftVertX;
    float shiftVertY;
    float hShift;
    float vShift;
};
```

### `struct SceFontInfo`

General font info.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontCharacterDataFloat](#struct-scefontcharacterdatafloat), [SceFontStyle](#struct-scefontstyle), [sceFontGetFontInfo()](#scefontgetfontinfo)

```c
struct SceFontInfo {
    SceFontCharacterData maxFixed;
    SceFontCharacterDataFloat maxFloat;
    unsigned short maxWidth;
    unsigned short maxHeight;
    unsigned int characters;
    unsigned int subCharacters;
    SceFontStyle fontStyle;
    unsigned char depth;
    char unknown[3];
};
```

### `struct SceFontRect`

Rectangular size of the font images.

**See also:** [SceFontImageBuffer](#struct-scefontimagebuffer), [sceFontGetShadowImageRect()](#scefontgetshadowimagerect), [sceFontGetCharImageRect()](#scefontgetcharimagerect)

```c
struct SceFontRect {
    unsigned short width;
    unsigned short height;
};
```

### `struct SceFontCache`

Font cache data.

**See also:** [SceFontLibData](#struct-scefontlibdata)

| Field | Description |
|---|---|
| `void ** cache` | Another cache instance, or just null. |
| `int(* lock)(void *cache)` | Lock the cache. |
| `int(* unlock)(void *cache)` | Unlock the cache. |
| `void *(* find)(void *cache, unsigned int value, int key[4], unsigned int *result)` | Find the key in cache.<br>**Parameters:**<br>- `cache` – Cache instance.<br>- `value` – Generated.<br>- `key` – Key to search for.<br>- `result` – 1 on success, 0 otherwise.<br>**Returns:** Pointer to the slot where it was found, NULL otherwise. |
| `int(* writeKV)(void *cache, void *slot, int key[4])` |  |
| `int(* write0)(void *cache, void *slot, void *data, int size)` |  |
| `int(* write1)(void *cache, void *slot, void *data, int size)` |  |
| `int(* write2)(void *cache, void *slot, void *data, int size)` |  |
| `int(* write3)(void *cache, void *slot, void *data, int size)` |  |
| `int(* read0)(void *cache, void *slot, void *dest)` |  |
| `int(* read1)(void *cache, void *slot, void *dest)` |  |
| `int(* read2)(void *cache, void *slot, void *dest)` |  |
| `int(* read3)(void *cache, void *slot, void *dest)` |  |

### `struct SceFontLibData`

Info about a specific font.

**See also:** [SceFontCache](#struct-scefontcache), [sceFontNewLib()](#scefontnewlib)

| Field | Description |
|---|---|
| `void * unknown` | Leave null when initializing. |
| `unsigned int maxFonts` | Max number of fonts open at the same time. |
| `SceFontCache * cache` |  |
| `void *(* alloc)(void *data, unsigned int size)` |  |
| `void(* free)(void *data, void *pointer)` |  |
| `void *(* open)(void *data, char *path, int *error)` |  |
| `int(* close)(void *data, void *fileHandle)` |  |
| `unsigned int(* read)(void *data, void *fileHandle, void *out, unsigned int size, unsigned int num, int *error)` |  |
| `int(* seek)(void *data, void *fileHandle, unsigned int offset)` |  |
| `int(* onError)(void *data, int error)` |  |
| `int(* onReadComplete)(void *data, int status)` |  |

### `struct SceFontImageBuffer`

Buffer of the image containing a font.

**See also:** [SceFontRect](#struct-scefontrect), [sceFontGetShadowGlyphImage()](#scefontgetshadowglyphimage), [sceFontGetShadowGlyphImage_Clip()](#scefontgetshadowglyphimage_clip), [sceFontGetCharGlyphImage()](#scefontgetcharglyphimage), [sceFontGetCharGlyphImage_Clip()](#scefontgetcharglyphimage_clip)

```c
struct SceFontImageBuffer {
    unsigned int pixelFormat;
    int x;
    int y;
    SceFontRect size;
    unsigned short bytesPerLine;
    short unknown;
    unsigned char * data;
};
```

### `struct SceFontCharacterInfo`

All the information regarding a single character.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [sceFontGetShadowInfo()](#scefontgetshadowinfo), [sceFontGetCharInfo()](#scefontgetcharinfo)

```c
struct SceFontCharacterInfo {
    unsigned int width;
    unsigned int height;
    int x;
    int y;
    SceFontCharacterData data;
    char unknown[4];
};
```

## Typedefs

### `SceFontStyle`

```c
typedef struct SceFontStyle SceFontStyle;
```

Font style info.

**See also:** [sceFontFindOptimumFont()](#scefontfindoptimumfont), [sceFontCalcMemorySize()](#scefontcalcmemorysize), [sceFontGetFontInfoByIndexNumber()](#scefontgetfontinfobyindexnumber), [sceFontFindFont()](#scefontfindfont), [sceFontGetFontList()](#scefontgetfontlist)

### `SceFontCharacterData`

```c
typedef struct SceFontCharacterData SceFontCharacterData;
```

Fixed-point info about singular characters.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontCharacterDataFloat](#struct-scefontcharacterdatafloat), [SceFontInfo](#struct-scefontinfo), [SceFontCharacterInfo](#struct-scefontcharacterinfo)

### `SceFontCharacterDataFloat`

```c
typedef struct SceFontCharacterDataFloat SceFontCharacterDataFloat;
```

Floating-point info about singular characters.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontInfo](#struct-scefontinfo)

### `SceFontInfo`

```c
typedef struct SceFontInfo SceFontInfo;
```

General font info.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [SceFontCharacterDataFloat](#struct-scefontcharacterdatafloat), [SceFontStyle](#struct-scefontstyle), [sceFontGetFontInfo()](#scefontgetfontinfo)

### `SceFontRect`

```c
typedef struct SceFontRect SceFontRect;
```

Rectangular size of the font images.

**See also:** [SceFontImageBuffer](#struct-scefontimagebuffer), [sceFontGetShadowImageRect()](#scefontgetshadowimagerect), [sceFontGetCharImageRect()](#scefontgetcharimagerect)

### `SceFontCache`

```c
typedef struct SceFontCache SceFontCache;
```

Font cache data.

**See also:** [SceFontLibData](#struct-scefontlibdata)

### `SceFontLibData`

```c
typedef struct SceFontLibData SceFontLibData;
```

Info about a specific font.

**See also:** [SceFontCache](#struct-scefontcache), [sceFontNewLib()](#scefontnewlib)

### `SceFontImageBuffer`

```c
typedef struct SceFontImageBuffer SceFontImageBuffer;
```

Buffer of the image containing a font.

**See also:** [SceFontRect](#struct-scefontrect), [sceFontGetShadowGlyphImage()](#scefontgetshadowglyphimage), [sceFontGetShadowGlyphImage_Clip()](#scefontgetshadowglyphimage_clip), [sceFontGetCharGlyphImage()](#scefontgetcharglyphimage), [sceFontGetCharGlyphImage_Clip()](#scefontgetcharglyphimage_clip)

### `SceFontCharacterInfo`

```c
typedef struct SceFontCharacterInfo SceFontCharacterInfo;
```

All the information regarding a single character.

**See also:** [SceFontCharacterData](#struct-scefontcharacterdata), [sceFontGetShadowInfo()](#scefontgetshadowinfo), [sceFontGetCharInfo()](#scefontgetcharinfo)

## Enumerations

### `enum SceFontFamily`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_FONT_FAMILY_DEFAULT` | `0x0` |  |
| `SCE_FONT_FAMILY_SANS_SERIF` | `0x1` |  |
| `SCE_FONT_FAMILY_SERIF` | `0x2` |  |
| `SCE_FONT_FAMILY_ROUNDED` | `0x3` |  |

### `enum SceFontStyles`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_FONT_STYLE_DEFAULT` | `0x0` |  |
| `SCE_FONT_STYLE_REGULAR` | `0x1` |  |
| `SCE_FONT_STYLE_ITALIC` | `0x2` |  |
| `SCE_FONT_STYLE_THIN` | `0x3` |  |
| `SCE_FONT_STYLE_ITALIC_THIN` | `0x4` |  |
| `SCE_FONT_STYLE_BOLD` | `0x5` |  |
| `SCE_FONT_STYLE_ITALIC_BOLD` | `0x6` |  |
| `SCE_FONT_STYLE_THICK` | `0x7` |  |
| `SCE_FONT_STYLE_ITALIC_THICK` | `0x8` |  |

### `enum SceFontPixelFormat`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_FONT_PIXEL_FORMAT_L4` | `0x0` |  |
| `SCE_FONT_PIXEL_FORMAT_R4` | `0x1` |  |
| `SCE_FONT_PIXEL_FORMAT_8` | `0x2` |  |
| `SCE_FONT_PIXEL_FORMAT_24` | `0x3` |  |
| `SCE_FONT_PIXEL_FORMAT_32` | `0x4` |  |

### `enum SceFontLanguage`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_FONT_LANGUAGE_DEFAULT` | `0x0` |  |
| `SCE_FONT_LANGUAGE_JAPANESE` | `0x1` |  |
| `SCE_FONT_LANGUAGE_ENGLISH` | `0x2` |  |
| `SCE_FONT_LANGUAGE_KOREAN` | `0x3` |  |
| `SCE_FONT_LANGUAGE_CHINESE` | `0x4` |  |
| `SCE_FONT_LANGUAGE_JKC` | `0x5` |  |

### `enum SceFontVendorCountry`

| Enumerator | Value | Description |
|---|---|---|
| `SCE_FONT_VENDOR_COUNTRY_DEFAULT` | `0x0` |  |
| `SCE_FONT_VENDOR_COUNTRY_JAPAN` | `0x1` |  |
| `SCE_FONT_VENDOR_COUNTRY_USA` | `0x2` |  |
| `SCE_FONT_VENDOR_COUNTRY_KOREA` | `0x3` |  |

## Functions

### `sceFontFlush()`

```c
int sceFontFlush(void *libraryId);
```

Flush local font cache.

**Parameters:**

- `libraryId` – Font handle.

**Returns:** 0 on success, error code otherwise.

### `sceFontFindOptimumFont()`

```c
int sceFontFindOptimumFont(void *libraryId, SceFontStyle *fontStyle, int *error);
```

Find an optimum font.

**Parameters:**

- `libraryId` – Font handle.
- `fontStyle` – Style data of a wanted font.
- `error` – Address for an error code.

**Returns:** Index of the optimum font, otherwise 0.

### `sceFontGetFontInfo()`

```c
int sceFontGetFontInfo(void *fontHandle, SceFontInfo *fontInfo);
```

Get font info.

**Parameters:**

- `fontHandle` – Font library handle.
- `fontInfo` – Font information output.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetNumFontList()`

```c
int sceFontGetNumFontList(void *libraryHandle, int *error);
```

Get number of all available font lists.

**Parameters:**

- `libraryHandle` – Font library handle.
- `error` – Address for an error code.

**Returns:** Number of available font lists.

### `sceFontCalcMemorySize()`

```c
int sceFontCalcMemorySize(void *libraryHandle, SceFontStyle *fontStyle, int *error);
```

Calculate required memory size for a font.

**Parameters:**

- `libraryHandle` – Font library handle.
- `fontStyle` – Style for the requested font.
- `error` – Address for an error code.

**Returns:** Required memory size.

### `sceFontIsElement()`

```c
int sceFontIsElement();
```

### `sceFontClose()`

```c
int sceFontClose(void *fontHandle);
```

Close the font handle.

**Parameters:**

- `fontHandle` – Font handle.

**Returns:** 0 on success, error code otherwise.

### `sceFontPointToPixelV()`

```c
float sceFontPointToPixelV(void *libraryHandle, float points, int *error);
```

Convert units from points to pixels in the vertical direction.

**Parameters:**

- `libraryHandle` – Font library handle.
- `points` – Points value to convert.
- `error` – Address for an error code.

**Returns:** Pixels units.

### `sceFontPointToPixelH()`

```c
float sceFontPointToPixelH(void *libraryHandle, float points, int *error);
```

Convert units from points to pixels in the horizontal direction.

**Parameters:**

- `libraryHandle` – Font library handle.
- `points` – Points value to convert.
- `error` – Address for an error code.

**Returns:** Pixels units.

### `sceFontSetResolution()`

```c
int sceFontSetResolution(void *libraryHandle, float hres, float vres);
```

Set font resolution.

**Parameters:**

- `libraryHandle` – Font library handle.
- `hres` – Horizontal resolution.
- `vres` – Vertical resolution.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetShadowImageRect()`

```c
int sceFontGetShadowImageRect(void *fontHandle, unsigned short code, SceFontRect *output);
```

### `sceFontGetFontInfoByIndexNumber()`

```c
int sceFontGetFontInfoByIndexNumber(void *libraryHandle, SceFontStyle *fontStyle, int index);
```

Get font style info by index number.

**Parameters:**

- `libraryHandle` – Font library handle.
- `fontStyle` – Style output.
- `index` – Font index.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetShadowGlyphImage()`

```c
int sceFontGetShadowGlyphImage(void *fontHandle, unsigned short code, SceFontImageBuffer *output);
```

### `sceFontDoneLib()`

```c
int sceFontDoneLib(void *libraryHandle);
```

Terminate a font handle.

**Parameters:**

- `libraryHandle` – Font library handle.

**Returns:** 0 on success, error code otherwise.

### `sceFontOpenUserFile()`

```c
void * sceFontOpenUserFile(void *libraryHandle, char *path, unsigned int mode, int *error);
```

Open local font file.

**Parameters:**

- `libraryHandle` – Font library handle.
- `path` – Full path to the font.
- `mode` – 0 for file based stream, 1 for memory based stream.
- `error` – Address for an error code.

**Returns:** Font handle.

### `sceFontGetCharImageRect()`

```c
int sceFontGetCharImageRect(void *fontHandle, unsigned short code, SceFontRect *output);
```

Get size of the image of the character.

**Parameters:**

- `fontHandle` – Font handle.
- `code` – Character code.
- `output` – Pointer to output with width and size of the image.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetShadowGlyphImage_Clip()`

```c
int sceFontGetShadowGlyphImage_Clip(void *fontHandle, unsigned short code, SceFontImageBuffer *output, int x, int y, unsigned int width, unsigned int height);
```

### `sceFontNewLib()`

```c
void * sceFontNewLib(SceFontLibData *data, int *error);
```

Initialize a font library.

**Parameters:**

- `data` – Setup for a font library.
- `error` – Address for an error code.

**Returns:** Font library handle.

### `sceFontFindFont()`

```c
int sceFontFindFont(void *libraryHandle, SceFontStyle *fontStyle, int *error);
```

Find the font that exactly matches the style.

**Parameters:**

- `libraryHandle` – Font library handle.
- `fontStyle` – Style for the font to find.
- `error` – Address for an error code.

**Returns:** Index value of the font, -1 if no font is found, or 0 on error.

### `sceFontPixelToPointH()`

```c
float sceFontPixelToPointH(void *libraryHandle, float pixels, int *error);
```

Convert units from pixels to points in the horizontal direction.

**Parameters:**

- `libraryHandle` – Font library handle.
- `pixels` – Pixels value to convert.
- `error` – Address for an error code.

**Returns:** Points units.

### `sceFontGetCharGlyphImage()`

```c
int sceFontGetCharGlyphImage(void *fontHandle, unsigned short code, SceFontImageBuffer *output);
```

Get image of a character.

**Parameters:**

- `fontHandle` – Font handle.
- `code` – Character code.
- `output` – Output data.

**Returns:** 0 on success, error code otherwise.

### `sceFontOpen()`

```c
void * sceFontOpen(void *libraryHandle, int index, unsigned int mode, int *error);
```

Open a new font.

**Parameters:**

- `libraryHandle` – Font library handle.
- `index` – Font index (0 for default).
- `mode` – 0 for file based stream, 1 for memory based stream.
- `error` – Address for an error code.

**Returns:** Font handle.

### `sceFontGetShadowInfo()`

```c
int sceFontGetShadowInfo(void *fontHandle, unsigned short code, SceFontCharacterInfo *output);
```

### `sceFontOpenUserMemory()`

```c
void * sceFontOpenUserMemory(void *libraryHandle, char *font, unsigned int size, int *error);
```

Open font from memory.

**Parameters:**

- `libraryHandle` – Font library handle.
- `font` – Pointer to font in memory.
- `size` – Size of the font data.
- `error` – Address for an error code.

**Returns:** Font handle.

### `sceFontGetFontList()`

```c
int sceFontGetFontList(void *libraryHandle, SceFontStyle *output, int size);
```

Get available fonts.

**Parameters:**

- `libraryHandle` – Font library handle.
- `output` – Array of [SceFontStyle](#struct-scefontstyle).
- `size` – Size of the output array.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetCharGlyphImage_Clip()`

```c
int sceFontGetCharGlyphImage_Clip(void *fontHandle, unsigned short code, SceFontImageBuffer *output, int x, int y, unsigned int width, unsigned int height);
```

Get clipped image of the character.

**Parameters:**

- `fontHandle` – Font handle.
- `code` – Character code.
- `output` – Output data.
- `x` – X position of clipping.
- `y` – Y position of clipping.
- `width` – Clipping width.
- `height` – Clipping height.

**Returns:** 0 on success, error code otherwise.

### `sceFontGetCharInfo()`

```c
int sceFontGetCharInfo(void *fontHandle, unsigned short code, SceFontCharacterInfo *output);
```

Get info about character.

**Parameters:**

- `fontHandle` – Font handle.
- `code` – Character code.
- `output` – Output of character information.

**Returns:** 0 on success, error code otherwise.

### `sceFontSetAltCharacterCode()`

```c
int sceFontSetAltCharacterCode(void *libraryHandle, unsigned short code);
```

Set a fallback character.

**Parameters:**

- `libraryHandle` – Font library handle.
- `code` – Character code.

**Returns:** 0 on success, error code otherwise.

### `sceFontPixelToPointV()`

```c
float sceFontPixelToPointV(void *libraryHandle, float pixels, int *error);
```

Convert units from pixels to points in the vertical direction.

**Parameters:**

- `libraryHandle` – Font library handle.
- `pixels` – Pixels value to convert.
- `error` – Address for an error code.

**Returns:** Points units.

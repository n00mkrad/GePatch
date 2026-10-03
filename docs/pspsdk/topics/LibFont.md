[PSPSDK documentation](../README.md) › Topics

# Fonts Library

This module contains the imports for fonts.

Headers: [`font/pspfont.h`](../files/font/pspfont.h.md)

## Data Structures

- [`struct SceFontStyle`](../files/font/pspfont.h.md#struct-scefontstyle) – Font style info.
- [`struct SceFontCharacterData`](../files/font/pspfont.h.md#struct-scefontcharacterdata) – Fixed-point info about singular characters.
- [`struct SceFontCharacterDataFloat`](../files/font/pspfont.h.md#struct-scefontcharacterdatafloat) – Floating-point info about singular characters.
- [`struct SceFontInfo`](../files/font/pspfont.h.md#struct-scefontinfo) – General font info.
- [`struct SceFontRect`](../files/font/pspfont.h.md#struct-scefontrect) – Rectangular size of the font images.
- [`struct SceFontCache`](../files/font/pspfont.h.md#struct-scefontcache) – Font cache data.
- [`struct SceFontLibData`](../files/font/pspfont.h.md#struct-scefontlibdata) – Info about a specific font.
- [`struct SceFontImageBuffer`](../files/font/pspfont.h.md#struct-scefontimagebuffer) – Buffer of the image containing a font.
- [`struct SceFontCharacterInfo`](../files/font/pspfont.h.md#struct-scefontcharacterinfo) – All the information regarding a single character.

## Typedefs

- [`SceFontStyle`](../files/font/pspfont.h.md#scefontstyle) – Font style info.
- [`SceFontCharacterData`](../files/font/pspfont.h.md#scefontcharacterdata) – Fixed-point info about singular characters.
- [`SceFontCharacterDataFloat`](../files/font/pspfont.h.md#scefontcharacterdatafloat) – Floating-point info about singular characters.
- [`SceFontInfo`](../files/font/pspfont.h.md#scefontinfo) – General font info.
- [`SceFontRect`](../files/font/pspfont.h.md#scefontrect) – Rectangular size of the font images.
- [`SceFontCache`](../files/font/pspfont.h.md#scefontcache) – Font cache data.
- [`SceFontLibData`](../files/font/pspfont.h.md#scefontlibdata) – Info about a specific font.
- [`SceFontImageBuffer`](../files/font/pspfont.h.md#scefontimagebuffer) – Buffer of the image containing a font.
- [`SceFontCharacterInfo`](../files/font/pspfont.h.md#scefontcharacterinfo) – All the information regarding a single character.

## Enumerations

- [`SceFontFamily`](../files/font/pspfont.h.md#enum-scefontfamily)
- [`SceFontStyles`](../files/font/pspfont.h.md#enum-scefontstyles)
- [`SceFontPixelFormat`](../files/font/pspfont.h.md#enum-scefontpixelformat)
- [`SceFontLanguage`](../files/font/pspfont.h.md#enum-scefontlanguage)
- [`SceFontVendorCountry`](../files/font/pspfont.h.md#enum-scefontvendorcountry)

## Functions

- [`sceFontFlush()`](../files/font/pspfont.h.md#scefontflush) – Flush local font cache.
- [`sceFontFindOptimumFont()`](../files/font/pspfont.h.md#scefontfindoptimumfont) – Find an optimum font.
- [`sceFontGetFontInfo()`](../files/font/pspfont.h.md#scefontgetfontinfo) – Get font info.
- [`sceFontGetNumFontList()`](../files/font/pspfont.h.md#scefontgetnumfontlist) – Get number of all available font lists.
- [`sceFontCalcMemorySize()`](../files/font/pspfont.h.md#scefontcalcmemorysize) – Calculate required memory size for a font.
- [`sceFontIsElement()`](../files/font/pspfont.h.md#scefontiselement)
- [`sceFontClose()`](../files/font/pspfont.h.md#scefontclose) – Close the font handle.
- [`sceFontPointToPixelV()`](../files/font/pspfont.h.md#scefontpointtopixelv) – Convert units from points to pixels in the vertical direction.
- [`sceFontPointToPixelH()`](../files/font/pspfont.h.md#scefontpointtopixelh) – Convert units from points to pixels in the horizontal direction.
- [`sceFontSetResolution()`](../files/font/pspfont.h.md#scefontsetresolution) – Set font resolution.
- [`sceFontGetShadowImageRect()`](../files/font/pspfont.h.md#scefontgetshadowimagerect)
- [`sceFontGetFontInfoByIndexNumber()`](../files/font/pspfont.h.md#scefontgetfontinfobyindexnumber) – Get font style info by index number.
- [`sceFontGetShadowGlyphImage()`](../files/font/pspfont.h.md#scefontgetshadowglyphimage)
- [`sceFontDoneLib()`](../files/font/pspfont.h.md#scefontdonelib) – Terminate a font handle.
- [`sceFontOpenUserFile()`](../files/font/pspfont.h.md#scefontopenuserfile) – Open local font file.
- [`sceFontGetCharImageRect()`](../files/font/pspfont.h.md#scefontgetcharimagerect) – Get size of the image of the character.
- [`sceFontGetShadowGlyphImage_Clip()`](../files/font/pspfont.h.md#scefontgetshadowglyphimage_clip)
- [`sceFontNewLib()`](../files/font/pspfont.h.md#scefontnewlib) – Initialize a font library.
- [`sceFontFindFont()`](../files/font/pspfont.h.md#scefontfindfont) – Find the font that exactly matches the style.
- [`sceFontPixelToPointH()`](../files/font/pspfont.h.md#scefontpixeltopointh) – Convert units from pixels to points in the horizontal direction.
- [`sceFontGetCharGlyphImage()`](../files/font/pspfont.h.md#scefontgetcharglyphimage) – Get image of a character.
- [`sceFontOpen()`](../files/font/pspfont.h.md#scefontopen) – Open a new font.
- [`sceFontGetShadowInfo()`](../files/font/pspfont.h.md#scefontgetshadowinfo)
- [`sceFontOpenUserMemory()`](../files/font/pspfont.h.md#scefontopenusermemory) – Open font from memory.
- [`sceFontGetFontList()`](../files/font/pspfont.h.md#scefontgetfontlist) – Get available fonts.
- [`sceFontGetCharGlyphImage_Clip()`](../files/font/pspfont.h.md#scefontgetcharglyphimage_clip) – Get clipped image of the character.
- [`sceFontGetCharInfo()`](../files/font/pspfont.h.md#scefontgetcharinfo) – Get info about character.
- [`sceFontSetAltCharacterCode()`](../files/font/pspfont.h.md#scefontsetaltcharactercode) – Set a fallback character.
- [`sceFontPixelToPointV()`](../files/font/pspfont.h.md#scefontpixeltopointv) – Convert units from pixels to points in the vertical direction.

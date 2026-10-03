[PSPSDK documentation](../README.md) › Topics

# Utils Library

Headers: [`user/psputils.h`](../files/user/psputils.h.md)

## Data Structures

- [`struct SceKernelTimeval`](../files/user/psputils.h.md#struct-scekerneltimeval) – This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.
- [`struct _SceKernelUtilsMt19937Context`](../files/user/psputils.h.md#struct-_scekernelutilsmt19937context) – Structure for holding a mersenne twister context.
- [`struct _SceKernelUtilsMd5Context`](../files/user/psputils.h.md#struct-_scekernelutilsmd5context) – Structure to hold the MD5 context.
- [`struct _SceKernelUtilsSha1Context`](../files/user/psputils.h.md#struct-_scekernelutilssha1context) – Type to hold a sha1 context.

## Typedefs

- [`SceKernelTimeval`](../files/user/psputils.h.md#scekerneltimeval) – This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.
- [`SceKernelUtilsMt19937Context`](../files/user/psputils.h.md#scekernelutilsmt19937context) – Structure for holding a mersenne twister context.
- [`SceKernelUtilsMd5Context`](../files/user/psputils.h.md#scekernelutilsmd5context) – Structure to hold the MD5 context.
- [`SceKernelUtilsSha1Context`](../files/user/psputils.h.md#scekernelutilssha1context) – Type to hold a sha1 context.

## Functions

- [`sceKernelLibcTime()`](../files/user/psputils.h.md#scekernellibctime) – Get the time in seconds since the epoc (1st Jan 1970)
- [`sceKernelLibcClock()`](../files/user/psputils.h.md#scekernellibcclock) – Get the processor clock used since the start of the process.
- [`sceKernelLibcGettimeofday()`](../files/user/psputils.h.md#scekernellibcgettimeofday) – Get the current time of time and time zone information.
- [`sceKernelDcacheWritebackAll()`](../files/user/psputils.h.md#scekerneldcachewritebackall) – Write back the data cache to memory.
- [`sceKernelDcacheWritebackInvalidateAll()`](../files/user/psputils.h.md#scekerneldcachewritebackinvalidateall) – Write back and invalidate the data cache.
- [`sceKernelDcacheWritebackRange()`](../files/user/psputils.h.md#scekerneldcachewritebackrange) – Write back a range of addresses from the data cache to memory.
- [`sceKernelDcacheWritebackInvalidateRange()`](../files/user/psputils.h.md#scekerneldcachewritebackinvalidaterange) – Write back and invalidate a range of addresses in the data cache.
- [`sceKernelDcacheInvalidateRange()`](../files/user/psputils.h.md#scekerneldcacheinvalidaterange) – Invalidate a range of addresses in data cache.
- [`sceKernelIcacheInvalidateAll()`](../files/user/psputils.h.md#scekernelicacheinvalidateall) – Invalidate the instruction cache.
- [`sceKernelIcacheInvalidateRange()`](../files/user/psputils.h.md#scekernelicacheinvalidaterange) – Invalidate a range of addresses in the instruction cache.
- [`sceKernelUtilsMt19937Init()`](../files/user/psputils.h.md#scekernelutilsmt19937init) – Function to initialise a mersenne twister context.
- [`sceKernelUtilsMt19937UInt()`](../files/user/psputils.h.md#scekernelutilsmt19937uint) – Function to return a new psuedo random number.
- [`sceKernelUtilsMd5Digest()`](../files/user/psputils.h.md#scekernelutilsmd5digest) – Function to perform an MD5 digest of a data block.
- [`sceKernelUtilsMd5BlockInit()`](../files/user/psputils.h.md#scekernelutilsmd5blockinit) – Function to initialise a MD5 digest context.
- [`sceKernelUtilsMd5BlockUpdate()`](../files/user/psputils.h.md#scekernelutilsmd5blockupdate) – Function to update the MD5 digest with a block of data.
- [`sceKernelUtilsMd5BlockResult()`](../files/user/psputils.h.md#scekernelutilsmd5blockresult) – Function to get the digest result of the MD5 hash.
- [`sceKernelUtilsSha1Digest()`](../files/user/psputils.h.md#scekernelutilssha1digest) – Function to SHA1 hash a data block.
- [`sceKernelUtilsSha1BlockInit()`](../files/user/psputils.h.md#scekernelutilssha1blockinit) – Function to initialise a context for SHA1 hashing.
- [`sceKernelUtilsSha1BlockUpdate()`](../files/user/psputils.h.md#scekernelutilssha1blockupdate) – Function to update the current hash.
- [`sceKernelUtilsSha1BlockResult()`](../files/user/psputils.h.md#scekernelutilssha1blockresult) – Function to get the result of the SHA1 hash.

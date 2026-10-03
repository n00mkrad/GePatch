[PSPSDK documentation](../README.md) › Topics

# Registry Kernel Library

Headers: [`registry/pspreg.h`](../files/registry/pspreg.h.md)

## Data Structures

- [`struct RegParam`](../files/registry/pspreg.h.md#struct-regparam) – Struct used to open a registry.

## Macros

- [`SYSTEM_REGISTRY`](../files/registry/pspreg.h.md#system_registry) – System registry path.
- [`REG_KEYNAME_SIZE`](../files/registry/pspreg.h.md#reg_keyname_size) – Size of a keyname, used in [sceRegGetKeys](../files/registry/pspreg.h.md#scereggetkeys).

## Typedefs

- [`REGHANDLE`](../files/registry/pspreg.h.md#reghandle) – Typedef for a registry handle.

## Enumerations

- [`RegKeyTypes`](../files/registry/pspreg.h.md#enum-regkeytypes) – Key types.

## Functions

- [`sceRegOpenRegistry()`](../files/registry/pspreg.h.md#sceregopenregistry) – Open the registry.
- [`sceRegFlushRegistry()`](../files/registry/pspreg.h.md#sceregflushregistry) – Flush the registry to disk.
- [`sceRegCloseRegistry()`](../files/registry/pspreg.h.md#sceregcloseregistry) – Close the registry.
- [`sceRegOpenCategory()`](../files/registry/pspreg.h.md#sceregopencategory) – Open a registry directory.
- [`sceRegRemoveCategory()`](../files/registry/pspreg.h.md#sceregremovecategory) – Remove a registry dir.
- [`sceRegCloseCategory()`](../files/registry/pspreg.h.md#sceregclosecategory) – Close the registry directory.
- [`sceRegFlushCategory()`](../files/registry/pspreg.h.md#sceregflushcategory) – Flush the registry directory to disk.
- [`sceRegGetKeyInfo()`](../files/registry/pspreg.h.md#scereggetkeyinfo) – Get a key's information.
- [`sceRegGetKeyInfoByName()`](../files/registry/pspreg.h.md#scereggetkeyinfobyname) – Get a key's information by name.
- [`sceRegGetKeyValue()`](../files/registry/pspreg.h.md#scereggetkeyvalue) – Get a key's value.
- [`sceRegGetKeyValueByName()`](../files/registry/pspreg.h.md#scereggetkeyvaluebyname) – Get a key's value by name.
- [`sceRegSetKeyValue()`](../files/registry/pspreg.h.md#sceregsetkeyvalue) – Set a key's value.
- [`sceRegGetKeysNum()`](../files/registry/pspreg.h.md#scereggetkeysnum) – Get number of subkeys in the current dir.
- [`sceRegGetKeys()`](../files/registry/pspreg.h.md#scereggetkeys) – Get the key names in the current directory.
- [`sceRegCreateKey()`](../files/registry/pspreg.h.md#sceregcreatekey) – Create a key.
- [`sceRegRemoveRegistry()`](../files/registry/pspreg.h.md#sceregremoveregistry) – Remove a registry (HONESTLY, DO NOT USE)

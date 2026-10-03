[PSPSDK documentation](../README.md) › Topics

# File IO Library

This module contains the imports for the kernel's IO routines.

Headers: [`user/pspiofilemgr.h`](../files/user/pspiofilemgr.h.md)

## Enumerations

- [`IoAssignPerms`](../files/user/pspiofilemgr.h.md#enum-ioassignperms) – Permission value for the sceIoAssign function.

## Functions

- [`sceIoOpen()`](../files/user/pspiofilemgr.h.md#sceioopen) – Open or create a file for reading or writing.
- [`sceIoOpenAsync()`](../files/user/pspiofilemgr.h.md#sceioopenasync) – Open or create a file for reading or writing (asynchronous)
- [`sceIoClose()`](../files/user/pspiofilemgr.h.md#sceioclose) – Delete a descriptor.
- [`sceIoCloseAsync()`](../files/user/pspiofilemgr.h.md#sceiocloseasync) – Delete a descriptor (asynchronous)
- [`sceIoRead()`](../files/user/pspiofilemgr.h.md#sceioread) – Read input.
- [`sceIoReadAsync()`](../files/user/pspiofilemgr.h.md#sceioreadasync) – Read input (asynchronous)
- [`sceIoWrite()`](../files/user/pspiofilemgr.h.md#sceiowrite) – Write output.
- [`sceIoWriteAsync()`](../files/user/pspiofilemgr.h.md#sceiowriteasync) – Write output (asynchronous)
- [`sceIoLseek()`](../files/user/pspiofilemgr.h.md#sceiolseek) – Reposition read/write file descriptor offset.
- [`sceIoLseekAsync()`](../files/user/pspiofilemgr.h.md#sceiolseekasync) – Reposition read/write file descriptor offset (asynchronous)
- [`sceIoLseek32()`](../files/user/pspiofilemgr.h.md#sceiolseek32) – Reposition read/write file descriptor offset (32bit mode)
- [`sceIoLseek32Async()`](../files/user/pspiofilemgr.h.md#sceiolseek32async) – Reposition read/write file descriptor offset (32bit mode, asynchronous)
- [`sceIoRemove()`](../files/user/pspiofilemgr.h.md#sceioremove) – Remove directory entry.
- [`sceIoMkdir()`](../files/user/pspiofilemgr.h.md#sceiomkdir) – Make a directory file.
- [`sceIoRmdir()`](../files/user/pspiofilemgr.h.md#sceiormdir) – Remove a directory file.
- [`sceIoChdir()`](../files/user/pspiofilemgr.h.md#sceiochdir) – Change the current directory.
- [`sceIoRename()`](../files/user/pspiofilemgr.h.md#sceiorename) – Change the name of a file.
- [`sceIoDopen()`](../files/user/pspiofilemgr.h.md#sceiodopen) – Open a directory.
- [`sceIoDread()`](../files/user/pspiofilemgr.h.md#sceiodread) – Reads an entry from an opened file descriptor.
- [`sceIoDclose()`](../files/user/pspiofilemgr.h.md#sceiodclose) – Close an opened directory file descriptor.
- [`sceIoDevctl()`](../files/user/pspiofilemgr.h.md#sceiodevctl) – Send a devctl command to a device.
- [`sceIoAssign()`](../files/user/pspiofilemgr.h.md#sceioassign) – Assigns one IO device to another (I guess)
- [`sceIoUnassign()`](../files/user/pspiofilemgr.h.md#sceiounassign) – Unassign an IO device.
- [`sceIoGetstat()`](../files/user/pspiofilemgr.h.md#sceiogetstat) – Get the status of a file.
- [`sceIoChstat()`](../files/user/pspiofilemgr.h.md#sceiochstat) – Change the status of a file.
- [`sceIoIoctl()`](../files/user/pspiofilemgr.h.md#sceioioctl) – Perform an ioctl on a device.
- [`sceIoIoctlAsync()`](../files/user/pspiofilemgr.h.md#sceioioctlasync) – Perform an ioctl on a device.
- [`sceIoSync()`](../files/user/pspiofilemgr.h.md#sceiosync) – Synchronise the file data on the device.
- [`sceIoWaitAsync()`](../files/user/pspiofilemgr.h.md#sceiowaitasync) – Wait for asyncronous completion.
- [`sceIoWaitAsyncCB()`](../files/user/pspiofilemgr.h.md#sceiowaitasynccb) – Wait for asyncronous completion (with callbacks).
- [`sceIoPollAsync()`](../files/user/pspiofilemgr.h.md#sceiopollasync) – Poll for asyncronous completion.
- [`sceIoGetAsyncStat()`](../files/user/pspiofilemgr.h.md#sceiogetasyncstat) – Get the asyncronous completion status.
- [`sceIoCancel()`](../files/user/pspiofilemgr.h.md#sceiocancel) – Cancel an asynchronous operation on a file descriptor.
- [`sceIoGetDevType()`](../files/user/pspiofilemgr.h.md#sceiogetdevtype) – Get the device type of the currently opened file descriptor.
- [`sceIoChangeAsyncPriority()`](../files/user/pspiofilemgr.h.md#sceiochangeasyncpriority) – Change the priority of the asynchronous thread.
- [`sceIoSetAsyncCallback()`](../files/user/pspiofilemgr.h.md#sceiosetasynccallback) – Sets a callback for the asynchronous action.

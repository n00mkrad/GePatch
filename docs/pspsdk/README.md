# PSP Software Development Kit

*Markdown conversion of the doxygen-generated PSPSDK documentation, generated from pspdev/pspsdk commit 6f15c15 (2026-09-28). Images and external links have been removed. The [API Reference](#api-reference) section at the end of this page lists the topics, files and data structures.*

`https://pspdev.github.io/`

## Introduction

PSPSDK is a collection of open source libraries and tools written for Sony's Playstation Portable (PSP) gaming console. It is part of the PSPDEV SDK.

## Features

### PSPSDK provides a full set of libraries for creating PSP software:

- Stub libraries and headers for interfacing with the PSP operating system, ranging from threading libraries, file io, display driver and wifi networking.
- Basic runtime support (crt0) for executables and libraries.
- A libcglue library for fulfill newlib system call requirements.
- Support code for linking with the full Standard C Library provided with the PSPDEV toolchain.
- An implementation of the libGU graphics library. libGU provides an interface to the 2D and 3D hardware acceleration features found in the PSP's Graphic Engine.
- An implementation of the libGUM library. libGUM provides an interface for manipulating matrices for use in 3D software.
- A simple audio library that can be used to play back PCM audio streams.
- Support for building static executables and PRX files (relocatable modules).

### PSPSDK also includes several tools to assist in building PSP software:

- `bin2c`, `bin2o`, and `bin2s` for converting binary files into C source, object files, and assembler source files, respectively.
- `mksfo` and `mksfoex` for creating PARAM.SFO files.
- `pack-pbp` and `unpack-pbp` for adding and removing files from EBOOT.PBP.
- `psp-config` for locating PSPDEV tools and libraries.
- `psp-prxgen` for converting specially made ELFs to PRX files.
- `psp-build-exports` for creating export tables
- `psp-fixup-imports` for fixing up import tables post-linking to remove unused functions from the executable.

Documentation for the libraries are also provided, and can be found in the `doc/` directory of the PSPSDK source and binary distributions.

A library for Make (`build.mak`) is also included to provide an easy way to build simple programs and libraries. See any PSPSDK sample program for details on how `build.mak` is used.

## Installation

See `https://pspdev.github.io/` for instructions on how to easily install PSPSDK along with other tools provided in the PSPDEV SDK.

## Installation from source

### Requirements

To use PSPSDK you must have the following software installed:

- PSPDEV Toolchain
- GNU Make
- Git client
- GNU autoconf and automake(GNU Autotools)
- Zlib development libraries and headers

The following packages are not required to build PSPSDK, but are used to build documentation:

- Doxygen
- Graphviz

### Building

PSPSDK can be found in the Git repository located at `https://github.com/pspdev/pspsdk`. You can do the following command to download PSPSDK:

```bash
git clone https://github.com/pspdev/pspsdk.git
```

Once you've downloaded PSPSDK, run the following command from the pspsdk directory to create the configure script and support files (you must have `autoconf` and `automake` installed):

```bash
./bootstrap
```

PSPSDK uses the GNU autotools (`autoconf` and `automake`) for its build system. To install PSPSDK, run the following commands:

```bash
./configure
make
make doxygen-doc
make install
```

> [!NOTE]
> If you haven't installed Doxygen or don't want to build the library documentation, you can skip the `make doxygen-doc` command.

> [!TIP]
> You can use `build-and-install.sh` script for convenience.

## Notes

- This is a BETA release of PSPSDK. Some of the features and tools described here may not be fully implemented.
- By default PSPSDK will install into the directory where the PSPDEV toolchain is installed. If you decide to install PSPSDK somewhere else then you must define a PSPSDK environment variable that points to your alternate directory. The psp-config build utility will look for PSPSDK in the location specified in the PSPSDK environment variable first, or use its own location to determine where PSPSDK is installed.
- The Makefile templates provided by the sample code are designed for building a single executable or a library, but not both. If you plan on using these templates in your project to build both libraries and executables be aware that you will have to structure your project so that each library and executable are built in a seperate directory.

## Bugs

If you find a bug in PSPSDK, open an issue at `https://github.com/pspdev/pspsdk/issues`. If possible, include any code or documentation that can be used by the PSPSDK developers to recreate the bug.

## License

PSPSDK is distributed under a BSD-compatible license, with the exception of the files located in `tools/PrxEncrypter`. The files located in the `tools/PrxEncrypter` directory are subject to the terms of the GNU General Public License version 3. See the `LICENSE` files for more information.

## Resources

### Official Source Documentation

This is generated automatically from the repository `master` branch: `https://pspdev.github.io/pspsdk/`

### Additional Documentation

Here are links to additional community made documentation for contributors to the PSPSDK, mostly on the PSP hardware:

- PSP Allegrex documentation: Non-official documentation on the PSP CPU and VFPU.
- Unofficial PSP docs: A collection of docs from different authors and sources, covering more specific topics.
- Yet Another PSP Documentation: A very detailed hardware documentation, including software interfaces.

### Discord

You can find PSPDEV Maintainers over at `https://discord.gg/bePrj9W` in the `#psp-toolchain` channel :)

### Code of Conduct

We're all here to build software and have fun with our PSPs, and everyone deserves to be able to do that without fear of harassment.

Please follow our [Code of Conduct](pages/code-of-conduct.md), and we encourage you to contact the PSPDEV Maintainers if you think something isn't right.

## Thanks

The PSPSDK developers wish to thank all the people who have contributed bug fixes, ideas and support for the project. Also big thanks to nem for kicking off PSP development with all his work, the original imports system is based on his work in the hello world demo.

---

## API Reference

### Topics

- [Chnnlsv Library](topics/Chnnlsv.md) – Library imports for the vsh chnnlsv library.
- [Controller Kernel Library](topics/Ctrl.md) – This module contains the imports for controllers (buttons, pad).
- [Debug Utility Library](topics/Debug.md)
- [Driver interface to IoFileMgr](topics/IoFileMgr_Kernel.md) – This module contains the imports for the kernel's IO routines.
- [Driver interface to Stdio](topics/Stdio_Kernel.md) – This module contains the imports for the kernel's stdio routines.
- [File IO Library](topics/FileIO.md) – This module contains the imports for the kernel's IO routines.
- [Fonts Library](topics/LibFont.md) – This module contains the imports for fonts.
- [Graphics Utility Library](topics/GU.md)
- [Hprm Remote](topics/Hprm.md)
- [Integrated Remote Control System Library](topics/Sony.md) – This module contains the imports for the kernel's remote control routines.
- [Interface to the KDebugForKernel library.](topics/Kdebug.md)
- [Interface to the LoadCoreForKernel library.](topics/LoadCore.md)
- [Interface to the LoadExecForKernel library.](topics/LoadExecKernel.md)
- [Interface to the sceIdStorage_driver library.](topics/IdStorage.md)
- [Interface to the sceSyscon_driver library.](topics/Syscon.md)
- [Interface to the sceSysreg_driver library.](topics/Sysreg.md)
- [Interrupt Manager](topics/IntrMan.md) – This module contains routines to manage interrupts.
- [Interrupt Manager Kernel](topics/IntrManKern.md) – This module contains routines to manage interrupts.
- [Kernel Module Manager Library](topics/ModuleMgrKern.md) – This module contains the imports for the kernel's module management routines.
- [LoadExec Library](topics/LoadExec.md)
- [Module Manager Library](topics/ModuleMgr.md) – This module contains the imports for the kernel's module management routines.
- [PSPSDK Utility Library](topics/PSPSDK.md)
- [Registry Kernel Library](topics/Reg.md)
- [SAS Core Audio Library](topics/SAS.md) – This module contains the imports for sceSasCore, the PSP's audio software mixer.
- [Stdio Library](topics/Stdio.md) – This module contains the imports for the kernel's stdio routines.
- [System Memory Manager](topics/SysMem.md) – This module contains routines to manage heaps of memory.
- [System Memory Manager Kernel](topics/SysMemKern.md) – This module contains routines to manage heaps of memory.
- [Thread Manager kernel functions](topics/ThreadmanKern.md) – This module contains routines to threads in the kernel.
- [Thread Manager Library](topics/ThreadMan.md) – Library imports for the kernel threading library.
- [UMD Kernel Library](topics/UMD.md) – This module contains the imports for UMD drive.
- [User Audio Library](topics/Audio.md) – This module contains the imports for audio frequencies.
- [Utils Library](topics/Utils.md)

### Files

**atrac3/**

- [`pspatrac3.h`](files/atrac3/pspatrac3.h.md)

**audio/**

- [`pspaudio.h`](files/audio/pspaudio.h.md)
- [`pspaudio_kernel.h`](files/audio/pspaudio_kernel.h.md)
- [`pspaudiocodec.h`](files/audio/pspaudiocodec.h.md)
- [`pspaudiolib.c`](files/audio/pspaudiolib.c.md)
- [`pspaudiolib.h`](files/audio/pspaudiolib.h.md)

**base/**

- [`as_reg_compat.h`](files/base/as_reg_compat.h.md)
- [`psptypes.h`](files/base/psptypes.h.md)

**ctrl/**

- [`pspctrl.h`](files/ctrl/pspctrl.h.md)
- [`pspctrl_kernel.h`](files/ctrl/pspctrl_kernel.h.md)

**debug/**

- [`bitmap.c`](files/debug/bitmap.c.md)
- [`callstack.c`](files/debug/callstack.c.md)
- [`exception.c`](files/debug/exception.c.md)
- [`font.c`](files/debug/font.c.md)
- [`gdb-kernellib.c`](files/debug/gdb-kernellib.c.md)
- [`gdb-stub.c`](files/debug/gdb-stub.c.md)
- [`gdb-userlib.c`](files/debug/gdb-userlib.c.md)
- [`kprintf.c`](files/debug/kprintf.c.md)
- [`profiler.c`](files/debug/profiler.c.md)
- [`pspdebug.h`](files/debug/pspdebug.h.md)
- [`pspdebugkb.c`](files/debug/pspdebugkb.c.md)
- [`pspdebugkb.h`](files/debug/pspdebugkb.h.md)
- [`scr_printf.c`](files/debug/scr_printf.c.md)
- [`screenshot.c`](files/debug/screenshot.c.md)
- [`sio.c`](files/debug/sio.c.md)
- [`stacktrace.c`](files/debug/stacktrace.c.md)
- [`stdio.c`](files/debug/stdio.c.md)

**display/**

- [`pspdisplay.h`](files/display/pspdisplay.h.md)
- [`pspdisplay_kernel.h`](files/display/pspdisplay_kernel.h.md)

**dmac/**

- [`pspdmac.h`](files/dmac/pspdmac.h.md)

**font/**

- [`pspfont.h`](files/font/pspfont.h.md)

**fpu/**

- [`pspfpu.c`](files/fpu/pspfpu.c.md)
- [`pspfpu.h`](files/fpu/pspfpu.h.md)

**ge/**

- [`pspge.h`](files/ge/pspge.h.md)

**gu/**

- [`guInternal.c`](files/gu/guInternal.c.md)
- [`guInternal.h`](files/gu/guInternal.h.md)
- [`pspgu.h`](files/gu/pspgu.h.md)
- [`sceGuEndObject.c`](files/gu/sceGuEndObject.c.md)
- [`sceGuInit.c`](files/gu/sceGuInit.c.md)
- [`sceGuLight.c`](files/gu/sceGuLight.c.md)
- [`sceGuTexImage.c`](files/gu/sceGuTexImage.c.md)
- [`vram.c`](files/gu/vram.c.md)

**gum/**

- [`gumInternal.c`](files/gum/gumInternal.c.md)
- [`gumInternal.h`](files/gum/gumInternal.h.md)
- [`pspgum.h`](files/gum/pspgum.h.md)

**hprm/**

- [`psphprm.h`](files/hprm/psphprm.h.md)

**kermit/**

- [`pspkermit.h`](files/kermit/pspkermit.h.md)

**kernel/**

- [`pspamctrl.h`](files/kernel/pspamctrl.h.md)
- [`pspexception.h`](files/kernel/pspexception.h.md)
- [`pspidstorage.h`](files/kernel/pspidstorage.h.md)
- [`pspimpose_driver.h`](files/kernel/pspimpose_driver.h.md)
- [`pspinit.h`](files/kernel/pspinit.h.md)
- [`pspintrman_kernel.h`](files/kernel/pspintrman_kernel.h.md)
- [`pspiofilemgr_kernel.h`](files/kernel/pspiofilemgr_kernel.h.md)
- [`pspkdebug.h`](files/kernel/pspkdebug.h.md)
- [`pspkernel.h`](files/kernel/pspkernel.h.md)
- [`psploadcore.h`](files/kernel/psploadcore.h.md)
- [`psploadexec_kernel.h`](files/kernel/psploadexec_kernel.h.md)
- [`pspmodulemgr_kernel.h`](files/kernel/pspmodulemgr_kernel.h.md)
- [`pspstdio_kernel.h`](files/kernel/pspstdio_kernel.h.md)
- [`pspsysclib.h`](files/kernel/pspsysclib.h.md)
- [`pspsyscon.h`](files/kernel/pspsyscon.h.md)
- [`pspsysevent.h`](files/kernel/pspsysevent.h.md)
- [`pspsysmem_kernel.h`](files/kernel/pspsysmem_kernel.h.md)
- [`pspsysreg.h`](files/kernel/pspsysreg.h.md)
- [`pspsystimer.h`](files/kernel/pspsystimer.h.md)
- [`pspthreadman_kernel.h`](files/kernel/pspthreadman_kernel.h.md)
- [`psputilsforkernel.h`](files/kernel/psputilsforkernel.h.md)

**libcglue/**

- [`cwd.c`](files/libcglue/cwd.c.md)
- [`fdman.c`](files/libcglue/fdman.c.md)
- [`fdman.h`](files/libcglue/fdman.h.md)
- [`glue.c`](files/libcglue/glue.c.md)
- [`init.c`](files/libcglue/init.c.md)
- [`lock.c`](files/libcglue/lock.c.md) – The lock API functions required by newlib.
- [`mutexman.c`](files/libcglue/mutexman.c.md)
- [`netdb.c`](files/libcglue/netdb.c.md)
- [`netdb.h`](files/libcglue/netdb.h.md)
- [`pipe.c`](files/libcglue/pipe.c.md)
- [`select.c`](files/libcglue/select.c.md)
- [`sleep.c`](files/libcglue/sleep.c.md)

**libcglue/arpa/**

- [`inet.h`](files/libcglue/arpa/inet.h.md)

**libcglue/netinet/**

- [`in.h`](files/libcglue/netinet/in.h.md)
- [`tcp.h`](files/libcglue/netinet/tcp.h.md)

**libcglue/sys/**

- [`socket.h`](files/libcglue/sys/socket.h.md)

**libpthreadglue/**

- [`osal.c`](files/libpthreadglue/osal.c.md)
- [`tls-helper.c`](files/libpthreadglue/tls-helper.c.md)

**mp3/**

- [`pspmp3.h`](files/mp3/pspmp3.h.md)

**mpeg/**

- [`pspjpeg.h`](files/mpeg/pspjpeg.h.md)
- [`pspmpeg.h`](files/mpeg/pspmpeg.h.md)
- [`pspmpegbase.h`](files/mpeg/pspmpegbase.h.md)

**nand/**

- [`pspnand_driver.h`](files/nand/pspnand_driver.h.md)

**net/**

- [`psphttp.h`](files/net/psphttp.h.md)
- [`pspnet.h`](files/net/pspnet.h.md)
- [`pspnet_adhoc.h`](files/net/pspnet_adhoc.h.md)
- [`pspnet_adhocctl.h`](files/net/pspnet_adhocctl.h.md)
- [`pspnet_adhocmatching.h`](files/net/pspnet_adhocmatching.h.md)
- [`pspnet_apctl.h`](files/net/pspnet_apctl.h.md)
- [`pspnet_inet.h`](files/net/pspnet_inet.h.md)
- [`pspnet_resolver.h`](files/net/pspnet_resolver.h.md)
- [`pspssl.h`](files/net/pspssl.h.md)

**openpsid/**

- [`pspopenpsid.h`](files/openpsid/pspopenpsid.h.md)

**power/**

- [`psppower.h`](files/power/psppower.h.md)

**prof/**

- [`prof.c`](files/prof/prof.c.md)
- [`pspprof.h`](files/prof/pspprof.h.md)

**registry/**

- [`pspreg.h`](files/registry/pspreg.h.md)

**rtc/**

- [`psprtc.h`](files/rtc/psprtc.h.md)

**sascore/**

- [`pspsascore.h`](files/sascore/pspsascore.h.md)

**sdk/**

- [`fixup.c`](files/sdk/fixup.c.md)
- [`loadmodule.c`](files/sdk/loadmodule.c.md)
- [`memory.c`](files/sdk/memory.c.md)
- [`modulemgr_patches.c`](files/sdk/modulemgr_patches.c.md)
- [`pspsdk.h`](files/sdk/pspsdk.h.md)
- [`threadutils.c`](files/sdk/threadutils.c.md)

**sircs/**

- [`pspsircs.h`](files/sircs/pspsircs.h.md)

**startup/**

- [`crt0.c`](files/startup/crt0.c.md)
- [`crt0_prx.c`](files/startup/crt0_prx.c.md)
- [`prxexports.c`](files/startup/prxexports.c.md)

**umd/**

- [`pspumd.h`](files/umd/pspumd.h.md)

**usb/**

- [`pspusb.h`](files/usb/pspusb.h.md)
- [`pspusbacc.h`](files/usb/pspusbacc.h.md)
- [`pspusbbus.h`](files/usb/pspusbbus.h.md)
- [`pspusbcam.h`](files/usb/pspusbcam.h.md)

**usbstor/**

- [`pspusbstor.h`](files/usbstor/pspusbstor.h.md)

**user/**

- [`pspaudiorouting.h`](files/user/pspaudiorouting.h.md)
- [`pspimpose.h`](files/user/pspimpose.h.md)
- [`pspintrman.h`](files/user/pspintrman.h.md)
- [`pspiofilemgr.h`](files/user/pspiofilemgr.h.md)
- [`pspiofilemgr_devctl.h`](files/user/pspiofilemgr_devctl.h.md)
- [`pspiofilemgr_dirent.h`](files/user/pspiofilemgr_dirent.h.md)
- [`pspiofilemgr_fcntl.h`](files/user/pspiofilemgr_fcntl.h.md)
- [`pspiofilemgr_stat.h`](files/user/pspiofilemgr_stat.h.md)
- [`pspkerneltypes.h`](files/user/pspkerneltypes.h.md)
- [`pspkerror.h`](files/user/pspkerror.h.md)
- [`psploadexec.h`](files/user/psploadexec.h.md)
- [`pspmoduleexport.h`](files/user/pspmoduleexport.h.md)
- [`pspmoduleinfo.h`](files/user/pspmoduleinfo.h.md)
- [`pspmodulemgr.h`](files/user/pspmodulemgr.h.md)
- [`pspmscm.h`](files/user/pspmscm.h.md)
- [`pspstdio.h`](files/user/pspstdio.h.md)
- [`pspsuspend.h`](files/user/pspsuspend.h.md)
- [`pspsysmem.h`](files/user/pspsysmem.h.md)
- [`pspthreadman.h`](files/user/pspthreadman.h.md)
- [`psputils.h`](files/user/psputils.h.md)

**utility/**

- [`psputility.h`](files/utility/psputility.h.md)
- [`psputility_avmodules.h`](files/utility/psputility_avmodules.h.md)
- [`psputility_gamesharing.h`](files/utility/psputility_gamesharing.h.md)
- [`psputility_htmlviewer.h`](files/utility/psputility_htmlviewer.h.md)
- [`psputility_modules.h`](files/utility/psputility_modules.h.md)
- [`psputility_msgdialog.h`](files/utility/psputility_msgdialog.h.md)
- [`psputility_netconf.h`](files/utility/psputility_netconf.h.md)
- [`psputility_netmodules.h`](files/utility/psputility_netmodules.h.md)
- [`psputility_netparam.h`](files/utility/psputility_netparam.h.md)
- [`psputility_osk.h`](files/utility/psputility_osk.h.md)
- [`psputility_savedata.h`](files/utility/psputility_savedata.h.md)
- [`psputility_sysparam.h`](files/utility/psputility_sysparam.h.md)
- [`psputility_usbmodules.h`](files/utility/psputility_usbmodules.h.md)

**vaudio/**

- [`pspvaudio.h`](files/vaudio/pspvaudio.h.md)

**vfpu/**

- [`pspvfpu.c`](files/vfpu/pspvfpu.c.md)
- [`pspvfpu.h`](files/vfpu/pspvfpu.h.md)

**video/**

- [`pspvideocodec.h`](files/video/pspvideocodec.h.md)

**vsh/**

- [`pspchnnlsv.h`](files/vsh/pspchnnlsv.h.md)

**wlan/**

- [`pspwlan.h`](files/wlan/pspwlan.h.md)

### Data Structures

- [`struct __descriptormap_type`](files/libcglue/fdman.h.md#struct-__descriptormap_type)
- [`struct __lock`](files/libcglue/lock.c.md#struct-__lock)
- [`struct _library_entry`](files/startup/crt0.c.md#struct-_library_entry)
- [`struct _pspChnnlsvContext1`](files/vsh/pspchnnlsv.h.md#struct-_pspchnnlsvcontext1)
- [`struct _pspChnnlsvContext2`](files/vsh/pspchnnlsv.h.md#struct-_pspchnnlsvcontext2)
- [`struct _PspDebugProfilerRegs`](files/debug/pspdebug.h.md#struct-_pspdebugprofilerregs) – Structure to hold the psp profiler register values.
- [`struct _PspDebugRegBlock`](files/debug/pspdebug.h.md#struct-_pspdebugregblock) – Structure to hold the register data associated with an exception.
- [`struct _PspDebugStackTrace`](files/debug/pspdebug.h.md#struct-_pspdebugstacktrace) – Structure to hold a single stack trace entry.
- [`struct _PspLibraryEntry`](files/user/pspmoduleexport.h.md#struct-_psplibraryentry) – Structure to hold a single export entry.
- [`struct _PspSysmemPartitionInfo`](files/kernel/pspsysmem_kernel.h.md#struct-_pspsysmempartitioninfo)
- [`struct _pspUtilityGameSharingParams`](files/utility/psputility_gamesharing.h.md#struct-_psputilitygamesharingparams) – Structure to hold the parameters for Game Sharing.
- [`struct _pspUtilityMsgDialogParams`](files/utility/psputility_msgdialog.h.md#struct-_psputilitymsgdialogparams) – Structure to hold the parameters for a message dialog.
- [`struct _pspUtilityNetconfData`](files/utility/psputility_netconf.h.md#struct-_psputilitynetconfdata)
- [`struct _returnCache`](files/debug/callstack.c.md#struct-_returncache)
- [`struct _SceKernelUtilsMd5Context`](files/user/psputils.h.md#struct-_scekernelutilsmd5context) – Structure to hold the MD5 context.
- [`struct _SceKernelUtilsMt19937Context`](files/user/psputils.h.md#struct-_scekernelutilsmt19937context) – Structure for holding a mersenne twister context.
- [`struct _SceKernelUtilsSha1Context`](files/user/psputils.h.md#struct-_scekernelutilssha1context) – Type to hold a sha1 context.
- [`struct _scemoduleinfo`](files/user/pspmoduleinfo.h.md#struct-_scemoduleinfo)
- [`struct _SceUtilityOskData`](files/utility/psputility_osk.h.md#struct-_sceutilityoskdata) – OSK Field data.
- [`struct _SceUtilityOskParams`](files/utility/psputility_osk.h.md#struct-_sceutilityoskparams) – OSK parameters.
- [`struct _ThreadInfoSkel`](files/sdk/threadutils.c.md#struct-_threadinfoskel)
- [`struct _uidControlBlock`](files/kernel/pspsysmem_kernel.h.md#struct-_uidcontrolblock) – Structure of a UID control block.
- [`struct BitmapHeader`](files/debug/bitmap.c.md#struct-bitmapheader)
- [`struct ConfigDescriptor`](files/usb/pspusbbus.h.md#struct-configdescriptor) – USB configuration descriptor.
- [`struct DeviceDescriptor`](files/usb/pspusbbus.h.md#struct-devicedescriptor) – USB device descriptor.
- [`struct DeviceRequest`](files/usb/pspusbbus.h.md#struct-devicerequest) – USB EP0 Device Request.
- [`struct EndpointDescriptor`](files/usb/pspusbbus.h.md#struct-endpointdescriptor) – USB endpoint descriptor.
- [`struct gmonhdr`](files/prof/prof.c.md#struct-gmonhdr) – gmon.out file header
- [`struct gmonparam`](files/prof/prof.c.md#struct-gmonparam) – context
- [`struct GuContext`](files/gu/guInternal.h.md#struct-gucontext)
- [`struct GuDisplayList`](files/gu/guInternal.h.md#struct-gudisplaylist)
- [`struct GuDrawBuffer`](files/gu/guInternal.h.md#struct-gudrawbuffer)
- [`struct GuSettings`](files/gu/guInternal.h.md#struct-gusettings)
- [`struct hard_trap_info`](files/debug/gdb-stub.c.md#struct-hard_trap_info)
- [`struct hostent`](files/libcglue/netdb.h.md#struct-hostent)
- [`struct in_addr`](files/libcglue/netinet/in.h.md#struct-in_addr)
- [`struct InterfaceDescriptor`](files/usb/pspusbbus.h.md#struct-interfacedescriptor) – USB Interface descriptor.
- [`struct iovec`](files/libcglue/sys/socket.h.md#struct-iovec)
- [`struct ip_mreq`](files/libcglue/netinet/in.h.md#struct-ip_mreq)
- [`struct ip_opts`](files/libcglue/netinet/in.h.md#struct-ip_opts)
- [`struct KermitPacket_`](files/kermit/pspkermit.h.md#struct-kermitpacket_)
- [`struct linger`](files/libcglue/sys/socket.h.md#struct-linger)
- [`struct msghdr`](files/libcglue/sys/socket.h.md#struct-msghdr)
- [`union netData`](files/utility/psputility_netparam.h.md#union-netdata) – Datatype for sceUtilityGetNetParam since it can return a u32 or a string we use a union to avoid ugly casting.
- [`struct pdpStatStruct`](files/net/pspnet_adhoc.h.md#struct-pdpstatstruct) – PDP status structure.
- [`struct productStruct`](files/net/pspnet_adhocctl.h.md#struct-productstruct) – Product structure.
- [`struct psp_audio_channelinfo`](files/audio/pspaudiolib.h.md#struct-psp_audio_channelinfo)
- [`struct pspAdhocMatchingMember`](files/net/pspnet_adhocmatching.h.md#struct-pspadhocmatchingmember) – Linked list for sceNetAdhocMatchingGetMembers.
- [`struct pspAdhocPoolStat`](files/net/pspnet_adhocmatching.h.md#struct-pspadhocpoolstat) – Linked list for sceNetAdhocMatchingGetMembers.
- [`struct pspAudioInputParams`](files/audio/pspaudio.h.md#struct-pspaudioinputparams)
- [`struct PspBufferInfo`](files/atrac3/pspatrac3.h.md#struct-pspbufferinfo)
- [`struct PspGeBreakParam`](files/ge/pspge.h.md#struct-pspgebreakparam) – Drawing queue interruption parameter.
- [`struct PspGeCallbackData`](files/ge/pspge.h.md#struct-pspgecallbackdata) – Structure to hold the callback data.
- [`struct PspGeContext`](files/ge/pspge.h.md#struct-pspgecontext) – Stores the state of the GE.
- [`struct PspGeListArgs`](files/ge/pspge.h.md#struct-pspgelistargs)
- [`struct PspGeStack`](files/ge/pspge.h.md#struct-pspgestack) – Structure storing a stack (for CALL/RET).
- [`struct PspIoDrv`](files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrv)
- [`struct PspIoDrvArg`](files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvarg) – Structure passed to the init and exit functions of the io driver system.
- [`struct PspIoDrvFileArg`](files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvfilearg) – Structure passed to the file functions of the io driver system.
- [`struct PspIoDrvFuncs`](files/kernel/pspiofilemgr_kernel.h.md#struct-pspiodrvfuncs) – Structure to maintain the file driver pointers.
- [`struct PspModuleExport`](files/sdk/fixup.c.md#struct-pspmoduleexport)
- [`struct PspOpenPSID`](files/openpsid/pspopenpsid.h.md#struct-pspopenpsid)
- [`struct PspPartitionData`](files/kernel/pspsysmem_kernel.h.md#struct-psppartitiondata)
- [`struct PspSysEventHandler`](files/kernel/pspsysevent.h.md#struct-pspsyseventhandler)
- [`struct PspSysMemPartition`](files/kernel/pspsysmem_kernel.h.md#struct-pspsysmempartition)
- [`struct pspThreadData`](files/libpthreadglue/osal.c.md#struct-pspthreaddata)
- [`struct pspUmdInfo`](files/umd/pspumd.h.md#struct-pspumdinfo) – UMD Info struct.
- [`struct PspUsbCamSetupMicExParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupmicexparam)
- [`struct PspUsbCamSetupMicParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupmicparam)
- [`struct PspUsbCamSetupStillExParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupstillexparam) – Structure for sceUsbCamSetupStillEx.
- [`struct PspUsbCamSetupStillParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupstillparam) – Structure for sceUsbCamSetupStill.
- [`struct PspUsbCamSetupVideoExParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupvideoexparam)
- [`struct PspUsbCamSetupVideoParam`](files/usb/pspusbcam.h.md#struct-pspusbcamsetupvideoparam)
- [`struct pspUtilityDialogCommon`](files/utility/psputility.h.md#struct-psputilitydialogcommon)
- [`struct pspUtilityHtmlViewerParam`](files/utility/psputility_htmlviewer.h.md#struct-psputilityhtmlviewerparam)
- [`struct pspUtilityNetconfAdhoc`](files/utility/psputility_netconf.h.md#struct-psputilitynetconfadhoc)
- [`struct PspUtilitySavedataFileData`](files/utility/psputility_savedata.h.md#struct-psputilitysavedatafiledata)
- [`struct PspUtilitySavedataListSaveNewData`](files/utility/psputility_savedata.h.md#struct-psputilitysavedatalistsavenewdata)
- [`struct PspUtilitySavedataSFOParam`](files/utility/psputility_savedata.h.md#struct-psputilitysavedatasfoparam) – title, savedataTitle, detail: parts of the unencrypted SFO data, it contains what the VSH and standard load screen shows
- [`struct PspUtilitySavedataSizeEntry`](files/utility/psputility_savedata.h.md#struct-psputilitysavedatasizeentry)
- [`struct PspUtilitySavedataSizeInfo`](files/utility/psputility_savedata.h.md#struct-psputilitysavedatasizeinfo)
- [`struct pspvfpu_context`](files/vfpu/pspvfpu.c.md#struct-pspvfpu_context)
- [`struct ptpStatStruct`](files/net/pspnet_adhoc.h.md#struct-ptpstatstruct) – PTP status structure.
- [`struct rawarc`](files/prof/prof.c.md#struct-rawarc) – frompc -> selfpc graph
- [`struct RegParam`](files/registry/pspreg.h.md#struct-regparam) – Struct used to open a registry.
- [`struct SceBootCallback`](files/kernel/pspinit.h.md#struct-scebootcallback) – This structure represents a boot callback belonging to a module.
- [`struct SceCipherKey`](files/kernel/pspamctrl.h.md#struct-scecipherkey)
- [`struct SceCtrlData`](files/ctrl/pspctrl.h.md#struct-scectrldata) – Controller data.
- [`struct SceCtrlLatch`](files/ctrl/pspctrl.h.md#struct-scectrllatch) – Controller latch data.
- [`struct SceDevctlCmd`](files/user/pspiofilemgr_devctl.h.md#struct-scedevctlcmd)
- [`struct SceDevInf`](files/user/pspiofilemgr_devctl.h.md#struct-scedevinf)
- [`struct SceFontCache`](files/font/pspfont.h.md#struct-scefontcache) – Font cache data.
- [`struct SceFontCharacterData`](files/font/pspfont.h.md#struct-scefontcharacterdata) – Fixed-point info about singular characters.
- [`struct SceFontCharacterDataFloat`](files/font/pspfont.h.md#struct-scefontcharacterdatafloat) – Floating-point info about singular characters.
- [`struct SceFontCharacterInfo`](files/font/pspfont.h.md#struct-scefontcharacterinfo) – All the information regarding a single character.
- [`struct SceFontImageBuffer`](files/font/pspfont.h.md#struct-scefontimagebuffer) – Buffer of the image containing a font.
- [`struct SceFontInfo`](files/font/pspfont.h.md#struct-scefontinfo) – General font info.
- [`struct SceFontLibData`](files/font/pspfont.h.md#struct-scefontlibdata) – Info about a specific font.
- [`struct SceFontRect`](files/font/pspfont.h.md#struct-scefontrect) – Rectangular size of the font images.
- [`struct SceFontStyle`](files/font/pspfont.h.md#struct-scefontstyle) – Font style info.
- [`struct SceGameInfo`](files/kernel/pspsysmem_kernel.h.md#struct-scegameinfo)
- [`struct SceGeStack`](files/ge/pspge.h.md#struct-scegestack) – Structure storing a stack (for CALL/RET)
- [`struct SceInit`](files/kernel/pspinit.h.md#struct-sceinit) – This structure represents an Init control block.
- [`struct SceIoDirent`](files/user/pspiofilemgr_dirent.h.md#struct-sceiodirent) – Describes a single directory entry.
- [`struct SceIoFatDirentPrivate`](files/user/pspiofilemgr_dirent.h.md#struct-sceiofatdirentprivate)
- [`struct SceIoStat`](files/user/pspiofilemgr_stat.h.md#struct-sceiostat) – Structure to hold the status information about a file.
- [`struct SceKermitCommand`](files/kermit/pspkermit.h.md#struct-scekermitcommand)
- [`struct SceKermitInterrupt`](files/kermit/pspkermit.h.md#struct-scekermitinterrupt)
- [`struct SceKermitRequest`](files/kermit/pspkermit.h.md#struct-scekermitrequest)
- [`struct SceKermitResponse`](files/kermit/pspkermit.h.md#struct-scekermitresponse)
- [`struct SceKernelAlarmInfo`](files/user/pspthreadman.h.md#struct-scekernelalarminfo) – Struct containing alarm info.
- [`struct SceKernelCallbackInfo`](files/user/pspthreadman.h.md#struct-scekernelcallbackinfo) – Structure to hold the status information for a callback.
- [`struct SceKernelEventFlagInfo`](files/user/pspthreadman.h.md#struct-scekerneleventflaginfo) – Structure to hold the event flag information.
- [`struct SceKernelEventFlagOptParam`](files/user/pspthreadman.h.md#struct-scekerneleventflagoptparam)
- [`struct SceKernelFplInfo`](files/user/pspthreadman.h.md#struct-scekernelfplinfo) – Fixed pool status information.
- [`struct SceKernelFplOptParam`](files/user/pspthreadman.h.md#struct-scekernelfploptparam)
- [`struct SceKernelLMOption`](files/user/pspmodulemgr.h.md#struct-scekernellmoption)
- [`struct SceKernelLoadExecParam`](files/user/psploadexec.h.md#struct-scekernelloadexecparam) – Structure to pass to loadexec.
- [`struct SceKernelLoadExecVSHParam`](files/kernel/psploadexec_kernel.h.md#struct-scekernelloadexecvshparam) – Structure for LoadExecVSH\* functions.
- [`struct SceKernelMbxInfo`](files/user/pspthreadman.h.md#struct-scekernelmbxinfo) – Current state of a messagebox.
- [`struct SceKernelMbxOptParam`](files/user/pspthreadman.h.md#struct-scekernelmbxoptparam) – Additional options used when creating messageboxes.
- [`struct SceKernelModuleInfo`](files/user/pspmodulemgr.h.md#struct-scekernelmoduleinfo)
- [`struct SceKernelMppInfo`](files/user/pspthreadman.h.md#struct-scekernelmppinfo) – Message Pipe status info.
- [`struct SceKernelMsgPacket`](files/user/pspthreadman.h.md#struct-scekernelmsgpacket) – Header for a message box packet.
- [`struct SceKernelSemaInfo`](files/user/pspthreadman.h.md#struct-scekernelsemainfo) – Current state of a semaphore.
- [`struct SceKernelSemaOptParam`](files/user/pspthreadman.h.md#struct-scekernelsemaoptparam) – Additional options used when creating semaphores.
- [`struct SceKernelSMOption`](files/user/pspmodulemgr.h.md#struct-scekernelsmoption)
- [`struct SceKernelSysClock`](files/user/pspthreadman.h.md#struct-scekernelsysclock) – 64-bit system clock type.
- [`struct SceKernelSystemStatus`](files/user/pspthreadman.h.md#struct-scekernelsystemstatus) – Structure to contain the system status returned by [sceKernelReferSystemStatus](files/user/pspthreadman.h.md#scekernelrefersystemstatus).
- [`struct SceKernelThreadEventHandlerInfo`](files/user/pspthreadman.h.md#struct-scekernelthreadeventhandlerinfo) – Struct for event handler info.
- [`struct SceKernelThreadInfo`](files/user/pspthreadman.h.md#struct-scekernelthreadinfo) – Structure to hold the status information for a thread.
- [`struct SceKernelThreadKInfo`](files/kernel/pspthreadman_kernel.h.md#struct-scekernelthreadkinfo) – Structure to hold the status information for a thread (kernel form) 1.5 form.
- [`struct SceKernelThreadOptParam`](files/user/pspthreadman.h.md#struct-scekernelthreadoptparam) – Additional options used when creating threads.
- [`struct SceKernelThreadRunStatus`](files/user/pspthreadman.h.md#struct-scekernelthreadrunstatus) – Statistics about a running thread.
- [`struct SceKernelTimeval`](files/user/psputils.h.md#struct-scekerneltimeval) – This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.
- [`struct SceKernelVplInfo`](files/user/pspthreadman.h.md#struct-scekernelvplinfo) – Variable pool status info.
- [`struct SceKernelVplOptParam`](files/user/pspthreadman.h.md#struct-scekernelvploptparam)
- [`struct SceKernelVTimerInfo`](files/user/pspthreadman.h.md#struct-scekernelvtimerinfo)
- [`struct SceKernelVTimerOptParam`](files/user/pspthreadman.h.md#struct-scekernelvtimeroptparam)
- [`struct SceLibraryEntryTable`](files/kernel/psploadcore.h.md#struct-scelibraryentrytable) – Defines a library and its exported functions and variables.
- [`struct SceLibraryStubTable`](files/kernel/psploadcore.h.md#struct-scelibrarystubtable) – Specifies a library and a set of imports from that library.
- [`struct SceLibStubEntry`](files/sdk/fixup.c.md#struct-scelibstubentry)
- [`struct SceLoadCoreBootModuleInfo`](files/kernel/psploadcore.h.md#struct-sceloadcorebootmoduleinfo)
- [`struct SceLoadCoreExecFileInfo`](files/kernel/psploadcore.h.md#struct-sceloadcoreexecfileinfo)
- [`struct SceLwMutexWorkarea`](files/user/pspthreadman.h.md#struct-scelwmutexworkarea) – Struct as workarea for lightweight mutex.
- [`struct SceMacKey`](files/kernel/pspamctrl.h.md#struct-scemackey)
- [`struct SceModule`](files/kernel/psploadcore.h.md#struct-scemodule) – Describes a loaded module in memory.
- [`struct SceModuleMgrParam`](files/kernel/pspmodulemgr_kernel.h.md#struct-scemodulemgrparam) – Structure used internally for many `sceModuleManager` module functions.
- [`struct SceMp3InitArg`](files/mp3/pspmp3.h.md#struct-scemp3initarg)
- [`struct SceMpegAu`](files/mpeg/pspmpeg.h.md#struct-scempegau)
- [`struct SceMpegAvcMode`](files/mpeg/pspmpeg.h.md#struct-scempegavcmode)
- [`struct SceMpegLLI`](files/mpeg/pspmpegbase.h.md#struct-scempeglli)
- [`struct SceMpegRingbuffer`](files/mpeg/pspmpeg.h.md#struct-scempegringbuffer)
- [`struct SceMpegYCrCbBuffer`](files/mpeg/pspmpegbase.h.md#struct-scempegycrcbbuffer)
- [`struct SceNetAdhocctlGameModeInfo`](files/net/pspnet_adhocctl.h.md#struct-scenetadhocctlgamemodeinfo)
- [`struct SceNetAdhocctlParams`](files/net/pspnet_adhocctl.h.md#struct-scenetadhocctlparams) – Params structure.
- [`struct SceNetAdhocctlPeerInfo`](files/net/pspnet_adhocctl.h.md#struct-scenetadhocctlpeerinfo) – Peer info structure.
- [`struct SceNetAdhocctlScanInfo`](files/net/pspnet_adhocctl.h.md#struct-scenetadhocctlscaninfo) – Scan info structure.
- [`union SceNetApctlInfo`](files/net/pspnet_apctl.h.md#union-scenetapctlinfo)
- [`struct SceNetInetPollfd`](files/net/pspnet_inet.h.md#struct-scenetinetpollfd)
- [`struct SceNetInetTimeval`](files/net/pspnet_inet.h.md#struct-scenetinettimeval) – This struct is needed because tv_sec size is different from what newlib expect Newlib expects 64bits for seconds and PSP expects 32bits.
- [`struct SceNetMallocStat`](files/net/pspnet.h.md#struct-scenetmallocstat)
- [`struct ScePspDateTime`](files/base/psptypes.h.md#struct-scepspdatetime)
- [`struct ScePspFColor`](files/base/psptypes.h.md#struct-scepspfcolor)
- [`struct ScePspFColorUnaligned`](files/base/psptypes.h.md#struct-scepspfcolorunaligned)
- [`struct ScePspFMatrix2`](files/base/psptypes.h.md#struct-scepspfmatrix2)
- [`struct ScePspFMatrix3`](files/base/psptypes.h.md#struct-scepspfmatrix3)
- [`struct ScePspFMatrix4`](files/base/psptypes.h.md#struct-scepspfmatrix4)
- [`struct ScePspFMatrix4Unaligned`](files/base/psptypes.h.md#struct-scepspfmatrix4unaligned)
- [`struct ScePspFQuaternion`](files/base/psptypes.h.md#struct-scepspfquaternion)
- [`struct ScePspFQuaternionUnaligned`](files/base/psptypes.h.md#struct-scepspfquaternionunaligned)
- [`struct ScePspFRect`](files/base/psptypes.h.md#struct-scepspfrect)
- [`struct ScePspFVector2`](files/base/psptypes.h.md#struct-scepspfvector2)
- [`struct ScePspFVector3`](files/base/psptypes.h.md#struct-scepspfvector3)
- [`struct ScePspFVector4`](files/base/psptypes.h.md#struct-scepspfvector4)
- [`struct ScePspFVector4Unaligned`](files/base/psptypes.h.md#struct-scepspfvector4unaligned)
- [`struct ScePspIMatrix2`](files/base/psptypes.h.md#struct-scepspimatrix2)
- [`struct ScePspIMatrix3`](files/base/psptypes.h.md#struct-scepspimatrix3)
- [`struct ScePspIMatrix4`](files/base/psptypes.h.md#struct-scepspimatrix4)
- [`struct ScePspIMatrix4Unaligned`](files/base/psptypes.h.md#struct-scepspimatrix4unaligned)
- [`struct ScePspIRect`](files/base/psptypes.h.md#struct-scepspirect)
- [`struct ScePspIVector2`](files/base/psptypes.h.md#struct-scepspivector2)
- [`struct ScePspIVector3`](files/base/psptypes.h.md#struct-scepspivector3)
- [`struct ScePspIVector4`](files/base/psptypes.h.md#struct-scepspivector4)
- [`struct ScePspL64Rect`](files/base/psptypes.h.md#struct-scepspl64rect)
- [`struct ScePspL64Vector2`](files/base/psptypes.h.md#struct-scepspl64vector2)
- [`struct ScePspL64Vector3`](files/base/psptypes.h.md#struct-scepspl64vector3)
- [`struct ScePspL64Vector4`](files/base/psptypes.h.md#struct-scepspl64vector4)
- [`union ScePspMatrix2`](files/base/psptypes.h.md#union-scepspmatrix2)
- [`union ScePspMatrix3`](files/base/psptypes.h.md#union-scepspmatrix3)
- [`union ScePspMatrix4`](files/base/psptypes.h.md#union-scepspmatrix4)
- [`struct ScePspSRect`](files/base/psptypes.h.md#struct-scepspsrect)
- [`struct ScePspSVector2`](files/base/psptypes.h.md#struct-scepspsvector2)
- [`struct ScePspSVector3`](files/base/psptypes.h.md#struct-scepspsvector3)
- [`struct ScePspSVector4`](files/base/psptypes.h.md#struct-scepspsvector4)
- [`union ScePspUnion128`](files/base/psptypes.h.md#union-scepspunion128)
- [`union ScePspUnion32`](files/base/psptypes.h.md#union-scepspunion32)
- [`union ScePspUnion64`](files/base/psptypes.h.md#union-scepspunion64)
- [`union ScePspVector2`](files/base/psptypes.h.md#union-scepspvector2)
- [`union ScePspVector3`](files/base/psptypes.h.md#union-scepspvector3)
- [`union ScePspVector4`](files/base/psptypes.h.md#union-scepspvector4)
- [`struct SceSasCore`](files/sascore/pspsascore.h.md#struct-scesascore) – Contains all data related to a sceSasCore state.
- [`struct SceSCContext`](files/kernel/pspthreadman_kernel.h.md#struct-scesccontext)
- [`struct SceSysmemPartInfo`](files/kernel/pspsysmem_kernel.h.md#struct-scesysmempartinfo)
- [`struct SceSysmemPartTable`](files/kernel/pspsysmem_kernel.h.md#struct-scesysmemparttable)
- [`struct SceThreadContext`](files/kernel/pspthreadman_kernel.h.md#struct-scethreadcontext) – Thread context Structues for the thread context taken from florinsasu's post on the forums.
- [`struct SceUtilitySavedataFileListEntry`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedatafilelistentry)
- [`struct SceUtilitySavedataFileListInfo`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedatafilelistinfo)
- [`struct SceUtilitySavedataIdListEntry`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedataidlistentry)
- [`struct SceUtilitySavedataIdListInfo`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedataidlistinfo)
- [`struct SceUtilitySavedataMsDataInfo`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedatamsdatainfo)
- [`struct SceUtilitySavedataMsFreeInfo`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedatamsfreeinfo)
- [`struct SceUtilitySavedataParam`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedataparam) – Structure to hold the parameters for the [sceUtilitySavedataInitStart](files/utility/psputility_savedata.h.md#sceutilitysavedatainitstart) function.
- [`struct SceUtilitySavedataUsedDataInfo`](files/utility/psputility_savedata.h.md#struct-sceutilitysavedatauseddatainfo)
- [`struct sircs_data`](files/sircs/pspsircs.h.md#struct-sircs_data)
- [`struct sockaddr`](files/libcglue/sys/socket.h.md#struct-sockaddr)
- [`struct sockaddr_in`](files/libcglue/netinet/in.h.md#struct-sockaddr_in)
- [`struct sockaddr_storage`](files/libcglue/sys/socket.h.md#struct-sockaddr_storage)
- [`struct StringDescriptor`](files/usb/pspusbbus.h.md#struct-stringdescriptor) – USB string descriptor.
- [`struct sw_breakpoint`](files/debug/gdb-stub.c.md#struct-sw_breakpoint)
- [`struct tag_IntrHandlerOptionParam`](files/user/pspintrman.h.md#struct-tag_intrhandleroptionparam)
- [`struct UsbConfiguration`](files/usb/pspusbbus.h.md#struct-usbconfiguration) – USB driver configuration.
- [`struct UsbData`](files/usb/pspusbbus.h.md#struct-usbdata) – Padded data structure, padding is required otherwise the USB hardware crashes.
- [`struct UsbData::ConfDesc`](files/usb/pspusbbus.h.md#struct-usbdataconfdesc)
- [`struct UsbData::Config`](files/usb/pspusbbus.h.md#struct-usbdataconfig)
- [`struct UsbData::Endp`](files/usb/pspusbbus.h.md#struct-usbdataendp)
- [`struct UsbData::InterDesc`](files/usb/pspusbbus.h.md#struct-usbdatainterdesc)
- [`struct UsbData::Interfaces`](files/usb/pspusbbus.h.md#struct-usbdatainterfaces)
- [`struct UsbdDeviceReq`](files/usb/pspusbbus.h.md#struct-usbddevicereq) – USB device request, used by [sceUsbbdReqSend](files/usb/pspusbbus.h.md#sceusbbdreqsend) and [sceUsbbdReqRecv](files/usb/pspusbbus.h.md#sceusbbdreqrecv).
- [`struct UsbDriver`](files/usb/pspusbbus.h.md#struct-usbdriver) – USB driver structure used by [sceUsbbdRegister](files/usb/pspusbbus.h.md#sceusbbdregister) and [sceUsbbdUnregister](files/usb/pspusbbus.h.md#sceusbbdunregister).
- [`struct UsbEndpoint`](files/usb/pspusbbus.h.md#struct-usbendpoint) – USB driver endpoint.
- [`struct UsbInterface`](files/usb/pspusbbus.h.md#struct-usbinterface) – USB driver interface.
- [`struct UsbInterfaces`](files/usb/pspusbbus.h.md#struct-usbinterfaces) – USB driver interfaces structure.

### Related Pages

- [Contributor Covenant Code of Conduct](pages/code-of-conduct.md)
- [Todo List](pages/todo.md)

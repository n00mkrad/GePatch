[PSPSDK documentation](../../README.md) › Files

# user/pspmoduleinfo.h

## Data Structures

### `struct _scemoduleinfo`

```c
struct _scemoduleinfo {
    unsigned short modattribute;
    unsigned char modversion[2];
    char modname[27];
    char terminal;
    void * gp_value;
    void * ent_top;
    void * ent_end;
    void * stub_top;
    void * stub_end;
};
```

## Macros

### `PSP_MODULE_INFO()`

```c
#define PSP_MODULE_INFO(name, attributes, major_version, minor_version) extern char __lib_ent_top[], __lib_ent_bottom[]; \
	extern char __lib_stub_top[], __lib_stub_bottom[]; \
	SceModuleInfo module_info \
		__attribute__((section(".rodata.sceModuleInfo"), \
			       aligned(16), unused)) = { \
	  attributes, { minor_version, major_version }, name, 0, _gp, \
	  __lib_ent_top, __lib_ent_bottom, \
	  __lib_stub_top, __lib_stub_bottom \
	}
```

### `PSP_MAIN_THREAD_PRIORITY()`

```c
#define PSP_MAIN_THREAD_PRIORITY(priority) unsigned int sce_newlib_priority = (priority)
```

### `PSP_MAIN_THREAD_STACK_SIZE_KB()`

```c
#define PSP_MAIN_THREAD_STACK_SIZE_KB(size_kb) unsigned int sce_newlib_stack_kb_size = (size_kb)
```

### `PSP_MAIN_THREAD_ATTR()`

```c
#define PSP_MAIN_THREAD_ATTR(attr) unsigned int sce_newlib_attribute = (attr)
```

### `PSP_MAIN_THREAD_ATTRIBUTE`

```c
#define PSP_MAIN_THREAD_ATTRIBUTE PSP_MAIN_THREAD_ATTR
```

### `PSP_MAIN_THREAD_PARAMS()`

```c
#define PSP_MAIN_THREAD_PARAMS(priority, size_kb, attribute) PSP_MAIN_THREAD_PRIORITY(priority); \
	PSP_MAIN_THREAD_STACK_SIZE_KB(size_kb); \
	PSP_MAIN_THREAD_ATTR(attribute)
```

### `PSP_NO_CREATE_MAIN_THREAD()`

```c
#define PSP_NO_CREATE_MAIN_THREAD() int sce_newlib_nocreate_thread_in_start = 1
```

### `PSP_HEAP_SIZE_KB()`

```c
#define PSP_HEAP_SIZE_KB(size_kb) int sce_newlib_heap_kb_size = (size_kb)
```

### `PSP_HEAP_THRESHOLD_SIZE_KB()`

```c
#define PSP_HEAP_THRESHOLD_SIZE_KB(size_kb) int sce_newlib_heap_threshold_kb_size = (size_kb)
```

### `PSP_MAIN_THREAD_NAME()`

```c
#define PSP_MAIN_THREAD_NAME(s) const char* sce_newlib_main_thread_name = (s)
```

### `PSP_DISABLE_NEWLIB()`

```c
#define PSP_DISABLE_NEWLIB() void __libcglue_init(int argc, char *argv[]) {} \
	void __libcglue_deinit() {}
```

### `PSP_DISABLE_NEWLIB_PIPE_SUPPORT()`

```c
#define PSP_DISABLE_NEWLIB_PIPE_SUPPORT() static int __pipe_not_supported() { \
		errno = ENOSYS; \
		return -1; \
	} \
	int __pipe_close(int fd) { return __pipe_not_supported(); } \
	int __pipe_nonblocking_read(int fd, void *buf, size_t len) { return __pipe_not_supported(); } \
	int __pipe_read(int fd, void *buf, size_t len) { return __pipe_not_supported(); } \
	int __pipe_write(int fd, const void *buf, size_t len) { return __pipe_not_supported(); } \
	int __pipe_nonblocking_write(int fd, const void *buf, size_t len) { return __pipe_not_supported(); }
```

### `PSP_DISABLE_NEWLIB_SOCKET_SUPPORT()`

```c
#define PSP_DISABLE_NEWLIB_SOCKET_SUPPORT() static int __socket_not_supported() { \
		errno = ENOSYS; \
		return -1; \
	} \
	int __socket_close(int sock) { return __socket_not_supported(); } \
	ssize_t	recv(int s, void *buf, size_t len, int flags) { return __socket_not_supported(); } \
	ssize_t	send(int s, const void *buf, size_t len, int flags) { return __socket_not_supported(); } \
	int	setsockopt(int s, int level, int optname, const void *optval, socklen_t optlen) { return __socket_not_supported(); }
```

### `PSP_DISABLE_NEWLIB_TIMEZONE_SUPPORT()`

```c
#define PSP_DISABLE_NEWLIB_TIMEZONE_SUPPORT() void __timezone_update() { }
```

### `PSP_DISABLE_NEWLIB_CWD_SUPPORT()`

```c
#define PSP_DISABLE_NEWLIB_CWD_SUPPORT() void __init_cwd(char *argv_0) {}
```

### `PSP_DISABLE_AUTOSTART_PTHREAD()`

```c
#define PSP_DISABLE_AUTOSTART_PTHREAD() void __libpthreadglue_init() {}
```

## Typedefs

### `_sceModuleInfo`

```c
typedef struct _scemoduleinfo _sceModuleInfo;
```

### `SceModuleInfo`

```c
typedef const _sceModuleInfo SceModuleInfo;
```

## Enumerations

### `enum PspModuleInfoAttr`

| Enumerator | Value | Description |
|---|---|---|
| `PSP_MODULE_USER` | `0` |  |
| `PSP_MODULE_NO_STOP` | `0x0001` |  |
| `PSP_MODULE_SINGLE_LOAD` | `0x0002` |  |
| `PSP_MODULE_SINGLE_START` | `0x0004` |  |
| `PSP_MODULE_KERNEL` | `0x1000` |  |

## Variables

### `_gp`

```c
char _gp[][];
```

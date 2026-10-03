[PSPSDK documentation](../../README.md) › Files

# libcglue/fdman.h

```c
#include <sys/types.h>
```

## Data Structures

### `struct __descriptormap_type`

```c
struct __descriptormap_type {
    uint32_t descriptor;
    uint32_t flags;
    uint32_t ref_count;
    char * filename;
    uint8_t type;
};
```

## Macros

### `__FILENO_MAX`

```c
#define __FILENO_MAX 1024
```

### `__IS_FD_VALID()`

```c
#define __IS_FD_VALID(FD) ( (FD >= 0) && (FD < __FILENO_MAX) && (__descriptormap[FD] != NULL) )
```

### `__IS_FD_OF_TYPE()`

```c
#define __IS_FD_OF_TYPE(FD, TYPE) ( (__IS_FD_VALID(FD)) && (__descriptormap[FD]->type == TYPE) )
```

## Enumerations

### `enum __fdman_fd_types`

| Enumerator | Description |
|---|---|
| `__DESCRIPTOR_TYPE_FILE` |  |
| `__DESCRIPTOR_TYPE_FOLDER` |  |
| `__DESCRIPTOR_TYPE_PIPE` |  |
| `__DESCRIPTOR_TYPE_SOCKET` |  |
| `__DESCRIPTOR_TYPE_TTY` |  |

## Functions

### `__fdman_init()`

```c
void __fdman_init();
```

### `__fdman_get_new_descriptor()`

```c
int __fdman_get_new_descriptor();
```

### `__fdman_get_dup_descriptor()`

```c
int __fdman_get_dup_descriptor(int fd);
```

### `__fdman_release_descriptor()`

```c
void __fdman_release_descriptor(int fd);
```

## Variables

### `__descriptormap`

```c
__descriptormap_type* __descriptormap[1024][1024];
```

[PSPSDK documentation](../../README.md) › Files

# sircs/pspsircs.h

Topics: [Integrated Remote Control System Library](../../topics/Sony.md)

## Data Structures

### `struct sircs_data`

```c
struct sircs_data {
    u8 type;
    u8 cmd;
    u16 dev;
};
```

## Functions

### `sceSircsSend()`

```c
int sceSircsSend(struct sircs_data *sd, int count);
```

## Variables

### `__packed__`

```c
struct sircs_data __packed__;
```

[PSPSDK documentation](../../README.md) › Files

# prof/pspprof.h

## Functions

### `gprof_start()`

```c
void gprof_start(void);
```

Start the profiler.

If the profiler is already running, this function stop previous one, and ignore the result. Finally, it initializes a new profiler session.

### `gprof_stop()`

```c
void gprof_stop(const char *filename, int should_dump);
```

Stop the profiler.

If the profiler is not running, this function does nothing.

**Parameters:**

- `filename` – The name of the file to write the profiling data to.
- `should_dump` – If 1, the profiling data will be written to the file. If 0, the profiling data will be discarded.

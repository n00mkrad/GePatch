[PSPSDK documentation](../../README.md) › Files

# usb/pspusbbus.h

## Data Structures

### `struct UsbInterface`

USB driver interface.

| Field | Description |
|---|---|
| `int expect_interface` | Expectant interface (0 or -1) |
| `int unk8` | Unknown. |
| `int num_interface` | Number of interfaces. |

### `struct UsbEndpoint`

USB driver endpoint.

| Field | Description |
|---|---|
| `int endpnum` | Endpoint number (must be filled in sequentially) |
| `int unk2` | Filled in by the bus driver. |
| `int unk3` | Filled in by the bus driver. |

### `struct StringDescriptor`

USB string descriptor.

```c
struct StringDescriptor {
    unsigned char bLength;
    unsigned char bDescriptorType;
    short bString[32];
};
```

### `struct DeviceDescriptor`

USB device descriptor.

```c
struct DeviceDescriptor {
    unsigned char bLength;
    unsigned char bDescriptorType;
    unsigned short bcdUSB;
    unsigned char bDeviceClass;
    unsigned char bDeviceSubClass;
    unsigned char bDeviceProtocol;
    unsigned char bMaxPacketSize;
    unsigned short idVendor;
    unsigned short idProduct;
    unsigned short bcdDevice;
    unsigned char iManufacturer;
    unsigned char iProduct;
    unsigned char iSerialNumber;
    unsigned char bNumConfigurations;
};
```

### `struct ConfigDescriptor`

USB configuration descriptor.

```c
struct ConfigDescriptor {
    unsigned char bLength;
    unsigned char bDescriptorType;
    unsigned short wTotalLength;
    unsigned char bNumInterfaces;
    unsigned char bConfigurationValue;
    unsigned char iConfiguration;
    unsigned char bmAttributes;
    unsigned char bMaxPower;
};
```

### `struct InterfaceDescriptor`

USB Interface descriptor.

```c
struct InterfaceDescriptor {
    unsigned char bLength;
    unsigned char bDescriptorType;
    unsigned char bInterfaceNumber;
    unsigned char bAlternateSetting;
    unsigned char bNumEndpoints;
    unsigned char bInterfaceClass;
    unsigned char bInterfaceSubClass;
    unsigned char bInterfaceProtocol;
    unsigned char iInterface;
};
```

### `struct EndpointDescriptor`

USB endpoint descriptor.

```c
struct EndpointDescriptor {
    unsigned char bLength;
    unsigned char bDescriptorType;
    unsigned char bEndpointAddress;
    unsigned char bmAttributes;
    unsigned short wMaxPacketSize;
    unsigned char bInterval;
};
```

### `struct UsbInterfaces`

USB driver interfaces structure.

| Field | Description |
|---|---|
| `struct InterfaceDescriptor * infp[2]` | Pointers to the individual interface descriptors. |
| `unsigned int num` | Number of interface descriptors. |

### `struct UsbConfiguration`

USB driver configuration.

| Field | Description |
|---|---|
| `struct ConfigDescriptor * confp` | Pointer to the configuration descriptors. |
| `struct UsbInterfaces * infs` | USB driver interfaces pointer. |
| `struct InterfaceDescriptor * infp` | Pointer to the first interface descriptor. |
| `struct EndpointDescriptor * endp` | Pointer to the first endpoint descriptor (each should be 16byte aligned) |

### `struct UsbData`

Padded data structure, padding is required otherwise the USB hardware crashes.

```c
struct UsbData {
    unsigned char devdesc[20];
    struct UsbData::Config config;
    struct UsbData::ConfDesc confdesc;
    unsigned char pad1[8];
    struct UsbData::Interfaces interfaces;
    struct UsbData::InterDesc interdesc;
    struct UsbData::Endp endp[4];
};
```

Nested types: [`UsbData::ConfDesc`](#struct-usbdataconfdesc), [`UsbData::Config`](#struct-usbdataconfig), [`UsbData::Endp`](#struct-usbdataendp), [`UsbData::InterDesc`](#struct-usbdatainterdesc), [`UsbData::Interfaces`](#struct-usbdatainterfaces)

### `struct UsbData::Config`

```c
struct Config {
    void * pconfdesc;
    void * pinterfaces;
    void * pinterdesc;
    void * pendp;
};
```

### `struct UsbData::ConfDesc`

```c
struct ConfDesc {
    unsigned char desc[12];
    void * pinterfaces;
};
```

### `struct UsbData::Interfaces`

```c
struct Interfaces {
    void * pinterdesc[2];
    unsigned int intcount;
};
```

### `struct UsbData::InterDesc`

```c
struct InterDesc {
    unsigned char desc[12];
    void * pendp;
    unsigned char pad[32];
};
```

### `struct UsbData::Endp`

```c
struct Endp {
    unsigned char desc[16];
};
```

### `struct DeviceRequest`

USB EP0 Device Request.

```c
struct DeviceRequest {
    unsigned char bmRequestType;
    unsigned char bRequest;
    unsigned short wValue;
    unsigned short wIndex;
    unsigned short wLength;
};
```

### `struct UsbDriver`

USB driver structure used by [sceUsbbdRegister](#sceusbbdregister) and [sceUsbbdUnregister](#sceusbbdunregister).

| Field | Description |
|---|---|
| `const char * name` | Name of the USB driver. |
| `int endpoints` | Number of endpoints in this driver (including default control) |
| `struct UsbEndpoint * endp` | List of endpoint structures (used when calling other functions) |
| `struct UsbInterface * intp` | Interface list. |
| `void * devp_hi` | Pointer to hi-speed device descriptor. |
| `void * confp_hi` | Pointer to hi-speed device configuration. |
| `void * devp` | Pointer to full-speed device descriptor. |
| `void * confp` | Pointer to full-speed device configuration. |
| `struct StringDescriptor * str` | Default String descriptor. |
| `int(* recvctl)(int arg1, int arg2, struct DeviceRequest *req)` | Received a control request arg0 is endpoint, arg1 is possibly data arg2 is data buffer. |
| `int(* func28)(int arg1, int arg2, int arg3)` | Unknown. |
| `int(* attach)(int speed, void *arg2, void *arg3)` | Configuration set (attach) function. |
| `int(* detach)(int arg1, int arg2, int arg3)` | Configuration unset (detach) function. |
| `int unk34` | Unknown set to 0. |
| `int(* start_func)(int size, void *args)` | Function called when the driver is started. |
| `int(* stop_func)(int size, void *args)` | Function called when the driver is stopped. |
| `struct UsbDriver * link` | Link to next USB driver in the chain, set to NULL. |

### `struct UsbdDeviceReq`

USB device request, used by [sceUsbbdReqSend](#sceusbbdreqsend) and [sceUsbbdReqRecv](#sceusbbdreqrecv).

| Field | Description |
|---|---|
| `struct UsbEndpoint * endp` | Pointer to the endpoint to queue request on. |
| `void * data` | Pointer to the data buffer to use in the request. |
| `int size` | Size of the data buffer (send == size of data, recv == size of max receive) |
| `int unkc` | Unknown. |
| `void * func` | Pointer to the function to call on completion. |
| `int recvsize` | Resultant size (send == size of data sent, recv == size of data received) |
| `int retcode` | Return code of the request, 0 == success, -3 == cancelled. |
| `int unk1c` | Unknown. |
| `void * arg` | A user specified pointer for the device request. |
| `void * link` | Link pointer to next request used by the driver, set it to NULL. |

## Functions

### `sceUsbbdRegister()`

```c
int sceUsbbdRegister(struct UsbDriver *drv);
```

Register a USB driver.

**Parameters:**

- `drv` – Pointer to a filled out USB driver

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdUnregister()`

```c
int sceUsbbdUnregister(struct UsbDriver *drv);
```

Unregister a USB driver.

**Parameters:**

- `drv` – Pointer to a filled out USB driver

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdClearFIFO()`

```c
int sceUsbbdClearFIFO(struct UsbEndpoint *endp);
```

Clear the FIFO on an endpoint.

**Parameters:**

- `endp` – The endpoint to clear

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdReqCancelAll()`

```c
int sceUsbbdReqCancelAll(struct UsbEndpoint *endp);
```

Cancel any pending requests on an endpoint.

**Parameters:**

- `endp` – The endpoint to cancel

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdStall()`

```c
int sceUsbbdStall(struct UsbEndpoint *endp);
```

Stall an endpoint.

**Parameters:**

- `endp` – The endpoint to stall

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdReqSend()`

```c
int sceUsbbdReqSend(struct UsbdDeviceReq *req);
```

Queue a send request (IN from host pov)

**Parameters:**

- `req` – Pointer to a filled out [UsbdDeviceReq](#struct-usbddevicereq) structure.

**Returns:** 0 on success, \< 0 on error

### `sceUsbbdReqRecv()`

```c
int sceUsbbdReqRecv(struct UsbdDeviceReq *req);
```

Queue a receive request (OUT from host pov)

**Parameters:**

- `req` – Pointer to a filled out [UsbdDeviceReq](#struct-usbddevicereq) structure

**Returns:** 0 on success, \< 0 on error

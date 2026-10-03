[PSPSDK documentation](../../README.md) › Files

# gum/pspgum.h

```c
#include <psptypes.h>
```

## Functions

### `sceGumDrawArray()`

```c
void sceGumDrawArray(int prim, int vtype, int count, const void *indices, const void *vertices);
```

### `sceGumDrawArrayN()`

```c
void sceGumDrawArrayN(int prim, int vtype, int count, int a3, const void *indices, const void *vertices);
```

### `sceGumDrawBezier()`

```c
void sceGumDrawBezier(int vtype, int ucount, int vcount, const void *indices, const void *vertices);
```

### `sceGumDrawSpline()`

```c
void sceGumDrawSpline(int vtype, int ucount, int vcount, int uedge, int vedge, const void *indices, const void *vertices);
```

### `sceGumLoadIdentity()`

```c
void sceGumLoadIdentity(void);
```

Load identity matrix.

\[1 0 0 0\] \[0 1 0 0\] \[0 0 1 0\] \[0 0 0 1\]

### `sceGumLoadMatrix()`

```c
void sceGumLoadMatrix(const ScePspFMatrix4 *m);
```

Load matrix.

**Parameters:**

- `m` – Matrix to load into stack

### `sceGumLookAt()`

```c
void sceGumLookAt(ScePspFVector3 *eye, ScePspFVector3 *center, ScePspFVector3 *up);
```

### `sceGumMatrixMode()`

```c
void sceGumMatrixMode(int mode);
```

Select which matrix stack to operate on.

Available matrix modes are:

- GU_PROJECTION
- GU_VIEW
- GU_MODEL
- GU_TEXTURE

**Parameters:**

- `mode` – Matrix mode to use

### `sceGumMultMatrix()`

```c
void sceGumMultMatrix(const ScePspFMatrix4 *m);
```

Multiply current matrix with input.

**Parameters:**

- `m` – Matrix to multiply stack with

### `sceGumOrtho()`

```c
void sceGumOrtho(float left, float right, float bottom, float top, float near, float far);
```

Apply ortho projection matrix.

**Note:** The matrix loses its orthonogal status after executing this function.

### `sceGumPerspective()`

```c
void sceGumPerspective(float fovy, float aspect, float near, float far);
```

Apply perspective projection matrix.

**Note:** The matrix loses its orthonogal status after executing this function.

### `sceGumPopMatrix()`

```c
void sceGumPopMatrix(void);
```

Pop matrix from stack.

### `sceGumPushMatrix()`

```c
void sceGumPushMatrix(void);
```

Push current matrix onto stack.

### `sceGumRotateX()`

```c
void sceGumRotateX(float angle);
```

Rotate around the X axis.

**Parameters:**

- `angle` – Angle in radians

### `sceGumRotateY()`

```c
void sceGumRotateY(float angle);
```

Rotate around the Y axis.

**Parameters:**

- `angle` – Angle in radians

### `sceGumRotateZ()`

```c
void sceGumRotateZ(float angle);
```

Rotate around the Z axis.

**Parameters:**

- `angle` – Angle in radians

### `sceGumRotateXYZ()`

```c
void sceGumRotateXYZ(const ScePspFVector3 *v);
```

Rotate around all 3 axis in order X, Y, Z.

**Parameters:**

- `v` – Pointer to vector containing angles

### `sceGumRotateZYX()`

```c
void sceGumRotateZYX(const ScePspFVector3 *v);
```

Rotate around all 3 axis in order Z, Y, X.

**Parameters:**

- `v` – Pointer to vector containing angles

### `sceGumRotate()`

```c
void sceGumRotate(const ScePspFQuaternion *q);
```

Apply rotation represented by quaternion q.

**Parameters:**

- `q` – Pointer to quaternion

### `sceGumScale()`

```c
void sceGumScale(const ScePspFVector3 *v);
```

Scale matrix.

**Note:** The matrix loses its orthonogal status after executing this function.

### `sceGumStoreMatrix()`

```c
void sceGumStoreMatrix(ScePspFMatrix4 *m);
```

Store current matrix in the stack.

**Parameters:**

- `m` – Matrix to write result to

### `sceGumTranslate()`

```c
void sceGumTranslate(const ScePspFVector3 *v);
```

Translate coordinate system.

**Parameters:**

- `v` – Translation coordinates

### `sceGumUpdateMatrix()`

```c
void sceGumUpdateMatrix(void);
```

Explicitly flush dirty matrices to the hardware.

### `sceGumFullInverse()`

```c
void sceGumFullInverse();
```

Invert 4x4 matrix.

This invert algorithm can operate on matrices that are not orthongal (See [sceGumFastInverse()](#scegumfastinverse))

### `sceGumFastInverse()`

```c
void sceGumFastInverse();
```

Invert orthonogal 4x4 matrix.

Note that the matrix in the stack has to be orthonogal (that is, all rotational axises must be unit length & orthonogal against the others), otherwise the result of the function cannot be depended on. If you need to invert a matrix that is not orthonogal, use [sceGumFullInverse()](#scegumfullinverse).

### `sceGumBeginObject()`

```c
void sceGumBeginObject(int vtype, int count, const void *indices, const void *vertices);
```

Stack-aware version of [sceGuBeginObject()](../gu/pspgu.h.md#scegubeginobject) (look in [pspgu.h](../gu/pspgu.h.md) for description)

**Note:** NOT YET IMPLEMENTED

**Parameters:**

- `vtype` – Vertex type to process
- `count` – Number of vertices to test
- `indices` – Optional index-list
- `vertices` – Vertex-list

### `sceGumEndObject()`

```c
void sceGumEndObject();
```

Stack-aware version of [sceGuEndObject()](../gu/pspgu.h.md#sceguendobject)

**Note:** NOT YET IMPLEMENTED

### `gumInit()`

```c
void gumInit(void);
```

### `gumLoadIdentity()`

```c
void gumLoadIdentity(ScePspFMatrix4 *m);
```

Load matrix with identity.

**Parameters:**

- `m` – Matrix to load with identity

### `gumLoadQuaternion()`

```c
void gumLoadQuaternion(ScePspFMatrix4 *r, const ScePspFQuaternion *q);
```

### `gumLoadMatrix()`

```c
void gumLoadMatrix(ScePspFMatrix4 *r, const ScePspFMatrix4 *a);
```

### `gumLookAt()`

```c
void gumLookAt(ScePspFMatrix4 *m, ScePspFVector3 *eye, ScePspFVector3 *center, ScePspFVector3 *up);
```

### `gumMultMatrix()`

```c
void gumMultMatrix(ScePspFMatrix4 *result, const ScePspFMatrix4 *a, const ScePspFMatrix4 *b);
```

### `gumOrtho()`

```c
void gumOrtho(ScePspFMatrix4 *m, float left, float right, float bottom, float top, float near, float far);
```

### `gumPerspective()`

```c
void gumPerspective(ScePspFMatrix4 *m, float fovy, float aspect, float near, float far);
```

### `gumRotateX()`

```c
void gumRotateX(ScePspFMatrix4 *m, float angle);
```

### `gumRotateXYZ()`

```c
void gumRotateXYZ(ScePspFMatrix4 *m, const ScePspFVector3 *v);
```

### `gumRotateY()`

```c
void gumRotateY(ScePspFMatrix4 *m, float angle);
```

### `gumRotateZ()`

```c
void gumRotateZ(ScePspFMatrix4 *m, float angle);
```

### `gumRotateZYX()`

```c
void gumRotateZYX(ScePspFMatrix4 *m, const ScePspFVector3 *v);
```

### `gumRotateMatrix()`

```c
void gumRotateMatrix(ScePspFMatrix4 *m, const ScePspFQuaternion *q);
```

### `gumScale()`

```c
void gumScale(ScePspFMatrix4 *m, const ScePspFVector3 *v);
```

### `gumTranslate()`

```c
void gumTranslate(ScePspFMatrix4 *m, const ScePspFVector3 *v);
```

### `gumFullInverse()`

```c
void gumFullInverse(ScePspFMatrix4 *r, const ScePspFMatrix4 *a);
```

### `gumFastInverse()`

```c
void gumFastInverse(ScePspFMatrix4 *r, const ScePspFMatrix4 *a);
```

Invert orthonogal 4x4 matrix.

Note that the matrix in the stack has to be orthonogal (that is, all rotational axises must be unit length & orthonogal against the others), otherwise the result of the function cannot be depended on. If you need to invert a matrix that is not orthonogal, use [gumFullInverse()](#gumfullinverse).

**Parameters:**

- `r` – Matrix receiving result
- `a` – Orthonogal matrix that is to be inverted

### `gumCrossProduct()`

```c
void gumCrossProduct(ScePspFVector3 *r, const ScePspFVector3 *a, const ScePspFVector3 *b);
```

### `gumDotProduct()`

```c
float gumDotProduct(const ScePspFVector3 *a, const ScePspFVector3 *b);
```

### `gumNormalize()`

```c
void gumNormalize(ScePspFVector3 *v);
```

### `gumRotateVector()`

```c
void gumRotateVector(ScePspFVector3 *r, const ScePspFQuaternion *q, const ScePspFVector3 *v);
```

### `gumNormalizeQuaternion()`

```c
void gumNormalizeQuaternion(ScePspFQuaternion *q);
```

### `gumLoadAxisAngle()`

```c
void gumLoadAxisAngle(ScePspFQuaternion *r, ScePspFVector3 *axis, float t);
```

### `gumMultQuaternion()`

```c
void gumMultQuaternion(ScePspFQuaternion *result, const ScePspFQuaternion *a, const ScePspFQuaternion *b);
```

# Compile a C program using `icc`

[icc](icc.md) is the Intel C [compiler](compilers.md).
This page describes how to compile C code using `icc`.

## Procedure

### 1. Load an `intel` module

For version of the Intel compiler to and including 2020,
load an `intel` module with a version having two digits,
from 15 to and including 20:

```bash
module load intel/20.4
```

C11 and C17 (bug fix) standards have support from intel/17+ (fully from 19).

### 2. 

Create and write a C source file called `hello_world.c`:

```bash
nano hello_world.c
```

In [nano](nano.md), write the C program as such:

```c
#include <stdio.h>

int main() {
  printf("hello, world\n");
}
```

After saving and closing nano, compile as such:

```bash
icc hello_world.c
```

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

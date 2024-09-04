# Compile a C program using `icx`

[icx](icx.md) is an Intel C [compiler](compilers.md).
This page describes how to compile C code using `icx`.

## Procedure

### 1. Load the modules

load an these modules:

``` console
module load intel-oneapi 
module load compiler/2023.1.0
```

### 2. Write the C program

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

### 3. Compile the C program

After saving and closing nano, compile as such:

```bash
icx hello_world.c
```

### 4. Run the executable

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

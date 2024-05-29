# Compile a C program using `icc`

[icc](icc.md) is the Intel C [compiler](compilers.md).
This page describes how to compile C code using the GCC.

## Procedure

### 1. Load an `intel` module

For version of the Intel compiler to and including 2020,
load an `intel` module :

```bash
module load intel/20.4
```

For newer Intel versions (2021-, see above):

``` console
module load intel-oneapi compiler
module load compiler/2023.1.0
```



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

## Other


and then compile with the command icc, or icx:

``` console
$ icc -o hello hello.c
```

or for newer versions:

``` console
$ icx -o hello hello.c
```

To run, enter:

``` console
$ ./hello
hello, world
```

c11 and c17 (bug fix) standards have support from intel/17+ (fully from 19).

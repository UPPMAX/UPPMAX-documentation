# Compile C using GCC

[GCC](gcc.md) (shorthand for 'GNU Compiler Collection')
is a collection of [compilers](compilers.md)
able to compile multiple different programming languages.

This page describes how to compile C code using the GCC.

## Procedure

### 0. Create a C source file

You will need C code to work on.

In this optional step, a file with a minimal C program is created.

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

### 1. Load a GCC module

Load a recent GCC module:

```bash
module load gcc/13.2.0
```

???- question "Do I really need to load a module?"

    No, as there is a system-installed GCC.

    For sake of doing reproducible research,
    always load a module of a specific version.

If you need the C11 or C17 standards, use these module versions or newer:

Module version|Description
--------------|------------------------------
`gcc/4.8`     |Fully implemented C11 standard
`gcc/8`       |Fully implemented C17 standard

### 2. Compile the source file

After saving and closing nano, compile as such:

```bash
gcc hello_world.c
```

This compiles the file `hello_world.c` using all defaults:

- default/no optimization
- the executable created is called `a.out`

To compiles the file `hello_world.c` with run-time speed optimization
and creating an executable with a more sensible name, use:

```bash
gcc -O3 -o hello_world hello_world.c
```

- `-O3`: optimize for run-time speed
- `-o hello_world`: the executable created is called `hello_world`

### 3. Run

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

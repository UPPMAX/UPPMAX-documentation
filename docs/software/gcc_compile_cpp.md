# Compile C++ using GCC

[GCC](gcc.md) (shorthand for 'GNU Compiler Collection')
is a collection of [compilers](compilers.md)
able to compile multiple different programming languages.

This page describes how to compile C++ code using the GCC.

## Procedure

### 0. Create a C++ source file

You will need C++ code to work on.

In this optional step, a file with a minimal C++ program is created.

Create and write a C++ source file called `hello_world.cpp`:

```bash
nano hello_world.c
```

In [nano](nano.md), write the C++ program as such:

```c++
#include <iostream>

int main()
{
  std::cout << "hello, world\n";
}
```

### 1. Load a GCC module

Load a recent GCC [module](../cluster_guides/modules.md):

```bash
module load gcc/13.2.0
```

???- question "Do I really need to load a module?"

    No, as there is a system-installed GCC.

    For sake of doing reproducible research,
    always load a module of a specific version.

### 2. Compile the source file

After saving and closing nano, compile as such:

```bash
g++ hello_world.cpp
```

This compiles the file `hello_world.cpp` using all defaults:

- default/no optimization
- the executable created is called `a.out`

To compiles the file `hello_world.cpp` with run-time speed optimization
and creating an executable with a more sensible name, use:

```bash
g++ -O3 -o hello_world hello_world.cpp
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

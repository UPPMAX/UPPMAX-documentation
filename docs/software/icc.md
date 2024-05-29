# Intel compiler

There are multiple [compilers](compilers.md) on the UPPMAX HPC clusters.
This page describes the Intel compiler.

The Intel compiler is part of the `intel` [module](../cluster_guides/modules.md)
and can be used to:

- [Compile a C program](#compile-a-c-program)
- [Compile a C++ program](#compile-a-cpp-program)

Working together with the Intel compiler are:

- A [debugger](debuggers.md) called [`gdb`](gdb.md)
- An obsolete [debugger](debuggers.md) called [`idb`](idb.md)
- Some general [profiler](profilers.md) called [Intel VTune](intel_vtune.md)
  and [Intel Advisor](intel_advisor.md)

## Compile a C program

Load a recent GCC module:

```bash
module load gcc/13.2.0
```

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

## Compile a Cpp program

!!! info "Technical note"

    This header should have been 'Compile a C++ program'.

???- question "Why not use 'Compile a C++ program' as a header?"

    The link to the header 'Compile a C program' and 'Compile a C++ program' 
    would be `#compile-a-c-program` for both, as
    all punctuation (hence, the plus signs) must be removed.

Load a recent Intel compiler module:

```bash
module load intel/20.4
```

Create and write a C++ source file called `hello_world.cpp`:

```bash
nano hello_world.cpp
```

In [nano](nano.md), write the C++ program as such:

```c++
#include <iostream>

int main() 
{
  std::cout << "hello, world\n";
}

```

After saving and closing nano, compile as such:

```bash
icpc hello_world.cpp 
```

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

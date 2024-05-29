# GCC

GCC is shorthand for 'GNU Compiler Collection',
a collection of [compilers](compilers.md).

GCC is part of the `gcc` [module](../cluster_guides/modules.md)
and can be used to:

- [Compile a C program](#compile-a-c-program)
- [Compile a C++ program](#compile-a-c++-program)

Working together with GCC are:

- A [debugger](debuggers.md) called [`gdb`](gdb.md)
- A [profiler](profilers.md) called [`gprof`](gprof.md)
- A general [profiler](profilers.md) called [Valgrind](valgrind.md)

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
gcc hello_world.c
```

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

## Compile a C++ program

Load a recent GCC module:

```bash
module load gcc/13.2.0
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
g++ hello_world.cpp 
```

Run the program:

```bash
./a.out 
```

Output:

```console
hello, world
```

# GCC

GCC is shorthand for 'GNU Compiler Collection',
a collection of [compilers](compilers.md).

GCC is part of the `gcc` [module](../cluster_guides/modules.md)
and can be used to:

- [Compile a C program](gcc_compile_c.md)
- [Compile a C++ program](gcc_compile_cpp.md)
- [Compile a Fortan program](gcc_compile_fortran.md)

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

### Again

## C programs

Enter the following c program and save in the file hello.c

``` c
/* hello.c :  print message on screen */
#include <stdio.h>
int main()
{
    printf("hello, world\n");
    return 0;
}
```

To compile using gcc installed with the system (4.8.5, 2015) and with no optimization, use the gcc command.

``` console
$ gcc -o hello hello.c
```

To use a newer version of ggc we load a module:

``` console
$ module load gcc/10.3.0
$ gcc -o hello hello.c
```

with basic optimization:

``` console
$ gcc -O3 -o hello hello.c
```

c11 standard has full support from gcc/4.8, c17 standard (bug-fix) from gcc/8.


## Compile a Cpp program

!!! info "Technical note"

    This header should have been 'Compile a C++ program'.

???- question "Why not use 'Compile a C++ program' as a header?"

    The link to the header 'Compile a C program' and 'Compile a C++ program' 
    would be `#compile-a-c-program` for both, as
    all punctuation (hence, the plus signs) must be removed.

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

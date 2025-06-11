# Compile a Fortran program using `ifx`

[ifx](ifx.md) is an Intel Fortran [compiler](compilers.md).
This page describes how to compile Fortran code using `ifx`.

## Procedure

### 1. Load the modules

Load a recent `intel` module:

```bash
module load intel-oneapi
module load compiler/2023.1.0
```

### 2. Write the Fortran program

Create and write a Fortran source file called `hello_world.f`:

```bash
nano hello_world.f
```

In [nano](nano.md), write the Fortran program as such:

```c++
C     HELLO.F :  PRINT MESSAGE ON SCREEN
      PROGRAM HELLO
      WRITE(*,*) "hello, world";
      END
```

### 3. Compile the C++ program

After saving and closing nano, compile as such:

```bash
ifx hello_world.f
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

# Compile Fortran using GCC

[GCC](gcc.md) (shorthand for 'GNU Compiler Collection')
is a collection of [compilers](compilers.md)
able to compile multiple different programming languages.

This page describes how to compile Fortran code using the GCC.

## Procedure

### 0. Create a Fortran source file

You will need Fortran code to work on.

In this optional step, a file with a minimal Fortran program is created.

Create and write a Fortran source file called `hello_world.f`:

```bash
nano hello_world.f
```

In [nano](nano.md), write the Fortran program as such:

``` fortran
C     HELLO.F :  PRINT MESSAGE ON SCREEN
      PROGRAM HELLO
      WRITE(*,*) "hello, world";
      END
```

### 1. Load a GCC module

Load a recent GCC module:

```bash
module load gcc/13.2.0
```

???- question "Do I really need to load a module?"

    No, as there is a system-installed GCC.

    For sake of doing reproducible research,
    always load a [module](../cluster_guides/modules.md) of a specific version.

### 2. Compile the source file

After saving and closing nano, compile as such:

```bash
gfortran hello_world.f
```

This compiles the file `hello_world.f` using all defaults:

- default/no optimisation
- the executable created is called `a.out`

To compiles the file `hello_world.f` with run-time speed optimisation
and creating an executable with a more sensible name, use:

```bash
gfortran -Ofast -o hello_world hello_world.f
```

- `-Ofast`: optimise for run-time speed, similar to `-O3`
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

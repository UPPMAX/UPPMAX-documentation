# `gdb`

There are many [debuggers](debuggers.md).
This page described `gdb`, the GNU debugger.

`gdb` is a debugger provided with the GNU [compilers](compilers.md). 
It works fine for C, C++ and Fortran. 
With older versions there were problems with fortran90/95.

- [Debugging GCC-compiled programs](#debugging-gcc-compiled-programs)
- [Debugging Intel-compiled programs](#Debugging-intel-compiled-programs)

## Debugging GCC-compiled programs

In order to use gdb do the following.
load a recent gcc module and a gdb module (system gdb is from 2013!).

```bash
module load gcc/10.3.0 gdb/11.2
```

compile your program with flags for debugging added, e.g. -ggdb

```bash
gcc -ggdb your-program.c -o your-program
```

run the gdb program:

```bash
gdb your-program
```

Then you can use the gdb commands, like run, break, step, help, ...

Exit with `Ctrl+D`.

## Debugging Intel-compiled programs

In order to use `gdb` with Intel-compiled programs, do the following"

Load the `icc` module

```bash
module load intel/20.4
```

Compile your program with flags for debugging added, e.g. -g

```bash
icc -g your-program.c -o your-program
```

Run the gdb program:

```bash
gdb your-program
```

Then you can use the gdb commands, like run, break, step, help, ...

Exit with `Ctrl+D`.


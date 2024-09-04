# `gprof`

There are multiple [profilers](profilers.md)
available on UPPMAX.
This page describes [gprof](gprof.md).

[gprof](gprof.md) is the GNU profiler, provided with the GNU compiler package.

In order to use `gprof` do the following:

Load a recent `gcc` [module](../cluster_guides/modules.md)
and a recent `binutils` module:

```bash
module load gcc
module load binutils
```

Compile your program with the `-pg -g` flags added

```bash
gcc -O0 -pg -g your-program.c -o your-program
```

run it:

```bash
./your-program
```

then do:

```bash
gprof your-program gmon.out > output-file
```

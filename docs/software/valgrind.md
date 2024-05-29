# Valgrind

There are multiple [profilers](profilers.md)
available on UPPMAX.
This page describes [Valgrind](valgrind.md).

Valgrind is a suite of simulation-based debugging and profiling tools for programs.

Valgrind contains several tools:

- `memcheck`, for detecting memory-management problems in your program
- `cachegrind`, for cache profiling
- `helgrind`, finds data races in multithreded programs
- `callgrind`, a call graph profiler
- `drd`, a thread error detector
- `massif`, a heap profiler
- `ptrcheck`, a pointer checking tool
- `lackey`, a simple profiler and memory tracer

Valgrind works best with the GCC and Intel compilers. 

There is a system `valgrind-3.15.0` from 2020.

First load compiler:

```bash
module load gcc
```

or

```bash
module load intel
```

then you can use `valgrind` by:

```text
valgrind [options] ./your-program [your programs options]
```

### How to use valgrind with MPI programs

Load your compiler, `openmpi` and the `valgrind` module as before:

```bash
module load gcc/10.3.0 openmpi/3.1.6
```

or

```bash
module load intel/20.4 openmpi/3.1.6
```

As of now, Valgrind seems not compatible with `openmpi/4.X.X`.

Then run:

```bash
LD_PRELOAD=$VALGRIND_MPI_WRAPPER
mpirun -np 2 valgrind ./your-program
```

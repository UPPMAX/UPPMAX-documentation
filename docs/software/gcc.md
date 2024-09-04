# GCC/`gcc`

GCC is shorthand for 'GNU Compiler Collection',
a collection of [compilers](compilers.md),
where `gcc` is the name of the actual program.

`gcc` is part of the `gcc` [module](../cluster_guides/modules.md).

???- question "How do I find the `gcc` module?"

    Like you'd find any [module](../cluster_guides/modules.md):

    ```bash
    module spider gcc
    ```

???- question "Which versions does the `gcc` module have?"

    Like you'd find the version of any [module](../cluster_guides/modules.md):

    ```bash
    module spider gcc
    ```

    This will look similar to this:

    ```bash
    [sven@rackham2 ~]$ module spider gcc

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      gcc:
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Versions:
            gcc/4.2.3
            gcc/4.3.0
            gcc/4.4
            gcc/4.8.2
            gcc/4.8.3
            gcc/4.9.2
            gcc/4.9.4
            gcc/5.2.0
            gcc/5.3.0
            gcc/5.4.0
            gcc/5.5.0
            gcc/6.1.0
            gcc/6.2.0
            gcc/6.3.0
            gcc/6.4.0
            gcc/7.1.0
            gcc/7.2.0
            gcc/7.3.0
            gcc/7.4.0
            gcc/8.1.0
            gcc/8.2.0
            gcc/8.3.0
            gcc/8.4.0
            gcc/9.1.0
            gcc/9.2.0
            gcc/9.3.0
            gcc/10.1.0
            gcc/10.2.0
            gcc/10.3.0
            gcc/11.2.0
            gcc/11.3.0
            gcc/12.1.0
            gcc/12.2.0
            gcc/12.3.0
            gcc/13.1.0
            gcc/13.2.0
            gcc/13.3.0
            gcc/14.1.0
         Other possible modules matches:
            GCC  GCCcore  gcccuda

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*gcc.*'

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      For detailed information about a specific "gcc" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider gcc/14.1.0
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ```

The GCC can be used to:

- [Compile a C program](gcc_compile_c.md)
- [Compile a C++ program](gcc_compile_cpp.md)
- [Compile a Fortran program](gcc_compile_fortran.md)

Working together with GCC are:

- A [debugger](debuggers.md) called [`gdb`](gdb.md)
- A [profiler](profilers.md) called [`gprof`](gprof.md)
- A general [profiler](profilers.md) called [Valgrind](valgrind.md)

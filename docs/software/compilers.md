# Compilers

UPPMAX supports multiple compilers:

Compiler         |Language(s)    |Description
-----------------|---------------|---------------------------
[GCC](gcc.md)    |C, C++, Fortran|The GNU compiler collection
[icc](icc.md)    |C              |Older Intel C compiler
[icpc](icpc.md)  |C++            |Intel C++ compiler
[icx](icx.md)    |C              |Newer Intel C compiler
[ifort](ifort.md)|Fortran        |Intel Fortran compiler
[javac](javac.md)|Java           |Java compiler

Different compilers are association with different [debuggers](debuggers.md)
and different [profiling tools](profilers.md).

???- question "How to make sure you have only the right compiler loaded?"

    Use

    ```
    module list
    ```

    to get a list of modules.

    This may look like this:

    ```
    Currently Loaded Modules:
      1)  uppmax    2) intel/19.5
    ```

    If there are modules connected to the incorrect compiler,
    unload the module, for example:

    ```
    module unload intel
    ```

    This scenario is valid if you want to use tools that use the GCC compiler.

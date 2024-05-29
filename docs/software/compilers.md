# Compilers

UPPMAX supports two kind of compilers:

- [GCC](gcc.md): the GNU compiler collection
- [icc](icc.md): an Intel compiler

Each compilers have its own [debuggers](debuggers.md)
and [profiling tools](profilers.md).

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

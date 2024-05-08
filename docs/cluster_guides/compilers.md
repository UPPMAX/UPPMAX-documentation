# Compilers

UPPMAX supports two kind of compilers:

- GNU project compilers
- Intel compilers

This tutorial will show how to use the tools provided
with the compilers and some other profiling tools.
Since all these tools is strongly connected to the compiler they come with,
it is recommended to only have that compiler module loaded.

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

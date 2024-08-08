# MultiQC

MultiQC is a tool with homepage <https://github.com/ewels/MultiQC>.

MultiQC can be found among [the UPPMAX modules](../cluster_guides/modules.md).

```bash
module spider MultiQC
```

???- question "How does that look like?"

    You output will look similar to this:

    ```bash
    [richel@rackham2 ~]$ module spider MultiQC

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      MultiQC:
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Versions:
            MultiQC/0.6
            MultiQC/0.7
            MultiQC/0.8
            MultiQC/0.9
            MultiQC/1.0
            MultiQC/1.2
            MultiQC/1.3
            MultiQC/1.5
            MultiQC/1.6
            MultiQC/1.7
            MultiQC/1.8
            MultiQC/1.9
            MultiQC/1.10
            MultiQC/1.10.1
            MultiQC/1.11
            MultiQC/1.12
            MultiQC/1.22.2

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      For detailed information about a specific "MultiQC" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider MultiQC/1.22.2
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ```

To find out how to load a specific version:

```bash
module spider MultiQC/1.22.2
```

???- question "How does that look like?"

    Output will look similar to:

    ```bash
    [richel@rackham2 ~]$ module spider MultiQC/1.22.2

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      MultiQC: MultiQC/1.22.2
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        You will need to load all module(s) on any one of the lines below before the "MultiQC/1.22.2" module is available to load.

          bioinfo-tools
     
        Help:
           MultiQC - use MultiQC 1.22.2
          
           Version 1.22.2
          
          
          Version 1.22.2 is installed using python/3.8.7
    ```      

After reading that documentation, we know how to load it:

```bash
module load bioinfo-tools 
module load MultiQC/1.22.2
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [richel@rackham2 ~]$ module load bioinfo-tools 
    [richel@rackham2 ~]$ module load MultiQC/1.22.2
    [richel@rackham2 ~]$ 
    ```

## Singularity script

If you want to put MultiQC in a [Singularity](singularity.md) container,
here is an example script:

```singularity
BootStrap: library
From: ubuntu:18.04

%runscript
  multiqc "$@"

%post
  echo "Hello from inside the container"
  apt-get update
  apt-get -y dist-upgrade
  apt-get clean
  apt-get -y install python-pip
  pip install multiqc
```

See [the documentation on Singularity](singularity.md)
how to do so.

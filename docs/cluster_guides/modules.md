---
tags:
  - module
  - modules
  - software module
  - software modules
  - lmod
---

# Software modules

![Working with a computer cluster module system](./img/627409_working_with_a_computer_cluster_module_system_256_x_256.png)

Here we show how to use the environment module system.

After describing [the background](#background)/reasoning
why such a system is needed,
we show [how to work with the module system](#working-with-the-module-system).

There is a table of [commonly used shorthand syntaxes](#common-shorthand-syntaxes),
as well as [links](#links) to almost all installed software and databases on UPPMAX.

## Background

The UPPPMAX clusters are shared Linux computers with all the standard Linux tools installed,
on which all users should be able to
do their work independently and undisturbed.

To ensure this, users cannot modify, upgrade or uninstall software themselves
and instead an [environment module system](https://lmod.readthedocs.io/en/latest/)
(from now on: 'module system') is used.
This allow users to independently use their favorite versions of their
favorite software.

Using a module system keeps installed software hidden by default,
and users have to explicitly tell their [terminal](../software/terminal.md)
which version of which software they need.

To have new software installed on an UPPMAX cluster,
users must explicitly request a version of a piece of software.
As of today, there are nearly
[800+ programs and packages, with multiple versions](../software/overview.md)
available on all UPPMAX clusters.
Using explicit versions of software is easy to do
and improves the reproducibility of the scripts written.

To preserve hard disk space, Bianca also
has [multiple big databases installed](../databases/overview.md).

!!! warning

    To access bioinformatics tools, load the **bioinfo-tools** module first.

## Working with the module system

!!! info Overview of module commands

    Command                         |Description
    --------------------------------|--------------------------------------
    `module load bioinfo-tools`     |Load this module first, to find others
    `module spider`                 |Search for a module
    `module spider [module]`        |Get info about a module, e.g. `module spider cowsay`
    `module list`                   |List all activated modules
    `module load [module]`          |Load a module, e.g. `module load cowsay`
    `module load [module]/[version]`|Load a module of a specific versions, e.g. `module load cowsay/3.03`
    `module help`                   |Show the help for a module
    `module unload [module]`        |Unload the module `[module]`, e.g. `module unload cowsay`

Working with the module system means:

- searching for a module
- activating ('loading') a module
- deactivate ('unloading') a module

This section describes these steps in more details.

The `module` command is the basic interface to the module system.

To search for a module, use `module spider [module]`,
for example `module spider cowsay`.

???- question "Would you like to see a video instead?"

    Watch the video that shows the use of modules on Bianca [here](https://youtu.be/lNlq2Eb-qgc)

???- question "What is `cowsay`?"

    See [the UPPMAX page on `cowsay`](../software/cowsay.md)

???- question "What is `R`?"

    `R` is the module for the R programming language.
    R is a free and open-source programming language,
    commonly used in data analysis and visualization.

???- question "How does the output of `module spider R` look like?"

    ```bash
    $ module spider R

    -------------------------------------------
      R:
    -------------------------------------------
         Versions:
            R/3.0.2
            R/3.2.3
            R/3.3.2
            R/3.4.0
            R/3.4.3
            R/3.5.0
            R/3.5.2
            R/3.6.0
            R/3.6.1
            R/4.0.0
            R/4.0.4
            R/4.1.1
            R/4.2.1
         Other possible modules matches:
            454-dataprocessing  ADMIXTURE  ANTLR  ARCS  ARC_assembler  ARPACK-NG  ART  AdapterRemoval  AlienTrimmer  Amber  AnchorWave  Arlequin  Armadillo  ArrowGrid  Bamsurgeon  BclConverter  BioBakery  BioBakery_data  ...

    -------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*R.*'

    -------------------------------------------
      For detailed information about a specific "R" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider R/4.2.1
    -------------------------------------------
    ```

???- question "What is `samtools`?"

    `samtools` is the module for SAMtools. From [wikipedia](https://en.wikipedia.org/wiki/SAMtools):

    > SAMtools is a set of utilities for interacting with
    > and post-processing short DNA sequence read alignments
    > in the SAM (Sequence Alignment/Map), BAM (Binary Alignment/Map)
    > and CRAM formats

???- question "How does the output of `module spider samtools` look like?"

    ```bash
    $ module spider samtools

    -------------------------------------------
      samtools:
    -------------------------------------------
         Versions:
            samtools/0.1.12-10
            samtools/0.1.19
            samtools/1.1
            samtools/1.2
            samtools/1.3
            samtools/1.4
            samtools/1.5_debug
            samtools/1.5
            samtools/1.6
            samtools/1.8
            samtools/1.9
            samtools/1.10
            samtools/1.12
            samtools/1.14
            samtools/1.16
            samtools/1.17
         Other possible modules matches:
            SAMtools

    -------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*samtools.*'

    -------------------------------------------
      For detailed information about a specific "samtools" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider samtools/1.17
    -------------------------------------------
    ```

???- question "How does the output of `module spider samtools/1.17` look like?"

    ```bash
    $ module spider samtools/1.17

    -------------------------------------------
      samtools: samtools/1.17
    -------------------------------------------

        You will need to load all module(s) on any one of the lines below before the "samtools/1.17" module is available to load.

          bioinfo-tools

        Help:
            samtools - use samtools 1.17

            Version 1.17
    ```

    This reminds us that we need to load the `bioinfo-tools`
    module to be able to load `samtools/1.17`.
    Again, this is required (just once) before loading bioinformatics software.

If there is an exact match, that module is reported first.
Of the module shown, also the different versions are reported.

!!! tip "Do `module load bioinfo-tools` first"

    When working with modules, do `module load bioinfo-tools` first

???- tip "What to do when you cannot find a module"

    Run `module load bioinfo-tools`.

    This will allow other modules to be found.

???- tip "What to do when `module load` gives an 'Lmod has detected the following error:  These module(s) or extension(s) exist but cannot be loaded as requested' error?"

    Ouch, now it is time to try out many things.

    Do not hesitate to [contact support](../support.md)
    so that you can spend time on your research
    and we figure this out :-)

To load a module, use `module load [module]`,
for example `module load cowsay`.
This will load the default version of that module,
which is almost always the latest version.
Loading a module always results in a helpful message
(such as that it worked fine), however,
it is *not* general help for using the tool itself.

???- question "How can I see which modules I've loaded?"

    Use the command `module list`.

???- question "How does the output of `module list` look like?"

    ```bash
    $ module list

    Currently Loaded Modules:
      1) uppmax   2) bioinfo-tools   3) samtools/1.17
    ```

    In this example case, we can see that the modules `bioinfo-tools`
    and `samtools` version 1.17 are loaded.

!!!- tip "Getting help on a module"

    Run `module help [module]`, e.g. `module help cowsay`
    to get the general help on a module

For reproducible research, however, it is good practice
to load a specific version. The information given by
`module spider` contains the versions of the module.
For example, to load the `samtools/1.17` module,
do `module load samtools/1.17`.

???- question "How does the output of `module load GATK/4.3.0.0` look like?"

    ```bash
    $ module load GATK/4.3.0.0
    Note that all versions of GATK starting with 4.0.8.0 use a different wrapper
    script (gatk) than previous versions of GATK.  You might need to update your
    jobs accordingly.

    The complete GATK resource bundle is in /sw/data/GATK

    See 'module help GATK/4.3.0.0' for information on activating the GATK Conda
    environment for using DetermineGermlineContigPloidy and similar other tools.
    ```

    This message references the command `module help GATK/4.3.0.0` for additional help with this module.

???- tip "Huh, `module load samtools/1.17` gives an error?"

    If you do `module load samtools/1.17` without
    doing `module load bioinfo-tools` first, you'll get the error:

    ```bash
    $ module load samtools/1.17
    Lmod has detected the following error:  These module(s) or
    extension(s) exist but cannot be loaded as requested: "samtools/1.17"
       Try: "module spider samtools/1.17" to see how to load the module(s).
    ```

    The solution is to do `module load bioinfo-tools` first.

To see which modules are loaded, use `module list`.

???- question "How does the output of `module list` look like?"

    ```text
    $ module list

    Currently Loaded Modules:
      1) uppmax   2) bioinfo-tools   3) samtools/1.17   4) java/sun_jdk1.8.0_151   5) GATK/4.3.0.0
    ```

    Modules can also be unloaded, which also unloads their prerequisites.

To see a module-specific help, use `module help [module]` (e.g. `module help cowsay`).

???- question "How does the output of `module help GATK/4.3.0.0` look like?"

    ```bash
    $ module help GATK/4.3.0.0

    -------------- Module Specific Help for "GATK/4.3.0.0" ---------------
    GATK - use GATK 4.3.0.0
    Version 4.3.0.0

    **GATK 4.3.0.0**

    Usage:

        gatk --help     for general options, including how to pass java options

        gatk --list     to list available tools

        gatk ToolName -OPTION1 value1 -OPTION2 value2 ...
                      to run a specific tool, e.g., HaplotypeCaller, GenotypeGVCFs, ...

    For more help getting started, see

        https://software.broadinstitute.org/gatk/documentation/article.php?id=9881

    ...
    ```

To unload a module, do `module unload [module]` (e.g. `module unload cowsay`).
This will also unload module that depend on the unloaded one.
For example, `module unload bioinfo-tools` will unload all bioinformatics tool.

## Using modules in an executable script

Using modules in an executable script is straightforward:
just load the module needed before using the software in that module.

For example, this is a valid bash script:

```text
#!/bin/bash
module load cowsay/3.03
cowsay hello
```

When using a bioinformatics tool such as `samtools` version 1.17,
one needs to first load `bioinfo-tools`:

```text
#!/bin/bash
module load bioinfo-tools
module load samtools/1.17
```

## Common shorthand syntaxes

Full command            |Shorthand syntax
------------------------|----------------
`module`                |-
`module avail`          |`ml av`
`module spider`         |`ml spider`
`module load`           |`ml`
`module list`           |`ml`
`module unload [module]`|`ml -[module]`

## Links

- [Almost all installed software on UPPMAX](../software/overview.md)
- [Almost all installed databases on UPPMAX](../databases/overview.md)
- [Wikipedia page on environment modules](https://en.wikipedia.org/wiki/Environment_Modules_(software))
- [lmod homepage](https://www.tacc.utexas.edu/research/tacc-research/lmod/)

## Extra materials

### About `module avail`

!!! info "Why here?"

    As far as I can see, there is no use case for `module avail`.

`module avail` list all modules immediately available,
or search for a specific available module:

- `module avail`
- `module avail *tool*`

This command is not so smart,
though, especially when searching for a specific tool, or a bioinformatics tool.
It only reports modules that are immediately available.

```bash
module avail R
```

outputs everything that has an `r` in the name... not useful.

```bash
$ module avail samtools
No module(s) or extension(s) found!
Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```

## Conflicting modules

Sometimes some tools cannot be run together, that is working when another module is loaded. Read about this in the page:

- [Conflicting modules](module_conflicts.md)

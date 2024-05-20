# Spack on UPPMAX

## Introduction

Spack is a simple package management tool or installer that also installs dependencies automatically to the main software. Installing a new software version does not break existing installations, so many configurations can coexist on the same system.

It offers a simple spec syntax so that users can specify versions and configuration options concisely. Spack is also simple for package authors: package files are written in pure Python, and specs allow package authors to maintain a single file for many different builds of the same package.

[Spack documentation](https://spack.readthedocs.io/en/latest/)

The UPPMAX staff has already other ways to install most software applications. Please use Spack only if other ways to install your tool is not possible or very difficult, e.g. requiring very many dependencies and it is not available through, e.g. Easybuild (that the staff can manage centrally). One or the reasons is that SPACK produces very many small files and that having two parallel build systems centrally may make things a little complex.

This guide may change with time. Please come back and see updates.

This version assumes no available SPACK module, which may come in the near future.
You have your own instance of Spack but can get a configuration file provided by UPPMAX.

## First steps: Installing your own instance of SPACK

You may want to use your project folder if you want your colleagues to be able to run the application. Then change directory to a good place before installing Spack.

``` console
$ cd <good place>
```

### Step 1: clone spack

``` console
$ module load git
$ git clone -c feature.manyFiles=true https://github.com/spack/spack.git 
$ cd spack
```

To get version v0.18:

``` console
$ git checkout releases/v0.18
```

Next, add Spack to your path. Spack has some nice command-line integration tools, so instead of simply appending to your PATH variable, source the Spack setup script.

``` console
$ source <root dir of spack>/spack/share/spack/setup-env.sh
```

Adding this line to your ``~/.bashrc`` as well will activate the "spack commands" each time you start a new terminal session.

### Orientation of the SPACK files

The Spack oriented files are stored in two places:

- Spack directory
    - the cloned git repository
    - directories (important in bold)
        - bin        spack executables
        - etc        configuration files
        - lib         libraries
        - share       documentation, scripts etc...
        - var        other settings
        - opt        produced after first installation, contains all packages (tools, dependencies and libraries)
            - tools are found in a tree: .`..opt/spack/linux-<arch>/<compiler>/tool/`
- .spack
    - local config and packages files
    - directories (important in bold)
        - bootstrap
        - cache
        - reports
        - linux
            - ​compilers.yaml
            - packages.yaml


The .yaml files in the .spack/linux directory contains information which tolls you want to include from the UPPMAX system.

- The compilers.yaml file lists the compilers (intel or gcc) modules available to build your software tool.
- The packages.yaml file lists tools available already as modules.

By default, these files are empty but you can copy working "central" files that can be extended for your needs. The content of the files can be larger than the needed packages/compilers, i.e. only the packages /dependencies needed for your installation will be "taken" from these files and the rest will be ignored. Therefore, the UPPMAX staff may update these central files once in a while.

### Get templates

Do the following to get these templates (be sure to not overwrite old versions of these .yaml files that you configured yourself and might need).

``` console
$ cp /sw/build/spack/0.17.1/src/spack/share/spack/templates/compilers.yaml ~/.spack/linux/
$ cp /sw/build/spack/0.17.1/src/spack/share/spack/templates/packages.yaml ~/.spack/linux/
```

## Install your program

Check available software applications via Spack:

``` console
$ spack list
$ spack list <search string>
```

Check already installed software applications with spack

``` console
$ spack find
$ spack find <search string>
```

Some installations won't need any compilers or "large dependencies". The installation is straightforward:

``` console
$ spack install <tool>
```

Example:

``` console
$ spack install zlib
```

In other cases, for larger applications tools that require larger dependencies (that we might already have as modules), watch the installation documentation to see what is needed. Any recommended compiler? You can also check with a "dry run" before installing, to see what Spack "thinks" its needs to install. Use the spec command:

``` console
$ spack spec -I <tool>
```

To check the presently, for Spack, available compilers, type:

``` console
$ spack compilers
```

If your desired compiler is not there you can add it by first loading the module and then integrate it into the compilers.yaml file with a spack command:

Example:

``` console
$ module load intel/20.4
$ spack compiler add
```

You can check if the compiler was added, either in the .spack/linux/compilers.yaml file or directly by:

``` console
$ spack compilers
```

To install a tool with a certain compiler version, if there are several compilers added for Spack, use "%". For specific version of the software tool or package, use "@".

``` console
$ spack install <tool>%<compiler>@<compiler-version>
```

Example:

``` console
$ spack install zlib%gcc@5.3.0
```

Large application tools may take a couple of hours so might be good to run in an interactive session (4 cores, -n 4).

``` console
$ spack install -j 4 <tool>
```

Use dependencies already available from our [environment module system](../cluster_guides/modules.md)) ('module load').

``` console
$ cat .spack/linux/packages.yaml
```

Fill it with text,defining the spack name and lmod module names (be careful with indentations)
Then install you tool, as above.
To install a specific version of a dependency with Spack, use the command "^":

``` console
$ spack install <tool>%<compiler>@<compiler-version>^<dependency>@<version>
```

Here is a summarizing table

Command |Option
-|-
@|Which version
%|which compiler
^|which dependency

## Use your tool

``` console
$ spack load <tool>  
# module load of the install dependencies will not be needed here, since their paths are integrated in spack
$ <tool> [<arguments>]
```

## Develop

More to come... Meanwhile:

[Developer guide](https://spack.readthedocs.io/en/latest/developer_guide.html)

[Developer workflows tutorial](https://spack-tutorial.readthedocs.io/en/latest/tutorial_developer_workflows.html)

The builds are by default located here: ``<spack-root>/opt/spack/linux-centos7-broadwell/<compiler-version>/``


## Packages and environments

More to come... Meanwhile:

[Packaging guide](https://spack-tutorial.readthedocs.io/en/latest/tutorial_developer_workflows.html)

[Environments guide](https://spack.readthedocs.io/en/latest/environments.html)

[Environments tutorial](https://spack-tutorial.readthedocs.io/en/latest/tutorial_environments.html)

## Garbage collection

Installing and uninstalling software will in the end use up your disk space so it is good practice to do some garbage collection

``` console
$ spack gc
```

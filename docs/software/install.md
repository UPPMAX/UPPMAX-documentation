# Software and package installation

## Install software yourself

### Build from source

- To build from source use a **compiler module**
- We have several compiler versions from GNU and INTEL
- check with: ``$ ml avail gcc`` and ``$ ml avail intel``
- [Guide for compiling **serial** programs](compiling_serial.md)
- [Guide for compiling **parallel** programs](compiling_parallel.md)
    - [Available **combinations** of compilers and parallel libraries](parallel_comb.md)

### Example

This guide might not work on all programs. **Read the installation instructions for your program!**

- Download the program, with ``wget`` or by other means like ``git clone <https-URL to `GITHUB repo>`.
- If the not cloning, unpack it with ``tar``, ``gunzip`` or similar.

```bash
tar xvfz program.tgz
```
**This is general**

- Read the installation instructions!
- If Fortran or C or C++, load a compiler. Often you'll have less problems with gcc but intel gives faster code.

```bash
module load gcc
```

- If applicable, do:

```bash
mkdir $HOME/glob/program_name
./configure --prefix=$HOME/glob/program_name
make
make test
make install
```

- Try to find a test on the home page of the program or in the installation instructions and try to run it.

## Packages and libraries to scripting programs

- Python, R and Julia all have some **centrally installed packages** that are available from the modules.
- R has a special module called ``R_packages``, and some Machine Learning python packages are included in the ``python_ML_packages`` module.
- If not found there you can try to install those by yourself.


!!! info "Tip Python packages"

    - Try Conda first directly on Bianca and PyPI on Rackham.
    - We have mirrored all major Conda repositories directly on UPPMAX, on both Rackham and Bianca. These are updated every third day.
    - If you want to keep number of files down, use PyPI (pip).
    - Also it is easier to get **conflicting environments if using both Python module and Conda in parallel**.

### Conda

- We have mirrored all major Conda repositories directly on UPPMAX, on both Rackham and Bianca. These are updated every third day.

!!! info "Available Conda channels"

    - bioconda
    - biocore
    - conda-forge
    - dranew
    - free
    - main
    - pro
    - qiime2
    - r
    - r2018.11
    - scilifelab-lts

- [Conda user guide](../software/conda.md)

### Python packages with pip

- [Installing with pip](../software/python_install_packages.md)

### R packages

- On UPPMAX the module ``R_packages`` is an omnibus package library containing almost all packages in the CRAN and BioConductor repositories.
- As of 2023-05-31, there were a total of 23100 R packages installed in ``R_packages/4.2.1``.
    - A total of 23109 packages were available in CRAN and BioConductor, and 23000 of these were installed in ``R_packages/4.2.1``
    - The additional 100 R packages available in this module were installed from the CRAN/BioConductor archives, or were hosted on github, gitlab or elsewhere.

- [Installing R packages](../software/r.md)

### Julia packages

- At UPPMAX there is a central library with installed packages.
- This is good, especially when working on Bianca, since you then do not need to install via the ``wharf``.
- A selection of the Julia packages and libraries installed on UPPMAX are:

        CSV
        CUDA
        MPI
        Distributed
        IJulia
        Plots
        PyPlot
        DataFrames

- [Installing julia packages](http://docs.uppmax.uu.se/software/julia/#how-to-install-personal-packages)

## Containers

!!! info

    - Containers let you install programs without needing to think about the computer environment, like
        - operative system
        - dependencies (libraries and other programs) with correct versions
    - Everything is included
    - Draw-backs
        - you install also things that may be already installed
        - therefore, probably more disk space is needed

### Singularity

See [the UPPMAX Singularity user guide](singularity.md)

### Docker

Docker will unfortunately not work on the clusters, since it requires root permission.

!!! info "More info"

    - [Singularity user guide](../software/singularity.md)
    - [Part from Bianca course but applicable also on Rackham](https://github.com/UPPMAX/bianca_workshop/blob/main/docs/extra/containers.md)

## Spack

- The UPPMAX staff has already other ways to install most software applications.
- Please use Spack only if other ways to install your tool is not possible or very difficult, e.g. requiring very many dependencies and it is not available through, e.g. Easybuild.
- [UPPMAX Spack user guide](../software/spack.md)

## Own development

- You may have your own code that you want to run on UPPMAX.
- [Guide for compiling **serial** programs](compiling_serial.md)
- [Guide for compiling **parallel** programs](compiling_parallel.md)
    - [Available **combinations** of compilers and parallel libraries](compiling_parallel.md#overview-of-available-compilers-from-gcc-and-intel-and-compatible-mpi-libraries)
- [User guide for debuggers](../software/debuggers.md)
- [User guide for profilers](../software/profilers.md)

## Run own scripts or programs

Unless your script or program is in the active path, you run it by the full path or `./<file>` if you are in the present directory.

## Summary

!!! abstract "Keypoints"
    - You have got an overview of the procedures to install packages/libraries and tools on Bianca through the ``wharf``
    - If you feel uncomfortable or think that many users would benefit from the software, ask the support to install it.

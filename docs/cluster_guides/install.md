# Software and package installation

## Install software yourself

- If not available on Bianca already (like Conda repositories) you may have to use the ``wharf`` to install your tools
    - Alternatively let an Application Expert install the tool as a module.

!!! note "Typical workflow for installation"

    - **Download the source code or binary** (Linux on x86 and 64-bit) to Rackham first
    - **Transfer** to the ``wharf``
    - Then, either 
        - You can install in your home directory.
            - This is handy for personal needs, low numbers of files (i.e. not Conda).
         - Usually better to install in project directory.
            - This way the project contains both data and software — good for reproducibility, collaboration, and everyone's general sanity.
    - Binaries for Linux on x86 and 64-bit should be able to be run directly as it is, see the software specific installation documentation.
    - or build from source, see next session.
     

### Build from source
- To build from source use a **compiler module**
- We have several compiler versions from GNU and INTEL
- check with: ``$ ml avail gcc`` and ``$ ml avail intel``
- [Guide for compiling **serial** programs](https://www.uppmax.uu.se/support/user-guides/compiling-source-code/){:target="_blank"}
- [Guide for compiling **parallel** programs](https://www.uppmax.uu.se/support/user-guides/mpi-and-openmp-user-guide/){:target="_blank"}
    - [Available **combinations** of compilers and parallel libraries](https://www.uppmax.uu.se/support/user-guides/mpi-and-openmp-user-guide/#tocjump_48302061903476823_2){:target="_blank"}


## Packages and libraries to scripting programs

- Python, R and Julia all have some **centrally installed packages** that are available from the modules. 
- R has a special module called ``R_packages``, and some Machine Learning python packages are included in the ``python_ml_packages`` module.
- If not found there you can try to install those by yourself.


!!! info "Tip Python packages"

    - Try Conda first directly on Bianca. We have mirrored all major Conda repositories directly on UPPMAX, on both Rackham and Bianca. These are updated every third day.
    - If you want to keep number of files down, use PyPI (pip), but then you need to use Rackham and the ``wharf``.

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

!!! info "More info"

    - [Conda user guide](conda.md)

### Python packages with pip

!!! info "Installation principle"

    - install on Rackham
        - ``pip install --user <package>``
        - ``python setup.py install --user or --prefix=<path>``
    - sync to ``wharf``
    - move the files on Bianca to correct place
    - you may have to update ``$PYTHONPATH``

!!! info "More info"

    - [Extra material: Installing pip packages](https://uppmax.github.io/bianca_workshop/pip/){:target="_blank"}
    - [UPPMAX Python user guide: Pip](https://www.uppmax.uu.se/support/user-guides/python-user-guide/#tocjump_9332829429720808_5){:target="_blank"}
    - [From Python course: packages](https://uppmax.github.io/R-python-julia-HPC/python/packages.html){:target="_blank"}
    - [From Python course: isolated environments](https://uppmax.github.io/R-python-julia-HPC/python/isolated.html){:target="_blank"}


### R packages

- On UPPMAX the module ``R_packages`` is an omnibus package library containing almost all packages in the CRAN and BioConductor repositories. 
- As of 2023-05-31, there were a total of 23100 R packages installed in ``R_packages/4.2.1``.
    -  A total of 23109 packages were available in CRAN and BioConductor, and 23000 of these were installed in ``R_packages/4.2.1``
    -  The additional 100 R packages available in this module were installed from the CRAN/BioConductor archives, or were hosted on github, gitlab or elsewhere.

Chances are good the R packages you need are already available once you load this module.  You can quickly check by loading it:

``$ ml R_packages/4.2.1``

Then within R, try loading the package you want:

``library(glmnet)``

Or a bit longer way, you can ``grep`` for the package after this module is loaded using the environment variable ``$R_LIBS_SITE``, which contains the locations of all R packages installed within the module.

```bash
$ ls -l $R_LIBS_SITE | grep glmnet
drwxrwsr-x  9 douglas sw  4096 May 28 16:59 EBglmnet
drwxrwsr-x 11 douglas sw  4096 May 25 01:22 glmnet
drwxrwsr-x  6 douglas sw  4096 May 25 04:03 glmnetSE
drwxrwsr-x  7 douglas sw  4096 May 25 04:04 glmnetUtils
drwxrwsr-x  8 douglas sw  4096 May 25 04:04 glmnetcr
drwxrwsr-x  7 douglas sw  4096 May 25 10:46 glmnetr
```

!!! info "Installation principle"

    - install on Rackham
    - sync to ``wharf``
    - move the files on Bianca

!!! info "More info"

    - [Extra material: Installing R packages](https://uppmax.github.io/bianca_workshop/rpackages/)
    - [From R course: packages](https://uppmax.github.io/R-python-julia-HPC/R/packagesR.html){:target="_blank"}
    - [From R course: isolated environments](https://uppmax.github.io/R-python-julia-HPC/R/isolatedR.html){:target="_blank"}

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

!!! info "Installation principle"

    - install on Rackham
    - sync to ``wharf``
    - move the files on Bianca

!!! info "More info"

    - [Extra material: Installing Julia packages](https://uppmax.github.io/bianca_workshop/julia/){:target="_blank"}
    - [Julia course: isolated environments](https://uppmax.github.io/R-python-julia-HPC/julia/isolatedJulia.html){:target="_blank"}

## "Containers"

!!! info
   
    - Containers let you install programs without needing to think about the computer environment, like    
        - operative system
        - dependencies (libraries and other programs) with correct versions
    - Everything is included
    - Draw-backs
        - you install also things that may be already installed
        - therefore, probably more disk space is needed

!!! info "More info"

    - [Extra material: Containers](https://uppmax.github.io/bianca_workshop/containers/)



!!! abstract "Keypoints"
    - You have got an overview of the procedures to install packages/libraries and tools on Bianca through the ``wharf``
    - If you feel uncomfortable or think that many users would benefit from the software, ask the support to install it.

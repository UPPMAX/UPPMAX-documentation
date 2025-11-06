# Python bundles

## Introduction

- The bundle names reflect the content, like Python packages, but also which Python version, compilers and libraries that are compatible with it.

- The module endings may contain GCCcore-X.Y.Z and/or [YEAR-a/b].
    - GCCcore reflects the GCC compiler version that is compatible when using C/C++ "back end" code.
    - The year reflects an EasyBuild toolchain, see [FOSS toolchains](https://docs.easybuild.io/common-toolchains/#common_toolchains_overview_foss).

!!! info "FOSS tool chains and Python version using them"

    FOSS | Python version
    -----| --------------
    2023b| 3.11.5
    2024a| 3.12.3

!!! warning

    - Make sure to use bundles that are compatible with each-other and with needed Python version.
    - Otherwise it is better to create isolated environments with Conda or virtual environments, see [Virtual environments in Python](python_virtual_environments.md).

## Biopython

Biopython is a set of freely available tools for biological
 computation written in Python by an international team of developers. It is
 a distributed collaborative effort to develop Python libraries and
 applications which address the needs of current and future work in
 bioinformatics.

- Homepage: <https://www.biopython.org>

!!! info "Main package(s)"

    - biopython
  
!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "1.84-foss-2024a"

        Some dependencies

        - Python/3.12.3-GCCcore-13.3.0
        - SciPy-bundle/2024.05-gfbf-2024a
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0

## IPython

IPython provides a rich architecture for interactive computing with:

- Powerful interactive shells (terminal and Qt-based).
- A browser-based notebook with support for code, text, mathematical expressions, inline plots and other rich media.
- Support for interactive data visualization and use of GUI toolkits.
- Flexible, embeddable interpreters to load into your own projects.
- Easy to use, high performance tools for parallel computing.

!!! info "Main package(s)"

    - ipython
    - matplotlib-inline

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "8.28.0-GCCcore-13.3.0"

        Dependencies

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0

## JupyterLab

JupyterLab is the next-generation user interface for Project Jupyter offering all the familiar
 building blocks of the classic Jupyter Notebook (notebook, terminal, text editor, file browser, rich outputs,
 etc.) in a flexible and powerful user interface. JupyterLab will eventually replace the classic Jupyter
 Notebook.

- Homepage: <https://jupyter.org/>

!!! info "Main package(s)"

    -  jupyterlab

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "4.2.5-GCCcore-13.3.0"

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - IPython/8.28.0-GCCcore-13.3.0

## mpi4py

MPI for Python (mpi4py) provides bindings of the Message Passing Interface (MPI) standard for
 the Python programming language, allowing any Python program to exploit multiple processors.

- Homepage: <https://github.com/mpi4py/mpi4py>

!!! info "Main package(s)"

    - mpi4py

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "3.1.5-gompi-2023b"

        - Python/3.11.5-GCCcore-13.2.0
        - OpenMPI/4.1.6-GCC-13.2.0

    ??? note "4.0.1-gompi-2024a"
    
        - Python/3.12.3-GCCcore-13.3.0
        - OpenMPI/5.0.3-GCC-13.3.0

## Python-bundle-PyPI

Bundle of Python packages from PyPI

- Homepage: <https://python.org/>

!!! info "Main package(s)"

    - Type ``ml help Python-bundle-PyPI/[version]`` on Pelle to see an output.

    Among others:

    - chardet
    - future
    - Jinja
    - pkginfo
    - psutil
    - Pygments
    - pydevtool
    - pytest
    - pytz
    - regex
    - Sphinx
    - threadpoolctl
    - toml
    - urllib
    
!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "2023.06-GCCcore-12.3.0"

        - Python/3.11.5-GCCcore-13.2.0
    
    ??? note "2023.10-GCCcore-13.2.0"

        - Python/3.11.5-GCCcore-13.2.0

    ??? note "2023.10-GCCcore-13.3.0"

        - Python/3.11.5-GCCcore-13.3.0
        
    ??? note "2024.06-GCCcore-13.3.0"

        - Python/3.12.3-GCCcore-13.3.0


## PyTorch

Tensors and Dynamic neural networks in Python with strong GPU acceleration.
PyTorch is a deep learning framework that puts Python first.

- Homepage: <https://pytorch.org/>

!!! info "Main package(s)"

    - torch

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "2.6.0-foss-2024a"

        - Python/3.12.3-GCCcore-13.3.0
        - OpenMPI/5.0.3-GCC-13.3.0
        
## SciPy-bundle

!!! info "Main package(s)"

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "2023.07-gfbf-2023a"

    ??? note "2023.11-gfbf-2023b"

    ??? note "2024.05-gfbf-2024a"
    
## sympy

!!! info "Main package(s)"

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "1.13.3-gfbf-2024a"


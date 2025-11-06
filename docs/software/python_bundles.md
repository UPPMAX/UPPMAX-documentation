# Python bundles

## Introduction

- The bundle names reflect the content, like Python packages, and its version, but also which Python version, compilers and libraries that are compatible with it.

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

    - jupyterlab

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "4.2.5-GCCcore-13.3.0"

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - IPython/8.28.0-GCCcore-13.3.0

## matplotlib

matplotlib is a python 2D plotting library which produces publication quality figures in a variety of
 hardcopy formats and interactive environments across platforms.

matplotlib can be used in python scripts, the
python
 and ipython shell, web application servers, and six graphical user interface toolkits.

- Homepage: <https://matplotlib.org>

!!! info "Main package(s)"

    - contourpy
    - Cycler
    - fonttools
    - kiwisolver
    - matplotlib

!!! tip "Load this version and get many other bundles on the fly!"

    Included are

    - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
    - SciPy-bundle/2024.05-gfbf-2024a

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "3.9.2-gfbf-2024a"

        Packages
        
        - contourpy-1.3.0
        - Cycler-0.12.1
        - fonttools-4.53.1
        - kiwisolver-1.4.5
        - matplotlib-3.9.2

        Dependencies

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - SciPy-bundle/2024.05-gfbf-2024a

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

## numba

Numba is an Open Source NumPy-aware optimizing compiler for
Python sponsored by Continuum Analytics, Inc. It uses the remarkable LLVM
compiler infrastructure to compile Python syntax to machine code.

- Homepage: https://numba.pydata.org/

!!! info "Main package(s)"

    - numba
    - llvmlite
    
!!! tip " Are you on a GPU node?"

    - Load a CUDA module and numba will use the GPU!

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "numba/0.60.0-foss-2024a"

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - SciPy-bundle/2024.05-gfbf-2024a
        
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
        
## scikit-learn

Scikit-learn integrates machine learning algorithms in the tightly-knit scientific Python world,
building upon numpy, scipy, and matplotlib. As a machine-learning module,
it provides versatile tools for data mining and analysis in any field of science and engineering.
It strives to be simple and efficient, accessible to everybody, and reusable in various contexts.

- Homepage: <https://scikit-learn.org/stable/index.html>

!!! info "Main package(s)"

    - scikit-learn (sklearn as alias)

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "1.6.1-gfbf-2024a"

        Packages
        
        - scikit-learn-1.6.1

        Dependencies

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - SciPy-bundle/2024.05-gfbf-2024a
        
## SciPy-bundle

Bundle of Python packages for scientific software

- Homepage: <https://python.org/>

!!! info "Main package(s)"

    - numpy
    - pandas
    - scipy

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "2023.07-gfbf-2023a"

        Packages
        
        - numpy-1.25.1
        - pandas-2.0.3
        - scipy-1.11.1

        Dependencies

        - Python/3.11.3-GCCcore-12.3.0
        - Python-bundle-PyPI/2023.06-GCCcore-12.3.0
        
    ??? note "2023.11-gfbf-2023b"

        Packages
        
        - numpy-1.26.2
        - pandas-2.1.3
        - scipy-1.11.4

        Dependencies

        - Python/3.11.5-GCCcore-13.2.0
        - Python-bundle-PyPI/2023.10-GCCcore-13.2.0
        
    ??? note "2024.05-gfbf-2024a"

        Packages
        
        - numpy-1.26.4
        - pandas-2.2.2
        - scipy-1.13.1

        Dependencies

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0

    
## sympy

SymPy is a Python library for symbolic mathematics. It aims to
 become a full-featured computer algebra system (CAS) while keeping the code as
 simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python and does not require any external libraries.

- Homepage: <https://sympy.org/>

!!! info "Main package(s)"

    - sympy

!!! info "Installed versions"

    Versions and dependencies
    
    ??? note "1.13.3-gfbf-2024a"

        - Python/3.12.3-GCCcore-13.3.0
        - Python-bundle-PyPI/2024.06-GCCcore-13.3.0
        - SciPy-bundle/2024.05-gfbf-2024a

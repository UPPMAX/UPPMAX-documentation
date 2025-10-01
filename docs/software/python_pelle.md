# Python on Pelle

![The Python logo](img/python_logo.png)

Welcome to the UPPMAX Python user guide for [Pelle cluster](../cluster_guides/pelle.md).

Here we, as a start, present Pelle specific topics that are different from Bianca and Rackham

We describe that there are [multiple Python versions](#python-versions).

Then, we show how to [load Python](#loading-python)
and to [load Python packages](#loading-python-packages).

## Python versions

Python (or to be precise: the Python interpreter) has different versions.
The current major version of Python is Python 3.
Python 3 is not backwards compatible with Python 2.
This means that you need to use the correct Python version
to run a Python script.

???- question "Which version of Python is `python`?"

    To determine which version `python` is, in a [terminal](../software/terminal.md), type:

    ```bash
    python --version
    ```

    to see which Python version you are using now.

???- question "Which version of Python is `python3`?"

    To determine which version `python3` is, in a terminal, type:

    ```bash
    python3 --version
    ```

    to see which Python version you are using now.

## Loading Python

The different versions of Python are available via
the module system on all UPPMAX clusters.
Loading a Python module also makes some Python packages available.

???- question "Forgot what the module system is?"

    See [the UPPMAX pages on the module system](../cluster_guides/modules.md).

???- question "UPPMAX modules or Python modules?"

    At this page, we will use the word 'modules' for UPPMAX modules
    and 'packages' for Python modules, to be clear in what is meant.
    The word 'package' is used in multiple other languages, such as R,
    with a similar definition as a Python module.

To find out which Python modules there are, use `module spider python`.

???- question "What is the output of that command?"

    The output of `module spider python` on the day of writing, is:

    ```bash
    [user@pelle ~]$ module spider python

    ---------------------------------------------------------------------------------------------------------------------------------------
      Python:
    ---------------------------------------------------------------------------------------------------------------------------------------
    Description:
      Python is a programming language that lets you work more quickly and integrate your systems more effectively.

     Versions:
        Python/2.7.15-fosscuda-2018b
        Python/2.7.18-GCCcore-10.2.0
        Python/2.7.18-GCCcore-13.3.0
        Python/3.7.4-GCCcore-8.3.0
        Python/3.8.6-GCCcore-10.2.0
        Python/3.9.6-GCCcore-11.2.0-bare
        Python/3.9.6-GCCcore-11.2.0
        Python/3.10.4-GCCcore-11.3.0-bare
        Python/3.10.4-GCCcore-11.3.0
        Python/3.11.3-GCCcore-12.3.0
        Python/3.11.3-GCCcore-13.3.0
        Python/3.11.5-GCCcore-13.2.0
        Python/3.11.5-GCCcore-13.3.0
        Python/3.12.3-GCCcore-13.3.0
        Python/3.13.1-GCCcore-14.2.0
     Other possible modules matches:
        Biopython  IPython  Python-bundle-PyPI 

    ---------------------------------------------------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*python.*'

    -------------------------------------------------------------------------------------------------------------------------
      For detailed information about a specific "Python" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:
     
         $ module spider Python/3.13.1-GCCcore-14.2.0
    -------------------------------------------------------------------------------------------------------------------------
    ```

To load a specific version of Python into your environment,
type `module load python/[version]`,
where `[version]` is a Python version,
for example, `module load Python/3.11.5-GCCcore-13.2.0`

???- question "Do I really need to load a Python module?"

    It is *recommended* to load a Python module,
    but in some case you will not get into trouble.

    When you do not load a module, the system-installed Python version are used.
    These is `python` version 3.9.21.

    If using those older versions give you no trouble, all is well,
    for example, when running basic Python scripts that have no package imports.

    However, when any problem occurs, load those newer modules.

After loading a Python module,
one can start the Python interpreter:

```bash
python
```

???- question "How does this look like?"

     After loading ``Python/3.13.1-GCCcore-14.2.0`` and starting the Python interpreter with ``python`` it looks like this:

     ```bash
     Python 3.13.1 (main, Jun 11 2025, 16:22:31) [GCC 14.2.0] on linux
     Type "help", "copyright", "credits" or "license" for more information.
     >>>
     ```

!!! warning

    The sections below needs updates

## Loading Python package modules

!!! note "Terminology"

    A Python package consists out of one or more Python modules.
    in this document, we avoid using this term,
    to avoid confusion with [the UPPMAX modules](../cluster_guides/modules.md).

For more complex complex Python packages,
there exist [UPPMAX modules](../cluster_guides/modules.md) to load these:

- `python_GIS_packages`: for geographic information system packages
- `python_ML_packages`: for machine learning Python packages

???- question "How could I find these modules myself?"

    Use:

    ```bash
    module spider packages
    ```

## Loading Python packages

!!! note "Terminology"

    A Python package consists out of one or more Python modules.
    in this document, we avoid using this term,
    to avoid confusion with [the UPPMAX modules](../cluster_guides/modules.md).

Many scientific tools are distributed as Python packages,
which allows any user to run complex tools from a terminal or script.
For example, the following Python code imports the functionality
of the `pandas` library:

```python
import pandas
```

Some packages/tools are preinstalled on all UPPMAX clusters.
To load such a package:

- determine if it comes with your Python version
- determine if it comes as a module

### Determine if a Python package comes with your Python module

To determine if a Python package comes with your Python module,
there are multiple ways:

- Using `pip list`
- Using the module help
- Importing the package

#### Using `pip list`

To determine if a Python package comes with your Python module,
`pip list` is one of the ways to do so.

On a terminal, type:

```bash
pip list
```

This shows a list of Python packages that are installed.

???- question "How does the output of `pip list` look like?"

    Here is an example:

    ```console
    Package                   Version
    ------------------------- ---------------
    anndata                   0.10.5.post1
    anyio                     4.2.0
    appdirs                   1.4.4
    argon2-cffi               23.1.0
    argon2-cffi-bindings      21.2.0
    [more Python packages]
    Werkzeug                  3.0.1
    wheel                     0.42.0
    widgetsnbextension        4.0.9
    zipp                      3.17.0
    zope.interface            6.1
    ```

#### Using the module help

Determine if a Python package comes with your Python module
using the module help, in a terminal, type:

```bash
module help Python/[module_version]
```

where `[module_version]` is a version of a Python module,
for example:

```bash
module help Python/3.13.1-GCCcore-14.2.0
```

???- question "What is the output of `module help Python/3.13.1-GCCcore-14.2.0`?"

    ```console
    --------------------------------- Module Specific Help for "Python/3.13.1-GCCcore-14.2.0" ----------------------------------
    
    Description
    ===========
    Python is a programming language that lets you work more quickly and integrate your systems
     more effectively.
    
    
    More information
    ================
     - Homepage: https://python.org/
    
    
    Included extensions
    ===================
    flit_core-3.10.1, packaging-24.2, pip-24.3.1, setuptools-75.6.0,
    setuptools_scm-8.1.0, tomli-2.2.1, typing_extensions-4.12.2, wheel-0.45.1
    ```

!!! warning

    - Note that the ordinary Python module contains much fewer packages than the ones on Bianca, Rackham and Snowy
    - It does though contain the so called "base", including packages like ``sys`` and ``math``.

#### Importing the package

Importing a Python package is a way to determine if a Python package
comes with your Python module installed.
From the terminal do:

```bash
python -c "import [your_package]"
```

???- question "What does that `-c` do?"

    `python -c` will run the text after it as Python code.
    In this way, you can directly run code, i.e.
    you do not need to create a file to run.

where `[your_package]` is the name of a Python package,
for example:

```bash
python -c "import pandas"
```

???- question "What is the output if the Python package is found?"

    The output if the Python package is found is nothing.

???- question "What is the output if the Python package is not found?"

    Here an absent package is loaded, with the nonsense name `absentpackage`:

    ```bash
    python -c "import absentpackage"
    ```

    This results in the following error:

    ```console
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ModuleNotFoundError: No module named 'absentpackage'
    ```

#### Determine if a Python package comes with a module

If the Python package is not pre-installed with your version of Python,
use [the UPPMAX module system](../cluster_guides/modules.md)
to search for it.

Not all packages are easy to find,
as some are part of super-packages,
for example [the TensorFlow Python libraries](tensorflow.md),
which are part of the `python_ML_packages/[version]-{cpu,gpu}`,
for example `python_ML_packages/3.11.8-cpu`.

???- question "Want to see a list of Python packages in `python_ML_packages/3.11.8-cpu` that are not in `python/3.11.8`?"

    Here you go:

    - absl-py
    - array-record
    - astunparse
    - cachetools
    - cons
    - dill
    - dm-tree
    - ducc0
    - etils
    - etuples
    - flatbuffers
    - gast
    - google-auth
    - google-auth-oauthlib
    - google-pasta
    - googleapis-common-protos
    - grpcio
    - imbalanced-learn
    - importlib_resources
    - keras
    - libclang
    - llvmlite
    - logical-unification
    - miniKanren
    - ml-dtypes
    - multipledispatch
    - nlp
    - numba
    - oauthlib
    - opt-einsum
    - patsy
    - promise
    - protobuf
    - pyasn1
    - pyasn1-modules
    - pytensor
    - requests-oauthlib
    - rsa
    - scikit-learn
    - seaborn
    - statsmodels
    - tensorboard
    - tensorboard-data-server
    - tensorflow-cpu
    - tensorflow-datasets
    - tensorflow-estimator
    - tensorflow-io-gcs-filesyst
    - tensorflow-metadata
    - tensorflow-probability
    - termcolor
    - threadpoolctl
    - toml
    - torch
    - torchaudio
    - torchvision
    - wrapt
    - xxhash

It may not always be easy to find your Python package within the many modules.
Do not hesitate to [contact support](../support.md)
so that you can spend time on your research
and we figure this out :-)


### Stand-alone tools

Some Python packages are working as stand-alone tools, for instance in
bioinformatics. The tool may be already installed as a module. Check if it is
there by using the module system `spider` function:

```bash
module spider [tool_name]
```

where `[tool_name]` is (part of) the name of the tool. `module spider`
is case-insensitive, hence `YourTool` and `yourtool` give similar results.

???- question "What are UPPMAX modules?"

    See [the page about the UPPMAX module system](../cluster_guides/modules.md)

## General things

General things can be found on the [general Python page](python.md).

- Running Python
- Use Python to run a Python script
- Use Python in an interactive session
- Programming in Python
- UPPMAX Python-related courses
- Installing Python packages


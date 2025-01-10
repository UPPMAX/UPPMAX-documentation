# Python user guide

![The Python logo](img/python_logo.png)

Welcome to the UPPMAX Python user guide.

We describe [what Python is](#what-is-python)
and that there are [multiple Python versions](#python-versions).

Then, we show how to [load Python](#loading-python)
and to [load Python packages](#loading-python-packages)
after which you can [run Python](#running-python).

Finally, you can find [UPPMAX Python-related courses](#uppmax-python-related-courses)
and these more advanced topics:

- [Programming in Python](python_programming.md)
- [Installing Python packages](python_install_packages.md)
- [Virtual environments in Python](python_virtual_environments.md)
- [How to run parallel jobs in Python](python_parallel_jobs.md)

## What is Python?

Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability
with the use of significant indentation [Kuhlman, 2009].

## Python versions

Python (or to be precise: the Python interpreter) has different versions.
The current major version of Python is Python 3.
Python 3 is not backwards compatible with Python 2.
This means that you need to use the correct Python version
to run a Python script.

???- question "Could you give me an example of a difference between Python 2 and 3?"

    One example is how Python 2 and Python 3 dividetwo integers.
    Here is an example that will work on all UPMMAX clusters.

    Load Python 2.7.15:

    ```bash
    module load python/2.7.15
    ```

    Then

    ```bash
    python -c "print(1/2)"
    ```

    will print `0`, as this is an integer division: two fits zero times in one.

    Load Python 3.11.4:

    ```bash
    module load python/3.11.4
    ```

    Then

    ```bash
    python -c "print(1/2)"
    ```

    will print `0.5`, as this is turned into a floating point division,
    equivalent to `1.0 / 2.0`.

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

???- question "Prefer seeing a video?"

    A video that shows how to load the Python
    [module](../cluster_guides/modules.md)
    can be found [here](https://youtu.be/wBebYj3XlNM).

The different versions of Python are available via
the module system on all UPPMAX clusters.
Loading a Python module also makes some Python packages available.

???- question "Forgot what the module system is?"

    See the UPPMAX pages on the module system [here](../cluster_guides/modules.md).

???- question "UPPMAX modules or Python modules?"

    At this page, we will use the word 'modules' for UPPMAX modules
    and 'packages' for Python modules, to be clear in what is meant.
    The word 'package' is used in multiple other languages, such as R,
    with a similar definition as a Python module.

To find out which Python modules there are, use `module spider python`.

???- question "What is the output of that command?"

    The output of `module spider python` on the day of writing, is:

    ```bash
    [user@rackham1 ~]$ module spider python

    ---------------------------------------------------------------------------------------
      python:
    ---------------------------------------------------------------------------------------
         Versions:
            python/2.7.6
            python/2.7.9
            python/2.7.11
            python/2.7.15
            python/3.3
            python/3.3.1
            python/3.4.3
            python/3.5.0
            python/3.6.0
            python/3.6.8
            python/3.7.2
            python/3.8.7
            python/3.9.5
            python/3.10.8
            python/3.11.4
         Other possible modules matches:
            Biopython  Boost.Python  GitPython  IPython  Python  biopython  flatbuffers-python
     ...

    ---------------------------------------------------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*python.*'

    ---------------------------------------------------------------------------------------
      For detailed information about a specific "python" package (including how to load the mod
    ules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider python/3.11.4
    ---------------------------------------------------------------------------------------
    ```

To load a specific version of Python into your environment,
type `module load python/[version]`,
where `[version]` is a Python version,
for example, `module load python/3.11.4`

???- question "Do I really need to load a Python module?"

    It is *recommended* to load a Python module,
    but in some case you will not get into trouble.

    When you do not load a module, the system-installed Python version are used.
    These are `python` version 2.7.5, and `python3` version 3.6.8.

    If using those older versions give you no trouble, all is well,
    for example, when running basic Python scripts that have no package imports.

    However, when any problem occurs, load those newer modules.

???- question "Why are there both ``python/3.X.Y`` and ``python3/3.X.Y`` modules?"

    Sometimes existing software might use `python2`
    and there’s nothing you can do about that.

    In pipelines and other toolchains the different tools may together
    require both `python2` and `python3`.

???- question "How to deal with tools that require both `python2` and `python3`?"

    You can run two python modules at the same time if
    one of the modules is `python/2.X.Y` and the other module is `python3/3.X.Y`
    (i.e. not `python/3.X.Y`).

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
module help python/[module_version]
```

where `[module_version]` is a version of a Python module,
for example:

```bash
module help python/3.11.4
```

???- question "What is the output of `module help python/3.11.4`?"

    Here is part of the output of `module help python/3.11.4`:

    ```console
    ------------------------ Module Specific Help for "python/3.11.4" -------------------------
        Python - use Python

        Version 3.11.4


    This module provides the executable names 'python' and 'python3'.

    Several additional python packages are also installed in this module. The complete list of
    packages in this module, produced using 'pip list', is:

    Package                   Version
    ------------------------- -----------
    anndata                   0.9.2
    anyio                     3.7.1
    argon2-cffi               21.3.0
    ...
    widgetsnbextension        4.0.8
    zipp                      3.16.2
    zope.interface            6.0
    ```

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

    See the page about the UPPMAX module system [here](../cluster_guides/modules.md)

## Running Python

You can run Python in multiple ways:

- use Python to run a Python script
- use Python in an interactive session

To *program* in Python, there are more ways,
which are discussed at the UPPMAX page on
Python programming [here](python_programming.md)

### Use Python to run a Python script

You can run a Python script in the shell by:

```console
python example_script.py
```

or, if you loaded a `python3` module:

```console
python3 example_script.py
```

### Use Python in an interactive session

You start a python session by typing:

```console
python
```

or

```console
python3
```

The python prompt looks like this:

```python
>>>
```

Exit with `<Ctrl-D>`, `quit()` or `exit()`.

## Programming in Python

To program in Python, there are more ways,
which are discussed at the UPPMAX page on
Python programming [here](python_programming.md)

## UPPMAX Python-related courses

See [the UPPMAX courses and workshops](../courses_workshops/courses_workshops.md)
to find UPPMAX courses related to Python.

## Installing Python packages

How to install Python packages
is described [here](python_install_packages.md).

## Virtual environments in Python

How to use virtual environments in Python
is described [here](python_virtual_environments.md).

## How to run parallel jobs in Python

How to run parallel jobs in Python
is described [here](python_parallel_jobs.md).

## References

- [Kuhlman, 2009] Kuhlman, Dave. A python book: Beginning python, advanced python, and python exercises. Lutz: Dave Kuhlman, 2009.

## Links

- [Official Python documentation](https://docs.python.org/3/)
- [Python forum](https://www.python.org/community/forums/)
- [Free online book: 'How to Think Like a Computer Scientist'](https://openbookproject.net/thinkcs/python/english3e/index.html)
- [UPPMAX TensorFlow guide](tensorflow.md)
- [UPPMAX PyTorch guide](pytorch.md)

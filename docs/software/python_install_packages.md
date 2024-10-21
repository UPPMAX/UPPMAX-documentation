---
tags:
  - pip
  - pip install
  - Python
  - package
---

# Installing Python packages

This page described how to install [Python](python.md) packages.

There are many ways to install a [Python](python.md) package:

- Using `setup.py`
- using a Python package installer
    - **PyPI** using [`pip`](#pip)
    - **Conda** using [`conda`](#conda)

You may want to [check if a package is already installed](#check-if-a-package-is-already-installed) first :-).

[The Python package installers are compared](#comparison-between-conda-and-pypi)
after which each is discussed:

- **PyPI** using [`pip`](#pip)
- **Conda** using [`conda`](#conda)

## Check if a package is already installed

There are multiple ways to check if a Python package is installed:

### 1. pip list

In the [terminal](../software/terminal.md), type:

```bash
pip list
```

You'll see a list of all installed packages.

### 2. import

Start Python. Then, within the Python interpreter, type:

```bash
import [package]
```

where `[package]` is the name of the Python package,
for example `import mkhcnuggets`.

Does it work? Then it is there!

## Comparison between Conda and PyPI

- **PyPI** (`pip`) is traditionally for Python-only packages but it is no problem to
also distribute packages written in other languages as long as they provide a
Python interface.

- **Conda** (`conda`) is more general and while it contains many Python packages and
packages with a Python interface, it is often used to also distribute packages
which do not contain any Python (e.g. C or C++ packages).

Parameter                    | `conda` | `pip`
-----------------------------|---------|-------
Installs Python packages     | Yes     | Yes
Installs non-Python software | Yes     | No

Many libraries and tools are distributed in both ecosystems.

## `pip`

`pip` is a popular Python package installer.

To install a Python package using `pip`,
in a terminal or Python shell, do:

```bash
pip install --user [package name]
```

where `[package name]` is the name of a Python package,
for example `pip install --user mhcnuggets`.

???- question "Can I also use `pip3`?"

    Yes, you can. The command then becomes:

    ```bash
    pip3 install --user [package name]
    ```

    For example `pip3 install --user mhcnuggets`.

    Most that applies to `pip` applies to `pip3`.

Due to using `--user`, the package ends up in
a subfolder of the user's home folder, which is `~/.local/lib/python[version]/site-packages/`,
where version is the Python version with only the major and minor version,
so for Python version 3.11.8, the folder will be `python3.11` (i.e. the patch number,
`8` is not included).

If you would like to have your packages installed in another folder, do:

```bash
pip install --prefix=[root_folder] [package name]
```

where `[root_folder]` is the root folder of the package installation,
for example `--prefix=~/.local`.
Using this root folder, this option is the same to using `--user`,
as described above.

When using a custom root folder, Python cannot find it without help.
Setting the environment variable `PYTHONPATH` to the correct folder
allows Python to find packages in a custom folder.

```bash
export PYTHONPATH=[root_folder]/lib/python[version]/site-packages/:$PYTHONPATH.
```

for example, when `[root_folder]` is `~/my_python_packages` and for using Python
3.11.8, this will be:

```bash
export PYTHONPATH=~/my_python_packages/lib/python3.11/site-packages/:$PYTHONPATH.
```

Consider adding this line to your `.bashrc` file,
so it is loaded every time you login.

## `conda`

See our [Conda user Guide](../software/conda.md)

## Using `setup.py`

Some Python packages are only available as downloads
and need to be installed using a Python script,
commonly called `setup.py`.

If that is the case for the package you need, this is how you do it:

- Pick a location for your installation
  (change below to fit - I am installing under a project storage)

    - ``mkdir /proj/<project>/<mystorage>/mypythonpackages``
    - ``cd /proj/<project>/<mystorage>/mypythonpackages``

- Load Python + (on Kebnekaise) site-installed prerequisites (SciPy-bundle, matplotlib, etc.)
- Install any remaining prerequisites. Remember to activate your Virtualenv if installing with pip!
- Download Python package, place it in your chosen installation dir, then untar/unzip it
- cd into the source directory of the Python package

    - Run ``python setup.py build``
    - Then install with: ``python setup.py install --prefix=<path to install dir>``

- Add the path to $HOME/.bash_profile (note that it will differ by Python version):

    - `export PYTHONPATH=$PYTHONPATH:<path to your install directory>/lib/python3.11/site-packages`

You can use it as normal inside Python (remember to load dependent modules as well as activate virtual environment if it depends on some packages you installed with pip): ``import <python-module>``

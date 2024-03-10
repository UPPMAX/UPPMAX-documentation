# Installing Python packages

This page described how to install Python packages.
For the general page about Python, see [here](python.md).

There are two package installation systems:

* **PyPI** (`pip`) is traditionally for Python-only packages but it is no problem to
also distribute packages written in other languages as long as they provide a
Python interface.

* **Conda** (`conda`) is more general and while it contains many Python packages and
packages with a Python interface, it is often used to also distribute packages
which do not contain any Python (e.g. C or C++ packages).

| Parameter                    | `conda` | `pip` |
|------------------------------|---------|-------|
| Installs Python packages     | Yes     | Yes   |
| Installs non-Python software | Yes     | No    |

Many libraries and tools are distributed in both ecosystems.

To make sure that the package is not already installed, type in python:

```bash
>>> import <module>
```
Does it work? Then it is there!

Otherwise, you can either use `pip` or `conda`.

### `pip`

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

```
export PYTHONPATH=[root_folder]/lib/python[version]/site-packages/:$PYTHONPATH.
```

for example, when `[root_folder]` is `~/my_python_packages` and for using Python
3.11.8, this will be:

```
export PYTHONPATH=~/my_python_packages/lib/python3.11/site-packages/:$PYTHONPATH.
```

Consider adding this line to your `.bashrc` file, 
so it is loaded every time you login.

### `conda`

See our [Conda user Guide](../cluster_guides/conda.md)


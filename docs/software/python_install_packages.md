# Installing Python packages

This page described how to install Python packages.
For the general page about Python, see [here](python.md).

There are two package installation systems

* **PyPI** (`pip`) is traditionally for Python-only packages but it is no problem to
also distribute packages written in other languages as long as they provide a
Python interface.

* **Conda** (`conda`) is more general and while it contains many Python packages and
packages with a Python interface, it is often used to also distribute packages
which do not contain any Python (e.g. C or C++ packages).

Many libraries and tools are distributed in both ecosystems.

To make sure that the package is not already installed, type in python:

```bash
>>> import <module>
```
Does it work? Then it is there!

Otherwise, you can either use `pip` or `conda`.

### `pip`

You use pip this way, in Linux shell or python shell:

```bash
$ pip install --user <package name>    # or pip3 if required from loaded python module
```
With --user, the package ends up in ~/.local/lib/python<version>/site-packages/ .

If you would like to have your packages in another place, like in your project directory do 

```bash
$ pip install --prefix=<path> <package name>
```

where prefix points to the "root" of the package installation. The
installations will placed in the directory `<prefix
path>/lib/pythonX.Y/site-packages/`. Note the needed replacement of `X.Y` and
that just the two first version numbers are needed.

To be able to find those packages with non-default path you have to set the
`PYTHONPATH` environment variable:

```
$ export PYTHONPATH=<prefix-path>/lib/pythonX.Y/site-packages/:$PYTHONPATH.
```

You may want to add this line in your `.bashrc` file!


### `conda`

See our [Conda user Guide](../cluster_guides/conda.md)


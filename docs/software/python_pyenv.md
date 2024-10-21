---
tags:
  - Python
  - pyenv
---

# Python `pyenv`

`pyenv` is one of multiple
[Python virtual environment managers](python_virtual_environments.md).

This approach is more advanced and should be, in our opinion, used only if the
above are not enough for the purpose. Probably Conda will work well for you.
The approach below allows you to install your own python version and much more…

Confer the official pyenv documentation.

## First time at UPPMAX

1. Download pyenv:

    ```bash
    git clone git://github.com/yyuu/pyenv.git ~/.pyenv
    ```

1. Make pyenv start when you login each time

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

To make sure everything gets loaded correctly, log out and back in to uppmax.

## Installing own python version (not already available as an UPPMAX module)

1. Get pyenv to install the python version of your liking.

    ```bash
    pyenv install 3.10.6
    ```

1. Make the version you just installed to the standard version for every time you run python.

    ```bash
    pyenv global 3.10.6
    ```

Now you should be all set. If you change your mind about which version of
Python to use, just redo this section and choose a different version. You can
also have multiple versions installed at the same time and just switch between
them usuing 'pyenv global' as shown above, if you have a script that requires
Python 3.3 or any other version.

## Install packages in your selected python version

1. Set python version with

    ```bash
    pyenv global <version>
    ```

1. Install packages in your python, use `pip`

    ```bash
    pip install [package name]
    ```

Example:

```bash
pip install mechanize
```

## Links

- CodeRefinery's course: [Python for Scientific Computing](https://aaltoscicomp.github.io/python-for-scicomp/).

# Isolated environments in Python

This page described how to use isolated environments in Python.
For the general pages on Python, go [here](python.md).

Good introduction at CodeRefinery's course in [Python for Scientific
Computing](https://aaltoscicomp.github.io/python-for-scicomp/).

Isolated environments solve a couple of problems:

* You can install specific, also older, versions into them.

* You can create one for each project and no problem if the two projects
require different versions.

* If you make some mistake and install something you did not want or need, you
can remove the environment and create a new one.

## Example with virtual environment

Create a `venv`. First load the python version you want to base your virtual
environment on. 

Example with `python/3.6.0`

```
$ module load python/3.6.0
$ python -m venv Example
```

* Here `Example` is the name of the virtual environment. It creates a new folder
called Example in the present working directory.

    If you want it in a certain place like `~/test/`:


    `$ python -m venv ~/test/Example`


* Activate it. To activate your newly created virtual environment locate the
script called `activate` and execute it.

    * `$ source Example/bin/activate`
    * Note that your prompt is changing to start with (Example) to show that you are within an environment.

* Install your packages, like `Numpy 1.13.1` and `Matplotlib 2.2.2`, into the virtual environment:
* `(Example) $ pip install numpy==1.13.1 matplotlib==2.2.2`
* Deactivate it:
    `(Example) $ deactivate`

Everytime you need the tools available in the virtual environment you activate it as above.

!!! note
    To save space, you should load any other Python modules you will need that are
    system installed before installing your own packages! Remember to choose ones
    that are compatible with the Python version you picked! --system-site-packages
    includes the packages already installed in the loaded python module.

    Example from above:

    ```python -m venv --system-site-packages Example```

    See further down how to use Jupyter from an isolated session where you used
`--system-site-packages`.

[More on virtual environment](https://docs.python.org/3/library/venv.html)

## Installing with `pyenv`

This approach is more advanced and should be, in our opinion, used only if the
above are not enough for the purpose. Probably Conda will work well four you.
The approach below allows you to install your own python version and much more… 

Confer the official pyenv documentation.

### First time at UPPMAX

1. Download pyenv:

    ```git clone git://github.com/yyuu/pyenv.git ~/.pyenv```

2. Make pyenv start when you login each time

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

To make sure everything gets loaded correctly, log out and back in to uppmax.

### Installing own python version (not already available as an UPPMAX module)

1. Get pyenv to install the python version of your liking.

    ```pyenv install 3.10.6```

1. Make the version you just installed to the standard version for every time you run python.

    ```pyenv global 3.10.6```

Now you should be all set. If you change your mind about which version of
Python to use, just redo this section and choose a different version. You can
also have multiple versions installed at the same time and just switch between
them usuing 'pyenv global' as shown above, if you have a script that requires
Python 3.3 or any other version.

## Install packages in your selected python version


1. Set python version with 

    ```pyenv global <version>```

1. Install packages in your python, use `pip`

    ```
    pip install [package name]
    ```

Example:
```
pip install mechanize
```

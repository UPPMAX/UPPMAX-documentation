# Python `venv`

`venv` is one of multiple 
[Python virtual environment managers](python_virtual_environments.md).

`venv` is a environment manager
and is [an official Python library](https://docs.python.org/3/library/venv.html).

Here it is described, using `venv` ...

- how to create an environment
- how to activate an environment
- how to deactivate an environment

### `venv`: create an environment

A virtual environment can be created in multiple ways, 
for example, from scratch, which is not recommended.

Here we discuss the recommended way to create a virtual environment,
which has these steps:
1. Load a Python module or a modules with Python packages
1. Create the virtual environment

The first step is described at 
['Loading Python'](http://docs.uppmax.uu.se/software/python/#loading-python)
and 
['Loading Python package modules'](http://docs.uppmax.uu.se/software/python/#loading-python-modules)

```
module load python/3.6.0
```


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

### `venv`: activate an environment

* Activate it. To activate your newly created virtual environment locate the
script called `activate` and execute it.

    * `$ source Example/bin/activate`
    * Note that your prompt is changing to start with (Example) to show that you are within an environment.

* Install your packages, like `Numpy 1.13.1` and `Matplotlib 2.2.2`, into the virtual environment:
* `(Example) $ pip install numpy==1.13.1 matplotlib==2.2.2`

### `venv`: deactivate an environment

* Deactivate it:
    `(Example) $ deactivate`

Everytime you need the tools available in the virtual environment you activate it as above.

### `venv`: optimization

To save space, you should load any other Python modules you will need that are
system installed before installing your own packages. 
Remember to choose ones
that are compatible with the Python version you picked. 
`--system-site-packages` includes the packages already installed in the 
loaded Python module.

Example from above:

```
python -m venv --system-site-packages Example
```

See further down how to use Jupyter from an isolated session where you used
`--system-site-packages`.

## Links

- CodeRefinery's course: [Python for Scientific Computing](https://aaltoscicomp.github.io/python-for-scicomp/).

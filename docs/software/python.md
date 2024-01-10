# Python user guide

Welcome to the UPPMAX Python user guide.

We describe [what Python is](#what-is-python)
and that there are [multiple Python versions](Python versions).

Then, we show how to [load Python](#loading-python)
and to [load Python packages](#loading-python-packages)
after which you can [run Python](#running-python).

Finally, you can find [UPPMAX Python-related courses](#uppmax-python-related-courses)
and these more advanced topics:

- [Installing Python packages](#installing-python-packages)
- [Isolated environments in Python](python_venv.md)
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

## Loading Python

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

## Loading Python packages

The external libraries, or dependencies, are called modules in Python. To
distinguish those from the module system of the tools in UPPMAX, we call them
packages as well.

* Python packages broaden the use of Python to almost infinity

* Instead of writing codes yourself there may be others that has done the same!

* Many scientific tools are distributed as python packages making it possible
to run a script in the prompt and there defining files to be analysed and
arguments defining exactly what to do.

Some packages are preinstalled. That means that they are available also on Bianca.

Some python packages are working as stand-alone tools, for instance in
bioinformatics. The tool may be already installed as a module. Check if it is
there by:

```bash
$ module spider <tool-name or tool-name part>
```

Using `module spider` lets you search regardless of upper- or lowercase
characters.

Check the pre-installed packages of a specific python module:
```bash
$ module help python/<version>
```

or with python module loaded (more certain), in shell:

```bash
$ list
```

You can also test from within python session to make sure that the package is not already installed:
```python
>>> import <package>
```
A very small selection of installed packages are:

1. `cffi`
2. `Cython`
3. `GitPython`
4. `h5py`
5. `ipython`
6. `jupyter`  (-notebook, not -lab)
7. `kiwisolver`
8. `matplotlib`
9. `numpy`
10. `packaging`
11. `pandas`
12. `pip`
13. `pyQt5`
14. `pytest`
15. `qtconsole`
16. `scipy`

+ all "standard/internal" libraries.

In the python scripts or python prompt packages are imported or loaded by the commands ``import``. 

## Running Python

You can run Python in multiple ways:

- use Python to run a Python script
- use Python in an interactive session

### Use Python to run a Python script

You can run a Python script in the shell by:

```console
$ python example_script.py 
```
or, if you loaded a `python3` module:

```console
$ python3 example_script.py 
```

### Use Python in an interactive session

You start a python session by typing:

```console
$ python
```

or

```console
$ python3
```

The python prompt looks like this:

```python
>>>
```
Exit with `<Ctrl-D>`, `quit()` or `exit()`.

## UPPMAX Python-related courses

There are these UPPMAX courses related to Python:

- 'Introduction to Python' connected to our [introduction week course](https://www.uppmax.uu.se/support/courses-and-workshops/introductory-course-summer-2023/)
- 1-day workshop 'Using Python in a HPC environment'
- 3-day course on Python, Julia and R

## References

 * [Kuhlman, 2009] Kuhlman, Dave. A python book: Beginning python, advanced python, and python exercises. Lutz: Dave Kuhlman, 2009.

## Links

* [Official Python documentation](https://docs.python.org/3/)
* [Python forum](https://www.python.org/community/forums/)
* [UPPMAX TensorFlow guide](https://www.uppmax.uu.se/support/user-guides/tensorflow-user-guide/)
* [UPPMAX PyTorch guide](https://www.uppmax.uu.se/support/user-guides/nvidia-deep-learning-frameworks/)

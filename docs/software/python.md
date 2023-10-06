# Python user guide

## Courses

There are three UPPMAX courses related to python.
- Introduction to Python connected to our [introduction week course](https://www.uppmax.uu.se/support/courses-and-workshops/introductory-course-summer-2023/).
- 1-day workshop Using Python in a HPC environment 
- 3-day course on Python, Julia and R.


## Python installations

Different versions of Python are already available via the module system on Rackham, Snowy, Bianca and Irma. Some installed packages are available via the loaded module. 

As of the time of writing we have the following modules:
``` tcl
[user@rackham1 ~]$ module available python
------------------------------------------------------
python:
------------------------------------------------------
Versions:
   python/2.7.6     python/3.3      python/3.6.0    python/3.9.5         python3/3.7.2
   python/2.7.9     python/3.3.1    python/3.6.8    python/3.10.8 (D)    python3/3.8.7
   python/2.7.11    python/3.4.3    python/3.7.2    python3/3.6.0        python3/3.9.5
   python/2.7.15    python/3.5.0    python/3.8.7    python3/3.6.8        python3/3.10.8 (D)
 
   Where:
   D:  Default Module

```

To load a specific version of Python into your environment, type e.g. ``module load python/3.8.7``.
There is a system-installed ``python`` (``2.7.5``), and ``python3`` (``3.6.8``) on the cluster, but these are not recommended to use for your purposes.
Be aware of that this version will be used if you are not loading any python module.
Why are there both ``python/3.X.Y`` and ``python3/3.X.Y`` modules?

Sometimes existing software might use ``python2`` and there’s nothing you can do about that. In pipelines and other toolchains the different tools may together require both python2 and python3. Here’s how you handle that situation:

You can run two python modules at the same time if ONE of the module is python/2.X.Y and the other module is python3/3.X.Y (not python/3.X.Y).

You can run a python script in the shell by:
```console
$ python example_script.py 
```
or, if you loaded a python3 module:
```console
$ python3 example_script.py 
```
You start a python session by typing:
```console
$ python
```
or
```console
$ python3
```

The python prompt looks like this:

``` python
>>>
```
​Exit with <Ctrl-D>, "quit()" or 'exit()'. 

## Introduction

Python is, according to the official home page:

Python is a great object-oriented, interpreted, and interactive programming language. It is often compared  to Lisp, Tcl, Perl, Ruby, C#, Visual Basic, Visual Fox Pro, Scheme or Java... and it's much more fun.

Python combines remarkable power with very clear syntax. It has modules, classes, exceptions, very high level dynamic data types, and dynamic typing. There are interfaces to many system calls and libraries, as well as to various windowing systems. New built-in modules are easily written in C or C++ (or other languages, depending on the chosen implementation). Python is also usable as an extension language for applications written in other languages that need easy-to-use scripting or automation interfaces. 

Useful links:

    Official documentation
    Python forum

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
$ py
```
or
```console
$ python3
```

The python prompt looks like this:

``` py
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
Packages, modules, and dependencies
The external libraries, or dependencies, are called modules in python. To distinguish those from the module system of the tools in UPPMAX, we call them packages as well.

Python packages broaden the use of python to almost infinity!

Instead of writing codes yourself there may be others that has done the same!

Many scientific tools are distributed as python packages making it possible to run a script in the prompt and there defining files to be analysed and arguments defining exactly what to do.

Some packages are preinstalled. That means that they are available also on Bianca.

Some python packages are working as stand-alone tools, for instance in bioinformatics. The tool may be already installed as a module. Check if it is there by:

$ module spider <tool-name or tool-name part>
Using module spider lets you search regardless of upper- or lowercase characters.

Check the pre-installed packages of a specific python module:

$ module help python/<version>
or with python module loaded (more certain), in shell:

$ list
You can also test from within python session to make sure that the package is not already installed:

>>> import <package>
A very small selection of installed packages are:

  "cffi"
  "Cython"
  "GitPython"
  "h5py"
  "ipython"
  "jupyter"  (-notebook, not -lab)
  "kiwisolver"
  "matplotlib"
  "numpy"
  "packaging"
  "pandas"
  "pip"
  "pyQt5
  "pytest"
  "qtconsole"
  "scipy"
+ all "standard/internal" libraries.

In the python scripts or python prompt packages are imported or loaded by the commands ``import``. 

## How to install packages

There are two package installation systems

PyPI (pip) is traditionally for Python-only packages but it is no problem to also distribute packages written in other languages as long as they provide a Python interface.

Conda (conda) is more general and while it contains many Python packages and packages with a Python interface, it is often used to also distribute packages which do not contain any Python (e.g. C or C++ packages).

Many libraries and tools are distributed in both ecosystems.

To make sure that the package is not already installed, type in python:

>>> import <module>
Does it work? Then it is there!

Otherwise, you can either use "pip" or "Conda".

### Pip

You use pip this way, in Linux shell or python shell:

   $ pip install --user <package name>    # or pip3 if required from loaded python module
With --user, the package ends up in ~/.local/lib/python<version>/site-packages/ .

If you would like to have your packages in another place, like in your project directory do 

$ pip install --prefix=<path> <package name>
where prefix points to the "root" of the package installation. The installations will placed in the directory <prefix path>/lib/pythonX.Y/site-packages/ . Note the needed replacement of "X.Y" and that just the two first version numbers are needed.

To be able to find those packages with non-default path you have to set the PYTHONPATH environment variable:

$ export PYTHONPATH=<prefix-path>/lib/pythonX.Y/site-packages/:$PYTHONPATH.
You may want to add this line in your .bashrc file!


### Conda

See our [Conda user Guide](../cluster_guides/conda.md)



## Isolated environments
Good introduction at CodeRefinery's course in Python for Scientific Computing .

Isolated environments solve a couple of problems:

You can install specific, also older, versions into them.

You can create one for each project and no problem if the two projects require different versions.

If you make some mistake and install something you did not want or need, you can remove the environment and create a new one.

### Example with virtual environment
Create a "venv". First load the python version you want to base your virtual environment on. 

Example with python/3.6.0

$ module load python/3.6.0
$ python -m venv Example
Here "Example" is the name of the virtual environment. It creates a new folder called Example in the present working directory.

If you want it in a certain place like “~/test/”:

$ python -m venv ~/test/Example
Activate it. To activate your newly created virtual environment locate the script called activate and execute it.

$ source Example/bin/activate
Note that your prompt is changing to start with (Example) to show that you are within an environment.
Install your packages, like Numpy 1.13.1 and Matplotlib 2.2.2, into the virtual environment:
(Example) $ pip install numpy==1.13.1 matplotlib==2.2.2
Deactivate it:

(Example) $ deactivate
Everytime you need the tools available in the virtual environment you activate it as above.

To save space, you should load any other Python modules you will need that are system installed before installing your own packages! Remember to choose ones that are compatible with the Python version you picked! --system-site-packages includes the packages already installed in the loaded python module.

Example from above:

python -m venv --system-site-packages Example
See further down how to use Jupyter from an isolated session where you used --system-site-packages.

More on virtual environment

### Installing with pyenv

This approach is more advanced and should be, in our opinion, used only if the above are not enough for the purpose. Probably Conda will work well four you. The approach below allows you to install your own python version and much more… 

Confer the official pyenv documentation.  

#### First time at UPPMAX

1. Download pyenv

git clone git://github.com/yyuu/pyenv.git ~/.pyenv
2. Make pyenv start when you login each time

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
To make sure everything gets loaded correctly, log out and back in to uppmax.

#### Installing own python version (not already available as an UPPMAX module)

1. Get pyenv to install the python version of your liking.

pyenv install 3.10.6

2. Make the version you just installed to the standard version for every time you run python.

pyenv global 3.10.6

Now you should be all set. If you change your mind about which version of Python to use, just redo this section and choose a different version. You can also have multiple versions installed at the same time and just switch between them usuing 'pyenv global' as shown above, if you have a script that requires Python 3.3 or any other version.

Install packages in your selected python version

1. Set python version with 

pyenv global <version>
2 Install packages in your python, use pip

pip install [package name]
Example:

pip install mechanize


## Running Python from Jupyter notebook (and -lab)
You can run Python in a notebook, i.e. in a web interface with possibility of inline figures and debugging. An easy way to do this is to load the python module as well. In shell:

module load python/<version>
jupyter-notebook
A Firefox session should start with the Jupyter notebook interface. If not,  copy-paste one of the addresses into the address files in an open firefox session.

Presently we have jupyter-lab only installed for python>=3.10.8. You can install a personal version with Conda for lower versions.

### Jupyter in a virtual environment (venv)
You could also use jupyter- (lab or notebook) in a virtual environment.

If you decide to use the --system-site-packages configuration you will get jupyter from the python modules you created you virtual environment with.
However, you won't find your locally installed packages from that jupyter session. To solve this reinstall jupyter within the virtual environment by force:

$ pip install -I jupyter
and run:

$ jupyter-notebook
Be sure to start the kernel with the virtual environment name, like "Example", and not "Python 3 (ipykernel)".

## How to run parallel jobs

Material here is taken partly from the parallel part of the online course Python for Scientific Computing 

Parallel computing is when many different tasks are carried out simultaneously. There are three main models:

Embarrassingly parallel: the code does not need to synchronize/communicate with other instances, and you can run multiple instances of the code separately, and combine the results later. If you can do this, great! (array jobs, task queues)

Shared memory parallelism: Parallel threads need to communicate and do so via the same memory (variables, state, etc). (OpenMP)

Message passing: Different processes manage their own memory segments. They share data by communicating (passing messages) as needed. (Message Passing Interface (MPI)).

There are several packages available for Python that let you run parallel jobs. Some of them are only able to run on one node, while others try to leverage several machines. 

### Threading

Threading divides up your work among a number of cores within a node. The threads shares its memory.

- Multi-threading documentation
- Examples


The designers of the Python language made the choice that only one thread in a process can run actual Python code by using the so-called global interpreter lock (GIL). This means that approaches that may work in other languages (C, C++, Fortran), may not work in Python without being a bit careful. At first glance, this is bad for parallelism. But it’s not all bad!:

External libraries (NumPy, SciPy, Pandas, etc), written in C or other languages, can release the lock and run multi-threaded. Also, most input/output releases the GIL, and input/output is slow.

If speed is important enough you need things parallel, you usually wouldn’t use pure Python.

More on the global interpreter lock

Threading python module. This is very low level and you shouldn’t use it unless you really know what you are doing.

We recommend you find a UNIX threading tutorial first before embarking on using the threading module.

### Distributed computing

As opposed to threading, Python has a reasonable way of doing something similar that uses multiple processes.

Distributed processing uses individual processes with individual memory, that communicate with each other. In this case, data movement and communication is explicit.
Python supports various forms of distributed computing.

    A native master-worker system based on remote procedure calls: multiprocessing.py
    MPI through mpi4py : a Python wrapper for the MPI protocol, see further down
If choosing between multiprocessing and MPI, distributed is easier to program, whereas MPI may be more suitable for multi-node applications.

#### Multiprocessing/distributed

The interface is a lot like threading, but in the background creates new processes to get around the global interpreter lock.

There are low-level functions which have a lot of the same risks and difficulties as when using threading.

To show an example, the split-apply-combine or map-reduce paradigm is quite useful for many scientific workflows. Consider you have this:

def square(x):
return x*x
You can apply the function to every element in a list using the map() function:

>>>list(map(square, [1, 2, 3, 4, 5, 6]))
[1, 4, 9, 16, 25, 36]
The multiprocessing.pool.Pool class provides an equivalent but parallelized (via multiprocessing) way of doing this. The pool class, by default, creates one new process per CPU and does parallel calculations on the list:

>>>from multiprocessing import Pool
>>>with Pool() as pool:
...    pool.map(square, [1, 2, 3, 4, 5, 6])
[1, 4, 9, 16, 25, 36]
As you can see, you can run distributed computing directly from the python shell. 

Another example, distributed.py: 

import random
def sample(n):
    """Make n trials of points in the square.  
    Return (n, number_in_circle)
    This is our basic function.  
    By design, it returns everything it needs to compute 
    the final answer: both n (even though it is an input
    argument) and n_inside_circle.  
    To compute our final answer, all we have to do is 
    sum up the n:s and the n_inside_circle:s and do our
    computation"""
    n_inside_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1.0:
            n_inside_circle += 1
    return n, n_inside_circle
import multiprocessing.pool
pool = multiprocessing.pool.Pool()
# The default pool makes one process per CPU
#%%timeit
# Do it once to time it
#results = pool.map(sample, [10**5] * 10)     # "* 10" would mean 10 processes
# Do it again to get the results, since the results of the above
# cell aren't accessible because of the %%timeit magic.
results = pool.map(sample, [10**5] * 10)
pool.close()
n_sum = sum(x[0] for x in results)
n_inside_circle_sum = sum(x[1] for x in results)
pi = 4.0 * (n_inside_circle_sum / n_sum)
print(pi)

##### Batch example

If you need to revive your knowledge about the scheduling system, please check Slurm user guide.

Batch script job_distributed.slurm:

#!/bin/bash
#SBATCH -A j<proj>
#SBATCH -p devel
#SBATCH --job-name=distr_py      # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=20              # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<email>
module load python/3.9.5
python distributed.py
​Put job in queue:

sbatch job_distributed.slurm

##### Interactive example 

salloc -A <proj> -p node -N 1 -n 10 -t 1:0:0 
python distributed.py

### MPI 
Presently you have to install your own mpi4py. You will need to activate paths to the MPI libraries. Therefore follow these steps.

1. If you use python 3.10.8: 

$ module load gcc/12.2.0 openmpi/4.1.4
     Otherwise:

$ module load gcc/9.3.0 openmpi/3.1.5
2. pip install locally or in an virtual environment

$ pip install --user mpi4py 
Remember that you will also have to load the the openmpi module before running mpi4py code, so that the MPI header files can be found (e.g. with the command "module load gcc/X.X.X openmpi/X.X.X"). Because of how MPI works, we need to explicitly write our code into a file,  pythonMPI.py:

import random
import time
from mpi4py import MPI
def sample(n):
    """Make n trials of points in the square.  
    Return (n, number_in_circle)
    This is our basic function.  
    By design, it returns everything it needs to compute 
    the final answer: both n (even though it is an input
    argument) and n_inside_circle.  
    To compute our final answer, all we have to do is 
    sum up the n:s and the n_inside_circle:s and do our
    computation"""
    n_inside_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 < 1.0:
            n_inside_circle += 1
    return n, n_inside_circle
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = 10 ** 7
if size > 1:
    n_task = int(n / size)
else:
    n_task = n
t0 = time.perf_counter()
_, n_inside_circle = sample(n_task)
t = time.perf_counter() - t0
  
print(f"before gather: rank {rank}, n_inside_circle: {n_inside_circle}")
n_inside_circle = comm.gather(n_inside_circle, root=0)
print(f"after gather: rank {rank}, n_inside_circle: {n_inside_circle}")
if rank == 0:
    pi_estimate = 4.0 * sum(n_inside_circle) / n
    print(f"\nnumber of darts: {n}, estimate: {pi_estimate}, 
        time spent: {t:.2} seconds")
You can execute your code the normal way as

      mpirun -n 3 python pythonMPI.py
A batch script, job_MPI.slurm, should include a "module load gcc/9.3.0 openmpi/3.1.5"

#!/bin/bash
#SBATCH -A j<proj>
#SBATCH -p devel
#SBATCH --job-name=MPI_py        # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=20              # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:05:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<email>
module load python/3.9.5
module load gcc/9.3.0 openmpi/3.1.5
mpirun -n 20 python pythonMPI.py


### Using the GPU nodes
Example with numba. First install numba locally:

pip install --user numba
Test script: add-list.py

import numpy as np
from timeit import default_timer as timer
from numba import vectorize
# This should be a substantially high value.
NUM_ELEMENTS = 100000000
# This is the CPU version.
def vector_add_cpu(a, b):
  c = np.zeros(NUM_ELEMENTS, dtype=np.float32)
  for i in range(NUM_ELEMENTS):
      c[i] = a[i] + b[i]
  return c
# This is the GPU version. Note the @vectorize decorator. This tells
# numba to turn this into a GPU vectorized function.
@vectorize(["float32(float32, float32)"], target='cuda')
def vector_add_gpu(a, b):
  return a + b;
def main():
  a_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
  b_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
  # Time the CPU function
  start = timer()
  vector_add_cpu(a_source, b_source)<
  vector_add_cpu_time = timer() - start
  # Time the GPU function
  start = timer()
  vector_add_gpu(a_source, b_source)
  vector_add_gpu_time = timer() - start
  # Report times
  print("CPU function took %f seconds." % vector_add_cpu_time)
  print("GPU function took %f seconds." % vector_add_gpu_time)
  return 0
if __name__ == "__main__":
  main()
Run in an interactive session with GPU:s on Snowy

[bjornc@rackham3 ~]$ interactive -A staff -n 1 -M snowy --gres=gpu:1  -t 1:00:01 --mail-type=BEGIN --mail-user=bjorn.claremar@uppmax.uu.se
You receive the high interactive priority.
Please, use no more than 8 GB of RAM.
Waiting for job 6907137 to start...
Starting job now -- you waited for 90 seconds.
[bjornc@s160 ~]$ ml python/3.9.5
[bjornc@s160 ~]$ python add-list.py  #run the script
CPU function took 36.849201 seconds.
GPU function took 1.574953 seconds.


### Machine and Deep Learning
Please see our Tensorflow and and PyTorch guides.

Useful links:

    Official documentation
    Python forum

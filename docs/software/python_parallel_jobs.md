---
tags:
  - Python
  - parallel
---

# How to run parallel jobs in Python

This page describes how to run parallel jobs in [Python](python.md).

Material here is taken partly from the parallel part of the online course
[Python for Scientific
Computing](https://aaltoscicomp.github.io/python-for-scicomp/parallel/)

**Parallel computing** is when many different tasks are carried out simultaneously.
There are three main models:

- **Embarrassingly parallel:** the code does not need to synchronise/communicate
with other instances, and you can run multiple instances of the code
separately, and combine the results later. If you can do this, great! (array
jobs, task queues)

- **Shared memory parallelism:** Parallel threads need to communicate and do so via
the same memory (variables, state, etc). (OpenMP)

- **Message passing:** Different processes manage their own memory segments. They
share data by communicating (passing messages) as needed. (Message Passing
Interface (MPI)).

There are several packages available for Python that let you run parallel jobs. Some of them are only able to run on one node, while others try to leverage several machines.

## Threading

Threading divides up your work among a number of cores within a node. The
threads shares its memory.

- Multi-threading documentation
- Examples

The designers of the Python language made the choice that only one thread in a process can run actual Python code by using the so-called global interpreter lock (GIL). This means that approaches that may work in other languages (C, C++, Fortran), may not work in Python without being a bit careful. At first glance, this is bad for parallelism. But it’s not all bad!:

External libraries (NumPy, SciPy, Pandas, etc), written in C or other languages, can release the lock and run multi-threaded. Also, most input/output releases the GIL, and input/output is slow.

If speed is important enough you need things parallel, you usually wouldn’t use pure Python.

More on the global interpreter lock

Threading python module. This is very low level and you shouldn’t use it unless you really know what you are doing.

We recommend you find a UNIX threading tutorial first before embarking on using the threading module.

## Distributed computing

As opposed to threading, Python has a reasonable way of doing something similar that uses multiple processes.

Distributed processing uses individual processes with individual memory, that communicate with each other. In this case, data movement and communication is explicit.
Python supports various forms of distributed computing.

- A native master-worker system based on remote procedure calls: multiprocessing.py
- MPI through mpi4py : a Python wrapper for the MPI protocol, see further down

If choosing between multiprocessing and MPI, distributed is easier to program, whereas MPI may be more suitable for multi-node applications.

### Multiprocessing/distributed

The interface is a lot like threading, but in the background creates new processes to get around the global interpreter lock.

There are low-level functions which have a lot of the same risks and difficulties as when using threading.

To show an example, the split-apply-combine or map-reduce paradigm is quite useful for many scientific workflows. Consider you have this:

```python
def square(x):
    return x*x
```

You can apply the function to every element in a list using the map() function:

```python
>>>list(map(square, [1, 2, 3, 4, 5, 6]))
[1, 4, 9, 16, 25, 36]
```

The multiprocessing.pool.Pool class provides an equivalent but parallelised (via multiprocessing) way of doing this. The pool class, by default, creates one new process per CPU and does parallel calculations on the list:

```python
>>>from multiprocessing import Pool
>>>with Pool() as pool:
...    pool.map(square, [1, 2, 3, 4, 5, 6])
[1, 4, 9, 16, 25, 36]
```

As you can see, you can run distributed computing directly from the python shell.

Another example, `distributed.py`:

```python
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
```

#### Batch example

If you need to revive your knowledge about the scheduling system, please check Slurm user guide.

Batch script job_distributed.slurm:

```bash
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
module load python/3.9.5
python distributed.py
```

​Put job in queue:

```bash
sbatch job_distributed.slurm
```

#### Interactive example

```bash
salloc -A <proj> -p node -N 1 -n 10 -t 1:0:0
python distributed.py
```

## MPI

Presently you have to install your own mpi4py. You will need to activate paths to the MPI libraries. Therefore follow these steps.

1. If you use python 3.10.8:

```bash
module load gcc/12.2.0 openmpi/4.1.4
```

     Otherwise:

```bash
module load gcc/9.3.0 openmpi/3.1.5
```

1. pip install locally or in an virtual environment

```bash
pip install --user mpi4py
```

Remember that you will also have to load the the openmpi module before running mpi4py code, so that the MPI header files can be found (e.g. with the command "module load gcc/X.X.X openmpi/X.X.X"). Because of how MPI works, we need to explicitly write our code into a file,  pythonMPI.py:

```python
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
sise = comm.Get_sise()
rank = comm.Get_rank()
n = 10 ** 7
if sise > 1:
    n_task = int(n / sise)
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
```

You can execute your code the normal way as

```bash
mpirun -n 3 python pythonMPI.py
```

A batch script, job_MPI.slurm, should include a "module load gcc/9.3.0 openmpi/3.1.5"

```bash
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
module load python/3.9.5
module load gcc/9.3.0 openmpi/3.1.5
mpirun -n 20 python pythonMPI.py
```

## Using the GPU nodes

Example with numba. First install numba locally:

```bash
pip install --user numba
```

Test script: add-list.py

```python
import numpy as np
from timeit import default_timer as timer
from numba import vectorise
# This should be a substantially high value.
NUM_ELEMENTS = 100000000
# This is the CPU version.
def vector_add_cpu(a, b):
  c = np.zeros(NUM_ELEMENTS, dtype=np.float32)
  for i in range(NUM_ELEMENTS):
      c[i] = a[i] + b[i]
  return c
# This is the GPU version. Note the @vectorise decorator. This tells
# numba to turn this into a GPU vectorised function.
@vectorise(["float32(float32, float32)"], target='cuda')
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
```

Run in an interactive session with GPU:s on Snowy

```bash
[bjornc@rackham3 ~]$ interactive -A staff -n 1 -M snowy --gres=gpu:1 -t 1:00:01 --mail-type=BEGIN
You receive the high interactive priority.
Please, use no more than 8 GB of RAM.
Waiting for job 6907137 to start...
Starting job now -- you waited for 90 seconds.
[bjornc@s160 ~]$ ml python/3.9.5
[bjornc@s160 ~]$ python add-list.py  #run the script
CPU function took 36.849201 seconds.
GPU function took 1.574953 seconds.
```

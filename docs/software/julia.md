# Julia user guide

## Julia installations

 There is no system-installed Julia on the clusters. Therefore you need to load Julia with the module system. Different versions of Julia are available via the module system on Rackham, Snowy, and Bianca. Some installed packages are available via the module.

As the time of writing we have the following modules:

```tcl
[user@rackham1 ~]$ module avail julia
------------------------------------------------------
julia:
------------------------------------------------------
Versions:
        julia/1.0.5_LTS
        julia/1.1.1
        julia/1.4.2
        julia/1.6.1
        julia/1.6.3
        julia/1.6.7_LTS
        julia/1.7.2
        julia/1.8.5
        julia/1.9.1
        julia/1.9.3 (Default)
```

- "LTS" stands for Long term support.

To load a specific version of Julia into your environment,  type e.g.

```console
$ module load julia/1.6.7_LTS
```

​Doing:

```console
$ module load julia
```

will give you the default version (1.9.3), often the latest version.

A good and important suggestion is that you always specify a certain version. This is to be able to reproduce your work, a very important key in research!

You can run a julia script in the shell by:

```console
$ julia example_script.jl
```

After loading the appropriate modules for Julia, you will have access to the read-eval-print-loop (REPL) command line by typing julia.

```console
$ julia
```

You will get a prompt like this:

```julia-repl
julia>
```

Julia has different modes, the one mentioned above is the so-called Julian mode where one can execute commands. The description for accessing these modes will be given in the following paragraphs. Once you are done with your work in any of the modes, you can return to the Julian mode by pressing the backspace key.

While being on the Julian mode you can enter the shell mode by typing ;:

```julia-repl
julia>;
shell>pwd
/current-folder-path
```

This will allow you to use Linux commands. Notice that the availabilty of these commands depend on the OS, for instance, on Windows it will depend on the terminal that you have installed and if it is visible to the Julia installation.

Another mode available in Julia is the package manager mode, it can be accessed by typing ] in the Julian mode:

```julia-repl
julia>]
(v1.8) pkg>
```

This will make your interaction with the package manager Pkg easier, for instance, instead of typing the complete name of Pkg commands such as Pkg.status() in the Julian mode, you can just type status in the package mode.

The last mode is the help mode, you can enter this mode from the Julian one by typing ?, then you may type some string from which you need more information:

```julia-repl
help?> ans
```

```julia-repl
julia>?
search: ans transpose transcode contains expanduser instances MathConstants readlines LinearIndices leading_ones leading_zeros
ans
A variable referring to the last computed value, automatically set at the interactive promp
```

!!! info

    Backspace will get you back to julian mode

!!! info
​
    - Exit with `<Ctrl-D>` or 'exit()'.


!!! seealso

    More detailed information about the modes in Julia can be found here: <https://docs.julialang.org/en/v1/stdlib/REPL/>


## Introduction

Julia is according to <https://julialang.org/>:

- Fast
- Dynamic
- Reproducible
- Composable
- General
- Open source

[Documentation](https://docs.julialang.org/en/v1/) for version 1.8.

[Julia discussions](https://discourse.julialang.org/)

## Packages

Some packages are pre-installed. That means that they are available also on **Bianca**. These include:

- "BenchmarkTools"
- "CSV"
- "CUDA"
- DataFrames"
- "Distributed"
- "DistributedArrays"
- "Gadfly"
- "IJulia"
- "MPI"
- "Plots"
- "PlotlyJS"
- "PyPlot"
- all "standard" libraries.

This list will be extended while you, as users, may wish more packages.

You may control the present "central library" by typing in julia shell :

```julia
using Pkg
Pkg.activate(DEPOT_PATH[2]*"/environments/v1.8");     #change version accordingly
Pkg.status()
Pkg.activate(DEPOT_PATH[1]*"/environments/v1.8");     #to return to user library
```

Packages are imported or loaded by the commands ``import`` and ``using``, respectively. The difference is shown here. Or briefly:

To use module functions, use import Module to import the module, and Module.fn(x) to use the functions.
Alternatively, using Module will import all exported Module functions into the current namespace.

### Use  centrally installed packages the first time

You may have to build the package the first time you run it. Julia will in such case ask you to do so. Then:

```julia-repl
julia> using Pkg
julia> Pkg.activate(DEPOT_PATH[2]*"/environments/v1.9");      #change version accordingly
julia> Pkg.build(<package_name>)
```

## How to install personal packages

You may ignore the pre-installed packages. They are there mainly for Bianca users, but may help you to relieving some disk space! If you ignore you can jump over the

### Check if packages are installed centrally

To make sure that the package is not already installed, type in Julia:

```julia
julia> using Pkg
julia> Pkg.activate(DEPOT_PATH[2]*"/environments/v1.8");  #change version accordingly
julia> Pkg.status()
```

To go back to your own personal packages:

```julia-repl
julia> Pkg.activate(DEPOT_PATH[1]*"/environments/v1.8");
julia> Pkg.status()
```

You can load (using/import) ANY package from both lotcal and central installation irrespective to which environment you activate. However, the setup is that your package is prioritized if there are similar names.

### Start an installation locally

To install personal packages, start to be sure that you are in your local environment. You type within Julia:

```julia-repl
     Pkg.activate(DEPOT_PATH[1]*"/environmentts/v1.8");
     Pkg.add("<package_name>")
```

This will install under the path ~/.julia/packages/. Then you can load it by just doing "using/import <package_name>".

```julia-repl
      using <package_name>
```

You can also activate a "package prompt" in julia with   ']':


```julia-repl
(@v1.8) pkg> add <package name>
```

For installing specific versions specify with `<package name>@<X.Y.Z>`.

After adding you may be asked to precompile or build. Do so according to instruction given on the screen. Otherwise, first time importing or using the package, Julia may start a precompilation that will take a few seconds up to several minutes.

Exit with `<backspace>`:


```julia-repl
julia>
```

### Own packages on Bianca

You can use make an installation on Rackham and then use the wharf to copy it over to your ~/.julia/ directory.

Otherwise, send an email to `support@uppmax.uu.se` and we'll help you.

## Running IJulia from Jupyter notebook

Like for python it is possible to run a Julia in a notebook, i.e. in a web interface with possibility of inline figures and debugging. An easy way to do this is to load the python module as well. In shell:

```console
$ module load julia/1.8.5
$ module load python/3.10.8
$ julia
```

In Julia:

using IJulia

```julia
notebook(dir="</path/to/work/dir/>")
```

A Firefox session will start with the Jupyter notebook interface.

If not, you may have to build IJulia the first time with Pkg.build(“IJulia”). Since “IJulia” is pre-installed centrally on UPPMAX you must activate the central environment by following these steps belo. This should only be needed the first time like this

```julia
> using Pkg
> Pkg.activate(DEPOT_PATH[2]*"/environments/v1.8");
> Pkg.build("IJulia")
> notebook(dir="</path/to/work/dir/>")
```

This builds the package also locally before starting the notebook. If not done, Jupyter will not find the julia kernel of that version. With notebook(dir="</path/to/work/dir/>", detached=true) the notebook will not be killed when you exit your REPL julia session in the terminal.

## How to run parallel jobs

There are several packages available for Julia that let you run parallel jobs. Some of them are only able to run on one node, while others try to leverage several machines. You'll find an introduction here.

### Run interactively on compute node

Always run parallel only on the compute nodes. This is an example with 4 cores on Rackham

```console
$ interactive -A <proj> -n 4 -t 3:00:00
Running interactively at UPPMAX
```


Slurm user guide

### Threading

Threading divides up your work among a number of cores within a node. The threads share their memory. Below is an example from within Julia. First, in the shell type:

```console
$ export JULIA_NUM_THREADS=4
$ julia
```

in Julia:

```julia
using Base.Threads
nthreads()
      a = zeros(10)
@threads for i = 1:10
        a[i] = Threads.threadid()
end
```

### Distributed computing

Distributed processing uses individual processes with individual memory, that communicate with each other. In this case, data movement and communication is explicit.
Julia supports various forms of distributed computing.

- A native master-worker system based on remote procedure calls: Distributed.jl
- MPI through MPI.jl : a Julia wrapper for the MPI protocol, see further down.
- DistributedArrays.jl: distribute an array among workers

If choosing between distributed and MPI, distributed is easier to program, whereas MPI may be more suitable for multi-node applications.

For more detailed info please confer the manual for distributed computing and julia MPI.

#### Master-Worker model

We need to launch Julia with

```console
$ julia -p 4
```

then inside Julia you can check

```julia
nprocs()
workers()
```

which should print 5 and [2,3,4,5]. Why 5, you ask? Because *"worker 1"* is the *"boss"*. And bosses don't work.

As you can see, you can run distributed computing directly from the julia shell.

#### Batch example

Julia script hello_world_distributed.jl:

```julia
using Distributed
# launch worker processes
num_cores = parse(Int, ENV["SLURM_CPUS_PER_TASK"])
addprocs(19)
println("Number of cores: ", nprocs())
println("Number of workers: ", nworkers())
# each worker gets its id, process id and hostname
for i in workers()
    id, pid, host = fetch(@spawnat i (myid(), getpid(), gethostname()))
    println(id, " " , pid, " ", host)
end
# remove the workers
for i in workers()
    rmprocs(i)
end
```

- Batch script job_distributed.slurm:

```bash
#!/bin/bash
#SBATCH -A j<proj>
#SBATCH -p devel
#SBATCH --job-name=distrib_jl     # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=20              # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<email>
module load julia/1.8.5
julia hello_world_distributed.jl
```

​Put job in queue:

```console
$ sbatch job_distributed.slurm
```


#### Interactive example

```console
$ salloc -A <proj> -p node -N 1 -n 10 -t 1:0:0
$ julia hello_world_distributed.jl
```


### MPI

The Threaded and Distributed packages are included in the Base installation. However, in order to use MPI with Julia you will need to follow the next steps (only the first time):

- Load the tool chain which contains a MPI library

For julia/1.6.3 and earlier:

```console
$ module load gcc/9.3.0 openmpi/3.1.5
```

For julia/1.6.7_LTS & 1.7.2:

```console
$ module load gcc/10.3.0 openmpi/3.1.6
```

For julia/1.8.5:

```console
$ module load gcc/11.3.0 openmpi/4.1.3
```

- Load Julia

```console
$ ml julia/1.8.5   # or other
```

- Start Julia on the command line

```console
$ julia
```

- Change to ``package mode`` and add the ``MPI`` package

```console
(v1.8) pkg> add MPI
```

- In the ``julian`` mode run these commands:

```console
julia> using MPI
julia> MPI.install_mpiexecjl()
[ Info: Installing `mpiexecjl` to `~/.julia/bin`...
[ Info: Done!
```

- Add the installed ``mpiexecjl`` wrapper to your path on the Linux command line

```bash
$ export PATH=~/.julia/bin:$PATH
```

- Now the wrapper should be available on the command line

Because of how MPI works, we need to explicitly write our code into a file, juliaMPI.jl:

```julia
import MPI
MPI.Init()
comm = MPI.COMM_WORLD
MPI.Barrier(comm)
root = 0
r = MPI.Comm_rank(comm)
sr = MPI.Reduce(r, MPI.SUM, root, comm)
if(MPI.Comm_rank(comm) == root)
@printf("sum of ranks: %s\n", sr)
end
MPI.Finalize()
```

You can execute your code as in an interactive session with several cores (at least 3 in this case):

```console
$ module load gcc/11.3.0 openmpi/4.1.3
$ mpiexecjl -np 3 julia juliaMPI.jl
```

A batch script, job_MPI.slurm, should include a "module load gcc/XXX openmpi/XXX"

```bash
#!/bin/bash
#SBATCH -A j<proj>
#SBATCH -p devel
#SBATCH --job-name=MPI_jl        # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=20              # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:05:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<email>
module load julia/1.8.5
module load gcc/11.3.0 openmpi/4.1.3
export PATH=~/.julia/bin:$PATH
mpiexecjl -n 20 julia juliaMPI.jl
```

- Run with

```console
$ sbatch job_MPI.slurm
```

See the MPI.jl examples for more input!

### GPU

Example Julia script, juliaCUDA.jl:

```julia
using CUDA, Test
N = 2^20
x_d = CUDA.fill(1.0f0, N)
y_d = CUDA.fill(2.0f0, N)
y_d .+= x_d
@test all(Array(y_d) .== 3.0f0)
println("Success")
```

Batch script juliaGPU.slurm, note settings for Bianca vs. Snowy:

```bash
#!/bin/bash
#SBATCH -A <proj-id>
#SBATCH -M <snowy OR bianca>
#SBATCH -p node
#SBATCH -C gpu   #NB: Only for Bianca
#SBATCH -N 1
#SBATCH --job-name=juliaGPU         # create a short name for your job
#SBATCH --gpus-per-node=<1 OR 2>             # number of gpus per node (Bianca 2, Snowy 1)
#SBATCH --time=00:15:00          # total run time limit (HH:MM:SS)
#SBATCH --qos=short              # if test run t<15 min
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=<email>
module purge
module load julia/1.8.5          # system CUDA works as of today
julia juliaCUDA.jl
```

- Put job in queue:

```console
$ sbatch juliaGPU.slurm
```

#### Interactive session with GPU

On Snowy, getting 1 cpu and 1 gpu:

```console
$ interactive -A <proj> -n 1 -M snowy --gres=gpu:1  -t 3:00:00
```

On Bianca, getting 2 cpu:s and 1 gpu:

```console
$ interactive -A <proj> -n 2 -C gpu --gres=gpu:1 -t 01:10:00
```

- wait until session is started

```console
$ julia/1.7.2
$ julia/1.8.5 (Default)
```

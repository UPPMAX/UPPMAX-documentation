# Gaussian 09 user guide

> A short guide on how to run g09 on UPPMAX.

## Access to Gaussian 09

Gaussian 09 is available at UPPMAX. Uppsala University has an university license for all employees. If you want to be able to run g09 email [support@uppmax.uu.se](mailto:support@uppmax.uu.se) and ask to be added to the g09 group.

## Running g09

In order to run g09 you must first set up the correct environment. You do this with:

`module load gaussian/g09.d01`

### Running single core jobs in SLURM

Here is an example of a submit script for SLURM:

```slurm
#!/bin/bash -l
#SBATCH -J g09test
#SBATCH -p core
#SBATCH -n 1
#If you ask for a single core in slurm on Rackham you get 6.4 Gb of memory
#SBATCH -t 1:00:00
#SBATCH -A your_project_name

module load gaussian/g09.d01
g09 mp2.inp mp2.out
```

If you run a single core job on Rackham you can't use more than 6.4GB of memory.

When specifying the memory requirements, make sure that you ask for some more memory in the submit-script than in g09 to allow for some memory overhead for the program. As a general rule you should ask for 200MB more than you need in the calculation.

The `mp2.inp` input file in the example above:

```text
%Mem=800MB
#P MP2 aug-cc-pVTZ OPT

test

0 1
Li
F 1 1.0
```

## Scratch space

The g09 module sets the environment `GAUSS_SCRDIR` to `/scratch/$SLURM_JOBID` in slurm. These directories are removed after the job is finished.

If you want to set `GAUSS_SCRDIR`, you must do it after module load `gaussian/g09.a02` in your script.

If you set `GAUSS_SCRDIR` to something else in your submit script remember to remove all unwanted files after your job has finished.

If you think you will use a large amount of scratch space, you might want to set **maxdisk** in your input file. You can either set **maxdisk** directly on the command line in your input file:

```text
#P MP2 aug-cc-pVTZ SCF=Tight maxdisk=170GB
```

or you can put something like:

```bash
MAXDISK=$( df | awk '/scratch/ { print $4 }' )KB
sed -i '/^#/ s/ maxdisk=[[:digit:]]*KB//' inputfile
sed -i '/^#/ s/$/ maxdisk='$MAXDISK'/'; inputfile
```

in your scriptfile. This will set **maxdisk** to the currently available size of the /scratch disk on the node you will run on. Read more on maxdisk in the [online manual](https://gaussian.com/maxdisk/).

## Running g09 in parallel

Gaussian can be run in parallel on a single node using shared memory. This is the input file for the slurm example below:

The `dimer4.inp` input:

```
%Mem=3800MB
%NProcShared=4
#P MP2 aug-cc-pVTZ SCF=Tight

methanol dimer MP2

0 1
6 0.754746 -0.733607 -0.191063
1 -0.033607 -1.456810 -0.395634
1 1.007890 -0.778160 0.867678
1 1.635910 -0.998198 -0.774627
8 0.317192 0.576306 -0.534002
1 1.033100 1.188210 -0.342355
6 1.513038 3.469264 0.971885
1 1.118398 2.910304 1.819367
1 0.680743 3.818664 0.361783
1 2.062618 4.333044 1.344537
8 2.372298 2.640544 0.197416
1 2.702458 3.161614 -0.539550
```

### Running g09 in parallel in slurm

This can be done by asking for CPUs on the same **node** using the parallel node environments and telling Gaussian to use several CPUs using the `NProcShared` link 0 command.

An example submit-script:

```slurm
#!/bin/bash -l
#SBATCH -J g09_4
#SBATCH -p node -n 8
#SBATCH -t 1:00:00
#SBATCH -A your_project_name

module load gaussian/g09.d01
export OMP_NUM_THREADS=1
ulimit -s $STACKLIMIT

g09 dimer4.inp dimer4.out
```

Notice that 8 cores are requested from the queue-system using the line `#SLURM -p node -n 8` and that Gaussian is told to use 4 cores with the link 0 command `%NProcShared=4`. The example above runs about 1.7 times as fast on eight cores than on four, just change in the input file to `%NProcShared=8`. Please benchmark your own inputs as the speedup depends heavily on the method and size of system. In some cases Gaussian cannot use all the cpus you ask for. This is indicated in the output with lines looking like this:

_PrsmSu: requested number of processors reduced to: 1 ShMem 1 Linda._

The reason for specifying `OMP_NUM_THREADS=1` is to not use the parts of OpenMP in the Gaussian code, but to use Gaussians own threads.

## Running g09 in parallel with linda

In order to run g09 in parallel over several nodes we have acquired Linda TCP.

### Running g09 in parallel with linda in slurm

This can be done by asking for CPUs on the same **node** using the parallel node environments and telling Gaussian to use several CPUs using the `NProcLinda` and `NProcShared` link 0 command.

An example submit-script:

```slurm
#!/bin/bash -l
#SBATCH -J g09-linda
#
#SBATCH -t 2:00:0
#
#SBATCH -p node -n 40
#SBATCH -A your_project_name

module load gaussian/g09.d01
ulimit -s $STACKLIMIT
export OMP_NUM_THREADS=1

#Next lines are there for linda to know what nodes to run on
srun hostname -s | sort -u > tsnet.nodes.$SLURM_JOBID
export GAUSS_LFLAGS='-nodefile tsnet.nodes.$SLURM_JOBID -opt "Tsnet.Node.lindarsharg: ssh"'

#export GAUSS_SCRDIR=
time g09 dimer20-2.inp dimer20-2.out

rm tsnet.nodes.$SLURM_JOBID
```

Here is the input file:

```text
%NProcLinda=2
%NProcShared=20
%Mem=2800MB
#P MP2 aug-cc-pVTZ SCF=Tight

methanol dimer MP2

0 1
6 0.754746 -0.733607 -0.191063
1 -0.033607 -1.456810 -0.395634
1 1.007890 -0.778160 0.867678
1 1.635910 -0.998198 -0.774627
8 0.317192 0.576306 -0.534002
1 1.033100 1.188210 -0.342355
6 1.513038 3.469264 0.971885
1 1.118398 2.910304 1.819367
1 0.680743 3.818664 0.361783
1 2.062618 4.333044 1.344537
8 2.372298 2.640544 0.197416
1 2.702458 3.161614 -0.539550

```

Notice that 40 cores are requested from the queue-system using the line `#SLURM -p node -n 40` and that g09 is told to use 2 nodes via linda with the `%NProcLinda=2` link 0 command and 20 cores on each node with the link 0 command `%NProcShared=20`.

Please benchmark your own inputs as the speedup depends heavily on the method and size of system.

In some cases Gaussian cannot use all the cpus you ask for. This is indicated in the output with lines looking like this:

```text
_ PrsmSu: requested number of processors reduced to: 1 ShMem 1 Linda._
```

## Number of CPUs on the shared memory nodes

Use the information below as a guide to how many CPUs to request for your calculation:

### On Rackham

- 272 nodes with two 10-core CPUs and 128GB memory
- 32 nodes with two 10-core CPUs and 256GB memory

### On Milou

- 174 nodes with two 8-core CPUs and 128GB memory
- 17 nodes with two 8-core CPUs and 256GB memory
- 17 nodes with two 8-core CPUs and 512GB memory

### Note on chk-files

You may experience difficulties if you mix different versions (g09 and g03) or revisions of gaussian. If you use a checkpoint file (.chk file) from an older revision (say g03 e.01), in a new calculation with revision a.02, g09 may not run properly.

We recommend using the same revision if you want to restart a calculation or reuse an older checkpoint file.

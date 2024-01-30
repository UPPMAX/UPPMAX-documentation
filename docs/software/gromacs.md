# Running Gromacs at UPPMAX

This page describes how to run the GROMACS molecular dynamics software on UPPMAX systems. See the [gromacs](http://www.gromacs.org/) web page for more information.

Have a look on this page as well - [best practices](https://docs.bioexcel.eu/gromacs_bpg/en/master/cookbook/cookbook.html) running GROMAC on HPC.



Selected setups for benchmarking on HPC2N as [examples](https://github.com/hpc2n/CourseEfficientMD/tree/main/benchmark/GROMACS).

## Loading the gromac module

``` bash
$ module load gromacs/2021.1.th
```

## SBATCH script

> adapted from [HPC2N](https://www.hpc2n.umu.se/resources/software/gromacs)

``` bash
#!/bin/bash -l
#SBATCH -A SNIC_project
#SBATCH -t 00:15:00
#SBATCH -p node -n 10
# Use 2 threads per task
#SBATCH -c 2

module load gromacs/2021.1.th

# Automatic selection of single or multi node based GROMACS
if [ $SLURM_JOB_NUM_NODES -gt 1 ]; then
  GMX="gmx_mpi"
  MPIRUN="mpirun"
  ntmpi=""
else
  GMX="gmx"
  MPIRUN=""
  ntmpi="-ntmpi $SLURM_NTASKS"
fi

# Automatic selection of ntomp argument based on "-c" argument to sbatch
if [ -n "$SLURM_CPUS_PER_TASK" ]; then
  ntomp="$SLURM_CPUS_PER_TASK"
else
  ntomp="1"
fi
# Make sure to set OMP_NUM_THREADS equal to the value used for ntomp
# to avoid complaints from GROMACS
export OMP_NUM_THREADS=$ntomp
$MPIRUN $GMX mdrun $ntmpi -ntomp $ntomp -s MEM.tpr -nsteps 10000 -resethway
```

## How important is to select appropriate options
Here is a simple benchmark ran on single interactive node with 20CPUs using  the MEM example from this benchmark https://www.mpibpc.mpg.de/grubmueller/bench.

``` bash
$ module load gromacs/2021.1.th
$ mpirun -np XX gmx_mpi mdrun -ntomp YY -s MEM.tpr -nsteps 10000 -resethway
```

where XX * YY = 20

``` bash linenums="1"
$ grep "gmx_mpi\|MPI ranks\|Performance" *

#md.log.1#:  gmx_mpi mdrun -ntomp 1 -s MEM.tpr -nsteps 10000 -resethway
#md.log.1#:On 12 MPI ranks doing PP, and
#md.log.1#:on 8 MPI ranks doing PME
#md.log.1#:Performance:       20.520        1.170

#md.log.2#:  gmx_mpi mdrun -ntomp 2 -s MEM.tpr -nsteps 10000 -resethway
#md.log.2#:On 10 MPI ranks, each using 2 OpenMP threads
#md.log.2#:Performance:       25.037        0.959

#md.log.3#:  gmx_mpi mdrun -ntomp 4 -s MEM.tpr -nsteps 10000 -resethway
#md.log.3#:On 5 MPI ranks, each using 4 OpenMP threads
#md.log.3#:Performance:        5.388        4.454

#md.log.4#:  gmx_mpi mdrun -ntomp 5 -s MEM.tpr -nsteps 10000 -resethway
#md.log.4#:On 4 MPI ranks, each using 5 OpenMP threads
#md.log.4#:Performance:       24.090        0.996

#md.log.5#:  gmx_mpi mdrun -ntomp 10 -s MEM.tpr -nsteps 10000 -resethway
#md.log.5#:NOTE: Your choice of number of MPI ranks and amount of resources results in using 10 OpenMP threads per rank, which is most likely inefficient. The optimum is usually between 1 and 6 threads per rank.
#md.log.5#:On 2 MPI ranks, each using 10 OpenMP threads
#md.log.5#:Performance:        3.649        6.577

md.log:  gmx_mpi mdrun -ntomp 20 -s MEM.tpr -nsteps 10000 -resethway
md.log:Performance:        2.012       11.931
```

Notice how bad is the last run 
`$ mpirun -np 1 gmx_mpi mdrun -ntomp 20 -s MEM.tpr -nsteps 10000 -resethway` (lines 25-26)

According to this short test, this particular setup runs best on single Rackham node with 
`$ mpirun -np 10 gmx_mpi mdrun -ntomp 2 -s MEM.tpr -nsteps 10000 -resethway` (lines 8-10)


## Running older versions of gromacs

### Versions 4.5.1 to 5.0.4:
The gromacs tools have been compiled serially. The mdrun program has also been compiled in parallel using MPI. The name of the parallel binary is mdrun_mpi.

Run the parallelized program using:
``` bash
mpirun -np XXX mdrun_mpi
```
... where XXX is the number of cores to run the program on.

### Version 5.1.1
The binary is gmx_mpi and (e.g.) the mdrun command is issued like this:
``` bash
mpirun -np XXX gmx_mpi mdrun
```

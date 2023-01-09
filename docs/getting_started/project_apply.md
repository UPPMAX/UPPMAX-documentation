??? t2s "Text to speech"
    <audio src="../project_apply.mp3" controls preload></audio>

# Welcome to UPPMAX userguide 


## Systems

| Specs    | Rackham    | Snowy    | Bianca    |
|---------------- | --------------- | --------------- | --------------- |
| CPUs    | Item2.1    | Item3.1    | Item4.1    |
| GPUs   | Item2.2   | Item3.2   | Item4.2   |


## Slurm Commands

The Slurm system is accessed using the following commands:

* `interactive` - Start an interactive session
* `sbatch` - Submit and run a batch job script
* `srun` - Typically used inside batch job scripts for running parallel jobs
  (See examples further down)
* `scancel` - Cancel one or more of your jobs.

### Specifying job parameters

Whether you use the UPPMAX clusters interactively or in batch mode, you always
have to specify a few things, like number of cores needed, running time et.c.
These things can be specified in two ways:

Either as flags sent to the different Slurm commands (sbatch, srun, the
interactive command, et.c.), like so

``` bash
sbatch -A p2012999 -p core -n 1 -t 12:00:00 -J some_job_name my_job_script_file.sh
```

or, when using the `sbatch` command, it can be specified inside the job script
file itself, by using special `SBATCH` comments, for example:

``` bash title="job_script.sh"
#!/bin/bash -l
 
#SBATCH -A p2012999
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 12:00:00
#SBATCH -J some_job_name

```

If doing this, then one will only need to start the script like so, without any
flags:

``` bash
sbatch job_script.sh
```

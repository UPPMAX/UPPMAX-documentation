---
tags:
  - Pelle
---

# Pelle test pilot guide
This page contains information and instructions for test pilot users
of Pelle.

## State of the system
* Not everything is finished
* Some things are broken and/or does not work as expected
* Not all configuration changes are final

We reserve the right to restart login nodes, compute nodes, kill
running jobs and similar with little to no warning. We will avoid this
when possible, but if necessary our continuing work on getting the
cluster ready have higher priority than the test usage.

## Provide feedback
Getting information from you about what works and what does not work
is an important part of the test pilot usage. This will help us find
issues and to prioritise our work. Please send feedback to
<support@uppmax.uu.se>.

Some ideas of things we would like to know about:

* You find something that is not working. But please check if it
  already mentioned as a known issue on this page first.

* You find something confusing or weird

* Performance issues

* Software not working

* Missing software

* Something that can be improved

* Things that are working great

## Log in
To log in to Pelle two-factor authentication using TOTP is required.

Follow our guide to [setup UPPMAX two factor
authentication](../getting_started/get_uppmax_2fa.md) if you don't
already have this.

## New operating system
Pelle is running [Rocky Linux 9](https://rockylinux.org/). Most system
software, including the Linux kernel, have newer versions compared to
Rackham and other UPPMAX clusters.

## Hardware
Pelle's compute nodes have much more CPU cores and memory compared to
previous UPPMAX cluster. All compute nodes have AMD Zen4 processors.

Details about the hardware is on the [Pelle/Maja
hardware](../hardware/clusters/pelle.md) page.

## Software installations
Software available on Pelle is not included in the Software list on
this web page yet. Please use the [module system](modules.md) to list
available software, for example by running `module avail` or `module
spider`.

We are working on installing more software packages.

## Slurm
Slurm on Pelle have been upgraded to version 24.11.

Several UPPMAX-specific Slurm changes have been removed from previous
clusters have been removed, to make the config use more Slurm
defaults. This makes the system easier to maintain and will behave
more similar to clusters at other sites. Unfortunately this means that
some extra changes to job scripts can be needed when moving from
Rackham/Snowy.

Our [Slurm documentation](./slurm.md) have not yet been updated with
the changes on Pelle.

### Project for test pilot jobs
Please use the `uppmax2025-2-325` project when submitting test pilot
jobs. `sbatch --account=uppmax2025-2-325`

### Job priority
Slurm's default fair-share priority are used for the job queue.

### 48 hour max job time limit
To prevent jobs occupying nodes for too long during the test period we
have reduced the max timelimit for jobs to 48 hours.

This is only during the pilot test period, after this the allowed time
limit will be increased.

### No node/core partitions
On Rackham you have used `-p node` or `-p core` to specify node/core
jobs. This is not used on Pelle. Instead Slurm's standard options is
used to specify the job requirements.

Example to request 2 full nodes: `--nodes=2 --exclusive`

One task, using two threads: `--ntasks=1 --cpus-per-task=2`

Two tasks, using one thread each: `--ntasks=2 --cpus-per-task=2`

### No devel partition
A way to get high priority for short devel jobs will be added later.

### Job memory specification ###
Currently you do not have to request additional CPUs to get additional
memory. You can use all Slurm options `--mem`, `--mem-per-cpu`,
`--mem-per-gpu` to specify memory requirements.

This might be changed later, the configuration is not final.

#### 2/3 TiB memory ####
Pelle have two fat nodes. One with 2 TiB of memory and one with 3 TiB.

Jobs on these nodes always allocate the entire node with all cores.

To use the 2 TiB node: `sbatch --partition=fat --constraints=2TB`

To use the 3 TiB node: `sbatch --partition=fat --constraints=3TB`

### interactive
The script `interactive` used to submit interactive jobs still works,
but does not provide as much information as on Rackham. It is now a
very thin wrapper around the `sacct` command.

### SMT
The compute node CPUs have Simultaneous multithreading (SMT)
enabled. Each CPU core runs two Threads. In Slurm the Threads are
referred to as CPUs.

Different jobs are never allocated to the same CPU core. The smallest
possible job always gets one Core with two Threads (CPUs).

Jobs requesting multiple tasks or cpus gets threads by default.

Some examples:  
`--ntasks=2` - one core, two threads  
`--ntasks=1 --cpus-per-task=4` - two cores, four threads  
`--ntasks=2 --cpus-per-task=3` - three cores, six threads.

#### One thread per core to avoid SMT
If you suspect SMT degrades the performance of your jobs, you can you
can specify `--threads-per-core=1` in your job.

Same examples as before but with `--threads-per-core=1`:  
`--ntasks=2 --threads-per-core=1` - two cores, (4 threads, 2 used)  
`--ntasks=1 --cpus-per-task=4 --threads-per-core=1` - 4 cores (8 threads, 4 unused)  
`--ntasks=2 --cpus-per-task=3 --threads-per-core=1` - 6 cores (12 threads, 6 unused)

When doing this you should launch your tasks using `srun` to ensure
your processes gets pinned to the correct CPUs (threads), one per
core.

## Known issues

### Missing tools
Some UPPMAX specific tools are not yet working on Pelle.

* `uquota` - works.
* `projinfo` - not implemented yet.
* `finishedjobinfo` - use `sacct` instead
* `jobinfo` - use tools like `squeue` and `sprio` instead
* `jobstats` - not working on Pelle. Might be replaced by an alternative solution.

### Missing projects
Only the test pilot project (uppmax2025-2-325) have been enabled on
the cluster. Other uppmax2025-projects cannot be used to run jobs yet.

Use the test pilot project for your test pilot jobs.

### Core jobs can get allocated resources across several compute nodes
A job requesting multiple tasks can get resources allocated
on multiple nodes. For example 3 tasks `sbatch -n3` might get
allocated three CPUs on three different compute nodes.

We will update the configuration to avoid this. For not the problem
can be avoided by specifying `--nodes=1-1` when submitting jobs.

# Snowy

![Snowy, from https://www.deviantart.com/shannonmai2002art/art/Snowy-From-Tintin-504387373](./img/snowy_120_x_186.jpg)

Snowy is one of the [UPPMAX clusters](uppmax_cluster.md).

- [Snowy's name](snowys_name.md)
- [Snowy's design](snowys_design.md)
- [Log in](../getting_started/login_snowy.md)
- [Submitting jobs, using Slurm](slurm.md)
- [Workshops and courses](../workshops_courses/workshops_courses.md)

## Accounts and log in

Snowy is different from other clusters at UPPMAX in that 
there are no login nodes for Snowy. 
All access to this system is done via secure shell (a.k.a [SSH](../software/ssh.md)) interactive login to the login node, 
using the domain name **rackham.uppmax.uu.se**

> `ssh -X user@rackham.uppmax.uu.se`

See [the UPPMAX page on how to get a user account](../getting_started/user_account.md) page.
on how to get a user account.

For questions concerning accounts and access to [Rackham](rackham.md) and [Snowy](snowy.md),
please contact [UPPMAX support](../support.md).

Note that the machine you arrive at when logged in is only a so called login node, where you can do various smaller tasks. 
We have [some limits](../cluster_guides/login_node_restrictions.md) in place that restricts your usage. 
For larger tasks you should use our batch system that pushes your jobs onto other machines within the cluster.

All access to [Snowy](snowy.md) is done using the batch system Slurm, either as an interactive job or non-interactive batch jobs.

## Using the batch system

To allow a fair and efficient usage of the system we use a resource manager to coordinate user demands. 
On Snowy we use [the Slurm resource manager](../cluster_guides/slurm.md),
as is discussed in more detail there.

**Note:** When accessing snowy from Rackhams login nodes you must always use the flag -M for all Slurm commands.  
Examples:

*   squeue -M snowy
*   jobinfo -M snowy
*   sbatch -M snowy slurm\_script\_file
*   scancel -u username -M snowy
*   interactive -A projectname -M snowy -p node -n 32 -t 01:00:00

**Note:** We always recommend loading all your modules in your job script file, This is even more important when running on Snowy since the module environment is not the same on the Rackham login nodes as on Snowy compute nodes.

### Some Limits

*   There is a job walltime limit of 30 days (720 hours).
*   We restrict each user to at most 5000 running and waiting jobs in total.
*   Each project has a 30 days running allocation of CPU hours. We do not forbid running jobs after the allocation is overdrafted, but instead allow to submit jobs with a very low queue priority, so that you may be able to run your jobs anyway, if a sufficient number of nodes happens to be free on the system.
*   Very wide jobs will only be started within a maintenance window (just before the maintenance window or at the end of the maintenance window). These are planned for the first Wednesday of each month. On Snowy a "very wide" job asks for 100 nodes or more.

### Convenience Variables

*   **$SNIC\_TMP - Path to node-local temporary disk space**
      
    The **$SNIC\_TMP** variable contains the path to a node-local temporary file directory that you can use when running your jobs, in order to get maximum disk performance (since the disks are local to the current compute node). This directory will be automatically created on your (first) compute node before the job starts and automatically deleted when the job has finished.
      
    The path specified in **$SNIC\_TMP** is equal to the path: /**scratch/$SLURM\_JOB\_ID**, where the job variable **$SLURM\_JOB\_ID** contains the unique job identifier of your job.
      
    **WARNING:** Please note, that in your "core" (see below) jobs, if you write data in the **/scratch** directory but outside of the /**scratch/$SLURM\_JOB\_ID** directory, your data may be automatically deleted during your job run.

### Details about the "core" and "node" partitions

A normal Snowy node contains 128 GB of RAM and 16 compute cores. An equal share of RAM for each core would mean that each core gets at most 8 GB of RAM. This simple calculation gives one of the limits mentioned below for a "core" job.

You need to choose between running a "**core**" job or a "**node**" job. A "core" job must keep within certain limits, to be able to run together with up to 15 other "core" jobs on a shared node. A job that cannot keep within those limits must run as a "node" job.

Some serial jobs must run as "**node**" jobs. You tell Slurm that you need a "node" job with the flag "-p node". (If you forget to tell Slurm, you are by default choosing to run a "core" job.)

A "**core**" job:

*   Will use a part of the resources on a node, from a 1/16 share to a 15/16 share of a node.
    
*   Must specify less cores than 16, i.e.between "**\-n 1**" to "**\-n 15**".
    

*   Must not demand "-N", "--nodes", or "--exclusive".
    
*   Is recommended not to demand "--mem"
    

*   Must not demand to run on a fat node (see below, for an explanation of "fat"), a devel node.
    

*   Must not use more than 8 GB of RAM for each core it demands. If a job needs half of the RAM, i.e. 64 GB, you need to reserve also at least half of the cores on the node, i.e. 8 cores, with the "-n 8" flag.
    

A "**core**" job is accounted on your project as one "core hour" (sometimes also named as a "CPU hour") per core you have been allocated, for each wallclock hour that it runs. On the other hand, a "**node**" job is accounted on your project as sixteen core hours for each wallclock hour that it runs, multiplied with the number of nodes that you have asked for.

### Node types

Rackham has two node types, _thin_ being the typical cluster node and _fat_ nodes having double the amount of memory available normally (256 GB). You may specify a node with more RAM, by adding the words "**\-C mem256GB**" or "**\-C fat**" to your job submission line and thus making sure that you will get 256 GB of RAM on each node in your job. If you need even more memory you can request a 512 GB memory node by adding "**\-C mem512GB**". Please note that there are only 13 nodes with 256GB and 17 with 512GB of RAM.

**To request a fat node, use -C mem256GB or -C fat in your Slurm command.** 

**To request the fattest nodes, use -C mem512GB in your Slurm command.** 

## File storage and disk space

At UPPMAX we have a few different kinds of storage areas for files, 
see [Disk Storage User Guide](../cluster_guides/uppmax_systems.md) for more information and recommended use.

## Very Long jobs

If you have very long jobs that require more than 10 days of CPU-time. We recommend using Snowy.  
But in order for our job to successfully run for severay weeks you should implement the following;

*   Use only local disk for your job. Copy all input and data files needed to **$SNIC\_TMP** at the start of your job and at the end, copy all output back to your project directory.
*   Book a full node with the Slurm flags **\-p node** (you won't be able to submit these jobs in the core partition).
*   If possible make sure you do not rely on files stored outside the node. One way of achieving this may be to copy program files to $SNIC\_TMP.

Even if you do this we can't promise that a 20 or 30 day long job will finish without being interrupted by the global file systems, the network or problems on the node,








## Snowy's design

Snowy is an (general-purpose) high-performance computing (HPC) cluster,
with GPUs and suitable for longer jobs.

???- question "What is an HPC cluster?"

    What an HPC cluster is, is described [here](uppmax_cluster.md).

Or: Snowy is a group of computers that can effectively run many calculations, 
as requested by multiple people, at the same time.
Snowy runs the Linux operating system and all users need some
basic Linux knowledge to use Snowy.

Additionally, Snowy has GPUs and allows for jobs running for maximally 30 days. 

Snowy does not have a login node. Instead, it uses a login node on [Rackham](rackham.md).

???- tip "Using Linux"

    Using Linux (and especially the so-called command-line/terminal) is essential
    to use Snowy. Learning the essential Linux commands 
    is described [here](../getting_started/linux.md).

## Snowy's system configuration

Snowy consists of 228 compute servers (nodes) where each compute server 
consists of two 8-core Xeon E5-2660 processors running at 2.2 GHz. 
We provide 198 nodes with 128 GB memory (`s1-s120`, `s151-s228`), 
13 nodes with 256 GB (`s138-s150`) and 17 nodes with 512 GB (`s121-s137`). 
All nodes are interconnected with a 2:1 
oversubscribed FDR (40 GB/s) Infiniband fabric. 
In total Snowy provides 3548 CPU cores in compute nodes.

## Compiling on Snowy

There are several compilers available through 
the [module system](modules.md) on Snowy. 
This gives you flexibility to obtain programs that run optimally on Snowy.

*   gcc - the newest version usually generates the best code, if you tell it to use the new instructions. Check which version is the newest by doing **module avail**.  
    The compiler executable is named gcc for C, g++ for C++, and gfortran for Fortran.
    To use the new instructions available on Snowy (AVX2 and FMA3), give the additional options "**\-mavx2 -mfma3**" to gcc. For good performance with this compiler you should also specify optimization at least at level **\-O2** or **\-O3**. Also try using **\-march=broadwell** for GCC >= 4.9.0 or **\-march=core-avx2** for GCC 4.8.x, which will enable all the instructions on the CPU.
*   Intel+MKL - usually generates the fastest code. As with gcc, it is good to use the latest version. The compiler executable is named icc for C, icpc for C++, and ifort for Fortran. You should give optimization options at least **\-O2**, preferably **\-O3** or **\-fast**. You can also try to use the **\-xCORE-AVX2** option to the compiler to output AVX2 instructions.
*   pgi - often generates somewhat slower code, but it is stable so often it is easier to obtain working code, even with quite advanced optimizations. The compiler executable is named pgcc for C, pgCC for C++, and pgfortran, pgf77, pgf90, or pgf95 for Fortran. For this compiler, you can generate code for Snowy using the following options "**UPDATES NEEDED**". Also give optimization options at least **\-O2**, preferably **\-Ofast**, even though the compile times are much longer, the result is often worth the wait.

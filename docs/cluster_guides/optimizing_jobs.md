# Optimizing jobs

The UPPMAX clusters use the [Slurm](slurm.md)
job scheduler.
However, a job may not have run optimally, i.e. reserving CPU power
and/or memory that is not used.

This page describes how to optimize your Slurm jobs.

## Commands

You will probably have good use of the following commands:

Command                                          |Description
-------------------------------------------------|--------------------------------------------------------
[finishedjobinfo](../software/finishedjobinfo.md)|information about finished jobs
[jobinfo](../software/jobinfo.md)                |telling you about running and waiting jobs
[jobstats](../software/jobstats.md)              |see CPU and memory use of finished job in a plot
**projinfo**                                     |telling you about the CPU hour usage of your projects
**projmembers**                                  |telling you about project memberships
**projsummary [project id]**                     |summarizes some useful information about projects
[uquota](../software/uquota.md)                  |telling you about your file system usage

???- info "Working on Snowy? Use -M snowy"

    For Slurm commands and for commands like **projinfo**, [jobinfo](../software/jobinfo.md) and **finishedjobinfo**,
    you may use the `-M` flag to ask for the answer to be given
    for a system that you are not logged in to.
    For example, when logged into Rackham,
    you may ask about information about current core hour usage on Snowy,
    with the command `projinfo -M Snowy`

## Check you storage with [`uquota`](../software/uquota.md)

## Check your CPU hour usage with ``projinfo``

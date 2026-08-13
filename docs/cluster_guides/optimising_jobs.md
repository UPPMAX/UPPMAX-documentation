# Optimising jobs

The UPPMAX clusters use the [Slurm](slurm.md)
job scheduler.
However, a job may not have run optimally, i.e. reserving CPU power
and/or memory that is not used.

This page describes how to optimise your Slurm jobs.

## Commands

You will probably have good use of the following commands:

Command                                          |Description
-------------------------------------------------|--------------------------------------------------------
[finishedjobinfo](../software/finishedjobinfo.md)|information about finished jobs
[jobinfo](../software/jobinfo.md)                |telling you about running and waiting jobs
[jobstats](../software/jobstats.md)              |see CPU and memory use of finished job in a plot
`projinfo`                                       |telling you about the CPU hour usage of your projects
`projmembers`                                    |telling you about project memberships
`projsummary [project id]`                       |summarises some useful information about projects
[uquota](../software/uquota.md)                  |telling you about your file system usage

## Check you storage with [`uquota`](../software/uquota.md)

## Check your CPU hour usage with ``projinfo``

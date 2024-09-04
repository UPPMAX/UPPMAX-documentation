---
tags:
  - scancel
---

# `scancel`

The [job scheduler](../cluster_guides/slurm.md) consists of many
programs to manage jobs.
`scancel` is a tool to cancel jobs that are in the job queue or are running.

Usage:

```bash
scancel [job_number]
```

Where the `[job_number]` is the number of the job.
You can see the job number when submitting a job using [`sbatch`](sbatch.md)
and you can find it in the job queue (when doing [`squeue`](squeue.md)).

For example:

```bash
[sven@rackham3 ~]$ sbatch -A my_project my_script.sh 
Submitted batch job 49311056
[sven@rackham3 ~]$ scancel 49311056
[sven@rackham3 ~]$ 
```

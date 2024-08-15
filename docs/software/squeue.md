# squeue

The [job scheduler](../cluster_guides/slurm.md) consists of many
programs to manage jobs.
`squeue` is a tool to view information about the job queues.

View all jobs in the queue:

```bash
squeue
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham1 ~]$ squeue | head -n 1; squeue | shuf | head
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
              49086999      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086465      core sbatch_l matca755 PD       0:00      1 (Priority)
              49085829      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086067      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086600      core sbatch_l matca755 PD       0:00      1 (Priority)
              49087075      core sbatch_l matca755 PD       0:00      1 (Priority)
              49080199      node /proj/sn torsteng PD       0:00      1 (Priority)
              49088741      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086825      core sbatch_l matca755 PD       0:00      1 (Priority)
              49087385      core sbatch_l matca755 PD       0:00      1 (Priority)
    ```

View your jobs in the queue:

```bash
squeue -u $USER
```

???- question "How does that look like?"

    Your output will be similar to this, when you have no jobs in the queue:

    ```bash
    [richel@rackham1 ~]$ squeue -u $USER
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    ```

# interactive

`interactive` is a tool to [start an interactive node](../cluster_guides/start_interactive_node.md).

```bash
[sven@rackham1 sven]$ interactive -h
Usage: interactive -A PROJECT [OPTION]...
Use salloc to start an interactive job.

The options are the same as for the sbatch command, but no batch script must be specified.
If you do not specify partition and timelimit, some defaults will be presented and used.

To start quickly, you may need to specify a timelimit no longer than 15 minutes and "--qos=short",
otherwise you have to wait in queue like other Slurm jobs.

If you run X and forward X to Rackham, you should be able to use X on the first node of your job.
```

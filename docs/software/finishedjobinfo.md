# `finishedjobinfo`

`finishedjobinfo` is a program to help [optimize Slurm jobs](../cluster_guides/optimizing_jobs).

## Show the help

To show the help of `finishedjobinfo`, in a terminal , do:

```
finishedjobinfo -h
```

???- question "How does that look like?"

    ```
    [sven@rackham3 ~]$ finishedjobinfo -h
    Usage: finishedjobinfo  [-h] [-M cluster_name] [-j jobid[,jobid...]] [-m|-y|-s YYYY-MM-DD[/hh:mm:ss]] [-e YYYY-MM-DD[/hh:mm:ss]] [project_or_user]...
        -h        Ask for help
        -M        Request data from a named other cluster
        -j        Request data for a specific jobid or jobids (comma-separated)
        -q        Quiet, quick, abbreviated output (no QOS or memory information)
        -v        Verbose, tells a little more
        -m        Start time is start of this month
        -y        Start time is start of this year
        -s        Request a start time (default is a month back in time)
        -e        Request an end time (default is now)
        Time can also be specified as NOW, TODAY, YYYY, YYYY-MM, YYYY-w<week number>, w<week number>, hh:mm:ss, or name of month

    Meaning of jobstate:
    CANCELLED    Job was cancelled, before or after it had started
    COMPLETED    Job run to finish, last command gave exit code 0
    FAILED        Job crashed or at least ended with an exit code that was not 0
    NODE_FAIL    One of your job nodes experienced a major problem, perhaps your job used all available memory
    TIMEOUT        Job exceeded the specified timelimit and was therefore terminated
    ````

## Show the information about a specific job

Use `finishedjobinfo -j [job_number]` to get information about a specific
job, where `[job_number]` is the job number, 
for example `finishedjobinfo -j 44981366`.

???- question "How does that look like?"

    Here is an example output:

    ```
    [richel@rackham3 ~]$ finishedjobinfo -j 44981366
    2024-02-09 12:30:37 jobid=44981366 jobstate=TIMEOUT username=richel account=staff nodes=r35 procs=1 partition=core qos=normal jobname=run_beast2.sh maxmemory_in_GiB=0.1 maxmemory_node=r35 timelimit=00:01:00 submit_time=2024-02-09T12:27:29 start_time=2024-02-09T12:29:18 end_time=2024-02-09T12:30:37 runtime=00:01:19 margin=-00:00:19 queuetime=00:01:49
    ```

    > 2024-02-09 12:30:37 
    > jobid=44981366 
    > jobstate=TIMEOUT username=richel account=staff 
    > nodes=r35 
    > procs=1 partition=core qos=normal jobname=run_beast2.sh maxmemory_in_GiB=0.1 maxmemory_node=r35 timelimit=00:01:00 submit_time=2024-02-09T12:27:29 start_time=2024-02-09T12:29:18 end_time=2024-02-09T12:30:37 runtime=00:01:19 margin=-00:00:19 queuetime=00:01:49

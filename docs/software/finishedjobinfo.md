# `finishedjobinfo`

`finishedjobinfo` shows information on jobs that have finished,
which is useful to help [optimize Slurm jobs](../cluster_guides/optimizing_jobs.md).

## Usage

```bash
finishedjobinfo
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ finishedjobinfo
    2024-10-08 00:00:01 jobid=50661814 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r65 procs=1 partition=core qos=normal jobname=P8913_295.chr12 maxmemory_in_GiB=2.1 maxmemory_node=r65 timelimit=12:00:00 submit_time=2024-10-07T21:07:37 start_time=2024-10-07T21:15:52 end_time=2024-10-08T00:00:01 runtime=02:44:09 margin=09:15:51 queuetime=00:08:15
    2024-10-08 00:00:09 jobid=50661456 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r437 procs=1 partition=core qos=normal jobname=P8913_276.chr16 maxmemory_in_GiB=2.1 maxmemory_node=r437 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:09 runtime=02:48:44 margin=09:11:16 queuetime=00:03:56
    2024-10-08 00:00:13 jobid=50661186 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r349 procs=1 partition=core qos=normal jobname=P8913_262.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r349 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:13 runtime=02:48:50 margin=09:11:10 queuetime=00:04:00
    2024-10-08 00:00:19 jobid=50661172 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r344 procs=1 partition=core qos=normal jobname=P8913_261.chr18 maxmemory_in_GiB=2.1 maxmemory_node=r344 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:19 runtime=02:48:56 margin=09:11:04 queuetime=00:04:00
    2024-10-08 00:00:23 jobid=50661695 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r370 procs=1 partition=core qos=normal jobname=P8913_289.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r370 timelimit=12:00:00 submit_time=2024-10-07T21:07:35 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:23 runtime=02:44:34 margin=09:15:26 queuetime=00:08:14
    2024-10-08 00:00:27 jobid=50661466 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r438 procs=1 partition=core qos=normal jobname=P8913_277.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r438 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:27 runtime=02:49:02 margin=09:10:58 queuetime=00:03:56
    2024-10-08 00:00:39 jobid=50661663 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r360 procs=1 partition=core qos=normal jobname=P8913_287.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r360 timelimit=12:00:00 submit_time=2024-10-07T21:07:34 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:39 runtime=02:44:50 margin=09:15:10 queuetime=00:08:15
    2024-10-08 00:00:43 jobid=50661471 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r441 procs=1 partition=core qos=normal jobname=P8913_277.chr12 maxmemory_in_GiB=2.1 maxmemory_node=r441 timelimit=12:00:00 submit_time=2024-10-07T21:07:30 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:43 runtime=02:49:18 margin=09:10:42 queuetime=00:03:55
    2024-10-08 00:00:58 jobid=50661227 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r387 procs=1 partition=core qos=normal jobname=P8913_264.chr16 maxmemory_in_GiB=2.1 maxmemory_node=r387 timelimit=12:00:00 submit_time=2024-10-07T21:07:24 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:58 runtime=02:49:35 margin=09:10:25 queuetime=00:03:59
    2024-10-08 00:01:00 jobid=50661458 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r437 procs=1 partition=core qos=normal jobname=P8913_276.chr18 maxmemory_in_GiB=2.1 maxmemory_node=r437 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:01:00 runtime=02:49:35 margin=09:10:25 queuetime=00:03:56
    ```


## Show the help

To show the help of `finishedjobinfo`, in a [terminal](../software/terminal.md) , do:

```bash
finishedjobinfo -h
```

???- question "How does that look like?"

    ```bash
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

    ```bash
    [richel@rackham3 ~]$ finishedjobinfo -j 44981366
    2024-02-09 12:30:37 jobid=44981366 jobstate=TIMEOUT username=richel account=staff nodes=r35 procs=1 partition=core qos=normal jobname=run_beast2.sh maxmemory_in_GiB=0.1 maxmemory_node=r35 timelimit=00:01:00 submit_time=2024-02-09T12:27:29 start_time=2024-02-09T12:29:18 end_time=2024-02-09T12:30:37 runtime=00:01:19 margin=-00:00:19 queuetime=00:01:49
    ```

    > 2024-02-09 12:30:37
    > jobid=44981366
    > jobstate=TIMEOUT username=richel account=staff
    > nodes=r35
    > procs=1 partition=core qos=normal jobname=run_beast2.sh maxmemory_in_GiB=0.1 maxmemory_node=r35 timelimit=00:01:00 submit_time=2024-02-09T12:27:29 start_time=2024-02-09T12:29:18 end_time=2024-02-09T12:30:37 runtime=00:01:19 margin=-00:00:19 queuetime=00:01:49

## How do I find jobs that have finished and took longer than an hour and less than a day?

```bash
finishedjobinfo | grep "runtime.[0-9][1-9]"
```

Press `CTRL-C` to stop the process: it will take very long to finish.

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ finishedjobinfo | grep "runtime.[0-9][1-9]"
    2024-10-08 00:00:01 jobid=50661814 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r65 procs=1 partition=core qos=normal jobname=P8913_295.chr12 maxmemory_in_GiB=2.1 maxmemory_node=r65 timelimit=12:00:00 submit_time=2024-10-07T21:07:37 start_time=2024-10-07T21:15:52 end_time=2024-10-08T00:00:01 runtime=02:44:09 margin=09:15:51 queuetime=00:08:15
    2024-10-08 00:00:09 jobid=50661456 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r437 procs=1 partition=core qos=normal jobname=P8913_276.chr16 maxmemory_in_GiB=2.1 maxmemory_node=r437 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:09 runtime=02:48:44 margin=09:11:16 queuetime=00:03:56
    2024-10-08 00:00:13 jobid=50661186 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r349 procs=1 partition=core qos=normal jobname=P8913_262.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r349 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:13 runtime=02:48:50 margin=09:11:10 queuetime=00:04:00
    2024-10-08 00:00:19 jobid=50661172 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r344 procs=1 partition=core qos=normal jobname=P8913_261.chr18 maxmemory_in_GiB=2.1 maxmemory_node=r344 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:19 runtime=02:48:56 margin=09:11:04 queuetime=00:04:00
    2024-10-08 00:00:23 jobid=50661695 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r370 procs=1 partition=core qos=normal jobname=P8913_289.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r370 timelimit=12:00:00 submit_time=2024-10-07T21:07:35 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:23 runtime=02:44:34 margin=09:15:26 queuetime=00:08:14
    2024-10-08 00:00:27 jobid=50661466 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r438 procs=1 partition=core qos=normal jobname=P8913_277.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r438 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:27 runtime=02:49:02 margin=09:10:58 queuetime=00:03:56
    2024-10-08 00:00:39 jobid=50661663 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r360 procs=1 partition=core qos=normal jobname=P8913_287.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r360 timelimit=12:00:00 submit_time=2024-10-07T21:07:34 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:39 runtime=02:44:50 margin=09:15:10 queuetime=00:08:15
    ```

    This output took around 1 second to produce.

## How do I find jobs that have finished and took longer than an hour?

```bash
finishedjobinfo | grep -E "runtime.([0-9]-)?[0-9][1-9]"
```

Press `CTRL-C` to stop the process: it will take very long to finish.

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ finishedjobinfo | grep -E "runtime.([0-9]-)?[0-9][1-9]"
    2024-10-08 00:00:01 jobid=50661814 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r65 procs=1 partition=core qos=normal jobname=P8913_295.chr12 maxmemory_in_GiB=2.1 maxmemory_node=r65 timelimit=12:00:00 submit_time=2024-10-07T21:07:37 start_time=2024-10-07T21:15:52 end_time=2024-10-08T00:00:01 runtime=02:44:09 margin=09:15:51 queuetime=00:08:15
    2024-10-08 00:00:09 jobid=50661456 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r437 procs=1 partition=core qos=normal jobname=P8913_276.chr16 maxmemory_in_GiB=2.1 maxmemory_node=r437 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:09 runtime=02:48:44 margin=09:11:16 queuetime=00:03:56
    2024-10-08 00:00:13 jobid=50661186 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r349 procs=1 partition=core qos=normal jobname=P8913_262.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r349 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:13 runtime=02:48:50 margin=09:11:10 queuetime=00:04:00
    2024-10-08 00:00:19 jobid=50661172 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r344 procs=1 partition=core qos=normal jobname=P8913_261.chr18 maxmemory_in_GiB=2.1 maxmemory_node=r344 timelimit=12:00:00 submit_time=2024-10-07T21:07:23 start_time=2024-10-07T21:11:23 end_time=2024-10-08T00:00:19 runtime=02:48:56 margin=09:11:04 queuetime=00:04:00
    2024-10-08 00:00:23 jobid=50661695 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r370 procs=1 partition=core qos=normal jobname=P8913_289.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r370 timelimit=12:00:00 submit_time=2024-10-07T21:07:35 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:23 runtime=02:44:34 margin=09:15:26 queuetime=00:08:14
    2024-10-08 00:00:27 jobid=50661466 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r438 procs=1 partition=core qos=normal jobname=P8913_277.chr7 maxmemory_in_GiB=2.1 maxmemory_node=r438 timelimit=12:00:00 submit_time=2024-10-07T21:07:29 start_time=2024-10-07T21:11:25 end_time=2024-10-08T00:00:27 runtime=02:49:02 margin=09:10:58 queuetime=00:03:56
    2024-10-08 00:00:39 jobid=50661663 jobstate=COMPLETED username=mrendon account=naiss2023-5-478 nodes=r360 procs=1 partition=core qos=normal jobname=P8913_287.chr13 maxmemory_in_GiB=2.1 maxmemory_node=r360 timelimit=12:00:00 submit_time=2024-10-07T21:07:34 start_time=2024-10-07T21:15:49 end_time=2024-10-08T00:00:39 runtime=02:44:50 margin=09:15:10 queuetime=00:08:15
    ```

    This output took around 1 second to produce.

## How do I find jobs that have finished and took longer than a day?

```bash
finishedjobinfo | grep "runtime.[0-9]-"
```

Press `CTRL-C` to stop the process: it will take very long to finish.

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ finishedjobinfo | grep "runtime.[0-9]-"
    2024-10-08 00:01:18 jobid=50597318 jobstate=COMPLETED username=nikolay account=naiss2024-22-35 nodes=r356 procs=20 partition=node qos=normal jobname=168011 maxmemory_in_GiB=5.3 maxmemory_node=r356 timelimit=10-00:00:00 submit_time=2024-10-02T10:36:59 start_time=2024-10-06T21:05:31 end_time=2024-10-08T00:01:18 runtime=1-02:55:47 margin=8-21:04:13 queuetime=4-10:28:32
    2024-10-08 00:21:55 jobid=50597286 jobstate=COMPLETED username=nikolay account=naiss2024-22-35 nodes=r432 procs=20 partition=node qos=normal jobname=1578718 maxmemory_in_GiB=5.3 maxmemory_node=r432 timelimit=10-00:00:00 submit_time=2024-10-02T10:36:10 start_time=2024-10-06T14:32:36 end_time=2024-10-08T00:21:55 runtime=1-09:49:19 margin=8-14:10:41 queuetime=4-03:56:26
    ```

    This output took 30 seconds to produce as there were few jobs at that time
    that took longer than a day to finish.

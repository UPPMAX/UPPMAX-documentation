# MATLAB user guide

## The MATLAB [module](../cluster_guides/modules.md)

MATLAB can be started only if you load the matlab module first. Most of available official toolboxes are also available. At the time of this writing, our most recent installation is: ``matlab/R2023b``

Doing:

```console
module load matlab
```

will give you the latest version.

If you need a different version, check the availability by:

```console
module avail matlab
```

To get started with MATLAB do (for instance):

```console
module load matlab/R2023a
matlab &
```

That will start a matlab session with the common GUI. Use ``&`` to have MATLAB in background making terminal still active for other work.

A good and important suggestion is that you always specify a certain version. This is to be able to reproduce your work, a very important key in research!

## First time, since May 13 2024

- If you use MATLAB after May 13 2024, of any version, you have to do the following step to be able to use the full features of running parallel jobs.
    - only needs to be called once per version of MATLAB.
    - Note, however, that on Bianca this has to be done separately.

- After logging into the cluster, configure MATLAB to run parallel jobs on the cluster by calling the shell script configCluster.sh.

```console
module load matlab/<version>
configCluster.sh <project-ID>    # Note: no '-A'
```

- This will run a short configuration job in an interactive session.
- Jobs will now default to the cluster rather than submit to the local machine.
- It should look like this (example for Bianca)

![matlab configCluster.sh](img/matlab_configCluster.PNG)

- The session should exit automatically but if not you can end the session by
    - ``exit``
    - or ``<CTRL-C>``
- When done, start Matlab as you usually do with  ``matlab &``.

!!! warning

    - Do these steps for each matlab version you will use.
    - On Bianca you need to do this for each sens project that will use MATLAB, as well.

!!! tip

    - Check the Matlab version for which you have set the slurm configuration by

    ```bash
    ls -l .matlab/*/parallel.mlsettings
    ```
    
    - Look for dates from May 2024 and onwards.

## Introduction

Using MATLAB on the cluster enables you to utilize high performance facilities like:

- [Parallel computing](https://se.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html?s_tid=CRUX_lftnav)
    - Parallel for-loops
    - Evaluate functions in the background
- [Big data processing](https://se.mathworks.com/help/parallel-computing/big-data-processing.html?s_tid=CRUX_lftnav)
    - Analyze big data sets in parallel
- [Batch Processing](https://se.mathworks.com/help/parallel-computing/batch-processing.html?s_tid=CRUX_lftnav)
    - Offload execution of functions to run in the background
- [GPU computing](https://se.mathworks.com/help/parallel-computing/gpu-computing.html?s_tid=CRUX_lftnav) (Available on Bianca and Snowy)
    - Accelerate your code by running it on a GPU
- Machine & Deep learning
    - [Statistics and Machine Learning](https://se.mathworks.com/help/stats/index.html)
    - [Deep Learning](https://se.mathworks.com/help/deeplearning/index.html)

[See MathWork's complete user guide](https://se.mathworks.com/help/parallel-computing/index.html?s_tid=CRUX_lftnav)

Some online tutorials and courses:

- [Parallel computing](https://se.mathworks.com/solutions/parallel-computing.html)
- Machine Learning
    - [Machine learning article](https://se.mathworks.com/solutions/machine-learning.html)
    - [Machine learning tutorial](https://matlabacademy.mathworks.com/details/machine-learning-onramp/machinelearning)
- Deep Learning
    - [Deep learning article](https://se.mathworks.com/solutions/deep-learning.html)
    - [Deep learning tutorial](https://matlabacademy.mathworks.com/details/deep-learning-onramp/deeplearning)

## Running MATLAB

### Graphical user interface

To start MATLAB with its usual graphical interface, start it with:

```console
matlab
```

If you will use significant resources, like processor or RAM, you should start an interactive session on a calculation node. Use at least 2 cores (-n 2), when running interactive. Otherwise MATLAB may not start. You can use several cores if you will do some parallel calculations (see parallel section below). Example:

```console
interactive -A <proj> -p core -n 2 -t 1:0:0
```

This example starts a session with 2 cores for a wall time of 1 hour.

### MATLAB in terminal

For simple calculations it is possible to start just a command shell in your [terminal](../software/terminal.md):

```console
matlab -nodisplay
```

Exit with 'exit'.

Run script from terminal or bash script

In order to run a script directly from terminal:

```console
matlab -batch "run('<path/to/script.m>')" | tail -n +2
```

List all ways to run/start MATLAB:

```console
matlab -h
```

### Thinlinc

You may get the best of the MATLAB graphics by runing it the ThinLinc environment.

- For rackham (in [ThinLinc app](https://www.cendio.com/thinlinc/download/)): ``rackham-gui.uppmax.uu.se``

- For Bianca (from web-browser): <https://bianca.uppmax.uu.se>

You may want to confer our UPPMAX [ThinLinc user guide](../software/thinlinc.md).

## How to run parallel jobs

### How to run parallel jobs for the first time, since May 13 2024

- If you use MATLAB after May 13 2024, of any version, you have to do the following step to be able to use the full features of running parallel jobs.
    - only needs to be called once per version of MATLAB.
    - Note, however, that on Bianca this has to be done separately.
- After logging into the cluster, configure MATLAB to run parallel jobs on the cluster by calling the shell script configCluster.sh.

```console
module load matlab
configCluster.sh <project-ID>    # Note: no '-A'
```

- This will run a short configuration job in an interactive session, closing itself when done.
- Jobs will now default to the cluster rather than submit to the local machine.

### Two MATLAB commands

Two commands in MATLAB are important to make your code parallel:

- **``parfor``** will distribute your "for loop" among several workers (cores)
- **``parfeval``** runs a section or a function on workers in the background

### Use interactive matlab

First, start an interactive session on a calculation node with, for instance 8 cores by:

```console
interactive -A <project> -p core -n 8 -t 3:00:00
```

In MATLAB open a parallel pool of 8 local workers:

```matlab
>> p = parpool(8)
```

What happens if you try to run the above command twice?  You can't run multiple parallel pools at the same time. Query the number of workers in the parallel pool:

```matlab
>> p.NumWorkers
```

``gcp`` will "get current pool" and return a handle to it.  If a pool has not already been started, it will create a new one first and then return the handle to it:

```matlab
>> p = gcp
```

Shutdown the parallel pool:

```matlab
>> delete(p)
```

Will check to see if a pool is open and if so, deletes it.

```matlab
>> delete(gcp('nocreate'))
```

This will delete a pool if it exists, but won't create one first if it doesn't already exist.

With parpool('local') or parcluster('local') you will use settings for 'local' . With parpool('local',20) you will get 20 cores, but else the 'local' settings, like automatic shutdown after 30 minutes.
You can change your settings here: HOME > ENVIRONMENT > Parallel > Parallel preferences.

### MATLAB Batch

With MATLAB you can e.g. submit jobs directly to our job queue scheduler, without having to use Slurm's commands directly. Let us first make two small function. The first one, little simpler, saved in the file ``parallel_example.m``:

```matlab
    function t = parallel_example(nLoopIters, sleepTime)
      t0 = tic;
      parfor idx = 1:nLoopIters
        A(idx) = idx;
        pause(sleepTime);
      end
      t = toc(t0);
```

and the second, little longer, saved in ``parallel_example_hvy.m``:

```matlab
    function t = parallel_example_hvy(nLoopIters, sleepTime)
      t0 = tic;
      ml = 'module list';
      [status, cmdout] = system(ml);
      parfor idx = 1:nLoopIters
        A(idx) = idx;
        for foo = 1:nLoopIters*sleepTime
          A(idx) = A(idx) + A(idx);
          A(idx) = A(idx)/3;
        end
      end
```

Begin by running the command

```matlab
>> configCluster %(on Bianca it will look a little different)
```

in Matlab Command Window to choose a cluster configuration. Matlab will set up a configuration and will then print out some instructions, seen below. You can also set environments that is read if you don't specify it. Go to HOME > ENVIRONMENT > Parallel > Parallel preferences.

```matlab
       [1] rackham
       [2] snowy
    Select a cluster [1-2]: 1
    >>
    >> c = parcluster('rackham'); %on Bianca 'bianca Rxxxxx'
    >> c.AdditionalProperties.AccountName = 'snic2021-X-YYY';
    >> c.AdditionalProperties.QueueName = 'node';
    >> c.AdditionalProperties.WallTime = '00:10:00';
    >> c.saveProfile
    >> job = c.batch(@parallel_example, 1, {90, 5}, 'pool', 19) %19 is for 20 cores. On Snowy and Bianca use 15.
    >> job.wait
    >> job.fetchOutputs{:}
```

Follow them. These inform you what is needed in your script or in command line to run in parallel on the cluster. The line ``c.batch(@parallel_example, 1, {90, 5}, 'pool', 19)`` can be understood as put the function ``parallel_example`` to the batch queue. The arguments to batch are:

```matlab
    c.batch(function name, number of output arguments, {the inputs to the function}, 'pool', no of additional workers to the master)

    c.batch(@parallel_example, 1 (t=toc(t0)), {nLoopIters=90, sleepTime=5}, 'pool', 19)
```

To see the output to screen from jobs, use job.Tasks.Diary. Output from the submitted function is fetched with 'fetchOutputs()'.

For jobs using several nodes (in this case 2) you may modify the call to:

```matlab
    >> configCluster
       [1] rackham
       [2] snowy
    Select a cluster [1-2]: 1
    >>
    >> c = parcluster('rackham'); %on Bianca 'bianca R<version>'
    >> c.AdditionalProperties.AccountName = 'snic2021-X-YYY';
    >> c.AdditionalProperties.QueueName = 'node';
    >> c.AdditionalProperties.WallTime = '00:10:00';
    >> c.saveProfile
    >> job = c.batch(@parallel_example_hvy, 1, {1000, 1000000}, 'pool', 39)% 31 on Bianca or Snowy
    >> job.wait
    >> job.fetchOutputs{:}
```

where parallel_example-hvy.m was the script presented above.

For the moment jobs are hard coded to be node jobs. This means that if you request 21 tasks instead (20 + 1) you will get a 2 node job, but only 1 core will be used on the second node. In this case you'd obviously request 40 tasks (39 + 1) instead.

For more information about Matlab's Distributed Computing features please see [Matlab's HPC Portal](https://se.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html?s_tid=CRUX_lftnav).

### GPU

Running MATLAB with GPU is, as of now, only possible on the Snowy and Bianca clusters. Uppsala University affiliated staff and students with allocation on Snowy can use this resource.

Start an interactive session with at least 2 cores (otherwise MATLAB may not start). On Snowy, getting (for instance) 2 cpu:s (-n 2) and 1 gpu:

```console
interactive -A <proj> -n 2 -M snowy --gres=gpu:1  -t 3:00:00
```

On Bianca, getting 3 cpu:s and 1 gpu:

```console
interactive -A <proj> -n 3 -C gpu --gres=gpu:1 -t 01:10:00
```

Note that wall time ``-t`` should be set to more than one hour to not automatically put job in ``devel`` or ``devcore`` queue, which is not allowed for gpu jobs. Also check the GPU quide for Snowy at Using the GPU nodes on Snowy.

Load MATLAB module and start matlab as usual (with &) in the new session. Then test if the gpu device is found by typing:

```matlab
>> gpuDevice
>> gpuDeviceCount
```

On Bianca you may get an error. Follow the instructons and you can run anyway. Example code:

```matlab
>> A = gpuArray([1 0 1; -1 -2 0; 0 1 -1]);
>> e = eig(A);
```

For more information about GPU computing confer the [MathWorks web about GPU computing](https://se.mathworks.com/help/parallel-computing/gpu-computing.html?s_tid=CRUX_lftnav).

#### Deep Learning with GPUs

For many functions in Deep Learning Toolbox, GPU support is automatic if you have a suitable GPU and Parallel Computing Toolbox™. You do not need to convert your data to gpuArray. The following is a non-exhaustive list of functions that, by default, run on the GPU if available.

- [trainNetwork](https://se.mathworks.com/help/deeplearning/ref/trainnetwork.html) (Deep Learning Toolbox)

- [predict](https://se.mathworks.com/help/deeplearning/ref/seriesnetwork.predict.html) (Deep Learning Toolbox)

- [predictAndUpdateState](https://se.mathworks.com/help/deeplearning/ref/seriesnetwork.predictandupdatestate.html) (Deep Learning Toolbox)

- [classify](https://se.mathworks.com/help/deeplearning/ref/seriesnetwork.classify.html) (Deep Learning Toolbox)

- [classifyAndUpdateState](https://se.mathworks.com/help/deeplearning/ref/seriesnetwork.classifyandupdatestate.html) (Deep Learning Toolbox)

- [activations](https://se.mathworks.com/help/deeplearning/ref/seriesnetwork.activations.html) (Deep Learning Toolbox)

### Shell batch jobs

Sometimes when matlab scripts are part of workflows/pipelines it may be easier to work directly with the batch scripts.

Batch script example with 2 nodes (Rackham), matlab_submit.sh.

```bash
#!/bin/bash -l
#SBATCH -A <proj>
#SBATCH -p devel
#SBATCH -N 2
#SBATCH -n 40
module load matlab/R2020b &> /dev/null
srun -N 2 -n 40  matlab -batch "run('<path/to/m-script>')"
```

Run with

```console
sbatch matlab_submit.sh
```

## Common problems

Sometimes things do not work out.

As a first step, try with removing local files:

```console
rm -rf ~/.matlab
```

If the graphics is slow, try:

```console
vglrun matlab -nosoftwareopengl
```

Unfortunately this only works from login nodes.

You may want to run MATLAB on a single thread. This makes it work:

```console
matlab -singleCompThread
```

## MATLAB client on the desktop

The Rackham MATLAB support package can be found at [uppsala.Desktop.zip](https://github.com/UPPMAX/UPPMAX-documentation/raw/main/docs/software/files/matlab/uppsala.Desktop.zip).

1. Download the ZIP file and start MATLAB.
2. The ZIP file should be unzipped in the location returned by calling

    ```matlab
    >> userpath
    ```

    You can unzip from MATLAB's Command window.

3. Configure MATLAB to run parallel jobs on the cluster by calling configCluster.  configCluster only needs to be called once per version of MATLAB.

    ```matlab
    >> configCluster
    ```

Submission to the cluster requires SSH credentials.  You will be prompted for username and password or identity file (private key).  The username and location of the private key will be stored in MATLAB for future sessions.
Jobs will now default to the cluster rather than submit to the local machine.
NOTE: To submit to the local machine instead of the cluster, run the following:

```matlab
>> % Get a handle to the local resources
>> c = parcluster('local');
```

CONFIGURING JOBS
Prior to submitting the job, various parameters can be assigned, such as queue, e-mail, walltime, etc.  The following is a partial list of parameters.  See AdditionalProperties for the complete list.  Only AccountName, Partition, MemUsage and WallTime.

```matlab
>> % Get a handle to the cluster
>> c = parcluster;

[REQUIRED]

>> % Specify the account
>> c.AdditionalProperties.AccountName = 'account-name';

>> % Specify the partition
>> c.AdditionalProperties.Partition = 'partition-name';

>> % Specify memory to use, per core (default: 4gb)
>> c.AdditionalProperties.MemUsage = '6gb';

>> % Specify the wall time (e.g., 1 day, 5 hours, 30 minutes)
>> c.AdditionalProperties.WallTime = '1-05:30';

[OPTIONAL]

>> % Specify a constraint 
>> c.AdditionalProperties.Constraint = 'feature-name';

>> % Request email notification of job status
>> c.AdditionalProperties.EmailAddress = 'user-id@uppmax.uu.se';

>> % Specify number of GPUs
>> c.AdditionalProperties.GPUsPerNode = 1;
>> c.AdditionalProperties.GPUCard = 'gpu-card';

>> % Specify cores per node
>> c.AdditionalProperties.ProcsPerNode = 4;

>> % Set node exclusivity (default: false)
>> c.AdditionalProperties.RequireExclusiveNode = true;

>> % Use reservation 
>> c.AdditionalProperties.Reservation = 'reservation-name';
```

Save changes after modifying AdditionalProperties for the above changes to persist between MATLAB sessions.

```matlab
>> c.saveProfile
```

To see the values of the current configuration options, display AdditionalProperties.

```matlab
>> % To view current properties
>> c.AdditionalProperties
```

Unset a value when no longer needed.

```matlab
>> % Turn off email notifications 
>> c.AdditionalProperties.EmailAddress = '';
>> c.saveProfile
```

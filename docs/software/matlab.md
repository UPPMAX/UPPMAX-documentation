# MATLAB user guide

The MATLAB module

MATLAB can be started only if you load the matlab module first. Most of available official toolboxes are also available. At the time of this writing, our most recent installation is:

    matlab/R2020b

If you need a different version, check the availability by:

        $ module avail matlab

For version before 2017 check this page. Don’t forget to replace clustername “tintin” with “rackham”.

To get started with MATLAB do (for instance):

        $ module load matlab/R2020b

        $ matlab &

That will start a matlab session with the common GUI. Use "&" to have MATLAB in background making terminal still active for other work.

Doing:

        $ module load matlab 

will give you matlab/R2019a on Rackham, otherwise the latest version.

A good and important suggestion is that you always specify a certain version. This is to be able to reproduce your work, a very important key in research!

## Introduction

Using MATLAB on the cluster enables you to utilize high performance facilities like:

    Parallel computing 
        Parallel for-loops
        Evaluate functions in the background
    Big data processing
        Analyze big data sets in parallel
    Batch Processing
        Offload execution of functions to run in the background
    GPU computing (Available on Snowy)
        Accelerate your code by running it on a GPU
    Machine & Deep learning
        Statistics and Machine Learning
        Deep Learning

See Mathwork's complete user guide.

Some online tutorials and courses:

    Parallel computing
    Machine Learning
        Machine learning article
        Machine learning tutorial
    Deep Learning
        Deep learning article
        Deep learning tutorial

## Running MATLAB
### Graphical user interface

To start MATLAB with its usual graphical interface, start it with:

        $ matlab

If you will use significant resources, like processor or RAM, you should start an interactive session on a calculation node. Use at least 2 cores (-n 2), when running interactive. Otherwise MATLAB may not start. You can use several cores if you will do some parallel calculations (see parallel section below). Example:

        $ interactive -A <proj> -p core -n 2 -t 1:0:0

This example starts a session with 2 cores for a wall time of 1 hour.
### 
MATLAB in terminal

For simple calculations it is possible to start just a command shell in your terminal:

        $ matlab -nodisplay

Exit with 'exit'.

Run script from terminal or bash script

In order to run a script directly from terminal:

        $ matlab -batch "run('<path/to/script.m>')" | tail -n +2

List all ways to run/start MATLAB:

        $ matlab -h

### Thinlinc

You may get the best of the MATLAB graphics by runing it the thinlinc environment.

For rackham (in ThinLinc app): rackham-gui.uppmax.uu.se

For Bianca (from web-browser): https://bianca.uppmax.uu.se

You may want to confer our UPPMAX ThinLinc user guide  
## How to run parallel jobs

### Two MATLAB commands

Two commands in MATLAB are important to make your code parallel:

    parfor will distribute your "for loop" among several workers (cores)
    parfeval runs a section or a function on workers in the background

### Use interactive matlab

First, start an interactive session on a calculation node with, for instance 8 cores by:

        $ interactive -A <project> -p core -n 8 -t 3:00:00

In MATLAB open a parallel pool of 8 local workers:

        >> p = parpool(8)

What happens if you try to run the above command twice?  You can't run multiple parallel pools at the same time. Query the number of workers in the parallel pool:

        >> p.NumWorkers

'gcp' will "get current pool" and return a handle to it.  If a pool has not already been started, it will create a new one first and then return the handle to it:

        >> p = gcp

Shutdown the parallel pool:

        >> delete(p)

Will check to see if a pool is open and if so, deletes it.

        >> delete(gcp('nocreate'))

This will delete a pool if it exists, but won't create one first if it doesn't already exist.

With parpool('local') or parcluster('local') you will use settings for 'local' . With parpool('local',20) you will get 20 cores, but else the 'local' settings, like automatic shutdown after 30 minutes.
You can change your settings here: HOME > ENVIRONMENT > Parallel > Parallel preferences.

### MATLAB Batch

With MATLAB you can e.g. submit jobs directly to our job queue scheduler, without having to use slurm's commands directly. Let us first make two small function. The first one, little simpler, saved in the file parallel_example.m:

    function t = parallel_example(nLoopIters, sleepTime) 
      t0 = tic; 
      parfor idx = 1:nLoopIters 
        A(idx) = idx; 
        pause(sleepTime); 
      end 
      t = toc(t0); 

and the second, little longer, saved in parallel_example_hvy.m:

    function t = parallel_example(nLoopIters, sleepTime) 
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

Begin by running the command

        >> configCluster %(on Bianca it will look a little different)

in Matlab Command Window to choose a cluster configuration. Matlab will set up a configuration and will then print out some instructions, seen below. You can also set environments that is read if you don't specify it. Go to HOME > ENVIRONMENT > Parallel > Parallel preferences. 

    "   [1] rackham
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
    >> job.fetchOutputs{:}"

Follow them. These inform you what is needed in your script or in command line to run in parallel on the cluster. The line "c.batch(@parallel_example, 1, {90, 5}, 'pool', 19)" can be understood as put the function "parallel_example" to the batch queue. The arguments to batch are:

    c.batch(function name, number of output arguments, {the inputs to the function}, 'pool', no of additional workers to the master)

    c.batch(@parallel_example, 1 (t=toc(t0)), {nLoopIters=90, sleepTime=5}, 'pool', 19)

To see the output to screen from jobs, use job.Tasks.Diary. Output from the submitted function is fetched with 'fetchOutputs()'.

For jobs using several nodes (in this case 2) you may modify the call to:

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

where parallel_example-hvy.m was the script presented above.

For the moment jobs are hard coded to be node jobs. This means that if you request 21 tasks instead (20 + 1) you will get a 2 node job, but only 1 core will be used on the second node. In this case you'd obviously request 40 tasks (39 + 1) instead.

For more information about Matlab's Distributed Computing features please see Matlab's HPC Portal.

### GPU

Running MATLAB with GPU is, as of now, only possible on the Snowy and Bianca clusters. Uppsala University affiliated staff and students with allocation on Snowy can use this resource.

Start an interactive session with at least 2 cores (otherwise MATLAB may not start). On Snowy, getting (for instance) 2 cpu:s (-n 2) and 1 gpu:

$ interactive -A <proj> -n 2 -M snowy --gres=gpu:1  -t 3:00:00

On Bianca, getting 3 cpu:s and 1 gpu:

$ interactive -A <proj> -n 3 -C gpu --gres=gpu:1 -t 01:10:00 

Note that wall time "-t" should be set to more than one hour to not automatically put job in "devel" or "devcore" queue, which is not allowed for gpu jobs. Also check the GPU quide for Snowy at Using the GPU nodes on Snowy.

Load MATLAB module and start matlab as usual (with &) in the new session. Then test if the gpu device is found by typing:

>> gpuDevice
>> gpuDeviceCount

On Bianca you may get an error. Follow the instructons and you can run anyway. Example code:

>> A = gpuArray([1 0 1; -1 -2 0; 0 1 -1]);
>> e = eig(A);

For more information about GPU computing confer the MathWorks web.

#### Deep Learning with GPUs

For many functions in Deep Learning Toolbox, GPU support is automatic if you have a suitable GPU and Parallel Computing Toolbox™. You do not need to convert your data to gpuArray. The following is a non-exhaustive list of functions that, by default, run on the GPU if available.

    trainNetwork (Deep Learning Toolbox)

    predict (Deep Learning Toolbox)

    predictAndUpdateState (Deep Learning Toolbox)

    classify (Deep Learning Toolbox)

    classifyAndUpdateState (Deep Learning Toolbox)

    activations (Deep Learning Toolbox)

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

$ sbatch matlab_submit.sh

## Common problems

Sometimes things do not work out.

As a first step, try with removing local files:

$ rm -rf ~/.matlab

If the graphics is slow, try:

$ vglrun matlab -nosoftwareopengl

Unfortunately this only works from login nodes.

You may want to run MATLAB on a single thread. This makes it work:

$ matlab -singleCompThread

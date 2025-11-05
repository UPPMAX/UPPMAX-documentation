# Using Slurm on Pelle

This page describes how to use Slurm on Pelle.

???- question "What is Slurm?"

    See [the general page about Slurm](slurm.md)

???- question "What is Pelle?"

    See [the general page about Pelle](pelle.md)

See [Slurm troubleshooting](slurm_troubleshooting.md)
how to fix Slurm errors.

???- note "Newer Slurm"

    - Slurm on Pelle have been upgraded to version 25.05.

    - Several UPPMAX-specific Slurm changes from previous clusters have been removed, to make the config use more Slurm defaults. This makes the system easier to maintain and will behave more similar to clusters at other sites. Unfortunately this means that some extra changes to job scripts can be needed when moving from Rackham/Snowy.

!!! warning

    - The max time limit for jobs is 10 days.
        - GPU jobs has a time limit of 2 days.

## `sbatch` (and `interactive`) on Pelle

`sbatch` (and `interactive`) work the same as on the other clusters,
the only difference is that some flags/options may be different, like partition name, see below.

???- question "Want to start an interactive session?"

    See [how to start an interactive session on Pelle](start_interactive_session_on_pelle.md)

Here it is shown how to submit a job with:

- Command-line Slurm parameters
- Slurm parameters in the script

## Partitions on Pelle

Partition flag is either ``--partition`` or ``-p``

Partition name|Description
--------------|----------------------------------
`pelle`       | (Default) Use one or more CPU cores
`fat`         | Use a fat node with 2 or 3 TB memory, see below
`gpu`         | GPU node, 2 types see below

### The `pelle` partition

The `pelle` partition is default so you can omit specifying ``-p`` or ``--partition``

Its allocates an ordinary CPU node (allows one to use one or more cores, up to 96 cores).

!!! warning

    - Time limit is 10 days on the CPU nodes.
    - You may, if really needed, ask for more through the support ``support@uppmax.uu.se``.

!!! info

    The compute node CPUs have Simultaneous multithreading (SMT) enabled. Each CPU core runs two Threads. In Slurm the Threads are
    referred to as CPUs. [Learn more here about SMT](slurm_on_pelle.md#smt)

#### Architecture

No of nodes     | CPUs                              | Cores<br/>Threads |  Memory     | Scratch | GPUs           | Name
--------------- | --------------------------------- | ----------------- | ---------   |-------- |--------------- |------------
115             |  AMD EPYC 9454P (Zen4)  2.75 GHz  | 48<br/>96         | **768 GiB** | 1.7 TB  | N/A            | p[1-115]

!!! note "Much more cores per node compared to Rackham"

    - You can now have 96 parallel processes per node!
    - :warning: Even more important that you not by mistake allocate a full node when needing just a part of it.
    - A full node is 768 GB, compared to 128 GB on Rackham. That means less need for a "fat" partition allocation.

#### Examples with core jobs

Here is the minimal use for one core:

```bash
sbatch -A [project_code] [script_filename]
```

For example:

```bash
sbatch -A staff my_script.sh
```

To specify multiple cores, use `--ntasks` (or `-n`) like this:

```bash
sbatch -A [project_code] --ntasks [number_of_cores] [script_filename]
```

For example:

```bash
sbatch -A staff --ntasks 2 my_script.sh
```

Here, two cores are used.

???- question "What is the relation between `ntasks` and number of cores?"

    Agreed, the flag `ntasks` only indicates the number of tasks.
    However, by default, the number of tasks per core is set to one.
    One can make this link explicit by using:

    ```bash
    sbatch -A [project_code] --partition core --ntasks [number_of_cores] --ntasks-per-core 1 [script_filename]
    ```

This is especially important if you might adjust core usage
of the job to be something less than a full node.

- One task, using two threads: ``--ntasks=1 --cpus-per-task=2``
- Two tasks, using one thread each: ``--ntasks=2 --cpus-per-task=1``


#### Examples with node jobs

- On Rackham you have used ``-p node`` or ``-p core`` to specify node/core jobs.
- This is not used on Pelle. Instead Slurm's standard options is used to specify the job requirements.

- Example to request 2 full nodes: ``--nodes=2 --exclusive``

#### Job memory specification

- Currently you do not have to request additional CPUs to get additional memory.
- You can use all Slurm options
    - ``--mem``
    - ``--mem-per-cpu``

### The `fat` partition

With the ``fat`` partition you reach compute nodes with more memory.

!!! warning

    - Time limit is 10 days on the fat nodes.
    - You may, if really needed, ask for more through the support ``support@uppmax.uu.se``.


Pelle has two fat nodes. One with 2 TiB of memory and one with 3 TiB.

!!! note

    Jobs on these nodes always allocate the entire node with all cores.

- To allocate 2 TB: ``-p fat -C 2TB``

    - Example: ``interactive -A staff -t 1:0:0 -p fat -C 2TB``

- To allocate 3 TB: ``-p fat -C 3TB``

    - Example: ``interactive -A staff -t 1:0:0 -p fat -C 3TB``

### The ``gpu`` partition

With the ``gpu`` partition you reach the nodes with GPUs.

!!! warning

    - Time limit is 2 days.
    - You may, if really needed, ask for more through the support ``support@uppmax.uu.se``.

There are two kinds of GPUs at the moment.

- 4 of the lighter type ``L40s``, enough for most problems. Each node has 10 (!) GPUs. Most often just one GPU is needed, so remember to state that you need just 1, see below.
- 2 of the large type ``H100``, which can be suitable for large training runs. Each node has 2 GPUs. Most often just one GPU is needed, so remember to state that you need just 1, see below.

Therefore, at first hand, allocate the default ``L40s`` and one of them

- To allocate L40s: ``-p gpu --gres=gpu:<number of GPUs>`` or ``-p gpu --gpus:l40s:<number of GPUs>``

    - Example with 1 GPU: ``interactive -A staff -t 1:0:0 -p gpu --gres=gpu:1``
    - Example with 11 GPUs: ``interactive -A staff -t 1:0:0 -p gpu --gres=gpu:11`` will fail because there are just 10 GPUs on one node!

- To allocate H100: ``-p gpu --gpus=h100:<number of GPUs>``

    - Example with 1 GPU: ``interactive -A staff -t 1:0:0 -p gpu --gpus=h100:1`
    - Example with 3 GPU: ``interactive -A staff -t 1:0:0 -p gpu --gpus=h100:3` will fail because there are just 2 GPUs on one node!

- Currently you do not have to request additional CPUs to get additional memory.
- You can use all Slurm options
    - ``--mem``
    - ``--mem-per-cpu``
    - ``--mem-per-gpu`` to specify memory requirements.

## `sbatch` a script with command-line Slurm parameters

The minimal command to use `sbatch` with command-line Slurm parameters is:

``` bash
sbatch -A [project_code] [script_filename]
```

where `[project_code]` is the project code, and `[script_filename]`
the name of a bash script, for example:

``` bash
sbatch -A uppmax2023-2-25 my_script.sh
```

???- question "Forgot your Rackham project?"

    One can go to the SUPR NAISS pages to see one's projects,

    ![Example of the Rackham project called 'UPPMAX 2023/2-25'](./img/naiss_supr_project_2023_2_25.png)

    > Example of the Rackham project called 'UPPMAX 2023/2-25'

    On the SUPR NAISS pages, projects are called 'UPPMAX [year]/[month]-[day]',
    for example, 'UPPMAX 2023/2-25'.
    The UPPMAX project name, as to be used on Rackham,
    has a slightly different name:
    the account name to use on Rackham is `uppmax[year]-[month]-[day]`,
    for example, `uppmax2023-2-25`

???- question "What is in the script file?"

    The script file `my_script.sh` is a minimal example script.
    Such a minimal example script could be:

    ```bash
    #!/bin/bash
    echo "Hello"
    ```

Again, what is shown here is a minimal use of [`sbatch`](../software/sbatch.md).

## `sbatch` a script with Slurm parameters in script

The minimal command to use `sbatch` with Slurm parameters in the script:

``` bash
sbatch [script_filename]
```

where `[script_filename]` the name of a bash script, for example:

```bash
sbatch my_script.sh
```

The script must contain at least the following lines:

```text
#SBATCH -A [project_code]
```

where `[project_code]` is the project code, for example:

```bash
#SBATCH -A uppmax2023-2-25
```

???- question "Forgot your Rackham project?"

    One can go to the SUPR NAISS pages to see one's projects,

    ![Example of the Rackham project called 'UPPMAX 2023/2-25'](./img/naiss_supr_project_2023_2_25.png)

    > Example of the Rackham project called 'UPPMAX 2023/2-25'

    On the SUPR NAISS pages, projects are called 'UPPMAX [year]/[month]-[day]',
    for example, 'UPPMAX 2023/2-25'.
    The UPPMAX project name, as to be used on Rackham,
    has a slightly different name:
    the account name to use on Rackham is `uppmax[year]-[month]-[day]`,
    for example, `uppmax2023-2-25`

A full example script would be:

```bash
#!/bin/bash
#SBATCH -A uppmax2023-2-25
echo "Hello"
```

### SMT

The compute node CPUs have Simultaneous multithreading (SMT)
enabled. Each CPU core runs two Threads. In Slurm the Threads are
referred to as CPUs.

Different jobs are never allocated to the same CPU core. The smallest
possible job always gets one Core with two Threads (CPUs).

Jobs requesting multiple tasks or cpus gets threads by default.

Some examples:

- `--ntasks=2` - one core, two threads
- `--ntasks=1 --cpus-per-task=4` - two cores, four threads
- `--ntasks=2 --cpus-per-task=3` - three cores, six threads.

#### One thread per core to avoid SMT

If you suspect SMT degrades the performance of your jobs, you can you
can specify `--threads-per-core=1` in your job.

Same examples as before but with `--threads-per-core=1`:

- `--ntasks=2 --threads-per-core=1` - two cores, (4 threads, 2 used)
- `--ntasks=1 --cpus-per-task=4 --threads-per-core=1` - 4 cores (8 threads, 4 unused)
- `--ntasks=2 --cpus-per-task=3 --threads-per-core=1` - 6 cores (12 threads, 6 unused)

When doing this you should launch your tasks using `srun` to ensure
your processes gets pinned to the correct CPUs (threads), one per
core.

Again, what is shown here is a minimal use of [`sbatch`](../software/sbatch.md).

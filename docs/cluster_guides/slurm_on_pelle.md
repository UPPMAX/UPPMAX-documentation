# Using Slurm on Pelle

This page describes how to use Slurm on Pelle.

???- question "What is Slurm?"

    See [the general page about Slurm](slurm.md)

???- question "What is Pelle?"

    See [the general page about Pelle](pelle.md)

See [Slurm troubleshooting](slurm_troubleshooting.md)
how to fix Slurm errors.


!!! warning

    Work in progress. Updating Racckham instructions to Pelle ones.

## `sbatch` (and `interactive`) on Pelle

`sbatch` (and `interactive`) work the same as on other clusters,
the only difference is that one need specify one want to use
the Rackham computer nodes.

???- question "Want to start an interactive session?"

    See [how to start an interactive session on Pelle](start_interactive_session_on_rackham.md)

Here it is shown how to submit a job with:

- command-line Slurm parameters
- Slurm parameters in the script

## Partitions on Pelle

Partition flag is either ``--partition`` or ``-p``

Partition name|Description
--------------|----------------------------------
`pelle`       | (Default) Use one or more CPU cores
`fat`         | Use a fat node with 2 or 3 TB memory, see below
`gpu`         | GPU node, 2 types see below

### The `pelle` partition

The `pelle` partition is default so you can omitt specifying ``-p`` or ``--partition``

Its allocates an ordinary CPU node (allows one to use one or more cores, up to 96 cores).

Here is the minimal use for one core:

```bash
sbatch -A [project_code] --partition core [script_filename]
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

### The `fat` partition

With the ``fat`` partition you reach compute nodes with more memory.
There are at the moment just one 2 TB node and one 3 TB node.

- To allocate 2 TB: ``-p fat -C 2TB``

    - Example: ``interactive -A staff -t 1:0:0 -p fat -C 2TB``

- To allocate 3 TB: ``-p fat -C 3TB``

    - Example: ``interactive -A staff -t 1:0:0 -p fat -C 3TB``

### The `gpu` partition

With the ``gpu`` partition you reach the nodes with GPUs.

There are two kinds of GPUs at the moment. 

- 4 of the lighter type ``L40s``, enough for most problems. Each node has 10 (!) GPUs. Most often just one GPU is needed, so remember to state that you need just 1, see below.
- 2 of the large type ``H100``, which can be suitable for large training runs. Each node has 2 GPUs. Most often just one GPU is needed, so remember to state that you need just 1, see below.

Therefore, at first hand, allocate the default ``L40s`` and one of them

- To allocate L40s: ``-p gpu --gres=gpu:<number of gpus>`` or ``-p gpu --gpus:l40s:number of gpus>``

    - Example with 1 gpu: ``interactive -A staff -t 1:0:0 -p gpu --gres=gpu:1``
    - Example with 11 gpus: ``interactive -A staff -t 1:0:0 -p gpu --gres=gpu:11`` will fail because there are just 10 gpus on one node!

- To allocate H100: ``-p gpu --gpus:h100:number of gpus>``

    - Example with 1 gpu: ``interactive -A staff -t 1:0:0 -p gpu --gpus=h100:1`
    - Example with 3 gpu: ``interactive -A staff -t 1:0:0 -p gpu --gpus=h100:3` will fail because there are just 2 gpus on one node!

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

Again, what is shown here is a minimal use of [`sbatch`](../software/sbatch.md).

## 


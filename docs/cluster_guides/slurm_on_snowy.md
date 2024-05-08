# Using Slurm on Snowy

This page describes how to use Slurm on Snowy.

???- question "What is Slurm?"

    See the general page on Slurm [here](slurm.md)

???- question "What is Snowy?"

    See the general page on Snowy [here](snowy.md)

See [Slurm troubleshooting](slurm_troubleshooting.md)
how to fix Slurm errors.

## `sbatch` (and `interactive`) on Snowy

`sbatch` (and `interactive`) work the same as on other clusters,
the only difference is that one need specify one want to use
the Snowy computer nodes.

???- question "Want to start an interactive job?"

    See how to start an interactive job on Snowy [here](start_interactive_job_on_snowy.md)

Here it is shown how to submit a job with:

- command-line Slurm parameters
- Slurm parameters in the script

## `sbatch` a script with command-line Slurm parameters

The minimal command to use `sbatch` with command-line Slurm parameters is:

``` bash
sbatch -A [project_code] -M snowy [script_filename]
```

where `[project_code]` is the project code, and `[script_filename]`
the name of a bash script, for example:

``` bash
sbatch -A uppmax2023-2-25 -M snowy my_script.sh
```

???- question "Forgot your Snowy project?"

    One can go to the SUPR NAISS pages to see one's projects,

    ![](./img/naiss_supr_project_2023_2_25.png)

    > Example of the Snowy project called 'UPPMAX 2023/2-25'

    On the SUPR NAISS pages, projects are called 'UPPMAX [year]/[month]-[day]',
    for example, 'UPPMAX 2023/2-25'.
    The UPPMAX project name, as to be used on Snowy,
    has a slightly different name:
    the account name to use on Snowy is `uppmax[year]-[month]-[day]`,
    for example, `uppmax2023-2-25`

???- question "What is in the script file?"

    The script file `my_script.sh` is a minimal example script.
    Such a minimal example script could be:

    ```bash
    #!/bin/bash
    echo "Hello"
    ```

Again, what is shown here is a minimal use of `sbatch`.
See the general page on Slurm [here](slurm.md).

## `sbatch` a script with Slurm parameters in script

The minimal command to use `sbatch` with Slurm parameters in the script:

``` bash
sbatch [script_filename]
```

where `[script_filename]` the name of a bash script, for example:

``` bash
sbatch my_script.sh
```

The script must contain at least the following lines:

```
#SBATCH -A [project_code]
#SBATCH -M snowy
```

where `[project_code]` is the project code, for example:

```bash
#SBATCH -A uppmax2023-2-25
#SBATCH -M snowy
```

???- question "Forgot your Snowy project?"

    One can go to the SUPR NAISS pages to see one's projects,

    ![](./img/naiss_supr_project_2023_2_25.png)

    > Example of the Snowy project called 'UPPMAX 2023/2-25'

    On the SUPR NAISS pages, projects are called 'UPPMAX [year]/[month]-[day]',
    for example, 'UPPMAX 2023/2-25'.
    The UPPMAX project name, as to be used on Snowy,
    has a slightly different name:
    the account name to use on Snowy is `uppmax[year]-[month]-[day]`,
    for example, `uppmax2023-2-25`

A full example script would be:

```bash
#!/bin/bash
#SBATCH -A uppmax2023-2-25
#SBATCH -M snowy
echo "Hello"
```

Again, what is shown here is a minimal use of `sbatch`.
See the general page on Slurm [here](slurm.md).

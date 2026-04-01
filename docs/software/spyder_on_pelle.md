---
tags:
  - Spyder
  - bundle
  - module
  - conda
  - Pelle
---

# Spyder on Pelle

![Jupyter on old cluster Rackham](./img/jupyter_rackham_thinlinc.png)

**FIX**

There are multiple [IDEs](../software/ides.md) on the UPPMAX clusters,
among other [Spyder](../software/jupyter.md).

Spyder is an [IDE](../software/ides.md) specialised for
[the Python programming language](../software/python.md).

## Procedure

### Principles

- start an interactive session
- load a Python or Spyder module
- load your Spyder environment
- start Spyder

### 1. Start a Pelle remote desktop environment

This can be either:

- [Login to the Pelle remote desktop environment using the website](../getting_started/login_pelle_remote_desktop_website.md)
- [Login to the Pelle remote desktop environment using a local ThinLinc client](../getting_started/login_pelle_remote_desktop_local_thinlinc_client.md)

### 2. Start an interactive session

Within the Pelle remote desktop environment, start a [terminal](../software/terminal.md).
Within that terminal,
[start an interactive session](../cluster_guides/start_interactive_session_on_pelle.md):

```bash
interactive -A [project_number] -t 8:00:00
```

Where `[project_number]` is your
[UPPMAX project](../getting_started/project.md), for example:

```bash
interactive -A uppmax2025-2-393 -t 8:00:00
```

???- question "What is my UPPMAX project number?"

    See [the UPPMAX documentation on how to see your UPPMAX projects](../getting_started/project.md)

### 3a. Use software modules to provide Python, Spyder and python packages needed

- Step 1. Decide what is needed in terms of

    - Python version (so far we have Spyder installed for the foss2023b tool chain)
    - Python packages (and versions)

- Step 2: Check our [Python Bundles page](python_bundles.md) and choose compatible modules.

    - Check if your needed python packages are compatible with a Spyder module.
    - If not you may need to go to 3b instead to create a isolated environment in Conda.

#### Example with compatible  versions on Pelle

- Within the terminal of the interactive session,
load the ``Spyder`` module compatible with the ``foss2023b`` toolchain (``GCCcore-13.2.0``).
- You get ``Python/3.11.5`` on the fly.
- Also load ``SciPy-bundle`` to get ``numpy`` and ``pandas``
- and ``matplotlib`` that is its own module.
- (You can add any other compatible python package module as well)

```bash
ml Spyder/6.0.1-GCCcore-13.2.0
ml SciPy-bundle/2023.11-gfbf-2023b
ml matplotlib/3.8.2-gfbf-2023b
```

???- question "Forgot what the module system is?"

    See [the UPPMAX pages on the module system](../cluster_guides/modules.md).

### 3b Create a conda environment and activate it

First time: 

``` bash
ml Miniforge3/24.11.3-0
export CONDA_PKG_DIRS=/proj/<project>
export CONDA_ENVS_PATH=/proj/<project>
conda create --prefix $CONDA_ENVS_PATH/spyder-env python=3.12 spyder -c conda-forge
source activate spyder-env
# A prompt "(/path-to/spyder-env/)" should show up
# double-check we are using python from the Conda environment!
which python  # should point to the conda environment!
python -V     # should give python version 3.12.X
```

Add some packages that you want

Example

``` bash
conda install pandas scipy matplotlib seaborn
```

Activating Spyder

``` bash
ml Miniforge3/24.11.3-0
export CONDA_PKG_DIRS=/proj/<project>
export CONDA_ENVS_PATH=/proj/<project>
source activate spyder-env
```

### 4. Start the Spyder notebook

Still within the terminal of the interactive session,
start a Spyder session like this:

``` bash
spyder &
```

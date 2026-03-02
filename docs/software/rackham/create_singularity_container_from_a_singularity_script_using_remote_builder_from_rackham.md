---
tags:
  - Singularity
  - Singularity script
  - create
  - build
  - remote builder
  - Rackham
---

# Create a Singularity container from a Singularity script using a remote build from Rackham

There are multiple ways how to [create a Singularity container](create_singularity_container.md).

This page shows how to do so using a remote build from Rackham.

## Building images on Rackham

On Rackham, the singularity capabilities are instead provided by [Apptainer](https://apptainer.org/). The differences are beyond the scope of this material, but you can safely assume you are working with Singularity. Apptainer, also allows you to build containers without sudo/administrative rights. In most of the cases, you can simply start building directly without sudo i.e. `singularity build myimage.img examples/ubuntu.def`. Here are some precautions that will allow you to safely build images on Rackham.

```bash
# Change to fit your account
PRJ_DIR=/crex/uppmax2022-0-00

# Singularity
export SINGULARITY_CACHEDIR=${PRJ_DIR}/nobackup/SINGULARITY_CACHEDIR
export SINGULARITY_TMPDIR=${PRJ_DIR}/nobackup/SINGULARITY_TMPDIR
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# Apptainer
export APPTAINER_CACHEDIR=${PRJ_DIR}/nobackup/SINGULARITY_CACHEDIR
export APPTAINER_TMPDIR=${PRJ_DIR}/nobackup/SINGULARITY_TMPDIR
mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR

# Disabling cache completelly - perfect when you only need to pull containers
# export SINGULARITY_DISABLE_CACHE=true
# export APPTAINER_DISABLE_CACHE=true
```

## Procedure

The remote builder service provided by Sylabs also supports remote builds through an API. This means you can call on it from the shell at UPPMAX.

Using this service also requires you to register/log in to the Sylabs cloud service. To use this, simply run

```bash
singularity remote login SylabsCloud
```

and you should see

```console
Generate an API Key at https://cloud.sylabs.io/auth/tokens, and paste here:
API Key:
```

if you visit that link and give a name, a text-token will be created for you. Copy and paste this to the prompt at UPPMAX. You should see

```console
INFO: API Key Verified!
```

once you've done this, you can go on and build images almost as normal, using commands like

```bash
singularity build --remote testcontainer.sif testdefinition.def
```

which will build the container from `testdefinition.def` remotely and transfer it to your directory, storing it as `testcontainer.sif`.

???- question "Could you give an example script?"

    A sample job script for running a tool provided in a container may look like

    ```slurm
    #!/bin/bash -l
    #SBATCH -N 1
    #SBATCH -n 1
    #SBATCH -t 0:30:00
    #SBATCH -A your-project
    #SBATCH -p core
    cd /proj/something/containers

    singularity exec ./ubuntu.img echo "Hey, I'm running ubuntu"
    singularity exec ./ubuntu.img lsb_release -a
    singularity run ./anotherimage some parameters here
    ./yetanotherimage parameters
    ```

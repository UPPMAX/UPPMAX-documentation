# Singularity User Guide

Singularity [www.sylabs.io/docs](https://www.sylabs.io/docs) provide tools for running containers that are more suitable to traditional HPC environments when some other tools such as Docker or lxc. These containers can be portable and could be run both on your desktop machine and our clusters.

One of the ways in which Singularity is more suitable for HPC is that it very actively restricts permissions so that you do not gain access to additional resources while inside the container. One consequence of this is that some common tools like ping or sudo do not work when run within a container (as a regular user).

Singularity is installed and usable to run custom container images on the clusters bianca and rackham.

## Running an existing image

It's possible to download and run pre-built images from the Singularity hub [https://singularity-hub.org](https://singularity-hub.org) and the singularity library ([https://cloud.sylabs.io](https://cloud.sylabs.io)  library) using the singularity pull sub command such as:

```bash
singularity pull library://ubuntu
```

Which will download the requested image and place it in the current directory. You can also upload and run image directly your self.

Once you have an image, you can "run" it with a command such as

```bash
singularity run singularityhub-ubuntu-14.04.img
```

which will try to execute a "run" target in the container. There are also the shell and exec subcommands for starting a shell and running a specific command respectively.

## Access to UPPMAX file systems

By default, singularity will try to help and map the UPPMAX file systems from the current cluster so that they can be accessed from within the container. For CentOS7 based clusters (snowy, rackham, bianca), this works as expected.

Singularity is installed on the system (on each separate node) and does not require any module load to be available.

It's possible to run Docker containers. You can try to run

```bash
singularity shell docker://debian:stretch
```

but note that Docker containers are typically designed to run with more privileges than are allowed with Singularity, so it's quite possible things do not work as expected.

## Not all images may work everywhere

Images run with the same linux kernel as the rest of the system. For HPC we systems, the kernel used tend to be quite old for stability reasons. This is not normally a problem, but can cause issues if the libraries of the images you try to run expects functionality added in newer kernels. How and what works is difficult to know without trying, but we have successfully started a shell in an image for the currently most recent Ubuntu release (17.04).

## Creating your own images

One can create a Singularity container from a Singularity script on a computer with Linux where you have super-user rights.
See [create a Singularity container from a Singularity script on a computer with Linux where you have super-user rights](create_singularity_container_from_a_singularity_script_on_linux.md)
how to do so.

Creating images directly on UPPMAX is not possible as it requires
administrator (root) privileges,
but it can be done [using the Sylabs cloud remote builder from the UPPMAX shell](#using-the-sylabs-cloud-remote-builder-from-the-uppmax-shell).

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

## Using the Sylabs cloud remote builder

From a Singularity script on can create a Singularity container
using a website, see [creating a Singularity container from a Singularity script using the Sylabs cloud remote builder](create_singularity_container_from_a_singularity_script_using_remote_builder.md).

After having done so, we can also run the created image without pulling it
explicitly, for example:

```bash
singularity run library://pontus/default/sortmerna:3.0.3
```

???- question "How does that look like?"

    Output will look similar to this:

    ```bash
    $ singularity run library://pontus/default/sortmerna:3.0.3
    WARNING: Authentication token file not found : Only pulls of public images will succeed

      Program:      SortMeRNA version 3.0.3
      Copyright:    2016-2019 Clarity Genomics BVBA:
                    Turnhoutseweg 30, 2340 Beerse, Belgium
                    2014-2016 Knight Lab:
                    Department of Pediatrics, UCSD, La Jolla
                    2012-2014 Bonsai Bioinformatics Research Group:
                    LIFL, University Lille 1, CNRS UMR 8022, INRIA Nord-Europe
      Disclaimer:   SortMeRNA comes with ABSOLUTELY NO WARRANTY; without even the
                    implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
                    See the GNU Lesser General Public License for more details.
      Contributors: Jenya Kopylova   jenya.kopylov@gmail.com
                    Laurent Noé      laurent.noe@lifl.fr
                    Pierre Pericard  pierre.pericard@lifl.fr
                    Daniel McDonald  wasade@gmail.com
                    Mikaël Salson    mikael.salson@lifl.fr
                    Hélène Touzet    helene.touzet@lifl.fr
                    Rob Knight       robknight@ucsd.edu

      For help or more information on usage, type `./sortmerna -h'
    ```

## Using the Sylabs cloud remote builder from the UPPMAX shell

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

## Examples

### Building a container from conda

To build a container from a conda environment, see [create a Singularity container from conda](create_singularity_container_from_conda.md)
how to do so.

### Building a container with an R package from GitHub

Although the `R_Packages` [module](../cluster_guides/modules.md)
has thousands of packages, sometimes you need a package from GitHub.

See [create a Singularity container for an R package](create_singularity_container_for_r_package.md)
how to do so.

### Building a container from DockerHub

If there is a Docker script on DockerHub,
it can be put into a Singularity container as described [here](create_singularity_container_from_dockerhub.md)
how to do so.

### Building a container from a `docker pull`

If the documentation of what you need mentions a `docker pull` to install it,
it can be put into a Singularity container as described [here](create_singularity_container_from_docker_pull.md)
how to do so.

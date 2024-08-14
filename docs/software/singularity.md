# Singularity User Guide

Singularity [www.sylabs.io/docs](https://www.sylabs.io/docs) provide tools for running containers that are more suitable to traditional HPC environments when some other tools such as Docker or lxc. These containers can be portable and could be run both on your desktop machine and our clusters.

One of the ways in which Singularity is more suitable for HPC is that it very actively restricts permissions so that you do not gain access to additional resources while inside the container. One consequence of this is that some common tools like ping or sudo do not work when run within a container (as a regular user).

Singularity is installed and usable to run custom container images on the clusters bianca and rackham.

## Pulling an existing Singularity image

It's possible to download and run pre-built images from the Singularity 
hub [https://singularity-hub.org](https://singularity-hub.org)
and the Singularity library ([https://cloud.sylabs.io](https://cloud.sylabs.io))
using the singularity pull sub command such as:

```bash
singularity pull library://ubuntu
```

Which will download the requested image and place it in the current directory.
You can also upload and run the image directly yourself.

## Creating a Singularity container

See [creating a Singularity container](create_singularity_container.md) for the multiple ways how to build a Singularity container.

### Examples

- [Create a Singularity container from conda](create_singularity_container_from_conda.md)
- [Create a Singularity container for an R package](create_singularity_container_for_r_package.md)
- [Create a Singularity container from DockerHub](create_singularity_container_from_dockerhub.md)
- [Create a Singularity container from a `docker pull`](create_singularity_container_from_docker_pull.md)

## Running an existing image

Once you have an image, you can "run" it with a command such as

```bash
singularity run singularityhub-ubuntu-14.04.img
```

which will try to execute a "run" target in the container.
There are also the `shell` and `exec` subcommands for starting a shell
and running a specific command respectively.

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


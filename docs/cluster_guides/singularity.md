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

## Access to UPPMAX file systems.
By default, singularity will try to help and map the UPPMAX file systems from the current cluster so that they can be accessed from within the container. For CentOS7 based clusters (snowy, rackham, bianca), this works as expected.

Singularity is installed on the system (on each separate node) and does not require any module load to be available.

It's possible to run Docker containers. You can try to run

```bash
singularity shell docker://debian:stretch
```

but note that Docker containers are typically designed to run with more privileges than are allowed with Singularity, so it's quite possible things do not work as expected.

## Not all images may work everywhere!
Images run with the same linux kernel as the rest of the system. For HPC we systems, the kernel used tend to be quite old for stability reasons (with milou using very old kernels). This is not normally a problem, but can cause issues if the libraries of the images you try to run expects functionality added in newer kernels. How and what works is difficult to know without trying, but we have successfully started a shell in an image for the currently most recent Ubuntu release (17.04).

## Creating your own images
If you have singularity on your own machine, you can create your own images and upload and run them from UPPMAX. Creating images directly on UPPMAX is not possible as it requires administrator (root) privileges (but see below).

Singularity provides functionality to create and bootstrap images, and the installation contains example definitions for bootstrapping various images you can use as a start (like Ubuntu, Scientific Linux and so on). If you normally run Linux and have administrative access, you can install Singularity and build images locally, typical usage would be:

```bash
sudo singularity build myimage.img examples/ubuntu.def
```
Look for more examples on the [UPPMAX Singularity workshop](https://pmitev.github.io/UPPMAX-Singularity-workshop/) page - "Case Studies" section.


## Building images on Rackham.

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

## Using the sylabs cloud remote builder, an example
Even if you don't run Linux on your desktop system, you can still build your own images. Typically software pages contain enough information as installation instructions to create a modified recipe to build images for software.

[Sylabs](https://www.sylabs.io/) (the company currently developing singularity) offer an experimental cloud service for building images from recipes. Here's an example on how to use that to build an image for a software (for this example, we picked [sortmerna](https://github.com/biocore/sortmerna)  as it was the first user software request that came up).

- First, we need to sign in to the sylabs remote builder, available at https://cloud.sylabs.io. It allows sign in through various providers (currently Google, Microsoft, GitHub, GitLab). If you don't have an account with one of these, at least one of them is likely to offer free registration.

- Once signed in, we want to create a project for this software, so we click on "Singularity Library" in the top menu and select "Create a new project", set ourselves as owner and enter sortmerna as project name. We also select to make images for this project public.

- Once we click onward, we can create our first image for the project. This can be done either by pushing an image from a client (commands are given) or by building in the cloud service.

- Since we want to use the cloud service, we click remote builder and get a box to fill in an image recipe. We also get a box to enter a tag or version and the possibility to enter a description.

- As we'll create an image for the currently latest release version (3.0.3), we enter 3.0.3 in the  tag field.

- Finally, we need to provide a recipe for the image, since this is not our first rodeo, we know roughly how it should look.

```singularity
BootStrap: library
From: ubuntu:18.04

%runscript
  sortmerna "$@"

%post
  echo "Hello from inside the container"
  apt-get update
  apt-get -y dist-upgrade
  apt-get clean
  apt-get -y install curl
  curl -L https://github.com/biocore/sortmerna/releases/download/v3.0.3/sortmerna-3.0.3-Linux_C6.sh > /tmp/sortmerna.sh 
  bash /tmp/sortmerna.sh --skip-license
```

- We paste that recipe in the box (or upload a file with it) and click build. The service will try to find an available builder and It will work for a while. Output from the build process will be displayed in a console window on the same page.

- Hopefully the build completes successfully (a notification is shown and build status is updated). We can when go to the the projects through the drop-down with our user name in the upper right corner, select "My projects", select the sortmerna project.

- Once on the project view, we select the tab "Images" to see what images we have built. We see that we have an image tagged 3.0.3 and are given the option to download the image file through the web browser as well as commands to let singularity pull it.

- As it's a hassle to transfer the image from our desktop, we just copy the command to pull the image and run it.

```bash
$ singularity pull library://pontus/default/sortmerna:3.0.3
WARNING: Authentication token file not found : Only pulls of public images will succeed
INFO:    Downloading library image
 65.02 MiB / 65.02 MiB [=========================================================================================================================================] 100.00% 30.61 MiB/s 2s

```

which downloads the image and creates sortmerna_3.0.3.sif for us. We can then run that just as sortmerna.

```bash
$ ./sortmerna_3.0.3.sif 

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

We can also transfer the file to another system (e.g. move it to bianca where it can be pulled directly).

Just like with the docker example, we can also run the image without pulling it explicitly.

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

If we wanted to install [multiqc](https://github.com/ewels/MultiQC) instead, we only change the recipe to

```singularity
BootStrap: library
From: ubuntu:18.04

%runscript
  multiqc "$@"

%post
  echo "Hello from inside the container"
  apt-get update
  apt-get -y dist-upgrade
  apt-get clean
  apt-get -y install python-pip
  pip install multiqc
```

## Using the sylabs cloud remote builder from the UPPMAX shell
The remote builder service provided by sylabs also supports remote builds through an API. This means you can call on it from the shell at UPPMAX.

Using this service also requires you to register/log in to the Sylabs cloud service. To use this, simply run
```bash
singularity remote login SylabsCloud
```
and you should see
```
Generate an API Key at https://cloud.sylabs.io/auth/tokens, and paste here:
API Key:
```

if you visit that link and give a name, a text-token will be created for you. Copy and paste this to the prompt at UPPMAX. You should see
```
INFO: API Key Verified!
```
once you've done this, you can go on and build images almost as normal, using commands like 
```bash
singularity build --remote testcontainer.sif testdefinition.def
```
which will build the container from testdefinition.def remotely and transfer it to your directory, storing it as testcontainer.sif

Running your container in jobs
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

## Another example; building a container from conda
To build a container from a conda environment, here we demonstrate for `qiime2`

```singularity
BootStrap: library
From: centos:7

%runscript
  . /miniconda/etc/profile.d/conda.sh
  PATH=$PATH:/miniconda/bin
  conda activate qiime2-2019.7
  qiime "$@"

%post
  yum clean all
  yum -y update
  yum -y install wget python-devel
  cd /tmp
  wget https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh
  bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /miniconda
  /miniconda/bin/conda update -y conda
  wget https://data.qiime2.org/distro/core/qiime2-2019.7-py36-linux-conda.yml
  /miniconda/bin/conda env create -n qiime2-2019.7 --file qiime2-2019.7-py36-linux-conda.yml
  # OPTIONAL CLEANUP
  rm qiime2-2019.7-py36-linux-conda.yml
  /miniconda/bin/conda clean -a
```
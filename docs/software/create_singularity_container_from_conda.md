# Create a Singularity container from conda

There are multiple ways how to [create a Singularity container](singularity.md).

This page shows how to create a Singularity container from a Singularity
script that uses [conda](conda.md).

As an example we use a script that build [qiime2](qiime2.md):

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

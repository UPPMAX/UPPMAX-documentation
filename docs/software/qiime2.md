# qiime2

qiime2 is a tool.

qiime2 can be found among [the UPPMAX modules](../cluster_guides/modules.md).

```bash
module spider qiime2
```

???- question "How does that look like?"

    You output will look similar to this:

    ```bash
    [sven@rackham3 ~]$ module spider qiime2

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      qiime2:
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Versions:
            qiime2/2018.11.0
            qiime2/2024.2

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      For detailed information about a specific "qiime2" package (including how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modules.
      For example:

         $ module spider qiime2/2024.2
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    ```

To find out how to load a specific version:

```bash
module spider qiime2/1.22.2
```

???- question "How does that look like?"

    Output will look similar to:

    ```bash
    [sven@rackham3 ~]$ module spider qiime2/2024.2

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    qiime2: qiime2/2024.2
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        You will need to load all module(s) on any one of the lines below before the "qiime2/2024.2" module is available to load.

          bioinfo-tools

        Help:
          qiime2 - use qiime2

          Description

          Version 2024.2

          https://qiime2.org

          The version installed is 2024.2 amplicon, slightly modified from the publicly available docker image.


             qiime ...


          You may see a message like

              Matplotlib created a temporary config/cache directory at /scratch/matplotlib-a10b2an0 because the default path (/home/qiime2/matplotlib) is not a writable directory...

          This is because qiime2 is running within an Apptainer container. This message can be ignored.

    ```

After reading that documentation, we know how to load it:

```bash
module load bioinfo-tools
module load qiime2/2024.2
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham3 ~]$ module load bioinfo-tools
    [sven@rackham3 ~]$ module load qiime2/2024.2
    [sven@rackham3 ~]$
    ```

## Singularity script

If you want to put qiime2 in a [Singularity](singularity.md) container,
here is an example script:

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

See [the documentation on Singularity](singularity.md)
how to do so.

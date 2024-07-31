# Conda

???- question "Want to see the video 'How to use Conda on Rackham'?"

    If you want to see a video how to use Conda on Rackham,
    go [here](https://youtu.be/SMhawXQhtls?si=_2t6T2Vn2B10M6LW)

## Install packages or not? Check it

### Python

- Check python versions: ``ml avail python``
- load a python version like: ``ml python/3.10.8``
- from the Python shell with the ``import`` command
- from BASH shell with the

- `pip list` command
- `module help python/3.9.5` (or other version) at UPPMAX

### Is it not there, or is it a stand-alone tool? Then proceed!**

!!! info "Tip Python packages"

    - Try Conda first directly on Bianca.
    - Otherwise, on **Rackham**, in first case use **Pip**.
    - We have mirrored all _major_ Conda repositories directly on UPPMAX, on both Rackham and Bianca. These are updated every third day.
    - If you want to keep number of files down, use PyPI (pip).

## Python packages with pip

???- question "Want to see the video 'Load and use Python packages on UPPMAX'?"

    If you want to see a video how to load and use Python packages
    on the UPPMAX (and HPC2N) HPC clusters,
    go [here](https://youtu.be/novRJfAa2QA?si=IQM3g37TsimemDl6)

See the [Python user guide](https://uppmax.github.io/UPPMAX-documentation/software/python/)

## Conda repositories

We have mirrored all major Conda repositories directly on UPPMAX, on both Rackham and Bianca. These are updated every third day.

!!! info "Available Conda channels"

    - bioconda
    - biocore
    - conda-forge
    - dranew
    - free
    - main
    - pro
    - qiime2
    - r
    - r2018.11
    - scilifelab-lts
    - nvidia
    - pytorch

!!! info "More info"

    - [Installing Conda packages on Bianca](https://uppmax.github.io/bianca_workshop/extra/conda/)

## Using Conda

!!! info "Conda cheat sheet"

    - List all environments: `conda info -e` or `conda env list`

    - Create a conda environment (it is good to directly define the packages included AND channels do not need to be explicitly mentioned)

        ```bash
        conda create --prefix /some/path/to/env <package1> [<package2> ... ]
        ```

        - On our systems the above should replace `conda create --name myenvironment ...`

    - Create a new environment from requirements.txt:

        - `conda create --prefix /some/path/to/env --file requirements.txt`

    - Activate a specific environment: `conda activate myenvironment`

    - List packages in present environment: `conda list`

        - Also pip list will work

    - Install additional package from an active environment:

        - `conda install somepackage`

    - Install from certain channel (conda-forge):

        - `conda install -c conda-forge somepackage`

    - Install a specific version: `conda install somepackage=1.2.3`

        - Install a specific version: `conda install somepackage=1.2.3`

    - Deactivate current environment: `conda deactivate`

    - [More](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Your conda settings on Rackham and Bianca

- ```export CONDA_ENVS_PATH=/a/path/to/a/place/in/your/project/```

!!! tip

    - You may want to have the same path for all conda environments in the present project
    - ``echo "export CONDA_ENVS_PATH=/a/path/to/a/place/in/your/project/" >> ~/.bashrc``
        - Example: ``echo "export CONDA_ENVS_PATH=/proj/<project>/conda" >> ~/.bashrc``

!!! warning

    - It seems you are required to use this path, ending with the name of your environment, together with ``--prefix`` when you install new envronments AND packages also after activating the conda environment!
      Like: ``conda install --prefix $CONDA_ENVS_PATH/<your-environment> ...``

!!! tip

    - REMEMBER TO `conda clean -a` once in a while to remove unused and unnecessary files

??? info "By choice"

    - Run `source conda_init.sh` to initialise your shell (bash) to be able to run `conda activate` and `conda deactivate` etcetera instead of `source activate`. It will modify (append) your `.bashrc` file.

    - When conda is loaded you will by default be in the ``base`` environment, which works in the same way as other Conda environments. It is a “best practice” to avoid installing additional packages into your base software environment unless it is very general packages

## Installing using Conda

We have mirrored all major Conda repositories directly on UPPMAX, on
both Rackham and Bianca. These are updated every third day. See above for these conda channels.

- You reach them all by loading the ``conda`` module.
- You don't have to state the specific channel when using UPPMAX.
- Also, you are offline on Bianca which means that the default is `--offline`, which you can specify if you want to simulate the experience on Rackham.

!!! tip

    If you need a channel that isn't in our repository, we can easily add it. Just send us a message and we will do it.

## Make a new conda environment

!!! tip

    - Since python or other packages are dependent on each-other expect solving the versions takes some time.
    - use an interactive session!

1. ```bash
   module load conda
   ```

   - This grants you access to the latest version of Conda and all major repositories on all UPPMAX systems.
   - Check the text output as ``conda`` is loaded, especially the first time, see below


1. Create the Conda environment

    - Example:
    
        ```bash
        conda create --prefix  $CONDA_ENVS_PATH/python36-env python=3.6 numpy=1.13.1 matplotlib=2.2.2
        ```

    !!! info "The `mamba` alternative is not needed in newer versions of Conda!

    - It all worked if you get something like this:

        ```bash
        # To activate this environment, use
        #
        #     $ conda activate python36-env
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
        ```

1. Activate the conda environment by `source activate` if you have not enabled ``conda activate``, see above:

   ```bash
   source activate python36-env
   ```

   - You will see that your prompt is changing to start with `(python-36-env)` to show that you are within an environment.

   - You can also see the installed packages by:

   ```bash
   conda list
   pip list
   ```

   - you can also add more packages within the environment by exact version (use `=`) or latest (?) compatible version:

   ```bash
   conda install --prefix   $CONDA_ENVS_PATH/python36-env pandas
   ```

   - that may have given you ``pandas=1.1.5`` which would be the newest version compatible with ``python3.6`` and ``numpy=1.13.1``

1. Now do your work!

1. Deactivate with ``conda deactivate`` (this will work in any case!)

   ```bash
   (python-36-env) $ conda deactivate
   ```

!!! warning

    - Conda is known to create _many small_ files.
      Your diskspace is not only limited in gigabytes,
      but also in number of files (typically 300000 in `$HOME`).
    - Check your disk usage and quota limit with `uquota`
    - Do a `conda clean -a` once in a while to remove unused and unnecessary files

## Working with Conda environments defined by files

- Create an environment based on dependencies given in an environment
  file:

        $ conda env create --file environment.yml

- Create file from present conda environment:

        $ conda env export > environment.yml

`environments.yml` (for conda) is a yaml-file which looks like this:

```yaml
name: my-environment
channels:        # not needed on bianca
- defaults
dependencies:
- numpy
- matplotlib
- pandas
- scipy
```

`environments.yml` with versions:

```yaml
name: my-environment
channels:            #not needed on bianca
- defaults
dependencies:
- python=3.7
- numpy=1.18.1
- matplotlib=3.1.3
- pandas=1.1.2
- scipy=1.6.2
```

!!! admonition "More on dependencies"

    - Dependency management from course [Python for Scientific computing](https://aaltoscicomp.github.io/python-for-scicomp/dependencies/)


!!! abstract "keypoints"

    - Conda is an installer of packages but also bigger toolkits

    - Conda on Bianca is easy since the repos in the most used channels are local.

    - Conda creates isolated environments not clashing with other installations of python and other versions of packages

    - Conda environment requires that you install all packages needed by yourself, although automatically.

    - That is, you cannot load the python module and use the packages therein inside your Conda environment.

## Conda in batch scripts

If you already have setup the CONDA_ENVS_PATH path and run 'conda init bash' a batch script containing a conda environment shall include

```bash
module load conda
conda activate <name of environment>
```

## Packages on Bianca

Since we have mirrored conda repositories locally conda will work also on Bianca!

First try Conda! There is a mirrored repository with many available packages.

If your desired package is not there but available as pip follow the guide below, perhaps , while looking at Bianca user guide  and Transit user guide.

Make an installation on Rackham and then use the wharf to copy it over to your directory on Bianca.

Path on Rackham and Bianca could be `~/.local/lib/python<version>/site-packages/`.

You may have to:

in source directory:

```bash
$ cp –a <package_dir> <wharf_mnt_path>
```

you may want to tar before copying to include all possible symbolic links:

```bash
$ tar cfz <tarfile.tar.gz> <package>
and in target directory (wharf_mnt) on Bianca:
$ tar xfz <tarfile.tar.gz> #if there is a tar file!
$ mv –a  <file(s)> ~/.local/lib/python<version>/site-packages/
```

If problems arise, send an email to `support@uppmax.uu.se` and we'll help you.

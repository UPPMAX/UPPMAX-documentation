# WRF user guide

## Introduction

- The Weather Research and Forecasting (WRF) Model is a next-generation mesoscale numerical weather prediction system designed to serve both operational forecasting and atmospheric research needs.

- [Model home page](https://www.mmm.ucar.edu/models/wrf)

- [ARW branch page](https://www2.mmm.ucar.edu/wrf/users/)

- WRF Preprocessing System (WPS). The Weather Research and Forecasting (WRF) Model is a next-generation mesoscale numerical weather prediction system designed to serve both operational forecasting and atmospheric research needs.

- WRF is installed as modules for version 4.1.3 and compiled with INTEL and parallelized for distributed memory (dmpar) or hybrid shared and distributed memory (sm+dm). These are available as:

    - WRF/4.1.3-dmpar     default as WRF/4.1.3
    - WRF/4.1.3-dm+sm
- WPS is installed as version 4.1 and available as:

    - WPS/4.1

- There are WPS_GEOG data available.
- Set the path in `namelist.wps` to:

```bash
geog_data_path = '/sw/data/WPS-geog/4/rackham/WPS_GEOG'
```

- Corine and metria data are included in the WPS_GEOG directory.
- In /sw/data/WPS-geog/4/rackham you'll find GEOGRID.TBL.ARW.corine_metria that hopefully works. Copy to your WPS/GEOGRID directory and then link to GEOGRID.TBL file.
- It may not work for a large domain. If so, either modify TBL file or use in inner domains only.

- To analyse the WRF output on the cluster you can use Vapor, NCL (module called as NCL-graphics) or wrf-python (module called as wrf-python). For details on how, please confer the web pages below:
    - [wrf-python](https://wrf-python.readthedocs.io/en/latest/),
    - [Vapor](https://www.vapor.ucar.edu/) or
    - [NCL](https://www.ncl.ucar.edu/Document/Pivot_to_Python/september_2019_update.shtml)
        - is not updated anymore and the developers recommend [GeoCAT](https://geocat.ucar.edu/) which serves as an umbrella over wrf-python, among others.

## Get started

- This section assumes that you are already familiar in running WRF. If not, please check the [tutorial](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/index.php), where you can at least omit the first 5 buttons and go directly to the last button, or depending on your needs, also check the “Static geography data” and “Real-time data”.

- When running WRF/WPS you would like your own settings for the model to run and not to interfere with other users. Therefore, you need to set up a local or project directory (e.g. 'WRF') and work from there like for a local installation. You also need some of the content from the central installation. Follow these steps:

1. Create a directory where you plan to have your input and result files.
1. Standing in this directory copy the all or some of the following directories from the central installation.
    1. Run directory                           for real runs

        - ``cp -r /sw/EasyBuild/rackham/software/WRF/4.1.3-intel-2019b-dmpar/WRF-4.1.3/run .``
        - You can remove *.exe files in this run directory because the module files shall be used.

    1. WPS directory                          if input data has to be prepared

        - ``cp -r /sw/EasyBuild/rackham/software/WPS/4.1-intel-2019b-dmpar/WPS-4.1 .``
        - You can remove *.exe files in the new directory because the module files shall be used.

    1. Test directory                          for ideal runs

        - ``cp -r /sw/EasyBuild/rackham/software/WRF/4.1.3-intel-2019b-dmpar/WRF-4.1.3/test .``
        - You can remove *.exe files because the module files shall be used.

1. When WRF or WPS modules are loaded you can run with “ungrib.exe” or for instance “wrf.exe”, i.e. without the “./”.
1. Normally you can run ungrib.exe, geogrid.exe and real.exe and, if not too long period, metgrid.exe, in the command line or in interactive mode.
1. wrf.exe has to be run on the compute nodes. Make a batch script, see template below:

```bash
#!/bin/bash
#SBATCH -J
#SBATCH --mail-user
#SBATCH --mail-type=ALL
#SBATCH -t 0-01:00:0
#set wall time c. 50% higher than expected
#SBATCH -A
#
#SBATCH -n 40 -p node
#this gives 40 cores on 2 nodes
module load WRF/4.1.3-dmpar
# With PMI jobs on very many nodes starts more efficiently.
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi2.so
export I_MPI_PMI2=yes
srun -n 40 --mpi=pmi2 wrf.exe
```

## Running smpar+dmpar

WRF compiled for Hybrid Shared + Distributed memory (OpenMP+MPI) can be more efficient than dmpar only. With good settings it runs approximately 30% faster and similarly less resources.

To load this module type:

```bash
module load WRF/4.1.3-dm+sm
```

The submit script can look like this:

```bash
#!/bin/bash -l
#SBATCH -J <jobname>
#SBATCH --mail-user <email address>
#SBATCH --mail-type=ALL
#SBATCH -t 0-01:00:0    #set wall time c. 50% higher than expected
#SBATCH -A <project name>
#
#SBATCH -N 2  ## case with 2 nodes = 40 cores on Rackham
#SBATCH -n 8  ## make sure that n x c = (cores per node) x N
#SBATCH -c 5
#SBATCH --exclusive
# We want to run OpenMP on one unit (the cores that share a memory channel, 10 on Rackham) or a part of it.
# So, for Rackham, choose -c to be either 10, 5 or 2.
# c = 5 seems to be the most efficient!
# Set flags below!
nt=1
if [ -n "$SLURM_CPUS_PER_TASK" ]; then
  nt=$SLURM_CPUS_PER_TASK
fi
ml purge > /dev/null 2>&1 # Clean the environment
ml WRF/4.1.3-dm+sm
export OMP_NUM_THREADS=$nt
export I_MPI_PIN_DOMAIN=omp
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi2.so
export I_MPI_PMI2=yes
srun -n 8 --mpi=pmi2 wrf.exe
```

## Local installation with module dependencies

If you would like to change in the FORTRAN code for physics or just want the latest version you can install locally but with the dependencies from the modules

### Step 1: WRF Source Code Registration and Download

1. [Register and download](https://www2.mmm.ucar.edu/wrf/users/download/get_source.html)
1. Identify download URLs you need (on Github for v4 and higher)

    1. WRF
    1. WPS
    1. Other?

1. In folder of your choice at UPPMAX:
    1. ``wget <download url>``
1. ``tar zxvf <file>``

### Step 2: Configure and compile

- Create and set the environment in a ``SOURCEME``  file, see example below for a intel-dmpar build.
- Loading module WRF sets most of the environment but some variables have different names in configure file.
- Examples below assumes dmpar, but can be interchanged to dm+sm for hybrid build.

```bash
#!/bin/bash

module load WRF/4.1.3-dmpar

module list

export WRF_EM_CORE=1

export WRFIO_NCD_LARGE_FILE_SUPPORT=1

export NETCDFPATH=$NETCDF

export HDF5PATH=$HDF5_DIR

export HDF5=$HDF5_DIR
```

- Then

```bash
source SOURCEME
./configure
```

- Choose intel and dmpar (15) or other, depending on WRF version and parallelization.
- When finished it may complain about not finding netcdf.inc file. This is solved below as you have to modify the configure.wrf file.

- Intelmpi settings (for dmpar)

```console
DM_FC           =        mpiifort

DM_CC           =        mpiicc -DMPI2_SUPPORT

#DM_FC           =       mpif90 -f90=$(SFC)

#DM_CC           =       mpicc -cc=$(SCC)
```

- NetCDF-fortran paths

```bash
LIB_EXTERNAL    = add  flags "-$(NETCDFFPATH)/lib -lnetcdff -lnetcdf"  (let line end with "\")
INCLUDE_MODULES =    add flag "-I$(NETCDFFPATH)/include" (let line end with "\")
Add the line below close to  NETCDFPATH:
NETCDFFPATH     =    $(NETCDFF)
```

Then:

```bash
./compile em_real
```

When you have made modification of the code and once configure.wrf is created, just

```bash
source SOURCEME
```

and run:

```bash
./compile em_real
```

## Running

Batch script should include:

```bash
module load WRF/4.1.3-dmpar

export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi2.so

export I_MPI_PMI2=yes

srun -n 40 --mpi=pmi2 ./wrf.exe     #Note ”./”, otherwise ”module version of wrf.exe” is used
```

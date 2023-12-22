# Short introduction to using R at UPPMAX

As of this writing, our most recent installations are

    R/4.3.1
    R_packages/4.3.1
    RStudio/2023.06.2-561
    If you need an older version, do module avail R or R_packages or RStudio to see older versions as well.

Note that R_packages/4.3.1 contains 23475 packages, nearly all packages available on CRAN and BioConductor, as well as several custom packages installed from Github and other repositories. See module help R_packages/4.3.1 and R_packages for more information.

Note that R_packages/4.3.1 loads R/4.3.1 as a prerequisite, so to get started with R and and have many installed modules available, simply do

     $ module load R_packages/4.3.1 
     $ R &

To use RStudio just add to loaded R_packages:

     $ module load RStudio/2022.07.1-554
     $ rstudio &

That will start an RStudio session with the latest R and R_packages.

All clusters also have a 'system' R and RStudio installed (version 3.6.0 and 1.1.423), so there is always R and Rscript available from the command line. We strongly recommend using R via the R_packages module though.

## How to install personal packages

First load R_packages to make sure that the package is not already installed!

To install personal packages in your own home directory you just type

    install.packages("package_name")

as usual. That will install all your packages under the path ~/R/[arch]/[version of R]/. Then you can load it by just doing "library(package_name)" or "require(package_name)" in the R environment.

You can also specify a specific folder for where to put your packages, with

    install.packages("package_name", lib="~/some/path/under/your/home/directory/")

But to then be able to find the package inside the R invironment you need to either export the R_LIBS_USER environment variable, or specify the flag "lib.loc" when calling require()/library(), e.g.

    library(package_name, lib.loc='~/some/path/under/your/home/directory')

Notice that if you are planning on running R on different clusters then it is probably wisest to manually specify the installation directory, and to have separate directories for each cluster. This is because some of the clusters have different architectures (e.g. milou and tintin), and this will render some packages unusable if you compile them on one system but try to run them on the other.

## How to use RStudio

There is a system installed version, available via the "rstudio" command (you will get RStudio/1.1.423). 

However, we recommend you to use a RStudio module.

- start a command line window
- ``module load R_packages/4.1.1``
- use 'module help R_packages/4.1.1' to see what is available in this certain version
- ``module load RStudio/1.4.1106``
- run 'rstudio &' from the command line, and wait
    - it might take 5-10 minutes for RStudio to start, but once it starts, there should be no further delays
- do *not* start RStudio through the graphical menu system, this will not have access to loaded modules

If you're going to run heavier computations within RStudio then you have to remember that you need to do it inside an interactive session on one of the computation nodes, and not on a login node. But if you mostly want to use it as a pretty code editor then you can run it on the login node as well. 

### RStudio on Bianca

When logging onto Bianca, you are placed on a login node, which has 1 CPU and a few GB of RAM. This is sufficient for doing some lightweight calculations, but interactive sessions and batch jobs provide access to much more resources and should be requested via the SLURM system.

Such is the case for using RStudio on Bianca. We recommend using at least two cores for this, and to get those resources, you must start an interactive job, for example,

```console
$ interactive -A <project> -n 2 -t hh:mm:sec
```
Once the interactive job has begun, load an RStudio module and an R_packages module and run "rstudio" from there. 

## What R packages are in the omnibus R_packages modules?

### R_PACKAGES/4.1.1
  As of 2021-11-11 there are a total of 21659 R packages installed. A total of 21740 packages are available in CRAN and BioConductor. 18022 CRAN packages are installed, out of 18348 available. 3382 BioConductor-specific packages are installed, out of 3392 available. 255 other R packages are installed. These are not in CRAN/BioConductor, and instead are hosted on github or elsewhere.

  These R packages are available as part of the R_packages/4.1.1 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/4.1.1 module.  When the R_packages/4.1.1 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

- To use some R packages from this module, other modules may need to be loaded. For example, to use the Rmpi package, the openmpi/3.1.5 module must be loaded after loading R_packages/4.0.4. 
- See module help R_packages/4.1.1 for more information.

### R_PACKAGES/4.0.4
  As of 2021-04-16 there are a total of 20663 CRAN and BioConductor packages installed, out of 20751 packages available. 17354 CRAN packages are installed, out of 17428 available. 3309 BioConductor-specific packages are installed, out of 3323 available.

  These R packages are available as part of the R_packages/4.0.4 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/4.0.4 module.  When the R_packages/4.0.4 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

- To use some R packages from this module, other modules may need to be loaded. For example, to use the Rmpi package, the openmpi/3.1.5 module must be loaded after loading R_packages/4.0.4.
- See module help R_packages/4.0.4 for more information.

### R_PACKAGES/4.0.0
  As of 2021-02-24 there are a total of 18652 CRAN and BioConductor packages installed, out of 20422 packages available. 14839 CRAN packages are installed, out of 17165 available. 3217 BioConductor-specific packages are installed, out of 3257 available.

  These R packages are available as part of the R_packages/4.0.0 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/4.0.0 module.  When the R_packages/4.0.0 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

See module help R_packages/4.0.0 for more information.

### R_PACKAGES/3.6.1
  As of 2019-09-18 there are a total of 17657 packages available in this module. This includes 14579 CRAN packages installed, out of 14913 available; and 3054 BioConductor-specific packages installed, out of 3079 available. These R packages are available as part of the R_packages/3.6.1 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/3.6.1 module.  When the R_packages/3.6.1 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

See module help R_packages/3.6.1 for more information.

### R_PACKAGES/3.6.0
  As of 2019-05-14 there are a total of 17257 packages available. This includes 13769 CRAN packages installed, out of 14178 available; and 3031 BioConductor-specific packages installed, out of 3079 available. These R packages are available as part of the R_packages/3.6.0 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/3.6.0 module.  When the R_packages/3.6.0 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

See module help R_packages/3.6.0 for more information.

### R_PACKAGES/3.5.2
  As of 2019-02-08 there are a total of 16642 packages available. This includes 13355 CRAN packages installed, out of 13683 available; and 2933 BioConductor-specific packages installed, out of 2959 available. These R packages are available as part of the R_packages/3.5.2 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/3.5.2 module.  When the R_packages/3.5.2 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

See module help R_packages/3.5.2 for more information.

### R_PACKAGES/3.5.0
With its 3.5.0 version, R_packages now attempts to install all available R packages from both CRAN and BioConductor.

  As of 2018-06-26 there are a total of 14532 packages available. This includes 11734 CRAN packages installed, out of 12867 available; and 2798 BioConductor-specific packages installed, out of 2843 available. These R packages are available as part of the R_packages/3.5.0 module as installed on rackham, irma, bianca and snowy, which requires and loads the R/3.5.0 module.  When the R_packages/3.5.0 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

See module help R_packages/3.5.0 for more information.

### R_packages/3.4.3
  A large number of R packages are available as part of the R_packages/3.4.3 module as installed on rackham, irma and bianca, which requires and loads the R/3.4.3 module.  When the R_packages/3.4.3 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

### R_packages/3.4.0
  A large number of R packages are available as part of the R_packages/3.4.0 module, which requires and loads the R/3.4.0 module.  When the R_packages/3.4.0 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

### R_packages/3.3.2
  A large number of R packages are available as part of the R_packages/3.3.2 module, which requires and loads the R/3.3.2 module.  When the R_packages/3.3.2 module is loaded, it adds a directory to the R_LIBS_SITE environment variable.  Within R, these packages will be available via library(package-name).

### R_packages/3.3.1
  A large number of R packages are available as part of the R_packages/3.3.1 module, which requires and loads the R/3.3.1 module.  When the R_packages/3.3.1 module is loaded, it adds a directory to the R_LIBS_SITE environment variable. Within R, these should be available via library(package-name).

### R_packages/3.3.0
  A large number of R packages are available as part of the R_packages/3.3.0 module, which requires and loads the R/3.3.0 module.  When the R_packages/3.3.0 module is loaded, it adds a directory to the R_LIBS_SITE environment variable. Within R, these should be available via library(package-name).



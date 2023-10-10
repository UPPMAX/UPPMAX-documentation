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

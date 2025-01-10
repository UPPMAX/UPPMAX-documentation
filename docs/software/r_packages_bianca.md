# Installing R packages on Bianca

???+ question "Read through the content below"

???+ question "Try to do the [exercise](r_packages_bianca.md#example-update-dowser)"


## First check if package is already in R_packages/x.y.z


- On UPPMAX the module ``R_packages`` is an omnibus package library containing almost all packages in the CRAN and BioConductor repositories.
    - As of 2023-11-21, there were a total of 23478  R packages installed in ``R_packages/4.3.1``.
        - A total of 23603 packages are available in CRAN and BioConductor
        - 19586 CRAN packages are installed, out of 20044 available
        - 3544 BioConductor-specific packages are installed, out of 3559 available
        - 346 other R packages are installed. These are not in CRAN/BioConductor, are only available in the CRAN/BioConductor archives, or are hosted on github, gitlab or elsewhere

Chances are good the R packages you need are already available once you load this module.  You can quickly check by loading it:

``$ ml R_packages/4.3.1``

Then within R, try loading the package you want:

``library(glmnet)``

Alternatively, and this is both a longer solution and not our recommended one, you can ``grep`` for the package after this module is loaded using the environment variable ``$R_LIBS_SITE``, which contains the locations of all R packages installed within the module.

```bash
$ ls -l $R_LIBS_SITE | grep glmnet
drwxrwsr-x  9 douglas sw  4096 May 28 16:59 EBglmnet
drwxrwsr-x 11 douglas sw  4096 May 25 01:22 glmnet
drwxrwsr-x  6 douglas sw  4096 May 25 04:03 glmnetSE
drwxrwsr-x  7 douglas sw  4096 May 25 04:04 glmnetUtils
drwxrwsr-x  8 douglas sw  4096 May 25 04:04 glmnetcr
drwxrwsr-x  7 douglas sw  4096 May 25 10:46 glmnetr
```

## Install steps

### Install on Rackham

- [R on UPPMAX course](https://uppmax.github.io/R-matlab-julia-HPC/r/packagesR.html){:target="_blank"}
- **note** First decide on which R version it should be based on and load that R_packages module.
- If not stated otherwise, your installation will end up in the ``~/R`` directory within your home directory

#### Methods

- automatic download and install from CRAN
    - <https://uppmax.github.io/bianca_workshops/extra/rpackages_copy/#automatic-download-and-install-from-cran>

- automatic download and install from GitHub
    - <https://uppmax.github.io/bianca_workshops/extra/rpackages_copy/#automatic-download-and-install-from-github>

- manual download and install
    - <https://uppmax.github.io/bianca_workshops/extra/rpackages_copy/#manual-download-and-install>
    - **NOTE** that if you install a package this way, you need to handle any dependencies yourself.
        - For instance you might get use of our modules  

### Transfer to wharf

- You may transfer the whole R library (in you home folder)  
    - this is usually the easiest way
- or select the directory(-ies) related to you new installation
    - **note** there may be more than one directory

### Move package to local Bianca R package path

- Sync or move the R directory or the specific folders to your ``~/R`` directory on bianca

### Test your installation

- Start an R session on bianca and load the new package

## Example: Update dowser

[dowser on ReadTheDocs](https://dowser.readthedocs.io/en/latest/){:target="_blank"}

!!! info

    - Dowser is part of the Immcantation analysis framework for Adaptive Immune Receptor Repertoire sequencing (AIRR-seq).
    - Dowser provides a set of tools for performing phylogenetic analysis on B cell receptor repertoires.
    - It supports building and visualizing trees using multiple methods, and implements statistical tests for discrete trait analysis of B cell migration, differentiation, and isotype switching.

The version of dowser in ``R_packages/4.2.1`` is 1.1.0. It was updated to version 1.2.0 on [2023-05-30](https://cran.rstudio.com/web/packages/dowser/){:target="_blank"}.

### Install dowser Rackham

You can update this for yourself by beginning on **rackham**. Do

``` bash
module load R_packages/4.2.1
```

and then, within R, do

``` R
install.packages('dowser')
```

The `install.packages()` command that you use to install new packages is also used to update already installed packages.

As the update begins, you will see two questions, answer yes to both:

``` R
Warning in install.packages("dowser") :
      'lib = "/sw/apps/R_packages/4.2.1/rackham"' is not writable
    Would you like to use a personal library instead? (yes/No/cancel) yes
```

and

``` R
Would you like to create a personal library
    '~/R/x86_64-pc-linux-gnu-library/4.2'
    to install packages into? (yes/No/cancel) yes
```

If you have already installed or updated an R package with R_packages/4.2.1 loaded that resulted in creating a personal library, you may not see one or both of these questions.

This will then lead to a brief installation process.  This creates the directory `~/R/x86_64-pc-linux-gnu-library/4.2` that it refers to in the question.  This directory contains your personal installations and updates of R packages.

The complete installation output for this update on rackham was:

``` R
> packageVersion('dowser')
[1] '1.1.0'
> install.packages('dowser')
Installing package into '/sw/apps/R_packages/4.2.1/rackham'
(as 'lib' is unspecified)
Warning in install.packages("dowser") :
  'lib = "/sw/apps/R_packages/4.2.1/rackham"' is not writable
Would you like to use a personal library instead? (yes/No/cancel) yes
Would you like to create a personal library
'/domus/h1/douglas/R/x86_64-pc-linux-gnu-library/4.2'
to install packages into? (yes/No/cancel) yes
--- Please select a CRAN mirror for use in this session ---
trying URL 'https://ftp.acc.umu.se/mirror/CRAN/src/contrib/dowser_1.2.0.tar.gz'
Content type 'application/x-gzip' length 1722229 bytes (1.6 MB)
==================================================
downloaded 1.6 MB

* installing *source* package 'dowser' ...
** package 'dowser' successfully unpacked and MD5 sums checked
** using staged installation
** R
** data
*** moving datasets to lazyload DB
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (dowser)

The downloaded source packages are in
    '/scratch/RtmpRo0Gz5/downloaded_packages'
>
> packageVersion('dowser')
[1] '1.2.0'
```

### Transfer to the Wharf

After installation, the next step is to copy the contents of this directory over to bianca so that it is the same directory within your bianca home directory.

Make sure you are in your **home directory**. Then connect to the bianca wharf.  Replace the name and project with your bianca user name and project.

``` bash
sftp douglas-sens2017625@bianca-sftp
```

You log in here like you log into bianca: the first password is your **password followed by the 6-digit authenticator code**, the second password (if required for you) is only your password.

Once sftp has connected, the contents of the current directory can be listed with

``` bash
dir
```

It should look like this:

    sftp> dir
    douglas-sens2017625

Now ``cd`` to this directory, which is your wharf directory within your project.

``` bash
sftp> cd douglas-sens2017625/
sftp> dir
sftp>
```

If you have not uploaded anything to your wharf, this will be empty. It might have a few things in it.

Now, upload your entire personal ``R`` directory from rackham here.

``` bash
sftp> put -r R
```

This will take a while to upload all the files. When it has completed, quit.

``` bash
sftp> quit
```

- Now, **log into bianca** using the shell, or using the web interface and start a terminal.
- Once you have a bianca shell, **change to your wharf directory** within your project.  Replace my user and project with yours.

``` bash
cd /proj/sens2017625/nobackup/wharf/douglas/douglas-sens2017625
```

Within this directory should be your R directory.

``` bash
[douglas@sens2017625-bianca douglas-sens2017625]$ ls -l
total 1892
drwxrwxr-x  3 douglas douglas    4096 Mar  2 14:27 R
```

### Sync from Wharf to Home directory

- Now sync this to your home directory:

``` bash
[douglas@sens2017625-bianca douglas-sens2017625]$ rsync -Pa R ~/
```

### Start an R session and load the new package

Because R_packages/4.2.1 was loaded when you installed/updated the packages in your personal R library, you need to have it loaded when you use these packages as well.

Simply change to the directory you want to work in, load the R_packages/4.2.1 module, and get to work.

``` bash
[douglas@sens2017625-bianca douglas-sens2017625]$ cd /proj/sens2017625/nobackup/douglas/
    [douglas@sens2017625-bianca douglas]$ module load R_packages/4.2.1
```

Then start R, and load the new package.

``` bash
[douglas@sens2017625-bianca douglas]$ R
```

``` R
    > packageVersion('dowser')
    [1] '1.2.0'
    > library(dowser)
    >
```


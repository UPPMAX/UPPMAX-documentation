# Installing R packages on Bianca

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

## Principles

- Find source files (``*.tar.gz``)
- Download to Transit and wharf folder with ``wget``
- Install On Bianca

### Detailed steps

Use [transit](../cluster_guides/login_transit.md)!

1. [Log in to transit](https://docs.uppmax.uu.se/cluster_guides/login_transit/)
2. [Go to the mounted project folder](https://docs.uppmax.uu.se/software/bianca_file_transfer_using_rsync/#3-mount-a-bianca-project)
3. [Download](#download-part) source files with ``wget``
4. Load R_packages of desired version (R is loaded on the fly)
5. Start R session
6. Install from source in R session

??? question "Can I use ``sftp`` to ``bianca-sftp.uppmax.uu.se``?"

    - No!
    - ``wget`` cannot be used within an SFTP session.

### Download part

- Use your **web browser** to find the package in
    - [CRAN](https://cran.r-project.org/web/packages/available_packages_by_name.html)
    - GitHub page
- Find the version of the package
    - CRAN: go to "old sources/Dowser archive"
    - GitHub: Go to Releases/tags

- Copy link for the package with name similar to ``<package>_<version>.tar.gz``.
- Go to the **terminal** and and be sure you are in the wharf folder, i.e. the mounted project folder in Transit
- Use the ``wget <copied link>`` command in Transit and correct project folder.

```console
wget <package>_<version>.tar.gz
```

### Installation part

- Log in to Bianca and the relevant project
- Load R_packages of desired version
- Start R session, either

    - from the wharf folder where the source files are
    - from other place and note the path to the source files

- Install from source in R session,

- from wharf folder

```R
> install.packages("<filename>", repos = NULL, type="source")
```

- from other folder

```R
> install.packages("<path-to/filename>", repos = NULL, type="source")
```

!!! example "Example with Dowser 2.0.0"

    [dowser on Readthedocs](https://dowser.readthedocs.io/en/latest/){:target="_blank"}

    !!! info

        - Dowser is part of the Immcantation analysis framework for Adaptive Immune Receptor Repertoire sequencing (AIRR-seq).
        - Dowser provides a set of tools for performing phylogenetic analysis on B cell receptor repertoires.
        - It supports building and visualising trees using multiple methods, and implements statistical tests for discrete trait analysis of         B cell migration, differentiation, and isotype switching.

        The version of dowser in ``R_packages/4.2.1`` is 1.1.0. It was updated to version 1.2.0 on [2023-05-30](https://cran.rstudio.com/web/packages/dowser/){:target="_blank"}.

    - Web page: <https://cran.r-project.org/web/packages/dowser/index.html>
    - just 2.4.0 is listed here
    - go to old sources/Dowser archive
    - choose 2.0.0.tar.gz
    - copy link
    - In project folder in **Transit**
    
    ```console
    wget https://cran.r-project.org/src/contrib/Archive/dowser/dowser_2.0.0.tar.gz
    ```

    - In **Bianca session** (right project!) and in wharf folder load ``R_packages`` and start R session
        
    - Ex: ``cd /proj/nobackup/sens2025560/wharf/bjornc/bjornc-sens2025560``

    ```console
    ml R_packages/4.3.1
    R
    ```

    In **R session**:

    ```R
    > install.packages("dowser_2.0.0.tar.gz", repos = NULL, type="source")
    ```
    
    - Type ``yes`` when asked about using a personal library.

    ??? question "Output"

        ```R
        Warning in install.packages("dowser_2.0.0.tar.gz", repos = NULL, type = "source") :
          'lib = "/sw/apps/R/4.3.1/rackham/lib64/R/library"' is not writable
        Would you like to use a personal library instead? (yes/No/cancel) yes
        Would you like to create a personal library
        ‘/castor/project/home/bjornc/R/x86_64-pc-linux-gnu-library/4.3’
        to install packages into? (yes/No/cancel) yes
        Installing package into ‘/castor/project/home/bjornc/R/x86_64-pc-linux-gnu-library/4.3’
        (as ‘lib’ is unspecified)
        Warning in untar2(tarfile, files, list, exdir, restore_times) :
          skipping pax global extended headers
        * installing *source* package ‘dowser’ ...
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
        >
        ```

    - Test it!

    ```R
    > library(dowser)
    Loading required package: ggplot2
    Registered S3 methods overwritten by 'treeio':
      method              from
      MRCA.phylo          tidytree
      MRCA.treedata       tidytree
      Nnode.treedata      tidytree
    ...
        
    ```  

    - Check the used version (look for the dowser ino)

    ```R
    sessionInfo()
    ```  

    ??? question "How may that look like?"

        ```R
        sessionInfo()
        R version 4.3.1 (2023-06-16)
        Platform: x86_64-pc-linux-gnu (64-bit)
        Running under: CentOS Linux 7 (Core)

        Matrix products: default
        BLAS:   /sw/apps/R/4.3.1/rackham/lib64/R/lib/libRblas.so
        LAPACK: /sw/apps/R/4.3.1/rackham/lib64/R/lib/libRlapack.so;  LAPACK version 3.11.0

        locale:
         [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C
         [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8
         [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8
         [7] LC_PAPER=en_US.UTF-8       LC_NAME=C
         [9] LC_ADDRESS=C               LC_TELEPHONE=C
        [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C

        time zone: Europe/Stockholm
        tzcode source: system (glibc)

        attached base packages:
        [1] stats     graphics  grDevices utils     datasets  methods   base

        other attached packages:
        [1] dowser_2.0.0  ggplot2_3.4.3

        loaded via a namespace (and not attached):
         [1] ade4_1.7-22                 tidyselect_1.2.0
         [3] dplyr_1.1.3                 Biostrings_2.68.1
         [5] bitops_1.0-7                fastmap_1.1.1
         [7] lazyeval_0.2.2              RCurl_1.98-1.12
         [9] GenomicAlignments_1.36.0    digest_0.6.33
        [11] phylotate_1.3               lifecycle_1.0.3
        [13] alakazam_1.3.0              tidytree_0.4.5
        [15] magrittr_2.0.3              compiler_4.3.1
        [17] rlang_1.1.1                 progress_1.2.2
        [19] tools_4.3.1                 igraph_1.5.1
        [21] utf8_1.2.3                  yaml_2.3.7
        [23] phangorn_2.11.1             prettyunits_1.2.0
        [25] S4Arrays_1.0.6              DelayedArray_0.26.7
        [27] KernSmooth_2.23-21          aplot_0.2.1
        [29] abind_1.4-5                 BiocParallel_1.34.2
        [31] withr_2.5.1                 purrr_1.0.2
        [33] BiocGenerics_0.46.0         grid_4.3.1
        [35] stats4_4.3.1                shazam_1.2.0
        [37] fansi_1.0.4                 colorspace_2.1-0
        [39] iterators_1.0.14            scales_1.2.1
        [41] MASS_7.3-60                 SummarizedExperiment_1.30.2
        [43] cli_3.6.1                   crayon_1.5.2
        [45] treeio_1.24.3               generics_0.1.3
        [47] ggtree_3.8.2                tzdb_0.4.0
        [49] ape_5.7-1                   cachem_1.0.8
        [51] stringr_1.5.0               zlibbioc_1.46.0
        [53] parallel_4.3.1              ggplotify_0.1.2
        [55] XVector_0.40.0              matrixStats_1.0.0
        [57] yulab.utils_0.1.0           vctrs_0.6.3
        [59] Matrix_1.6-1.1              jsonlite_1.8.7
        [61] gridGraphics_0.5-1          IRanges_2.34.1
        [63] hms_1.1.3                   patchwork_1.1.3
        [65] S4Vectors_0.38.2            seqinr_4.2-30
        [67] foreach_1.5.2               diptest_0.76-0
        [69] tidyr_1.3.0                 glue_1.6.2
        [71] codetools_0.2-19            stringi_1.7.12
        [73] gtable_0.3.4                GenomeInfoDb_1.36.3
        [75] quadprog_1.5-8              GenomicRanges_1.52.0
        [77] munsell_0.5.0               tibble_3.2.1
        [79] pillar_1.9.0                GenomeInfoDbData_1.2.10
        [81] R6_2.5.1                    airr_1.5.0
        [83] doParallel_1.0.17           lattice_0.21-8
        [85] Biobase_2.60.0              markdown_1.9
        [87] readr_2.1.4                 Rsamtools_2.16.0
        [89] memoise_2.0.1               ggfun_0.1.3
        [91] Rcpp_1.0.11                 fastmatch_1.1-4
        [93] gridExtra_2.3               nlme_3.1-162
        [95] fs_1.6.3                    MatrixGenerics_1.12.3
        [97] pkgconfig_2.0.3
        >
        ```

- You should see: ``dowser_2.0.0``
- This confirms that you are using version ``2.0.0``!
- You can now remove the source file from the wharf folder.

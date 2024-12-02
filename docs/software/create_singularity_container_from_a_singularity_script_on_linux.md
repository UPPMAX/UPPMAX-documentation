---
tags:
  - Singularity
  - Singularity script
  - create
  - build
  - Linux
  - local computer
---

# Create a Singularity container from a Singularity script on a computer with Linux where you have super-user rights

There are multiple ways how to [create a Singularity container](create_singularity_container.md).

This page shows how to do so using a computer with Linux where you have super-user rights.

Note that users have no super-user rights on our UPPMAX clusters.

## Procedure

### 1. Save the script to a Singularity file

Save the script as a file called `Singularity` (this is the recommended filename
for Singularity scripts).

???- question "Do you have an example Singularity script?"

    Yes! Here is an example Singularity script:

    ```singularity
    Bootstrap: docker
    From: rocker/tidyverse

    %post
        # From https://github.com/brucemoran/Singularity/blob/8eb44591284ffb29056d234c47bf8b1473637805/shub/bases/recipe.CentOs7-R_3.5.2#L21
        echo 'export LANG=en_US.UTF-8 LANGUAGE=C LC_ALL=C LC_CTYPE=C LC_COLLATE=C  LC_TIME=C LC_MONETARY=C LC_PAPER=C LC_MEASUREMENT=C' >> $SINGULARITY_ENVIRONMENT

        Rscript -e 'install.packages(c("remotes", "devtools"))'
        Rscript -e 'remotes::install_github("bmbolstad/preprocessCore")'

    %runscript
    Rscript "$@"
    ```

### 2. Build the Singularity container

Here is how you create a Singularity container called `my_container.sif` from the Singularity script:

```bash
sudo singularity build my_container.sif Singularity
```

Which will build a Singularity container called `my_container.sif`.

???- question "How does that look like?"

    You output will be similar to this:

    ```bash
    sven@richel-N141CU:~/temp$ sudo singularity build my_container.sif Singularity 
    INFO:    Starting build...
    INFO:    Fetching OCI image...
    307.6MiB / 307.6MiB [================================================================================================================================================] 100 % 0.0 b/s 0s
    30.9MiB / 30.9MiB [==================================================================================================================================================] 100 % 0.0 b/s 0s
    28.2MiB / 28.2MiB [==================================================================================================================================================] 100 % 0.0 b/s 0s
    261.1MiB / 261.1MiB [================================================================================================================================================] 100 % 0.0 b/s 0s
    193.7MiB / 193.7MiB [================================================================================================================================================] 100 % 0.0 b/s 0s
    26.3MiB / 26.3MiB [==================================================================================================================================================] 100 % 0.0 b/s 0s
    288.7KiB / 288.7KiB [================================================================================================================================================] 100 % 0.0 b/s 0s
    INFO:    Extracting OCI image...
    INFO:    Inserting Singularity configuration...
    INFO:    Running post scriptlet
    + echo export LANG=en_US.UTF-8 LANGUAGE=C LC_ALL=C LC_CTYPE=C LC_COLLATE=C  LC_TIME=C LC_MONETARY=C LC_PAPER=C LC_MEASUREMENT=C
    + Rscript -e install.packages(c("remotes", "devtools"))
    Installing packages into ‘/usr/local/lib/R/site-library’
    (as ‘lib’ is unspecified)
    trying URL 'https://p3m.dev/cran/__linux__/jammy/latest/src/contrib/remotes_2.5.0.tar.gz'
    Content type 'binary/octet-stream' length 436043 bytes (425 KB)
    ==================================================
    downloaded 425 KB

    trying URL 'https://p3m.dev/cran/__linux__/jammy/latest/src/contrib/devtools_2.4.5.tar.gz'
    Content type 'binary/octet-stream' length 435688 bytes (425 KB)
    ==================================================
    downloaded 425 KB

    * installing *binary* package ‘remotes’ ...
    * DONE (remotes)
    * installing *binary* package ‘devtools’ ...
    * DONE (devtools)

    The downloaded source packages are in
     ‘/tmp/Rtmpow1CFQ/downloaded_packages’
    + Rscript -e remotes::install_github("bmbolstad/preprocessCore")
    Downloading GitHub repo bmbolstad/preprocessCore@HEAD
    ── R CMD build ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ✔  checking for file ‘/tmp/Rtmpx5C1XE/remotes13a1238df5bce/bmbolstad-preprocessCore-33ccbd9/DESCRIPTION’ (337ms)
    ─  preparing ‘preprocessCore’:
    ✔  checking DESCRIPTION meta-information ...
    ─  cleaning src
    ─  running ‘cleanup’
    ─  checking for LF line-endings in source and make files and shell scripts
    ─  checking for empty or unneeded directories
    ─  building ‘preprocessCore_1.61.0.tar.gz’
       
    Installing package into ‘/usr/local/lib/R/site-library’
    (as ‘lib’ is unspecified)
    * installing *source* package ‘preprocessCore’ ...
    ** using staged installation
    'config' variable 'CPP' is defunct
    checking for gcc... gcc
    checking whether the C compiler works... yes
    checking for C compiler default output file name... a.out
    checking for suffix of executables... 
    checking whether we are cross compiling... no
    checking for suffix of object files... o
    checking whether we are using the GNU C compiler... yes
    checking whether gcc accepts -g... yes
    checking for gcc option to accept ISO C89... none needed
    checking how to run the C preprocessor... gcc -E
    checking for library containing pthread_create... none required
    checking for grep that handles long lines and -e... /usr/bin/grep
    checking for egrep... /usr/bin/grep -E
    checking for ANSI C header files... yes
    checking for sys/types.h... yes
    checking for sys/stat.h... yes
    checking for stdlib.h... yes
    checking for string.h... yes
    checking for memory.h... yes
    checking for strings.h... yes
    checking for inttypes.h... yes
    checking for stdint.h... yes
    checking for unistd.h... yes
    checking for stdlib.h... (cached) yes
    checking if PTHREAD_STACK_MIN is defined... yes
    checking if R is using flexiblas... flexiblas not found. preprocessCore threading will not be disabled
    configure: Enabling threading for preprocessCore
    configure: creating ./config.status
    config.status: creating src/Makevars
    ** libs
    using C compiler: ‘gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0’
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_colSummarize.c -o R_colSummarize.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_plmd_interfaces.c -o R_plmd_interfaces.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_plmr_interfaces.c -o R_plmr_interfaces.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_rlm_interfaces.c -o R_rlm_interfaces.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_subColSummarize.c -o R_subColSummarize.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c R_subrcModel_interfaces.c -o R_subrcModel_interfaces.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c avg.c -o avg.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c avg_log.c -o avg_log.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c biweight.c -o biweight.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c init_package.c -o init_package.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c lm.c -o lm.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c log_avg.c -o log_avg.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c log_median.c -o log_median.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c matrix_functions.c -o matrix_functions.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c median.c -o median.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c median_log.c -o median_log.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c medianpolish.c -o medianpolish.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c plmd.c -o plmd.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c plmr.c -o plmr.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c psi_fns.c -o psi_fns.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c qnorm.c -o qnorm.o
    qnorm.c: In function ‘qnorm_c_l’:
    qnorm.c:595:63: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘size_t’ {aka ‘long unsigned int’} [-Wformat=]
      595 |          error("ERROR; return code from pthread_join(thread #%d) is %d, exit status for thread was %d\n",
          |                                                              ~^
          |                                                               |
          |                                                               int
          |                                                              %ld
      596 |                i, returnCode, *((int *) status));
          |                ~                                               
          |                |
          |                size_t {aka long unsigned int}
    qnorm.c:616:63: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘size_t’ {aka ‘long unsigned int’} [-Wformat=]
      616 |          error("ERROR; return code from pthread_join(thread #%d) is %d, exit status for thread was %d\n",
          |                                                              ~^
          |                                                               |
          |                                                               int
          |                                                              %ld
      617 |                i, returnCode, *((int *) status));
          |                ~                                               
          |                |
          |                size_t {aka long unsigned int}
    qnorm.c: In function ‘qnorm_c_determine_target_l’:
    qnorm.c:2004:63: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘size_t’ {aka ‘long unsigned int’} [-Wformat=]
     2004 |          error("ERROR; return code from pthread_join(thread #%d) is %d, exit status for thread was %d\n",
          |                                                              ~^
          |                                                               |
          |                                                               int
          |                                                              %ld
     2005 |                i, returnCode, *((int *) status));
          |                ~                                               
          |                |
          |                size_t {aka long unsigned int}
    qnorm.c: In function ‘qnorm_c_determine_target_via_subset_l’:
    qnorm.c:2604:63: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘size_t’ {aka ‘long unsigned int’} [-Wformat=]
     2604 |          error("ERROR; return code from pthread_join(thread #%d) is %d, exit status for thread was %d\n",
          |                                                              ~^
          |                                                               |
          |                                                               int
          |                                                              %ld
     2605 |                i, returnCode, *((int *) status));
          |                ~                                               
          |                |
          |                size_t {aka long unsigned int}
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c rlm.c -o rlm.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c rlm_anova.c -o rlm_anova.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c rlm_se.c -o rlm_se.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c rma_background4.c -o rma_background4.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c rma_common.c -o rma_common.o
    gcc -I"/usr/local/lib/R/include" -DNDEBUG -I/usr/local/include  -I/usr/local/include   -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDLIB_H=1 -DUSE_PTHREADS=1 -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c weightedkerneldensity.c -o weightedkerneldensity.o
    gcc -shared -L/usr/local/lib/R/lib -L/usr/local/lib -o preprocessCore.so R_colSummarize.o R_plmd_interfaces.o R_plmr_interfaces.o R_rlm_interfaces.o R_subColSummarize.o R_subrcModel_interfaces.o avg.o avg_log.o biweight.o init_package.o lm.o log_avg.o log_median.o matrix_functions.o median.o median_log.o medianpolish.o plmd.o plmr.o psi_fns.o qnorm.o rlm.o rlm_anova.o rlm_se.o rma_background4.o rma_common.o weightedkerneldensity.o -llapack -lblas -lgfortran -lm -lquadmath -L/usr/local/lib/R/lib -lR
    installing to /usr/local/lib/R/site-library/00LOCK-preprocessCore/00new/preprocessCore/libs
    ** R
    ** inst
    ** byte-compile and prepare package for lazy loading
    ** help
    *** installing help indices
    ** building package indices
    ** testing if installed package can be loaded from temporary location
    ** checking absolute paths in shared objects and dynamic libraries
    ** testing if installed package can be loaded from final location
    ** testing if installed package keeps a record of temporary installation path
    * DONE (preprocessCore)
    INFO:    Adding runscript
    INFO:    Creating SIF file...
    INFO:    Build complete: my_container.sif
    ```

### 3. Use the container

How to use a container, depends on what it does.

Here are some thing to try:

Run the container without arguments, in the hope of getting a clear error message with instructions:

```bash
./my_container.sif
```

Run the container in the hope of seeing its documentation:

```bash
./my_container.sif --help
```

Run the container on the local folder, in the hope of getting a clear error message with instructions:

```bash
./my_container.sif .
```

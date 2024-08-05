# Picard

'Picard is a set of command line tools for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF'
([source: the Picard documentation](https://broadinstitute.github.io/picard/index.html)).

## Usage

Load the `bioinfo-tools` [module](../cluster_guides/modules.md) first:

```bash
module load bioinfo-tools
```

Then search for you favorite Picard version:

```bash
module spider picard
```

???- question "How does this look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham2 ~]$ module spider picard

    ----------------------------------------------------------------------------
      picard:
    ----------------------------------------------------------------------------
         Versions:
            picard/1.92
            picard/1.118
            picard/1.141
            picard/2.0.1
            picard/2.10.3
            picard/2.19.2
            picard/2.20.4
            picard/2.23.4
            picard/2.27.5
            picard/3.1.1

    ----------------------------------------------------------------------------
      For detailed information about a specific "picard" package (including how to l
    oad the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider picard/3.1.1
    ----------------------------------------------------------------------------
    ```

Then load your favorite version:


```bash
module load picard/3.1.1
```

???- question "How does this look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham2 ~]$ module load picard/3.1.1
    picard/3.1.1: java -jar $PICARD command ...
    ```

Read up on how to use Picard:

```bash
module help picard/3.1.1
```

???- question "How does this look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham2 ~]$ module help picard/3.1.1

    ----------------------------------------------------------------------- Module Specific Help for "picard/3.1.1" -----------------------------------------------------------------------
     picard - use picard/3.1.1

        Version 3.1.1

    Usage:

        java -jar $PICARD command ...

    or

        java -jar $PICARD_ROOT/picard.jar command ...

    where 'command' is the desired Picard command, and ... are the desired further arguments.

    ```

Here is an example of using Picard to test if a file is a valid BAM/CRAM/SAM file:

```bash
java -jar $PICARD ValidateSamFile --INPUT my_file.bam
```

???- question "How does this look like?"

    First, download an example BAM file from the Picard GitHub repository:

    ```bash
    [richel@rackham2 ~]$ wget https://github.com/broadinstitute/picard/raw/master/testdata/picard/flow/reads/input/sample_mc.bam

    --2024-08-05 09:16:40--  https://github.com/broadinstitute/picard/raw/master/testdata/picard/flow/reads/input/sample_mc.bam
    Resolving github.com (github.com)... 140.82.121.3
    Connecting to github.com (github.com)|140.82.121.3|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://raw.githubusercontent.com/broadinstitute/picard/master/testdata/picard/flow/reads/input/sample_mc.bam [following]
    --2024-08-05 09:16:40--  https://raw.githubusercontent.com/broadinstitute/picard/master/testdata/picard/flow/reads/input/sample_mc.bam
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 117715 (115K) [application/octet-stream]
    Saving to: ‘sample_mc.bam’

    100%[=============================================================================================================================================>] 117,715     --.-K/s   in 0.001s  

    2024-08-05 09:16:41 (171 MB/s) - ‘sample_mc.bam’ saved [117715/117715]
    ```

    Your output will be similar to this, when using that valid BAM file:

    ```bash
    [richel@rackham2 ~]$ java -jar $PICARD ValidateSamFile --INPUT sample_mc.bam 
    Aug 05, 2024 9:16:47 AM com.intel.gkl.NativeLibraryLoader load
    INFO: Loading libgkl_compression.so from jar:file:/sw/bioinfo/picard/3.1.1/rackham/picard.jar!/com/intel/gkl/native/libgkl_compression.so
    [Mon Aug 05 09:16:47 CEST 2024] ValidateSamFile --INPUT sample_mc.bam --MODE VERBOSE --MAX_OUTPUT 100 --IGNORE_WARNINGS false --VALIDATE_INDEX true --INDEX_VALIDATION_STRINGENCY EXHAUSTIVE --IS_BISULFITE_SEQUENCED false --MAX_OPEN_TEMP_FILES 8000 --SKIP_MATE_VALIDATION false --VERBOSITY INFO --QUIET false --VALIDATION_STRINGENCY STRICT --COMPRESSION_LEVEL 5 --MAX_RECORDS_IN_RAM 500000 --CREATE_INDEX false --CREATE_MD5_FILE false --help false --version false --showHidden false --USE_JDK_DEFLATER false --USE_JDK_INFLATER false
    [Mon Aug 05 09:16:47 CEST 2024] Executing as richel@rackham2.uppmax.uu.se on Linux 3.10.0-1160.119.1.el7.x86_64 amd64; OpenJDK 64-Bit Server VM 17+35-2724; Deflater: Intel; Inflater: Intel; Provider GCS is available; Picard version: Version:3.1.1
    WARNING 2024-08-05 09:16:47 ValidateSamFile NM validation cannot be performed without the reference. All other validations will still occur.
    No errors found
    [Mon Aug 05 09:16:48 CEST 2024] picard.sam.ValidateSamFile done. Elapsed time: 0.01 minutes.
    Runtime.totalMemory()=2181038080
    [richel@rackham2 ~]$ 
    ```

    Your output will be similar to this, when using an invalid file,
    such as an R script file:

    ```bash
    [richel@rackham2 ~]$ java -jar $PICARD ValidateSamFile --INPUT app.R 
    Aug 05, 2024 9:13:20 AM com.intel.gkl.NativeLibraryLoader load
    INFO: Loading libgkl_compression.so from jar:file:/sw/bioinfo/picard/3.1.1/rackham/picard.jar!/com/intel/gkl/native/libgkl_compression.so
    [Mon Aug 05 09:13:20 CEST 2024] ValidateSamFile --INPUT app.R --MODE VERBOSE --MAX_OUTPUT 100 --IGNORE_WARNINGS false --VALIDATE_INDEX true --INDEX_VALIDATION_STRINGENCY EXHAUSTIVE --IS_BISULFITE_SEQUENCED false --MAX_OPEN_TEMP_FILES 8000 --SKIP_MATE_VALIDATION false --VERBOSITY INFO --QUIET false --VALIDATION_STRINGENCY STRICT --COMPRESSION_LEVEL 5 --MAX_RECORDS_IN_RAM 500000 --CREATE_INDEX false --CREATE_MD5_FILE false --help false --version false --showHidden false --USE_JDK_DEFLATER false --USE_JDK_INFLATER false
    [Mon Aug 05 09:13:21 CEST 2024] Executing as richel@rackham2.uppmax.uu.se on Linux 3.10.0-1160.119.1.el7.x86_64 amd64; OpenJDK 64-Bit Server VM 17+35-2724; Deflater: Intel; Inflater: Intel; Provider GCS is available; Picard version: Version:3.1.1
    WARNING 2024-08-05 09:13:21 ValidateSamFile NM validation cannot be performed without the reference. All other validations will still occur.
    ERROR::MISSING_READ_GROUP:Read groups is empty
    SAMFormatException on record 01
    ERROR 2024-08-05 09:13:21 ValidateSamFile SAMFormatException on record 01
    [Mon Aug 05 09:13:21 CEST 2024] picard.sam.ValidateSamFile done. Elapsed time: 0.01 minutes.
    Runtime.totalMemory()=2181038080
    To get help, see http://broadinstitute.github.io/picard/index.html#GettingHelp
    ```


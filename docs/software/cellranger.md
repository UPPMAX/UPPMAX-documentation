---
tags:
  - cellranger
  - cell ranger
  - Cellranger
  - Cell Ranger
  - 10XGenomics
  - 10x Genomics
---

# Cell Ranger

According to
[the Cell Ranger GitHub repository](https://github.com/10XGenomics/cellranger):

> Cell Ranger is a set of analysis pipelines that perform sample
> demultiplexing, barcode processing, single cell 3' and 5' gene counting,
> V(D)J transcript sequence assembly and annotation,
> and Feature Barcode analysis from 10x Genomics Chromium Single Cell data.

Cell Ranger (the tool) is part of the `cellranger`
[module](../cluster_guides/modules.md).

Finding the [module](../cluster_guides/modules.md) that
has `cowsay` installed:

```bash
module spider cellranger
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ module spider cellranger

    ----------------------------------------------------------------------------
      cellranger:
    ----------------------------------------------------------------------------
         Versions:
            cellranger/1.1.0
            cellranger/1.3.0
            cellranger/2.0.2
            cellranger/2.2.0
            cellranger/3.0.1
            cellranger/4.0.0
            cellranger/5.0.1
            cellranger/6.0.2
            cellranger/6.1.2
            cellranger/7.0.0
            cellranger/7.0.1
            cellranger/7.1.0
            cellranger/8.0.1
         Other possible modules matches:
            cellranger-ARC  cellranger-ARC-data  cellranger-ATAC  cellranger-ATAC-da
    ta  ...

    ----------------------------------------------------------------------------
      To find other possible module matches execute:

          $ module -r spider '.*cellranger.*'

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger" package (including how
    to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger/8.0.1
    ----------------------------------------------------------------------------
    ```


???- question "How to see the tools similar to `cellranger`?"

    In case you want to search for similar tools, add
    a dash at the end of the search term:

    ```bash
    module spider cellranger-
    ```

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ module spider cellranger-

    ----------------------------------------------------------------------------
      cellranger-ARC:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-ARC/1.0.0
            cellranger-ARC/2.0.2

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-ARC" package (including
    how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-ARC/2.0.2
    ----------------------------------------------------------------------------

    ----------------------------------------------------------------------------
      cellranger-ARC-data:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-ARC-data/2020-A
            cellranger-ARC-data/2020-A-2.0.0

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-ARC-data" package (inclu
    ding how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-ARC-data/2020-A-2.0.0
    ----------------------------------------------------------------------------

    ----------------------------------------------------------------------------
      cellranger-ATAC:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-ATAC/1.2.0
            cellranger-ATAC/2.0.0
            cellranger-ATAC/2.1.0

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-ATAC" package (including
     how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-ATAC/2.1.0
    ----------------------------------------------------------------------------

    ----------------------------------------------------------------------------
      cellranger-ATAC-data:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-ATAC-data/1.2.0
            cellranger-ATAC-data/2.0.0

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-ATAC-data" package (incl
    uding how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-ATAC-data/2.0.0
    ----------------------------------------------------------------------------

    ----------------------------------------------------------------------------
      cellranger-DNA: cellranger-DNA/1.1.0
    ----------------------------------------------------------------------------

        You will need to load all module(s) on any one of the lines below before the
     "cellranger-DNA/1.1.0" module is available to load.

          bioinfo-tools

        Help:
           cellranger-DNA - use cellranger-DNA 1.1.0


          The cellranger-DNA-data/1.0.0 module is loaded as a prerequisite.




    ----------------------------------------------------------------------------
      cellranger-DNA-data: cellranger-DNA-data/1.0.0
    ----------------------------------------------------------------------------

        This module can be loaded directly: module load cellranger-DNA-data/1.0.0

        Help:
           cellranger-DNA-data - use cellranger-DNA-data 1.0.0


          10X Genomics Chromium Cell Ranger DNA data
          Version 1.0.0
          https://support.10xgenomics.com/single-cell-dna/software/downloads/latest

          NOTE: This is a data module. The software that uses this data is the cellr
    anger-DNA module, which loads this.


          Default data for GRCh38, GRCh38 and GRCm38 references can be found in $CEL
    LRANGER_DNA_DATA.
          To see the top-level directories:

           ls -l $CELLRANGER_DNA_DATA

          Genome assembly    Subdirectory
          ---------------    ------------
          GRCh38             refdata-GRCh38-1.0.0
          GRCh37             refdata-GRCh37-1.0.0
          GRCm38             refdata-GRCm38-1.0.0

          Sample Index Set Sequences (both CSV and JSON formats)
          ------------------------------------------------------
          Chromium DNA     chromium-shared-sample-indexes-plate.csv
                           chromium-shared-sample-indexes-plate.json

          For information on how each dataset was produced, see the References secti
    on of
          https://support.10xgenomics.com/single-cell-dna/software/downloads/latest




    ----------------------------------------------------------------------------
      cellranger-VDJ-data:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-VDJ-data/4.0.0
            cellranger-VDJ-data/5.0.0
            cellranger-VDJ-data/7.0.0
            cellranger-VDJ-data/7.1.0

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-VDJ-data" package (inclu
    ding how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-VDJ-data/7.1.0
    ----------------------------------------------------------------------------

    ----------------------------------------------------------------------------
      cellranger-data:
    ----------------------------------------------------------------------------
         Versions:
            cellranger-data/1.1.0
            cellranger-data/1.2.0
            cellranger-data/3.0.0
            cellranger-data/2020-A
            cellranger-data/2024-A

    ----------------------------------------------------------------------------
      For detailed information about a specific "cellranger-data" package (including
     how to load the modules) use the module's full name.
      Note that names that have a trailing (E) are extensions provided by other modu
    les.
      For example:

         $ module spider cellranger-data/2024-A
    ----------------------------------------------------------------------------
    ```


Loading the latest version of the `cellranger` module:

```bash
module load bioinfo-tools cellranger/8.0.1
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ module load bioinfo-tools cellranger/8.0.1
    Default data for several references are available at $CELLRANGER_DATA; see 'module help cellranger-data/2024-A' for more information
    Default data for GRCh38 and GRCm38 immune profiling references are available at $CELLRANGER_VDJ_DATA; see 'module help cellranger-VDJ-data/7.1.0' for more information
    ```

Now you can run Cell Ranger:

```bash
cellranger
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ cellranger
    cellranger cellranger-8.0.1

    Process 10x Genomics Gene Expression, Feature Barcode, and Immune Profiling data

    Usage: cellranger <COMMAND>

    Commands:
      count           Count gene expression and/or feature barcode reads from a
                          single sample and GEM well
      multi           Analyse multiplexed data or combined gene
                          expression/immune profiling/feature barcode data
      multi-template  Output a multi config CSV template
      vdj             Assembles single-cell VDJ receptor sequences from 10x
                          Immune Profiling libraries
      aggr            Aggregate data from multiple Cell Ranger runs
      reanalyze       Re-run secondary analysis (dimensionality reduction,
                          clustering, etc)
      mkvdjref        Prepare a reference for use with CellRanger VDJ
      mkfastq         Run Illumina demultiplexer on sample sheets that contain
                          10x-specific sample index sets
      testrun         Execute the 'count' pipeline on a small test dataset
      mat2csv         Convert a feature-barcode matrix to CSV format
      mkref           Prepare a reference for use with 10x analysis software.
                          Requires a GTF and FASTA
      mkgtf           Filter a GTF file by attribute prior to creating a 10x
                          reference
      upload          Upload analysis logs to 10x Genomics support
      sitecheck       Collect Linux system configuration information
      help            Print this message or the help of the given subcommand(s)

    Options:
      -h, --help     Print help
      -V, --version  Print version
    ```

## Using Cell Ranger from Python

???- info "For staff"

    Related to [ticket 297240](https://github.com/UPPMAX/ticket_297240)

## Links

- [Cell Ranger GitHub repository](https://github.com/10XGenomics/cellranger)

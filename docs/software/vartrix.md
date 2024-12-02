# VarTrix

VarTrix is 'a software tool for extracting single cell variant information
from 10x Genomics single cell data' (as quoted from [the VarTrix repository](https://github.com/10XGenomics/vartrix)).

To use VarTrix on an UPPMAX cluster, do

```bash
module load bioinfo-tools
```

After this, search for the [module](../cluster_guides/modules.md)
of your favorite Vartrix version, using:

```bash
module spider vartrix
```

???- question "How does that look like?"

    The output will look similar to:


    ```bash
    [sven@rackham3 vartrix]$ module spider vartrix

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      vartrix: vartrix/1.1.22
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        You will need to load all module(s) on any one of the lines below before the "vartrix/1.1.22" module is available to load.

          bioinfo-tools
     
        Help:
          vartrix - use vartrix 
          
          Description
          
          Single-Cell Genotyping Tool
          
          Version 1.1.22
          
          https://github.com/10XGenomics/vartrix
          
          Usage:
              
              Example:
          
              vartrix --bam $VARTRIX_TEST/test_dna.bam \
                      --cell-barcodes $VARTRIX_TEST/dna_barcodes.tsv \
                      --fasta $VARTRIX_TEST/test_dna.fa  \
                      --vcf $VARTRIX_TEST/test_dna.vcf
    ```

Then load your favorite version, for example:

```bash
module load vartrix/1.1.22
```

## Links

- [vartrix repository](https://github.com/10XGenomics/vartrix)

# Simons Genome Diversity Project datasets

The Simons Foundation's Genome Diversity Project datasets are now available on UPPMAX. These represent deep human genome sequence data sampled to represent as much diversity as possible:

sgdp geographical distribution

There are currently approximately 14 TB of data, in the form of CRAM files with associated indices and summaries of the BAM files from which the CRAM files werre derived.

Our current SGDP data are those aligned to human reference genome GRCh38DH found at ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/simons_diversity_data/. The local UPPMAX directory for these data is /sw/data/SGDP/. The command used to collect the data was

echo "mirror data" | lftp ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/simons_diversity_data

As a result, the local UPPMAX archive is found at /sw/data/SGDP/data/. Within this directory are subdirectories for each of the populations included in the full dataset, with individual samples found within each population directory. For example,

rackham1: /sw/data/SGDP $ ls -l data/Greek
total 8
drwxr-s--- 3 douglas kgp 4096 Apr 29 14:03 SAMEA3302732
drwxr-s--- 3 douglas kgp 4096 Apr 29 14:03 SAMEA3302763

and one of these sample directories contains

rackham1: /sw/data/SGDP $ ls -l data/Greek/SAMEA3302732/alignment/
total 34529204
-rw-r----- 1 douglas kgp         635 Nov 30  2020 SAMEA3302732.alt_bwamem_GRCh38DH.20200922.Greek.simons.bam.bas
-rw-r----- 1 douglas kgp 35355769475 Nov 30  2020 SAMEA3302732.alt_bwamem_GRCh38DH.20200922.Greek.simons.cram
-rw-r----- 1 douglas kgp     2079029 Dec  1  2020 SAMEA3302732.alt_bwamem_GRCh38DH.20200922.Greek.simons.cram.crai

To access this data, please request membership in the kgp group by emailing <support@uppmax.uu.se>. As for the 1000 Genomes Project, this is not to restrict access in any way, but rather to make it easier to inform UPPMAX users using the datasets of any relevant changes. Because the local copies of these datasets are hosted on UPPMAX systems, access is restricted to UPPMAX users; non-UPPMAX users will need to follow the procedures described on the SGDP website to download their own copies of the datasets.

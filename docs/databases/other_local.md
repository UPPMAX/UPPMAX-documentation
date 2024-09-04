# Other bioinformatics-oriented local data resources

Haplotype Reference Consortium

The Haplotype Reference Consortium VCF database is a large reference panel of human haplotypes produced by combining together sequencing data from multiple cohorts.  Version r1.1 is installed on all systems as data [module](../cluster_guides/modules.md) HaplotypeReferenceConsortium/r1.1.
GnomAD: Genome Aggregation Database

The Genome Aggregation Database (gnomAD) VCF database is downloaded and loacated in /sw/data/gnomad_data/vcf/{exomes, genomes}.
ExAC: Exome Aggregation Consortium

The ExAC Exome Aggregation Consortium database releases 0.1, 0.2, 0.3 and 0.3.1 are downloaded in their entirety and are available at /sw/data/ExAC/release{0.1,0.2,0.3,0.3.1}.
Pfam

The Pfam database versions 2011, 28.0, 31.0 and 35.0 are downloaded in their entirety and available via the data modules Pfam/{2011,28.0,31.0,35.0} which each define the environment variable PFAM_ROOT to the location of the Pfam downloads. See the appropriate module help for further information. In particular, the family-specific trees are available in $PFAM_ROOT/trees. The given directory can be used for the -dir argument to the pfam_scan.pl script provided by the pfam_scan modules, which each load the appropriate Pfam data module.  Module version pfam_scan/1.5 is for Pfam/28.0, and module version pfam_scan/1.6 is for Pfam/31.0. This latter module might also work with Pfam/35.0

    pfam_scan.pl -dir $PFAM_ROOT ...

The pfam_scan.pl script is designed to work with the Pfam database.
dbCAN

The dbCAN 4.0 database for automated carbohydrate-active enzyme annotation is now available in directory /sw/data/dbCAN/4.0 on Uppmax servers. The database is formatted for use with the hmmer/3.1b1-{gcc,intel} modules. For more information see /sw/data/dbCAN/4.0/readme.txt or the remote version.

The local path to the script for post-processing hmmscan --domtblout output is /sw/data/dbCAN/4.0/hmmscan-parser.sh. The CAZyDB trees have also been unpacked and are available in /sw/data/dbCAN/4.0/CAZyDB-phylogeny.
Variant Effect Predictor cache files

A local cache for all database files available for Ensembl's Variant Effect Predictor 87, 89 and 91 are available in directories /sw/data/vep/{87,89,91}. When module version vep/89 or vep/91 is loaded, the environment variable VEP_CACHE is set to the directory for the appropriate version.  Local caches for versions 82, 84 and 86 exist only for homo_sapiens.  To use the cached databases, run the script using the --cache option to indicate the use of a locally-cached database, and the --dir option to specify where this is:

    vep --cache --dir $VEP_CACHE  ...

If you are using vep/89, use:

    variant_effect_predictor.pl --cache --dir $VEP_CACHE  ...

All plugins are also available.  For more script options, see its online help page.
CDD - Position-Specific Scoring Matrices for CD-Search

The CDD database versions 3.14 and 3.16 are downloaded in their entirety and are available at /sw/data/cdd/{3.14,3.16}. These directories contains collections of position-specific scoring matrices (PSSMs) that have been created for the CD-Search service.

The PSSMs are meant to be used for compiling RPS-BLAST search databases,
which can be used with the standalone RPS-BLAST programs (rpsblast and rpsblastn).
These programs, as well as the makeprofiledb application
needed to convert files in this directory,
are part of the BLAST+ executables (available on Uppmax as part of `bioinfo-tools`,
e.g., module blast/2.2.31+).
The makeprofiledb application is described at [http://www.ncbi.nlm.nih.gov/books/NBK1763](http://www.ncbi.nlm.nih.gov/books/NBK1763).

More information is available in the CDD README either via FTP or its local copy /sw/data/cdd/README.
iGenomes - Collection of reference sequences and annotation files

A local copy of illumina's iGenomes collection of commonly analyzed organisms is available at /sw/data/igenomes. In addition to the annotations provided by the collection, Bismark and STAR indexes have been added.
UK Biobank institutional data set (GENETICS)

The UKBB data set is available for eligible projects in the system for sensitive research SNIC-SENS Bianca. If you believe you are eligible, contact Professor Tove Fall to gain access.

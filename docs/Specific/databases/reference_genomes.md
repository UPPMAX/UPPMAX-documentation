# Reference genomes

NOTE: The Illumina igenomes are also available at UPPMAX, with additional indices built for Bismarck and STAR.  The scripts used to build the additional indices are available at the UPPMAX/bio-data github repository.

Many next-generation sequencing applications involves alignment of the sequence reads to a reference genome. We store reference sequences in a directory that is accessible for all users in the system. The table below shows all currently available genomes.

Reference genome          |Assembly version
--------------------------|-----------------------
Homo sapiens              |Feb. 2009 (GRCh37/hg19)
Pan troglodytes           |Mar. 2006 (CGSC2.1/PanTro2)
Macaca mulatta            |Jan. 2006 (RheMac2)
Sus scrofa                |Apr. 2009 (Sscrofa9)
Canis familiaris          |Sep. 2011 (CanFam3)
Mus musculus              |July 2007 (NCBIM37/mm9), Jan. 2012 (GRCm38)
Gallus gallus             |May 2006 (WASHUC2/galGal3)
Taeniopygia guttata       |Mar. 2010 (TaeGut3.2.4)
Saccharomyces cerevisiae  |Mar 2010 (ScereEF2)
Equus caballus            |Sep. 2007 (EquCab2)
Pichia stipitis           |Picst3
Rattus norvegicus         |Nov. 2004 (RGSC3.4.61)
Schizosaccharomyces pombe |20090701

Directory structure

The data files are located at /sw/data/reference and the directory structure is e.g.: Homo_sapiens/GRCh37.

Each directory contains several subdirectories, explained below:

dna_ftp.ensembl.org_ contains the original data files from the ENSEMBL ftp server, and should not be modified.

chromosomes contains fasta files for individual chromosomes.

chromosomes_rm contains the same files, masked with RepeatMasker.

concat contains most of the fasta files in "chromosome" concatenated into a single fasta file. The exceptions are alternate contig files and DNA not mapped to any chromosome.

concat_rm contains most of the fasta files in "chromosome_rm" concatenated into a single fasta file. The exceptions are alternate contig files and DNA not mapped to any chromosome.

program_files contains index files and metadata for software packages used to work with reference genomes, e.g. SAMtools and aligners such as Bowtie, BWA.

Requests for additional reference genomes or software data/index files should be directed to UPPMAX support.

# Using CRAM to compress BAM files

## Introduction

### Biological data is being produced at a higher rate each day, and it is a challenge to store it all somewhere

The bioinformatics community is trying to keep up with the growing data amounts, and new file formats is part of this evolution. The BAM format was a huge success due to its ability to compress aligned reads by ~50-80% of their original size, but even that is not sustainable in the long run.

CRAM is a new program that can compress SAM/BAM files even more, which makes it suitable for long-term storage. We think this format will become more common, and that it will be supported by most tools, like the BAM format is today.

There are a couple of options you can give to CRAM that will make it behave differently. Even more about the different options on the developers homepage.

Lossless compression: When converting BAM -> CRAM -> BAM, the final BAM file will look identical to the initial BAM file.

Lossy compression: You can specify how to deal with the quality scores in a multitude of different way. To cite the creators of CRAM:

"Bam2Cram allows to specify lossy model via a string which can be composed of one or more words separated by '-'.
Each word is read or base selector and quality score treatment, which can be binning (Illumina 8 bins) or full scale (40 values).
Here are some examples:
N40-D8 - preserve quality scores for non-matching bases with full precision, and bin quality scores for positions flanking deletions.
m5 - preserve quality scores for reads with mapping quality score lower than 5
R40X10-N40 - preserve non-matching quality scores and those matching with coverage lower than 10
*8 - bin all quality scores

Selectors:
R - bases matching the reference sequence N aligned bases mismatching the reference, this only applies to 'M', '=' (EQ) or 'X' BAM cigar elements.
U - unmapped read
Pn - pileup: capture all bases at a given position on the reference if there are at least n mismatches D read positions flanking a deletion
Mn - reads with mapping quality score higher than n
mn - reads with mapping quality score lower than n
I - insertions
* - all

By default no quality scores will be preserved.

Illumina 8-binning scheme:
0, 1, 6, 6, 6, 6, 6, 6, 6, 6, 15, 15, 15, 15, 15, 15, 15, 15, 15,
15, 22, 22, 22, 22, 22, 27, 27, 27, 27, 27, 33, 33, 33, 33, 33, 37,
37, 37, 37, 37, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40"

[Illumina's white paper on the matter](../files/c_557912-l_1-k_whitepaper_datacompression.pdf)

## Compression rate

So, how much compression are we talking about here? Here are the results of a test with a 1.9 GB BAM file (7.4 GB SAM format).

CRAM COMPRESSION RATE

File format |File size (GB)
------------|--------------
SAM |7.4
BAM |1.9
CRAM lossless| 1.4
CRAM 8 bins| 0.8
CRAM no quality scores| 0.26

![Graph showing the content of the above table](../img/c_557912-l_1-k_cram_compression.png)

## Examples

### Lossless compression of a BAM file

Lossless compression means that the BAM file will be identical before and after compression/decompression The downside of this is that the produced CRAM file will be larger since if has to save each and every quality score. To make a lossless compression, use the following command (can also be written as a single line by removing the backslashes):

$ module load bioinfo-tools cramtools
$ java -jar $CRAM_HOME/cram.jar cram \
-I file.bam \
-O file.cram \
-R ref.fa \
--capture-all-tags \
--lossless-quality-score
The important parts here are:

-I which means the input file (name of the BAM file to be compressed).
-O which means the output file (name of the new compressed CRAM file).
-R which means the reference file (the FASTA reference to be used. Must be the same when decompressing).
--capture-all-tags which means that all the tags in the BAM file will be saved.
--lossless-quality-score which means the quality scores will be preserved.

CRAM assumed you have indexed your reference genome using e.g. samtools faidx, i.e. that you will have both ref.fa and ref.fa.fai (Note the index name: ref.fa.fai, NOT ref.fai)

To decompress the CRAM file to a BAM file again, use this command (can also be written as a single line by removing the backslashes):

```console
$ module load bioinfo-tools cramtools
$ java -jar $CRAM_HOME/cram.jar bam \
-I file.cram \
-O file.bam \
-R ref.fa
```

If you had NM or MD tags in your original BAM file, you have to specify that they should be added in the BAM file that is to be created by adding

```console
--calculate-md-tag
and/or
--calculate-nm-tag
```

to the command.

### Lossy compression of a BAM file

The motivation to use a lossy compression is that the compression ratio will be much larger, i.e. the cram file will be much smaller. The best compression ratio is reached, naturally, when the quality scores are removed all together. This does have an impact on future analysis such as SNP calling, so the trick is, as usual, to find a good balance.

Illumina has started with a practice called binning. That means that instead of having 40 unique quality scores, you put similar values into bins. Illumina thought 8 bins would get the job done, and that is what CRAM recommends. See this page's introduction for more details about the bins.

To compress your BAM file and binning the quality scores in the same way as Illumina, use this command (can also be written as a single line by removing the backslashes):

```console
$ module load bioinfo-tools cramtools
$ java -jar $CRAM_HOME/cram.jar cram \
-I file.bam \
-O file.cram \
-R ref.fa \
--capture-all-tags \
--lossy-quality-score-spec \*8
```

The important parts here are:

**-I** which means the input file (name of the BAM file to be compressed).
**-O** which means the output file (name of the new compressed BRAM file).
**-R** which means the reference file (the FASTA reference to be used. Must be the same when decompressing.).
**--capture-all-tags** which means that all the tags in the BAM file will be saved.
**--lossy-quality-score-spec \*8** which means the quality scores will be binned into 8 bins the Illumina way. (Notice that we need to apply a "\" before the "8" as your shell Bash will otherwise expand this expression if you'd happen to have any filenames ending with eights in the current directory.)

To decompress the CRAM file to a BAM file again, use this command (can also be written as a single line by removing the backslashes):

```console
$ module load bioinfo-tools cramtools
$ java -jar $CRAM_HOME/cram.jar bam \
-I file.cram \
-O file.bam \
-R ref.fa

```

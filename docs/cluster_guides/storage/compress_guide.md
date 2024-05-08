# Brief compression guide

To avoid filling up the storage at UPPMAX, we all users to do their part and store their files in a good way. The best way to store files is of course to delete everything you don't need anymore, like temporary and intermediate files. For everything else you need to keep, here are some useful commands to know (section about biological data below).

## General files
We have several compression programs installed and you are free to chose whichever you want (any better than none). Examples:

### gzip (fast, good compression)

gzip also has a parallel version (pigz) that will let the program use multiple cores, making it much faster. If you want to run multithreaded you should make a reservation in the queue system, as the login nodes will throttle your programs if they use too much resources.

```
# compress a file 
$ gzip file.txt            # single threaded
$ pigz -p 4 file.txt       # using 4 threads
# decompress a file
$ gunzip file.txt.gz       # single threaded
$ unpigz -p 4 file.txt     # using 4 threads (4 is max)
```

### bzip2 (slow, better compression)

bzip2 also has a parallel version (pbzip2) that will let the program use multiple cores, making it much faster. If you want to run multithreaded you should make a reservation in the queue system, as the login nodes will throttle your programs if they use too much resources.

```
# compress a file 
$ bzip2 file.txt            # single threaded
$ pbzip2 -p4 file.txt       # using 4 threads
# decompress a file
$ bunzip2 file.txt.gz       # single threaded
$ pbunzip2 -p4 file.txt.gz  # using 4 threads
```

### zstd (fast, better compression)

zstd has built in support for using multiple threads when compressing data only, making it much faster. If you want to run multithreaded you should make a reservation in the queue system, as the login nodes will throttle your programs if they use too much resources.

```
# compress a file 
$ zstd --rm file.txt        # single threaded
$ zstd --rm -T4 file.txt    # using 4 threads
# decompress a file, only single threaded
$ unzstd --rm file.txt.zst
```

## Compressing lots of files
The commands above work on a single file at a time, and if you have 1000s of files it is quite boring to go through them manually. If you want to combine all the files into a single compressed archive, you can use a program named tar.

```
# to compress a folder (folder/)
# and all files/folder inside it, 
# creating a archive file named files.tar.gz
$ tar -czvf files.tar.gz folder/
# to decompress the archive later
$ tar -xzvf files.tar.gz
```

If you don't want to combine them in a single file, and instead compress them one by one, you can use the command find.

```
# to find all files with a name ending
# with .fq and compress them
$ find /path/to/search/in -iname *.fq -print -exec gzip "{}" \;
# example to compress all FastQ file in
# the current directory and all its
# subdirectories, using 4 threads
$ find . \( -iname '*.fq' -o -iname '*.fastq' \) -print -exec pigz -p 4 "{}" \;
# same as above, but starting 4 single
# threaded instances of gzip in parallel
$ find . \( -iname '*.fq' -o -iname '*.fastq' \) -print0 | xargs -0 -P 4 gzip
```

## Biological data
There are some compression algorithms that have become standard practice to use in the realm of biological data. Most programs can read the compressed versions of files as long as it's compressed with the correct program. Leaving out the decompression commands, mostly because they are already described in the General files section about, but also because there is little reason to ever decompress biological data.

### fastq files

```
# compress sample.fq 
$ gzip sample.fq        # single threaded
$ pigz -p 4 sample.fq   # using 4 threads
```

### sam files

```
# load samtools
$ module load bioinfo-tools samtools
# compress sample.sam, but remember to delete
# sample.sam when finished, since samtools
# will not do that automatically
# single threaded
$ samtools view -b -o sample.bam sample.sam
# using 4 threads
$ samtools view -@ 4 -b -o sample.bam sample.sam
```

### vcf / g.vcf files

```
# load htslib
$ module load bioinfo-tools htslib
# compress sample.vcf / sample.g.vcf
$ bgzip sample.vcf         # single threaded
$ bgzip -@ 4 sample.vcf    # using 4 threads
# index sample.vcf.gz / sample.g.vcf.gz 
$ tabix sample.vcf.gz
```

## Programs that don't read compressed files
There are clever ways to get around programs that don't support reading compressed files. Let's say you have a program that only reads plain text files. You can use something called process substitution (also known as anonymous named pipes) to be able to decompress the data on-the-fly while feeding it to the program.

### How you normally would run the program

```
# run the program with uncompressed file
$ the_program uncompressed.txt
# now, let's compress the file first and run
# the program using process substitution
# to decompress the file
$ gzip uncompressed.txt
# run the program using the compressed file
# (zcat works like cat, but read gzipped files)
$ the_program <(zcat compressed.txt.gz)
# same as above, but reading a
# bzip2 compressed file
$ the_program <(bzcat compressed.txt.gz)
# same as above, but reading a
# zstd compressed file
$ the_program <(zstdcat compressed.txt.gz)
```

In this example we give the program not the name of a file to read, but instead we use process substitution to run zcat and feed the uncompressed data to the program, as if it was reading a file.

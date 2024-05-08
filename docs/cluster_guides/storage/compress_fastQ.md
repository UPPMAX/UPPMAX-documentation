# How should I compress FastQ-format files?

**Short answer: The best compression using a widely available format is provided by bzip2 and its parallel equivalent pbzip2. The best compression ratio for FastQ is provided by fqz_comp in the fqzcomp/4.6 module.  However, this tool is experimental and is not recommended for general, everyday use.**

## Long answer
We conducted an informal examination of two specialty FastQ compression tools by recompressing an existing fastq.gz file. The first tool fqzcomp (available in the module fqzcomp/4.6) uses a compiled executable (fqz_comp) that works similar to e.g., gzip, while the second tool (LFQC in the module lfqc/1.1) uses separate ruby-language scripts for compression (lfqc.rb) and decompression (lfqcd.rb). It does not appear the LFQC scripts accept piping but the documentation is limited.

```
module load bioinfo-tools
module load fqzcomp/4.6
module load lfqc/1.1
```

Both modules have 'module help' available for more info. The help for fqzcomp gives the location of their README which is very helpful in describing minor changes that might occur to the FastQ file during decompression (these do not affect the read name, sequence or quality data).

One thing changed from the 'standard' implementation of LFQC was to make the scripts stand-alone with #! header lines, rather than requiring e.g., 'ruby lfqc.rb ...' as you see in their documentation.

Since piping is not available with LFQC, it is preferable to avoid creating a large intermediate decompressed FastQ file. So, create a named pipe using mkfifo that is named like a fastq file.

```
mkfifo UME_081102_P05_WF03.se.fastq
zcat UME_081102_P05_WF03.se.fastq.gz > UME_081102_P05_WF03.se.fastq &
lfqc.rb UME_081102_P05_WF03.se.fastq
rm UME_081102_P05_WF03.se.fastq
```

This took a long time, 310 wall seconds.

Next,fqz_comp from fqzcomp/4.6. Since this works like gzip, just use it in a pipe.

```
zcat UME_081102_P05_WF03.se.fastq.gz | fqz_comp > UME_081102_P05_WF03.se.fastq.fqz
```

This used a little multithreading (up to about 150% CPU) and was much faster than LFQC, just 2-3 seconds. There are other compression options (we tried -s1 and -s9+) but these did not outperform the default (equivalent to -s3). This is not necessarily a surprise; stronger compression means attempting to make better guesses and sometimes these guesses are not correct. No speedup/slowdown was noticed with other settings but the input file was relatively small.

```
-rw-rw-r-- 1 28635466 Mar 10 12:53 UME_081102_P05_WF03.se.fastq.fqz1
-rw-rw-r-- 1 29271063 Mar 10 12:52 UME_081102_P05_WF03.se.fastq.fqz9+
-rw-rw-r-- 1 46156932 Jun 6   2015 UME_081102_P05_WF03.se.fastq.gz
-rw-rw-r-- 1 28015892 Mar 10 12:53 UME_081102_P05_WF03.se.fastq.fqz
-rw-rw-r-- 1 24975360 Mar 10 12:45 UME_081102_P05_WF03.se.fastq.lfqc
```

We also compared against bzip2 and xz, which are general-use compressors. These both function like gzip (and thus like fqz_comp) and both outperform gzip, as expected. xz is becoming a more widely-used general compressor like bzip2, but for this file it required perhaps 20x as much time as bzip2 and did worse.

```
-rw-rw-r-- 1 35664555 Mar 10 13:10 UME_081102_P05_WF03.se.fastq.bz2
-rw-rw-r-- 1 36315260 Mar 10 13:10 UME_081102_P05_WF03.se.fastq.xz
```

Neither of these improved general-use compressors did as well with FastQ as the specialty compressors. This makes sense given the specialty compressors can take advantages of the restrictions of the format.


### Which is the best method in this trial?
From the results of this trial, the tool that provides the best compression ratio in a reasonable amount of time is fqz_comp in the fqzcomp/4.6 module. It is as fast as bzip2 which is also much better than gzip but does a much better job of compressing FastQ.  However, fqz_comp is experimental so we do not recommend using fqz_comp for everyday use.  We recommend using bzip2 or its parallel equivalent, pbzip2.

The fqz_comp executable could be used to decompress FastQ within a named pipe if FastQ is required for input:

```
... <(fqz_comp -d < file.fastq.fqz) ...
```

Note that fqz_comp is designed to compress FastQ files alone, and neither method here provides the blocked compression format suitable for random access that bgzip does; see [which-compression-format-should-i-use-for-ngs-related-files](../storage/compress_format.md) for more on that subject.


### Why not LFQC?
Though LFQC has the best compression of FastQ, there are some strong disadvantages. First, it takes quite a long time, perhaps 50x longer than fqz_comp. Second, it apparently cannot be used easily within a pipe like many other compressors. Third, it contains multiple scripts with multiple auxiliary programs, rather than a single executable. Fourth, it is quite verbose during operation, which can be helpful but cannot be turned off. Finally, it was difficult to track down for installation; two different links were provided in the publications and neither worked. It was finally found in a github repository, the location of which is provided in the module help.

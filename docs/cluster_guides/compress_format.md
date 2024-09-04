# Which compression format should I use for NGS-related files?

How well things compress will vary a great deal with the input data. An additional consideration is how useful the compressed format will be to you later. Some tools can handle only one compressed format (almost always gzip) and some can handle two (almost always gzip and bzip2). The help information for the tool should be explicit about which formats it understands. You can also use named pipes or the bash <() syntax to uncompress files 'on the fly' if the tool you are using cannot handle that compressed format.

Another consideration for usefulness is the structure
of the specific compressed format.
By default gzip is not 'blocked';
the compression is applied continually across the entire file,
and to uncompress something in the middle
it is necessary to uncompress everything up to that point.
Tools that understand compressed VCF and GFF files
require these to be compressed with **bgzip** (available as part of the **htslib** module), which applies blocked gzip compression, so that it is possible to uncompress interior chunks of the files efficiently. This is useful when viewing compressed VCF/GFF files in a viewer such as IGV, for example. For viewing, such files also need an index created, which is accomplished using **tabix** (also part of the **htslib** module), which understands bgzip-compressed files. BAM files also use a type of gzip compression that is blocked. Files compressed with bgzip can be uncompressed with gzip.

Bzip2 is inherently blocked. Bzip2 is a more efficient compression method than gzip, but takes perhaps twice as long or longer to compress the same file. Fortunately, another advantage of blocked compression is that multiple parts of the file can be compressed at once. Uppmax has **pbzip2** available as a system tool, which can perform parallel compression and decompression of bzip2-format files using multiple threads. This is quite fast. Do 'pbzip2 -h' for help. An Uppmax user has provided a helpful SBATCH script.

Another disadvantage of compression formats that are not blocked is that an error in a file generally screws up the remainder of the file. Files with blocked compression can recover all non-error-containing blocks.

Other compressed formats are available, including 7z, available by loading the **p7zip** module, and xz, available as the system tool xz and by loading the **liblzma** module. For compressing FastQ files in particular, which have a very strict format, our small-scale comparison of tools showed that xz was slightly inferior to bzip2 and much slower during compression, and specialty tools for FastQ compression were superior in compression ratios to general-purpose compressors. See [How Should I Compress FastQ-format Files?](compress_fastQ.md) for more on FastQ compression.

Most compression tools have options that allow you to trade off between speed of compression and size reduction of compression. The defaults are almost always sufficient.

It makes little sense to compress an already-compressed file with a different format. It is much better to set up a pipe to uncompress the file and then recompress in the new format.

Apart from compression dictated by file usage (see above), it is recommended that files that are being compressed for long-term storage (e.g., raw sequence data) are compressed using pbzip2. If the files are already compressed in long-term storage (e.g. SweStore) I don't think it is worthwhile to retrieve the files, decompress-recompress them, then reupload them.

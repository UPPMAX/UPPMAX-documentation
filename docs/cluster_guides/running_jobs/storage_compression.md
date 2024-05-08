# Storage and compression

## Storage

[Disk storage guide](../storage/disk_storage_guide.md)

???- question "How does automatic backup of project areas work at UPPMAX?"

    [Backup](../backup.md)
    
???- question "What is this 'glob' folder in my home folder?"

    - The glob directory found in your home has been deprecated since early 2017. 
    - It is now a normal directory and shared your default 32GByte sized home. 
    - The glob directory remains to not interfere with scripts who might reference ~/glob in the source code.

    - Historically, the glob directory was the main storage area for storage of user data. 
        - It was shared by all nodes. 
        - The directory was used for files needed by all job instances and could house files exceeding the quota of the home directory. 
        - Job input and output files was (and can still be) stored here.

    - You might also be interested in our [disk storage guide](../storage/disk_storage_guide.md).


## Compression
???- question "File compression guide"

    [Compression guide](../storage/compress_guide.md)

???- question "How can I compress my files as quickly and efficiently as possible?"

    - You can use this [SBATCH script](https://github.com/brainstorm/scilifelab/blob/master/scripts/sbatch/compress_pbzip2.sh) [1] to run the compression in parallel as a node job, with a parallel version of the highly efficient bzip2 compression software.

    - Remember to modify the appropriate #SBATCH parameters at the top of the file, according to your project, and the estimated time to compress your files.

    - [1] Thanks Roman Valls Guimera, for contributing this script.

???- question "How should I compress FastQ-format files?"

     [Compress FastQ](../storage/compress_fastQ.md)

???- question "Which compression format should I use for NGS-related files (FastQ, Fasta, VCF, GFF, etc.)?"

     [Compression format](../storage/compress_format.md)

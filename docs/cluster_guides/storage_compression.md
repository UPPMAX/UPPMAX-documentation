---
tags:
  - storage
  - compression
---

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

???- question "Disk quota exceeded when copying data"

    The problem is that if you have data in a project directory,
    e.g. `/proj/snic2017-1-999`, and are copying the data to another project directory,
    e.g. `/proj/uppstore2017-999`, then you may get a "disk quota exceeded" error.

    This happens when your (snic2017-1-999) project quota is almost full and you're copying the data without changing the group ownership of the files. Even though the destination folder is owned by a project with sufficient quota, the files will for a short time be owned by the original project. By copying the files, the earlier project's disk usage is increased and the quota is exceeded.

    The solution is one of these options:

    1. Use `mv` instead of `cp`
    2. Give the flag `--no-g` to `rsync` to set the group ownership of the destination files to that of the destination directory
    3. Use `newgroup [the-group-i-want]` to change the group ownership of the files first, then ``rsync -rlpt /old-location /new-location``

    Explanation:

        `-r` is for recursive
        `-l` is to preserve links
        `-p` is to preserve permissions
        `-t` is to preserve times

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

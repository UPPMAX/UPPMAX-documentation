# Storage and compression

## Storage
???- question "How does automatic backup of project areas work at UPPMAX?"

    [Backup](../backup.md)
    
???- question "What is this 'glob' folder in my home folder?"

    The glob directory found in your home has been deprecated since early 2017. It is now a normal directory and shared your default 32GByte sized home. The glob directory remains to not interfere with scripts who might reference ~/glob in the source code.

    Historically, the glob directory was the main storage area for storage of user data. It was shared by all nodes. The directory was used for files needed by all job instances and could house files exceeding the quota of the home directory. Job input and output files was (and can still be) stored here.

    You might also be interested in our disk storage guide at http://www.uppmax.uu.se/support/user-guides/disk-storage-guide/.


## Compression
???- question "File compression guide"

???- question "How can I compress my files as quickly and efficiently as possible?"

???- question "How should I compress FastQ-format files?"

???- question "Which compression format should I use for NGS-related files (FastQ, Fasta, VCF, GFF, etc.)?"


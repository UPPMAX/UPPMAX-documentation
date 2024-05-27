# Manage you projects


## CPU hours


## Storage

- [Disk storage guide](storage/disk_storage_guide.md)
- [Backup](backup.md)

???- question "What is this 'glob' folder in my home folder?"

    - The glob directory found in your home has been deprecated since early 2017.
    - It is now a normal directory and shared your default 32GByte sized home.
    - The glob directory remains to not interfere with scripts who might reference ~/glob in the source code.

    - Historically, the glob directory was the main storage area for storage of user data.
        - It was shared by all nodes.
        - The directory was used for files needed by all job instances and could house files exceeding the quota of the home directory.
        - Job input and output files was (and can still be) stored here.

 - [Display the disk quota on the more detailed level](storage/disk_quota_more.md)       

## Members

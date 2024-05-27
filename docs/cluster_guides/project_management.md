# Manage you projects


## CPU hours


## Storage

- [Disk storage guide](storage/disk_storage_guide.md)
- [Backup](backup.md)

### Display storage quota

- Display your project quota with the command:

```console
$ uquota
```
- Usage

```bash
usage: uquota [-h] [-q] [-d] [-u USER] [-p PROJECTS_FILE] [--include-expired]
              [--random-usage] [--only-expired] [--sort-by-col SORT_BY_COL]
              [-s] [-f]

optional arguments:
  -h, --help            Ask for help
  -q, --quiet           Quiet, abbreviated output
  -d, --debug           Include debug output
  -u USER, --user USER
  -p PROJECTS_FILE, --projects-file PROJECTS_FILE
  --include-expired     Include expired projects
  --random-usage        removed option, don't use
  --only-expired        Only show expired projects
  --sort-by-col SORT_BY_COL
                        Index (0-4) of column to sort by. Default is 0.
  -s, --slow            Deprecated. Previously ran 'du' command
```


- [Display the disk quota on the more detailed level](storage/disk_quota_more.md)

 - ???- question "What is this 'glob' folder in my home folder?"

    - The glob directory found in your home has been deprecated since early 2017.
    - It is now a normal directory and shared your default 32GByte sized home.
    - The glob directory remains to not interfere with scripts who might reference ~/glob in the source code.

    - Historically, the glob directory was the main storage area for storage of user data.
        - It was shared by all nodes.
        - The directory was used for files needed by all job instances and could house files exceeding the quota of the home directory.
        - Job input and output files was (and can still be) stored here.



## Members

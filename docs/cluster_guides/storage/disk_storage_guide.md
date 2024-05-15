# Disk storage guide

## Quota

Users have access to shared network storage on various cluster file systems. This mean that whenever you are logged in to a login server or if you are running on a compute node you will have the same view of the storage.

There are several different classes of disk storage available with different policies for usage, limits and backup:

The user home file system
Local scratch file systems
The network project and nobackup file system
Temporary virtual filesystem
Users have access to shared network storage on various cluster file systems, and backup home directories and some project storages to tape.

### If you need more quota

If more quota is needed, contact support (`support@uppmax.uu.se`) for advice. The uquota command is used to check current disk usage and limits. This command is available in the 'uppmax' module, which is loaded by default.

We do not extend quotas for home directories or SNIC project directories, but it's possible to apply for storage projects.

Before contacting support, clean out unnecessary data and make an inventory of the data in your project (what type of data, how big, why it's needed). Here are two commands. The first results in a list of subdirectories ordered by size and proportion of total size. The second produces a list of the files in the current directory that take up most space. These may take a long time to complete, use 'ctrl-c' to cancel execution if you change your mind:

du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}'
find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn

### If you need even more quota for archiving

Please contact UPPMAX support at `support@uppmax.uu.se`.
We have a previously been able to provide users with a low-cost moderate performant storage solution for a cost of 500SEK/TB/year, for a commitment of four years and 50TB.

### Environmental variables

We have defines several environment variables to help our users. They are:

$HOME (or $SNIC_BACKUP) is a traditional one, pointing to the users home directory.
$TMPDIR or ($SNIC_TMP) points to node-local storage, suitable for temporary files that can be deleted when the job finishes
$SNIC_NOBACKUP points to an UPPMAX-wide storage suitable for temporary files (not deleted when the job is finished)

## Types of storage

### User Home directories

Paths: $HOME or $SNIC_BACKUP

Permanent storage of users files during the lifetime of the accounts. Shared access on all cluster nodes. Snapshots are normally enabled on this file system, and you can access the snapshots in every directory by 'ls .snapshot' or 'cd .snapshot'. The quota is 32GB per user. We provide backup of this volume, and we keep the files on tape up to 90 days after they are deleted from disk. If you have files you do not want to back up place them in a folder called 'nobackup'.

We recommend you do not use your home directory for running jobs. Our general recommendation is to keep everything related to a specific research project in its project directory.

### Local Scratch

Paths: $TMPDIR or $SNIC_TMP

Each node has a /scratch volume for local access providing the most efficient disk storage for temporary files. Users have read/write access to this file system. SLURM defines the environment variable TMPDIR which you may use in job scripts. On clusters with SLURM you may use /scratch/$SLURM_JOB_ID. This area is for local access only, and is not directly reachable from other nodes or from the front node. There is no backup of the data and the lifetime of any file created is limited to the current user session or batch job. Files are automatically erased when space is needed by other users.

### Projects global (network) storage

Paths: /proj/[proj-id]

The project global storage is permanent storage of project's files during the lifetime of the project. Disk quota on this volume is shared by all project members. Default quota allocation is determined by your project type.

Note that the quota system on crex is built on group ownership for files/directories. This means that moving files between project directories does not directly affect quota. We have scripts and other tricks that tries to ensure the correct group is always used, but  in general this may lag quite some time - it takes a while to go through everything, especially since we don't want to affect performance. To make sure quota information is correct, you can change the group to the correct one after moving directories:

chgrp -R PROJECT_YOU_MOVED_TO PATH_OF_THE_MOVED_DIRECTORY

if you don't do this, it will still be fixed, but it may take a while.

The files are backed up to tape and we keep the files for 30 days after they are deleted from disk. In the project folder you should keep all your raw data and important scripts.

On Bianca and in SLLStore and UppStore projects, all temporary files, and files that can be regenerated (e.g.. data created from your computations), should be moved to the nobackup folder.

More information about backup at UPPMAX.

### Temporary virtual filesystem

Paths: /dev/shm/[job-id]

On all our clusters we have a temporary virtual filesystem implemented as a shared memory area. I.e. it uses primarily the RAM for storage (until it eventually might have to swap out to physical disk), and can be accessed via the path /dev/shm/[job-id].

In some situations this "disk" area can be quicker to read/write to, but depending on the circumstances it can also be slower than local scratch disk. Also note that it is a shared resource among all running jobs on a specific node, so depending on the node and how much memory your job has been allocated, the amount of data you can write will vary.

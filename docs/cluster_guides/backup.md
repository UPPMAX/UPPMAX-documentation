# How does backup at UPPMAX work?

**Backup of data is especially important to data-driven science. This page provides the ins and outs of how backup works on UPPMAX storage systems.**

As PI, you and your academic institution are ultimately responsible for your data. We recommend you maintain a primary copy of your data on a system you control, when possible. At the very least, double-check that your collaborators are taking care of your data in a responsible way.

While UPPMAX systems may have backup, these are not designed to act as the sole repository of primary data, e.g. raw data or originals.

## What does "backup" mean for my data?

The type of backup that is generally available for project storage at UPPMAX is incremental backup with 30 day retention. This means that any file that was deleted more than 30 days ago is irretrievably gone. Changes in a file are kept for 30 days, so we can potentially retrieve an old version up to a month after you edited it.

The backup service tries to backup all changes as often as they occur, but rapid changes will not register. Due to the large amounts of files in the file systems, a single backup session may take upwards of a week or more. This means that if you create a file and delete it the next day, it will probably not be backed up.

Backups are sent off-site to either KTH or LiU, depending on the storage system.

To ensure timely backups, it is very important to reduce the workload of the backup system as much as possible. Create directories with "nobackup" in their name or use the pre-existing nobackup directory in /proj/XYZ to store data that does not need backup.

- It is especially important that temporary files and files that are changed often are placed in nobackup directories.

## Which directories are backed up?

Backup is done on:

- Home directories (on Rackham these also have snapshots)
- All of Bianca (projects named sensYYYYXXX), except in folders named "nobackup"
- SciLifeLab Storage projects (named sllstoreYYYYXXX), except in folders named "nobackup"
- UPPMAX Storage projects (uppstore20YYXXX) except in folders named "nobackup"
- UPPMAX Offload Storager projects (uppoff20YYXXX)
- SNIC projects (named snicYYYY-X-ZZZZ)

# What should I put in directories with backup?

- In short, irreplaceable data should be placed there. This includes especially raw sequencing data and any other data that cannot be recreated by any effort. Scripts and other files that are needed to reproduce or repeat the analyses should also be placed on backup.

## What should I not put in directories with backup?

- Directories where you are actively working, especially if you are creating or modifying many files.
  The backup mechanisms cannot keep up with large amounts of files changing on a rapid basis.

## How robust is uppmax storage?

- All UPPMAX storage systems use RAID technology to make storage more robust through redundancy.
- This means that two or more disks must fail in the same "RAID volume" before there is a risk of data loss.

- However, this technology does not protect against user error (e.g. "rm -rf * in your project directory) or in case of a significant disaster (e.g. fire in computer hall).
- Off-site backup is crucial.

## How can I access my backups?

You must contact UPPMAX support and ask for help. Provide as much information as possible, especially directory and file names.

## What about "snapshots"?

- In addition to the regular backup service, the home directories on Rackham have a feature called "snapshots".
- Snapshot makes a frozen "picture" of some file structure as it looks at the time the snapshot was taken.
- This allows you to restore a particular file as it was at some time point.
- Snapshots reside on the same storage system as the original data — when the storage system fails catastrophically then the snapshots are gone as well.
- Snapshots are taken on regular basis and only available for home directories.

- You can easily access snapshots in every directory by 'ls .snapshot' or 'cd .snapshot' in a terminal. The '.snapshot' is a hidden directory.

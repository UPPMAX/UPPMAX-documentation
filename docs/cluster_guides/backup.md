---
tags:
  - backup
  - back-up
  - back up
---

# Backup

A backup allows one to restore his/her data
after it has been (accidentally) lost.

This page describes how UPPMAX does backups.

While UPPMAX systems may have backup,
these are not designed to act as the sole repository of primary data,
e.g. raw data or originals.

!!! warning "The PI is the main responsible person"

    A PI and his/her academic institution are ultimately responsible
    for his/her data.

    We recommend PIs to maintain a primary copy of their data on a system
    they control, when possible. 

    If not, ensure that 
    collaborators can only use the data in a responsible way.
    See [the best practices on an UPPMAX filesystem](uppmax_filesystem.md#best-practices)

## What does "backup" mean for my data?

The type of backup that is generally available for project storage at UPPMAX
is incremental backup with 30 day retention.
This means that any file that was deleted
more than 30 days ago is irretrievably gone.
Changes in a file are kept for 30 days,
so we can potentially retrieve an old version up to a month after you edited it.

The backup service tries to backup all changes as often as they occur,
but rapid changes will not register.
Due to the large amounts of files in the file systems,
a single backup session may take upwards of a week or more.
This means that if you create a file and delete it the next day,
it will probably not be backed up.

To ensure timely backups, it is important to reduce the workload
of the backup system as much as possible.
Create directories with `nobackup` in their name
or use the pre-existing `nobackup` directory in project folders
to store data that does not need backup.
It is especially important that temporary files and files that are changed
often are placed in `nobackup` directories.

## Which directories are backed up?

Backup is done on:

Folder                 |Example                |Description           |Exceptions?
-----------------------|-----------------------|----------------------|------------------------
`/home/[username]`     |`/home/sven`           |Your home folder      |Folders named `nobackup`
`/proj/sensYYYYXXX`    |`/proj/sens2016001`    |Sensitive data project|Folders named `nobackup`
`/proj/sllstoreYYYYXXX`|`/proj/sllstore2017096`|SciLifeLab Storage    |Folders named `nobackup`
`/proj/uppoff20YYXXX`  |`/proj/uppoff2021003`  |UPPMAX offload storage|Folders named `nobackup`
`/proj/snicYYYY-X-ZZZZ`|`/proj/snic2022-6-85`  |SNIC projects         |Folders named `nobackup`

## What should I put in directories with backup?

Irreplaceable data that you are not actively working on.

???- question "What are examples of irreplacable data?"

    Examples of irreplaceable data are:

    - Raw/unprocessed measurements, which cannot be reproduced from
      a script
    - Scripts for your analysis

???- question "Why should I not work actively on my data in a regular folder?"

    The backup mechanisms cannot keep up with large amounts
    of files changing on a rapid basis.

## What should I put in directories without backup?

Reproducible/intermediate data that you are actively working on.

The backup mechanisms cannot keep up
with large amounts of files changing on a rapid basis.

## How robust is UPPMAX storage?

The hardware setup of UPPMAX storage is robust
and unlikely to be the cause of lost data.

???- question "How is the hardware set up?"

    All UPPMAX storage systems use RAID technology
    to make storage more robust through redundancy.

    This means that two or more disks must fail in the same 'RAID volume'
    before there is a risk of data loss, which has a rather low chance.

    Still, this does not protect against disasters, e.g.
    a fire in the computer hall.

    To take this into account, backups are sent off-site
    to either KTH or LiU, depending on the storage system.

This setup, however, does not protect against user error
(e.g. removing all files in your project directory).

## How can I access my backups?

You must contact UPPMAX support and ask for help.
Provide as much information as possible, especially directory and file names.

## What about "snapshots"?

- In addition to the regular backup service, the home directories on Rackham have a feature called "snapshots".
- Snapshot makes a frozen "picture" of some file structure as it looks at the time the snapshot was taken.
- This allows you to restore a particular file as it was at some time point.
- Snapshots reside on the same storage system as the original data — when the storage system fails catastrophically then the snapshots are gone as well.
- Snapshots are taken on regular basis and only available for home directories.

- You can easily access snapshots in every directory by 'ls .snapshot' or 'cd .snapshot' in a [terminal](../software/terminal.md). The '.snapshot' is a hidden directory.

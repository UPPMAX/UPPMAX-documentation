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

## How can I access my backups?

[Contact UPPMAX support](../support.md) and ask for help.
Provide as much information as possible, especially directory and file names.

## What is the UPPMAX backup procedure?

UPPMAX performs an incremental backup with **30** day retention.

This means:

- After 30 days: your data is irretrievably gone
- Until 30 days: you can get your data back. If you've edited data,
  there is change you may be able to retrieve the newest version

???- question "What determines if a newly-edited file gets a backup?"

    - The duration of the change persisting.
      For example, a file that is created and deleted
      within a day is unlikely to get a backup.
      The longer the change persisted,
      the likelier it is to have
      its latest version in the backup
    - The workload of the backup service is low.
      The lower the workload of the backup service,
      the likelier it is you have more recent versions of your files
      in a backup

The backup service works best when it can keep up with the changes
on files that have a backup.

One important way to help work the backup service,
is to put intermediate/temporary data in a directory with `nobackup`
in its name.

These folders have such a backup:

Folder                 |Example                |Description           |Exceptions
-----------------------|-----------------------|----------------------|------------------------
`/home/[username]`     |`/home/sven`           |Your home folder      |Folders named `nobackup`
`/proj/sensYYYYXXX`    |`/proj/sens2016001`    |Sensitive data project|Folders named `nobackup`
`/proj/sllstoreYYYYXXX`|`/proj/sllstore2017096`|SciLifeLab Storage    |Folders named `nobackup`
`/proj/uppoff20YYXXX`  |`/proj/uppoff2021003`  |UPPMAX offload storage|Folders named `nobackup`
`/proj/snicYYYY-X-ZZZZ`|`/proj/snic2022-6-85`  |SNIC projects         |Folders named `nobackup`

Additionally, your home folder has snapshots taken,
which take place more often and can be recoved yourself.
See [the UPPMAX documentation on snapshots](snapshots.md).

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

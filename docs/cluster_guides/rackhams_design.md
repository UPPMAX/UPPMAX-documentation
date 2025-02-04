# Rackham's design

[Rackham](rackham.md) is an (general-purpose) high-performance computing (HPC) cluster.

???- question "What is an HPC cluster?"

    What an HPC cluster is, is described [here](uppmax_cluster.md).

Or: Rackham is a group of computers that can effectively run many calculations,
as requested by multiple people, at the same time.
Rackham runs the Linux operating system and all users need some
basic Linux knowledge to use Rackham.

???- tip "Using Linux"

    Using Linux (and especially the so-called command-line/[terminal](../software/terminal.md)) is essential
    to use Rackham. Learning the essential Linux commands
    is described [here](../getting_started/linux.md).

## Folder structure

These are the most important folders on Rackham:

General name                   |Example name                     |Description                                  |Purpose
-------------------------------|---------------------------------|---------------------------------------------|---------------------------------------
`/home/[username]`             |`/home/sven`                     |Your home folder                             |Small/general/personal things
`/proj/[project_name]`         |`/proj/uppmax2025-2-262`         |Your project folder                          |Work on your project here
`/proj/[project_name]/nobackup`|`/proj/uppmax2025-2-262/nobackup`|The folder of your project thas has no backup|Folder for intermediate/temporary files

To be able to retrieve (accidentally) lost files,
Rackham has [backups](backup.md) and [snapshots](snapshot.md).

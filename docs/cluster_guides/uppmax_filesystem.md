---
tags:
  - filesystem
  - file system
  - UPPMAX
---

# UPPMAX filesystem

One can store files on the UPPMAX clusters.

Here we show some common directories
and best practices.

Directory name|Description
--------------|---------------------------
`backup`      |A folder that is guaranteed to have a backup for 30 days
Home folder   |Your home folder, `/home/[username]`, e.g. `/home/sven`
`nobackup`    |A folder without a backup
Project folder|Your project folder, `/proj/[project_name]`, e.g. `/proj/snic2021-22-780`
Wharf         |A Bianca-only folder for file transfer

Some folders do and some do not have a [backup](backup.md).
See [the UPPMAX documentation on 'backup'](backup.md) for details.

## Best practices

???- question "Are there any horror story on this?"

    Yes, ask the UPPMAX staff :-)

1. Keep an inventory of important data and make a plan
   for how it should be treated. Inform collaborators of this plan.
1. Make sure you keep a separate copy of the most important data.
1. Put important data in a backed up directory
   (and nothing else, so that the backup system does
   not get bogged down with junk).
1. Run `chmod -R -w .` on directories containing critical
   data that should be preserved.

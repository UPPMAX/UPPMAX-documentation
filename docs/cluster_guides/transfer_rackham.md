---
tags:
  - Rackham
  - file
  - transfer
  - data
---

# File transfer to/from Rackham

There are multiple ways to transfer files to/from Rackham:

Method                                                        |Features
--------------------------------------------------------------|---------------------------------------------
[Using a graphical program](#using-a-graphical-program)       |Graphical interface, intuitive, for small amounts of data only
[Using rsync](#using-rsync)                                   |Terminal, easy to learn, can be used in scripts, efficient for backups
[Using SCP](#using-scp)                                       |Terminal, easy to learn, can be used in scripts
[Using SFTP](#using-sftp)                                     |Terminal, easy to learn, secure

Each of these methods is discussed below.

## Using a graphical program

One can transfer files to/from Rackham using a graphical program.
A graphical interface is intuitive to most users.
However, it can be used for small amounts of data only
and whatever you do cannot be automated.

See [Rackham file transfer using a graphical program](rackham_file_transfer_using_gui.md)
for a step-by-step guide how to transfer files using
a graphical tool.

## Using `rsync`

One can transfer files to/from Rackham
using [rsync](../software/rsync.md)
in a [terminal](../software/terminal.md).
This works similar to a regular copy of files,
except that a remote (instead of a local) address needs to be specified.
`rsync` can be used in scripts for regular file transfer.
However, `rsync` shines by providing a so-called 'delta' file transfer:
when you transfer files twice, `rsync` will only transfer the files that have
changed. This is ideal for backups.

See [Rackham file transfer using rsync](../software/rackham_file_transfer_using_rsync.md)
for a step-by-step guide how to transfer files using `rsync`.

## Using SCP

One can transfer files to/from Rackham
using SCP in a [terminal](../software/terminal.md).
This works similar to a regular copy of files,
except that a remote address needs to be specified.
The advantage of SCP is that is can be used in scripts.

See [Rackham file transfer using SCP](../software/rackham_file_transfer_using_scp.md)
for a step-by-step guide how to transfer files using SCP.

## Using SFTP

One can transfer files to/from Rackham using SFTP in a [terminal](../software/terminal.md).
One connects a local and a remote folder,
after which one can upload and download files.
SFTP is considered a secure file transfer protocol.

See [Rackham file transfer using SFTP](../software/rackham_file_transfer_using_sftp.md)
for a step-by-step guide how to transfer files using SFTP.

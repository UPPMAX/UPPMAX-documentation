# `rsync` on Rackham

[`rsync`](../software/rsync.md) is a command-line tool for [file transfer](../cluster_guides/file_transfer.md).

This page describes how to use [`rsync`](../software/rsync.md) on [Rackham](rackham.md).

## Copy a folder from local to Rackham

```mermaid
flowchart LR
  local_computer[Your local computer\nRun rsync from here]
  rackham[Rackham]

  local_computer --> |rsync| rackham
```

Copy a folder from a local computer to a Rackham home folder.

On your local computer, do:

```
rsync --recursive [folder_name] [user_name]@rackham.uppmax.uu.se:/home/[user_name]/
```

For example:

```
rsync --recursive my_folder sven@rackham.uppmax.uu.se:/home/sven/
```

The `--recursive` flag is used to
copy a folder and all of its subfolders.

## Copy a folder from Rackham to local

```mermaid
flowchart LR
  local_computer[Your local computer\nRun rsync from here]
  rackham[Rackham]

  rackham --> |rsync| local_computer
```

Copy a folder from Rackham
to your local computer.

On your local computer, do:

```
rsync --recursive [user_name]@rackham.uppmax.uu.se:/home/[user_name]/[folder_name] [local_folder_destination]
```

For example:

```
rsync --recursive sven@rackham.uppmax.uu.se:/home/sven/my_folder .
```

Where `.` means 'the folder where I am now'.

## Links

* [`rsync` homepage](https://rsync.samba.org/)

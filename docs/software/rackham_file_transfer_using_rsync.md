---
tags:
  - transfer
  - data transfer
  - file transfer
  - rsync
  - Rackham
---

# Data transfer to/from Rackham using rsync

There are multiple ways to [transfer files to or from Rackham](../cluster_guides/transfer_rackham.md).

Here it is described how to do file transfer to/from Rackham
using [rsync](../software/rsync.md).
`rsync` can be used in scripts for regular file transfer.
However, `rsync` shines by providing a so-called 'delta' file transfer:
when you transfer files twice, `rsync` will only transfer the files that have
changed. This is ideal for backups.

## Procedure

???- question "Prefer a video?"

    See this procedure as a video at [YouTube](https://youtu.be/p-27aIh2acA).

### 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 2. Transfer files to Rackham

You can transfer files to Rackham by:

- [2a. Transfer individual files to Rackham](#2a-transfer-individual-files-to-rackham)
- [2b. Transfer all files in a folder to Rackham](#2b-transfer-all-files-in-a-folder-to-rackham)

### 2a. Transfer individual files to Rackham

On local computer, do:

```bash
rsync [my_local_file] [username]@rackham.uppmax.uu.se:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your UPPMAX username

for example:

```bash
rsync my_local_file.txt sven@rackham.uppmax.uu.se:/home/sven/
```

If asked, give your UPPMAX password.
You can get rid of this prompt if you are
[using an SSH key pair](ssh_key_use_rackham.md).

### 2b. Transfer all files in a folder to Rackham

On local computer, do:

```bash
rsync --recursive my_folder [username]@rackham.uppmax.uu.se:[target_folder]
```

where

- `[target_folder]` is the target folder  
- `[username]` is your UPPMAX username

for example:

```bash
rsync --recursive my_folder sven@rackham.uppmax.uu.se:/home/sven/
```

If asked, give your UPPMAX password.
You can get rid of this prompt if you are
[using an SSH key pair](ssh_key_use_rackham.md).

Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder sven@rackham.uppmax.uu.se:/home/sven` |Will put the files in `my_folder` in the Rackham home folder
`rsync --recursive my_folder sven@rackham.uppmax.uu.se:/home/sven/`|Will put the folder `my_folder` in the Rackham home folder

## 3. Transfer files from Rackham to you local computer

You can transfer files from Rackham to your local computer by:

- [3a. Transfer individual files from Rackham to your local computer](#3a-transfer-individual-files-from-rackham-to-your-local-computer)
- [3b. Transfer all folders from Rackham to you local computer](#3b-transfer-all-folders-from-rackham-to-you-local-computer)

## 3a. Transfer individual files from Rackham to your local computer

On your local computer, do:

```bash
rsync [username]@rackham.uppmax.uu.se:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your UPPMAX username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync sven@rackham.uppmax.uu.se:/home/sven/my_file.txt .
```

If asked, give your UPPMAX password.
You can get rid of this prompt if you are
[using an SSH key pair](ssh_key_use_rackham.md).

## 3b. Transfer all folders from Rackham to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@rackham.uppmax.uu.se:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your UPPMAX username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive sven@rackham.uppmax.uu.se:/home/sven/my_folder .
```

If asked, give your UPPMAX password.
You can get rid of this prompt if you are
[using an SSH key pair](ssh_key_use_rackham.md).

---
tags:
  - rsync
  - Dardel
---

# File transfer to/from Dardel using `rsync`

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the PDC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

HPC clusters have different ways to do
[file transfer using `rsync`](file_transfer_using_rsync.md).

This page shows how to do so for Dardel.

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to Dardel
    using rsync, watch the video [here](https://youtu.be/IustC5zai68)

`rsync` is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from Dardel using `rsync`, do
the following steps:

## 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 2. Transfer files to Dardel

You can transfer files to Dardel by:

- [2a. Transfer individual files to Dardel](#2a-transfer-individual-files-to-dardel)
- [2b. Transfer all files in a folder to Dardel](#2b-transfer-all-files-in-a-folder-to-dardel)

### 2a. Transfer individual files to Dardel

On local computer, do:

```bash
rsync [my_local_file] [username]@dardel.pdc.kth.se:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your PDC username

for example:

```bash
rsync my_file.txt svensv@dardel.pdc.kth.se:~
```

If asked, give your PDC password.

### 2b. Transfer all files in a folder to Dardel

On local computer, do:

```bash
rsync --recursive my_folder [username]@dardel.pdc.kth.se:[target_folder]
```

where

- `[target_folder]` is the target folder  
- `[username]` is your PDC username

for example:

```bash
rsync --recursive my_folder svensv@dardel.pdc.kth.se:~/
```

If asked, give your PDC password.


Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder svensv@dardel.pdc.kth.se:~/` |Will put the files in `my_folder` in the Dardel home folder
`rsync --recursive my_folder svensv@dardel.pdc.kth.se:~/`|Will put the folder `my_folder` in the Dardel home folder

## 3. Transfer files from Dardel to you local computer

You can transfer files from Dardel to your local computer by:

- [3a. Transfer individual files from Dardel to your local computer](#3a-transfer-individual-files-from-dardel-to-your-local-computer)
- [3b. Transfer all folders from Dardel to you local computer](#3b-transfer-all-folders-from-dardel-to-you-local-computer)

## 3a. Transfer individual files from Dardel to your local computer

On your local computer, do:

```bash
rsync [username]@dardel.pdc.kth.se:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your PDC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync svensv@dardel.pdc.kth.se:~/my_file.txt .
```

If asked, give your PDC password.


## 3b. Transfer all folders from Dardel to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@dardel.pdc.kth.se:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your PDC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive svensv@dardel.pdc.kth.se:~/my_folder .
```

If asked, give your PDC password.

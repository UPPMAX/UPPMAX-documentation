---
tags:
  - rsync
  - Tetralith
---

# File transfer to/from Tetralith using `rsync`

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the NSC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

HPC clusters have different ways to do
[file transfer using `rsync`](file_transfer_using_rsync.md).

This page shows how to do so for Tetralith.

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to Tetralith
    using rsync, watch the video `TODO`

`rsync` is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from Tetralith using `rsync`, do
the following steps:

## 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 2. Transfer files to Tetralith

You can transfer files to Tetralith by:

- [2a. Transfer individual files to Tetralith](#2a-transfer-individual-files-to-tetralith)
- [2b. Transfer all files in a folder to Tetralith](#2b-transfer-all-files-in-a-folder-to-tetralith)

### 2a. Transfer individual files to Tetralith

On local computer, do:

```bash
rsync [my_local_file] [username]@tetralith.nsc.liu.se:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your NSC username

for example:

```bash
rsync my_file.txt x_svesv@tetralith.nsc.liu.se:~
```

If asked, give your NSC password.

### 2b. Transfer all files in a folder to Tetralith

On local computer, do:

```bash
rsync --recursive my_folder [username]@tetralith.nsc.liu.se:[target_folder]
```

where

- `[target_folder]` is the target folder  
- `[username]` is your NSC username

for example:

```bash
rsync --recursive my_folder x_svesv@tetralith.nsc.liu.se:~/
```

If asked, give your NSC password.


Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder x_svesv@tetralith.nsc.liu.se:~/` |Will put the files in `my_folder` in the Tetralith home folder
`rsync --recursive my_folder x_svesv@tetralith.nsc.liu.se:~/`|Will put the folder `my_folder` in the Tetralith home folder

## 3. Transfer files from Tetralith to you local computer

You can transfer files from Tetralith to your local computer by:

- [3a. Transfer individual files from Tetralith to your local computer](#3a-transfer-individual-files-from-tetralith-to-your-local-computer)
- [3b. Transfer all folders from Tetralith to you local computer](#3b-transfer-all-folders-from-tetralith-to-you-local-computer)

## 3a. Transfer individual files from Tetralith to your local computer

On your local computer, do:

```bash
rsync [username]@tetralith.nsc.liu.se:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your NSC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync x_svesv@tetralith.nsc.liu.se:~/my_file.txt .
```

If asked, give your NSC password.


## 3b. Transfer all folders from Tetralith to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@tetralith.nsc.liu.se:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your NSC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive x_svesv@tetralith.nsc.liu.se:~/my_folder .
```

If asked, give your NSC password.

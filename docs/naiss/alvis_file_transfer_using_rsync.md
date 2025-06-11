---
tags:
  - rsync
  - Alvis
---

# File transfer to/from Alvis using rsync

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the C3SE documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

HPC clusters have different ways to do
[file transfer using rsync](file_transfer_using_rsync.md).

This page shows how to do so for Alvis.

## Procedure

???- question "Would you like a video?"

    See the YouTube video
    [file transfer from/to Alvis using rsync](https://youtu.be/dzqQ-HBjIfo).

`rsync` is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from Alvis using `rsync`, do
the following steps:

### 1. Get inside SUNET

[Get inside of SUNET](../getting_started/get_inside_sunet.md).

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

### 2. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 3. Transfer files to Alvis

You can transfer files to Alvis by:

- [3a. Transfer individual files to Alvis](#3a-transfer-individual-files-to-alvis)
- [3b. Transfer all files in a folder to Alvis](#3b-transfer-all-files-in-a-folder-to-alvis)

### 3a. Transfer individual files to Alvis

On local computer, do:

```bash
rsync [my_local_file] [username]@alvis1.c3se.chalmers.se:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your C3SE username

for example:

```bash
rsync my_file.txt svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis/
                                                              ^
                                                              |
                                                              +--- username
```

If asked, give your C3SE password.

### 3b. Transfer all files in a folder to Alvis

On local computer, do:

```bash
rsync --recursive my_folder [username]@alvis1.c3se.chalmers.se:[target_folder]
```

where

- `[target_folder]` is the target folder
- `[username]` is your C3SE username

for example:

```bash
rsync --recursive my_folder svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis/
```

If asked, give your C3SE password.


Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis` |Will put the files in `my_folder` in the Alvis home folder
`rsync --recursive my_folder svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis/`|Will put the folder `my_folder` in the Alvis home folder

## 4. Transfer files from Alvis to you local computer

You can transfer files from Alvis to your local computer by:

- [4a. Transfer individual files from Alvis to your local computer](#4a-transfer-individual-files-from-alvis-to-your-local-computer)
- [4b. Transfer all folders from Alvis to you local computer](#4b-transfer-all-folders-from-alvis-to-you-local-computer)

## 4a. Transfer individual files from Alvis to your local computer

On your local computer, do:

```bash
rsync [username]@alvis1.c3se.chalmers.se:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your C3SE username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis/my_file.txt .
```

If asked, give your C3SE password.


## 4b. Transfer all folders from Alvis to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@alvis1.c3se.chalmers.se:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your C3SE username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive svens@alvis1.c3se.chalmers.se:/cephyr/users/svens/Alvis/my_folder .
```

If asked, give your C3SE password.


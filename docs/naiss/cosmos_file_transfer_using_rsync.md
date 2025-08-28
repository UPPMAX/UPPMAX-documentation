---
tags:
  - transfer
  - data transfer
  - file transfer
  - rsync
  - COSMOS
---

# Data transfer to/from COSMOS using rsync

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the LUNARC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

There are multiple ways to transfer files to or from COSMOS.
Here it is described how to do file transfer to/from COSMOS
using [rsync](../software/rsync.md).

## Procedure

???- question "Prefer a video?"

    Watch the YouTube video
    [Data transfer to/from COSMOS using rsync](https://youtu.be/hpug-nhLZ6Y).

## 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 2. Transfer files to COSMOS

You can transfer files to COSMOS by:

- [2a. Transfer individual files to COSMOS](#2a-transfer-individual-files-to-cosmos)
- [2b. Transfer all files in a folder to COSMOS](#2b-transfer-all-files-in-a-folder-to-cosmos)

## 2a. Transfer individual files to COSMOS

On local computer, do:

```bash
rsync [my_local_file] [username]@cosmos.lunarc.lu.se:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your LUNARC username

for example:

```bash
rsync my_local_file.txt sven@cosmos.lunarc.lu.se:/home/sven/
```

If asked, give your LUNARC password.

## 2b. Transfer all files in a folder to COSMOS

On local computer, do:

```bash
rsync --recursive my_folder [username]@cosmos.lunarc.lu.se:[target_folder]
```

where

- `[target_folder]` is the target folder
- `[username]` is your LUNARC username

for example:

```bash
rsync --recursive my_folder sven@cosmos.lunarc.lu.se:/home/sven/
```

If asked, give your LUNARC password.

Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder sven@cosmos.lunarc.lu.se:/home/sven` |Will put the files in `my_folder` in the COSMOS home folder
`rsync --recursive my_folder sven@cosmos.lunarc.lu.se:/home/sven/`|Will put the folder `my_folder` in the COSMOS home folder

## 3. Transfer files from COSMOS to you local computer

You can transfer files from COSMOS to your local computer by:

- [3a. Transfer individual files from COSMOS to your local computer](#3a-transfer-individual-files-from-cosmos-to-your-local-computer)
- [3b. Transfer all folders from COSMOS to you local computer](#3b-transfer-all-folders-from-cosmos-to-you-local-computer)

## 3a. Transfer individual files from COSMOS to your local computer

On your local computer, do:

```bash
rsync [username]@cosmos.lunarc.lu.se:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your LUNARC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync sven@cosmos.lunarc.lu.se:/home/sven/my_file.txt .
```

If asked, give your LUNARC password.

## 3b. Transfer all folders from COSMOS to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@cosmos.lunarc.lu.se:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your LUNARC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive sven@cosmos.lunarc.lu.se:/home/sven/my_folder .
```

If asked, give your LUNARC password.

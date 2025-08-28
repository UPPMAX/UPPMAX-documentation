---
tags:
  - transfer
  - data transfer
  - file transfer
  - rsync
  - LUMI
  - CSC
---

# Data transfer to/from LUMI using rsync

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the CSC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

There are multiple ways to transfer files to or from LUMI.
Here it is described how to do file transfer to/from LUMI
using [rsync](../software/rsync.md).

## Procedure

???- question "Prefer a video?"

    Watch the YouTube video
    [Data transfer to/from LUMI using rsync](https://youtu.be/hpug-nhLZ6Y).

## 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

## 2. Transfer files to LUMI

You can transfer files to LUMI by:

- [2a. Transfer individual files to LUMI](#2a-transfer-individual-files-to-cosmos)
- [2b. Transfer all files in a folder to LUMI](#2b-transfer-all-files-in-a-folder-to-cosmos)

## 2a. Transfer individual files to LUMI

On local computer, do:

```bash
rsync [my_local_file] [username]@lumi.csc.fi:[target_folder]
```

where

- `[my_local_file]` is the path to your local file
- `[target_folder]` is the path of the folder you want to copy your file to
- `[username]` is your CSC username

for example:

```bash
rsync my_local_file.txt sven@lumi.csc.fi:/users/sven/
```

If asked, give your CSC password.

## 2b. Transfer all files in a folder to LUMI

On local computer, do:

```bash
rsync --recursive my_folder [username]@lumi.csc.fi:[target_folder]
```

where

- `[target_folder]` is the target folder
- `[username]` is your CSC username

for example:

```bash
rsync --recursive my_folder sven@lumi.csc.fi:/users/sven/
```

If asked, give your CSC password.

Note that in `rsync`, a slash (`/`) matters:

Command                                                            |Effect
-------------------------------------------------------------------|------------------------------------------------------------
`rsync --recursive my_folder sven@lumi.csc.fi:/users/sven`         |Will put the files in `my_folder` in the LUMI home folder
`rsync --recursive my_folder sven@lumi.csc.fi:/users/sven/`        |Will put the folder `my_folder` in the LUMI home folder

## 3. Transfer files from LUMI to you local computer

You can transfer files from LUMI to your local computer by:

- [3a. Transfer individual files from LUMI to your local computer](#3a-transfer-individual-files-from-cosmos-to-your-local-computer)
- [3b. Transfer all folders from LUMI to you local computer](#3b-transfer-all-folders-from-cosmos-to-you-local-computer)

## 3a. Transfer individual files from LUMI to your local computer

On your local computer, do:

```bash
rsync [username]@lumi.csc.fi:[path_to_file] .
```

where

- `[path_to_file]` is the path to the file you want to download
- `[username]` is your CSC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync sven@lumi.csc.fi:/users/sven/my_file.txt .
```

If asked, give your CSC password.

## 3b. Transfer all folders from LUMI to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@lumi.csc.fi:/[source_folder] .
```

where

- `[source_folder]` is the path to the folder you want to download
- `[username]` is your CSC username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive sven@lumi.csc.fi:/users/sven/my_folder .
```

If asked, give your CSC password.

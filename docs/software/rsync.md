# `rsync`

`rsync` is a command-line tool for file transfer,
with the goal of ensuring integrity of the data,
as well as a minimal amount of data transfer.

`rsync` can be used for copying, but also synchronising files,
such as is ideal for making a backup. At this page, we use the word 'copy',
although `rsync` by default does a one-way synchronise: if the data is already
there, it will do nothing.

- [Using `rsync` on Bianca](../software/rsync_on_bianca.md)
- [Using `rsync` on Rackham](../software/rsync_on_rackham.md)

## Installing `rsync`

To installing `rsync`, see [the official `rsync` download page](https://rsync.samba.org/download.html).

???- question "Tip for Ubuntu users"

    Use `apt` like usual:

    ```bash
    sudo apt install rsync
    ```

???- question "Tip for Windows users"

    When looking to download an executable of `rsycn`,
    look for the words 'binary' (all executables are binary)
    and Cygwin (the environment in which the `rsync` executable
    was built on Windows).

## Copy a folder from local to Rackham

Copy a folder from a local computer to a Rackham home folder.

On your local computer, do:

```bash
rsync --recursive [folder_name] [user_name]@rackham.uppmax.uu.se:/home/[user_name]/
```

For example:

```bash
rsync --recursive my_folder sven@rackham.uppmax.uu.se:/home/sven/
```

The `--recursive` flag is used to
copy a folder and all of its subfolders.

???- question "Want to preserve timestamps?"

    To preserve the files' timestamps, use the `--archive` flag, e.g.

    ```bash
    rsync --recursive --archive my_folder sven@rackham.uppmax.uu.se:/home/sven/
    ```

## Copy a folder from Rackham to local

Copy a folder from Rackham
to your local computer.

On your local computer, do:

```bash
rsync --recursive [user_name]@rackham.uppmax.uu.se:/home/[user_name]/[folder_name] [local_folder_destination]
```

For example:

```bash
rsync --recursive sven@rackham.uppmax.uu.se:/home/sven/my_folder .
```

Where `.` means 'the folder where I am now'.

???- question "Want to preserve timestamps?"

    To preserve the files' timestamps, use the `--archive` flag, e.g.

    ```bash
    rsync --recursive --archive my_folder sven@rackham.uppmax.uu.se:/home/sven/
    ```

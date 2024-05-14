# `rsync`

`rsync` is a command-line tool for file transfer,
with the goal of ensuring integrity of the data,
as well as a minimal amount of data transfer.

`rsync` can be used for copying, but also synchronizing files,
such as is ideal for making a backup. At this page, we use the word 'copy',
although `rsync` by default does a one-way synchronize: if the data is already
there, it will do nothing.

* [Using `rsync` on Bianca](../cluster_guides/rsync_on_bianca.md)
* [Using `rsync` on Rackham](../cluster_guides/rsync_on_rackham.md)

## Copy a folder from local to Rackham

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

???- question "Want to preserve timestamps?"

    To preserve the files' timestamps, use the `--archive` flag, e.g.

    ```
    rsync --recursive --archive my_folder sven@rackham.uppmax.uu.se:/home/sven/
    ```

## Copy a folder from Rackham to local

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

???- question "Want to preserve timestamps?"

    To preserve the files' timestamps, use the `--archive` flag, e.g.

    ```
    rsync --recursive --archive my_folder sven@rackham.uppmax.uu.se:/home/sven/
    ```

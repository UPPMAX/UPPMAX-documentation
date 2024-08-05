# `uquota`

`uquota` is an UPPMAX tool to determine how much storage space
is left in all projects.

See the help file:

```bash
uquota --help
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham1 ~]$ uquota --help
    usage: uquota [-h] [-q] [-d] [-u USER] [-p PROJECTS_FILE] [--include-expired]
                  [--random-usage] [--only-expired] [--sort-by-col SORT_BY_COL]
                  [-s] [-f]

    optional arguments:
      -h, --help            Ask for help
      -q, --quiet           Quiet, abbreviated output
      -d, --debug           Include debug output
      -u USER, --user USER
      -p PROJECTS_FILE, --projects-file PROJECTS_FILE
      --include-expired     Include expired projects
      --random-usage        removed option, don't use
      --only-expired        Only show expired projects
      --sort-by-col SORT_BY_COL
                            Index (0-4) of column to sort by. Default is 0.
      -s, --slow            Deprecated. Previously ran 'du' command
      -f, --files           Reports on number of files. Only for home directories
    ```

Usage:

```bash
uquota
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham3 ~]$ uquota
    Your project     Your File Area       Unit        Usage  Quota Limit  Over Quota
    ---------------  -------------------  -------  --------  -----------  ----------
    home             /home/sven           GiB          24.7           32
    home             /home/sven           files       79180       300000
    naiss2024-22-49  /proj/worldpeace     GiB           5.1          128
    naiss2024-22-49  /proj/worldpeace     files       20276       100000
    ```

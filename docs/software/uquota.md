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

If you find out that your home folder is full,
but do not know which folder takes up most space,
use the command below to find it:

```bash
du --human --max-depth 1 .
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [sven@rackham2 ~]$ du --human --max-depth 1 .
    28K	./bin
    52M	./.config
    8.0K	./glob
    1.5G	./users
    484K	./.ssh
    9.7M	./.lmod.d
    514M	./.gradle
    4.0K	./.oracle_jre_usage
    84K	./.pki
    3.2G	./.singularity
    4.0K	./.git-credential-cache
    8.0K	./.keras
    6.1G	./.cache
    344M	./R
    740K	./.local
    8.0K	./.nv
    32M	./.nextflow
    88K	./.r
    140K	./.dbus
    48K	./.subversion
    8.0K	./.gnupg
    480K	./.java
    8.0K	./.vscode-oss
    29M	./.mozilla
    41M	./private
    64K	./.ipython
    8.0K	./.rstudio-desktop
    4.0K	./.allinea
    8.8M	./.beast
    688K	./.gstreamer-0.10
    8.4G	./.apptainer
    4.0K	./my_best_folder
    3.7G	./GitHubs
    260K	./.kde
    24K	./.jupyter
    849M	./.conda
    4.7M	./lib
    176M	./.vscode-server
    16K	./.MathWorks
    8.2M	./.matlab
    25G	.
    ```

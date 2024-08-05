# `uquota`

`uquota` is an UPPMAX tool to determine how much storage space
is left in all projects.

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
# `projinfo`

`projinfo` is a tool to see all [UPPMAX projects](../getting_started/project.md)
on an UPPMAX HPC cluster.

On an UPPMAX HPC cluster, on a terminal, run:

```bash
projinfo
```

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham3 ~]$ projinfo
    (Counting the number of core hours used since 2025-08-27/00:00:00 until now.)

    Project             Used[h]   Current allocation [h/month]
       User
    -----------------------------------------------------
    snic2017-7-132         0.00                2000

    -----------------------------------------------------
    staff                 62.86          2000000000
       agback              0.00
       dahlo               9.19
       douglas             5.61
       sven                48.05

    -----------------------------------------------------
    testappl               0.00                2000

    -----------------------------------------------------
    testqt                 7.37                2000
       batchtst            7.37

    -----------------------------------------------------
    uppmax2025-2-1       456.80                5000
       fruano            456.80

    -----------------------------------------------------
    uppmax2025-2-10     2412.91                4000
       raphaj           2412.91

    -----------------------------------------------------
    uppmax2025-2-100        0.00                2000

    -----------------------------------------------------
    uppmax2025-2-101        0.00              200000

    -----------------------------------------------------
    uppmax2025-2-102       10.09              100000
       patrikro           10.09

    -----------------------------------------------------
    uppmax2025-2-104        0.00               35000

    -----------------------------------------------------
    uppmax2025-2-105       26.62                5000
       gramoken           26.62

    -----------------------------------------------------
    uppmax2025-2-106    81063.53               10000
       andersl         81063.53

    -----------------------------------------------------
    uppmax2025-2-107        0.00                2000

    ```

To see your projects, use:

```bash
projinfo | grep $USER -B 10
```

This command will look for your username and display the
10 lines before it, in the hope of showing the project you belong to.

For example:

```bash
[sven@rackham3 ~]$ projinfo | grep $USER -B 10
Project             Used[h]   Current allocation [h/month]
   User
-----------------------------------------------------
uppmax1999-1-234       0.00                2000

-----------------------------------------------------
uppmax2025-1-234      62.86          2000000000
   knatte              0.00
   fnatte              9.19
   tjatte              5.61
   sven                48.05
```

Here we see that `sven` is part of `uppmax2025-1-234`.
He does not belong to `uppmax1999-1-234`, as he is not listed
there.

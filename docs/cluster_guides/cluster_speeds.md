---
tags:
  - UPPMAX
  - cluster
  - clusters
  - speed
  - fast
  - slow
---

# Cluster speeds

Sometimes you feel a cluster is slow.

Below are some benchmark results, so you can compare with what you are
experiencing.

Please [contact support](support.md) when you find out that your favorite
cluster is slower than expected.

???- question "What could cause such a slowdown?"


    > When things are slow it is usually due to latency
    > when many processes are accessing the same files
    > and physical hard drives

    Examples:

    - 2024-12-06: Castor is still holding some file systems for Bianca
      or a user that is running a lot of very short lived Perl jobs on Bianca,
      that are running too hard on Castor.

## Starting an interactive node


### `interactive -A sens2017625 -n 2 -t 1:00:00`

???- question "What was the system usage at the time of these measurements?"

    Bianca used around 800 out of around 3200 cores.

    ![Bianca sytem usage at 2024-12-18](./img/bianca_system_usage_20241218.png)

???- question "What was the project CPU usage at the time of these measurements?"

    CPU usage was close to zero:

    ![CPU usage at 2024-12-18](./img/cpu_usage_sens2017625.png)

Attempt|You waited for `x` seconds|Complete time (secs)
-------|--------------------------|--------------------
1      |1                         |37
2      |2                         |35
3      |1                         |37
4      |1                         |34
5      |1                         |36

### `interactive -A sens2017625 --partition devcore -n 2 -t 1:00:00`

???- question "What was the system usage at the time of these measurements?"

    Bianca used around 800 out of around 3200 cores.

    ![Bianca sytem usage at 2024-12-18](./img/bianca_system_usage_20241218.png)

???- question "What was the project CPU usage at the time of these measurements?"

    CPU usage was close to zero:

    ![CPU usage at 2024-12-18](./img/cpu_usage_sens2017625.png)

Attempt|You waited for `x` seconds|Complete time (secs)
-------|--------------------------|--------------------
1      |1                         |37
2      |1                         |34
3      |1                         |34
4      |1                         |37
5      |1                         |35


### `interactive -A sens2023036 -n 2 -t 1:00:00`

???- question "What was the system usage at the time of these measurements?"

    Bianca used around 800 out of around 3200 cores.

    ![Bianca sytem usage at 2024-12-18](./img/bianca_system_usage_20241218.png)

???- question "What was the project CPU usage at the time of these measurements?"

    CPU usage was close to zero:

    ![CPU usage at 2024-12-18](./img/cpu_usage_sens2023036.png)

Attempt|You waited for `x` seconds|Complete time (secs)
-------|--------------------------|--------------------
1      |More than 60*60*2 (i.e. 2 hours) |Interrupted
2      |.                         |.
3      |.                         |.
4      |.                         |.
5      |.                         |.

### `interactive -A sens2023036 --partition devcore -n 2 -t 1:00:00`

???- question "What was the system usage at the time of these measurements?"

    Bianca used around 800 out of around 3200 cores.

    ![Bianca sytem usage at 2024-12-18](./img/bianca_system_usage_20241218.png)

???- question "What was the project CPU usage at the time of these measurements?"

    CPU usage was close to zero:

    ![CPU usage at 2024-12-18](./img/cpu_usage_sens2023036.png)

Attempt|You waited for `x` seconds|Complete time (secs)
-------|--------------------------|--------------------
1      |More than 60*60*2 (i.e. 2 hours) |Interrupted
2      |.                         |.
3      |.                         |.
4      |.                         |.
5      |.                         |.

## Loading the `R_packages/4.3.1` module

For [a benchmark to solve a ticket](https://github.com/UPPMAX/ticket_304069/blob/master/module_load.md#answers),
the following command was run in multiple settings:

```bash
time module load R_packages/4.3.1
```

From the three resulting times, the 'Real' time is used.

Here are some expected timings:

Project    |Setting                     |Real loading time
-----------|----------------------------|-----------------
Rackham    |SSH                         |0m0.758s
Bianca     |SSH                         |0m8.984s

Here are some unexpected timings:

Project    |Setting                     |Real loading time
-----------|----------------------------|-----------------
sens2023598|SSH                         |6m1.265s
sens2023598|Website                     |6m20.234s
sens2017625|SSH                         |6m4.584s
sens2017625|Website, interactive session|7m41.433s
sens2017625|SSH, interactive session    |7m13.111s


## Loading the `RStudio/2023.12.1-402` module

Project    |Setting                     |Real loading time
-----------|----------------------------|-----------------
Bianca     |Website                     |2m3.184s


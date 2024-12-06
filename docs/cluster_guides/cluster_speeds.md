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

Here are some unexpected timings:

Project    |Setting                     |Real loading time
-----------|----------------------------|-----------------
sens2023598|SSH                         |6m1.265s
sens2023598|Website                     |6m20.234s
sens2017625|SSH                         |6m4.584s
sens2017625|Website, interactive session|7m41.433s
sens2017625|SSH, interactive session    |7m13.111s


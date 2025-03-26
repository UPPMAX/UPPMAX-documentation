---
tags:
  - Slurm
  - scheduler
  - efficiency
  - tool
  - software
---

# `seff`

`seff` is [software](software.md) to determine the efficiency
of Slurm jobs. On UPPMAX, use [jobstats](jobstats.md) instead.

???- question "Why is this on the UPPMAX pages?"

    As there may be plans to have it on UPPMAX too.


???- question "How does its output look like?"

    Output will be similar to this, as run on Dardel:

    ```bash
    svensv@login1:~> seff 123456
    Job ID: 123456
    Cluster: dardel
    User/Group: bobek/bobek
    State: COMPLETED (exit code 0)
    Nodes: 1
    Cores per node: 256
    CPU Utilized: 1-07:31:54
    CPU Efficiency: 21.56% of 6-02:16:32 core-walltime
    Job Wall-clock time: 00:34:17
    Memory Utilized: 7.26 GB
    Memory Efficiency: 3.27% of 222.00 GB
    ```

HPC cluster|Has `seff` installed?
-----------|---------------------------------------
Dardel     |Yes
Rackham    |No, use [jobstats](jobstats.md) instead


\---

tags:

&#x20; - Slurm

&#x20; - scheduler

&#x20; - efficiency

&#x20; - tool

&#x20; - software

\---



\# `seff`



`seff` is a tool to determine the efficiency

of Slurm jobs. On UPPMAX, use \[jobstats](jobstats.md) instead.



???- question "Why is this on the UPPMAX pages?"



&#x20;   As there may be plans to have it on UPPMAX too.





???- question "What does its output look like?"



&#x20;   Output will be similar to this, as run on Dardel:



&#x20;   ```bash

&#x20;   svensv@login1:\~> seff 123456

&#x20;   Job ID: 123456

&#x20;   Cluster: dardel

&#x20;   User/Group: bobek/bobek

&#x20;   State: COMPLETED (exit code 0)

&#x20;   Nodes: 1

&#x20;   Cores per node: 256

&#x20;   CPU Utilised: 1-07:31:54

&#x20;   CPU Efficiency: 21.56% of 6-02:16:32 core-walltime

&#x20;   Job Wall-clock time: 00:34:17

&#x20;   Memory Utilised: 7.26 GB

&#x20;   Memory Efficiency: 3.27% of 222.00 GB

&#x20;   ```



HPC cluster|Has `seff` installed?

\-----------|---------------------------------------

Dardel     |Yes




---
tags:
  - overview
  - hardware
  - specifications
  - specs
---

# Hardware overview

This page describes the hardware architecture of the different compute clusters
at UPPMAX as well as their storage systems.

UPPMAX is part of the [National Academic Infrastructure for
Supercomputing in Sweden (NAISS)](https://www.naiss.se/).

Parameter               |Pelle                  |Rackham                |Snowy                                  |[Bianca](clusters/bianca.md)       |UPPMAX Cloud
------------------------|-----------------------|-----------------------|---------------------------------------|-----------------------------------|-----------------------------
**Purpose**             |General-purpose        |General-purpose        |General-purpose                        |Sensitive data                     |IaaS
**Reserved for**        |Uppsala researchers and course projects|Uppsala researchers and course projects |Uppsala researchers and course projects|See [Bianca](clusters/bianca.md)   |NAISS and local projects
**Nodes (Intel)**       |coming                |486+144                |228 + 50 N vidia T4 GPUs               |See [Bianca](clusters/bianca.md)   |40 + 20 A2 and 4 T4 Nvidia GPUs
**Cores per node**      |coming                |20/16                  |16                                     |See [Bianca](clusters/bianca.md)   |16
**Memory per node**     |coming               |128GB                  |128GB                                  |See [Bianca](clusters/bianca.md)   |128/256GB
**Fat nodes**           |coming            |256, 512 GB & 4TB                      |See [Bianca](clusters/bianca.md)   |N/A
**Local disk (scratch)**|coming               |2/3TB                  |4TB                                    |See [Bianca](clusters/bianca.md)   |N/A
**Network**             |coming                |InfiniBand FDR 56Gbit/s|InfiniBand FDR 40Gbit/ s               |See [Bianca](clusters/bianca.md)   |10GbE
**Operating System**    |coming               |CentOS 7               |CentOS 7                               |See [Bianca](clusters/bianca.md)   |[Linux cloud image](https://cloud.snic.se/instances/)
**Login nodes**         |coming                |Yes                    |No (reached from Rackham)              |See [Bianca](clusters/bianca.md)   |N/A
**"Home" storage**      |coming                |Domus                  |Domus                                  |See [Bianca](clusters/bianca.md)   |N/A
**"Project" Storage**   |coming                |Crex, Lutra            |Crex, Lutra                            |See [Bianca](clusters/bianca.md)   |N/A

The storage systems we have provide a total volume of about 20 PB, the
equivalent of nearly 15 billion 3.5-inch floppy disks or 40,000 years of
128-bit encoded music.

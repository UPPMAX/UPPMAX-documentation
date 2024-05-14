This page describes the hardware architecture of the different compute clusters
at UPPMAX as well as their storage systems.

UPPMAX is part of the [National Academic Infrastructure for
Supercomputing in Sweden (NAISS)](https://www.naiss.se/) and as such


| |Rackham|Snowy|Bianca|UPPMAX Cloud|
|-------|-----|------|---|---|
|**Purpose**|General-purpose|General-purpose|Sensitive data|IaaS
|**Reserved for**|NAISS projects|Uppsala researchers and course projects|NAISS-SENS projects|NAISS and local projects |
|**  Nodes (Intel)**|486+144|228+ <br>50 N vidia T4 GPUs|272 +  <br>4 nodes á 2 <br>NVIDIA A100 GPUs| 40 + <br> 20 A2 and 4 T4 Nvidia GPUs |
|**Cores per node**|20/16|16|16/64| 16
|**Memory per node**|128GB|128GB|128GB |128/256GB |
|**Fat nodes**|256GB & 1TB| 256, 512 GB & 4TB| 256 & 512GB|N/A
|**Local disk (scratch)**|2/3TB| 4TB| 4TB |N/A
|**Network**|Infiniband FDR 56Gbit/s| Infiniband FDR 40Gbit/s | Dual 10Gbit/s | 10GbE
|**Operating System**|CentOS 7| CentOS 7| CentOS 7| [Linux cloud image](https://cloud.snic.se/instances/) |
|**Login nodes**|Yes| No (reached from Rackham)|Yes (2 cores and 15 GB)| N/A
    |**"Home" storage**|Domus|Domus|Castor| N/A
|**"Project" Storage**|Crex, Lutra|Crex, Lutra|Castor| N/A

The storage systems we have provide a total volume of about 20 PB, the
equivalent of nearly 15 billion 3.5-inch floppy disks or 40,000 years of
128-bit encoded music. Read more on the

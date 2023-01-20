This page describes the hardware architecture of the different compute clusters
at UPPMAX as well as their storage systems. 

UPPMAX is part of the [National Academic Infrastructure for
Supercomputing in Sweden (NAISS)](https://www.naiss.se/) and as such


| |Rackham|Snowy|Bianca|Miarka|UPPMAX Cloud|
|-------|-----|------|---|---|---|
|**Purpose**|General-purpose|General-purpose|Sensitive data|Bioinformatics|IaaS
|**Reserved for**|NAISS projects|Uppsala researchers and course projects|NAISS-SENS projects|[SciLifeLab](https://www.scilifelab.se/) | NAISS and local projects | 
|**  Nodes (Intel)**|486+144|228+ <br>50 N vidia T4 GPUs|272 +  <br>4 nodes á 2 <br>NVIDIA A100 GPUs| 68 + 2 + 1 <br> 4 A100 Nvidia GPUs  | 40 + <br> 20 A2 and 4 T4 Nvidia GPUs |
|**Cores per node**|20/16|16|16/64| 24 | 16
|**Memory per node**|128GB|128GB|128GB | 384GB |128/256GB |
|**Fat nodes**|256GB & 1TB| 256, 512 GB & 4TB| 256 & 512GB| 2/4TB| N/A
|**Local disk (scratch)**|2/3TB| 4TB| 4TB | 12TB | N/A
|**Network**|Infiniband FDR 56Gb/s| Infiniband FDR 40GB/s | ? | ? | 10GbE
|**Operating System**|CentOS 7| CentOS 7| CentOS 7| Rock Linux 8.5 | [Linux cloud image](https://cloud.snic.se/instances/) |
|**Login nodes**|Yes| No (reached from Rackham)|Yes (2 cores and 15 GB)| Yes | N/A
    |**"Home" storage**|Domus|Domus|Castor| ? | N/A
|**"Project" Storage**|Crex, Lutra|Crex, Lutra|Castor| ? | N/A

The storage systems we have provide a total volume of about 20 PB, the
equivalent of nearly 15 billion 3.5-inch floppy disks or 40,000 years of
128-bit encoded music. Read more on the

# Pelle/Maja hardware

No of nodes     | CPUs                              | Cores<br/>Threads |  Memory   | Scratch | GPUs           | Name
--------------- | --------------------------------- | ----------------- | --------- |-------- |--------------- |------------
116             |  AMD EPYC 9454P (Zen4)  2.75 GHz  | 48<br/>96         | 768 GiB   | 6? TB   | N/A            | p[1-115]
2               |  AMD EPYC 9454P (Zen4)  2.75 GHz  | 48<br/>96         | 2 / 3 TiB | 6? TB   | N/A            | p[251-252]
4               |  2 x AMD EPYC 9124 (Zen4)  3 GHz  | 2 x 16<br/>2 x 32 | 384 GiB   | 6? TB   | 10 x L40       | p[201-204]
2               |  2 x AMD EPYC 9124 (Zen4)  3 GHz  | 2 x 16<br/>2 x 32 | 384 GiB   | 6? TB   | 2 x H100       | p[205-206]

## CPUs

- [AMD EPYC 9454P (Zen4) 48-Core Processor 2.75 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html)
- [AMD EPYC 9124 (Zen4) 16-Core Processor 3 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9124.html)

## GPUs

- [L40](https://www.nvidia.com/en-us/data-center/l40/)

    - Unprecedented visual computing performance for the data center.
    - GPU memory 48 GB
    - GPU Memory Bandwidth 864GB/s

- [H100](https://www.nvidia.com/en-us/data-center/h100/) tensor core

    - Extraordinary performance, scalability, and security for every data center.
    - GPU memory 94 GB
    - GPU Memory Bandwidth 3.9 TB/s

## Network

100 Gbit/s

## Storage

- Gorilla
- Domus/Crex in an transition period

## OS

Rocky 9

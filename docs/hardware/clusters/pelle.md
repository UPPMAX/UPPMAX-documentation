# Pelle/Maja hardware

Nodes  | CPUs                              | Cores<br/>Threads | Memory    | Scratch | GPUs
-------| --------------------------------- | ----------------- | --------- |-------- |----------
115    |  AMD EPYC 9454P (Zen4)  2.75 GHz  | 48<br/>96         | 768 GiB   | 1.7 TiB | N/A
2      |  AMD EPYC 9454P (Zen4)  2.75 GHz  | 48<br/>96         | 2 / 3 TiB | 6.9 TiB | N/A
4      |  2 x AMD EPYC 9124 (Zen4)  3 GHz  | 2 x 16<br/>2 x 32 | 384 GiB   | 6.9 TiB | 10 x L40s
2      |  2 x AMD EPYC 9124 (Zen4)  3 GHz  | 2 x 16<br/>2 x 32 | 384 GiB   | 6.9 TiB | 2 x H100

## CPUs

- [AMD EPYC 9454P (Zen4) 48-Core Processor 2.75 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html)
- [AMD EPYC 9124 (Zen4) 16-Core Processor 3 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9124.html)

## GPUs

- [L40s](https://www.nvidia.com/en-us/data-center/l40s/)

    - Unprecedented visual computing performance for the data centre.
    - GPU memory 48 GB
    - GPU Memory Bandwidth 864GB/s

- [H100](https://www.nvidia.com/en-us/data-center/h100/) tensor core

    - Extraordinary performance, scalability, and security for every data centre.
    - GPU memory 94 GB
    - GPU Memory Bandwidth 3.9 TB/s

## Network

100 Gbit/s

## Storage

- Gorilla
    - Home folder is mounted
- Domus/Crex in an transition period
    - Projects are still on crex/
    - Software is still on domus/

## OS

Rocky 9

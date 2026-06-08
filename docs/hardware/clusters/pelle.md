# Pelle hardware

Nodes | CPUs                                 | Cores<br/>Threads | Memory  | Scratch | GPUs
----- | ------------------------------------ | ----------------- | ------- |-------- |----------
80    | AMD EPYC 9454P (Zen4)  2.75 GHz      | 48<br/>96         | 768 GiB | 1.7 TiB | N/A
1     | AMD EPYC 9454P (Zen4)  2.75 GHz      | 48<br/>96         | 2 TiB   | 6.9 TiB | N/A
1     | AMD EPYC 9454P (Zen4)  2.75 GHz      | 48<br/>96         | 3 TiB   | 6.9 TiB | N/A
4     | 2x AMD EPYC 9124 (Zen4)  3 GHz       | 2 x 16<br/>2 x 32 | 384 GiB | 6.9 TiB | 10 x L40s
2     | 2x AMD EPYC 9124 (Zen4)  3 GHz       | 2 x 16<br/>2 x 32 | 384 GiB | 6.9 TiB | 2 x H100
36    | 2x Xeon E5-2630 v3 2.4 GHz (Haswell) | 2 x 8<br/>2 x 8 | 256 GiB | 1.8 TB  | N/A
34    | 2x Xeon E5-2630 v3 2.4 GHz (Haswell) | 2 x 8<br/>2 x 8 | 256 GiB | 1.8 TB  | NVIDIA T4

## CPUs

- [AMD EPYC 9454P (Zen4) 48-Core Processor 2.75 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html)
- [AMD EPYC 9124 (Zen4) 16-Core Processor 3 GHz](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9124.html)
- [Intel Xeon E5-2630 v3 (Haswell) 8-Core Processor 2.4 GHz](https://www.intel.com/content/www/us/en/products/sku/83356/intel-xeon-processor-e52630-v3-20m-cache-2-40-ghz/specifications.html)

## GPUs

- [Nvidia H100 NVL](https://www.nvidia.com/en-us/data-center/h100/#specifications)

    - Grace Hopper architecture
    - Fourth generation Tensor cores
    - 94 GB memory
    - 3.9 TB/s memory bandwidth

- [Nvidia L40s](https://www.nvidia.com/en-us/data-center/l40s/#specifications)

    - 18 176 CUDA cores, Ada Lovelace architecture
    - 568 Tensor cores, fourth generation
    - 48 GB memory
    - 864 GB/s memory bandwidth

- [Nvidia T4](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet.pdf)

    - 2 560 CUDA cores, Turing architecture
    - 320 Tensor cores, Turing architecture
    - 16 GB memory
    - 300 GB/s memory bandwidth

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

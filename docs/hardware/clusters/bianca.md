---
tags:
  - Bianca
  - hardware
  - specifications
  - specs
---

# Bianca hardware

## Technical Summary

- 148 (ordinary/thin) compute nodes with
    - single or dual CPUs with 256 GB RAM and
    - one 4TB mechanical drive or 1 TB SSD
    - each CPU has 16 cores
- 10 fat compute nodes
    - 6 nodes with 512 GB memory each
    - 4 nodes with 1 TB memory each
- 27 GPU nodes
    - 9 GPU compute nodes each equipped with 2xNVIDIA A100 (40 GB) **GPUs**
    - 17 GPU compute nodes each equipped with 1xNVIDIA T4 (16 GB) **GPUs**
- 35 Zen4 type compute nodes, 768 GB each
    - 105 virtual nodes á 3 256 GB each
- Total number of CPU cores is 4800
- Login nodes have 4vCPU each and 50 GB memory
- Dual 10 Gigabit Ethernet for all nodes

## Parameters

Parameter               |Bianca
------------------------|-----------------------------------
**Purpose**             |Sensitive data
**Reserved for**        |NAISS-SENS projects
**Nodes (Intel)**       |272 + 9 nodes of 2 NVIDIA A100 GPUs + 17 nodes of NVIDIA T4 GPUs
**Nodes (AMD)**         |45 (3 virtual nodes per physical node)
**Cores per node**      |16
**Memory per node**     |256GB
**Fat nodes**           |512 & 1 TB
**Local disk (scratch)**|4TB
**Network**             |Dual 10Gbit/s
**Operating System**    |CentOS 7
**Login nodes**         |Yes (4 cores and 50 GB)
**"Home" storage**      |Cygnus
**"Project" Storage**   |Cygnus

## CPU

### Intel nodes (4th generation)

- Architecture: x86_64
- [Intel Xeon E5-2630 v3 Huawei XH620 V3](https://www.intel.com/content/www/us/en/products/sku/83356/intel-xeon-processor-e52630-v3-20m-cache-2-40-ghz/specifications.html) nodes
- Advanced Vector Extensions 2 (AVX2)
- CPU op-mode(s): 32-bit, 64-bit
- Byte Order: Little Endian
- CPU(s): 16
- Thread(s) per core: 1
- Core(s) per socket: 8
- Socket(s): 2
- NUMA node(s): 2
- Model name: Intel Core Processor (**Haswell**, no TSX, IBRS)
- CPU MHz: 2.4 GHz
- For more info, type: lscpu in the terminal

### AMD nodes (Zen4)

**[Zen4](https://en.wikipedia.org/wiki/Zen_4)** type compute nodes

Settings on Bianca (virtualisation)

- Physical nodes divided into 3 sections, each with:
    - 16 cores 256 GB RAM

## GPUs

- 10 compute nodes each equipped with 2xNVIDIA **[A100](https://www.nvidia.com/en-us/data-center/a100/)** (40 GB) **GPUs**
- 17 compute nodes each equipped with 1xNVIDIA **[T4](https://en.wikipedia.org/wiki/Turing_(microarchitecture))** (16 GB) **GPU**

## Network

Dual 10 Gigabit Ethernet for all nodes

## Storage

[Cygnus](../storage/cygnus.md)

## Security

Since Bianca is designed to handle sensitive personal data security is a key aspect of the configuration. In order to ensure that the data is safe we have implemented a series of security measures including, but not limited to:

- One virtualised cluster per project, no resources are shared between projects.
- Separate storage volumes per project.
- Detailed logging of file transfers in and out of the cluster.
- Two factor authentication
- No internet access inside the clusters.
- Locked racks for the hardware
- Destruction of broken hard drives

Uppsala University has decided on the following KRT classifications for Bianca:

- 321 for project directories
- 322 for home directories

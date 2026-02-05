---
tags:
  - Bianca
  - hardware
  - specifications
  - specs
---

# Bianca hardware

## Technical Summary

- 204 compute nodes with single or dual CPUs with 128 GB RAM and one 4TB mechanical drive or 1TB SSD
- Each CPU has 16 cores
- 75 compute nodes, 256 GB memory each.
- 15 compute nodes, 512 GB memory each
- 10 compute nodes each equipped with 2xNVIDIA A100 (40GB) GPUs
- 105 Zen4 type compute nodes, 256 GB each
- Total number of CPU cores is 4800
- Login nodes have 2vCPU each and 16GB memory
- Dual 10 Gigabit Ethernet for all nodes

## Parameters

Parameter               |Bianca
------------------------|-----------------------------------
**Purpose**             |Sensitive data
**Reserved for**        |NAISS-SENS projects
**Nodes (Intel)**       |272 + 4 nodes of 2 NVIDIA A100 GPUs
**Cores per node**      |16/64
**Memory per node**     |128GB
**Fat nodes**           |256 & 512GB
**Local disk (scratch)**|4TB
**Network**             |Dual 10Gbit/s
**Operating System**    |CentOS 7
**Login nodes**         |Yes (2 cores and 30 GB)
**"Home" storage**      |Castor/Cygnus
**"Project" Storage**   |Castor/Cygnus

## CPU

## GPU

## Network

## Storage

Cygnus

## Security

Since Bianca is designed to handle sensitive personal data security is a key aspect of the configuration. In order to ensure that the data is safe we have implemented a series of security measures including, but not limited to:

- One virtualized cluster per project, no resources are shared between projects.
- Separate storage volumes per project.
- Detailed logging of file transfers in and out of the cluster.
- Two factor authentication
- No internet access inside the clusters.
- Locked racks for the hardware
- Destruction of broken hard drives

Uppsala University has decided on the following KRT classifications for Bianca:

- 321 for project directories
- 322 for home directories

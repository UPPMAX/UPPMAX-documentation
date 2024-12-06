---
tags:
  - Bianca
  - hardware
  - specifications
  - specs
---

# Bianca hardware

## Technical Summary

- 204 compute nodes with single or dual CPUs and one 4TB mechanical drive or 1TB SSD
- Each CPU has 8 cores
- 75 compute nodes, 256 GB memory each.
- 15 compute nodes, 512 GB memory each
- 10 compute nodes each equipped with 2xNVIDIA A100 (40GB) GPUs
- Total number of CPU cores is 4800
- Login nodes have 2vCPU each and 16GB memory
- Dual 10 Gigabit Ethernet for all nodes

## CPU

## GPU

## Network

## Storage

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

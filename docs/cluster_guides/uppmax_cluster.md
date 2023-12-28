# UPPMAX cluster

UPPMAX is an organization that provides HPC clusters.

???- question "Where can I find an overview of UPPMAX?"

    One can find an overview of UPPMAX [here](uppmax.md)

???- question "Where can I find an overview of UPPMAX's systems?"

    One can find an overview of UPPMAX's systems [here](uppmax_systems.md)


After giving [an overview of the different UPPMAX clusters](#overview-of-uppmax-clusters),
it is discussed [what a computer cluster is](#what-is-a-computer-cluster-technically?),
how [it differs from a supercomputer](#difference-between-a-supercomputer-and-a-(high-performing)-computer-cluster),
what [the restrictions of a computer cluster are](#restrictions-on-a-computer-cluster),
as well as some added [restrictions on a sensitive data computer cluster](#restrictions-on-a-sensitive-data-computer-cluster).

This is followed by a [detailed technical summary of the clusters](#uppmax-clusters-technical-summary)
and a [detailed overview of the clusters](#detailed-overview-of-the-uppmax-systems).

## Overview of UPPMAX clusters

UPPMAX clusters are computing systems, 
i.e. they allow a user to do heavy computational calculations.

All UPPMAX clusters are named after a Tintin character.
UPPMAX has, among others, the following clusters:

- [Bianca](bianca_portal.md): for sensitive data, general use. 
- Miarka: for sensitive data, SciLifeLab-only
- [Rackham](rackham_portal.md): regular data, general purpose
- Snowy: regular data, long runs and GPU:s

```mermaid
flowchart TD
    UPPMAX(Which UPPMAX cluster?)
    Bianca
    Rackham
    Miarka
    Snowy
    is_sensitive[Do you use sensitive data?]
    is_scilifelab[Do you work at SciLifeLab?]
    is_long[Do you use long runs and/or GPUs?]

    UPPMAX --> is_sensitive 
    is_sensitive --> |yes|is_scilifelab
    is_scilifelab --> |yes|Miarka
    is_scilifelab --> |no|Bianca
    is_sensitive --> |no|is_long
    is_long --> |no|Rackham
    is_long --> |yes|Snowy
```

## What is a computer cluster technically?

A computer cluster is a machine that consists out of many computers.
These computers work together.

Each computer of a cluster is called a **node**.

There are three types of nodes:

- **login nodes**: nodes where a user enters and interacts with the system

???- tip "Logging in"

    Logging in is described separately per cluster: 

    - [Bianca](../getting_started/login_bianca.md).
    - [Rackham](../getting_started/login_rackham.md).
    - [Snowy](../getting_started/login_snowy.md).

- **calculation nodes**: nodes that do the calculations

???- tip "Requesting a calculation to run"

    Requesting a calculation to run is described [here](slurm.md).
    This is done by using the SLURM scheduler.

- **interactive nodes**: a type of calculation node, where a user can do calculations directly

???- tip "Requesting an interactive node"

    Requesting an interactive node is described per cluster:

    - [Bianca](start_interactive_node_on_bianca.md)
    - [Rackham](start_interactive_node_on_rackham.md)

    This is done by requesting an interactive node 
    from the SLURM scheduler.

Each node contains several CPU/GPU cores, RAM and local storage space.

A user logs in to a login node via the Internet.

## Difference between a supercomputer and a (high-performing) computer cluster

![A supercomputer, from https://en.wikipedia.org/wiki/File:IBM_Blue_Gene_P_supercomputer.jpg](./img/IBM_Blue_Gene_P_supercomputer_422_x_280.jpg)

A supercomputer is a machine that is optimized for doing calculations
quickly. For example, to predict the weather for tomorrow, the calculation
may not take a week. The image above is a supercomputer.

![A computer cluster using some Raspberry Pi's](./img/small_cluster_307_x_230.jpg)

A computer cluster is a machine that is optimized for doing a lot of calculations.
The image above shows a home-made computer cluster.
This home-made computer cluster may not be suitable for high-performance.

![The Rackham computer cluster](./img/uppmax-light2_412_x_285.jpg)

The image above shows Rackham, another UPPMAX 
computer cluster, suitable for high-performance computing.
This makes Rackham an high-performance computing (HPC) cluster.
Bianca and Rackham are HPC clusters.

## Restrictions on a computer cluster

A computer cluster is a group of computers that can run
many calculations, as requested by multiple people, at the same time.

To ensure fair use of this shared resource, regular users
are restricted in some ways:

- Users cannot run calculations directly. 
  Instead, users need to request either (1) a calculation to be run,
  or (2) an interactive node

???- tip "Requesting a calculation to run"

    Requesting a calculation to run is described [here](slurm.md).
    This is done by using the SLURM scheduler.

???- tip "Requesting an interactive node"

    Requesting an interactive node is described per cluster:

    - [Bianca](start_interactive_node_on_bianca.md)
    - [Rackham](start_interactive_node_on_rackham.md)

    This is done by requesting an interactive node 
    from the SLURM scheduler.

- Users cannot install software directly. 
  Instead, users need to use pre-installed software or learn
  techniques how to run custom software anyway

???- tip "Using pre-installed software"

    Using pre-installed software is described [here](modules.md).
    This is done by using the module system.

???- tip "How to run custom software"

    Techniques how to run custom software is *not* part of this course.
    Instead, one technique is part of the intermediate Bianca course 
    and can be found described [here](extra/containers/),
    which is about using containers

These restrictions apply to most general-purpose clusters
and all UPPMAX clusters.

## Restrictions on a sensitive data computer cluster

Next to the general restrictions above, 
a sensitive data cluster has additional restrictions.

Here is an overview which clusters are designed for sensitive data:

Cluster name|Sensitive data yes/no?
------------|----------------------
Bianca      |Yes
Rackham     |No
Snowy       |No


On a sensitive data cluster, 
(sensitive) data must be protected to remain there,
due to which there are these additional restrictions to users:

- Users have no direct access to internet.
  Instead, users can up/download files from/to a special folder.

???- tip "File transfer"

    Transferring files is described per sensitive data cluster:

    - [Bianca](transfer_bianca.md).

The goal is *not* to prevent the up/download of sensitive data,
instead it is to prevent the *accidental* up/download of sensitive data.
As these up/downloads are monitored, in case of an accident, 
the extent of the leak and the person (accidentally) causing it
is known. Identifying a responsible person in case of such an
accident is required by law.

## UPPMAX clusters technical summary

This is a technical summary of the UPPMAX clusters:

|                        |Rackham        |Snowy                     |Bianca                                      |
|------------------------|---------------|--------------------------|--------------------------------------------|
|**Purpose**             |General-purpose|General-purpose           |Sensitive                                   |
|**# Intel CPU Nodes**   |486+144        |228                       |288                                         |
|**# GPU Nodes**         |-              |50, Nvidia T4             |10, 2x Nvidia A100 each                     |
|**Cores per node**      |20/16          |16                        |16/64                                       |
|**Memory per node**     |128 GB         |128 GB                    |128 GB                                      |
|**Fat nodes**           |256 GB & 1 TB  |256, 512 GB & 4 TB        |256 & 512 GB                                |
|**Local disk (scratch)**|2/3 TB         |4 TB                      |4 TB                                        |
|**Login nodes**         |Yes            |No (reached from Rackham) |Yes (2 cores and 15 GB)                     |
|**"Home" storage**      |Domus          |Domus                     |Castor                                      |
|**"Project" Storage**   |Crex, Lutra    |Crex, Lutra               |Castor                                      |

## Detailed overview of the UPPMAX systems

```mermaid

  graph TB

  Node1 -- interactive --> SubGraph2Flow
  Node1 -- sbatch --> SubGraph2Flow
  subgraph "Snowy"
  SubGraph2Flow(calculation nodes) 
        end

        thinlinc -- usr-sensXXX + 2FA + VPN ----> SubGraph1Flow
        terminal -- usr --> Node1
        terminal -- usr-sensXXX + 2FA + VPN ----> SubGraph1Flow
        Node1 -- usr-sensXXX + 2FA + no VPN ----> SubGraph1Flow
        
        subgraph "Bianca"
        SubGraph1Flow(Bianca login) -- usr+passwd --> private(private cluster)
        private -- interactive --> calcB(calculation nodes)
        private -- sbatch --> calcB
        end

        subgraph "Rackham"
        Node1[Login] -- interactive --> Node2[calculation nodes]
        Node1 -- sbatch --> Node2
        end
```

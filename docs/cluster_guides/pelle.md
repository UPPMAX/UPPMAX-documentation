---
tags:
  - Pelle
  - cluster
  - general-purpose
---

# Pelle

![Image of Pelle Svanslös, from https://www.comics.org/issue/105368/cover/4](./img/pelle.jpg)

- [Pelle's name](pelles_name.md)

Pelle is an upcoming general-purpose UPPMAX cluster,
paid by Uppsala University.

Uppsala users of [Rackham](rackham.md) will be moved to Pelle
by UPPMAX after [applying to a Pelle project](../getting_started/project_apply_pelle.md).

Non-Uppsala users of [Rackham](rackham.md) can move their data to
Dardel, see [the Rackham to Dardel migration guide](../cluster_guides/dardel_migration.md).

???- question "Why use Pelle over another NAISS system?"

    Here is a table of why you want to use Pelle over another NAISS
    HPC cluster.

    Parameter|Tetralith|Pelle
    Max job time|10 days|Longer
    Storage per compute|Decent|High

???- question "What is the status of Pelle?"

    See [the Pelle status page](https://status.uppmax.uu.se/2025-04-09/pelle/)

    **Pelle is now open for all users for testing. Welcome!**

    Let us know if you are missing your favorite tools. We'll install those on demand.

???- question "What is different on Pelle in comparison to Rackham?"

    New operating system

    - Pelle is running [Rocky Linux 9](https://rockylinux.org/).
    - Most system software, including the Linux kernel, have newer versions compared to Rackham and other UPPMAX clusters.

    Hardware

    - Pelle's compute nodes have much more CPU cores and memory compared to previous UPPMAX cluster. 
    - All compute nodes have AMD Zen4 processors.
    - Details about the hardware is on the [Pelle/Maja
hardware](../hardware/clusters/pelle.md) page.

    Software installations

    - Software available on Pelle is not included in the Software list on
this web page yet.
    - Please use the [module system](modules.md) to list
available software, for example by running `module avail` or `module
spider`.

    Compute nodes

    - 48 physial cores (96 logical cores) per node, instead of 20.
    - No node/core partitions
    - No devel partition
    - Job memory specification
    - Simultaneous multithreading/Hyper-threading

!!! info

    - You can reach all Rackham/Crex projects from Pelle!
    - Transition from Crex storage to Gorilla storage will be made from our side. You do not have to do anything!
    
## [How to apply to a Pelle project](../getting_started/project_apply_pelle.md)

## [How to log in to Pelle](../getting_started/login_pelle.md)

## Features of Pelle, compared to Rackham

Pelle is quite similar to [Rackham](rackham.md) but we have prepared Pelle specific pages for some topics.

- [File transfer](transfer_pelle.md)
- [The module system](pelle_modules.md)
- [Slurm on Pelle](slurm_on_pelle.md)
- [Starting an interactive session](start_interactive_session_on_pelle.md)
- [IDEs](../software/ides_on_pelle.md)

???- warning "We are still preparing documentation of these subjects"

    - [IDEs](../software/ides_on_pelle.md)
        - Jupyter
        - RStudio
        - VSCode
    - Isolated environments
        - venv
    - Run webexport

## Migration from Rackham to Pelle

As both clusters are UPPMAX clusters,
we will transfer your data from [Rackham](rackham.md)
to Pelle. Users will have to [apply to a Pelle project](../getting_started/project_apply_pelle.md).

## Pelle hardware

[Pelle/Maja hardware](../hardware/clusters/pelle.md)

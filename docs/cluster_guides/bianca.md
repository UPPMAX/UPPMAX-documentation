---
tags:
  - Bianca
  - cluster
  - sensitive data
---

# Bianca

![Bianca Castafiore, from https://en.wikipedia.org/wiki/File:Bianca_Castafiore-Tintin_comics_series.png](./img/bianca_castafiore_192_x_226.png)

[Bianca](bianca.md) is one of the [UPPMAX clusters](uppmax_cluster.md),
suitable for working with sensitive data.

!!! info

    We are now officially running parts of Bianca on Maja nodes!

    Short story:

    If you run 256 GB memory jobs on Bianca you may use the new faster Maja hardware!

??? info "Long story (5 Feb)"

    Starting yesterday 4 February we have added 35 compute nodes to Bianca.

    The new Maja nodes are the same model as in Pelle. Every Maja node is currently running three virtual Bianca nodes with 16 cores and 256 GB RAM each.

    We may have to fine tune Slurm and the meta scheduler for Bianca further ahead to make efficient use of the new Maja hardware.

    The new Maja nodes are running a single AMD EPYC 9454P with 48 cores and 768 GB RAM and the majority of the old Bianca nodes are running two Intel E5-2630 with 8 cores each and 128 GB RAM.

    To use the new nodes, there is a high probability you get them if you start jobs with -C mem256GB

    We also unfortunatelly also have an old limitation of maximum five 256 GB RAM nodes per running project. But since we now have 105 new and 54 old nodes with 256 GB RAM we would love to increase that number. But. Read more below.

    Upgrade login nodes to 30 GB RAM

    Since we got a lot of 256 GB RAM nodes now we have started to use some of the older ones to upgrade the virtual login nodes for Bianca from 15 GB to 30 GB RAM each. They still have two cores each. We can fit 8 virtual login nodes with 2 cores and 30 GB RAM each in a server with 256 GB RAM.

    Future possible upgrade of older 128 GB RAM nodes to 256 GB nodes

    The memory of the decomissioned Rackham seems to fit in Bianca. It seems to be very possible to upgrade the 128 GB RAM nodes in Bianca to 256 GB RAM. No 128 GB RAM nodes would be left.

    If we do this upgrade, we would have to think a bit on how to configure the meta scheduler and Slurm for Bianca for all nodes to be used efficiently. With so many 256 GB nodes we cannot use the sise of the nodes to choose between type. We also do not want to change too much on how users are launching jobs on Bianca. We would like the upgrade to be mostly seamless.

    Maybe we can use the Maja hardware to run 512 + 256 GB or 768 GB RAM virtual nodes then instead. If such a node is requested then that would mean it would get the fastest CPUs too.

    The fattest Rackham nodes may also be able to donate memory to Bianca. From them we can build either four 1 TB RAM nodes in Bianca, which would be new for Bianca, or maybe eight more 512 GB RAM nodes. Some users have expressed a big interest in large memory nodes also on Bianca.

    One tricky thing is that both Slurm and OpenStack has ideas on the sise of the nodes being requested and started up. The nodes provided to the virtual cluster has to be in the right sise or larger for the jobs to start running.

    Other nice side-effects by repurposing clusters

    Surprisingly enough the new storage nodes for Gorilla accept the same generation of memory, DDR4, and the exact same speed as installed on some of the fatter nodes of Rackham and Bianca.

    We have discovered after running Gorilla for a while that they preferred a bit more memory than we initially expected to get Ceph happy. So some of the excess memory from Rackham has now been repurposed to upgrade storage nodes in Gorilla from 256 to 384 GB RAM. This upgrade was welcome.

- [Bianca's name](biancas_name.md)
- [Bianca's design](biancas_design.md)
- [Bianca's hardware](../hardware/clusters/bianca.md)
- NAISS-sens
    - [Project application(../getting_started/project_apply_bianca.md]
- [Log in](../getting_started/login_bianca.md)
- [Directory structure for projects](bianca_file_tree.md)
- [File transfer](transfer_bianca.md)
    - [File transfer using rsync](../software/bianca_file_transfer_using_rsync.md) (recommended)
    - [File transfer using FileZilla](../software/bianca_file_transfer_using_filezilla.md) (easiest)
- [The module system](bianca_modules.md)
    - [R packages](../software/r.md#r-packages)
    - [Python](../software/python.md)
- [Submitting jobs, using Slurm](slurm.md)
- [Starting an interactive session](start_interactive_session_on_bianca.md)
- [IDEs](../software/ides_on_bianca.md)
    - [Jupyter](../software/jupyter_on_bianca.md)
    - [RStudio](../software/rstudio_on_bianca.md)
    - [VSCodium](../software/vscodium_on_bianca.md)
    - :no_entry: [VSCode](../software/vscode_on_bianca.md)
- [Bianca workshops](https://uppmax.github.io/bianca_workshops/)
- Best practices
    - [Git on Bianca](../software/git_on_bianca.md)
- Bianca installation guides
    - [link to course material](https://uppmax.github.io/bianca_workshops/intermediate/install/)

# Snowy's design

[Snowy](snowy.md) is an (general-purpose) high-performance computing (HPC) cluster,
with GPUs and suitable for longer jobs.

???- question "What is an HPC cluster?"

    What an HPC cluster is, is described [here](uppmax_cluster.md).

Or: Snowy is a group of computers that can effectively run many calculations,
as requested by multiple people, at the same time.
Snowy runs the Linux operating system and all users need some
basic Linux knowledge to use Snowy.

Additionally, Snowy has GPUs and allows for jobs running for maximally 30 days.

Snowy does not have a [login node](../cluster_guides/login_node.md).
Instead, it uses a login node on [Rackham](rackham.md).

???- tip "Using Linux"

    Using Linux (and especially the so-called command-line/[terminal](../software/terminal.md)) is essential
    to use Snowy. Learning the essential Linux commands
    is described [here](../getting_started/linux.md).

## Snowy's system configuration

Snowy consists of 228 compute servers (nodes) where each compute server
consists of two 8-core Xeon E5-2660 processors running at 2.2 GHz.
We provide 198 nodes with 128 GB memory (`s1-s120`, `s151-s228`),
13 nodes with 256 GB (`s138-s150`) and 17 nodes with 512 GB (`s121-s137`).
All nodes are interconnected with a 2:1
oversubscribed FDR (40 GB/s) Infiniband fabric.
In total Snowy provides 3548 CPU cores in compute nodes.

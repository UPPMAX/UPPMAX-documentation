# Bianca

Bianca is one of the [UPPMAX clusters](uppmax_cluster.md).

Here we describe [Bianca's name](#bianca's-name)
and [Bianca's design](#bianca's-design).

!!! info "[Go to the Bianca portal](bianca_portal.md)"

    [The Bianca portal](bianca_portal.md) 
    is the starting page on using Bianca.

## Bianca's name

Bianca, like all [UPPMAX clusters](uppmax_cluster.md), 
is named after a Tintin character,
in this case after Bianca Castafiore.

![Bianca Castafiore, from https://en.wikipedia.org/wiki/File:Bianca_Castafiore-Tintin_comics_series.png](./img/bianca_castafiore_192_x_226.png)

???- question "What are the UPPMAX clusters?"

    All UPPMAX clusters can be found [here](uppmax_cluster.md).

## Bianca's design

Bianca is an high-performance computing (HPC) cluster for sensitive data.

???- question "What is an HPC cluster for sensitive data?"

    What an HPC cluster for sensitive data is, is described [here](uppmax_cluster.md).

Or: Bianca is a group of computers that can effectively run many calculations, 
as requested by multiple people, at the same time.
As the data is sensitive, it is protected to remain only on Bianca.

Bianca is designed to

- Protect the sensitive data: 
    - (1a) Accidental data leaks should be difficult
    - (1b) Law: if data is leaked, the person doing so should be possibly identified
- Emulate a standard HPC cluster environment:
    - (2a) Use the hardware as efficient as possible
    - (2b) Distributes shared resources (CPU, memory) in a fair way
    - (2c) make correct data management as easy as possible

Bianca runs the Linux operating system and all users need some
basic Linux knowledge to use her.

???- tip "Using Linux"

    Using Linux (and especially the so-called command-line/terminal) is essential
    to use Bianca. Learning the essential Linux commands 
    is described [here](../getting_started/linux.md).

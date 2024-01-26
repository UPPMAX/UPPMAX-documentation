# Snowy

Snowy is one of the [UPPMAX clusters](uppmax_cluster.md).

Here we describe [Snowy's name](#snowy's-name)
and [Snowy's design](#snowy's-design).

!!! info "[Go to the Snowy portal](snowy_portal.md)"

    [The Snowy portal](snowy_portal.md) 
    is the starting page on using Snowy.

## Snowy's name

Snowy, like all [UPPMAX clusters](uppmax_cluster.md), 
is named after a Tintin character,
in this case after Snowy, Tintin's dog:

![Snowy, from https://www.deviantart.com/shannonmai2002art/art/Snowy-From-Tintin-504387373](./img/snowy_120_x_186.jpg)

???- question "What are the UPPMAX clusters?"

    All UPPMAX clusters can be found [here](uppmax_cluster.md).

## Snowy's design

Snowy is an (general-purpose) high-performance computing (HPC) cluster,
with GPUs and suitable for longer jobs.

???- question "What is an HPC cluster?"

    What an HPC cluster is, is described [here](uppmax_cluster.md).

Or: Snowy is a group of computers that can effectively run many calculations, 
as requested by multiple people, at the same time.
Snowy runs the Linux operating system and all users need some
basic Linux knowledge to use Snowy.

Additionally, Snowy has GPUs and allows for jobs running for maximally 30 days. 

Snowy does not have a login node. Instead, it uses a login node on [Rackham](rackham.md).

???- tip "Using Linux"

    Using Linux (and especially the so-called command-line/terminal) is essential
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

## Compiling on Snowy

There are several compilers available through 
the [module system](modules.md) on Snowy. 
This gives you flexibility to obtain programs that run optimally on Snowy.

*   gcc - the newest version usually generates the best code, if you tell it to use the new instructions. Check which version is the newest by doing **module avail**.  
    The compiler executable is named gcc for C, g++ for C++, and gfortran for Fortran.
    To use the new instructions available on Snowy (AVX2 and FMA3), give the additional options "**\-mavx2 -mfma3**" to gcc. For good performance with this compiler you should also specify optimization at least at level **\-O2** or **\-O3**. Also try using **\-march=broadwell** for GCC >= 4.9.0 or **\-march=core-avx2** for GCC 4.8.x, which will enable all the instructions on the CPU.
*   Intel+MKL - usually generates the fastest code. As with gcc, it is good to use the latest version. The compiler executable is named icc for C, icpc for C++, and ifort for Fortran. You should give optimization options at least **\-O2**, preferably **\-O3** or **\-fast**. You can also try to use the **\-xCORE-AVX2** option to the compiler to output AVX2 instructions.
*   pgi - often generates somewhat slower code, but it is stable so often it is easier to obtain working code, even with quite advanced optimizations. The compiler executable is named pgcc for C, pgCC for C++, and pgfortran, pgf77, pgf90, or pgf95 for Fortran. For this compiler, you can generate code for Snowy using the following options "**UPDATES NEEDED**". Also give optimization options at least **\-O2**, preferably **\-Ofast**, even though the compile times are much longer, the result is often worth the wait.


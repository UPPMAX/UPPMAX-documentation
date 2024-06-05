# Intel VTune

There are multiple [profilers](profilers.md)
available on UPPMAX.
This page describes [Intel VTune](intel_vtune.md).

[Intel VTune](intel_vtune.md) is a broad set of tools
with a focus on performance improvement
of Intel-compiled code.

Intel's performance analysis suite can probably answer
any question you have about the performance of your code,
including MPI and OpenMP code.

VTune is focused choosing optimizing techniques that will yield good results,
whereas Amplifier is more broadly aimed at performance analysis.

In order to use VTune do the following:

```bash
module load intel-oneapi vtune
```

Making sure you have a graphical connection
through [SSH X-forwarding](ssh_x_forwarding.md) or [ThinLinc](thinlinc.md),
then run VTune graphically like this:

```bash
vtune-gui
```

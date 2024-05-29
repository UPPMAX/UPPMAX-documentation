# Intel Advisor

There are multiple [profilers](profilers.md)
available on UPPMAX.
This page describes [Intel Advisor](intel_advisor.md).

[Intel Advisor](intel_advisor.md) is a broad set of tools 
with a focus on performance analysis
of Intel-compiled code.

Intel's performance analysis suite can probably answer 
any question you have about the performance of your code, 
including MPI and OpenMP code.

In order to use Advisor, do the following:

```bash
module load intel intel-oneapi advisor
```

Making sure you have a graphical connection 
through [SSH X-forwarding](ssh_x_forwarding.md) or [ThinLinc](thinlinc.md), 
then run Advisor graphically like this:

```bash
advixe-gui
```

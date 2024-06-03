# Allinea DDT

UPPMAX has many [debuggers](debuggers.md) installed.
This page describes Allinea DDT ('Distributed Debugging Tool').

UPPMAX has 96 licenses (one license per (MPI) process)
that allows you to debug programs running in parallel
with up to 6 nodes on 16 cores or any other combination.
The licenses are shared between all users that are in active debugging session.


To use the graphical user interface
use [ssh with forwarding](ssh_x_forwarding.md)
or [ThinLinc](thinlinc.md).

To use the program load the `ddt` [module](../cluster_guides/modules.md)
from you command line:

```bash
module load ddt
```


To start the program run:

```bash
ddt
```

or

```bash
ddt ./myprogram
```

`ddt` can only do debugging if you have compiled your code with debugging flag options.

## Debugging Multithreaded programs

Start an interactive job with multiple
cores (e.g. `interactive -p core -n 20 -A snicXYZ -t 04:00:00`)
before starting DDT.
In the run window, select the OpenMP box.
You can change the number of OpenMP threads directly in the DDT window before running.

## Debugging MPI programs

To be able to debug MPI program select
MPI option as well as the 'Submit to Queue' option,
and then click on 'Change' to select submission script configuration
for Rackham and provide the job specific options:

- 'System | MPI/UPC Implementation | check Auto-Detect'
- 'System | MPI/UPC Implementation | tick Create Root and Workers group automatically'
- Select a template file depending on the partition you want to use:
    - `core`: 'Job Submission | Submission template file | Browse and select `/sw/comp/ddt/7.0/templates/rackham-core.qtf`
    - `node`: 'Job Submission | Submission template file | Browse and select `/sw/comp/ddt/7.0/templates/rackham-node.qtf`
    - `devcore`: 'Job Submission | Submission template file | Browse and select `/sw/comp/ddt/7.0/templates/rackham-node.qtf`
- 'Job Submission | tick Quick Restart':
  allows you to restart your program without cancelling
  the allocated time and allocating it again.
- Edit Queue Submission Parameters to specify Partition, Project and requested time.
  Failing to provide project number will cause failures in the submission process

On the main configuration window the button "Run" will change to "Submit".
Click on this button to submit your debugging session to the queue manager.

If you enable "Memory debugging",
click the "Details" button and tick 'Preload the memory debugging library'
and select "C/Fortran threads" in the "Language:" field.
Read the manual for more detail on the other options in this panel.

## Links

- [DDT home page](https://www.linaroforge.com/linaro-ddt) (formerly: Allinea, now Linaroforge)

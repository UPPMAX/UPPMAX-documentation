---
tags:
  - start
  - interactive
  - session
  - Bianca
---

# Starting an interactive session on Bianca

![Log in to Bianca via a terminal](./img/login_bianca_via_terminal_terminal_462_x_202.png)

This page describes how to start an interactive session on [Bianca](bianca.md).
See the [general information on starting an interactive session](start_interactive_node.md)
on how to do so in general.

???- question "Prefer a video?"

    See the video [Starting an interactive session on Bianca](https://youtu.be/hQkMKW41-u4)

To use an interactive session, in a [terminal](../software/terminal.md), type:

```bash
interactive -A [project name] -n [number_of_cores] -t [session_duration]
```

Where

- `[project name]` is your project name, for example `sens2023598`
- `[number_of_cores]` is the number of core, for example `2`
- `[session_duration]` is the duration of the session, for example `8:00:00`
  for eight hours

For example:

```bash
interactive -A sens2023598 -n 2 -t 8:00:00
```

This starts an interactive session using project `sens2023598`
that uses 2 cores and has a maximum duration of 8 hours.

The script [interactive](../software/interactive.md) has many same arguments
as [sbatch](../software/sbatch.md).

???- question "Forgot your Bianca projects?"

    One easy way to see your Bianca projects is to use the
    Bianca remote desktop login screen at <https://bianca.uppmax.uu.se/>.

    ![The Bianca remote desktop login screen](../getting_started/img/bianca_remote_desktop_login_shows_sens_projects.png)

!!! note "Has Bianca frozen?"

    It can take tens of minutes before an interactive session is allocated.
    
    Bianca has not frozen, go ahead and have a coffee break :-)

    You can see the regular timings at [cluster speeds](cluster_speeds.md).

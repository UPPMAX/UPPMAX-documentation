# Starting an interactive node on Bianca

![](./img/login_bianca_via_terminal_terminal_462_x_202.png)

This page describes how to start an interactive node on [Bianca](bianca.md),
unlike the [general information on starting an interactive node](start_interactive_node.md).

To use an interactive node, in a terminal, type:

```bash
interactive -A [project name] -n [number_of_cores] -t [session_duration]
```

For example:

```bash
interactive -A sens2023598 -n 2 -t 8:00:00
```

This starts an interactive session using project `sens2023598`
that uses 2 cores and has a maximum duration of 8 hours.

!!! note "Has Bianca frozen?"

    It can take tens of minutes before an interactive node is allocated.

    Bianca has not frozen, go ahead and have a coffee break :-)

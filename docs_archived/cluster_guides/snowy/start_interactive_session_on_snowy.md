---
tags:
  - start
  - interactive
  - session
  - Snowy
---

# Starting an interactive session on Snowy

![Log in to Rackham4 via a terminal](./img/login_rackham4_via_terminal_terminal_395_x_204.png)

This page describes how to start an interactive session on [Snowy](snowy.md),
unlike the [general information on starting an interactive session](start_interactive_session.md).

To start an interactive session, in a [terminal](../software/terminal.md), type:

```bash
interactive -A [project name] -M snowy
```

For example:

```bash
interactive -A uppmax2023-2-25 -M snowy
```

This starts an interactive session using project `uppmax2023-2-25`
that has a default duration of 1 hours.

???- tip "Forgot your Snowy project?"

    One can go to the SUPR NAISS pages to see one's projects,

    ![Example of the Snowy project called 'UPPMAX 2023/2-25'](./img/naiss_supr_project_2023_2_25.png)

    > Example of the Snowy project called 'UPPMAX 2023/2-25'

    On the SUPR NAISS pages, projects are called 'UPPMAX [year]/[month]-[day]',
    for example, 'UPPMAX 2023/2-25'.
    The UPPMAX project name, as to be used on Snowy,
    has a slightly different name:
    the account name to use on Snowy is `uppmax[year]-[month]-[day]`,
    for example, `uppmax2023-2-25`

To increase the duration of the interactive session,
add the use of `-t`:

```bash
interactive -A [project name] -M snowy -t [session_duration]
```

For example:

```bash
interactive -A uppmax2023-2-25 -M snowy -t 8:00:00
```

This starts an interactive session using project `uppmax2023-2-25`
that has a maximum duration of 8 hours.

!!! note "Has Snowy frozen?"

    It can take tens of seconds before the computer
    core(s)/node(s) are allocated.

    Snowy has not frozen, just be a bit more patient.

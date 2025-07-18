---
tags:
  - text
  - editor
  - editors
  - text editor
  - text editors
---

# Text editors

There are many editors that can be used on the UPPMAX clusters:

Editor type                                                 |Features
------------------------------------------------------------|-----------------------------------------------------
[Simple terminal editors](#simple-terminal-editors)         |Used in [terminal](../software/terminal.md), easy to learn, limited features
[Advanced terminal editors](#advanced-terminal-editors)     |Used in [terminal](../software/terminal.md), harder to learn, powerful features
[Simple graphical editors](#simple-graphical-editors)       |Graphical, needs [X forwarding](../software/ssh_x_forwarding.md), easy to learn, limited features
[Advanced graphical editors](#advanced-graphical-editors)   |Graphical, needs [X forwarding](../software/ssh_x_forwarding.md), harder to learn, powerful features

Try them out and pick one favorite editor!

!!! tip

    **These commands are useful in the command line when something is stuck or a program is limiting you to do further work.**

    - ``ctrl-C`` interrupts a program or a command that is "stuck"
    - ``ctrl-D`` quits some programs from the program environment in the terminal
    - ``ctrl-Z`` pauses a program, can be continued in background (`bg`) or  foreground (`fg`)

## Simple terminal editors

- [nano](nano.md): used in terminal, easy to learn, limited features

## Advanced terminal editors

!!! warning

    - we suggest that you learn this tools before trying to work with them on UPPMAX
    - If you start one of these editors you may have difficulties to exit!

- [emacs](../software/emacs.md)
- [vim](../software/vim.md)

## Simple graphical editors

To use a graphical editors you will need to:

- work on an UPPMAX cluster that allows [SSH X forwarding](../software/ssh_x_forwarding.md)
- login with [SSH X forwarding](../software/ssh_x_forwarding.md) enabled

See the [SSH X forwarding page](../software/ssh_x_forwarding.md) how to do so.

???- question "And what about Bianca?"

    Bianca is an UPPMAX cluster that does not allow [X forwarding](../software/ssh_x_forwarding.md).

    See [the 'How to login to Bianca' page](../getting_started/login_bianca.md)
    for more details.

### [gedit](gedit.md)

See [gedit](gedit.md)

## Advanced graphical editors

### gvim

- `vim` with a GUI, lots of features, very fast

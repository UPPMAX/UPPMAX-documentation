---
tags:
  - terminal
---

# Terminal

![A terminal](./img/xeyes_no_ssh_x_forwarding.png)

> A terminal.

A terminal is a program that allows you to run commands.

???- question "How to copy-paste to/from a terminal?"

    This depends on the terminal you use, however,
    this is the most common options:

    Press `CTRL + SHIFT + C` for copt, `CTRL + SHIFT + V` for pasting.

???- question "What does all the stuff on the line I can type on mean?"

    The text at the start of the line you can type on,
    is called the command prompt. It indicates
    that the terminal is waiting for user input.

    Here is an example prompt:

    ```bash
    [sven@rackham2 my_folder]$ 
    ```

    - `[` and `]`: indicates the beginning and end of information
    - `sven`: the username
    - `@`: at which cluster
    - `rackham2`: the remote node's name,
      in this case Rackham's second login node
    - `my_folder`: (part of) the path of the user,
      in this case, a folder called `my_folder`.
      The indication `~` means that the user in the home folder
    - `$`: indicate to be ready for user input

    The node's name is useful to find out where you are:

    Name                    |Location
    ------------------------|---------------------------
    `rackham1` to `rackham4`|A Rackham login node
    `r1` and higher         |A Rackham compute node node
    `bianca`                |A Bianca login node
    `b1` and higher         |A Bianca compute node


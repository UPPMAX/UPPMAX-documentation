# SSH client

An SSH client is a program that allows on to use SSH.

## Overview of SSH clients

Operating system|SSH Client|Provides SSH with [X forwarding](ssh_x_forwarding.md)
----------------|----------|-----------------------------------------------------
Linux           |`ssh`     |Yes
MacOS           |`ssh`     |Yes, after installing [XQuartz](https://www.xquartz.org/)
Windows         |MobaXterm |Yes
Windows         |PuTTY     |Yes, after installing [Xming](www.straightrunning.com/XmingNotes/)

- [X forwarding](ssh_x_forwarding.md) allows one to use graphical applications

For Windows, we recommend MobaXterm, as it has a built-in X server.

### `ssh`

`ssh` is an SSH client that comes already installed with Linux and MacOS.
Its usage is described at the UPPMAX page on `ssh` [here](ssh.md).

### MobaXterm

MobaXterm is an SSH client that is easy to use and install for Windows.
When MobaXterm is started, start a terminal to run `ssh`.
The usage of `ssh` is described at the UPPMAX page on `ssh` [here](ssh.md).

 * [MobaXterm homepage](https://mobaxterm.mobatek.net/)

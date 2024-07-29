# SSH client

An SSH client is a program that allows on to use SSH.

## Overview of SSH clients

Operating system|SSH Client               |Recommended?|Allows graphics? [1]|Description
----------------|-------------------------|------------|--------------------|---------------------------------
Linux           |[`ssh`](ssh.md)          |Yes         |Yes                 |Start from a terminal
MacOS           |[`ssh`](ssh.md)          |Yes         |Yes [2]             |Start from a terminal, needs install for graphics [2]
Windows         |[MobaXterm](mobaxterm.md)|Yes         |Yes                 |Easiest for Windows users [5]
Windows         |PuTTY                    |Neutral     |Yes [3]             |Needs install for graphics [3]
Windows         |[`ssh`](ssh.md)          |Neutral     |Unknown             |Start from `CMD`, later Windows versions [4]
Windows         |[`ssh`](ssh.md)          |Neutral     |Unknown             |Start from PowerShell [4]

- [1] The technical question is 'Allows [X forwarding](ssh_x_forwarding.md)',
  as this is the way graphical displays are allowed
- [2] After installing [XQuartz](https://www.xquartz.org/)
- [3] After installing [Xming](http://www.straightrunning.com/XmingNotes/#head-13)
- [4] Untested
- [5] [MobaXterm](mobaxterm.md) has a built-in X server

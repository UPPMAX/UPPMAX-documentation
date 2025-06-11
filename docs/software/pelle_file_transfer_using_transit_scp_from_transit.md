---
tags:
  - transfer
  - data transfer
  - file transfer
  - Transit
  - transit
  - Pelle
  - SCP
  - scp
---

# Data transfer to/from Pelle using Transit using SCP from Transit

!!! warning "Does not work yet"

    [Pelle](../cluster_guides/pelle.md) is a new UPPMAX HPC cluster
    that is in the process of being deployed.

    The procedure as described on this page does not work yet or is untested.

    This page will be updated when this works.

There are multiple ways to [transfer data to/from Pelle](../cluster_guides/transfer_pelle.md).

One can use SCP to copy files between Pelle and Transit,
from either Pelle or Transit.

One can transfer files to/from Pelle using the UPPMAX Transit server,
using SCP.
The program `scp` allows you to copy file between Pelle and Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Transit

Use a [terminal](../software/terminal.md) to login to Transit.

???- question "Forgot how to login to Transit?"

    A step-by-step guide how to login to Transit
    See [our step-by-step guide how to login to Transit](../cluster_guides/login_transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

## 3a. Run `scp` to copy files from Transit to Pelle

In the terminal, run `scp` to copy files from Transit to Pelle by doing:

```bash
scp [username]@pelle.uppmax.uu.se:/home/[username]/[file_on_pelle] [path_on_transit]
```

where `[file_on_pelle]` is the name of a file on Pelle,
`[username]` is your UPPMAX username,
and `[path_on_transit]` is the target path on Transit,
for example:

```bash
scp sven@pelle.uppmax.uu.se:/home/sven/my_pelle_file.txt .
```

Where `.` means 'the directory where I am now on Transit'.

## 3b. :no_entry: Run `scp` to copy files from Pelle to Transit

This is how you **would** copy a file from Pelle to Transit:
in the terminal, run `scp` to copy files from Pelle to Transit by doing:

```bash
scp [file_on_pelle] [username]@transit.uppmax.uu.se
```

where `[file_on_transit]` is the name of a file on Transit
and `[username]` is your UPPMAX username, for example:

```bash
scp my_local_pelle_file.txt [username]@transit.uppmax.uu.se
```

However, [Transit is a service, not a file server](../cluster_guides/transit.md).
The `scp` command will complete successfully,
yet the file will not be found on Transit.

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

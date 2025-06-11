---
tags:
  - transfer
  - data transfer
  - file transfer
  - SCP
  - scp
  - Transit
  - transit
  - Pelle
---

# Data transfer to/from Pelle using Transit using SCP from Pelle

!!! warning "Does not work yet"

    [Pelle](../cluster_guides/pelle.md) is a new UPPMAX HPC cluster
    that is in the process of being deployed.

    The procedure as described on this page does not work yet or is untested.

    This page will be updated when this works.

There are multiple ways to [transfer data to/from Pelle](../cluster_guides/transfer_pelle.md).

One can transfer files to/from Pelle using the UPPMAX Transit server, using SCP.
The program `scp` allows you to copy file between Pelle and Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Pelle

Use a [terminal](../software/terminal.md) to login to Pelle.

???- question "Forgot how to login to Pelle?"

    See [this step-by-step guide how to login to Pelle](../getting_started/login_pelle.md).

    Spoiler: `ssh [username]@pelle.uppmax.uu.se`

## :no_entry: 3a. Run `scp` to copy files from Pelle to Transit

This is how you **would** copy a file from Pelle to Transit:
in the terminal, run `scp` to copy files from Pelle to Transit by doing:

```bash
scp [file_on_pelle] [username]@transit.uppmax.uu.se
```

where `[file_on_pelle]` is the name of a file on Pelle
and `[username]` is your UPPMAX username, for example:

```bash
scp my_pelle_file.txt [username]@transit.uppmax.uu.se
```

However, [Transit is a service, not a file server](../cluster_guides/transit.md).
The `scp` command will complete successfully,
yet the file will not be found on Transit.

## 3b. Run `scp` to copy files from Transit to Pelle

In the terminal, run `scp` to copy files from Transit to Pelle by doing:

```bash
scp [file_on_pelle] [username]@transit.uppmax.uu.se
```

where `[file_on_pelle]` is the name of a file on Pelle
and `[username]` is your UPPMAX username, for example:

```bash
scp my_pelle_file.txt [username]@transit.uppmax.uu.se
```

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

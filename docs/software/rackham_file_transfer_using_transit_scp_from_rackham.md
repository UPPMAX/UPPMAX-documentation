---
tags:
  - transfer
  - data transfer
  - file transfer
  - SCP
  - scp
  - Transit
  - transit
  - Rackham
---

# Data transfer to/from Rackham using Transit using SCP from Rackham

There are multiple ways to [transfer data to/from Rackham](../cluster_guides/transfer_rackham.md).

One can transfer files to/from Rackham using the UPPMAX Transit server, using SCP.
The program `scp` allows you to copy file between Rackham and Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Rackham

Use a [terminal](../software/terminal.md) to login to Rackham.

???- question "Forgot how to login to Rackham?"

    A step-by-step guide how to login to Rackham
    can be found [here](../getting_started/login_rackham.md).

    Spoiler: `ssh [username]@rackham.uppmax.uu.se`

## :no_entry: 3a. Run `scp` to copy files from Rackham to Transit

This is how you **would** copy a file from Rackham to Transit:
in the terminal, run `scp` to copy files from Rackham to Transit by doing:

```bash
scp [file_on_rackham] [username]@transit.uppmax.uu.se
```

where `[file_on_rackham]` is the name of a file on Rackham
and `[username]` is your UPPMAX username, for example:

```bash
scp my_rackham_file.txt [username]@transit.uppmax.uu.se
```

However, [Transit is a service, not a file server](../cluster_guides/transit.md).
The `scp` command will complete successfully,
yet the file will not be found on Transit.

## 3b. Run `scp` to copy files from Transit to Rackham

In the terminal, run `scp` to copy files from Transit to Rackham by doing:

```bash
scp [file_on_rackham] [username]@transit.uppmax.uu.se
```

where `[file_on_rackham]` is the name of a file on Rackham
and `[username]` is your UPPMAX username, for example:

```bash
scp my_rackham_file.txt [username]@transit.uppmax.uu.se
```

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

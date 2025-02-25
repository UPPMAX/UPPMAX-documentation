---
tags:
  - transfer
  - data transfer
  - file transfer
  - Transit
  - transit
  - Rackham
  - SCP
  - scp
---

# Data transfer to/from Rackham using Transit using SCP from Transit

There are multiple ways to [transfer data to/from Rackham](../cluster_guides/transfer_rackham.md).

One can use SCP to copy files between Rackham and Transit,
from either Rackham or Transit.

One can transfer files to/from Rackham using the UPPMAX Transit server,
using SCP.
The program `scp` allows you to copy file between Rackham and Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Transit

Use a [terminal](../software/terminal.md) to login to Transit.

???- question "Forgot how to login to Transit?"

    A step-by-step guide how to login to Transit
    can be found [here](../cluster_guides/login_transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

## 3a. Run `scp` to copy files from Transit to Rackham

In the terminal, run `scp` to copy files from Transit to Rackham by doing:

```bash
scp [username]@rackham.uppmax.uu.se:/home/[username]/[file_on_rackham] [path_on_transit]
```

where `[file_on_rackham]` is the name of a file on Rackham,
`[username]` is your UPPMAX username,
and `[path_on_transit]` is the target path on Transit,
for example:

```bash
scp sven@rackham.uppmax.uu.se:/home/sven/my_rackham_file.txt .
```

Where `.` means 'the directory where I am now on Transit'.

## 3b. :no_entry: Run `scp` to copy files from Rackham to Transit

This is how you **would** copy a file from Rackham to Transit:
in the terminal, run `scp` to copy files from Rackham to Transit by doing:

```bash
scp [file_on_rackham] [username]@transit.uppmax.uu.se
```

where `[file_on_transit]` is the name of a file on Transit
and `[username]` is your UPPMAX username, for example:

```bash
scp my_local_rackham_file.txt [username]@transit.uppmax.uu.se
```

However, [Transit is a service, not a file server](../cluster_guides/transit.md).
The `scp` command will complete successfully,
yet the file will not be found on Transit.

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

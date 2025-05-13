---
tags:
  - transfer
  - data transfer
  - file transfer
  - scp
  - SCP
  - Pelle
---

# Data transfer to/from Pelle using SCP

!!! warning "Does not work yet"

    [Pelle](../cluster_guides/pelle.md) is a new UPPMAX HPC cluster
    that is in the process of being deployed.

    File transfer to/from Pelle using FileZilla does not work yet.

    This page will be updated when this works.

There are multiple ways to [transfer files to or from Pelle](../cluster_guides/transfer_pelle.md).

Here it is described how to do file transfer to/from Pelle using SCP.
SCP is an abbreviation of 'Secure copy protocol',
however, it is not considered 'secure' anymore:
instead it is considered an outdated protocol.
The program `scp` allows you to transfer files to/from Pelle using SCP,
by coping them between your local computer and Pelle.

## Procedure

???- question "Prefer a video?"

    See this procedure as a video at [YouTube](https://youtu.be/tUr-gTXmpAA)

### 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

### 2. Copy files using `scp`

In the terminal, copy files using `scp` to connect to Pelle:

```bash
scp [from] [to]
```

Where `[from]` is the file(s) you want to copy, and `[to]` is the destination.
This is quite a shorthand notation!

This is how you copy a file from your local computer to Pelle:

```bash
scp [local_filename] [username]@pelle.uppmax.uu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your UPPMAX username, for example:

```bash
scp my_file.txt sven@pelle.uppmax.uu.se:/home/sven
```

To copy a file from Pelle to your local computer, do the command above in reverse order:

```bash
scp [username]@pelle.uppmax.uu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your UPPMAX username,
and `[local_folder]` is your local folder, for example:

```bash
scp sven@pelle.uppmax.uu.se:/home/sven/my_remote_file.txt /home/sven
```

### 3. If asked, give your UPPMAX password

If asked, give your UPPMAX password.
You can get rid of this prompt if you have setup SSH keys

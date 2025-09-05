---
tags:
  - transfer
  - data transfer
  - file transfer
  - scp
  - SCP
  - COSMOS
---

# Data transfer to/from COSMOS using scp

???- question "Why is this page at LUNARC?"

    It is the intention that this guide is moved to the LUNARC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

There are multiple ways to transfer files to or from COSMOS.
Here it is described how to do file transfer to/from COSMOS
using [scp](../software/scp.md).

## Procedure

### 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer

### 2. Copy files using `scp`

In the terminal, copy files using [`scp`](../software/scp.md) to connect to Cosmos:

```bash
scp [from] [to]
```

Where `[from]` is the file(s) you want to copy, and `[to]` is the destination.
This is quite a shorthand notation!

This is how you copy a file from your local computer to Cosmos:

```bash
scp [local_filename] [username]@cosmos.lunarc.lu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your LUNARC username, for example:

```bash
scp my_file.txt sven@cosmos.lunarc.lu.se:/home/sven
```

To copy a file from Cosmos to your local computer,
do the command above in reverse order:

```bash
scp [username]@cosmos.lunarc.lu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your LUNARC username,
and `[local_folder]` is your local folder, for example:

```bash
scp sven@cosmos.lunarc.lu.se:/home/sven/my_remote_file.txt /home/sven
```

### 3. If asked, give your LUNARC password

If asked, give your LUNARC password and TOTP code from your ["Pocket pass" application](https://lunarc-documentation.readthedocs.io/en/latest/getting_started/authenticator_howto/).

You may get rid of this prompt if you have setup SSH keys


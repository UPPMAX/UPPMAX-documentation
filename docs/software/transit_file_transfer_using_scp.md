---
tags:
  - transfer
  - data transfer
  - file transfer
  - scp
  - SCP
  - Transit
  - transit
---

# Data transfer to/from Transit using SCP

Data transfer to/from [Transit](../cluster_guides/transit.md) using [`scp`](scp.md)
is one of the ways ways to [transfer files to/from Transit](../cluster_guides/transfer_transit.md).

???- question "What is Transit?"

    Transit is an UPPMAX service to send files around.
    It is not a file server.

    See [the page about Transit](../cluster_guides/transit.md) for more detailed information.

???- question "What are the other ways to transfer files from/to Transit?"

    See [the other ways to transfer data to/from Transit](../cluster_guides/transfer_transit.md)

One **cannot** transfer files to/from Transit using [`scp`](scp.md):
[`scp`](scp.md) is not considered 'secure' anymore:
instead it is considered an outdated protocol.

The program [`scp`](scp.md) allows you to transfer files to/from Transit using SCP,
by coping them between your local computer and Transit.

## How to transfer files between a local computer and Transit

The process is:

### 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

### 2. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer


### 3a. Using `scp` to download from Transit

In the terminal, copy files using `scp` to download files from Transit:

```bash
scp [username]@transit.uppmax.uu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your UPPMAX username,
and `[local_folder]` is your local folder, for example:

```bash
scp sven@transit.uppmax.uu.se:/home/sven/my_remote_file.txt /home/sven
```

If asked, give your UPPMAX password.

You can get rid of this prompt if you have setup SSH keys

### :no_entry: 3b. Using `scp` to upload to Transit

This is how you **would** copy a file from your local computer to Transit:

```bash
scp [local_filename] [username]@transit.uppmax.uu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your UPPMAX username, for example:

```bash
scp my_file.txt sven@transit.uppmax.uu.se:/home/sven
```

However, Transit is not a file server.
The `scp` command will complete successfully,
yet the file will not be found on Transit.

If asked, give your UPPMAX password.
You can get rid of this prompt if you have setup SSH keys

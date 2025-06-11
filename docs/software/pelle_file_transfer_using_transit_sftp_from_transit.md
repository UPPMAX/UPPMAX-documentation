# Data transfer to/from Pelle using Transit and SFTP from Transit

!!! warning "Does not work yet"

    [Pelle](../cluster_guides/pelle.md) is a new UPPMAX HPC cluster
    that is in the process of being deployed.

    The procedure as described on this page does not work yet or is untested.

    This page will be updated when this works.

There are multiple ways to [transfer data to/from Pelle](../cluster_guides/transfer_pelle.md).

Data transfer to/from Pelle using [Transit](../cluster_guides/transit.md)
is one of the ways ways to transfer files to/from Pelle

One can transfer files to/from Pelle using the UPPMAX Transit server.
Transit is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Pelle using Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Transit

Use a [terminal](../software/terminal.md) to login to Transit

???- question "Forgot how to login to Transit?"

    See [our step-by-step guide how to login to Transit](../cluster_guides/login_transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

## 3. Run `sftp` to connect to Pelle

In the terminal, run `sftp` to connect to Pelle by doing:

```bash
sftp [username]@pelle.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
sftp sven@pelle.uppmax.uu.se
```

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

## 5. In `sftp`, upload/download files to/from Pelle

[Transit is a service, not a file server](../cluster_guides/transit.md).
This means that if you upload files to Transit using
[SFTP](../software/sftp.md),
they will remain there as long a the connection is active.
These files need to be forwarded to more permanent storage.

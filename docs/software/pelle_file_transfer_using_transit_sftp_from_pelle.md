# Data transfer to/from Pelle using Transit and SFTP from Pelle

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

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Pelle

Use a [terminal](../software/terminal.md) to login to Pelle.

???- question "Forgot how to login to Pelle?"

    A step-by-step guide how to login to Transit
    can be found [here](../getting_started/login_pelle.md).

    Spoiler: `ssh [username]@pelle.uppmax.uu.se`

## 3. Run `sftp` to connect to Transit

In the terminal, run `sftp` to connect to Transit by doing:

```bash
sftp [username]@transit.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
sftp sven@transit.uppmax.uu.se
```

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

## 5. In `sftp`, upload/download files to/from Transit

[Transit is a service, not a file server](../cluster_guides/transit.md).
This means that if you upload files to Transit using SFTP,
they will remain there as long a the connection is active.
These files need to be forwarded to more permanent storage.

Basic `sftp` command can be found [here](../software/sftp.md).

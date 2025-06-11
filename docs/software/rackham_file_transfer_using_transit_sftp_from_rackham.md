# Data transfer to/from Rackham using Transit and SFTP from Rackham

There are multiple ways to [transfer data to/from Rackham](../cluster_guides/transfer_rackham.md).

Data transfer to/from Rackham using [Transit](../cluster_guides/transit.md)
is one of the ways ways to transfer files to/from Rackham

One can transfer files to/from Rackham using the UPPMAX Transit server.
Transit is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Rackham using Transit.

The process is:

## 1. Get inside SUNET

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

## 2. Use the terminal to login to Rackham

Use a [terminal](../software/terminal.md) to login to Rackham.

???- question "Forgot how to login to Rackham?"

    See [this step-by-step guide how to login to Rackham](../getting_started/login_rackham.md).

    Spoiler: `ssh [username]@rackham.uppmax.uu.se`

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

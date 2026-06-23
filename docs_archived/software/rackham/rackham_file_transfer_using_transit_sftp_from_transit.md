# Data transfer to/from Rackham using Transit and SFTP from Transit

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

## 2. Use the terminal to login to Transit

Use a [terminal](../software/terminal.md) to login to Transit

???- question "Forgot how to login to Transit?"

    See [this step-by-step guide how to login to Transit](../cluster_guides/login_transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

## 3. Run `sftp` to connect to Rackham

In the terminal, run `sftp` to connect to Rackham by doing:

```bash
sftp [username]@rackham.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
sftp sven@rackham.uppmax.uu.se
```

## 4. If asked, give your UPPMAX password

You can get rid of this prompt if you have setup SSH keys

## 5. In `sftp`, upload/download files to/from Rackham

[Transit is a service, not a file server](../cluster_guides/transit.md).
This means that if you upload files to Transit using
[SFTP](../software/sftp.md),
they will remain there as long a the connection is active.
These files need to be forwarded to more permanent storage.

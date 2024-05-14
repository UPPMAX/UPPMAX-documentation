# `wharf`

`wharf` is a folder on [Bianca](bianca.md) used
for [file transfer on Bianca](transfer_bianca.md).

He it is described:

* [What is `wharf`?](#what-is-wharf)
* [The `wharf` location](#the-wharf-location)
* [`wharf` use](#wharf-use)
* [mounting `wharf`](#mounting-wharf)

## What is `wharf`?

The `wharf` is like a "postbox" :postbox: for data/file exchange
between the Internet restricted Bianca cluster
and the remaining of the World Wide Internet.
This "postbox" is reachable to transfer data from two internal servers -
`bianca-sftp.uppmax.uu.se` and `transit.uppmax.uu.se`.

## The `wharf` location

The path to this special folder is:

```
/proj/[project_id]/nobackup/wharf/[user_name]/[user_name]-[project_id]
```

where

* `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)
* `[user_name]` is the name of your [UPPMAX user account](../getting_started/user_account.md)

For example:

```
/proj/sens2023598/nobackup/wharf/sven/sven-sens2023598
```

## `wharf` use

To [transfer data from/to Bianca](transfer_bianca.md),
`wharf` is to folder where files are sent to/from.

Do not keep files in `wharf`, as this folder is connected to the outside
world and hence is a security risk. Instead, move your data to your project folder.

You have full access to your `wharf` and read-only access
to other users' `wharf` folders in that same project.

`wharf` is only accessible when [inside the university networks](../getting_started/get_inside_sunet.md).

## Mounting `wharf`

Mounting `wharf` means that a `wharf` folder is added to the
filesystem of your local computer, after which you can use
it like any other folder. The data shown in the folder is on Bianca,
not on your local harddisk.

One can mount `wharf` on your local computer using `sshfs`
when [inside the university networks](../getting_started/get_inside_sunet.md).
`sshfs` is available on most Linux distributions:

Distro            |Package name
------------------|-------------
Ubuntu            | `sshfs`
Fedora            | `fuse-sshfs`
RHEL7/CentOS7 [1] | `fuse-sshfs`
RHEL8 [2]         | `fuse-sshfs`
CentOS8 [3]       | `fuse-sshfs`

* [1] Enable EPEL repository
* [2] Enable `codeready-builder` repository
* [3] Enable `powertools` repository

UPPMAX does not have `sshfs` installed for security reasons.

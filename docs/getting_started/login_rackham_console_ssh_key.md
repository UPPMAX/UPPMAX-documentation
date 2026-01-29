---
tags:
  - login
  - log in
  - Rackham
  - console
  - terminal
  - SSH
search:
  boost: 0
---

# Login to the Rackham console environment using SSH keys

There are multiple ways to [log in to Rackham](login_rackham.md).

This page describes how to [log in to Rackham](login_rackham.md)
using a [terminal](../software/terminal.md) and an SSH key pair.

## 1. Get inside SUNET

When inside SUNET, one can access a Rackham console environment
using SSH and SSH keys.

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

This is considered a bit harder to setup,
but one only needs to type one password to login to Rackham.
If you don't mind typing your UPPMAX password twice,
an easier setup is [log in to the Rackham console environment with a password](login_rackham_console_password.md).

## 2. Use `ssh` to log in

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -A [user]@rackham.uppmax.uu.se
```

For example:

```bash
ssh -A sven@rackham.uppmax.uu.se
```

## 3. Type your UPPMAX password

Type your UPPMAX password.

## 4. You are in

Enjoy! You are in! To be precise, you are on a Rackham [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_session_on_rackham.md).

In a Rackham console environment:

- Text display is limited to 50kBit/s.
  This means that if you create a lot of text output,
  you will have to wait some time before you get your prompt back.
- Cut, copy and paste work as usual.
  Be careful to not copy-paste sensitive data!

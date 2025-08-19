---
tags:
  - login
  - log in
  - Rackham
  - console
  - terminal
  - password
  - ssh
  - SSH
---

# Login to the Rackham console environment with a password

There are multiple ways to [log in to Rackham](login_rackham.md).
This page describes how to do so using a terminal and a password.

If you want to get rid of using a password every time,
see [login to the Rackham console environment with an SSH key](login_rackham_console_ssh_key.md).

## Procedure

???- question "Prefer a video?"

    This procedure is also shown by [this YouTube video](https://youtu.be/TSVGSKyt2bQ).

### 1. Use `ssh` to log in

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [username]@rackham.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh sven@rackham.uppmax.uu.se
```

???- question "What does this look like the first time?"

    ```bash
    sven@svens_computer:~$ ssh sven@rackham.uppmax.uu.se
    The authenticity of host 'rackham.uppmax.uu.se (89.44.250.8<X>)' can't be established.
    ECDSA key fingerprint is SHA256:W/MazH3WrH0wKrHBOJpPbDaU4qeYGqiv3FRPsdXIsb4.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    - Type `yes`!

    - Other valid fingerprints are:
        - ``SHA256:y241gg8SExSktACnpD+OvROrMPTJcXYYdT/zYReef+k``
        - ``SHA256:hkhuV+0mUDL7N4Jpr8/OWInrORSAL5ZRpvAqfjyg7Jg``


???- question "Why no `-X`?"

    On Rackham, one can use `-X`:

    ```bash
    ssh -X username@rackham.uppmax.uu.se
    ```

    This option is only useful when you want to
    enable so-called [X forwarding](../software/ssh_x_forwarding.md):
    which allows you to run programs that require light graphics,
    such as [eog](../software/eog.md) to display an image.

???- question "Why no `-A`?"

    On Rackham, one can use `-A`:

    ```bash
    ssh -A username@rackham.uppmax.uu.se
    ```

    This option is only useful when you want to
    [log in to Rackham via the console using an SSH key](login_rackham_console_ssh_key.md).
    As we here use passwords (i.e. no SSH keys)
    to access Rackham, `-A` is unused
    and hence we simplify this documentation by omitting it.

## 2. Type your UPPMAX password

Type your UPPMAX password and press enter.
You will see no asterisks to indicate how many
characters you've typed in.

If you are outside
[the university networks](../getting_started/get_inside_sunet.md)
you will be asked for your UPPMAX 2-factor authentication number.

## 3. You are in

Enjoy! You are in! Or, to be precise,
you are in your home folder on a Rackham [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_session_on_rackham.md).

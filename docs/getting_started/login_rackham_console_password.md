# Login to the Rackham console environment with a password

There are multiple ways to [log in to Rackham](login_rackham.md).

This page describes how to [log in to Rackham](login_rackham.md)
using a terminal and a password.

## Procedure

### 1. Use `ssh` to log in

From a terminal, use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -X [username]@rackham.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:


```bash
ssh -X sven@rackham.uppmax.uu.se
```

`-X` enables so-called [X forwarding](../software/ssh_x_forwarding.md),
which allows you to run programs that require light graphics,
such as [eog](../software/eog) to display an image.

???- question "Can I log in without `-X`?"

    Yes!

    If you do not need [X forwarding](../software/ssh_x_forwarding.md)
    to run programs that require light graphics,
    omitting the `-X` is just fine.

???- question "Why no `-A`?"

    On Rackham, one can use `-A`:

    ```bash
    ssh -A username@rackham.uppmax.uu.se
    ```

    this option is only useful when you want to
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
you are in your home folder on a Rackham login node.

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive node](../cluster_guides/start_interactive_node_on_rackham.md).


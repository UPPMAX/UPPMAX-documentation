---
tags:
  - login
  - log in
  - Bianca
  - console
  - terminal
  - password
---

# Login to the Bianca console environment with a password

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a terminal and a password.

When inside SUNET, one can access a Bianca console environment
using SSH with an SSH password.

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 1. Use `ssh` to log in

From a terminal, use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [user]-[project name]@bianca.uppmax.uu.se
```

For example:

```bash
ssh sven-sens2023598@bianca.uppmax.uu.se
```

???- question "How does it look like when outside of SUNET?"

    [Here](https://youtu.be/W-PMTyNcbYI?si=iYxNToDb-EpTdnAO&t=79) you can
    see how this looks like when outside of SUNET.

    Spoiler: quite dull, as nothing happens until these is a timeout.

???- question "Why no `-A`?"

    On Bianca, one can use `-A`:

    ```bash
    ssh -A username@bianca.uppmax.uu.se
    ```

    this option is only useful when you want to
    [log in to Bianca via the console using an SSH key](login_bianca_console_ssh_key.md).
    As we here use passwords (i.e. no SSH keys)
    to access Bianca, `-A` is unused
    and hence we simplify this documentation by omitting it.

???- question "Why no `-X`?"

    On Rackham, one can use `-X`:

    ```bash
    ssh -X username@rackham.uppmax.uu.se
    ```

    However, on Bianca, this so-called
    [X forwarding](../software/ssh_x_forwarding.md) is disabled.
    Hence, we do not teach it :-)


## 2. Type your UPPMAX password with 2FA

Type your UPPMAX password,
directly followed by the UPPMAX 2-factor authentication number,
for example `verysecret678123`, then press enter.
In this case, the password is `verysecret` and `678123`
is the 2FA number.

After authenticated using the UPPMAX password and 2FA,
you are logged in on Bianca's shared network,
on a so-called 'jumphost'.

However, you will still need to login to your own
private virtual project cluster.
As you are already properly authenticated (i.e. using an UPPMAX password
and UPPMAX 2FA), you don't need 2FA anymore.

???- question "What is a virtual project cluster?"

    As Bianca holds sensitive data, by regulations,
    each Bianca project must be isolated from each other
    and are not allowed to, for example, share the same memory.

    One way to achieve this, would be to build one HPC cluster
    per project. While this would guarantee isolated project environments,
    this would be quite impractical.

    Instead, we create isolated project environments by using software,
    that creates so-called virtual clusters, as if they would be
    physical clusters. Like physical clusters, a virtual cluster
    has a guaranteed isolated project environment.

When you login to Bianca's shared network,
you will get a message of your project's login node status.
It can be `up and running` or `down`.
If it is `down`, the virtual cluster is started,
which may take some minutes.

## 3. Type your UPPMAX password

Type your UPPMAX password,
for example `verysecret`

## 4. You are in

Enjoy! You are in! Or, to be precise,
you are on the [login node](../cluster_guides/login_node.md) of your own virtual project cluster.

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive node](../cluster_guides/start_interactive_node_on_rackham.md).

By default, this node has one core,
hence if you need more memory or more CPU power,
you submit a job (interactive or batch),
and an idle node will be moved into your project cluster.

???- tip "Video: how to use a terminal and SSH to access the Bianca console environment"

    This video shows how to use a terminal and SSH to access
    the Bianca console environment: [YouTube](https://youtu.be/upBozh2BI5c)

## Troubleshooting

Here are some common errors and their solutions:

### Permission denied, please try again

```
Permission denied, please try again.
```

Here are questions to solve that problem:

```mermaid
flowchart TD
    error[Permission denied, please try again.]
    correct_password[Is your password correct?]
    added_2fa[Have you added a 2FA number at the end of your password?]
    added_correct_2fa[Have you added the correct 2FA number at the end of your password?]
    in_sunet[Are you within the university networks?]
    active_bianca_project[Is that Bianca project active?]
    member_of_bianca_project[Are you a member of that Bianca project]

    error --> correct_password
    error --> in_sunet
    
    in_sunet --> active_bianca_project

    correct_password --> added_2fa --> added_correct_2fa
    active_bianca_project --> member_of_bianca_project
```

???- question "How do I know my password is correct?"

    You don't. 

    It could be a typo: you don't see your password when you type (this is a
    security measure), so a typo is likely to occur. Also check if 'Caps Lock'
    is off.

    It could be that you've forgotten your password. That can happen to all of
    us. You can then reset your password at <https://suprintegration.uppmax.uu.se/getpasswd>
    
???- question "What do you mean 'Have you added a 2FA number at the end of your password?'?"

    When you type your password, this needs to be followed by a two-factor authentication
    number.

    For example, if your password is `verysecret` and `314159` is the 2FA number,
    you should type `verysecret314159`

???- question "What is the correct 2FA number?"

    The UPPMAX one, titled `[username]@UPPMAX`, for example `sven@UPPMAX`.

    When using UPPMAX, one needs to create other 2FAs too, such as for SUPR
    or the Uppsala VPN. Don't use those numbers to login to Bianca. 

???- question "How do I know if I am within the university networks?"

    If you login via `eduroam` you are within the university networks.

    When unsure, go to the Bianca remote desktop website at
    [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se):
    if this page does not load, you are outside of the university networks.

    See [How to get inside of the university networks](../getting_started/get_inside_sunet.md)
    if you outside of the university networks.

???- question "How do I know if the Bianca project is active?"

    A quick way to confirm your Bianca project is active:
    go to <https://bianca.uppmax.uu.se>
    and type your username. If the project is displayed, it is active.

    To confirm your project is active or inactive, use the SUPR NAISS website. 
    See [the UPPMAX documentation on projects](../getting_started/project.md)
    how to see if your project is active?

???- question "How do I know if I am a member of the Bianca project?"

    A quick way to confirm you are a member of the Bianca project:
    go to <https://bianca.uppmax.uu.se>
    and type your username. If the project is displayed,
    you are a member of the Bianca project.

    To confirm your project is active or inactive, use the SUPR NAISS website. 
    See [the UPPMAX documentation on projects](../getting_started/project.md)
    how to see which projects you are a member of.

---
tags:
  - login
  - log in
  - Pelle
  - console
  - terminal
  - password
  - ssh
  - SSH
---

# Login to the Pelle console environment with a password

There are multiple ways to [log in to Pelle](login_pelle.md).
This page describes how to do so using a terminal and a password.

If you want to get rid of using a password every time,
see [login to the Pelle console environment with an SSH key](login_pelle_console_ssh_key.md).

## Procedure

???- question "Prefer a video?"

    Watch the YouTube video
    [Login to the Pelle console environment with a password](https://youtu.be/zsw3QD_NinU)


## 1. Use `ssh` to log in

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [username]@pelle.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh sven@pelle.uppmax.uu.se
```

Using this login, graphics (i.e. images) on Pelle cannot be displayed.

???- question "How does this look like the first time?"

    ```bash
    sven@svens_computer:~$ ssh -X sven@pelle.uppmax.uu.se
    The authenticity of host 'pelle.uppmax.uu.se (89.44.250.8<X>)' can't be established.
    ECDSA key fingerprint is SHA256:W/MazH3WrH0wKrHBOJpPbDaU4qeYGqiv3FRPsdXIsb4.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    - Type `yes`!

    - Other valid fingerprints are:
        - ``SHA256:y241gg8SExSktACnpD+OvROrMPTJcXYYdT/zYReef+k``
        - ``SHA256:hkhuV+0mUDL7N4Jpr8/OWInrORSAL5ZRpvAqfjyg7Jg``


???- question "How can I display graphics on Pelle?"

    To display graphics (i.e. images) on Pelle, use `-X`:

    ```bash
    ssh -X username@pelle.uppmax.uu.se
    ```

    This option enable so-called
    [X forwarding](../software/ssh_x_forwarding.md),
    which allows you to run programs that require light graphics,
    such as [eog](../software/eog.md) to display an image.

???- question "Why no `-A`?"

    On Pelle, one can use `-A`:

    ```bash
    ssh -A username@pelle.uppmax.uu.se
    ```

    This option is only useful when you want to
    [log in to Pelle via the console using an SSH key](login_pelle_console_ssh_key.md).
    As we here use passwords (i.e. no SSH keys)
    to access Pelle, `-A` is unused
    and hence we simplify this documentation by omitting it.

## 2. Type your UPPMAX password

Type your UPPMAX password.

???- question "How does this look like?"

    ```bash
    Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

    (sven@pelle.uppmax.uu.se) Password:
    (sven@pelle.uppmax.uu.se)
    ```

   After which you'll asked for your TOTP. Go to the next step.

## 3. Type your TOTP

Type the TOTP from the UPPMAX 2-factor authentication service,
for example `123456`, then press enter.

???- question "How does this look like?"

    ```bash
    Second factor (TOTP UPPMAX):
    ```

## 4. You are in

Enjoy! You are in! Or, to be precise,
you are in your home folder on a Pelle [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_pelle.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_session_on_pelle.md).

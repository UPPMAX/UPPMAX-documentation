---
tags:
  - Bianca
  - ssh
  - SSH
  - ssh key
  - SSH key
  - ssh keys
  - SSH keys
  - ssh key pair
  - SSH key pair
  - create
---

# Create an SSH key pair for use with Bianca

This page describes [how to create and use an SSH key](ssh_key_use.md)
for the [Bianca](../cluster_guides/bianca.md) cluster.

## Procedure

This procedure will fail if:

- You are outside of the university networks,
  see [how to get inside the university networks](../getting_started/get_inside_sunet.md).
  [This video](https://youtu.be/-f0C66zIrwI) shows it will fail when being
  outside of the university networks

Here is the procedure.

### 1. Create an SSH key pair

On your local computer, create an SSH key pair with the following command:

???- question "Can I also do this from Rackham?"

    Yes.

    In that case, read 'Rackham' instead of 'local computer'

```bash
ssh-keygen -a 100 -t ed25519 -f ~/.ssh/id_ed25519_uppmax_login -C "My comment"
```

Here is a description of the flags:

- `-a 100`:  100 rounds of key derivations,
  making your key's password harder to brute-force,
  as is recommended
  [by this StackExchange post](https://security.stackexchange.com/a/144044)
- `-t ed25519`: type of encryption scheme
- `-f ~/.ssh/id_ed25519_uppmax_login`: specify filename,
  following the naming scheme as suggested
  [in this Superuser post](https://superuser.com/a/1261644)
- `-C "My comment"`: a comment that will be stored in the key, so you can find out what it was for

### 2. Add the content of your public key to Bianca's authorised keys

Add the content of the public key `id_ed25519_uppmax_login.pub`
on your local computer to the Bianca's `$HOME/.ssh/authorised_keys`.

There are multiple ways to do so.

???- question "Can I use `ssh-copy`?"

    No.

    You can not use `ssh-copy`.

One way is to, on your local computer, view the content of the file:

```bash
cat $HOME/.ssh/id_ed25519_uppmax_login.pub
```

Then copy that line to your clipboard.

???- question "How does that look like?"

    ```bash
    $ cat $HOME/.ssh/id_ed25519_uppmax_login.pub
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFGXV8fRK+cazt8qHX+fGS+w6WPOuE82Q19A12345678 Sven's key to UPPMAX
    ```

On Bianca, to edit the authorised keys file, do:

```bash
nano $HOME/.ssh/authorised_keys
```

In `nano`, paste the line in your clipboard.
Save the file and close `nano`.

!!! warning "The public key must be one line"

    The public key you've just copy-pasted must be one line.
    It must not be wrapped/split over multiple lines.

???- question "How can I check?"

    On Bianca, do:

    ```bash
    cat .ssh/authorised_keys
    ```

    You should find your public key there. It looks similar to this:

    ```bash
    [sven@sens2017625-bianca ~]$ cat .ssh/authorised_keys
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFGXV8fRK+cazt8qHX+fGS+w6WPOuE82Q19A12345678 Sven's key to UPPMAX
    ```

### 3. Set the right permissions

On Bianca, do:

```bash
chmod 700 .ssh/authorised_keys
chmod 700 .ssh
chmod 700 ~
```

???- question "How can I check?"

    You can check by doing the following and observing similar output:

    ```bash
    ls -ld .ssh
    ```

    Output should be:

    ```text
    drwx--S--- 2 sven sven 4096 Jan  8 10:26 .ssh
    ```


    Second checkL

    ```bash
    [richel@sens2017625-bianca ~]$ ls -ld .ssh/authorised_keys
    ```

    Output should be similar to:

    ```text
    -rwx------ 1 sven sven 104 Jan  8 10:26 .ssh/authorised_keys
    ```

    Third check:

    ```bash
    ls -l .ssh
    ```

    Output should be similar to:

    ```text
    total 1
    -rw-r----- 1 user user 743 May  7  2019 authorised_keys
    ```

    or

    ```text
    total 1
    -rwx------ 1 sven sven 104 Jan  8 10:26 authorised_keys
    ```

### 4. [Log in to Bianca via the console using an SSH key](../getting_started/login_bianca_console_ssh_key.md)

[Log in to Bianca via the console using an SSH key](../getting_started/login_bianca_console_ssh_key.md),
using `ssh -A`:

```bash
ssh -A [username]@bianca.uppmax.uu.se
```

For example:

```bash
ssh -A sven@bianca.uppmax.uu.se
```

You will still get a login, asking for (1) your UPPMAX password,
(2) your UPPMAX 2FA, and (3) your UPPMAX project.

If all worked, there will be no need anymore to again type the UPPMAX
password.

## Troubleshooting

To debug, run SSH commands with the `-vv` flag.

???- question "How does that look like?"

    ```console
    ...
    debug1: Requesting authentication agent forwarding.
    debug2: channel 1: request auth-agent-req@openssh.com confirm 0
    ...

    debug1: client_input_channel_open: ctype auth-agent@openssh.com rchan 2 win 65536 max 16384
    debug1: client_request_agent: bound agent to hostkey
    debug2: fd 8 setting O_NONBLOCK
    debug1: channel 2: new [authentication agent connection]
    debug1: confirm auth-agent@openssh.com
    Last login: Tue Jul 11 18:44:21 2023 from 172.18.144.254
     _   _ ____  ____  __  __    _    __  __
    | | | |  _ \|  _ \|  \/  |  / \   \ \/ /   | System:    sens2017625-bianca
    | | | | |_) | |_) | |\/| | / _ \   \  /    | User:      user
    | |_| |  __/|  __/| |  | |/ ___ \  /  \    |
     \___/|_|   |_|   |_|  |_/_/   \_\/_/\_\   |

      ###############################################################################
    ```

### On Linux, it still asks for a password

From [this post](https://unix.stackexchange.com/questions/26371/ssh-prompts-for-password-despite-ssh-authorised-keys)
and [its answer](https://unix.stackexchange.com/a/664213):

On Bianca, do:

```bash
chmod 700 .ssh/authorised_keys
chmod 700 .ssh
chmod 700 ~
```

On your local computer, do:

```bash
chmod 700 .ssh/authorised_keys
chmod 700 .ssh
chmod 700 ~
```

## Links

- [Notes from Pavlin Mitev](https://hackmd.io/@pmitev/SSH_tips)

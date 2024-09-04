---
tags:
  - ssh
  - SSH
---

# ssh

From [Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell):

> The Secure Shell Protocol (SSH) is a cryptographic network protocol
> for operating network services securely over an unsecured network.

At UPPMAX we allow users to login via SSH, using the program `ssh`.

- to use graphical applications, use [SSH X forwarding](ssh_x_forwarding.md),
  i.e. `ssh -X` when logging in
- to login via SSH, see [how to create and use an SSH key](ssh_key_use.md) for the different HPC clusters

## SSH key management

For WSL2 under Windows10 or Windows11,
here as a neat way to get persistent key-manager in WSL2 (credits: [original source](https://esc.sh/blog/ssh-agent-windows10-wsl2/)).

```bash
sudo apt-get install keychain
```

Replace `XXXX` with the output of `hostname` command on the command line.

```bash
/usr/bin/keychain -q --nogui $HOME/.ssh/id_ed25519_key
source $HOME/.keychain/XXXX-sh
```

Remove `-q` to get some information if you want

```bash
* keychain 2.8.5 ~ http://www.funtoo.org
* Found existing ssh-agent: 4487
* Known ssh key: /home/user/.ssh/id_ed25519_key
```

First time you login, you will be asked for the password and the key will be handled by the key-manager. Check with

```bash
ssh-add -l
256 SHA256:wLJvQOM....   ....cTTtiU MyNewKey (ED25519)
```

## MobaXterm

In MobaXterm you can use the internal `MobAgent` or/and the `Peagent`
from the `PuTTy` tools.

![MobaXterm](./img/mobaxterm_use_internal_ssh_agend_mobagent.png)

## OPTIONAL: SSH config

Example `$HOME/.ssh/config` file to make your work easier.

```bash
Host rackham
User username
HostName rackham.uppmax.uu.se
ServerAliveInterval 240
ServerAliveCountMax 2

# Default settings
#=======================================
Host *
ForwardAgent no
ForwardX11 yes
ForwardX11Trusted yes
ServerAliveInterval 120
#=======================================
```

Now

```bash
# without config
ssh -X username@rackham.uppmax.uu.se
# with config
ssh rackham

# without config
scp local_file username@rackham.uppmax.uu.se:remote_folder/
# with config
scp local_file rackham:remote_folder/

rsync ...
sftp ...
```

## Links

- [SSH Tips by Pavlin Mitev](https://hackmd.io/@pmitev/SSH_tips)

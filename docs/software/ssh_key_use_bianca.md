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
- You use Ubuntu 24.04 Noble, as demonstrated by [this video](https://youtu.be/j6F8sJu2NFs),
  where a password is still requested after doing this procedure
  on Rackham

Here is the procedure:

- Add the content of your public key `id_ed25519_key.pub` to
  `$HOME/.ssh/authorized_keys`.
  **You can not** use the same command ssh-copy as in the case for Rackham,
  i.e. you have to manually bring the key on Bianca.
  If you paste it, **make sure it is in one line**,
  not wrapped/split over multiple lines.
- **Make sure the permissions look something like this:**

```bash
ls -ld .ssh
drwx--S--- 2 user user 4096 May  7  2019 .ssh

ls -l .ssh
total 1
-rw-r----- 1 user user 743 May  7  2019 authorized_keys
```

Then [log in to Bianca via the console using an SSH key](../getting_started/login_bianca_console_ssh_key.md):

```bash
ssh -A user-sensXXXXX@bianca.uppmax.uu.se
```

- To debug, run with `-vv`

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

---
tags:
  - create
  - ssh
  - SSH
  - key
  - ssh key
  - SSH key
  - ssh key pair
  - SSH key pair
  - Pelle
---

# Create an SSH key pair for Pelle

This page describes [how to create and use an SSH key](ssh_key_use.md)
so that you can
[login to the Pelle console environment with an SSH key](../getting_started/login_pelle_console_ssh_key.md)

## Procedure

???- question "Prefer a video?"

    Watch the YouTube video
    [Create an SSH key pair for Pelle](https://youtu.be/U2LxIpx7SD8)

This figure shows the procedure:

```mermaid
flowchart TD
  subgraph ip_inside_sunet[IP inside SUNET]
    create[1.Create an SSH key pair]
    add[2.Add your keys to an SSH agent]
    copy[3.Copy the public key to Pelle]
  end
  create --> add
  add --> copy
```

This procedure fails if:

- You use Ubuntu 24.04 Noble, even when
  [inside the university networks](../getting_started/get_inside_sunet.md).
  as demonstrated in the end of the YouTube video
  [Create an SSH key pair for Pelle](https://youtu.be/U2LxIpx7SD8)

### 1. Create an SSH key pair

On your local computer, in a terminal,
create an SSH key pair with the following command:

```bash
ssh-keygen -a 100 -t ed25519 -f ~/.ssh/id_ed25519_uppmax_login -C "My comment"
```

- `-a 100`:  100 rounds of key derivations,
  making your key's password harder to brute-force,
  as is recommended by
  [this StackExchange post](https://security.stackexchange.com/a/144044)
- `-t ed25519`: type of encryption scheme
- `-f ~/.ssh/id_ed25519_uppmax_login`: specify filename,
  following the naming scheme as suggested
  [in this Superuser post](https://superuser.com/a/1261644)
- `-C "My comment"`: a comment that will be stored in the key, so you can find out what it was for

### 2. Add your keys to an SSH agent

On your local computer, in a terminal,
add your newly generated `ed25519` key to an SSH agent:

```bash
ssh-add ~/.ssh/id_ed25519_uppmax_login
```

### 3. Copy the public key to Pelle

On your local computer, in a terminal,
copy the public key to Pelle:

```bash
ssh-copy-id -i .ssh/id_ed25519_uppmax_login.pub [username]@pelle.uppmax.uu.se
```

- `-i .ssh/id_ed25519_uppmax_login.pub`: the identity file, the public key's filename
- `[username]@pelle.uppmax.uu.se`: your UPPMAX username, for example `sven@pelle.uppmax.uu.se`

After this, you can login to Pelle without specifying a password.

## Troubleshooting

### On Linux, it still asks for a password

This may be for multiple reasons.

Possible reason 1 is that the SSH key needs to be specified explicitly, e.g.

```bash
ssh -i [path_to_SSH_key] [UPPMAX_username]@pelle.uppmax.uu.se
```

For example:

```bash
ssh -i ~/.ssh/id_ed25519_uppmax_login sven@pelle.uppmax.uu.se
```

Possible reason 2 is that the folders used by SSH do not have proper rights (from [this post](https://unix.stackexchange.com/questions/26371/ssh-prompts-for-password-despite-ssh-authorized-keys) and [its answer](https://unix.stackexchange.com/a/664213):

To give the folders needed by SSH the proper rights, on Pelle, do:

```bash
chmod 700 .ssh/authorized_keys
chmod 700 .ssh
chmod 700 ~
```

On your local computer, do:

```bash
chmod 700 .ssh/authorized_keys
chmod 700 .ssh
chmod 700 ~
```

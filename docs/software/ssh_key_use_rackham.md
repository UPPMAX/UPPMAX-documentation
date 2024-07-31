# Create and use an SSH key pair for Rackham

This page describes [how to create and use an SSH key](ssh_key_use.md)
for the [Rackham](../cluster_guides/rackham.md) cluster.

Create an SSH key pair with the following command:

<!-- ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_key -C "MyNewKey" -->
<!-- ssh-keygen --rounds 100 -t ed25519 --filename ~/.ssh/id_ed25519_key --comment "Sven's key to UPPMAX" -->
<!-- ssh-keygen -t ed25519 --filename ~/.ssh/id_ed25519_uppmax_login --comment "Sven's key to UPPMAX" -->

```bash
ssh-keygen -a 100 -t ed25519 -f ~/.ssh/id_ed25519_uppmax_login -C "Sven's key to UPPMAX"
```

 * `-a 100`:  100 rounds of key derivations, making your key's password harder to brute-force, as is recommended [here](https://security.stackexchange.com/a/144044)
 * `-t ed25519`: type of encryption scheme
 * `-f ~/.ssh/id_ed25519_uppmax_login`: specify filename, following the naming scheme as suggested [here](https://superuser.com/a/1261644)
 * `-C "Sven's key to UPPMAX"`: a comment that will be stored in the key, so you can find out what it was for

Add your newly generated `ed25519` key to an **SSH agent**:

<!-- ssh-add ~/.ssh/id_ed25519_key -->

```bash
ssh-add ~/.ssh/id_ed25519_uppmax_login
```

Copy the public key to Rackham or other server.

<!-- ssh-copy-id -i .ssh/id_ed25519_key.pub username@rackham.uppmax.uu.se -->
<!-- ssh-copy-id --identity_file .ssh/id_ed25519_key.pub [username]@rackham.uppmax.uu.se -->



```bash
ssh-copy-id -i .ssh/id_ed25519_uppmax_login.pub [username]@rackham.uppmax.uu.se
```

 * `-i .ssh/id_ed25519_uppmax_login.pub`: the identity file, the public key's filename
 * `[username]@rackham.uppmax.uu.se`: your UPPMAX username, for example `sven@rackham.uppmax.uu.se`

After this, you can login to Rackham without specifying a password.

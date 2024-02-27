# Create and use an SSH key pair for Rackham

This page describes [how to create and use an SSH key](ssh_key_use.md)
for the [Rackham](rackham.md) cluster.

Create an SSH key pair with the following command:

```
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_key -C "MyNewKey"
```

Add your newly generated `ed25519` key to an **SSH agent**:

```
ssh-add ~/.ssh/id_ed25519_key
```

Copy the public key to Rackham or other server.

```
ssh-copy-id -i .ssh/id_ed25519_key.pub rackham.uppmax.uu.se
```

Connect

```
ssh username@rackham.uppmax.uu.se
```

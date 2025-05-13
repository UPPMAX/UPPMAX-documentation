---
tags:
  - login
  - log in
  - Pelle
---

# Log in to Pelle

There are multiple UPPMAX clusters one can [log in to](../getting_started/login.md).
Here we describe how to log in to [Pelle](../cluster_guides/pelle.md).

!!! warning "Pelle is not ready yet"

    Pelle is not completely ready yet,
    hence the content of this page will change.
    Also, the content will be shorter and sloppier, until procedures
    solidify.

## Log in to Pelle via SSH

Currently, this is the only way to log in to Pelle:
one cannot access Pelle yet via a website, nor
via a local ThinLinc client.

### 1. Use `ssh` to log in to Rackham5

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [username]@rackham5.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh sven@rackham5.uppmax.uu.se
```

???- question "Want to use graphical programs?"

    If you want to use graphical programs,
    you need to use [SSH X forwarding](../software/ssh_x_forwarding).

    In short: add the `-X` flag when running `ssh`, e.g.:

    ```bash
    ssh -X sven@rackham5.uppmax.uu.se
    ```

    For more details, see
    [the SSH X forwarding page](../software/ssh_x_forwarding.md).

### 2. Use `ssh` to log in to Pelle1

From the [terminal](../software/terminal.md) at Rackham5,
use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -X [username]@pelle1.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh -X sven@pelle1.uppmax.uu.se
```

### 3. You are in

You are in :-)

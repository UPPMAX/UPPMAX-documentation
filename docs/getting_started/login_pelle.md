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

    - Pelle is not completely ready yet,
    hence the content of this page will change.
    - Also, the content will be shorter and sloppier, until procedures
    solidify.
    - The instructions below will not work as of today.

!!! info "Test users are testing the Pelle environment"

    - We have pilot test users testing Pelle right now.
    - Soon all Rackham users will be let in.
    - In addition to SSH also ThinLinc will be available

## Log in to Pelle via SSH

### 1. Use `ssh` to log in to Pelle

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [username]@pelle.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh sven@pelle.uppmax.uu.se
```

???- question "Want to use graphical programs?"

    If you want to use graphical programs,
    you need to use [SSH X forwarding](../software/ssh_x_forwarding.md).

    In short: add the `-X` flag when running `ssh`, e.g.:

    ```bash
    ssh -X sven@pelle.uppmax.uu.se
    ```

    For more details, see
    [the SSH X forwarding page](../software/ssh_x_forwarding.md).


### 2. You are in

You are in :-)

## Log in via ThinLinc

Follow the [instructions for Rackham](./login_rackham_remote_desktop_local_thinlinc_client.md),
but use the address:

```bash
pelle-gui.uppmax.uu.se
```

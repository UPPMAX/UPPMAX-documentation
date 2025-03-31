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

    Pelle is not ready yet, hence the content of this page will change.
    Also, the content will be shorter and sloppier, until procedures
    solidify.

## Log in to Pelle via SSH


### 1. Use `ssh` to log in to Rackham5

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -X [username]@rackham5.uppmax.uu.se
```

`[username]` is your UPPMAX username, for example, `sven`,
resulting in:

```bash
ssh -X sven@rackham5.uppmax.uu.se
```

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

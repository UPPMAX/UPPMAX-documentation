---
tags:
  - login
  - log in
  - Bianca
  - console
  - terminal
  - password
  - out
  - outside
  - SUNET
  - university networks
---

# Login to the Bianca console environment with a password from outside of the Swedish university networks

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a [terminal](../software/terminal.md) and a password
from outside of the Swedish university networks.

!!! danger

    - Do not log in to Rackham and from there log in to Bianca.
    - This will let all sensitive data land on Rackham uncypted as a an intermediate step.
    - Rackham is not a secure system and can be spied on.

## Procedure with using Rackham as a "jump host"

- Log in to Bianca via Rackham in one line

```console
ssh bjornc@bianca.uppmax.uu.se -J bjornc@rackham.uppmax.uu.se
bjornc@rackham.uppmax.uu.se's password:

Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

(bjornc@bianca.uppmax.uu.se) Password:
(bjornc@bianca.uppmax.uu.se) Second factor (TOTP UPPMAX):
```

- You are now inside the Bianca session and sensitive data is not seen by Rackham at all.

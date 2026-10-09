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
search:
  boost: 1
---

# Login to the Bianca console environment with a password from outside of SUNET

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a [terminal](../software/terminal.md) and a password
from outside of the Swedish university networks.

!!! danger

    - Do not log in to a SUNET server like Pelle or Rackham or Arrhenius and from there log in to Bianca.
    - This will let all sensitive data land on that server uncrypted as an intermediate step.
    - Other clusters in SUNET are not secure systems and could be spied on.

## Procedure with using Rackham as a "jump host"

- Log in to Bianca via Rackham in one line

```console
ssh sven@bianca.uppmax.uu.se -J sven@rackham.uppmax.uu.se
sven@rackham.uppmax.uu.se's password:
sven@rackham.uppmax.uu.se) Second factor (TOTP UPPMAX):

Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

(sven@bianca.uppmax.uu.se) Password:
(sven@bianca.uppmax.uu.se) Second factor (TOTP UPPMAX):
```

- You are now inside the Bianca session and sensitive data is not seen by Rackham at all.

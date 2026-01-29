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

# Login to the Bianca console environment with a password from outside of the Swedish university networks

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a [terminal](../software/terminal.md) and a password
from outside of the Swedish university networks.

!!! danger

    - Do not log in to Rackham/Pelle and from there log in to Bianca.
    - This will let all sensitive data land on Rackham/Pelle uncrypted as a an intermediate step.
    - Rackham/Pelle is not a secure system and could be spied on.

## Procedure with using Pelle as a "jump host"

- Log in to Bianca via Pelle in one line

```console
ssh bjornc@bianca.uppmax.uu.se -J sven@pelle.uppmax.uu.se
sven@pelle.uppmax.uu.se's password:
sven@pelle.uppmax.uu.se) Second factor (TOTP UPPMAX):

Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

(bjornc@bianca.uppmax.uu.se) Password:
(bjornc@bianca.uppmax.uu.se) Second factor (TOTP UPPMAX):
```

- You are now inside the Bianca session and sensitive data is not seen by Pelle at all.

## Procedure with using any server within SUNET as a "jump host"

We give here an example of using Tetralith cluster at NSC. Replace "Tetralith" with the cluster or server (in SUNET) you have account on.

- Log in to Bianca via Tetralith in one line:

```console
ssh bjornc@bianca.uppmax.uu.se -J sm_bcarl@tetralith.nsc.liu.se
(sm_bcarl@tetralith.nsc.liu.se) Password:
(sm_bcarl@tetralith.nsc.liu.se) Verification code:

Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

(bjornc@bianca.uppmax.uu.se) Password:
(bjornc@bianca.uppmax.uu.se) Second factor (TOTP UPPMAX):
```

- You are now inside the Bianca session and sensitive data is not seen by Tetralith (or the server you use) at all.

---
tags:
  - login
  - log in
  - Bianca
  - remote desktop
  - website
  - URL
  - out
  - outside
  - SUNET
  - university networks
---

# Log in to the Bianca remote desktop environment website from outside of the Swedish university networks

If you cannot use VPN this may be the solution for you.

!!! danger

    - Do not log in "normally" with ThinLinc (web or client) to Rackham and from there log in to Bianca.
    - This will let all sensitive data land on Rackham uncrypted as a an intermediate step.
    - Rackham is not a secure system and could be spied on.

## Procedure

From the terminal, connect to Pelle with ``ssh`` and forward local connection from you computer to Bianca web interface.

```bash
ssh -L 8443:bianca:443 sven@pelle.uppmax.uu.se
```


In your browser, enter the following web address [https://bianca-localhost.uppmax.uu.se](https://bianca-localhost.uppmax.uu.se)
Do not forget ``https://``

![Bianca with local port forward](./img/thinlinc_jump_bianca.png)

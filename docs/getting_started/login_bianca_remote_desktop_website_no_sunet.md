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
search:
  boost: 1
---

# Log in to the Bianca remote desktop environment website from outside of the Swedish university networks

If you cannot use VPN this may be the solution for you.

!!! danger

    - Do not log in "normally" with ThinLinc (web or client) to Rackham and from there log in to Bianca.
    - This will let all sensitive data land on Rackham uncrypted as a an intermediate step.
    - Rackham is not a secure system and could be spied on.

## Procedure

From the terminal, connect to Pelle or other SUNET server with ``ssh`` and forward local connection from your computer to Bianca web interface.

Example Pelle:

```bash
ssh -L 8443:bianca:443 sven@pelle.uppmax.uu.se
```

Example Tetralith:

```bash
ssh -L 8443:bianca:443 sven@tetralith.liu.uu.se
```

- In your browser, enter the following web address [https://bianca-localhost.uppmax.uu.se](https://bianca-localhost.uppmax.uu.se)
    - Do not forget ``https://``
- You may need to add ``:8443`` so: [https://bianca-localhost.uppmax.uu.se:8443](https://bianca-localhost.uppmax.uu.se:8443)

![Bianca with local port forward](./img/thinlinc_jump_bianca.png)

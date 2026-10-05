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

# Log in to the Bianca remote desktop environment website from outside of the Swedish university networks

There are multiple ways to [log in to Bianca](login_bianca.md).
If you need Graphics  and cannot use VPN follow this procedure.
This page describes how to log in to Bianca Remote desktop using a Rackham4 to get into SUNET
from outside of the Swedish university networks.

!!! danger

    - Do not log in to a SUNET server like Pelle and from there log in to Bianca.
    - This will let all sensitive data land on that server uncrypted as an intermediate step.
    - Other clusters in SUNET are not secure systems and could be spied on.

Regarding Users outside SUNET, like "Karolinska Institutet" users without VPN and working abroad, for instance.

## Procedure with using rackham4 as a "SOCKS proxy"

??? question "What is SOCKS proxy?"

    First, let's explain what SSH tunneling means (``-L``).
    ``ssh -L`` opens a local port. Everything that you send to that port is put through the ssh connection and leaves through the server.
    If you do, e.g., ``ssh -L 4444:google.com:80``, if you open ``http://localhost:4444`` on your browser, you'll actually see google's page.

    ``ssh -D`` opens a local port, but it doesn't have a specific endpoint like with -L. Instead, it pretends to be a SOCKS proxy.
    If you open, e.g., ``ssh -D 7777``, when you tell your browser to use ``localhost:7777`` as your SOCKS proxy,
    everything your browser requests goes through the ssh tunnel. 
    To the public internet, it's as if you were browsing from your ssh server instead of from your computer.

### Get inside SUNET

In a terminal:

```console
ssh -D 10443 <username>@rackham4.uppmax.uu.se
```

Give the credentials
You are on the rackham4 cluster
but leave it open and instead...

### Connect via web browser

=== "Windows"

    Go to the Firefox browser (must be if you are using windows) and go for settings.
    Search for "socks"
    Then type ``https://content.uppmax.uu.se/bianca.pac`` and click check boxes according to the attached image.

    start a new page and go to ``bianca.uppmax.uu.se``

=== "Mac/Linux"

    Go to a browser
    start a new page and go to bianca.uppmax.uu.se

Things should look like it is [presented here](login_bianca_remote_desktop_website.md).

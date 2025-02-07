---
tags:
  - setup
  - set up
  - VPN
  - Linux
  - UU
  - Uppsala
---

# Setup a VPN from Uppsala University for Linux

How to [set up a VPN](setup_vpn.md) differs between universities
and differs between operating systems.
This page describes how to set up a VPN from Uppsala University for Linux.

## Procedure

### 1. Install the needed packages

In a terminal, do:

```bash
sudo apt-get install openconnect network-manager-openconnect network-manager-openconnect-gnome
```

## 2. Follow the images from UIT

Here is the procedure, as suggested by UIT:

![Setup a VPN from Uppsala University for Linux 1](./img/setup_vpn_uu_linux_1.png)

![Setup a VPN from Uppsala University for Linux 2](./img/setup_vpn_uu_linux_2.png)

![Setup a VPN from Uppsala University for Linux 3](./img/setup_vpn_uu_linux_3.png)

The 2FA should be called `[akka_id]`, e.g. `svesv314`
(and not `sven.svensson@icm.uu.se`).

???- question "Forgot how to set up 2FA for your UU user account?"

    UU describes how to setup 2FA for your user
    account [here](https://www.uu.se/en/staff/service-and-tools/tools-and-guides/log-in-securely).

    Pick the options for 'user account' (i.e. not for SharePoint).

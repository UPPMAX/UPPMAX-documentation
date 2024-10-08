---
tags:
  - SUNET
  - University network
  - University networks
  - Get inside
  - edoroam
---

# Get inside the university networks

One cannot connect to all UPPMAX clusters everywhere around the world.
Instead, one needs to get inside the university networks first.
This page described how to get inside the university networks,
or, to use more precise language, to obtain a [SUNET](https://www.sunet.se/) Internet Protocol ('IP') address.

???- question "How do I know if I am inside the university networks?"

    Go to <https://bianca.uppmax.uu.se/>.

    - If nothing happens, you are outside of the university networks

    ![A user that is outside of the university network sees nothing](./img/login_uppmax_bianca_website_outside_sunet_browser_short.png)

    > A user that is outside of the university network sees nothing.

    - If you so a login screen, you are inside of the university networks

    ![A user that is outside of the university network sees a login screen](./img/bianca_gui_login_1st.png)

    > A user that is outside of the university network sees a login screen.

There are these ways to do this:

- Physically move inside SUNET
- Use a VPN (a 'virtual private network')
- Use an HPC cluster within SUNET

Each of these three ways are described below.

```mermaid
flowchart TD

    subgraph sub_outside[IP outside SUNET]
      outside(Physically outside SUNET)
    end

    subgraph sub_inside[IP inside SUNET]
      physically_inside(Physically inside SUNET)
      inside_using_vpn(Inside SUNET using VPN)
      inside_using_rackham(Inside SUNET using Rackham)
    end

    %% Outside SUNET
    outside-->|Move physically|physically_inside
    outside-->|Use a VPN|inside_using_vpn
    outside-->|Login to Rackham|inside_using_rackham

    %% Inside SUNET
    physically_inside-.->inside_using_rackham
    physically_inside-.->inside_using_vpn
```

## Physically move inside SUNET

To connect to all UPPMAX clusters, one must be inside SUNET.

All Swedish university buildings are within SUNET.
Hence, working from a University building
is a non-technical solution to get direct access to Bianca.

## Use a virtual private network

???- question "Want a video to see how to install the UU VPN?"

    - [Install VPN client for Ubuntu and Uppsala university](https://youtu.be/AIJKbJeu0MI?si=9ES3ZECykwc8tT28)

To connect to all UPPMAX clusters, one must be inside SUNET.

A virtual private network (VPN) allows one to access all UPPMAX clusters indirectly:
your computer connects to the VPN within SUNET, where that VPN accesses
your favorite UPPMAX cluster.

To setup a VPN, see [the UPPMAX documentation on how to setup a VPN](setup_vpn.md).

???- tip "Want a video to see how the UU VPN is used?"

    - [Use the UU VPN with 2FA](https://youtu.be/QEJTKvQoiVI)
    - [Use the UU VPN (yet without 2FA) to access the Bianca remote desktop website](https://youtu.be/Ni9nyCf7me8)

## Use an HPC cluster within SUNET

To connect to all UPPMAX clusters, one must be inside SUNET.

An HPC cluster within SUNET (for example, [Rackham](../cluster_guides/rackham.md))
allows one to access all other clusters:
your computer connects to the HPC cluster within SUNET,
after which one accesses all other clusters.

However, when using this method, one can only use the console
environments (i.e. no remote desktop environment).

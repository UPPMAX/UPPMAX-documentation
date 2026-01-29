---
tags:
  - login
  - log in
  - general
search:
  boost: 3
---

# Log in

!!! warning

    N.B. You are NOT supposed to log in to any webpage with the password
    and username you get via UPPMAX support,
    with the exception of the ThinLinc webinterface.

One needs to log in into an UPPMAX cluster to use it.

There are two environments one can login to:

- a remote desktop environment
    - using a webbrowser
    - using a local ThinLinc client
- a console environment, using an [SSH client](../software/ssh_client.md)

![The Bianca environments](./img/bianca_environments_926_x_261.png)

> The two environments to work on Bianca.
> At the left is a remote desktop environment.
> At the the right is the console environment.

Because logging in differs between clusters, each cluster
has its own login page:

- [Login to Bianca](login_bianca.md)
- [Login to Pelle](login_pelle.md)
- [Login to Rackham](login_rackham.md)
- [Login to Snowy](login_snowy.md)

Go to those pages for more details.

After login, you will be on a [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_session_on_rackham.md).

Other things to log in to, shown for completeness:

- [Login to Dardel](login_dardel.md) (this is not an UPPMAX cluster)
- [Login to Transit](../cluster_guides/login_transit.md) (this is an UPPMAX service, not a cluster)

---
tags:
  - login
  - log in
  - Rackham
---

# Log in to Rackham

Here we describe how to log in to [Rackham](../cluster_guides/rackham.md).

- [Prerequisites](rackham_usage_prerequisites.md) describes what is needed before one can access Rackham
- [Which way to login?](#which-way-to-login)
    - [Website](login_rackham_remote_desktop_website.md)
    - [Terminal](login_rackham_console_password.md)
    - [Local ThinLinc client](login_rackham_remote_desktop_local_thinlinc_client.md)

## Which way to login?

There are multiple ways to log in to [Rackham](../cluster_guides/rackham.md):

Login                |Description                                   |Screenshot
---------------------|----------------------------------------------|---------------------------------
[Website](login_rackham_remote_desktop_website.md)              |Remote desktop, no installation needed, slow  |![The Rackham remote desktop via the website](./img/rackham_remote_desktop_via_website_480_x_270.png)
[Terminal](login_rackham_console_password.md)             |Console environment, recommended              |![The Rackham console environment](./img/login_rackham_via_terminal_terminal_409_x_290.png)
[Local ThinLinc client](login_rackham_remote_desktop_local_thinlinc_client.md)|Remote desktop, recommended, need installation|![The Rackham remote desktop via the a local ThinLinc client](../software/img/thinlinc_local_rackham_zoom.png)

Here is a decision tree, to determine which way to log in:

```mermaid
flowchart TD
  need_gui(Need to run a graphical program?)
  use_terminal[Use a terminal]
  use_website[Use the remote desktop website]
  need_easy_or_speedy(Need easiest or fastest?)
  use_local[Use a local ThinLinc client]

  need_gui --> |no| use_terminal
  need_gui --> |yes| need_easy_or_speedy
  need_easy_or_speedy --> |easiest| use_website
  need_easy_or_speedy --> |fastest| use_local

  how_login(How to log in?)

  use_password[Use password\nStart here]
  use_ssh_keys[Use SSH keys\nNo more password needed]

  use_terminal --> how_login
  how_login --> use_password
  how_login --> use_ssh_keys
```

The procedures can be found at:

- [Login to the Rackham remote desktop environment using the website](login_rackham_remote_desktop_website.md)
- [Login to the Rackham console environment with a password](login_rackham_console_password.md).
  If you want to get rid of using a password every time, see [login to the Rackham console environment with an SSH key](login_rackham_console_ssh_key.md)
- [Login to the Rackham remote desktop environment using a local ThinLinc client](login_rackham_remote_desktop_local_thinlinc_client.md)

After login, you will be on a login node.

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive node](../cluster_guides/start_interactive_node_on_rackham.md).


---
tags:
  - login
  - log in
  - Pelle
  - remote desktop
  - website
  - URL
---

# Log in to Pelle's remote desktop via a webbrowser

There are multiple ways to [log in to Pelle](login_pelle.md).
This page describes how to log in to its remote desktop environment
via a web browser.

## Procedure

???- question "Prefer a video?"

    Watch the YouTube video
    [Log in to Pelle's remote desktop via a webbrowser](https://youtu.be/XjLMA0cAu1o)

This is a procedure with one step.
Most work will be to fulfill all [Pelle usage prerequisites](pelle_usage_prerequisites.md).

## 1. Go to [https://pelle-gui.uppmax.uu.se](https://pelle-gui.uppmax.uu.se)

In a webbrowser, go to [https://pelle-gui.uppmax.uu.se](https://pelle-gui.uppmax.uu.se).

???- question "How does that look like?"

    ![Pelle website login screen](login_pelle_remote_desktop_website_1.png)

## 2. Fill in your name and password

At [https://pelle-gui.uppmax.uu.se](https://pelle-gui.uppmax.uu.se)
fill in your details:

- In the first field, fill in your UPPMAX username, e.g. `sven`
- In the second field, fill in your UPPMAX password
- Press "Log in" button

???- question "How does that look like?"

    ![Pelle website login screen with details](login_pelle_remote_desktop_website_2.png)

## 3. Fill in your time-based one-time password

The next dialog of [https://pelle-gui.uppmax.uu.se](https://pelle-gui.uppmax.uu.se)
asks for a time-based one-time password (TOTP)

- Fill in the TOTP from your [UPPMAX 2FA](../getting_started/get_uppmax_2fa.md),
e.g. `123456`.

???- question "How does that look like?"

    ![Pelle website login screen with details](login_pelle_remote_desktop_website_4.png)

## 4. (sometimes) pick a profile

Sometimes the ThinLinc profile chooser pops up.

At the first dialog, click 'Forward'.

???- question "How does that look like?"

    ![Pelle website login screen with details](login_pelle_remote_desktop_website_5.png)


At the second dialog, pick your favorite desktop environment. Both are
equally fine.

???- question "How does that look like?"

    ![Pelle website login screen with details](login_pelle_remote_desktop_website_6.png)

## 5. Welcome on Pelle's login node

Welcome on a Pelle [login node](../cluster_guides/login_node.md)!

???- question "How does that look like?"

    ![Pelle website login screen with details](login_pelle_remote_desktop_website_7.png)

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_pelle.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_session_on_pelle.md).

For tips on how to work with this environment,
see [the UPPMAX ThinLinc page](../software/thinlinc.md)
(as that software is used to do the heavy lifting for that website).

---
tags:
  - login
  - log in
  - Bianca
  - console
  - terminal
  - SSH
---

# Login to the Bianca console environment using SSH keys

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a [terminal](../software/terminal.md) and an SSH key pair.

## 1. Get inside SUNET

When inside SUNET, one can access a Bianca console environment
using SSH and SSH keys.

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

This is considered a bit harder to setup,
but one only needs to type one password to login to Bianca.
If you don't mind typing your UPPMAX password twice,
an easier setup is [log in to the Bianca console environment with a password](login_bianca_console_password.md).

## 2. Use `ssh` to log in

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -A [user]@bianca.uppmax.uu.se
```

For example:

```bash
ssh -A sven@bianca.uppmax.uu.se
```

???- question "How does it look like when outside of SUNET?"

    [Here](https://youtu.be/W-PMTyNcbYI?si=iYxNToDb-EpTdnAO&t=79) you can
    see how this looks like when outside of SUNET.

    Spoiler: quite dull, as nothing happens until these is a timeout.

???- question "Why no `-X`?"

    On Rackham, one can use `-X`:

    ```bash
    ssh -X username@rackham.uppmax.uu.se
    ```

    However, on Bianca, this so-called
    [X forwarding](../software/ssh_x_forwarding.md) is disabled.
    Hence, we do not teach it :-)

## 3. Type your UPPMAX password

Type your UPPMAX password.

???- question "How does this look like?"

    ```bash
    $ ssh -A sven@bianca.uppmax.uu.se

    Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

    (sven@bianca.uppmax.uu.se) Password: 
    (sven@bianca.uppmax.uu.se) 
    ```

## 4. Type your TOTP

Type your UPPMAX TOTP.

???- question "How does this look like?"

    ```bash
    Second factor (TOTP UPPMAX): 
    ```

## 5. Type your Bianca project's name

Type your Bianca project's name.

???- question "How does this look like?"

    ```bash
    Project name (pick from sens2016001 sens2017625 sens2023598): sens2017625
    ```

## 6. You are in

Enjoy! You are in! To be precise,
you are on a Bianca [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_node_on_rackham.md).

In a Bianca console environment:

- Text display is limited to 50kBit/s.
  This means that if you create a lot of text output,
  you will have to wait some time before you get your prompt back.
- Cut, copy and paste work as usual.
  Be careful to not copy-paste sensitive data!

???- question "Why does one need two passwords?"

    The first password is needed to get into the shared Bianca environment.
    This password contains both an UPPMAX password and an UPPMAX 2FA number.

    The second password is needed to go to the login node
    of a project's virtual cluster.

    ```mermaid
    flowchart TD

        %% Give a white background, instead of a transparent one
        classDef node fill:#fff,color:#000,stroke:#000
        classDef focus_node fill:#fff,color:#000,stroke:#000,stroke-width:4px

        subgraph sub_bianca_shared_env[Bianca shared network]
          bianca_shared_console[Bianca console environment login]
          bianca_shared_remote_desktop[Bianca remote desktop login]
          subgraph sub_bianca_private_env[The project's private virtual project cluster]
            bianca_private_console[Bianca console environment]
            bianca_private_remote_desktop[Bianca remote desktop]
            bianca_private_terminal[Terminal]
          end
        end

        %% Shared subgraph color scheme
        %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
        %% style sub_inside fill:#fcc,color:#000,stroke:#fcc
        style sub_bianca_shared_env fill:#ffc,color:#000,stroke:#ffc
        style sub_bianca_private_env fill:#cfc,color:#000,stroke:#cfc

        %% Shared Bianca
        bianca_shared_console --> |UPPMAX password|bianca_private_console
        bianca_shared_remote_desktop-->|UPPMAX password|bianca_private_remote_desktop

        %% Private Bianca
        bianca_private_console---|is a|bianca_private_terminal
        bianca_private_remote_desktop-->|must also use|bianca_private_terminal
    ```


```
richel@richel-N141CU:~$ ssh -A richel@bianca.uppmax.uu.se

Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

(richel@bianca.uppmax.uu.se) Password: 
(richel@bianca.uppmax.uu.se) 
Second factor (TOTP UPPMAX): 
Project name (pick from sens2016001 sens2017625 sens2023598): sens2017625
****************************************************************************
* Login node up and running. Redirecting now!                              *
****************************************************************************

Last login: Fri Feb  7 13:08:54 2025 from 172.18.144.254
 _   _ ____  ____  __  __    _    __  __
| | | |  _ \|  _ \|  \/  |  / \   \ \/ /   | System:    sens2017625-bianca
| | | | |_) | |_) | |\/| | / _ \   \  /    | User:      richel
| |_| |  __/|  __/| |  | |/ ___ \  /  \    | 
 \___/|_|   |_|   |_|  |_/_/   \_\/_/\_\   | 

###############################################################################

        User Guides: http://www.uppmax.uu.se/support/user-guides
        FAQ: http://www.uppmax.uu.se/support/faq

        Write to support@uppmax.uu.se, if you have questions or comments.


[richel@sens2017625-bianca ~]$ exit
```

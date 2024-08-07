# Login to the Bianca console environment using SSH keys

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a terminal and an SSH key pair.

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

From a terminal, use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -A [user]-[project name]@bianca.uppmax.uu.se
```

For example:

```bash
ssh -A sven-sens2023598@bianca.uppmax.uu.se
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

## 3. Type your UPPMAX password and 2FA

Type your UPPMAX password,
directly followed by the UPPMAX 2-factor authentication number,
for example `verysecret678123`, then press enter.
In this case, the password is `verysecret` and `678123`
is the 2FA number.

## 4. You are in

Enjoy! You are in! To be precise,
you are on a Bianca [login node](../cluster_guides/login_node.md).

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive node](../cluster_guides/start_interactive_node_on_rackham.md).

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

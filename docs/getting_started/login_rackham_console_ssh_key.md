# Login to the Rackham console environment using SSH keys

There are multiple ways to [log in to Rackham](login_rackham.md).

This page describes how to [log in to Rackham](login_rackham.md)
using a terminal and an SSH key pair.

## 1. Get inside SUNET

When inside SUNET, one can access a Rackham console environment
using SSH and SSH keys.

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

This is considered a bit harder to setup,
but one only needs to type one password to login to Rackham.
If you don't mind typing your UPPMAX password twice,
an easier setup is [log in to the Rackham console environment with a password](login_rackham_console_password.md).

## 2. Use `ssh` to log in

From a terminal, use [`ssh`](../software/ssh.md) to log in:

```bash
ssh -A [user]-[project name]@rackham.uppmax.uu.se
```

For example:

```bash
ssh -A sven-sens2023598@rackham.uppmax.uu.se
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

    However, on Rackham, this so-called
    [X forwarding](../software/ssh_x_forwarding.md) is disabled.
    Hence, we do not teach it :-)

## 3. Type your UPPMAX password and 2FA

Type your UPPMAX password,
directly followed by the UPPMAX 2-factor authentication number,
for example `verysecret678123`, then press enter.
In this case, the password is `verysecret` and `678123`
is the 2FA number.

## 4. You are in

Enjoy! You are in! To be precise, you are on a Rackham login node.

In a Rackham console environment:

- Text display is limited to 50kBit/s.
  This means that if you create a lot of text output,
  you will have to wait some time before you get your prompt back.
- Cut, copy and paste work as usual.
  Be careful to not copy-paste sensitive data!

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive node](../cluster_guides/start_interactive_node_on_rackham.md).

???- question "Why does one need two passwords?"

    The first password is needed to get into the shared Rackham environment.
    This password contains both an UPPMAX password and an UPPMAX 2FA number.

    The second password is needed to go to the login node
    of a project's virtual cluster.

    ```mermaid
    flowchart TD

        %% Give a white background, instead of a transparent one
        classDef node fill:#fff,color:#000,stroke:#000
        classDef focus_node fill:#fff,color:#000,stroke:#000,stroke-width:4px

        subgraph sub_rackham_shared_env[Rackham shared network]
          rackham_shared_console[Rackham console environment login]
          rackham_shared_remote_desktop[Rackham remote desktop login]
          subgraph sub_rackham_private_env[The project's private virtual project cluster]
            rackham_private_console[Rackham console environment]
            rackham_private_remote_desktop[Rackham remote desktop]
            rackham_private_terminal[Terminal]
          end
        end

        %% Shared subgraph color scheme
        %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
        %% style sub_inside fill:#fcc,color:#000,stroke:#fcc
        style sub_rackham_shared_env fill:#ffc,color:#000,stroke:#ffc
        style sub_rackham_private_env fill:#cfc,color:#000,stroke:#cfc

        %% Shared Rackham
        rackham_shared_console --> |UPPMAX password|rackham_private_console
        rackham_shared_remote_desktop-->|UPPMAX password|rackham_private_remote_desktop

        %% Private Rackham
        rackham_private_console---|is a|rackham_private_terminal
        rackham_private_remote_desktop-->|must also use|rackham_private_terminal
    ```

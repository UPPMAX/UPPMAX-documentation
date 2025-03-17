---
tags:
  - login
  - log in
  - Bianca
  - console
  - terminal
  - password
---

# Login to the Bianca console environment with a password

There are multiple ways to [log in to Bianca](login_bianca.md).

This page describes how to [log in to Bianca](login_bianca.md)
using a [terminal](../software/terminal.md) and a password:

- [Procedure](#procedure): describes the procedure
- [Troubleshooting](#troubleshooting): describes how to fix errors

## Procedure

???- tip "Video: how to use a terminal and SSH to access the Bianca console environment"

    This video shows how to use a terminal and SSH to access
    the Bianca console environment: [YouTube](https://youtu.be/7mKDxnXqi_M)

### 1. Get inside the university networks

Get inside the university networks.

???- question "Forgot how to get within the university networks?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

### 2. Use `ssh` to log in

From a [terminal](../software/terminal.md), use [`ssh`](../software/ssh.md) to log in:

```bash
ssh [username]@bianca.uppmax.uu.se
```

For example:

```bash
ssh sven@bianca.uppmax.uu.se
```

???- question "How does this look like (when inside of SUNET)?"

    ```bash
    sven@svens_computer:~$ ssh sven@bianca.uppmax.uu.se

    Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

    (sven@bianca.uppmax.uu.se) Password: 
    ```

    After which a password will be asked. Go to the next step.

???- question "How does this look like the first time?"

    ```bash
    sven@svens_computer:~$ ssh sven@bianca.uppmax.uu.se
    The authenticity of host 'bianca.uppmax.uu.se (89.44.250.74)' can't be established.
    ECDSA key fingerprint is SHA256:Z9FeKcfgw9PicHfotfkCVZTzWTY0xPjy0qa9Ap/7Aws.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    - Type `yes`!

    - Other valid fingerprint is: ``SHA256:ZUsJUznqix7DjFbwV90nhfKq5u/x3+GUSX7F6C9s3rA``

    

    

???- question "How does it look like when outside of SUNET?"

    ```bash
    sven@svens_computer:~$ ssh sven@bianca.uppmax.uu.se
    ```

    After which there is only waiting...

???- question "Why no `-A`?"

    On Bianca, one can use `-A`:

    ```bash
    ssh -A [username]@bianca.uppmax.uu.se
    ```

    this option is only useful when you want to
    [log in to Bianca via the console using an SSH key](login_bianca_console_ssh_key.md).
    As we here use passwords (i.e. no SSH keys)
    to access Bianca, `-A` is unused
    and hence we simplify this documentation by omitting it.

???- question "Why no `-X`?"

    On Rackham, one can use `-X`:

    ```bash
    ssh -X [username]@rackham.uppmax.uu.se
    ```

    However, on Bianca, this so-called
    [X forwarding](../software/ssh_x_forwarding.md) is disabled.
    Hence, we do not teach it :-)

### 3. Type your UPPMAX password

Type your UPPMAX password.

???- question "How does this look like?"

    ```bash
    Provide your normal UPPMAX password. You will supply the TOTP code separately, in the next step.

    (sven@bianca.uppmax.uu.se) Password: 
    (sven@bianca.uppmax.uu.se) 
    ```

   After which you'll asked for your TOTP. Go to the next step.

### 4. Type your TOTP

Type the TOTP from the UPPMAX 2-factor authentication service,
for example `123456`, then press enter.

???- question "How does this look like?"

    ```bash
    Second factor (TOTP UPPMAX): 
    ```

   After which you'll asked for your Bianca project. Go to the next step.

After authenticated using the UPPMAX password and UPPMAX TOTP,
you are now asked to pick a Bianca project.

### 5. Type your Bianca project

You will be asked for your UPPMAX project's name.
Type it and press enter.

???- question "How does this look like?"

    ```bash
    Project name (pick from sens2016001 sens2017625 sens2023598): sens2017625
    ```

The next step is to login to your own
private virtual project cluster.
As you are already properly authenticated (i.e. using an UPPMAX password
and UPPMAX TOTP), you don't need to use your 2FA anymore.

???- question "What is a virtual project cluster?"

    As Bianca holds sensitive data, by regulations,
    each Bianca project must be isolated from each other
    and are not allowed to, for example, share the same memory.

    One way to achieve this, would be to build one HPC cluster
    per project. While this would guarantee isolated project environments,
    this would be quite impractical.

    Instead, we create isolated project environments by using software,
    that creates so-called virtual clusters, as if they would be
    physical clusters. Like physical clusters, a virtual cluster
    has a guaranteed isolated project environment.

When you login to Bianca's shared network,
you will get a message of your project's login node status.
It can be `up and running` or `down`.
If it is `down`, the virtual cluster is started,
which may take some minutes.

???- question "How does this look like?"

    Here is how it looks like when the node is already running:

    ```text
    ****************************************************************************
    * Login node up and running. Redirecting now!                              *
    ****************************************************************************
    ```

### 6. Type your UPPMAX password

Type your UPPMAX password,
for example `verysecret`

???- question "How does this look like?"

    ```bash
    sven@sens2017625-bianca.uppmax.uu.se's password: 
    ```

### 7. You are in

Enjoy! You are in! Or, to be precise,
you are on the [login node](../cluster_guides/login_node.md) of your own virtual project cluster.

???- question "How does this look like?"

    ```bash
    Last login: Fri Feb  7 12:09:32 2025 from 172.18.144.254
     _   _ ____  ____  __  __    _    __  __
    | | | |  _ \|  _ \|  \/  |  / \   \ \/ /   | System:    sens2017625-bianca
    | | | | |_) | |_) | |\/| | / _ \   \  /    | User:      sven
    | |_| |  __/|  __/| |  | |/ ___ \  /  \    | 
     \___/|_|   |_|   |_|  |_/_/   \_\/_/\_\   | 

    ###############################################################################

            User Guides: http://www.uppmax.uu.se/support/user-guides
            FAQ: http://www.uppmax.uu.se/support/faq

            Write to support@uppmax.uu.se, if you have questions or comments.


    [sven@sens2017625-bianca ~]$ 
    ````

!!! note "How to behave on a login node"

    On a login node, one can and should do simple things only:
    it is a resource shared with all other users on that node.

    If you need to do more intense calculations,
    [use the Slurm job scheduler](../cluster_guides/slurm_on_rackham.md).

    If you need to do more intense calculations interactively,
    [use an interactive session](../cluster_guides/start_interactive_node_on_rackham.md).

By default, this node has one core,
hence if you need more memory or more CPU power,
you submit a job (interactive or batch),
and an idle node will be moved into your project cluster.

## Troubleshooting

Here are some common errors and their solutions:

### Permission denied, please try again

```bash
Permission denied, please try again.
```

Here are the questions we will ask to solve your problem:

```mermaid
flowchart TD
    error[Permission denied, please try again.]
    correct_password[Is your password correct?]
    added_2fa[Have you added a 2FA number at the end of your password?]
    added_correct_2fa[Have you added the correct 2FA number at the end of your password?]
    in_sunet[Are you within the university networks?]
    active_bianca_project[Is that Bianca project active?]
    member_of_bianca_project[Are you a member of that Bianca project]
    contact_support[Contact support]

    error --> correct_password
    error --> in_sunet
    
    in_sunet --> |yes| active_bianca_project

    correct_password --> |yes| added_2fa
    added_2fa --> |yes| added_correct_2fa
    active_bianca_project -->  |yes| member_of_bianca_project
    member_of_bianca_project --> |yes| contact_support
    added_correct_2fa --> |yes| contact_support
```

???- question "How do I know my password is correct?"

    You don't.

    It could be a typo: you don't see your password when you type (this is a
    security measure), so a typo is likely to occur. Also check if 'Caps Lock'
    is off.

    It could be that you've forgotten your password. That can happen to all of
    us. You can then reset your password at <https://suprintegration.uppmax.uu.se/getpasswd>

???- question "What is the correct 2FA service?"

    The UPPMAX one, titled `[username]@UPPMAX`, for example `sven@UPPMAX`.

    When using UPPMAX, one needs to create other 2FAs too, such as for SUPR
    or the Uppsala VPN. Don't use those numbers to login to Bianca.

???- question "How do I know if I am within the university networks?"

    If you login via `eduroam` you are within the university networks.

    When unsure, go to the Bianca remote desktop website at
    [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se):
    if this page does not load, you are outside of the university networks.

    See [How to get inside of the university networks](../getting_started/get_inside_sunet.md)
    if you outside of the university networks.

???- question "How do I know if the Bianca project is active?"

    A quick way to confirm your Bianca project is active:
    go to <https://bianca.uppmax.uu.se>
    and type your username. If the project is displayed, it is active.

    To confirm your project is active or inactive, use the SUPR NAISS website.
    See [the UPPMAX documentation on projects](../getting_started/project.md)
    how to see if your project is active?

See [the UPPMAX page on contacting support](../support.md)
on how to contact us.

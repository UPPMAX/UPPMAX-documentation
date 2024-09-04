# Using Visual Studio Code on Rackham

![VSCode from a local computer working on Rackham.](./img/vscode_connected_to_rackham.png)

> VSCode from a local computer working on Rackham.

## Introduction

Visual Studio Code ('VSCode') is an [IDE](../software/ides.md)
that can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

In this session, we show how to use VSCode on Rackham.

## Procedure to start VSCode

!!! warning "This procedure fails!"

    Due to a recent change in VSCode and/or the 'Remote Tunnels'
    plugin, this approach does not work anymore.

    This is reported at [Issue 121](https://github.com/UPPMAX/UPPMAX-documentation/issues/121).

Below is a step-by-step procedure to start RStudio.
This procedure is also demonstrated in [this YouTube video](https://youtu.be/RG2FWA8yoUs).

### 1. Install VSCode on your local computer

### 2. Start VSCode on your local computer

![Start VSCode on your local computer](./img/start_vscode_ubuntu.png)

### 3. In VSCode, install the VSCode 'Remote Tunnels' plugin

![Install the VSCode 'Remote Tunnels' plugin](./img/vscode_remote_tunnels_before_install.png)

![Installed the VSCode 'Remote Tunnels' plugin](./img/vscode_remote_tunnels_after_install.png)

### 4. In VSCode, connect to Rackham

In VSCode, at the 'Remote Explorer' tab, click on '[SSH](../software/ssh.md)',
then on 'New Remote'.

![VSCode: add New Remote](./img/vscode_add_new_remote.png)

Type `ssh [username]@rackham.uppmax.uu.se`
where `[username]` is your UPPMAX username,
for example, `ssh sven@rackham.uppmax.uu.se`.

![VSCode: SSH to Rackham](./img/vscode_ssh_to_rackham.png)

Use the `~/.ssh/config` file:

![VSCode: setup config](./img/vscode_remote_tunnels_use_ssh_config_in_home.png)

Click on 'Connect':

![VSCode: connect](./img/vscode_connect_to_rackham.png)

Now, you can work directly on your Rackham files!

![VSCode connected to Rackham](./img/vscode_connected_to_rackham.png)

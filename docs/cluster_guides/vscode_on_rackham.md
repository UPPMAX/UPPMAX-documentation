# Using Visual Studio Code on Rackham

![](./img/vscode_connected_to_rackham.png)

> VSCode from a local computer working on Rackham.

## Introduction

Visual Studio Code ('VSCode') is an [IDE](../software/ides.md)
that can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

In this session, we show how to use VSCode on Rackham.

## Procedure to start VSCode

### 1. Install VSCode on your local computer

### 2. Start VSCode on your local computer

![](./img/start_vscode_ubuntu.png)

### 3. In VSCode, install the VSCode 'Remote Tunnels' plugin

![](./img/vscode_remote_tunnels_before_install.png)

![](./img/vscode_remote_tunnels_after_install.png)

### 4. In VSCode, connect to Rackham

In VSCode, at the 'Remote Explorer' tab, click on '[SSH](../software/ssh.md)',
then on 'New Remote'.

![](./img/vscode_add_new_remote.png)

Type `ssh [username]@rackham.uppmax.uu.se` 
where `[username]` is your UPPMAX username,
for example, `ssh sven@rackham.uppmax.uu.se`.

![](./img/vscode_ssh_to_rackham.png)

Use the `~/.ssh/config` file:

![](./img/vscode_remote_tunnels_use_ssh_config_in_home.png)

Click on 'Connect':

![](./img/vscode_connect_to_rackham.png)

Now, you can work directly on your Rackham files!

![](./img/vscode_connected_to_rackham.png)

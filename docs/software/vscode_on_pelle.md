---
tags:
  - VSCode
  - Rackham
  - connect
---

# Connecting Visual Studio Code to Pelle

![VSCode from a local computer working on Rackham.](./img/vscode_connected_to_rackham.png)

> VSCode from a local computer working on Rackham.

## Introduction

Visual Studio Code ('VSCode') is an [IDE](../software/ides.md)
that can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

In this session, we show how to connect VSCode on your local computer
to work with your files on Rackham.

## Procedure

Below is a step-by-step procedure to start VSCode.

???- question "Prefer a video?"

    See [this YouTube video](https://youtu.be/MkrKi5oU_po).

    An older version of this procedure, where the 'Remote Tunnel'
    extension is used, can be seen in [this YouTube video](https://youtu.be/RG2FWA8yoUs).

### 1. Install VSCode on your local computer

Install VSCode on your local computer.

### 2. Start VSCode on your local computer

???- question "How does that look like?"

    ![Start VSCode on your local computer](./img/start_vscode_ubuntu.png)

### 3. In VSCode, install the VSCode 'Remote-SSH' plugin

In VSCode, install the VSCode 'Remote-SSH' plugin.

???- question "How does that look like?"

    ![Install the VSCode 'Remote-SSH' plugin](./img/vscode_on_rackham_install_remote_ssh.png)

### 4. Enable TOTP interactivity

Since most clusters now has added the TOTP feature you have to make another setting as well.  

- Go to settings (the lower-left corner wheel):

![VSCode_settings](./img/VSCode_settings.png)

![VSCode_settings](./img/VSCode_ssh_login.png)

Search for the right setting and enable it.

### 5. In the 'Remote Explorer' tab, at SSH, click the plus

In VSCode, go to the 'Remote Explorer' tab.
At the SSH section, click on the '+' (with tooltip 'New remote').

???- question "How does that look like?"

    ![Click on the plus](./img/vscode_on_rackham_add_new_remote.png)

### 6. Give the SSH command to connect to Rackham

In the main edit bar, give the SSH command to connect to Rackham,
e.g. `ssh sven@rackham.uppmax.uu.se`

???- question "How does that look like?"

    ![Type the SSH command](./img/vscode_on_rackham_new_remote_ssh_command.png)

### 7. Pick the a location for the SSH config file

In the dropdown menu, pick the a location for the SSH config file,
e.g. the first, which is similar to `/home/sven/.ssh/config`.

???- question "How does that look like?"

    ![Type a location for an SSH config file](./img/vscode_on_rackham_new_remote_ssh_config.png)

### 8. Click 'Connect'

In the bottom left of VSCode, click on the popup window 'Connect'.

???- question "How does that look like?"

![Click on 'Connect'](./img/vscode_on_rackham_new_remote_click_connect.png)

### 9. Done

You are now connected: there is a new window with VSCode connected to Rackham.

???- question "How does that look like?"

    The window that is connected to a Rackham home folder:

    ![Connected to Rackham in subwindow](./img/vscode_on_rackham_connected.png)

    Going to `/proj/staff`:

    ![Connected to Rackham's project folder](./img/vscode_on_rackham_show_proj_folder.png)

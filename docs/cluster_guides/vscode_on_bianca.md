# Using Visual Studio Code on Bianca

!!! warning "VSCode fails, use VSCodium instead"

    The approach below will fail
    (note that [using VSCode on Rackham](vscode_on_rackham.md) does work).

    Instead, go to the page [Using VSCodium on Bianca](vscodium_on_bianca.md)

## Introduction

Visual Studio Code ('VSCode') is an [IDE](../software/ides.md)
that can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

In this session, we show how to use VSCode on Bianca.

## Procedure to start VSCode

### 1. Install VSCode on your local computer

### 2. Start VSCode on your local computer

![](./img/start_vscode_ubuntu.png)

### 3. In VSCode, install the VSCode 'Remote Tunnels' plugin

![](./img/vscode_remote_tunnels_before_install.png)

![](./img/vscode_remote_tunnels_after_install.png)

### 4. In VSCode, connect to Bianca

In VSCode, at the 'Remote Explorer' tab, click on 'SSH',
then on 'New Remote'.

![](./img/vscode_add_new_remote.png)

!!! warning "This is the step that fails"

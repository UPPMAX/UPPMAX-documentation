---
tags:
  - VSCodium
  - Pelle
---

# Using VSCodium on Pelle

!!! warning "Copy"

    This page is just a copy from its Pelle counterpart.

    Its content has not been checked.

![VSCodium on another cluster, as VSCodium on Pelle fails](./img/vscodium_on_bianca_480_x_270.png)

> VSCodium on another cluster, as VSCodium on Pelle fails

!!! warning "VSCodium fails, use VSCode instead"

    The approach below will fail
    (note that [using VSCodium on Bianca](vscodium_on_bianca.md) does work).

    Instead, go to the page [Using VSCode on Pelle](vscode_on_pelle.md)

## Introduction

VSCodium is the community edition of Visual Studio Code
and can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

In this session, we show how to use VSCodium on Pelle,
using Pelle's remote desktop environment.

???- tip "Forgot how to login to a remote desktop environment?"

    See [the 'Logging in to Pelle' page](../getting_started/login_pelle.md).

As VSCodium is a resource-heavy program,
it must be run on an interactive session.

## Procedure to start VSCodium

### 1. Start the Pelle remote desktop environment

???- tip "Forgot how to start Pelle's remote desktop environment?"

    See [the 'Logging in to Pelle' page](../getting_started/login_pelle.md).

### 2. Start an interactive session

Within the Pelle remote desktop environment, start a [terminal](../software/terminal.md).
Within that terminal, start an interactive session with 1 core.

???- tip "Forgot how to start an interactive session?"

    See [the 'Starting an interactive session' page](../cluster_guides/start_interactive_session_on_pelle.md).

    Spoiler: use:

    ```bash
    interactive -A uppmax2023-2-25
    ```

### 3. Load the modules needed

VSCodium needs the `VSCodium/latest` module.

In the terminal of the interactive session, do:

```bash
module load VSCodium/latest
```

### 4. Start VSCodium

With the modules loaded,
in that same terminal,
start VSCodium:

```bash
code
```

VSCodium will give an error?

???- info "How does the VSCodium error look on Pelle?"

    ![VSCodium on Pelle fails](./img/vscodium_on_pelle_error.png)

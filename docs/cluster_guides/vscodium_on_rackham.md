# VSCodium on Rackham

![](./img/vscodium_on_rackham_480_x_270.png)

## Introduction

VSCodium is the community edition of Visual Studio Code
and can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](ides.md).

In this session, we show how to use VSCodium on Rackham,
using Rackham's remote desktop environment.

???- tip "Forgot how to login to a remote desktop environment?"

    See [the 'Logging in to Rackham' page](../getting_started/login_rackham.md).

As VSCodium is a resource-heavy program,
it must be run on an interactive node.

## Procedure to start VSCodium

### 1. Start the Rackham remote desktop environment

???- tip "Forgot how to start Rackham's remote desktop environment?"

    See [the 'Logging in to Rackham' page](../getting_started/login_rackham.md).

### 2. Start an interactive session

Within the Rackham remote desktop environment, start a terminal.
Within that terminal, start an interactive session with 1 core.

???- tip "Forgot how to start an interactive node?"

    See [the 'Starting an interactive node' page](start_interactive_node_on_rackham.md).

    Spoiler: use:

    ```
    interactive -A uppmax2023-2-25
    ```

### 3. Load the modules needed

VSCodium needs the `VSCodium/latest` module.

In the terminal of the interactive session, do:

```
module load VSCodium/latest`
```

### 4. Start VSCodium

With the modules loaded, 
in that same terminal, 
start VSCodium:


```
code
```

VSCodium will give an error?

???- info "How does the VSCodium error look on Rackham?"

    ![](./img/vscodium_on_rackham_error.png)

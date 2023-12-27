# VSCodium

![](./img/vscodium_on_bianca_480_x_270.png)

!!! info "Objectives" 

    - Start VSCodium on Bianca

???- info "Notes for teachers"

    Teaching goals:

    - The learners demonstrate to have started VSCodium on Bianca

    Schedule (45 minutes):

    - 5 mins: Let the learners start an interactive node: this can take dozens of minutes!
    - 5 mins: kill some time
    - 5 mins: discuss this page
    - 15 mins: do the exercises
    - 15 mins: discuss the exercises

## Introduction

VSCodium is the community edition of Visual Studio Code
and can be used for software development in many languages.

???- tip "What is an IDE?"

    See [the page on IDEs](ides.md).

In this session, we show how to use VSCodium on Bianca,
using Bianca's remote desktop environment.

???- tip "Forgot how to login to a remote desktop environment?"

    See [the basic Bianca course page 'Logging in'](../login_bianca.md).

As VSCodium is a resource-heavy program,
it must be run on an interactive node.

## Procedure to start VSCodium


### 1. Get within SUNET

???- tip "Forgot how to get within SUNET?"

    See [the basic Bianca course page 'Login to Bianca'](../login_bianca.md).

### 2. Start the Bianca remote desktop environment

???- tip "Forgot how to start Bianca's remote desktop environment?"

    See [the basic Bianca course page 'Login to Bianca'](../login_bianca.md).

### 3. Start an interactive session

Within the Bianca remote desktop environment, start a terminal.
Within that terminal, start an interactive session with 1 core.

???- tip "Forgot how to start an interactive node?"

    See [the basic Bianca course page 'Starting an interactive node'](../start_interactive_node.md).

    Spoiler: use:

    ```
    interactive -A sens2023598 -n 1 -t 8:00:00
    ```

### 4. Load the modules needed

VSCodium needs the `VSCodium/latest` module.

In the terminal of the interactive session, do:

```
module load VSCodium/latest`
```

### 5. Start VSCodium

With the modules loaded, 
in that same terminal, 
start VSCodium:


```
code
```

VSCodium starts up quickly.

???- info "How does VSCodium look on Bianca?"

    ![](./img/vscodium_on_bianca.png)

## Exercises

???- question "Exercise: Start VSCodium"

    The goal of this exercise is to make sure you can start
    VSCodium.

    How to start VSCodium is in the instructions above
    and in [this YouTube video](https://youtu.be/i7sjHOX4B_M).

???- question "How to find out if you are on a login or interactive node"

    In the terminal, type `hostname`

    - the login node has `[project]-bianca`, where `[project]` is the name of the project, e.g. `sens2023598`
    - the interactive node has `b[number]` in it, where `[number]` is the compute node number



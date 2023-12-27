# RStudio

![](./img/rstudio_in_action_480_x_270.png)

!!! info "Objectives" 

    - Start RStudio on Bianca

???- info "Notes for teachers"

    Teaching goals:

    - The learners demonstrate to have started RStudio on Bianca

    Schedule (45 minutes):

    - 5 mins: Let the learners start an interactive node: this can take dozens of minutes!
    - 5 mins: kill some time
    - 5 mins: discuss this page
    - 15 mins: do the exercises
    - 15 mins: discuss the exercises

## Introduction

RStudio is an IDE specialized for the R programming language.

???- tip "What is an IDE?"

    See [the page on IDEs](ides.md).

In this session, we show how to use RStudio on Bianca,
using Bianca's remote desktop environment.

???- tip "Forgot how to login to a remote desktop environment?"

    See [the basic Bianca course page 'Logging in'](../login_bianca.md).

    Spoiler: go to [https://bianca.uppmax.uu.se/](https://bianca.uppmax.uu.se/)

As RStudio is a resource-heavy program,
it must be run on an interactive node.

???- tip "Forgot how to start an interactive node?"

    See [the basic Bianca course page 'Starting an interactive node'](../start_interactive_node.md).

## Procedure to start RStudio

### 1. Get within SUNET

???- tip "Forgot how to get within SUNET?"

    See [the basic Bianca course page 'Login to Bianca'](../login_bianca.md).

### 2. Start the Bianca remote desktop environment

???- tip "Forgot how to start Bianca's remote desktop environment?"

    See [the basic Bianca course page 'Login to Bianca'](../login_bianca.md).

### 3. Start an interactive session

Within the Bianca remote desktop environment, start a terminal.
Within that terminal, start an interactive session with 2 cores.

!!!- info "Why two cores?"

    RStudio is a resource-heavy program.
    Due to this, we recommend using at least two cores 
    for a more pleasant user experience.

???- tip "Forgot how to start an interactive node?"

    See [the basic Bianca course page 'Starting an interactive node'](../start_interactive_node.md).

    Spoiler: use:

    ```
    interactive -A sens2023598 -n 2 -t 8:00:00
    ```

### 4. Load the modules needed

RStudio needs R and its R packages.
These should be loaded via the module system.

In the terminal of the interactive session, do:

```
module load R_packages/4.3.1 RStudio/2023.06.2-561
```

### 5. Start RStudio

With the modules loaded, start RStudio from the terminal (on the
interactive node):

```
rstudio
```

RStudio can be slow to startup, as R has thousands (!) of packages.
Additionally, at startup and if enabled, your saved RStudio workspace
(with potentially a lot of data!) is read.

???- info "How does RStudio look on Bianca?"

    RStudio when starting up:

    ![](./img/rstudio_starting_up.png)

    RStudio when started up:

    ![](./img/rstudio_started.png)

    RStudio in action:

    ![](./img/rstudio_in_action.png)

    The RStudio debugger, at the error message level:

    ![](./img/rstudio_debugger_at_error_level.png)

    The RStudio debugger, at the function-that-caused-the-error level:

    ![](./img/rstudio_debugger_at_function_level.png)

    The RStudio debugger, at the program level:

    ![](./img/rstudio_debugger_at_program_level.png)

## Exercises

???- question "Exercise: Start RStudio"

    The goal of this exercise is to make sure you can start
    RStudio.

    How to start RStudio is in the instructions above
    and in [this YouTube video](https://youtu.be/rRUb4pqaVak).

???- question "How to find out if you are on a login or interactive node"

    In the terminal, type `hostname`

    - the login node has `[project]-bianca`, where `[project]` is the name of the project, e.g. `sens2023598`
    - the interactive node has `b[number]` in it, where `[number]` is the compute node number


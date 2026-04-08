---
tags:
  - RStudio
  - Pelle
---

# RStudio on Pelle

## Introduction

[RStudio](../software/rstudio.md) is an [IDE](../software/ides.md)
specialised for the [R](../software/r.md) programming language

In this session, we show how to use RStudio on Pelle,
using Pelle's remote desktop environment.

???- tip "Forgot how to login to a remote desktop environment?"

    See [the 'Logging in to Pelle' page](../getting_started/login_pelle.md).

    Spoiler: go to [https://pelle.uppmax.uu.se/](https://pelle.uppmax.uu.se/)

As RStudio is a resource-heavy program,
it must be run on an interactive session.

???- tip "Forgot how to start an interactive session?"

    See [the 'Starting an interactive session' page](../cluster_guides/start_interactive_session_on_pelle.md).

## Procedure to start RStudio

Below is a step-by-step procedure to start RStudio on Pelle.

??? question "Prefer a video?"

    Watch
    [the YouTube Video 'RStudio on Pelle'](https://youtu.be/90sfHzE_k1k)

## 1. Start a Pelle remote desktop environment

This can be either:

- [Login to the Pelle remote desktop environment using the website](../getting_started/login_pelle_remote_desktop_website.md)
- [Login to the Pelle remote desktop environment using a local ThinLinc client](../getting_started/login_pelle_remote_desktop_local_thinlinc_client.md)

## 2. Start an interactive session

Within the Pelle remote desktop environment, start a [terminal](../software/terminal.md).
Within that terminal, [start an interactive session](../cluster_guides/start_interactive_session_on_pelle.md)
with 2 cores:

```bash
interactive -A [naiss_project_id] -n 2 -t [duration]
```

Where:

- `[naiss_project_id]` is an [UPPMAX project code](../getting_started/project.md)
- `[duration]` is the duration of the interactive session

Resulting in, For example:

```bash
interactive -A naiss2024-22-310 -n 2 -t 8:00:00
```

!!!- info "Why two cores?"

    RStudio is a resource-heavy program.
    Due to this, we recommend using at least two cores
    for a more pleasant user experience.

???- tip "What is an interactive session?"

    See [start an interactive session](../cluster_guides/start_interactive_session_on_pelle.md)

!!!- warning "Do not start RStudio from the menus"

    You can start a version of RStudio from the menus.
    However, this will not have access to loaded modules.

    Instead, load RStudio from the module system instead.

## 3. Load the modules needed

In the terminal of the interactive session, do:

```bash
module load R/4.5.1-gfbf-2024a RStudio/2025.09.0-387
```

???- question "What happens if I do not load `R`?"

    Then you will have the sytem-wide R version
    without any packages installed.


## 4. Start RStudio

With the modules loaded, start RStudio from the terminal (on the
interactive session):

```bash
rstudio &
```

RStudio can be slow to startup, if you also load the R-bundles, as thousands (!) of packages need to be registered by RStudio.
Additionally, at startup and if enabled, your saved RStudio workspace
(with potentially a lot of data!) is read.

???- info "How does RStudio look? (Example from Bianca)"

    RStudio when starting up:

    ![RStudio when starting up](./img/rstudio_starting_up.png)

    RStudio when started up:

    ![RStudio when started up](./img/rstudio_started.png)

    RStudio when ready:

    ![RStudio when started up](./img/rstudio_with_r_v4_3_1.png)

    RStudio in action:

    ![RStudio in action](./img/rstudio_in_action.png)

    The RStudio debugger, at the error message level:

    ![The RStudio debugger, at the error message level](./img/rstudio_debugger_at_error_level.png)

    The RStudio debugger, at the function-that-caused-the-error level:

    ![The RStudio debugger, at the function-that-caused-the-error level](./img/rstudio_debugger_at_function_level.png)

    The RStudio debugger, at the program level:

    ![The RStudio debugger, at the program level](./img/rstudio_debugger_at_program_level.png)

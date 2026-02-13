---
tags:
  - RStudio
  - LUMI
---

# RStudio on LUMI

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the CSC documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

## Introduction

[RStudio](../software/rstudio.md) is an [IDE](../software/ides.md)
specialised for the [R](../software/r.md) programming language.

In this session, we show how to use RStudio on LUMI.

As RStudio is a resource-heavy program,
it must be run on an interactive session.

## Procedure to start RStudio

Below is a step-by-step procedure to start RStudio on LUMI.

??? question "Prefer a video?"

    This procedure is also demonstrated in `TODO`.

## 1. Start a LUMI remote desktop environment

...

## 2. Start an interactive session

Within the LUMI remote desktop environment, start a [terminal](../software/terminal.md).
Within that terminal, start an interactive session with 2 cores:

```bash
interactive -A [naiss_project_id] -n 2 -t [duration]
```

Where:

- `[naiss_project_id]` is your [UPPMAX project code](../getting_started/project.md)
- `[duration]` is the duration of the interactive session

Resulting in, For example:

```bash
interactive -A naiss2024-22-310 -n 2 -t 8:00:00
```

!!!- info "Why two cores?"

    RStudio is a resource-heavy program.
    Due to this, we recommend using at least two cores
    for a more pleasant user experience.

## 3. Load the modules needed

In the terminal of the interactive session, do:

```bash
# Something like this
module load R/4.3.1 R_packages/4.3.1 RStudio/2023.12.1-402
```

???- question "How does that look like?"

    Your output will be similar to:

    ```bash
    [sven@r210 sven]$ module load R/4.3.1 R_packages/4.3.1 RStudio/2023.06.2-561
    R/4.3.1: Nearly all CRAN and BioConductor packages are installed and available by loading
    the module R_packages/4.3.1
    R_packages/4.3.1: Note that loading some spatial analysis packages, especially geo-related packages, might
    R_packages/4.3.1: require you to load additional modules prior to use. monocle3 is such a package. See
    R_packages/4.3.1: 'module help R_packages/4.3.1'

    R_packages/4.3.1: The RStudio packages pane is disabled when loading this module, due to RStudio slowdowns
    R_packages/4.3.1: because there are >20000 available packages. *All packages are still available.*  For
    R_packages/4.3.1: more information and instructions to re-enable the packages pane (not recommended) see
    R_packages/4.3.1: 'module help R_packages/4.3.1'

    RStudio/2023.12.1-402: Sandboxing is not enabled for RStudio at UPPMAX. See 'module help RStudio/2023.12.1-402' for more information
    ```

## 4. Start RStudio

With the modules loaded, start RStudio from the terminal (on the
interactive session):

```bash
rstudio
```

RStudio can be slow to startup, as R has thousands (!) of packages.
Additionally, at startup and if enabled, your saved RStudio workspace
(with potentially a lot of data!) is read.

---
tags:
  - course
  - workshop
  - AWK
---

# Awk workshop

AWK is an interpreted programming language designed for text processing and typically used as a data extraction and reporting tool.

This two-days workshop aims to promote and demonstrate the flexibility of the tool, where the overhead of more sophisticated approaches and programming languages is not worth the bother.

## Learn how to

- use Awk as **an advanced** grep command, capable of arithmetic selection rules with control over the content of the matched lines
- perform simple conversions, analysis or filter you data on the fly making it easy to plot or read in your favorite research tool
- handle and take advantage on data split over multiple file data sets.
- use Awk as simple function or data generator
- perform simple sanity checks on your results

## Awk for bioinformaticians

Use what you learn and dive into the basic concepts of bioinformatics with simple exercises on typical scientific problems and tasks.

!!! note "Venue and registration:"

    **Date**: 16 and 17 January, 2025
    **Time**: 9:15 - 12:00 and 13:15 -16:00
    **Location**: Zoom: link will be sent to applicants
    **Application**: [form](https://forms.gle/Hz1mQJSiA6ewfLqz8).


## Schedule

---

### 1-st day 9:15 - 12:00

[Seminar session](https://pmitev.github.io/to-awk-or-not/)

- Examples of typical problems suitable for Awk “treatment”
- Introduction to the basics of Awk scripting language
- Solving interactively simple problems

#### 1-st day lunch break

[Exercises](https://pmitev.github.io/to-awk-or-not/Exercises/Exercises/) 13:15 -16:00

- Solving interactively the exercise problems

### 2-nd day 9:15 - 12:00

- Awk for bioinformaticians - seminar
- Case Study: [Manipulating the output from a genome analysis - vcf and gff](https://pmitev.github.io/to-awk-or-not/Case_studies/manipulating_vcf/)
- Filtering and formatting raw data
- Counting and piling features
- Indexing and hashing to compare variants and annotations

#### 2-nd day lunch break

Walk-through session on various topics:

- Awk parsing “simultaneously” multiple input files
- Multiple input files - second approach scenario will be discussed.
- How to trick awk to accept options on the command line like regular program i.e. `$ script.awk filename parameter1 parameter2` [link](https://pmitev.github.io/to-awk-or-not/More_awk/Command_params/)
- Declaring and calling functions in awk - [link](https://pmitev.github.io/to-awk-or-not/More_awk/User_defined_functions/)
- Input/output to/from an external programs
- Learn how to send input to an external program (might be based on your data) and read the result back - [link](https://pmitev.github.io/to-awk-or-not/More_awk/Input_output/)
- Handy tips: awk oneliners use with Vim, gnuplot…

Also: [Suggest topic](https://forms.gle/usYYkbWaZVkNceSK6) for discussion or see recently [suggested topics](https://docs.google.com/forms/d/1tQYWc504BQ-uYRA7MWgu1pNXM613r4Ua1wP_yBPlNDM/viewanalytics).

## Prerequisites

---

### MacOS

The system provided awk version will work for most of the examples during the workshop with few exceptions, which are noted in the online material.

_Tilda `~` sign on Mac with Swedish keyboard layout - Alt + ^_

### Linux

Several distributions have other awk flavors installed by default. The easiest fix is to install the gnu version gawk i.e. for Ubuntu: `sudo apt install gawk`

### Windows 10/11

- [Ubuntu for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10) - it is better to read from the source, despite it might not be the easiest tutorial. To my experience, this is the best Linux environment without virtualization.
- [MobaXterm](https://mobaxterm.mobatek.net/) use the internal package manager to install gawk. The default is provided by Busybox and is not enough for the purpose of the workshop.

### Linux computer center

- Just login to your account and use the provided awk - any version newer than 4 will work.

```bash
rackham3:[~] awk -V GNU Awk 4.0.2 Copyright (C) 1989, 1991-2012 Free Software Foundation.
```

### Virtual Linux Machine

Just follow some tutorial on how to setup and use the virtual Linux environment.

- [VirtualBox](https://www.virtualbox.org/)
- [Ubuntu on Public Clouds](https://ubuntu.com/public-cloud)
- [GitHub & Binder](https://pmitev.github.io/to-awk-or-not/Other/Binder/) (you need only a browser)
- [Singularity](https://sylabs.io/) `singularity run shub://pmitev/Teoroo-singularity:gawk 'BEGIN{ for(i=1;i<=4;i++) print i}'`

??? "Feedback from previous workshops"

    - [2024.08](https://docs.google.com/forms/d/1GRELoVvXo975c4lQkx9a8k-93mxXe-WqQaZg_Zk5HeA/viewanalytics) | [2024.01](https://docs.google.com/forms/d/1eGzI8FxBlhP6SV8iPQPTfQn7CWJyBf4ZaCmvJ2srxDk/viewanalytics)
    - [2023.09](https://docs.google.com/forms/d/16xCpKhhHqhcQpN-tD7yiFxoIhN3_7fp5-IpsUUOAgxM/viewanalytics) | 2023.01 (not enough data to be anonymous)
    - [2022.09](https://docs.google.com/forms/d/1UUZP97qXq3rwxY7VGJsu1w-4QWfRCzEmO1xZWva-CVM/viewanalytics) | [2022.01](https://docs.google.com/forms/d/1mIboAG1nudj1yPN07-HZbQ6L9ghlZxrCLTFbAMJpARg/viewanalytics)
    ​- [2021.09](https://docs.google.com/forms/d/1GILWudpKGoZSkyfkyBR-kRGTYieoXC1yPOz0Jn0UrcI/viewanalytics) | [2021.01](https://docs.google.com/forms/d/1be529TgFwsaNnsH_YQ-6qJWFNV15NTl510dWqrqzu1A/viewanalytics)
    - [2020.08](https://docs.google.com/forms/d/1I6tMA-mXy5kIMEy5H1Nt2fbKcuMZpvxE_WYpJPkAJ5Q/viewanalytics) | [2020.01](https://docs.google.com/forms/d/1Wa9lCwxp0Pes38KFziilNbdcvYfHwxBiou9j3c3hNO0/viewanalytics)
    - [2019.08](https://docs.google.com/forms/d/1-wha3xg_jkcZ03ljF6HmPnTFQGzGe08Jun5c0IAFfEU/viewanalytics) | [2019.01](https://docs.google.com/forms/d/1O1v8i3f1UDavfmntbEZ9cvm8_U-5Mj5P6GTEHUWyuuk/viewanalytics)
    - [2018.08](https://docs.google.com/forms/d/1PG8dt0LSOdp9gv1rFCjEe1kiapx3a-SiSJkvl2MOlyA/viewanalytics) | [2018.01](https://docs.google.com/forms/d/1d85npGj6O5xuQEF9drBRhneqYKjW0yAZJOnTiI1QP0c/viewanalytics)
    - [2017.01](https://docs.google.com/forms/d/1aTeYzOJTLNVkRYnXqOAOWFbtWIzgigqbt6hvuc4EBoE/viewanalytics) | [2017.08](https://docs.google.com/forms/d/1Y_D8kKDHsVCeu3Hli87iphnxp_ayNXfVJRcmFDiSe7Y/viewanalytics)
    - [2016.08](https://docs.google.com/forms/d/1PXdyRsABx60Uq6mDwepKv8-0ztur8z9dEkoUOmmfqjg/viewanalytics) | [2016.01](https://docs.google.com/forms/d/11q4-HAOSy7LB8mla0EkP0PhkfuBVdyIpOKb9pSqCkb0/viewanalytics)
    - [2015.10](https://docs.google.com/forms/d/1KSab3x3IlXdgtTScXPfHbFR81FrEpZ8j__hOgV8P5wU/viewanalytics)


## Contacts for the course

---
[Pavlin Mitev](https://katalog.uu.se/profile/?id=N3-1425)
[Jonas Söderberg](https://katalog.uu.se/empinfo/?id=N2-1277)
[Lars Eklund](https://katalog.uu.se/empinfo/?id=N5-89)
[Richel Bilderbeek](https://www.katalog.uu.se/empinfo/?id=N21-617)
[UPPMAX](https://www.uu.se/en/centre/uppmax)


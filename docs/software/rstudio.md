---
tags:
  - RStudio
---

# RStudio

RStudio is an IDE specialized for [the R programming language](r.md).

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

Using RStudio differs per UPPMAX cluster:

- [RStudio on Bianca](../software/rstudio_on_bianca.md)
- [RStudio on Rackham](../software/rstudio_on_rackham.md)


## RStudio versions

???- question "Which versions of RStudio are available?"

    Use `module spider Rstudio` to see all versions:


    ```bash
    [richel@r210 richel]$ module spider Rstudio

    ----------------------------------------------------------------------------
      RStudio:
    ----------------------------------------------------------------------------
         Versions:
            RStudio/1.0.136
            RStudio/1.0.143
            RStudio/1.0.153
            RStudio/1.1.423
            RStudio/1.1.463
            RStudio/1.4.1106
            RStudio/2022.02.0-443
            RStudio/2022.02.3-492
            RStudio/2022.07.1-554
            RStudio/2023.06.0-421
            RStudio/2023.06.2-561
            RStudio/2023.12.1-402 (may not always work)
    ```

Some links between version and official documentation:

RStudio module         |RStudio Builds documentation
-----------------------|-----------------------
`RStudio/2023.06.2-561`|[here](https://dailies.rstudio.com/version/2023.06.2+561.pro1/)


## Troubleshooting

### R encountered a fatal error

Full error message:

```text
R encountered a fatal error. The session was terminated.
```

![R encountered a fatal error. The session was terminated](./img/rstudio_error_r_encountered_a_fatal_error.png)

This is because the home folder is full.

Check this by using [uquota.md](uquota.md).

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [richel@rackham3 ~]$ uquota
    Your project     Your File Area       Unit        Usage  Quota Limit  Over Quota
    ---------------  -------------------  -------  --------  -----------  ----------
    home             /home/sven           GiB          24.7           32
    home             /home/sven           files       79180       300000
    naiss2024-22-49  /proj/worldpeace     GiB           5.1          128
    naiss2024-22-49  /proj/worldpeace     files       20276       100000
    ```

Candidates for files that are too big, that are hidden files:

- `.RData`
- `.Renviron`
- `.Rhistory`

One can use `ls -all` to see all files, including hidden files:

```bash
ls --all
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [sven@rackham2 ~]$ ls --all
    .                      .gtkrc               .nextflow.log.8
    ..                     .ICEauthority        .nextflow.log.9
    .allinea               .ipython             .nv
    .bash_history          .java                .oracle_jre_usage
    .bash_logout           .jupyter             .pki
    .bash_profile          .kde                 private
    .bashrc                .keras               .profile
    .bashrc.save           .lesshst             .python_history
    .beast                 lib                  .r
    bin                    .lmod.d              R
    .cache                 .local               .RData
    .conda                 .login               .Rhistory
    .config                .MathWorks           .rstudio-desktop
    .cshrc                 .matlab              .ssh
    .dbus                  .mozilla             .subversion
    DNABERT_2              my_little_turtle.py  ticket_297538
    .emacs                 .nextflow            users
    .esd_auth              .nextflow.log        .viminfo
    .gitconfig             .nextflow.log.1      .vscode-oss
    .git-credential-cache  .nextflow.log.2      .vscode-server
    glob                   .nextflow.log.3      .wget-hsts
    .gnupg                 .nextflow.log.4      .Xauthority
    .gracetimefile         .nextflow.log.5      .xfce4-session.verbose-log
    .gradle                .nextflow.log.6      .xfce4-session.verbose-log.last
    .gstreamer-0.10        .nextflow.log.7      .zshrc
    ```

You can delete these hidden files, by:

```bash
rm .RData
rm .Renviron
rm .Rhistory
```

???- note "For staff"

    Full report can be found at RT ticket 298623


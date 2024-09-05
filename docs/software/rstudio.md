# RStudio

RStudio is an IDE specialized for [the R programming language](r.md).

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

Using RStudio differs per UPPMAX cluster:

- [RStudio on Bianca](../software/rstudio_on_bianca.md)
- [RStudio on Rackham](../software/rstudio_on_rackham.md)


## RStudio versions


```
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
        RStudio/2023.12.1-402
```

Some links between version and official documentation:

RStudio module         |RStudio Builds documentation
-----------------------|-----------------------
`RStudio/2023.12.1-402`|[here](https://dailies.rstudio.com/version/2023.12.1+402.pro1/)


## Troubleshooting

### R encountered a fatal error

Full error message:

```text
R encountered a fatal error. The session was terminated.
```

![R encountered a fatal error. The session was terminated](./img/rstudio_error_r_encountered_a_fatal_error.png)

Hypothesis: the home folder is full.
Check this by using [uquota.md](uquota.md).

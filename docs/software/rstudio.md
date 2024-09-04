# RStudio

RStudio is an IDE specialized for [the R programming language](r.md).

???- tip "What is an IDE?"

    See [the page on IDEs](../software/ides.md).

Using RStudio differs per UPPMAX cluster:

- [RStudio on Bianca](../software/rstudio_on_bianca.md)
- [RStudio on Rackham](../software/rstudio_on_rackham.md)

## Troubleshooting

### R encountered a fatal error

Full error message:

```
R encountered a fatal error. The session was terminated.
```

![R encountered a fatal error. The session was terminated](rstudio_error_r_encountered_a_fatal_error.png)

Hypothesis: the home folder is full.
Check this by doing this in the home folder:

```bash
du --max-depth 1 .
```

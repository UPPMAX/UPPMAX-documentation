# Contributing

Thanks for considering to contribute and reading this!

Here we discuss how to contribute

- [spoken text](#spoken-text), e.g. ideas, feedback, messages, etc. and are written in English.
- [code](#code), e.g. textual changes where the text is formatted in Markdown

## Spoken text

Spoken text are ideas, feedback, messages, etc. and are written in English.

For ideas or feedback, create an [Issue](https://github.com/UPPMAX/UPPMAX-documentation/issues).
These Issues will be discussed in a meeting and/or below that Issue.

Ideas that improve the experience of UPPMAX users trying to use our resources will likely be accepted.

## Code

We welcome any contribution that:

- improves the experience of UPPMAX users trying to use our resources
- follow all standards set by the continuous integration tools (e.g. use 4 spaces for indentation)
- puts the files in reasonable folders (see [Where to put files?](#where-to-put-files) below)

As an UPPMAX contributor, one can contribute by:

1. Clone this repository
1. Add a branch
1. Work on your branch
1. When done, create a Pull Request from your branch to `main`
1. If the change is accepted after review it will be merged into the main branch
1. Your branch will be deleted after merging

As an external contributor, one can contribute by:

1. Fork this repository
1. Modify your Fork
1. When done, creating a Pull Request from your Fork to this repository,
   merging to the `main` branch is fine :-)
1. If the change is accepted after review it will be merged into the main branch

## Where to put files?

All files are put in `docs` or `docs/[some_folder]`,
but not not deeper than that.

Description                                | Where          | Typical name
-------------------------------------------|----------------|------------------------------------------
Information about clusters                 |`cluster_guides`|`bianca.md`, `rackham.md`, `snowy.md`
Information about Slurm                    |`cluster_guides`|`slurm.md`
Information about general cluster processes|`cluster_guides`|`[general_process_name].md`
Cluster-specific information for software  |`software`      |`[x]_on_bianca.md`
Software in general                        |`software`      |`[name of program].md`

Examples on file transfer:

- `cluster_guides/bianca_file_transfer_using_rsync.md`
- `software/rsync.md`
- `cluster_guides/file_transfer.md`

Examples on job scheduler:

- `software/slurm_on_bianca.md`
- `software/squeue.md`
- `software/sbatch.md`
- `cluster_guides/slurm.md`

Examples on general software use:

- `software/gcc.md` (a collection of programs is software)
- `software/gcc_compile_c.md` (same for all clusters)

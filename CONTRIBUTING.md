# Contributing

Thanks for considering to contribute and reading this!

Here we discuss how to contribute

- [Spoken text](#spoken-text), e.g. ideas, feedback, messages, etc. and are written in English.
- [Code](#code), e.g. textual changes where the text is formatted in Markdown
- [Where to put files](#where-to-put-files)
- [Which branch](#which-branch)

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

## Where to put a new page: here or at <https://www.uu.se/en/centre/uppmax>?

- <https://www.uu.se/en/centre/uppmax> is our 'landing page'.
  It’s for 'nice' looking pages with general information about UPPMAX,
  which don’t need to be updated very often.
  The news function and a calendar of events can be here as well,
  because it makes sense for this to be visible on our homepage.
  There's supposed to be an automatically-generated list of staff as well.
- this page: is for more detailed documentation for our users,
  for pages that we want to automate, etc.
  Guides, documentation, anything with code snippets.

I’m sure there are things that fall in a grey zone,
but we can discuss that a little and then decide what’s best.

## Where to put files

All files are put in `docs` or `docs/[some_folder]`,
but not not deeper than that.

Description                                             | Where          | Typical name
--------------------------------------------------------|----------------|------------------------------------------
Information about clusters                              |`cluster_guides`|`bianca.md`, `rackham.md`, `snowy.md`
Information about Slurm                                 |`cluster_guides`|`slurm.md`
Information about general cluster processes             |`cluster_guides`|`[general_process_name].md`
Cluster-specific information about Slurm                |`cluster_guides`|`slurm_on_bianca.md`, `slurm_[something].md`
Cluster-specific information for software, except Slurm |`software`      |`[x]_on_bianca.md`, `rackham_do_something_with_[x].md`
Software in general, except Slurm                       |`software`      |`[name of program].md`

Examples on file transfer:

- `software/bianca_file_transfer_using_rsync.md`
- `software/rsync.md`
- `cluster_guides/file_transfer.md`

Examples on job scheduler:

- `cluster_guides/slurm_on_bianca.md`
- `software/squeue.md`
- `software/sbatch.md`
- `cluster_guides/slurm.md`

Examples on general software use:

- `software/gcc.md` (a collection of programs is software)
- `software/gcc_compile_c.md` (same for all clusters)

## Which branch

Submitting to the main branch is fine! Thanks!

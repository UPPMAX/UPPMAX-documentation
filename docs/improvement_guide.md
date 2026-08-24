---
tags:
  - contributing
  - writing
  - restructuring
---

# Guidelines for improving this documentation

## Documentation usecases

Documentation is used in three distinct ways by readers:

1. As reference material: for looking up specific information.
2. As step-by-step guides: for following a prescribed procedure.
3. As learning material: for in-depth learning.

Note that a reader will only choose the third option if/when they regard the
topic at hand as a skill worth investing time in, a long-term tool.
Most tools are often regarded as temporary or secondary skills, hence the reader
will prefer options&nbsp;1 and&nbsp;2.
The entire field of HPC may be seen that way by many of our readers.

This documentation is mostly written as for cases&nbsp;2 and&nbsp;3, with a
widespread and occasionally severe lack of focus on usecase&nbsp;1.
Writing with more focus on use as reference material is therefore one major
avenue for improving this documentation.

## Restructuring

> A clear and concise navigation structure is an important aspect of good
> project documentation.
>
> &mdash; <cite>[Zensical documentation](https://zensical.org/docs/setup/navigation/)</cite>

This holds true both for readers and authors.

Not-in-nav pages are antithetical to structured documentation.
They can be very confusing for both readers and authors.

Information that should be a part of the documentation should also have a
natural place in the structure of the documentation.
There should be one, and as far as possible only one, obvious place to look for
any piece of information.
This is sometimes hard to achieve, in which case it is generally worthwhile to
work on.

### The case for file structure as navigation structure

Authors working on a webpage are not necessarily tied to working within the same
structure as is presented on the page (as they would be if working on a single
document).
This creates far more problems than it solves:

- Duplicate information in disparate places
- Related information in disparate places
- Unnecessarily difficult to navigate/understand project structure
- **Lack of awareness about structure and context when authoring**

A good way to work would be to use the file structure as the navigation
structure for the website, with some structured way of doing exceptions for
extreme edgecases such as the website landing page and external links directly
in the navigation. One additional desirable feature would be to have the option
to collapse/show by default at different depths of navigation, because some
branches are naturally deeper or shallower before they get to specifics.

Zensical have a large overhaul of navigation features on their
[roadmap](https://zensical.org/about/roadmap/#modular-navigation).
Whether the way of working I suggest in the previous paragraph will be
well-supported or not is an open question, but I'm hopeful it will.

### The attempt started by Linus

An attempt to create a structure for this documentation is in the branch
[restructuring](https://github.com/UPPMAX/UPPMAX-documentation/tree/restructuring).
Background work and a work-in-progress proposed structure is in the folder
[restructuring-workdir](https://github.com/UPPMAX/UPPMAX-documentation/tree/restructuring/restructuring-workdir).

The `mkdocs.yml` config file has been replaced by a very basic `zensical.toml`
as a quick way to use the file structure as navigation structure.

This has surfaced many pages with zero or questionable usefulness and repeatedly
showcased the four problems listed above.

Some of the existing pages do not fit neatly in the proposed structure.
Some of the proposed structure will require the writing of new pages.

Some of the proposed structure may be wise, some of it may be foolish.

## Write for faster reading

### Search reading

### Continuous reading

## Snippets

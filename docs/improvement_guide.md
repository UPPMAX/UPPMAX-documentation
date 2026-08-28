---
tags:
  - contributing
  - writing
  - restructuring
---

# Guidelines for improving this documentation

!!! Note
    This page itself is written in a style not fully appropriate for any other
    page of the documentation. It is not to be taken as an example, it is to be
    read as guiding note or lecture showing a path forward.

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

## Style: write for faster reading

There are many style guides for writing, for different subject matter and for
different intended audiences&mdash;the two origins for how to write.

!!! note "What we're writing here:"
    Documentation for professional tooling.

!!! note "Who we're writing it for:"
    These professionals are *researchers*.

This means that our audience is more likely than not to prefer a less
conversational, more efficient style than that of e.g. Microsoft or Google
documentation.
They want to learn things or look things up as quickly as possible and they are
some of the most proficient people on the planet at doing so.

In some cases they are newcomers to all of HPC and Linux and terminals, in other
cases they are veterans of all three looking for a new or forgotten detail or
procedure.

This is the audience to keep in mind.
Do not waste their time.

### Optimize for scanning

#### When: always, why: to help every reader every time

Most reading of documentation will be done in a scanning strategy, looking to
identify the wanted bit of information as quickly as possible.
Reference material is essentially only read this way.

With step-by-step guides, beware!
Authors can fall into the trap of assuming that readers will fully read and then
fully execute every step in order.
In practice, that is an extremely rare case.
Most tasks will be self-explanatory or include their own instructions, causing
even a hypothetical user without pre-existing knowledge or assumptions to
occasionally skip ahead, which may in turn cause a need to skip back and
reconcile the inevitable differencies between the instructions and the reality.

Thus, in good documentation, even the step-by-step guides are highly optimized
for the reader scanning for any specific bit of information in it.

Text written primarily to be read as a full document with a flow to it can also
be optimized for fast scanning when the reader instead is looking for specific
details.
Professional technical and scientific reports are often good examples of this.

#### How to: some techniques

* Front-load good clues about the current topic of the text at every
  opportunity.
    - Descriptive headings and good structure.
        * Good structure is comprehensive and enables each part of the text to
          make use of the context given by the surrounding parts of the text.
    - Focused paragraphs, with at least a key phrase or a couple of key words at
      the beginning of each paragraph, so that it can be quickly and confidently
      skipped when irrelevant.
* Keep the text short. Less scrolling and reading for the same amount of
  information gets the reader to where they want faster.
   - Each paragraph, each section, each page, each directory of pages should be
     kept short enough to be scanned somewhat instantly by our average reader.
* Formatting should be consistent and purposeful.
    - Focussing on the wanted information is easier when unwanted information
      can be easily ignored.
    - Finding related or specific information is greatly helped if it *always*
      looks the same. If the reader cannot rely on visual consistency,
      effortless scanning quickly turns into tedious careful reading.
    - Attention-grabbing formatting (such as colourful admonitions) should only
      be used to call out something that nobody reading the page should ignore.
    - Especially optional information, e.g. videos or extra screenshots, should
      be formatted in a consistent and easy-to-ignore way, perhaps a grey
      admonition style? ABSOLUTELY NO IMPORTANT INFORMATION can ever be
      formatted THE SAME WAY AS THE OPTIONAL STUFF.
* Terminology and framing should be consistent. This makes it easier not only to
  scan the text by eye, it also makes it easier to search the documentation with
  tools or even to summarize it with an LLM.

This can make for efficient reading in terms of time, focus and energy also for
readers who are reading through the whole page without scanning for something
specific.

### Style guides

AFAIK, no existing comprehensive style guide is directly applicable to our
usecase.

Many style guides are based on US English, while we have recently decided to go
with UK spellings instead.
Note that regional differences occur in all parts of language, not just
spelling, so it is not wise to base our style on a US-based style guide
(consistency is a fundamental good in these matters).

A combination of parts of the following, with all previous information on this
page as a guide for which parts to adopt and which parts to ignore, may be a
good basis for a good writing style for HPC documentation:

* Resources on good, relevant, style:
    - [GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/)
      has what appears to be the best starting points and reference guides for
      our use, including their
      [Technical A to Z style guide](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/technical-a-to-z/)
      and some excellent writing guidelines such as
      [Write content to meet user needs](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/meet-user-needs/)
      and
      [Create a clear structure for your content](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/).
      Clearly we may need to deviate, e.g. with regards to footnotes.
    - [Stylish Academic Writing, Helen Sword](https://www.hup.harvard.edu/books/9780674064485)
      is a book I have not read or even acquired yet, but from the description
      it seems to be a well-informed guide to a writing style that our audience
      would highly appreciate.
* Relevant terminology may be found in related projects:
    - [Rocky Linux Documentation Style Guide](https://docs.rockylinux.org/10/guides/contribute/style_guide/#style-guidelines)
      is relevant due to our underlying OS being Rocky Linux. Alas, their guide
      does not (currently) seem very useful to us, but their documentation as a
      whole can be used for finding canonical terminology.
    - EuroHPC JU currently does not have so much as a glossary, even though they
      probably should.
      [Their publications](https://www.eurohpc-ju.europa.eu/media-events/publications_en)
      may be assumed to be written with canonical terminology.
    - University of Arizona has a long history of HPC know-how and their current
      [UArizona HPC Documentation Site](https://hpcdocs.hpc.arizona.edu)
      can serve as a good model, perhaps as a good external resource.
* Less relevant but more comprehensive resources:
    - [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
      is a comprehensive resource and a standard/classic in software
      documentation, but consistently too conversational, verbose and
      inefficient for professional tooling and for academic readers. And
      US-based.
    - [Red Hat Technical Writing Style Guide](https://stylepedia.net/style/)
      is another comprehensive one, also US-based.
    - [Red Hat supplementary style guide for product documentation](https://redhat-documentation.github.io/supplementary-style-guide/)
      is what is used for the documentation that may be relevant. It is based
      not on the above Red Hat guide, but on the IBM guide, which is not
      distributed. Nevertheless, this is the kind of supplement that placed on
      top of the GOV.UK guides might make for a comprehensive style guide for
      our usecase.
    - [Simplified Technical English, ASD-STE100](https://www.asd-ste100.org/about_STE.html):
      a European, originally aerospace, standard for the language of technical
      documentation. Strictly adhering to this is probably too dry and
      rudimentary, but learning it may be a great guide towards writing that is
      quicker to understand. This is about grammar and wording and does not deal
      with other aspects of style.

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

### The goals

To always have an overview of what information is in here and what isn't.

To make it easy to keep the documentation structured, focussed, complete and
up-to-date.

### How to achieve and maintain those goals

This is MUCH easier to do when the structure is already good.

The basic task is this: look at all related pages / sections / pieces of
information and answer these questions:

- Should it be kept and continually reworked and improved?
- Should it instead be archived, but in an accessible manner?
  (In this case it should be reworked as to be future-proof, with zero outgoing
  links and zero information with unclear best-before-date.)
- Should it be removed?

After you've done so, look at all remaining related pieces and look at their
relative organization.

- Can something get a better heading? Good headings are both short and
  descriptive.
- Should something be moved? Sequentially or hierarchically?
- Is this related to information

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

## Snippets

This is an
[existing feature](https://zensical.org/docs/setup/extensions/python-markdown-extensions/#snippets)
within the Zensical / Python Markdown system.
We have some usecases for this, such as video guides, "Forgot your project ID?"
et.c.

## Shortlist of weak points to improve upon

- Structure, headings, comprehensive navigation
- The green question admonitions are used too widely, I never know if I need to
  read them or need to ignore them
- Visual clutter other than that, on some pages (e.g. Slurm on Pelle)
- Clutter in terms of unneeded pages and information
- Repetition, saying the same things way too many times and on way too many
  pages (repetition may be good for learning, but in documentation it mostly
  takes up space and causes confusion)
- Verbosity (yes this includes this page)

Priority one is clearly structure and headings.
Priority two should be consistency, and please include the usage of question
admonitions in here.
Third, but nonetheless as an explicit priority, I recommend to rework every
single page (most important and most problematic pages first) with the goal of
making it as friendly as possible to readers scanning for some specific detail.

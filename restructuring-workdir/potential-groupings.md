# Potential groupings

This is a note trying to list many potentially helpful
groupings/categories/buckets that pages of the documentation might belong to,
before deciding on which ones to use for the structure. The rest may be useful
as tags or found not sufficiently helpful.

It should not make sense to keep this file around after deciding on a structure.
The groupings used for structure is readily apparent and available, while the
groupings found helpful but not used in the structure should be available by
taking inventory of all tags used.

At this point, I do not attempt to sort or group these, I just try to find as
many as possible. Nevertheless, there is one group of groupings big enough that
I will make use of it, let's start there.

## The list

### Specific to and general across...

- Linux
- Servers
- Linux servers
- Clusters
- HPC clusters
- NAISS clusters
- UPPMAX clusters
- Clusters relevant to UPPMAX users (ignore lateral alternatives, but remember
  that LUMI has AMD GPUs if our users need to scale up (perhaps unlikely given
  the GPU power of Arrhenius and Mimer?))
- Any specific cluster
- Slurm
- LMOD
- Distributed memory
  - MPI implementations
  - MPI jobs
  - Any other way of doing distributed memory work
- Multithreaded with a single set of memory
- GPU usage (vendor agnostic)
- Nvidia GPU usage
- Python
- any other programming language/environment
- pre-written software, i.e. whenever the user is not the author of the code
- user-written code
- Accessing from
  - Windows
  - Mac OS
  - Linux

### Tasks

- Logging in
  - for interactive access to login nodes
  - for file transfer
- Transferring files
- Running non-interactive jobs
- Interactive jobs
- Running specific software
- Figuring out what you need / what you want / what your available choices are
  (e.g. I have this niche software I need to run, how do I find out what kind of
  job it is or can be in HPC terms? What cluster should I apply for an account
  at? How big/wide can I make my computation, at what cost? How do I know
  whether I should or can use GPUs?)

### Other kinds of groupings

- Guides
- Reference material (the opposite of guides, optimized for looking things up
  rather than following a procedure)
- Level of detail (not sure how to name or group the different levels here)
- Level of expertise/experience

## New list: groupings indicated by inventory of tags

From the file tags-counted-as-of-dfa35a.txt we learn that our most-used tags can
be summarized as:

- Bianca
- Pelle
- File/data transfer
- UPPMAX
- login
- terminal
- SSH

Then there's two that have numerous pages even though they probably shouldn't
have numerous pages in this set of documentation:

- RStudio
- Python

And two that are entirely unhelpful and should not be used as tags at all as
they don't really specify a topic at all, at least in this context (create what?
software in which role?):

- create
- software
- tool
- session  (found further down, same problem)

After that there's both deeper subsections...:

- FileZilla
- Transit
- rsync
- scp
- ThinLinc
- WinSCP
- password
- MFA / 2FA

...and new categories:

- Singularity
- build
- Dardel
- project
- course
- application
- module
- COSMOS
- Tetralith
- SUNET
- R
- NAISS
- Linux
- Jupyter

## Third list: groupings indicated by the AI-wiki

From the file grouped-top-topics-from-AI-wiki.txt, where I have manually
grouped the topics that referred to three or more pages in the
documentation---with reservation for cases of duplicate filenames, which have
been counted as a single page by the AI wiki system (and documented in
duplicate-filenames-in-docs.txt).

This (probably) includes all large categories but ignores some important ones.
It can be summarized as follows (partially structured):

- Access
  - Login
  - File transfer
- HPC in general
- Terminal / CLI tools
- Text editors
- Programming and adjacent tools
  - IDEs
  - Notebooks
  - Debugging
  - Profiling and optimization
  - Programming languages
    - Python
    - R
  - Compilers
- Containerization
- Security
- Isolation
- Specific research softwares
  - Bioinformatics
  - Genomics
- Data analysis
- Machine learning
- Resources and job management: Slurm
- Module / software / package -management
- Software installation
- Project management
- Account management
- Cluster management?
- Data / storage -management
  - Version control
  - File managers
  - Compression
- Permissions
- Database management
- Documentation
- Environment management
- Scripting
- Networking
- Naming conventions
- Support

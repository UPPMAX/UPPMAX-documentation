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

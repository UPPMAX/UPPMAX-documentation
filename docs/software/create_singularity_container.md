---
tags:
  - Singularity
  - Singularity container
  - create
  - build
---

# Creating a Singularity container

There are many ways to create a [Singualrity](singularity.md) container.

## How and where to build?

Here is a decision tree on how and where to build a Singularity container.

```mermaid
flowchart TD
  where_to_build[Where to build my Singularity container?]
  where_to_build --> have_linux
  have_linux[Do you have Linux with sudo rights and Singularity installed?]
  build_short[Is the build short?]
  use_linux(Build on Linux computer with sudo rights)
  use_remote_builder_website(Build using Sylabs remote builder website)
  use_remote_builder_rackham(Build using Sylabs remote builder from Rackham)

  have_linux --> |yes| use_linux
  have_linux --> |no| build_short
  build_short --> |yes| use_remote_builder_website
  build_short --> |yes| use_remote_builder_rackham
```

How and where                                                                                                             |Features
--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------
[Local Linux](create_singularity_container_from_a_singularity_script_on_linux.md)                                         |Easiest for Linux users, can do longer builds
[Remote builder from website](create_singularity_container_from_a_singularity_script_using_remote_builder.md)             |Easiest for non-Linux users, short builds only
[Remote builder from Rackham](create_singularity_container_from_a_singularity_script_using_remote_builder_from_rackham.md)|Can do longer builds

# Data transfer to/from Pelle using Transit

!!! warning "Does not work yet"

    [Pelle](../cluster_guides/pelle.md) is a new UPPMAX HPC cluster
    that is in the process of being deployed.

    The procedure as described on this page does not work yet or is untested.

    This page will be updated when this works.

Data transfer to/from Pelle using [Transit](../cluster_guides/transit.md)
is one of the ways ways to transfer files to/from Pelle

???- question "What is Transit?"

    See [the page about the UPPMAX Transit server](transit.md).

???- question "What are the other ways?"

    Other ways to transfer data to/from Pelle are described [here](transfer_pelle.md)

This page assumes your files are 'posted' to Transit.
[Transit is a service, not a file server](transit.md).

???- question "How to transfer files to/from Transit?"

    See [here](transfer_transit.md)

To transfer files between Pelle and Transit can be done in multiple ways too:

- [Using SCP](../software/pelle_file_transfer_using_transit_scp.md)
- [Using SFTP](../software/pelle_file_transfer_using_transit_sftp.md)

## Overview

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#fcf,color:#000,stroke:#f0f
    classDef calculation_node fill:#ccf,color:#000,stroke:#00f
    classDef transit_node fill:#fff,color:#000,stroke:#fff

    subgraph sub_inside[SUNET]
      direction LR
      user(User)
      subgraph sub_transit_env[Transit]
        transit_login(Transit login):::calculation_node
        files_on_transit(Files posted to Transit):::transit_node
      end
      subgraph sub_pelle_shared_env[Pelle]
          files_in_pelle_home(Files in Pelle home folder):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#ccc,color:#000,stroke:#000
    style sub_transit_env fill:#cfc,color:#000,stroke:#000
    style sub_pelle_shared_env fill:#fcc,color:#000,stroke:#000

    user --> |logs in |transit_login

    transit_login --> |can use|files_on_transit
    %% user_local_files <--> |graphical tool|files_in_pelle_home
    %% user_local_files <--> |SCP|files_in_pelle_home
    files_on_transit <==> |transfer|files_in_pelle_home
```

> Overview of file transfer on Pelle
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.

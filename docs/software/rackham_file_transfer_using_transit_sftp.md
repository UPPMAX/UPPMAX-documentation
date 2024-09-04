# Data transfer to/from Rackham using Transit and SFTP

Data transfer to/from Rackham using [Transit](../cluster_guides/transit.md)
is one of the ways ways to transfer files to/from Rackham

One can use SFTP to copy files between Rackham and Transit,
from either Rackham or Transit.

Both ways are shown step-by-step below.

- [Using SFTP from Rackham](rackham_file_transfer_using_transit_sftp_from_rackham.md)
- [Using SFTP from transit](rackham_file_transfer_using_transit_sftp_from_transit.md)

Basic `sftp` command can be found [here](../software/sftp.md).

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
      subgraph sub_rackham_shared_env[Rackham]
          files_in_rackham_home(Files in Rackham home folder):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#ccc,color:#000,stroke:#000
    style sub_transit_env fill:#cfc,color:#000,stroke:#000
    style sub_rackham_shared_env fill:#fcc,color:#000,stroke:#000

    user --> |logs in |transit_login

    transit_login --> |can use|files_on_transit
    %% user_local_files <--> |graphical tool|files_in_rackham_home
    %% user_local_files <--> |SCP|files_in_rackham_home
    files_on_transit <==> |transfer|files_in_rackham_home
```

> Overview of file transfer on Rackham
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.

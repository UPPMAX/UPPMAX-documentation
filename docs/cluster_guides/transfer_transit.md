# Data transfer to/from Transit

There are multiple ways to transfer files to/from Transit:

Method                                                        |Features
--------------------------------------------------------------|---------------------------------------------
[Using a graphical program](#using-a-graphical-program)       |Graphical interface, intuitive, for small amounts of data only
[Using SCP](#using-SCP)                                       |Terminal, easy to learn, can be used in scripts
[Using SFTP](#using-SFTP)                                     |Terminal, easy to learn, secure

Each of these methods is discussed below.

## Using a graphical program

One can transfer files to/from Transit using a graphical program.
A graphical interface is intuitive to most users.
However, it can be used for small amounts of data only
and whatever you do cannot be automated.

See [Transit file transfer using a graphical program](transit_file_transfer_using_gui.md)
for a step-by-step guide how to transfer files using
a graphical tool.

## Using SCP

One can transfer files to/from Transit 
using SCP in a terminal.
This works similar to a regular copy of files,
except that a remote address needs to be specified.
The advantage of SCP is that is can be used in scripts.

See [Transit file transfer using SCP](transit_file_transfer_using_scp.md)
for a step-by-step guide how to transfer files using SCP.

## Using SFTP

One can transfer files to/from Transit using SFTP in a terminal.
One connects a local and a remote folder, 
after which one can upload and download files.
SFTP is considered a secure file transfer protocol.

See [Transit file transfer using SFTP](transit_file_transfer_using_sftp.md)
for a step-by-step guide how to transfer files using SFTP.

## Using `transit`

One can transfer files to/from Transit using the UPPMAX `transit` server.
One connects a local folder and the `transit` server, 
after which one can upload and download files.

See [Transit file transfer using `transit`](transit_file_transfer_using_transit.md)
for a step-by-step guide how to transfer files using the `transit` UPPMAX server.

### Overview

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#fff,color:#000,stroke:#000
    classDef calculation_node fill:#ccf,color:#000,stroke:#00f
    classDef transit_node fill:#fff,color:#000,stroke:#fff

    subgraph sub_inside[SUNET]
      user_local_files(Local user files):::file_node

      subgraph sub_transit_env[Transit]
        files_on_transit(Files posted to transit):::transit_node
      end
      subgraph sub_rackham_shared_env[Rackham]
        files_in_rackham_home(Files in Rackham home folder):::file_node
      end
      subgraph sub_bianca_private_env[Bianca]
        files_in_bianca_project(Files in Bianca project folder):::file_node
      end
      subgraph sub_other_clusters[Other clusters]
        files_on_other_clusters(Files on other clusters):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#ccc,color:#000,stroke:#000
    style sub_transit_env fill:#cfc,color:#000,stroke:#000
    style sub_rackham_shared_env fill:#fcc,color:#000,stroke:#000
    style sub_bianca_private_env fill:#ccf,color:#000,stroke:#000
    style sub_other_clusters fill:#ffc,color:#000,stroke:#000
    

    
    user_local_files <--> |graphical tool|files_on_transit
    user_local_files <--> |SCP|files_on_transit
    user_local_files <--> |SFTP|files_on_transit

    files_on_transit <--> |SCP|files_in_rackham_home
    files_on_transit <--> |SFTP|files_in_rackham_home

    files_on_transit <--> |SCP|files_in_bianca_project
    files_on_transit <--> |SFTP|files_in_bianca_project

    files_on_transit <--> |transfer|files_on_other_clusters

```

> Overview of file transfer on Transit

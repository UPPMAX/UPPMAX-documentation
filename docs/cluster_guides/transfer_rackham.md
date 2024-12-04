---
tags:
  - Rackham
  - file
  - transfer
  - data
---

# File transfer to/from Rackham

There are multiple ways to transfer files to/from Rackham:

Method                                                        |Features
--------------------------------------------------------------|---------------------------------------------
[Using a graphical program](#using-a-graphical-program)       |Graphical interface, intuitive, for small amounts of data only
[Using SCP](#using-scp)                                       |Terminal, easy to learn, can be used in scripts
[Using SFTP](#using-sftp)                                     |Terminal, easy to learn, secure
[Using transit](#using-transit)                               |Terminal, easy to learn, secure, can transfer between HPC clusters

Each of these methods is discussed below.

## Using a graphical program

One can transfer files to/from Rackham using a graphical program.
A graphical interface is intuitive to most users.
However, it can be used for small amounts of data only
and whatever you do cannot be automated.

See [Rackham file transfer using a graphical program](rackham_file_transfer_using_gui.md)
for a step-by-step guide how to transfer files using
a graphical tool.

## Using SCP

One can transfer files to/from Rackham
using SCP in a [terminal](../software/terminal.md).
This works similar to a regular copy of files,
except that a remote address needs to be specified.
The advantage of SCP is that is can be used in scripts.

See [Rackham file transfer using SCP](../software/rackham_file_transfer_using_scp.md)
for a step-by-step guide how to transfer files using SCP.

## Using SFTP

One can transfer files to/from Rackham using SFTP in a [terminal](../software/terminal.md).
One connects a local and a remote folder,
after which one can upload and download files.
SFTP is considered a secure file transfer protocol.

See [Rackham file transfer using SFTP](../software/rackham_file_transfer_using_sftp.md)
for a step-by-step guide how to transfer files using SFTP.

## Using `transit`

One can transfer files to/from Rackham using the UPPMAX `transit` server.
One connects a local folder and the `transit` server,
after which one can upload and download files.

See [Rackham file transfer using `transit`](rackham_file_transfer_using_transit.md)
for a step-by-step guide how to transfer files using the `transit` UPPMAX server.

### Overview

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
      user_local_files(Local user files):::file_node

      subgraph sub_transit_env[Transit]
        transit_login(Transit login):::calculation_node
        files_on_transit(Files posted to Transit):::transit_node
      end
      subgraph sub_rackham_shared_env[Rackham]
          rackham_login(Rackham login node):::calculation_node
          files_in_rackham_home(Files in Rackham home folder):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#ccc,color:#000,stroke:#000
    style sub_transit_env fill:#cfc,color:#000,stroke:#000
    style sub_rackham_shared_env fill:#fcc,color:#000,stroke:#000

    user --> |has|user_local_files
    user --> |logs in |transit_login
    user --> |logs in |rackham_login

    user_local_files <--> |graphical tool|files_in_rackham_home
    user_local_files <--> |SCP|files_in_rackham_home
    user_local_files <--> |SFTP|files_in_rackham_home
    user_local_files <--> |graphical tool|files_on_transit
    user_local_files <--> |SFTP|files_on_transit

    rackham_login --> |can use|files_in_rackham_home

    transit_login --> |can use|files_on_transit
    files_on_transit <--> |transfer|files_in_rackham_home

    files_in_rackham_home ~~~ transit_login
```

> Overview of file transfer on Rackham
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.

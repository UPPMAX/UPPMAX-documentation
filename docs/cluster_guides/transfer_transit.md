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

## Overview

```
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    subgraph sub_inside[IP inside SUNET]
      subgraph sub_bianca_shared_env[Bianca]
        files_in_wharf(Files in wharf)
      end
      subgraph sub_rackham_env[Rackham]
        files_on_rackham(Files on Rackham)
      end
      user_local_files(Files on user computer)
      subgraph sub_transit_env[Transit]
        files_on_transit(Files on transit)
      end
      files_on_other_clusters(Files on other HPC clusters):::file_node
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#ccc,color:#000,stroke:#999
    style sub_bianca_shared_env fill:#cfc,color:#000,stroke:#090
    style sub_rackham_env fill:#fcc,color:#000,stroke:#900
    style sub_transit_env fill:#ccf,color:#000,stroke:#009

    user_local_files -.- files_in_wharf
    user_local_files <==> |transfer files|files_on_transit
    user_local_files -.- files_on_rackham
    files_on_transit <==> |transfer files|files_in_wharf
    files_on_transit <==> |transfer files|files_on_rackham
    files_on_transit -.- |transfer files|files_on_other_clusters
```

> Overview of file transfer on Transit

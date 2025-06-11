# File transfer to/from Bianca using a graphical tool

![FileZilla connected to Bianca](./img/filezilla_login_to_bianca_236_x_266.png)

> FileZilla connected to Bianca

## Overview

As a user, we need to transfer files
between our local computer and Bianca.
There are
[many ways to transfer files to/from Bianca](../cluster_guides/transfer_bianca.md).
On this page, we learn how to transfer files
to Bianca using a graphical tool/program.

There are constraints on which programs
we can use, due to Bianca being an HPC cluster
for sensitive data.
Details are described in 'Bianca's constraints',
here are graphical tools that work:

Tool                                                |Description
----------------------------------------------------|---------------------
[FileZilla](bianca_file_transfer_using_filezilla.md)|All operating systems
[WinSCP](bianca_file_transfer_using_winscp.md)      |Windows-only

When using such a graphical tool,
one needs [to be inside of SUNET](../getting_started/get_inside_sunet.md).

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

When a tool is setup, one can only transfer files
between you local computer and [your Bianca `wharf` folder](../cluster_guides/wharf.md).

## Bianca's constraints

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#faf,color:#000,stroke:#f0f
    classDef calculation_node fill:#aaf,color:#000,stroke:#00f

    subgraph sub_inside[IP inside SUNET]
      subgraph sub_bianca_shared_env[Bianca shared network]
        subgraph sub_bianca_private_env[The project's private virtual project cluster]
          login_node(login/calculation/interactive node):::calculation_node
          files_in_wharf(Files in wharf):::file_node
          files_in_bianca_project(Files in Bianca project folder):::file_node
        end
      end
      user(User)
      user_local_files(Files on user computer):::file_node
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#fcc,color:#000,stroke:#fcc
    style sub_bianca_shared_env fill:#ffc,color:#000,stroke:#ffc
    style sub_bianca_private_env fill:#cfc,color:#000,stroke:#cfc

    user --> |logs in |login_node
    user --> |uses| user_local_files

    %% As of 2023-12-22, using `**text**` for bold face, does not render correctly
    %% user_local_files <== "`**transfer files**`" ==> files_in_wharf
    user_local_files <== "transfer files" ==> files_in_wharf

    login_node --> |can use|files_in_bianca_project
    login_node --> |can use|files_in_wharf
    files_in_wharf <--> |transfer files| files_in_bianca_project
```

> Overview of file transfer on Bianca, when using a graphical tool.
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> In this session, we will transfer files between
> 'Files on user computer' and 'Files in wharf'
> using a graphical tool, e.g. FileZilla

Bianca is an HPC cluster for sensitive data.
To protect that sensitive data,
Bianca has no direct internet connection.
This means that files cannot be downloaded directly.

???- tip "What is an HPC cluster again?"

    See [the UPPMAX page on HPC clusters](../cluster_guides/uppmax_cluster.md).

Instead, one needs to learn one of the many ways to do **secure** file transfer.

Here, we show how to transfer files using a graphical tool called FileZilla.

In general, one can pick any graphical tools with these constraints:

- the tool must support SFTP
- the tool must not store a password

Whatever tool one picks, it must do secure file transfer.
For secure file transfer, Bianca supports the SFTP protocol.
So, for secure file transfer to Bianca, one needs a tool
that supports SFTP.

???- warning "Use SFTP ... and why users think incorrectly that SCP will work"

    Only SFTP will work. SCP will never work.

    However, some users use tools that support SFTP,
    yet that have 'SCP' in the name, for example, 'WinSCP'.
    As users hear from colleagues that the tool 'WinSCP' works,
    they may incorrectly conclude that SCP will work.

    SCP will never work. Only SFTP will work.

Whatever tool one picks, additionally, the tool must **not** store a password.
Due to security reasons, one needs to connect to Bianca using a password
**and** a two-factor authentication number (e.g. `VerySecret123456`).
If a tool stores a password, that password will be valid for only one session.

One tool that can be used for file transfer to Bianca
is FileZilla, which is described in detail below.
The extra materials at the bottom of this page contain
other tools.

### File transfer overview

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#fcf,color:#000,stroke:#f0f
    classDef calculation_node fill:#ccf,color:#000,stroke:#00f
    classDef transit_node fill:#fff,color:#000,stroke:#fff

    subgraph sub_inside[IP inside SUNET]
      subgraph sub_bianca_shared_env[Bianca shared network]
        subgraph sub_bianca_private_env[The project's private virtual project cluster]
          login_node(login/calculation/interactive node):::calculation_node
          files_in_wharf(Files in wharf):::file_node
          files_in_bianca_project(Files in Bianca project folder):::file_node
        end
      end
      user(User)
      user_local_files(Files on user computer):::file_node
      files_on_transit(Files posted to Transit):::transit_node
      files_on_other_clusters(Files on other HPC clusters):::file_node
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#fcc,color:#000,stroke:#fcc
    style sub_bianca_shared_env fill:#ffc,color:#000,stroke:#ffc
    style sub_bianca_private_env fill:#cfc,color:#000,stroke:#cfc

    user --> |logs in |login_node
    user --> |uses| user_local_files
    user_local_files <--> |transfer files|files_in_wharf
    user_local_files <--> |transfer files|files_on_transit
    files_on_transit <--> |transfer files|files_in_wharf
    files_on_transit <--> |transfer files|files_on_other_clusters
    login_node --> |can use|files_in_bianca_project
    login_node --> |can use|files_in_wharf
    files_in_wharf <--> |transfer files| files_in_bianca_project
```

> Overview of file transfer on Bianca
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.

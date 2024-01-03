# Data transfer to/from Rackham using Transit

Data transfer to/from Rackham using Transit
is one of the ways ways to transfer files to/from Rackham

???- question "What are the other ways?"

    Other ways to transfer data to/from Rackham are described [here](transfer_rackham.md)

To transfer to/from Rackham using Transit can be done in multiple ways too:

 * [Using SCP](#using-scp)
 * [Using SFTP](#using-sftp)

## Using SCP


### Login to Rackham

One can transfer files to/from Rackham using the UPPMAX Transit server,
using SCP.
The program `scp` allows you to copy file between Rackham and Transit.

The process is:

1. Get inside SUNET

???- tip "Forgot how to get inside SUNET?"

    It is discussed [at the 'login to Bianca' page](login_bianca.md). 

2. Use the terminal to login to Rackham.

???- question "Forgot how to login to Rackham?"

    A step-by-step guide how to login to Rackham
    can be found [here](../getting_started/login_rackham.md).

    Spoiler: `ssh [username]@rackham.uppmax.uu.se`

3. In the terminal, run `scp` to copy files to Transit by doing:

```
scp [file_on_rackham] [username]@transit.uppmax.uu.se 
```

where `[file_on_rackham]` is the name of a file on Rackham
and `[username]` is your UPPMAX username, for example:

```
scp my_rackham_file.txt [username]@transit.uppmax.uu.se 
```

4. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

### Login to transit

One can transfer files to/from Rackham using the UPPMAX Transit server,
using SCP.
The program `scp` allows you to copy file between Rackham and Transit.

The process is:

1. Get inside SUNET

???- tip "Forgot how to get inside SUNET?"

    It is discussed [at the 'login to Bianca' page](login_bianca.md). 

2. Use the terminal to login to Transit.

???- question "Forgot how to login to Transit?"

    A step-by-step guide how to login to Transit
    can be found [here](transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

3. In the terminal, run `scp` to copy files to Rackham by doing:

```
scp [file_on_transit] [username]@rackham.uppmax.uu.se 
```

where `[file_on_transit]` is the name of a file on Transit
and `[username]` is your UPPMAX username, for example:

```
scp my_transit_file.txt [username]@rackham.uppmax.uu.se 
```

4. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

## Using SFTP

### Login to transit

One can transfer files to/from Rackham using the UPPMAX Transit server.
Transit is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Rackham using Transit.

The process is:

1. Get inside SUNET

???- tip "Forgot how to get inside SUNET?"

    It is discussed [at the 'login to Bianca' page](login_bianca.md). 

2. Use the terminal to login to Transit.

???- question "Forgot how to login to Transit?"

    A step-by-step guide how to login to Transit
    can be found [here](transit.md).

    Spoiler: `ssh [username]@transit.uppmax.uu.se`

3. In the terminal, run `sftp` to connect to Rackham by doing:

```
sftp [username]@rackham.uppmax.uu.se 
```

where `[username]` is your UPPMAX username, for example:

```
sftp sven@rackham.uppmax.uu.se 
```

4. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

5. In `sftp`, upload/download files to/from Rackham

Basic `sftp` command can be found [here](https://www.uppmax.uu.se/support/user-guides/basic-sftp-commands/).

### Login to Rackham

One can transfer files to/from Rackham using the UPPMAX Transit server.
Transit is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Rackham using Transit.

The process is:

1. Get inside SUNET

???- tip "Forgot how to get inside SUNET?"

    It is discussed [at the 'login to Bianca' page](login_bianca.md). 

2. Use the terminal to login to Rackham.

???- question "Forgot how to login to Rackham?"

    A step-by-step guide how to login to Transit
    can be found [here](../getting_started/login_rackham.md).

    Spoiler: `ssh [username]@rackham.uppmax.uu.se`

3. In the terminal, run `sftp` to connect to Transit by doing:

```
sftp [username]@transit.uppmax.uu.se 
```

where `[username]` is your UPPMAX username, for example:

```
sftp sven@transit.uppmax.uu.se 
```

4. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

5. In `sftp`, upload/download files to/from Transit

Basic `sftp` command can be found [here](https://www.uppmax.uu.se/support/user-guides/basic-sftp-commands/).

## Overview

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#fcf,color:#000,stroke:#f0f
    classDef calculation_node fill:#ccf,color:#000,stroke:#00f

    subgraph sub_inside[SUNET]
      direction LR
      user(User)
      subgraph sub_transit_env[Transit]
        transit_login(Transit login):::calculation_node
        files_on_transit(Files on transit):::file_node
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

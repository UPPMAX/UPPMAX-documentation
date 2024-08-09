# Data transfer to/from Rackham using SFTP

Data transfer to/from Rackham using SFTP
is one of the ways ways to transfer files to/from Rackham

???- question "What are the other ways?"

    Other ways to transfer data to/from Rackham are described [here](../cluster_guides/transfer_rackham.md)

One can transfer files to/from Rackham using SFTP.
SFTP is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Rackham using SFTP.

The process is described here:

## Step 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer.

## Step 2. Run `sftp` to connect to Rackham

In the terminal, run `sftp` to connect to Rackham by doing:

```bash
sftp [username]@rackham.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
sftp sven@rackham.uppmax.uu.se
```

### Step 3. If asked, give your UPPMAX password

If asked, give your UPPMAX password.
You can get rid of this prompt if you have setup SSH keys

### Step 4. Upload/download files to/from Rackham

In `sftp`, upload/download files to/from Rackham.

Basic `sftp` command can be found [here](../software/sftp.md).

```mermaid
flowchart TD

    %% Give a white background to all nodes, instead of a transparent one
    classDef node fill:#fff,color:#000,stroke:#000

    %% Graph nodes for files and calculations
    classDef file_node fill:#fcf,color:#000,stroke:#f0f
    classDef calculation_node fill:#ccf,color:#000,stroke:#00f

    user(User)
      user_local_files(Files on user computer):::file_node

    subgraph sub_inside[SUNET]
      subgraph sub_rackham_shared_env[Rackham]
          login_node(login/calculation/interactive node):::calculation_node
          files_in_rackham_home(Files in Rackham home folder):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#fcc,color:#000,stroke:#fcc
    style sub_rackham_shared_env fill:#ffc,color:#000,stroke:#ffc

    user --> |logs in |login_node
    user --> |uses| user_local_files

    login_node --> |can use|files_in_rackham_home
    %% user_local_files <--> |graphical tool|files_in_rackham_home
    %% user_local_files <--> |SCP|files_in_rackham_home
    user_local_files <==> |SFTP|files_in_rackham_home

    %% Aligns nodes prettier
    user_local_files ~~~ login_node
```

> Overview of file transfer on Rackham
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.

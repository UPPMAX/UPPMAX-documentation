# Data transfer to/from Rackham using SCP

Data transfer to/from Rackham using SCP
is one of the ways ways to transfer files to/from Rackham

???- question "What are the other ways?"

    Other ways to transfer data to/from Rackham are described [here](../cluster_guides/transfer_rackham.md)

One can transfer files to/from Rackham using SCP.
SCP is an abbreviation of 'Secure copy protocol',
however, it is not considered 'secure' anymore:
instead it is considered an outdated protocol.
The program `scp` allows you to transfer files to/from Rackham using SCP,
by coping them between your local computer and Rackham.

The process is:

## Step 1. Start a terminal on your local computer

Start a terminal on your local computer

## Step 2. Copy files using `scp`

In the terminal, copy files using `scp` to connect to Rackham:

```bash
scp [from] [to]
```

Where `[from]` is the file(s) you want to copy, and `[to]` is the destination.
This is quite a shorthand notation!

This is how you copy a file from your local computer to Rackham:

```bash
scp [local_filename] [username]@rackham.uppmax.uu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your UPPMAX username, for example:

```bash
scp my_file.txt sven@rackham.uppmax.uu.se:/home/sven
```

To copy a file from Rackham to your local computer, do the command above in reverse order:

```bash
scp [username]@rackham.uppmax.uu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your UPPMAX username,
and `[local_folder]` is your local folder, for example:

```bash
scp sven@rackham.uppmax.uu.se:/home/sven/my_remote_file.txt /home/sven
```

## Step 3. If asked, give your UPPMAX password

If asked, give your UPPMAX password.
You can get rid of this prompt if you have setup SSH keys


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
    user_local_files <==> |SCP|files_in_rackham_home
    %% user_local_files <--> |SFTP|files_in_rackham_home

    %% Aligns nodes prettier
    user_local_files ~~~ login_node
```

> Overview of file transfer on Rackham
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.


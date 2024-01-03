# Data transfer to/from Transit using SCP

Data transfer to/from Transit using SCP
is one of the ways ways to transfer files to/from Transit

???- question "What are the other ways?"

    Other ways to transfer data to/from Transit are described [here](transfer_transit.md)

One can transfer files to/from Transit using SCP.
SCP is an abbreviation of 'Secure copy protocol',
however, it is not considered 'secure' anymore:
instead it is considered an outdated protocol.
The program `scp` allows you to transfer files to/from Transit using SCP,
by coping them between your local computer and Transit.

The process is:

1. Start a terminal on your local computer
2. In the terminal, copy files using `scp` to connect to Transit:

```
scp [from] [to]
```

Where `[from]` is the file(s) you want to copy, and `[to]` is the destination.
This is quite a shorthand notation!

This is how you copy a file from your local computer to Transit:

```
scp [local_filename] [username]@transit.uppmax.uu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your UPPMAX username, for example:

```
scp my_file.txt sven@transit.uppmax.uu.se:/home/sven
```

To copy a file from Transit to your local computer, do the command above in reverse order:

```
scp [username]@transit.uppmax.uu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your UPPMAX username, 
and `[local_folder]` is your local folder, for example:

```
scp sven@transit.uppmax.uu.se:/home/sven/my_remote_file.txt /home/sven
```

3. If asked, give your UPPMAX password. 
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
      subgraph sub_transit_shared_env[Transit]
          login_node(login/calculation/interactive node):::calculation_node
          files_in_transit_home(Files in Transit home folder):::file_node
      end
    end

    %% Shared subgraph color scheme
    %% style sub_outside fill:#ccc,color:#000,stroke:#ccc
    style sub_inside fill:#fcc,color:#000,stroke:#fcc
    style sub_transit_shared_env fill:#ffc,color:#000,stroke:#ffc

    user --> |logs in |login_node
    user --> |uses| user_local_files

    login_node --> |can use|files_in_transit_home
    %% user_local_files <--> |graphical tool|files_in_transit_home
    user_local_files <==> |SCP|files_in_transit_home
    %% user_local_files <--> |SFTP|files_in_transit_home

    %% Aligns nodes prettier
    user_local_files ~~~ login_node
```

> Overview of file transfer on Transit
> The purple nodes are about file transfer,
> the blue nodes are about 'doing other things'.
> The user can be either inside or outside SUNET.


## Failure log

```
richel@richel-N141CU:~$ scp demo.txt richel@transit.uppmax.uu.se:/home/richel
demo.txt                                  100%   53     8.8KB/s   00:00    
richel@richel-N141CU:~$ ssh richel@transit.uppmax.uu.se
Last login: Wed Jan  3 12:41:33 2024 from vpnpool188-187.anst.uu.se

Transit server

You can mount bianca wharf with the command

mount_wharf PROJECT [path]

If you do not give a path the mount will show up as PROJECT in your home
directory.

Note; any chagnes you do to your normal home directory will not persist.


[richel@transit ~]$ ls
Documents                    project_number.txt
environment.yml              q.sh
fake.csv                     qsp.sh
genpipes                     qs.sh
GitHubs                      R
glob                         requirements.txt
iamonrackham                 send_to_bianca_sens2021565.sh
login_bianca_sens2017625.sh  staff
mapAD                        start_interactive.sh
mi.license                   to_bianca.sh
private                      uppmax2023-2-25
[richel@transit ~]$ 
```

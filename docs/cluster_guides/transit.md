# `transit`

`transit` is an UPPMAX server that can be used to securely transfer files.

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

## Login to `transit`

Below is a step-by-step procedure to login to `transit`.

### 1. Get within SUNET

???- tip "Forgot how to get within SUNET?"

    See [the 'Logging in to Bianca' page](../getting_started/login_bianca.md).

### 2. Use SSH to login

On your local computer, start a terminal and use `ssh` to login to `transit`: 

```
ssh [username]@transit.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```
ssh sven@transit.uppmax.uu.se
```

If you haven't setup using SSH keys, you will be asked for your UPPMAX password.



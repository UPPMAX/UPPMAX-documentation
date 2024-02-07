# File transfer to/from Dardel

![Dardel server racks](./img/dardel_racks.png)

This page describes how to transfer files to Dardel,
the HPC cluster at PDC in Stockholm.

## Why do I need this?

The Rackham cluster will be decommissioned at the end of 2024 
so all projects have to migrate their data and calculations to other resources. 
The plan from NAISS is that all Rackham users will move to 
the Dardel cluster at PDC.

## How do I do this?

First, we are here to help.
Please [contact support](../support.md) if you run into problems
when trying the guide below.

To transfer your files to Dardel, follow the steps below.

```mermaid
flowchart TD
  get_supr_project[1. Access to a SUPR project with Dardel]
  get_pdc_account[2. Access to a PDC account]
  create_ssh_key[3. Create SSH key pair on Rackham]
  download_ssh_keys[4. Download public SSH key]
  upload_ssh_key[5. Upload public SSH key to Dardel]
  transfer_files[6. Tranfer files to Dardel]
  
  get_pdc_account --> |requires| get_supr_project 
  download_ssh_keys --> |requires| create_ssh_key
  upload_ssh_key --> |requires| download_ssh_keys
  upload_ssh_key --> |requires| get_pdc_account
  transfer_files --> |requires| upload_ssh_key
```

### 1. Get access to a SUPR project with Dardel

First step is to get get access to a SUPR project with Dardel.
This is described at [PDC's page on getting access to Dardel](https://www.pdc.kth.se/support/documents/getting_access/get_access.html).
You will get an email when you are added to a project,
this can take some hours.

???- question "How do I know I have access to a Dardel project?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    If there is a PDC project,
    you may have access to a project with Dardel.

    ![](./img/supr_naiss_dardel_project.png)

    > Example user that has access to a PDC project

    If you may a PDC project that does not use Dardel,
    click on the project to go the the project overview.

    ![](./img/supr_naiss_dardel_project_overview.png)

    > Example PDC project overview

    From there, scroll down to 'Resources'.
    If you see 'Dardel' among the compute resources, 
    you have confirmed you have access to a Dardel project.

    ![](./img/naiss_project_dardel_resources.png)

    > Resources from an example PDC project

### 2. Get a PDC account via SUPR

Get a PDC account via SUPR.
This is described at [the PDC page on getting access](https://www.pdc.kth.se/support/documents/getting_access/get_access.html#supr-account).
You will get a PDC account overnight.

???- question "How do I know I have a PDC account?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    and click on 'Accounts' in the main menu bar at the left.

    If you see 'Dardel' among the resources, and status 'Enabled'
    in the same row, you have a PDC account!

    ![](./img/supr_naiss_dardel_account.png)

    > Example of a user having an account at PDC's Dardel HPC cluster

### 3. Create an SSH key pair

How to create an SSH key pair is
described  at [the PDC page on how to create an SSH key pair](https://www.pdc.kth.se/support/documents/login/ssh_login.html#how-to-create-ssh-key-pairs).

On way to do so, is to use the UPPMAX tool `dardel_ssh-keygen`.

On Rackham, do:

```
$ export PATH=$PATH:/proj/staff/dahlo/testarea/darsync
$ dardel_ssh-keygen
SSH key created successfully.
```

and you have created a SSH key pair.

???- question "How do I know this worked?"

    On Rackham, in a terminal, type:

    ```
    $ cat ~/.ssh/id-ed25519-pdc
    ```

    This will show a text similar to:

    ```
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    QyNTUxOQAAACBDgv7syuRoZ0G4hv3fgg7azq/oiAKdRKen2oipM6s+4AAAAKBo5xJaaOcS
    WgAAAAtzc2gtZWQyNTUxOQAAACBDgv7syuRoZ0G4hv3fgg7azq/oiAKdRKe42oipM6s+4A
    ABAEDIq45Rv4Vg8YuKozcWIJexp6jq+zHIxg1r0u69e3VPF0OC/uzK5GhnQbiG/d+CDtrO
    r+iIAp1Ep6faiKkzqz7gAAAAHHJpY2hlbEByYWNraGFtMi51cHBtYXgudXUuc2UB
    -----END OPENSSH PRIVATE KEY-----
    ```

    Note that this is your **private** key. Do not distribute it!

### 4. Download the public SSH key to your local computer

Download the public SSH key in file `~/.ssh/id-ed25519-pdc.pub`
to your local computer.
Transferring files to/from Rackham is documented [here](tranfer_rackham.md).

???- question "How does that look like?"

    ![](./img/rackham_download_dardel_ssh_public_key.png)

    Here the public SSH key is downloaded using FileZilla.

### 5. Upload the public SSH key to Dardel

How to upload the SSH public key is described
in [the PDC documentation on how to log in with SSH keys](https://www.pdc.kth.se/support/documents/login/ssh_login.html).

???- question "How does the upload look like?"

    ![](./img/pdc_prove_identity.png)

    > Click on 'Prove Indentity'

    ![](./img/pdc_key_management_no_keys.png)

    > PDC key managements before any keys are added.

After having uploaded your public SSH key, you will be able to see your registered keys.

???- question "How does that look like?"

    ![](pdc_key_management_rackham_key.png)

    > Here we see that there is an SSH key uploaded.

### 6. Transfer files

To facilitate this move we have created Darsync, 
a tool that can inspect your files and make suggestions 
to make the transfer easier, 
as well as generating a script file you can submit to [SLURM](slurm.md) 
to perform the actual file transfer. 
[Read more about how to use Darsync here](../cluster_guides/darsync.md).

### 6. Delete the SSH key pair


## Link

 * [PDC's page on getting access to Dardel](https://www.pdc.kth.se/support/documents/getting_access/get_access.html)

 * [PDC's page on login to Dardel](https://www.pdc.kth.se/support/documents/login/dardel.html)



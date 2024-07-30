# Dardel migration

![Dardel server racks](./img/dardel_racks.png)

This page describes how to transfer files to Dardel,
the HPC cluster at PDC in Stockholm.

???- info "Visit the Rackham 2 Dardel Drop-in"

    Every Tuesday at 11:15 (except for the month of July)
    there is online Rackham 2 Dardel Drop-in at Zoom
    with meeting ID 64896912764

Please join us if you need assistance logging in to Dardel or migrating your data.

???- question "Why do I need this?"

    The Rackham cluster will be decommissioned at the end of 2024,
    hence all project directories will be deleted.
    The plan from NAISS is that all Rackham users can move to the Dardel cluster at PDC,
    and we encourage you to do so right away.

    Researchers at Uppsala University, should they so desire,
    can choose to keep data at UPPMAX.
    Projects with UU affiliation that remain on Rackham
    at the end of this year can be transferred to a new local system.

    To facilitate this move,
    we have created a tool that makes the transfer easier.

    [More details of Rackham end of life here](https://www.uu.se/centrum/uppmax/nyheter/nyheter/2024-02-16-rackham-end-of-life).

## Short version

The really short description is:

1. Become a member of a project with resources at Dardel in [SUPR](https://supr.naiss.se/).
1. Create a [passwordless SSH key](#3-create-ssh-key-pair).
1. Add the key to the [PDC login portal](https://loginportal.pdc.kth.se/).
1. Add `*.uppmax.uu.se` as allowed address for the key.
1. Load module `darsync` and run `darsync check` on the folder you want to transfer.
1. Create a Slurm script using `darsync gen` on the folder you want to transfer.
1. Submit the created Slurm script.

See the rest of this guide for more information about these steps.


## Long version

???- question "Prefer a video?"

    This procedure is also shown in [this YouTube video](https://youtu.be/rivtgTnulNA).

First, we are here to help.
Please [contact support](../support.md) if you run into problems
when trying the guide below.

This migration consists of a couple of steps summarized below.
Press the links to get more detailed explanation of each step.
Note that step 1 requires some hours of waiting
and step 2 requires an overnight wait.

```mermaid
flowchart TD
  get_supr_project[1. Access to a SUPR project with Dardel]
  get_pdc_account[2. Access to a PDC account]
  create_ssh_key[3. Create temporary SSH keys]
  add_ssh_key[4. Add the SSH keys to the PDC Login Portal]
  run_darsync[5. Run Darsync]
  slurm[6. Submit the script created by Darsync]
  check_logs[7. Check logs]
  delete_ssh_keys[8. Delete the temporary SSH keys]

  get_supr_project --> |needed for| get_pdc_account

  create_ssh_key --> |needed for| add_ssh_key
  get_pdc_account --> |needed for| add_ssh_key
  add_ssh_key --> |needed for| run_darsync
  run_darsync --> |needed for| slurm
  slurm --> |needed for| check_logs
  check_logs --> |needed for| delete_ssh_keys
```

> Overview of the migration process.
> Note that step 1 requires some hours of waiting
> and step 2 requires an overnight wait.

After those steps, the procedure will take around 20 minutes,
as shown in [the YouTube video that shows this procedure](https://youtu.be/rivtgTnulNA).

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
This is described at [the PDC page on how to apply for a SUPR account](https://www.pdc.kth.se/support/documents/getting_access/get_access.html#apply-via-a-supr-account).
You will get a PDC account overnight.

???- question "How do I know I have a PDC account?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    and click on 'Accounts' in the main menu bar at the left.

    If you see 'Dardel' among the resources, and status 'Enabled'
    in the same row, you have a PDC account!

    ![](./img/supr_naiss_dardel_account.png)

    > Example of a user having an account at PDC's Dardel HPC cluster

### 3. Create SSH key pair

First we will create SSH keys to be able to connect to Dardel. We have made a small tool to create the keys for Darsync for you, so just run these commands on UPPMAX:

```bash
module load darsync
darsync sshkey
```

### 4. Add the public key to the PDC Login Portal

See [create and use an SSH key pair for Dardel, step 2](http://docs.uppmax.uu.se/software/ssh_key_use_dardel/#2-how-to-add-an-ssh-key-to-the-pdc-login-portal),
to see how to upload the public SSH key to the PDC Login Portal.

### 5. Run the migration tool Darsync

#### 5.1 Load the module

```bash
module load darsync
```

#### 5.2 Check for problems

This step is optional, yet may help against possible problems.

Running `darsync check` will make Darsync prompt for questions:


```bash
darsync check
```

???- question "Can I also give the arguments on the command line?"

    If you prefer to specify everything from the command-line, do:

    ```bash
    darsync check --local-dir [foldername]
    ```

    where `[foldername]` is the name to a folder,
    for example `darsync check --local-dir ~/my_folder`.

    There are some more optional arguments, see these by doing:

    ```bash
    darsync check --help
    ```

If there are problems reported, [contact support](../support.md)
or try to fix them yourself.

???- question "What is the file `darsync_[dirname].ownership.gz`?"

    This is a file containing file ownership information. It is created in
    the root of the folder you told Darsync to transfer to Dardel.

    When a user transfer all the files in a project to a project at Dardel,
    all the files at Dardel will be owned by the user who did the transfer.
    By saving the ownership information of the files at UPPMAX,
    we can map the file ownership information to the corresponding users at Dardel.

???- question "Can I delete the file `darsync_[dirname].ownership.gz`?"

    No, keep it until you feel at home at Dardel and have worked in your
    new project a couple of months. By that time you should have encountered
    any problems with file permissions that you might have.

    If you discover that you get problems because of wrong owner of files
    (write permissions etc), this file contains the information needed to
    recreate the file ownerships as they were before you transfered the files,
    even if your UPPMAX project has already been deleted.

???- question "How to fix `WARNING: files with uncompressed file extensions above the threshold detected`"
    It looks for files with file endings matching common uncompressed file formats, like `.fq`, `.sam`, `.vcf`, `.txt`. If the combined file size of these files are above a threshold it will trigger the warning. Most programs that uses these formats can also read the compressed version of them.

    Examples of how to compress common formats:

    ```bash
    # fastq/fq/fasta/txt
    gzip file.fq

    # vcf
    bgzip file.vcf

    # sam
    samtools view -b file.sam > file.bam
    # when the above command is completed successfully:
    # rm file.sam
    ```

    For examples on how to compress other file formats, use an internet search engine to look for
    ```
    how to compress <insert file format name> file

???- question "How to fix `WARNING: Total number of files, or number of files in a single directory`"

    If a project consists of many small files it will decrease the data transfer speed, as there is an overhead cost to starting and stopping each file transfer. A way around this is to pack all the small files into a single `tar` archive, so that it only has to start and stop a single time.

    Example of how to pack a folder and all files in it into a single `tar` archive.

    ```bash
    ### on uppmax

    # pack it
    tar -czvf folder.tar.gz /path/to/folder

    # the the command above finished without error messages and you have a folder.tar.gz file that seems about right in size,
    rm -r /path/to/folder


#### 5.3 Generate script

In this third step, the [Slurm](slurm.md) script is created.

!!! info "A lot of questions"

    The script will ask multiple questions.
    Below it is described how to get the answers :-)

Running `darsync gen` will make Darsync prompt for questions:


```bash
darsync gen
```

After answering all the questions a new file will be created. By default it will
be created in your home directory, named `darsync_foldername.sh`,
where `foldername` is the name of the folder you told it to transfer,
e.g. `~/darsync_nais2024-23-9999.sh`

In case of a typo, you can also modify the transfer script created by Darsync,
which is a regular [Slurm](slurm.md) script.

???- question "Can I also give the arguments on the command line?"

    If you prefer to specify everything from the command-line, do:

    ```bash
    darsync gen \
      --local-dir [foldername on UPPMAX] \
      --remote-dir [foldername on Dardel] \
      --slurm-account [slurm_account] \
      --cluster [slurm_cluster] \
      --username [pdc_username] \
      --ssh-key [private_ssh_key_path] \
      --outfile [output_filename]
    ```

    where

    - `[foldername]` is the name to a folder, e.g. `~/my_folder`
    - `[slurm_account]` is the UPPMAX project ID, e.g. `uppmax2023-2-25`
    - `[slurm_cluster]` is the cluster on UPPMAX where the job will run, e.g. `rackham` or `snowy`
    - `[pdc_username]` is your PDC username, e.g `svenan`
    - `[private_ssh_key_path]` is the path the private SSH key, e.g. `~/id_ed25519_pdc`
    - `[output_filename]` is the name of the Slurm output file, e.g. `~/dardel_naiss2024-23-9999.sh`

    resulting in:

    ```bash
    darsync gen \
      --local-dir ~/my_folder \
      --remote-dir /cfs/klemming/projects/nais2024-23-9999
      --slurm-account uppmax2023-2-25 \
      --username svenan \
      --ssh-key ~/id_ed25519_pdc \
      --outfile ~/dardel_naiss2024-23-9999.sh
    ```

    There are some more optional arguments, see these by doing:

    ```bash
    darsync gen --help
    ```

???- question "How to find out my UPPMAX project ID?"

    The UPPMAX project ID is used in your [Slurm](slurm.md) scripts,
    with the `-A` flag.

    Your UPPMAX project IDs can be found at [https://supr.naiss.se/](https://supr.naiss.se/).
    UPPMAX projects for Rackham usually start with `NAISS` or `UPPMAX`
    and have '(UPPMAX)' after the project name.

    Here is how to convert the UPPMAX project name to UPPMAX project ID:

    UPPMAX project name|UPPMAX project ID
    -------------------|-----------------
    NAISS 2024/22-49   |`naiss2024-22-49`
    UPPMAX 2023/2-25   |`uppmax2023-2-25`

    ![](supr_naiss_example_projects.png)

    > Example [https://supr.naiss.se/](https://supr.naiss.se/) page.
    > Eligible candidates seem 'NAISS 2024/22-49' and 'UPPMAX 2023/2-25'.

???- question "How to find out my PDC username?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    and click on 'Accounts' in the main menu bar at the left.

    If you see 'Dardel' among the resources, and status 'Enabled'
    in the same row, you have a PDC account.
    In the first column of such a row, you will see your username

    ![](./img/supr_naiss_dardel_account.png)

    > Example of a user having an account at PDC's Dardel HPC cluster.
    > In this case, the username is `richelbi`

???- question "How to find out where on Dardel I will transfer your data to?"

    * Your home folder: `/cfs/klemming/home/r/[username]`,
      where `[username]` is your PDC username,
      for example `/cfs/klemming/home/r/sven`
    * Your project folder: `/cfs/klemming/projects/[project_storage]`,
      where `[project_storage]` is your PDC project storage folder,
      for example `/cfs/klemming/projects/snic/naiss2023-22-1027`

    ![](./img/supr_naiss_dardel_storage.png)

    > Composite image of a PDC project and its associated storage folder
    > at the bottom.
    > In this case, the full folder name is `/cfs/klemming/projects/snic/naiss2023-22-10271`

### 6. Submit the script created by Darsync

You submit the transfer script the same way you submit any jobs at UPPMAX:
Replace `nais2024-23-9999` with the name of the folder you told Darsync to transfer.

```bash
sbatch ~/dardel_naiss2024-23-9999.sh
```

???- question "I get an error 'sbatch: error: Batch job submission failed'. What do I do?"

    It means that the script created for you has a mistake.

    See [Slurm troubleshooting](slurm_troubleshooting.md) for guidance
    on how to troubleshoot this.

### 7. Check logs

Once the submitted job has finished, have a look at the log file produced by the job and make sure it did not end in a error message.
Replace `nais2024-23-9999` with the name of the folder you told Darsync to transfer.

```bash
tail ~/dardel_naiss2024-23-9999.out
tail ~/dardel_naiss2024-23-9999.err
```

### 8. Delete the SSH key

After the migration, these temporary SSH keys can and should be deleted:

```bash
rm ~/id_ed25519_pdc*
```

## Troubleshooting

### `ssh: connect to host dardel.pdc.kth.se port 22: No route to host`

Full error message:

```text
[richel@rackham1 ~]$ bash /domus/h1/richel/dardel_transfer_script.sh
ssh: connect to host dardel.pdc.kth.se port 22: No route to host
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at io.c(226) [sender=3.1.2]
```

Likely cause:

This probably means that Dardel is down, likely due to maintenance.

Solution:

You can do nothing, except wait until Dardel is up again.

You may check the PDC news at
[https://www.pdc.kth.se/about/pdc-news](https://www.pdc.kth.se/about/pdc-news)
to confirm that there is indeed a problem with Dardel.

### `rsync: [generator] failed to set times on "/cfs/klemming/projects/snic/naiss2024-23-352/.": Operation not permitted (1)`

Full error message:

```bash
$ bash darsync_my_folder.slurm
sending incremental file list
rsync: [generator] failed to set times on "/cfs/klemming/projects/snic/naiss2024-23-352/.": Operation not permitted (1)
```

after which the script keeps running.

???- question "For UPPMAX staff"

    An example can be found at [https://github.com/UPPMAX/ticket_296149](https://github.com/UPPMAX/ticket_296149).

Hypothesized cause:

This darsync script is running for the second (or more) time,
hence it has already created the target folders on Dardel.
This hypothesis is backed by [this Stack Overflow post](https://stackoverflow.com/a/54861420)
where it is suggested to delete the folders; in this case: the target folders on Dardel.

Solution:

On Dardel, delete the target folders that are already there
and re-run the script.

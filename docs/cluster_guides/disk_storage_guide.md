# Disk storage guide

## Quota

Users have access to shared network storage on various cluster file systems.
This mean that whenever you are logged in to a login server
or if you are running on a compute node you will have the same view of the storage.

There are several different classes of disk storage available with different policies for usage, limits and backup:

- The user home file system
- Local scratch file systems
- The network project and nobackup file system
- Temporary virtual filesystem

Users have access to shared network storage on various cluster file systems,
and backup home directories and some project storages to tape.

## How much of my quota do I use?

Use [uquota](../software/uquota.md)to check current disk usage and limits.

???- question "How does that look like?"

    Your output will look similar to this:

    ```bash
    [sven@rackham3 ~]$ uquota
    Your project       Your File Area           Unit        Usage  Quota Limit  Over Quota
    -----------------  -----------------------  -------  --------  -----------  ----------
    home               /home/richel             GiB          16.6           32            
    home               /home/richel             files      104165       300000            
    naiss2024-22-1202  /proj/r-py-jl-m-rackham  GiB           0.0          128            
    naiss2024-22-1202  /proj/r-py-jl-m-rackham  files           4       100000            
    naiss2024-22-49    /proj/introtouppmax      GiB           5.1          128            
    naiss2024-22-49    /proj/introtouppmax      files       20290       100000            
    staff              /proj/staff              GiB       66064.8       102400            
    staff              /proj/staff              files    21325500     15000000           *
    ```

## I use more quota than I think. How do I find out the cause?

To find out which folder uses most storage,
run the following command to find the 20 folders that take up most storage
space:


```bash
du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}' | head -n 20
```

???- question "How does that look like?"

    Your output looks similar to this:

    ```bash
    [sven@rackham3 ~]$ du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}' | head -n 20
    100% 17643266006 /home/sven
    50% 8984271436 /home/sven/.cache
    45% 8016778981 /home/sven/.cache/pip
    39% 6988369390 /home/sven/.cache/pip/http
    28% 4986824453 /home/sven/.local
    28% 4986117855 /home/sven/.local/lib
    27% 4816372185 /home/sven/.local/lib/python3.8
    27% 4816368089 /home/sven/.local/lib/python3.8/site-packages
    15% 2797022871 /home/sven/.local/lib/python3.8/site-packages/nvidia
    10% 1876238645 /home/sven/.cache/pip/http/3
    9% 1648194862 /home/sven/.local/lib/python3.8/site-packages/torch
    9% 1589833684 /home/sven/users
    8% 1569946463 /home/sven/users/fares
    8% 1553069908 /home/sven/.local/lib/python3.8/site-packages/torch/lib
    8% 1431151816 /home/sven/.cache/pip/http/0
    7% 1411093224 /home/sven/.cache/pip/http/3/c
    5% 1023338615 /home/sven/.local/lib/python3.8/site-packages/nvidia/cudnn
    5% 1022966263 /home/sven/.local/lib/python3.8/site-packages/nvidia/cudnn/lib
    5% 983932032 /home/sven/.cache/pip/http-v2
    5% 983390581 /home/sven/.cache/pip/http/9
    ```


To find out which files uses most storage,
run the following command to find the 20 files that take up most storage
space:

```bash
find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn
```

???- question "How does that look like?"

    Your output looks similar to this:

    ```bash
    [sven@rackham3 ~]$ find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn | head -n 20
    1546936200 /home/sven/users/anna/H10_Avian_1650_2000_HA_alignment.trees
    902414441 /home/sven/.local/lib/python3.8/site-packages/torch/lib/libtorch_cuda.so
    797076603 /home/sven/.cache/pip/http/0/c/d/a/3/0cda36001dc173401b525a7e434e8b7f1079d34f31141b688325244b
    755535721 /home/sven/.cache/pip/http/9/b/8/7/5/9b875d1148ce95ad551df724a540378d1dc8158fa59145beb2ec4125
    731727087 /home/sven/.cache/pip/http/3/c/e/f/9/3cef90e2f33f3b9a1b50e02cc0736e09cc97714cb8b1101d706d912d
    664753951 /home/sven/.cache/pip/http/3/c/8/2/7/3c827aae7500e30cec6930647f8971adb3eafb1cd65a44fcf02ba940
    589831274 /home/sven/.cache/pip/http-v2/9/4/c/e/7/94ce755eb45386ac0cd2115e71a8162388f908eac28abff6118b7e7a.body
    569645536 /home/sven/.local/lib/python3.8/site-packages/nvidia/cudnn/lib/libcudnn_engines_precompiled.so.9
    515090264 /home/sven/.local/lib/python3.8/site-packages/nvidia/cublas/lib/libcublasLt.so.12
    497648053 /home/sven/.cache/pip/http/0/e/3/7/9/0e379b2d265d90194ab62c0f7704318e349017777b755c72c955e025
    497624428 /home/sven/.cache/pip/http/4/b/7/9/b/4b79bbc6cc88163d2cba55b1492741f457013fc2c14b26bdd398a0a3
    495148366 /home/sven/.cache/pip/http/e/7/c/6/1/e7c618a0177b1a48a4599a6785fda5ffd4946442a77e875b970fdfee
    492151297 /home/sven/.local/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
    468354983 /home/sven/.cache/huggingface/hub/models--zhihan1996--DNABERT-2-117M/blobs/7ff39ec77a484dd01070a41bfd6e95cdd7247bec80fe357ab43a4be33687aeba
    410595986 /home/sven/.cache/pip/http/3/9/a/e/6/39ae6aa825aebb75b0193714975cbc9defffa90203c5342f2214137e
    264876688 /home/sven/.local/lib/python3.8/site-packages/nvidia/cusparse/lib/libcusparse.so.12
    240706416 /home/sven/.local/lib/python3.8/site-packages/nvidia/cudnn/lib/libcudnn_adv.so.9
    232685936 /home/sven/.local/lib/python3.8/site-packages/nvidia/nccl/lib/libnccl.so.2
    209353474 /home/sven/.cache/pip/http/d/4/c/3/e/d4c3ec899ac2836a7f89ffad88e243bf35b92f56ff0b61ad0f5badf5
    195959494 /home/sven/.cache/pip/http/6/e/f/7/a/6ef7ae373253a3997ffc8ac7b70e67716f79d6365ffa5c28f40f349a
    ```

### If you need more quota

If more quota is needed, [contact support](../support.md) for advice.
We do not extend quotas for home directories or SNIC project directories,
but it's possible to apply for storage projects.

Before contacting support, clean out unnecessary data and make an inventory of
the data in your project (what type of data, how big, why it's needed).
Here are two commands:

```bash
du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}'
```

This first command results in a list of subdirectories ordered
by size and proportion of total size.


```bash
find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn
```

This second command produces a list of the files in the current directory
that take up most space. These may take a long time to complete, use `CTRL + C`
to cancel execution if you change your mind.

### If you need even more quota for archiving

Please [contact support](../support.md).

We have a previously been able to provide users with a low-cost
moderate performant storage solution for a cost of 500SEK/TB/year,
for a commitment of four years and 50TB.

### Environmental variables

We have defines several environment variables to help our users. They are:

- `$HOME` (or `$SNIC_BACKUP`) is a traditional one, pointing to the users home directory.
- `$TMPDIR` or (`$SNIC_TMP`) points to node-local storage, suitable for temporary files that can be deleted when the job finishes
- `$SNIC_NOBACKUP` points to an UPPMAX-wide storage suitable for temporary files (not deleted when the job is finished)

## Types of storage

### User Home directories

Paths: $HOME or $SNIC_BACKUP

Permanent storage of users files during the lifetime of the accounts. Shared access on all cluster nodes. Snapshots are normally enabled on this file system, and you can access the snapshots in every directory by 'ls .snapshot' or 'cd .snapshot'. The quota is 32GB per user. We provide backup of this volume, and we keep the files on tape up to 90 days after they are deleted from disk. If you have files you do not want to back up place them in a folder called 'nobackup'.

We recommend you do not use your home directory for running jobs. Our general recommendation is to keep everything related to a specific research project in its project directory.

### Local Scratch

Paths: `$TMPDIR` or `$SNIC_TMP`

Each node has a `/scratch` volume for local access providing the most efficient disk storage for temporary files. Users have read/write access to this file system. SLURM defines the environment variable TMPDIR which you may use in job scripts. On clusters with SLURM you may use /scratch/$SLURM_JOB_ID. This area is for local access only, and is not directly reachable from other nodes or from the front node. There is no backup of the data and the lifetime of any file created is limited to the current user session or batch job. Files are automatically erased when space is needed by other users.

### Projects global (network) storage

Paths: /proj/[proj-id]

The project global storage is permanent storage of project's files during the lifetime of the project. Disk quota on this volume is shared by all project members. Default quota allocation is determined by your project type.

Note that the quota system on crex is built on group ownership for files/directories. This means that moving files between project directories does not directly affect quota. We have scripts and other tricks that tries to ensure the correct group is always used, but  in general this may lag quite some time - it takes a while to go through everything, especially since we don't want to affect performance. To make sure quota information is correct, you can change the group to the correct one after moving directories:

chgrp -R PROJECT_YOU_MOVED_TO PATH_OF_THE_MOVED_DIRECTORY

if you don't do this, it will still be fixed, but it may take a while.

The files are backed up to tape and we keep the files for 30 days after they are deleted from disk. In the project folder you should keep all your raw data and important scripts.

On Bianca and in SLLStore and UppStore projects, all temporary files, and files that can be regenerated (e.g.. data created from your computations), should be moved to the nobackup folder.

More information about backup at UPPMAX.

### Temporary virtual filesystem

Paths: `/dev/shm/[job-id]`

On all our clusters we have a temporary virtual filesystem implemented as a shared memory area. I.e. it uses primarily the RAM for storage (until it eventually might have to swap out to physical disk), and can be accessed via the path /dev/shm/[job-id].

In some situations this "disk" area can be quicker to read/write to, but depending on the circumstances it can also be slower than local scratch disk. Also note that it is a shared resource among all running jobs on a specific node, so depending on the node and how much memory your job has been allocated, the amount of data you can write will vary.

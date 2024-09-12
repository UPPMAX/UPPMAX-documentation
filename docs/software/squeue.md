---
tags:
  - squeue
---

# `squeue`

The [job scheduler](../cluster_guides/slurm.md) consists of many
programs to manage jobs.
`squeue` is a tool to view information about the job queues.

## View all jobs 

### View all jobs in the Bianca or Rackham queue
 
View all jobs in the [Bianca](../cluster_guides/bianca.md) or [Rackham](../cluster_guides/rackham.md) queue:

```bash
squeue
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [sven@rackham1 ~]$ squeue | head -n 1; squeue | shuf | head
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
              49086999      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086465      core sbatch_l matca755 PD       0:00      1 (Priority)
              49085829      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086067      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086600      core sbatch_l matca755 PD       0:00      1 (Priority)
              49087075      core sbatch_l matca755 PD       0:00      1 (Priority)
              49080199      node /proj/sn torsteng PD       0:00      1 (Priority)
              49088741      core sbatch_l matca755 PD       0:00      1 (Priority)
              49086825      core sbatch_l matca755 PD       0:00      1 (Priority)
              49087385      core sbatch_l matca755 PD       0:00      1 (Priority)
    ```

### View all jobs in Snowy queue

View all jobs in the [Snowy](../cluster_guides/snowy.md) queue:

```bash
squeue -M snowy
```

???- question "How does that look like?"

    Your output will be similar to this:

    ```bash
    [sven@rackham1 ~]$ squeue -M snowy
    CLUSTER: snowy
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               9642748      core blast2un qiuzh610 PD       0:00      1 (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions)
               9642749      core blast2un qiuzh610 PD       0:00      1 (Priority)
               9642750      core blast2un qiuzh610 PD       0:00      1 (Priority)
               9642751      core blast2un qiuzh610 PD       0:00      1 (Priority)
               9640955      core interact    teitu  R 1-00:09:18      1 s201
               9642778      core snakejob yildirim  R       9:18      1 s25
               9641765      core Ridge_al yildirim  R   17:28:32      1 s201
               9642747      core blast2un qiuzh610  R      31:48      1 s33
               6968659      core  bpe_nmt moamagda RD       0:00      1 (Reservation uppmax2022-2-18_4 was deleted)
               6968658      core  bpe_nmt moamagda RD       0:00      1 (Reservation uppmax2022-2-18_4 was deleted)
               6968656      core word_nmt moamagda RD       0:00      1 (Reservation uppmax2022-2-18_4 was deleted)
               6968644      core word_nmt  matsten RD       0:00      1 (Reservation uppmax2022-2-18_4 was deleted)
               9642777      node P20608_5    teitu PD       0:00      1 (Resources)
               9642764      node     flye   octpa7  R    8:14:14      1 s9
               9641505      node Fed_3_10  koussai  R   21:48:40      1 s73
               9639430      node hmm_alig   ninaza  R 8-16:57:07      1 s149
               9642775      node rhd0_st3    ariah  R      31:58      8 s[123-124,126-129,131,133]
               9642763      node rhd1_st3    ariah  R   13:57:58      8 s[121,139,141,143-145,147-148]
               9639541   veryfat interact  nikolay PD       0:00      1 (ReqNodeNotAvail, UnavailableNodes:s230)
               9545835   veryfat     BAND    baldo PD       0:00      1 (AssocMaxCpuMinutesPerJobLimit)
               9639540   veryfat interact  nikolay  R 7-21:34:31      1 s229
    ```

## View your jobs in the queue

### View your jobs in the Bianca or Rackham queue

View your jobs in the in the [Bianca](../cluster_guides/bianca.md) or [Rackham](../cluster_guides/rackham.md) queue:

```bash
squeue -u $USER
```

???- question "How does that look like?"

    Your output will be similar to this, when you have no jobs in the queue:

    ```bash
    [sven@rackham1 ~]$ squeue -u $USER
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    ```


### View your jobs in the Snowy queue

View your jobs in the in the [Snowy](../cluster_guides/snowy.md) queue:

???- question "How does that look like?"

    Your output will be similar to this, when you have no jobs in the queue:

    ```bash
    [sven@rackham1 ~]$ squeue -u $USER -M snowy
    CLUSTER: snowy
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    ```


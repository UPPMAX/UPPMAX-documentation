# Starting Integrative Genomics Viewer (IGV) on Rackham/Snowy

This guide will go through step by step how to start Integrative Genomics Viewer.

## Step 1: Connect to UPPMAX with X-forwarding enabled. (Important step)

In a terminal, use [SSH with X forwarding enabled](../software/ssh_x_forwarding.md):

```console
ssh -X [user name]@rackham.uppmax.uu.se
```

For example:

```
ssh -X sven@rackham.uppmax.uu.se
```

- Windows users: we recommend the [SSH client](../software/ssh_client.md) MobaXterm
- MacOS users: the built-in [SSH client](../software/ssh_client.md) `ssh` does need [XQuartz](https://www.xquartz.org/) installed too

## Step 2: Reserve a node using "interactive"
Since genomic sequences require lots of memory, it is not suitable to run IGV on one of the login nodes. That would slow down the response times for all other users on the same login node..

Instead, reserve a node that you will have all by yourself. This command will reserve a whole node for 12 hours, the maximum amount of interactive time you can get and still receive a high priority for your job (feel free to change that if you want to).

```console
interactive -A [UPPMAX project id] -p node -t 12:00:00
```
For example:

```console
interactive -A snic2017-7-274 -p node -t 12:00:00
```

For interactive session on Snowy add the flag "-M snowy":

```console
interactive -A snic2017-7-274 -M snowy -p node -t\ 12:00:00
```

## Step 3: Load the IGV module
When your job has been started, type the following command to load the IGV module:

```console
module load bioinfo-tools IGV
```

## Step 4: Start IGV
To start IGV, type the following:

```console
igv-node
```
That's it, now IGV should be loaded and ready to go. For more information about how to use IGV, please visit [IGV's user guide](https://igv.org/doc/desktop/).

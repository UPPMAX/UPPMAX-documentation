# Starting Integrative Genomics Viewer (IGV) on Rackham/Snowy

This guide will go through step by step how to start Integrative Genomics Viewer.

## Step 1: Connect to UPPMAX with X-forwarding enabled. (Important step)

In a terminal window using [`ssh`](../software/ssh.md) looks like:

```
ssh -X [user name]@rackham.uppmax.uu.se
```

For example:

```
ssh -X sven@rackham.uppmax.uu.se
```

On a Windows computer, please use MobaXterm for connecting. PuTTY does not support X-forwarding without an installed X-server, which MobaXterm conveniently has preinstalled.

If you are using a current Mac OS version then X11 is not any longer bundled and you will have to install it yourself first from the  XQuartz download page.

## Step 2: Reserve a node using "interactive"
Since genomic sequences require lots of memory, it is not suitable to run IGV on one of the login nodes. That would slow down the response times for all other users on the same login node..

Instead, reserve a node that you will have all by yourself. This command will reserve a whole node for 12 hours, the maximum amount of interactive time you can get and still receive a high priority for your job (feel free to change that if you want to).

interactive -A [UPPMAX project id] -p node -t 12:00:00
For example:

interactive -A snic2017-7-274 -p node -t 12:00:00
For interactive session on Snowy add the flag "-M snowy":

interactive -A snic2017-7-274 -M snowy -p node -t\ 12:00:00

## Step 3: Load the IGV module
When your job has been started, type the following command to load the IGV module:

module load java bioinfo-tools IGV
Step 4: Start IGV
To start IGV, type the following:

igv-node
That's it, now IGV should be loaded and ready to go. For more information about how to use IGV, please visit IGV's user guide.

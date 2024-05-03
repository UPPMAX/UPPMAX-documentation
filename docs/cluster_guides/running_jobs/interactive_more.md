# How to run interactively on a compute node?
https://www.uppmax.uu.se/support/faq/running-jobs-faq/how-can-i-run-interactively-on-a-compute-node/

You may want to run an interactive application on one or several compute nodes. You may want to use one or several compute nodes as a development workbench, interactively. How can this be arranged?
The program interactive may be what you are looking for.

The best way to use the command is usually to add as few parameters as possible, because the interactive command tries to find an optimal solution to give you a high queue priority and thus a quick job start. If you have a clear idea about what parameters you need, please specify them, otherwise it might be a good idea to first see what you get with fewer parameters.

The one parameter you must always specify is the project name. Let's assume for this article that your project name is p2010099.

To get one compute core with the proportional amount of RAM, we recommend you to use the most simple command on the login node for the cluster you want to use:

interactive -A p2010099
If you need more than one core, or special features on your node, you can specify that to the interactive command, e.g. on milou:

interactive -A p2010099 -n 16 -C fat
as if it was an sbatch command. Actually, interactive is implemented partly as an sbatch command and you can use most sbatch flags here. Please note that only a few nodes are fat, so you may have to wait for quite a long time to get your session started.

There are three ways to get a priority boost, and the interactive command knows how to use them all:

Internally using the sbatch flag "--qos=interact", that allows a single-node job with a timelimit of up to 12 hours. (Please note that you are not allowed to keep more than one "--qos=interact" jobs in the batch system simultaneously, and please note that you can not use this "priority lane" when you have oversubscribed your 30 days running core hour allocation.)
Internally using the special devel partition, that allows the job to use 1-4 nodes, with a timelimit of up to one hour. (Please note that you are not allowed to keep more than one "devel" job in the batch system simultaneously, regardless if they are running or merely queued.)
Internally using the sbatch flag "--qos=short", that allows the job to use 1-4 nodes, with a timelimit of up to 15 minutes. (Please note that your are not allowed to keep more than two "short" jobs in the batch system simultaneously.)
If you do not specify any timelimit, the interactive command will give you the maximum timelimit allowed, according to the rules for priority boosts.

In the last example ("interactive -A p2010099 -n 16 -C fat"), the interactive command can not use "priority lane" 1 above, because it uses more than one node (one node contains eight cores, two nodes contain a total of sixteen cores), and it can not use "priority lane" 2 above, because the special devel partition contains no fat nodes, so the interactive command tries to give you a high-priority 15-minute job.

If you also want to run for 15 hours, you may say so, with the command

interactive -A p2010099 -n 16 -C fat -t 15:00:00
but no "priority lane" can be used, you get your normal queue priority, and you might have to wait for a very long time for your session to start. Please note that you need to keep watch over when the job starts, because you are accounted for all the time from job start even if you are sleeping, and because an allocated and unused node is a waste of expensive resources.


NB. You can not launch an interactive job from an other cluster with the flag -M, which otherwise is a common flag to other SLURM commands. You must launch it from a login node to the cluster you want to use.

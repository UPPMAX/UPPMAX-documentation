# What do the fields PRIORITY and REASON mean in "jobinfo" output?

???- info "For UPPMAX staff"

    TODO: InfoGlue link: `https://www.uppmax.uu.se/support/faq/running-jobs-faq/your-priority-in-the-waiting-job-queue/`

Initial priority, at submit time

One of the columns in "jobinfo" output is named PRIORITY. The queue is sorted on priority, i.e. normally the job with the highest priority starts first, so this is an important parameter.

When you submit a job at UPPMAX, it gets an initial priority. Normally this is 100000, but some jobs start at a priority of 200000 or more:

On a limited amount of nodes, a group of people get a higher priority, due to e.g. that they have funded those nodes.
Jobs that have asked for the interactive priority, with the flag "--qos=interact". This is for one-node jobs with a timelimit of at most 12 hours.
Jobs that have asked for the short-job priority, with the flag "--qos=short". This is for jobs of from one to four nodes, with a timelimit of at most 15 minutes.
When your project has overdrafted its 30 days running core hour allocation, the jobs within your project get a low initial priority of 70000 or less. These jobs are named bonus jobs. Instead of disallowing them from running, they are allowed to start, if there are free resources, when all higher-priority jobs have started. For each 10000 more core hours, that the project overdrafts its allocation, the priority gets lowered by 10000 more. The bottom value is 10000, i.e. a bonus job can start queuing with any of the following priorities, depending on how big the overdraft is: 70000, 60000, 50000, 40000, 30000, 20000, or 10000.

For every minute waiting in queue, a job gets a priority increase of approximately one, up to a waiting time of 14 days.

Now the waiting for each kind of jobs will be described: For high-priority jobs, bonus jobs and normal jobs.

High-priority job
Getting a high priority, i.e. a priority higher than 210000, already at submit time, this job will probably start quickly.

The priority value will slowly increase, for each minute passing, until the job starts.

Bonus job
Getting a low priority already at submit time, this job may have to wait a long time before starting. It is very difficult to estimate the waiting time, because all new high-priority and normal jobs will have a higher priority.

At night or during next weekend, this job may be lucky and start. Waiting long enough, the monthly allocation of the project will not be overdrafted any longer, and the job automatically converted to a normal job.

The priority value will slowly increase, for each minute passing, until the job starts.

Once the job has started, it will be treated like any other job.

Normal job
A normal job, starting at priority 100000, increases slowly in priority and may eventually start at a priority a little above 100000.

But more likely, something else will happen to it before that: It will be elevated to a higher starting priority: 190000. At the same time it loses the extra priority it accumulated while waiting at the priority 100000 level.

Only normal jobs, will be elevated like this, and only one job or a few jobs for each user may be elevated at the same time.

The reason for the elevated level, is to give each user a fair chance to start at least one job within a reasonable time, even if other users have thousands of jobs already waiting in queue. The job start time will not depend mainly on the number of jobs that are waiting, but instead on the number of other users that are waiting.

At least one job for each user are permitted to wait at the elevated level. Up to 64 jobs for each user are permitted there, if they are very small. Every five minutes the system will try to elevate more jobs and every five minutes each old, elevated job gets five additional priority points.

Once the job has been elevated, its START_TIME approximations will be much more accurate. The main risk for a later start, is that someone submits new, high-priority jobs. On the other hand, running jobs usually terminate earlier than what their timelimit suggests.

Here is a detailed description on how jobs are picked for elevation:

Jobs are picked strictly in order of priority.
A job is not elevated, if its timelimit does not allow it to finish before next planned maintenance stop.
At least one job per user is elevated, regardless of size and regardless of the two limitations mentioned below in this list.
The elevated jobs of a user must not together ask for more than 64 cores.
The elevated jobs of a user must not together ask for more than 2688 core hours, i.e. 112 core days.

How does SLURM decide what job to start next?
When there are free nodes, an approximate model of SLURM's behaviour is this:

Step 1: Can the job in position one start now?
Step 2: If it can, remove it from the queue, start it, and continue with step 1.
Step 3: If it can not, look at next job.
Step 4: Can it start now, without risking that the jobs before it in the queue get a higher START_TIME approximation?
Step 5: If it can, remove it from the queue, start it, recalculate what nodes are free, look at next job and continue with step 4.
Step 6: If it can not, look at next job, and continue with step 4.
As soon as a new job is submitted and as soon as a job finishes, SLURM restarts with step 1, so most of the time only jobs at the top of the queue are tested for the possibility to start it. As a side effect of this restart behaviour, START_TIME approximations are normally NOT CALCULATED FOR ALL JOBS.

More about other jobinfo columns for waiting jobs
Until now, we have looked into the PRIORITY and USER columns. Let us talk about some of the others, for waiting jobs:

JOBID: This is the best way to identify a job in a unique way. If you succeed to submit a job, it gets a jobID. The jobID of your finished jobs can be found with the finishedjobinfo command.
POS: This is a numbering of the lines, by jobinfo, after sorting with PRIORITY as first key and JOBID as the second. This is an approximation of the queue position.
PARTITION: A SLURM partition is a set of compute nodes, together with some rules about how jobs must be handled, if they ask for this partition. An UPPMAX cluster normally sports the "devel", "core" and "node" partitions.
NAME: This is the job name, specificed at submission time with the "-J" or "--job-name" flag. This name can help you to keep track of what the job was meant to do.
ACCOUNT: The specified project name, to keep track of how many core hours each project has needed. The projinfo command sums up those core hours.
ST: Means status. Status "PD" means pending (waiting), status "R" means running, status "CG" means completing (the job has finished, but the clean-up after the job is not finished yet).
START_TIME: An estimation about when the job will start, if all jobs run until the end of their timelimit. You can make guesses about when nodes gets free also by looking at the TIME_LEFT column of running jobs. SLURM computes START_TIME only when it needs the information, i.e. you can not find that information for all jobs.
TIME_LEFT: The specified timelimit for the job. When getting near to a maintenance stop, long jobs can not start, because they may not finish before the maintenance stop starts.
REASON: There are a number of possible reasons for a job not to have started yet. Some are explained here:
AssociationJobLimit: probably means that the job never will start, because it breaks some system limit, set by UPPMAX.
BeginTime: says that the user has specified that the job must not start until some specified time in the future.
Dependency: means that the job will not start until some special other job(s) has (have) finished.
JobHeldAdmin: means that some systems administrator has told that the job must not start.
JobHeldUser: means that the job owner has told that job must not start.
None: might mean that SLURM has not yet had time to put a reason there.
Priority, ReqNodeNotAvail, and Resources: are the normal reasons for waiting jobs, meaning that your job can not start yet, because free nodes for your job are not found.
QOSResourceLimit: means that the job has asked for a QOS and that some limit for that QOS has been reached. The job can not start as long as the limit still is reached.
QOSJobLimit: probably means that the job can never start, because it breaks some system limit, set by UPPMAX.
FEATURES: There are quite a few of these and some are explained here:
null: means that no special features have been asked for.
fat: means that a fat node (a node with a more-than-standard -- for this cluster -- amount of memory) is needed.
thin: means that a standard (i.e. non-fat) node must be used, and this feature is automatically set for most jobs with no memory requirements and a high timelimit, so the job will not unnecessarily hog a fat node for a long time.

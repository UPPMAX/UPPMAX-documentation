# Runtime tips

## General

???- question "How can I run X11 applications inside GNU screen?"

    **If I log in to the [login node](../cluster_guides/login_node.md) with ssh -XA user@hostname
    as supposed when wanting to run X applications,
    and then try to start an X application inside a screen session,
    why does this not work?**

    (This applies also for trying to do PNG output in R,
    since it depends on X11)

    When starting a screen session, your DISPLAY environment can sometimes change from the one that you had when you logged in.

    To solve this problem, you simply have to set the DISPLAY variable inside the screen session, to the same value that you have outside it.

    So, outside the screen session, do:

    ```bash
    echo $DISPLAY
    ```

    You might see something like:

    ```console
    localhost:45.0
    ```

    Then, inside your screen session, set your DISPLAY env variable to that same value using the export command, like so:

    ```bash
    export DISPLAY=localhost:45.0
    ```

    (NOTE: The actual number above might be different for you, and should be changed accordingly!)

???- question "I want my program to send data to both stdout and to a file but nothing comes until the program ends"

    There is a program called unbuffer. You could try using it like (tee takes care of sending both to stdout and to a file):

    ```bash
    unbuffer your_program |tee some_output_file
    ```

???- question "My program suddenly seems to stop executing but it does not crash, the process is still alive. What is wrong?"

    - This may happen if your executable binary file is deleted while the program is running.
    - For example, if you recompile your program the previous executable file is deleted, which can cause running instances of the program to crash with "Bus error".
    - The recommended solution is that if you need to recompile or reinstall while the program is running, create a copy of the executable file and execute the copy.
    - Then, the original executable file can be safely deleted. -
    - Alternatively, rename the currently executing file to something new and unique (using the mv command) before recompiling/reinstalling your program.

???- question "My program crashes with the error message 'Bus error'. Why?"

    - This may happen if your executable binary file is deleted while the program is running.
    - For example, if you recompile your program the previous executable file is deleted, which can cause running instances of the program to crash with "Bus error".
    - The recommended solution is that if you need to recompile or reinstall while the program is running, create a copy of the executable file and execute the copy.
    - Then, the original executable file can be safely deleted. -
    - Alternatively, rename the currently executing file to something new and unique (using the mv command) before recompiling/reinstalling your program.

???- question "I have strange problems with my text-files / scripts when they have been copied from other computers"

    ???- info "For UPPMAX staff"

        TODO: InfoGlue link: `https://www.uppmax.uu.se/support/faq/running-jobs-faq/strange-problems-with-text-files---scripts-copied-from-other-computers/`

    One reason is that copy-and-paste sometimes doesn't work. Rich text files and PDF's often replace symbols like quotes and white space with different symbols to improve readability, and copying from sources like these is generally not a good idea.

    Another possible reason is that lines of text files are terminated differently on UNIX/Windows/MAC. Read on for information on how to solve this:

    This might happen because your file was created, for instance, on a Windows computer and later copied to UPPMAX Linux machines. Text files have different line terminations on for instance Windows and Linux/Unix. If this is an ordinary textfile you can test this by using the "file" command, like this:

    ```bash
    $ file myfile
    myfile: ASCII text, with CRLF line terminators
    ```

    `CRLF terminators` tells you that each line of the file is ended by both a carriage-return and a line-feed, as on Windows. On all UPPMAX systems, the file can simply be converted to UNIX style text files using the "dos2unix" command:

    ```bash
    $ dos2unix myfile
    dos2unix: converting file myfile to UNIX format ...
    ```

    Checking the file again with the "file" command reveals that it now has ordinary UNIX line terminators (only LF):

    ```bash
    $ file myfile
    myfile: ASCII text
    ```

    Similarly, a file from a Mac can be converted using the "mac2unix" command.

    If a shell script is behaving strangely, it can be due to the same problem. Trying to execute a program where the end of line marker is wrong might result in an error message such as the one below:

    ```bash
    $ cat myscript.sh
    #!/bin/sh
    ./program
    $ ./myscript.sh
    : No such file or directory
    ```

    The "file" command does not work in this case as it simply tells us that the script is a "Bourne shell script text executable". Opening the script using "vi" shows at the bottom of the screen "myscript.sh" [dos] 2L, 22C. The "[dos]" is a sure marker of the same problem. Opening the same file in emacs reveals the same thing (-uu-(DOS)---F1 myscript.sh). Convert the script to unix-format using the "dos2unix" command as described above. An alternative is to copy the file and use the "dos2unix" command on the copy and compare the file sizes using "ls -l":

    ```bash
    $ ls -l testme.sh
    rwxr-xr-x  1 daniels uppmax_staff 22 Dec 15 10:53 testme.sh
    $ dos2unix testme.sh
    dos2unix: converting file testme.sh to UNIX format ...
    $ ls -l testme.sh
    -rwxr-xr-x  1 daniels uppmax_staff 20 Dec 15 10:54 testme.sh
    ```

    Note that the file size went from 22 bytes to 20, reflecting that the two CR bytes at the (almost) end of the line were removed.

???- question "How to run interactively on a compute node?"

    - [Start an interactive node](../cluster_guides/start_interactive_node.md)
    - [More about interactive](interactive_more.md)

???- question "I got problems running Perl on UPPMAX with messages about 'locale'"

    - Edit your ``.bashrc`` file (located in your home folderon a UPPMAX cluster, like Rackham) and add the following lines:

    ```bash
    export LC_CTYPE=en_US.UTF-8 
    export LC_ALL=en_US.UTF-8 
    ```
    
    - ... then restart your [terminal](../software/terminal.md), or run, when located in your home folder:

    ```bash
    source .bashrc
    ```

## Related to Batch jobs

???- question "Looking at "jobinfo" output, PRIORITY and REASON for my waiting jobs change over time. Please explain what is going on!"

    [What do the fields PRIORITY and REASON mean in "jobinfo" output?](../software/jobinfo.md)

???- question "How do I use the modules in batch jobs?"

    - In order to make running installed programs easier you should use the module command.
    - The different [modules](../cluster_guides/modules.md) that are installed sets the correct environments that are needed for the programs to run, like ``PATH``, ``LD_LIBRARY_PATH`` and ``MANPATH``.
    -To see what what modules that are available, type ``module avail``. To see what modules you have loaded, type ``module list``.

    - Note. For the batch system slurm to work with modules you must have

    ```console
    #!/bin/bash -l
    ```

    in your submit script.

    - For more information, read the [module system guide](../cluster_guides/modules.md)

???- question "What is causing the sbatch script error 'Unknown shell type `load`'?"

    - If you're getting the error message

    ```console
    init.c(379):ERROR:109: Unknown shell type load
    ```

    when running your sbatch script, then your script is probably starting with the line

    ```console
    #!/bin/bash
    ```

    To remedy this you need to make sure that your script starts with

    ```console
    #!/bin/bash -l
    ```

    i.e. notice the trailing "-l". This tells bash to load the correct environment settings, which makes the module system usable.

???- question "I get ``slurmstepd: error: _get_pss:ferror() /proc/$$/smaps``"

    Sometimes, this error message occurs in the Slurm output file: ``slurmstepd: error: _get_pss: ferror() indicates error on file /proc/$$/smaps``
    
    This error does not affect the results and can be ignored.
    
    Statistics are collected when a job has finished, including PSS, which is a measure of memory usage. The error message means that when Slurm tries to collect all info to calculate PSS, the file exposing kernel statistics for the process is already gone. This is probably due to the cleaning process being slightly out of sync.
    
    Job statistics based on the PSS value, like how much memory a job has used, might not be reliable. But since this is something that happens after the job has finished, results should not be affected.

???- question "How can I see my job's memory usage?"

    - Historical information can first of all be found by issuing the command ``finishedjobinfo -j``. That will print out the maximum memory used by your job.

    - If you want more details then we also save some memory information each 5 minute interval for the job in a file under ``/sw/share/slurm/[cluster-name]/uppmax_jobstats/``. Notice that this is only stored for 30 days.

    - You can also ask for an e-mail containing the log, when you submit your job with sbatch or start an "interactive" session, by adding a "-C usage_mail" flag to your command. Two examples:

    ```bash
    sbatch -A testproj -p core -n 5 -C usage_mail batchscript1
    ```

    or, if interactive

    ```bash
    interactive -A testproj -p node -n 1 -C "fat&usage_mail"
    ```

    - As you see, you have to be careful with the syntax when asking for two features, like "fat" and "usage_mail", at the same time. The logical AND operator "&" combines the flags.

    - If you overdraft the RAM that you asked for, you will probably get an automatic e-mail anyway.

    - If, on the other hand, you want to view your memory consumption in real time then you will have to login to the node in question in another SSH session. (You will probably find a more recently updated memory information file there, named /var/spool/uppmax_jobstats/.)

    - By naively looking at the memory consumption with tools like ``ps`` and ``top`` you as a user can easily get the wrong impression of the system, as the Linux kernel uses free memory for lots of buffers and caches to speed up other processes (but releases this as soon as applications requests it).

    - If you know that you are the only user running on the node (from requesting a node job for example), then you could issue the command "free -g" instead. That will show you how much memory is used/free by the whole system, exclusive to these caches. Look for the row called "-/+ buffers/cache".

    - If you require more detailed live information,
      then it would probably be best if the tool called `smem` is used.
      Download the latest version from [http://www.selenic.com/smem/download/](http://www.selenic.com/smem/download/) and unpack it in your home directory.
      Inside you will find an executable Python script, and by executing the command `smem -utk` you will see your user's memory usage reported in three different ways.

        - USS is the total memory used by the user without shared buffers or caches.
        - RSS is the number reported in "top" and "ps"; i.e. including ALL shared buffered/cached memory.
        - And then there's also the PSS figure which tries to calculate a proportional memory usage per user for all shared memory buffers and caches (i.e. the figure will fall between USS and RSS).

???- question "My job has very low priority! What can be wrong?"

    - One reason could be that your project has consumed its allocated hours.

    - Background: Every job is associated with a project.
        - Suppose that that you are working for a SNIC project s00101-01 that's been granted 10000 core hours per 30-days running.
        - At the start of the project, s00101-01 is credited with 10000 hours and jobs that runs in that project are given a high priority.
        - All the jobs that are finished or are running during the last 30 days is compared with this granted time.
        - If enough jobs have run to consume this amount of hours the priority is lowered.
        - The more you have overdrafted your granted time, the lower the priority.

    - If you have overdrafted your granted time it's still possible to run jobs. You will probably wait for a longer time in the queue.

    - To check status for your projects, run

    ```bash
    $ projinfo
    (Counting the number of core hours used since 2010-05-12/00:00:00 until now.)

    Project             Used[h]   Current allocation [h/month]
    User
    -----------------------------------------------------
    s00101-01          72779.48               50000
    some-user       72779.48
    ```

    - If there are enough jobs left in projects that have not gone over their allocation, jobs associated with this project are therefore stuck wating at the bottom of the jobinfo list until the usage for the last 30 days drops down under its allocated budget again.

    - On the other side they may be lucky to get some free nodes, so it could happen that they run as a bonus job before this happens.

    - The job queue, that you can see with the jobinfo command, is ordered on job priority. Jobs with a high priority will run first, if they can (depending on number of free nodes and any special demands on e.g. memory).

    - Job priority is the sum of the following numbers (you may use the sprio command to get exact numbers for individual jobs):

        - A high number (100000 or 130000) if your project is within its allocation and a lower number otherwise. There are different grades of lower numbers, depending on how many times your project is overdrafted. As an example, a 2000 core hour project gets priority 70000 when it has used more than 2000 core hours, gets priority 60000 when it has used more than 4000 core hours, gets priority 50000 when it has used more than 6000 core hours, and so on. The lowest grade gives priority 10000 and does not go down from there.
        - The number of minutes the job has been waiting in queue (for a maximum of 20160 after fourteen days).
        - A job size number, higher for more nodes allocated to your job, for a maximum of 104.
        - A very, very high number for "short" jobs, i.e. very short jobs that is not wider than four nodes.
        - If your job priority is zero or one, there are more serious problems, for example that you asked for more resources than the batch system finds on the system.

    - If you ask for a longer run time (TimeLimit) than the maximum on the system, your job will not run. The maximum is currently ten days. If you must run a longer job, submit it with a ten-day runtime and contact UPPMAX support.

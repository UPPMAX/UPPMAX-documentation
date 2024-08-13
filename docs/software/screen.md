# Running a detachable screen process in a job

When you run the `interactive` command, you get a command prompt in the _screen_ program.

!!! warning
    When running the screen program in other environments, you can detach from your screen and later reattach to it. Within the environment of the `interactive` command, you lose this ability: Your job is terminated when you detach. (This is a design decision and not a bug.)

In case you want the best of both worlds, i.e. to be able to detach and reattach to your screen program within a job, you need to start a job in some other way and start your screen session from a separate ssh login. Here is an example of how you can do this:

```bash
$ salloc -A project_ID -t 15:00  -n 1 --qos=short --bell --no-shell
salloc: Pending job allocation 46964140
salloc: job 46964140 queued and waiting for resources
salloc: job 46964140 has been allocated resources
salloc: Granted job allocation 46964140
salloc: Waiting for resource configuration
salloc: Nodes r174 are ready for job
```

Check the queue manager for the allocated node. In the example bellow, one core was allocated on `r174` compute node.

```bash
$ squeue -j 46964140
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          46964140      core no-shell     user  R       0:44      1 r174
```

You can start `xterm` [terminal](../software/terminal.md) in this allocated session like this:

```bash
xterm -e ssh -AX r174 &
```

`salloc` command gives you a job allocation of one node for 15 minutes (the "--no-shell" option is important here). Instead you can log in to any node of any of your running jobs, started with e.g. the `sbatch` command.

You get a job number and from that you can find out the node name, in this example r174.

When you log in to the node with the `ssh` command, start the screen program:

```bash
screen
```

When you detach from the screen program, with e.g. the "d" command, you can later in the same ssh session or in another ssh session reattach to your screen session:

```bash
screen -r
```

When your job has terminated, you can neither reattach to your screen session nor log in to the node.

The screen session of the `interactive` command is integrated into your job, so e.g. all environment variables for the job is correctly assigned. For a separate ssh session, as in this example, that is not the case.

Please note that it is the job allocation that determines your core hour usage and not your ssh or screen sessions.

## Tips

- Start a new screen session with a command:

    ```bash
    screen -dm your_command
    ```

    This will start a new screen session, run the command, and then detach from the session.

- If you want to run multiple commands, you can do so like this:

    ```bash
    screen -dm bash -c "command1; command2"
    ```

    This will run `command1` and `command2` in order.

- To reattach to the screen session, use:

    ```bash
    screen -r
    ```

    If you have multiple sessions, you'll need to specify the session ID.

- To list your current screen sessions, use:

    ```bash
    screen -ls
    ```

Please note that when a program terminates, `screen` (by default) kills the window that contained it. If you don't want your session to get killed after the script is finished, add `exec sh` at the end. For example:

```bash
screen -dm bash -c 'your_command; exec sh'
```

This will keep the screen session alive after `your_command` has finished executing.

YouTube : [How to use GNU SCREEN - the Terminal Multiplexer](https://www.youtube.com/watch?v=I4xVn6Io5Nw)

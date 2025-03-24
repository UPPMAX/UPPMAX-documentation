# Matlab configure for the cluster

## First time, since May 13 2024

- If you use MATLAB after May 13 2024, of any version, you have to do the following step to be able to use the full features of running parallel jobs.
    - Only needs to be run once.
    - Note, however, that on Bianca this has to be done separately.

- After logging into the cluster, configure MATLAB to run parallel jobs on the cluster by calling the shell script configCluster.sh.

```console
module load matlab/<version>
configCluster.sh <project-ID>    # Note: no '-A'
```

- This will run a short configuration job in an interactive session.
- Jobs will now default to the cluster rather than submit to the local machine.
- It should look like this (example for Bianca)

![matlab configCluster.sh](img/matlab_configCluster.PNG)

- The session should exit automatically but if not you can end the session by
    - ``exit``
    - or ``<CTRL-C>``
- When done, start Matlab as you usually do with  ``matlab &``.

!!! warning

    - On Bianca you need to do this for each sens project that will use MATLAB, as well.

<!--
    - Do these steps for each matlab version you will use.

!!! tip

    - Check the Matlab version for which you have set the slurm configuration by

    ```bash
    ls -l .matlab/*/parallel.mlsettings
    ```
    
    - Look for dates from May 2024 and onwards.

-->

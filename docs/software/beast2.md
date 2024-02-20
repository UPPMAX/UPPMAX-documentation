# BEAST2

BEAST2 is a tool for Bayesian phylogenetic analysis.

???- question "Is BEAST2 a new version of BEAST?"

    No. 

    Although BEAST and BEAST2 achieve a similar goal,
    BEAST and BEAST2 are developed independently.

    Hence, 
    - there are things BEAST can do that BEAST2 cannot, and vice versa
    - one cannot create a BEAST XML file and expect BEAST2 to be able to run it, and vice versa

## Using BEAST2

## 1. Load a `beast2` module

First step is to load a BEAST2 module.

Here is how to find the BEAST2 versions on the UPPMAX clusters:

```
module spider beast2
```

When loading a BEAST2 module, also load `bioinfo-tools`:

```
module load bioinfo-tools beast2/2.7.4
```

???- question "How does that look like?"

    ```
    $ module load bioinfo-tools beast2/2.7.4
    beast2/2.7.4: Also loaded beagle/4.0.0
    beast2/2.7.4: Many Beast packages are available, to see the list, 'packagemanager -list'
    beast2/2.7.4: Use BEAST_XMX to specify the amount of RAM (default 5g), 'export BEAST_XMX=15g'. Do not exceed RAM available to your job.
    ```

## 2. Run `BEAUti`

Next step is to create a BEAST2 configuration file
using `BEAUti`. This graphical tool can be started using:

```
beauti
```

Make sure you have X-forwarding enabled, 
see [Login to Rackham](../getting_started/login_rackham.md)
to see this.

???- question "How does that look like?"

    Starting `BEAUti` results in the following pop-up window:

    ![](./img/beauti.png)

After using `BEAUti`, save the file with your BEAST2 model.

## 3. Run 

A BEAST2 run takes a lot of computing power,
hence do not run it on a login node.
Instead, run it on an interactive node 
or use a script.

???- question "How to start an interactive node?"

    View the UPPMAX documentation
    ['How to start an interactive node on Rackham'](../cluster_guides/start_interactive_node_on_rackham).


On an interactive node, run BEAST2 on the saved BEAST2 model:

```
beast beast2_setup.xml
```

When using a script, put that line in a script.
Below is an example script, called `run_beast2.sh`:

```bash title="run_beast2.sh"
#!/bin/bash
#SBATCH -A uppmax2023-2-25
module load bioinfo-tools beast2/2.7.4
beast beast2_setup.xml
```

 * In line 2, replace `uppmax2023-2-25` with [your UPPMAX project](../getting_started/project.md).
 * In line 3, you may want to replace `beast2/2.7.4` with your favorite BEAST2 version

Then run this script using `sbatch run_beast2.sh`.

Note that this is a *minimal* script.
See [the UPPMAX documentation on Slurm](../cluster_guides/slurm.md)
for ways to improve this script.

## View the trees using DensiTree

DensiTree is a tool that allows one to display the posterior tree distribution
of a BEAST2 run.

Run:

```
densitree [trees_filename]
```

where `[trees_filename]` is the name of the file containing the posterior trees,
resulting in, for example, `densitree my_file.trees`.

![](./img/densitree.png)

## Run Tracer

Tracer is a tool to analyse the results of a BEAST2 run.
It is not an UPPMAX module.

Instead, it needs to be download and run:

### 1. Download 

Pick [a Tracer release](https://github.com/beast-dev/tracer/releases),
such as [Tracer v1.7.2](https://github.com/beast-dev/tracer/releases/tag/v1.7.2)
and download the Linux/UNIX version.

???- question "How does that look like?"

    Here is how the release page of [Tracer v1.7.2](https://github.com/beast-dev/tracer/releases/tag/v1.7.2)
    looks like:
    
    ![](./img/tracer_release.png)

    Download the file `Tracer_v1.7.2.tgz`.

???- question "How to download from the command-line?"

    Use `wget` on the URL to download from, for example:

    ```
    wget https://github.com/beast-dev/tracer/releases/download/v1.7.2/Tracer_v1.7.2.tgz
    ```

### 2. Extract

Extract the downloaded file.

???- question "How to do so, using the remote desktop environment?"

    Right-click the file and click 'Extract here'.

    ![](../cluster_guides/img/rackham_remote_desktop_extract_file.png)

???- question "How to do so, using the console environment?"

    Use `tar` on the file to extract:

    ```
    tar zxvf  Tracer_v1.7.2.tgz
    ```

### 3. Run

Use `java` to run the Tracer `jar` file:

```
java -jar lib/tracer.jar
```

???- question "How does that look like?"

    Here is how Tracer looks like in a console environment:

    ![](./img/tracer_on_rackham_console.png)

    For this to work, one needs to login using X-forwarding (`ssh -X`),
    as described in the ['getting started'](../getting_started/get_started.md)
    pages.

## Show info

```
beast -beagle_info
```

???- "How does that look like?"

    Here the command is run on a [Rackham](../cluster_guides/rackham.md) 
    compute node, using an interactive session:

    ```
    [richel@s93 ~]$ beast -beagle_info

                            BEAST v2.7.4, 2002-2023
                 Bayesian Evolutionary Analysis Sampling Trees
                           Designed and developed by
     Remco Bouckaert, Alexei J. Drummond, Andrew Rambaut & Marc A. Suchard
                                        
                       Centre for Computational Evolution
                             University of Auckland
                           r.bouckaert@auckland.ac.nz
                            alexei@cs.auckland.ac.nz
                                        
                       Institute of Evolutionary Biology
                            University of Edinburgh
                               a.rambaut@ed.ac.uk
                                        
                        David Geffen School of Medicine
                     University of California, Los Angeles
                               msuchard@ucla.edu
                                        
                          Downloads, Help & Resources:
                               http://beast2.org/
                                        
      Source code distributed under the GNU Lesser General Public License:
                       http://github.com/CompEvol/beast2
                                        
                               BEAST developers:
       Alex Alekseyenko, Trevor Bedford, Erik Bloomquist, Joseph Heled, 
     Sebastian Hoehna, Denise Kuehnert, Philippe Lemey, Wai Lok Sibon Li, 
    Gerton Lunter, Sidney Markowitz, Vladimir Minin, Michael Defoin Platel, 
              Oliver Pybus, Tim Vaughan, Chieh-Hsi Wu, Walter Xie
                                        
                                   Thanks to:
              Roald Forsberg, Beth Shapiro and Korbinian Strimmer


    --- BEAGLE RESOURCES ---

    0 : CPU (x86_64)
        Flags: PRECISION_SINGLE PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL EIGEN_COMPLEX SCALING_MANUAL SCALING_AUTO SCALING_ALWAYS SCALERS_RAW SCALERS_LOG VECTOR_SSE VECTOR_NONE THREADING_CPP THREADING_NONE PROCESSOR_CPU FRAMEWORK_CPU
    ```

## Links

 * [DensiTree GitHub repository](https://github.com/rbouckaert/DensiTree)

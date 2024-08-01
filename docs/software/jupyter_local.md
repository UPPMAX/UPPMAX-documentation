# Jupyter in local browser

To increase the speed of graphics it is possible to run Jupyter on a compute node, but using the graphics on your local computer. That will speed up the interaction with plotting figures and GUI management.

This possible for the Rackham and Snow clusters.

!!! warning

    This feature is not possible for Bianca

## Step 1: Login to an UPPMAX cluster

- Using ThinLinc or a terminal does not matter.,

## Step 2: start an interactive session

Start a terminal. Within that terminal, start an interactive session from the login node (change to the correct NAISS project ID).
  
### For Rackham

```sh
$ interactive -A <naiss-project-id>  -t 4:00:00
```

### For Snowy

```sh
$ interactive -M snowy -A <naiss-project-id>  -t 4:00:00
```

## Step 3: start Jupyter in the interactive session

Within your terminal with the interactive session, load a modern Python module:

```sh
module load python/3.11.8
```

Then, start ``jupyter-notebook`` (or ``jupyter-lab``):

```sh
jupyter-notebook --ip 0.0.0.0 --no-browser
```

Leave this terminal open.

The terminal will display multiple URLs.

Copy one of these, like:

  ``http://r486:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``

## Step 4: On own computer

- If you use ssh to connect to Rackham, you need to forward the port of the interactive node to your local computer.
    - On Linux or Mac this is done by running in another terminal. Make sure you have the ports changed if they are not at the default ``8888``.

```sh
   $ ssh -L 8888:r486:8888 username@rackham.uppmax.uu.se
```

- Replace ``r486`` if you got another node
- If you use Windows it may be better to do this in the PowerShell instead of a WSL2 terminal.
- If you use PuTTY - you need to change the settings in "Tunnels" accordingly (could be done for the current connection as well).

![putty](../software/img/putty.jpg)

[SSH port forwarding](https://uplogix.com/docs/local-manager-user-guide/advanced-features/ssh-port-forwarding)

On your computer open the address you got but replace ``r486`` with ``localhost`` or ``127.0.0.0`` i.e.

``http://localhost:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``
or
``http://127.0.0.0:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``

This should bring the jupyter interface on your computer and all calculations and files will be on Rackham compute node.

[Back to jupyter page](jupyter.md)

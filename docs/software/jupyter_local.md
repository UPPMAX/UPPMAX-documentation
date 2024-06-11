# Jupyter on compute nodes

## Introduction

Jupyter is web application that allows literature programming
for Python. That is, Jupyter allows to create documents 
where Python code is shown and run and its results shown, 
surrounded by written text (e.g. English).

Additionally, Jupyter allows to share files and hence includes a file manager.

Jupyter is:

- started and running on a server, for example, an interactive node
- displayed in a **web browser**, such as ``firefox``.

Jupyter can be slow when using remote desktop webpage
(e.g. ``https://rackham-gui.uppmax.uu.se``).

- For UPPMAX, one can use a locally installed ThinLinc client to speed up Jupyter.
  See `the UPPMAX documentation on ThinLinc <https://www.uppmax.uu.se/support/user-guides/thinlinc-graphical-connection-guide>`_
  on how to install the ThinLinc client locally

## UPPMAX procedure

### UPPMAX procedure step 1: login to a remote desktop

Login to a remote desktop:

- Login to the remote desktop website at ``rackham-gui.uppmax.uu.se``
- Login to your local ThinLinc client

### UPPMAX procedure step 2: start an interactive session

Start a terminal. Within that terminal, 
start an interactive session from the login node 
(change to the correct NAISS project ID) 
  
**For Rackham**

```sh
$ interactive -A <naiss-project-id>  -t 4:00:00
```

**For Snowy**

```sh
$ interactive -M snowy -A <naiss-project-id>  -t 4:00:00
```

### UPPMAX procedure step 3: start Jupyter in the interactive session

Within your terminal with the interactive session, 
load a modern Python module:

```sh
module load python/3.11.8
```

Then, start ``jupyter-notebook`` (or ``jupyter-lab``):

```sh
jupyter-notebook --ip 0.0.0.0 --no-browser
```

Leave this terminal open.

### UPPMAX procedure step 4: connect to the running notebook 

The terminal will display multiple URLs.

If you use the remote desktop website:

- start ``firefox`` on the remote desktop
- browse to the first URL, which will be similar to ``file://domus/h1/[username]/.local/share/jupyter/runtimejpserver-[number]-open.html``

In both cases, you can access Jupyter from your local computer

- start ``firefox`` on your local computer
- browse to the second URL, which will be similar to 
  ``http://r486:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``

### On own computer

- If you use ssh to connect to Rackham, you need to forward the port of the interactive node to your local computer.
    - On Linux or Mac this is done by running in another terminal. Make sure you have the ports changed if they are not at the default ``8888``.

```sh
   $ ssh -L 8888:r486:8888 username@rackham.uppmax.uu.se
```
    - If you use Windows it may be better to do this in the PowerShell instead of a WSL2 terminal.
    - If you use PuTTY - you need to change the settings in "Tunnels" accordingly (could be done for the current connection as well).

![putty](../img/putty.png)

[SSH port forwarding](https://uplogix.com/docs/local-manager-user-guide/advanced-features/ssh-port-forwarding)
    
On your computer open  the address you got but replace r486 with localhost i.e.

``http://localhost:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``
or 
``http://127.0.0.0:8888/?token=5c3aeee9fbfc75f7a11c4a64b2b5b7ec49622231388241c2``

    This should bring the jupyter interface on your computer and all calculations and files will be on Rackham.

.. warning:: 

   **Running Jupyter in a virtual environment**

   You could also use ``jupyter`` (``-lab`` or ``-notebook``) in a virtual environment.

   If you decide to use the --system-site-packages configuration you will get ``jupyter`` from the python modules you created your virtual environment with.
   However, you **won't find your locally installed packages** from that jupyter session. To solve this reinstall jupyter within the virtual environment by force:

```sh
$ pip install -I jupyter
```
   and run:

```sh
$ jupyter-notebook
```
   
Be sure to start the **kernel with the virtual environment name**, like "Example", and not "Python 3 (ipykernel)".

Links
---------

- `The Jupyter project <https://jupyter.org/>`_ contains a lot of information and inspiration
- `The Jupyter Notebook documentation <https://jupyter-notebook.readthedocs.io/en/stable/>`_  
- `Video: Starting a Jupyter notebook on the Rackham UPPMAX HPC cluster using a ThinLinc remote desktop (YouTube) <https://youtu.be/72rYjwGvWEc>`_

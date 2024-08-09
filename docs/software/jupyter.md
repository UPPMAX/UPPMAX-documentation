# Jupyter

There are multiple [IDEs](../software/ides.md) on the UPPMAX clusters,
among other [Jupyter](../software/jupyter.md).
Here we describe how to run [Jupyter](../software/jupyter.md).

Jupyter is an [IDE](../software/ides.md) specialized for [the Python programming language](../software/python.md).

!!! info

    - You can run Python in a **Jupyter-notebook**,
      i.e. in a web interface with possibility of inline figures and debugging.
    - **Jupyter-lab** is installed in the **python>=3.10.8 module**

!!! warning

    Always start Jupyter in a **ThinLinc** session
    and preferably in an **interactive** session.

???- tip "Want to see a video?"

    If you want to see a video how to start Jupyter on Rackham,
    go [here](https://youtu.be/72rYjwGvWEc?si=Rn2F2ieO-kPufO9f)

## Links

- [The Jupyter project](https://jupyter.org/) contains a lot of information and inspiration
- [The Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/stable/)  

## Introduction

Jupyter is web application that allows literature programming for Python. That is, Jupyter allows to create documents where Python code is shown and run and its results shown, surrounded by written text (e.g. English).

Additionally, Jupyter allows to share files and hence includes a file manager.

Jupyter is:

- started and running on a server, for example, an interactive node
- displayed in a **web browser**, such as ``firefox``.

Jupyter can be slow when using remote desktop webpage
(e.g. ``https://rackham-gui.uppmax.uu.se``).

- For UPPMAX, one can use a locally installed ThinLinc client to speed up Jupyter. See `the UPPMAX documentation on ThinLinc <https://www.uppmax.uu.se/support/user-guides/thinlinc-graphical-connection-guide>`_ on how to install the ThinLinc client locally.

- It is also possible to run Jupyter with a local browser to speed up the graphics but still use the benefits of many CPU:s and much RAM.
    - [Run Jupyter in your local browser](jupyter_local.md)

### Some links

- `The Jupyter project <https://jupyter.org/>`_ contains a lot of information and inspiration
- `The Jupyter Notebook documentation <https://jupyter-notebook.readthedocs.io/en/stable/>`_  

## Start

### Step 1: login to a remote desktop

Login to a remote desktop:

- Login to the remote desktop website at ``rackham-gui.uppmax.uu.se``
- Login to your local ThinLinc client

### Step 2: start an interactive session

Start a [terminal](../software/terminal.md).
Within that terminal, start an interactive session from the login node (change to the correct NAISS project ID).
  
#### For Rackham

```sh
interactive -A <naiss-project-id>  -t 4:00:00
```

#### For Snowy

```sh
interactive -M snowy -A <naiss-project-id>  -t 4:00:00
```

### Step 3: start Jupyter in the interactive session

Within your terminal with the interactive session, load a modern Python module:

```sh
module load python/3.11.8
```

Then, start ``jupyter-notebook`` (or ``jupyter-lab``):

```sh
jupyter-notebook --ip 0.0.0.0 --no-browser
```

Leave this terminal open.
Start a notebook like this:

```bash
module load python/<version>
jupyter-notebook --ip 0.0.0.0 --no-browser
```

or jupyter lab:

``` bash
jupyter-lab --ip 0.0.0.0 --no-browser
```

- copy-paste one of the URL addresses from the jupyter output in the terminal into the address files in the open ``firefox`` session.

- Make Jupyter work in background, start Firefox with the copied URL address.
- `<ctrl-z>`
- `bg`
- `firefox <URL> &`
    - Example ``firefox http://127.0.0.1:8889/tree?token=7c305e62f7dacf65d74a4b966e2851987479ad0a258de33f &``

## Jupyter in a virtual environment (venv)

You could also use jupyter- (lab or notebook) in a [`venv` virtual environment](python_venv.md).

If you decide to use the ``--system-site-packages`` configuration you will get ``jupyter`` from the python modules you created you virtual environment with.
However, you won't find your locally installed packages from that jupyter session. To solve this, reinstall jupyter within the virtual environment by force (option ``-I``):

```bash
pip install -I jupyter
```

and run it as above.

Be sure to start the kernel with the virtual environment name, like "project A", and not "Python 3 (ipykernel)".

## [Run Jupyter in your local browser](jupyter_local.md)

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

## Start

Start a notebook like this:

```bash
$ module load python/<version>
$ jupyter-notebook --ip 0.0.0.0 --no-browser
```

or jupyter lab:

``` bash
$ jupyter-lab --ip 0.0.0.0 --no-browser
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
$ pip install -I jupyter
```

and run it as above.

Be sure to start the kernel with the virtual environment name, like "project A", and not "Python 3 (ipykernel)".

!!! info "Jupyter from web browser on your computer"

## [Run Jupyter in your local browser](jupyter_local.md)



    - Get insipration from <https://uppmax.github.io/R-python-julia-HPC/python/jupyter.html#on-own-computer>

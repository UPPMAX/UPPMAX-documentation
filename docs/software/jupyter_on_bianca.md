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


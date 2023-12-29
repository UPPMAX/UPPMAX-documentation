# Jupyter on Bianca

Jupyter is an IDE specialized for the Python programming language.

???- tip "What is an IDE?"

    See [the page on IDEs](ides.md).

!!! info

    - You can run Python in a **Jupyter-notebook**, i.e. in a web interface with possibility of inline figures and debugging.
    - **Jupyter-lab** is installed in the **python>=3.10.8 module**

!!! warning

    Always start Jupyter in a **ThinLinc** session and preferably in an **interactive** session.

???- tip "Want to see a video?"

    If you want to see a video how to start Jupyter on Rackham,
    go [here](https://youtu.be/72rYjwGvWEc?si=Rn2F2ieO-kPufO9f)

## Start

Start a notebook like this:

```bash
$ module load python/<version>
$ jupyter-notebook
```
or jupyter lab:

``` bash
$ jupyter-lab
```

A local Firefox session (not a internet web page!) should start with the Jupyter notebook/lab interface. 
- If not, make jupyter work in background, start firefox and paste the address.
- `` <ctrl-z>``
- ``bg``
- ``firefox &``
- copy-paste one of the addresses from the jupyter output in the terminal into the address files in the open ``firefox`` session.

- You can browse in jupyter to a test notebook in ``/proj/workshop/Jupyter-demo/Test-01.ipynb``

## Jupyter in a virtual environment (venv)

You could also use jupyter- (lab or notebook) in a virtual environment.

If you decide to use the ``--system-site-packages`` configuration you will get ``jupyter`` from the python modules you created you virtual environment with.
However, you won't find your locally installed packages from that jupyter session. To solve this, reinstall jupyter within the virtual environment by force (option ``-I``):

```bash
$ pip install -I jupyter
```
and run it as above.

Be sure to start the kernel with the virtual environment name, like "project A", and not "Python 3 (ipykernel)".
      

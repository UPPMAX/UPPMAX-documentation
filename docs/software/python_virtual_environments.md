# Virtual environments in Python

This page described how to use virtual environments in [Python](python.md).

## Why use virtual environments?

Virtual environments allows one to have independent Python environments.

This allows one to have multiple projects 

- You can install specific, also older, versions into them
- You can create one for each project and no problem if the two projects
  require different versions
- If you make some mistake and install something you did not want or need, you
  can remove the environment and create a new one

## Environment managers

Here is an incomplete overview of virtual environment managers that work with Python:

Virtual environment manager          |Description
-------------------------------------|--------------------------------
[`venv`](python_venv.md)             |Works on [Rackham](../cluster_guides/rackham.md)
[`virtualenv`](python_virtualenv.md) |`venv` for older Python versions
[`conda`](../cluster_guides/conda.md)|Works on [Rackham](../cluster_guides/rackham.md), recommended on [Bianca](../cluster_guides/bianca.md)
[`pyenv`](python_pyenv.md)           |More advanced than `venv`






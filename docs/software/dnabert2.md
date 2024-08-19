# DNABERT 2

DNABERT 2 is 'a foundation model
trained on large-scale multi-species genome that achieves the
state-of-the-art performanan on 28 tasks of the GUE benchmark',
according to [DNABERT 2](https://github.com/MAGICS-LAB/DNABERT_2)

DNABERT 2 is not part of 
[the UPPMAX module system](../cluster_guides/modules.md).

For [Rackham](../cluster_guides/rackham.md), installing
seems to be find, as [conda](conda.md) will install it in a home folder.

For [Bianca](../cluster_guides/bianca.md),
maybe a [Singularity](../software/singularity.md) container
is needed.

## Singularity container

This is untested to work.

Using [this Singularity definition file, called 'dnabert2.def'](dnabert2.def):

Building a Singularity container:

```bash
sudo singularity build dnabert2.sif dnabert2.def 
```

Running the container, using
[this example Python script, called 'dnabert2.py'](dnabert2.py):

```bash
singularity run dnabert2.sif dnabert2.py
```

## Links

- [DNABERT 2 GitHub repository](https://github.com/MAGICS-LAB/DNABERT_2)

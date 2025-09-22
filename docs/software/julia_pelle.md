# Julia on Pelle

## Introduction

Julia is according to <https://julialang.org/>:

- Fast
- Dynamic
- Reproducible
- Composable
- General
- Open source

[Documentation](https://docs.julialang.org/en/v1/) for version 1.8.

[Julia discussions](https://discourse.julialang.org/)

[NAISS Julia workshop](https://uppmax.github.io/R-matlab-julia-HPC/julia/intro/)

## Julia installations

 There is no system-installed Julia on the clusters. Therefore you need to load Julia with the module system.

## Start Julia

## Packages

### How to install personal packages

You may ignore the pre-installed packages. They are there mainly for Bianca users, but may help you to relieving some disk space! If you ignore you can jump over the this section.

### Start an installation locally

## Running IJulia from Jupyter notebook


## How to run parallel jobs

There are several packages available for Julia that let you run parallel jobs. Some of them are only able to run on one node, while others try to leverage several machines. You'll find an introduction here.

### Run interactively on compute node

### Threading

### Distributed computing

#### Master-Worker model

#### Batch example

#### Interactive example

```console
salloc -A <proj> -p node -N 1 -n 10 -t 1:0:0
julia hello_world_distributed.jl
```

### GPU

#### Interactive session with GPU


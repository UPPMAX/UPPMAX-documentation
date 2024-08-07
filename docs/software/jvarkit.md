# jvarkit

According to [the `jvarkit` GitHub repository](https://github.com/lindenb/jvarkit)
`jvarkit` is 'Java utilities for Bioinformatics',

`jvarkit` is unavailable in [the UPPMAX module system](../cluster_guides/modules.md).

## Create a `jvarkit` Singularity container

To create a [Singularity](singularity.md) container
one can follow the procedure documented at ['Create a Singularity container from DockerHub'](create_singularity_container_from_dockerhub.md).

Spoiler:

```bash
sudo singularity build my_container.sif docker:lindenb/jvarkit:1b2aedf24
```

Note that `1b2aedf24` is the tag of the latest version of this Docker script.
In the future, they may be newer tags.

Usage:

```bash
./jvarkit.sif java -jar /opt/jvarkit/dist/jvarkit.jar --help
```

## Links

- [the `jvarkit` GitHub repository](https://github.com/lindenb/jvarkit)

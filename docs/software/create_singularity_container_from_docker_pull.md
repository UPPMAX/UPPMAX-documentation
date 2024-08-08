# Create a Singularity container from a Docker pull

There are multiple ways how to [create a Singularity container](singularity.md).

This page shows how to create a Singularity container from a Docker pull,
such as this one (from [here](https://github.com/lycheeverse/lychee?tab=readme-ov-file#docker))

```bash
docker pull lycheeverse/lychee
```

## Procedure

???- question "Prefer a video?"

    You can see the procedure below in the video [Create a Singularity container from `docker pull`](https://youtu.be/gFpRvEUpJZ4).

The hardest part of this procedure may be to have
Linux with Singularity installed on a computer where you have
super-user rights.

In this example, we create a Singularity container
for [lychee](https://github.com/lycheeverse/lychee),
a tool to check for broken links in text files.

## 1. Create the Singularity container

Here we build a Singularity container from a Docker file:

```bash
sudo singularity build my_container.sif [location to Docker file]
```

The magic is in `[location to Docker file]`.

In our case, we have seen the documentation state the command `docker pull lycheeverse/lychee`
to install this Docker container. Using a `docker pull` like this, means that
the Docker script is on [Docker Hub](https://hub.docker.com).
And yes, [our Docker script is on Docker Hub](https://hub.docker.com/r/lycheeverse/lychee)!

To build a Singularity container from a Docker file on Docker Hub, do:

```bash
sudo singularity build my_container.sif docker:lycheeverse/lychee
```

## 2. Use the Singularity container

```bash
./my_container.sif [your command-line arguments]
```

For example, in this case:

```bash
./my_container.sif .
```

The `.` means 'in this folder'.

As, in this example, we have created a Singularity container
for [lychee](https://github.com/lycheeverse/lychee),
a tool to check for broken links in text files.
Hence, the full command can be read as
'Check all files in this folder for broken links'.

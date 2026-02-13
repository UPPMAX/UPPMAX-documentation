# The project directory structure on Bianca

The project folders are organised in a special way.

- The project folders for your project is the only project that can be seen when logged in to Bianca.
- It can be found in ``/proj/``
- There are 2 areas of project storage
    - **nobackup** shown by the folder name ``nobackup`` which is, wait for it...            **NOT BACKED UP!!!**
    - A backed up area that is found in the other parts

## Same files at different places

- **Nobackup** can be reached in several folders, namely:
    - ``/proj/nobackup/sens202YXXX/``
    - ``/proj/sens202YXXX/nobackup/``
    - ``/cygnus/proj/nobackup/``
    - ``/castor/project/proj/nobackup/``
    - ``/castor/project/proj_nobackup/``
- This is not seen as symbolic links but is instead so-called bind mounts.
- So you cannot tell from what you see that you are looking at the same files if not learning this structure or keep notice of dates when files and folders were changed.

!!! warning "What does this mean?"

    - Files here are the same, so removing files at one place (because you want to save some storage space) will delete them in both places.
    - Deleting files will not be recovered, since you are in the nobackup area.

!!! tip

    Use one folder always to work with, for instance:

    - ``/proj/sens202YXXX/``
    - Here you can reach both non backed up files and backed up files.

## Example of file tree

```console
[bjornc@sens2025560-bianca ~]$ tree /proj/ -L 3
/proj/
├── nobackup
│   └── sens2025560
│       ├── Should_this_Be_possible
│       └── wharf
└── sens2025560
    ├── bjornc
    │   └── gatk_4.6.2.0.sif
    ├── nobackup
    │   ├── Should_this_Be_possible
    │   └── wharf
    ├── pmitev-test-work
    │   ├── AOC-A25G-m2SM\ Updating\ FW\ to\ version\ FW\ 26.41.1000.zip
    │   ├── CellChat
    │   └── UPPMAX-Slurm-2024-08.pdf
    ├── richel
    ├── selecting_modules
    │   ├── bjornc
    │   └── exercises.tar.gz.1
    ├── sven
    │   ├── Exercises
    │   └── exercises.tar.gz
    └── workshop
        ├── cgall
        ├── completed
        ├── data
        ├── slurm
        └── soumic

```

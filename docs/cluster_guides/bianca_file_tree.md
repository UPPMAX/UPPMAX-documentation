# The project directory structure on Bianca

The project folders are organized in a special way.

- The project folders for your project is the only project that can be seen when logged in to Bianca.
- It can be found in ``proj/``
- There are 2 areas of project storage
    - **nobackup** shown by the folder name ``nobackup`` which is, wait for it...            **NOT BACKED UP!!!**
    - A backed up area that is found in the pther parts
 
## Same files at different places

- **Nobackup** can be reached in several folders, namely:
   - ``/proj/nobackup/sens202YXXX/``
   - ``/proj/sens202YXXX/nobackup/``
- This is not seen as symlinks but is instead so-called bind mounts.

!!! warning "What does this mean?"

    - Files here are the same, so removing files at one place (because you want to save some storage space) will delete them in both places.


## Example of file tree


```console
$ tree /proj -L 2
.
├── nobackup
│   └── sens2025560
└── sens2025560
    ├── bjornc
    ├── nobackup
    ├── pmitev-test-work
    ├── richel
    ├── sven
    └── workshop
```

/castor/project/proj_nobackup/_nobackup/private/
/castor/project/proj/<proj>/nobackup/private/
/castor/project/proj/<proj>/private/nobackup/

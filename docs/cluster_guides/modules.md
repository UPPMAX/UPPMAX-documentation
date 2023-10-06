# Software modules

## Background

The UPPPMAX clusters are shared Linux computers with all the standard Linux/GNU tools installed,
on which all users should be able to do their work independently and undisturbed.

To ensure this, users cannot modify, upgrade or uninstall "system-wide" software themselves and instead a [module system](https://lmod.readthedocs.io/en/latest/) is used.
This allow users to independently use their favorite versions of their favorite software.

- This system keeps installed software hidden by default, and users have to explicitly tell their terminal which version of which software they need.

- The modules are most often available across cluster (except for Miarka)

As of today, there are  [1000+ programs and packages, with multiple versions](https://www.uppmax.uu.se/resources/software/installed-software/) (**FIX LINK**)
available on all UPPMAX clusters.
Using explicit versions of software is easy to do and improves the *reproducibility of the scripts written*.

To preserve hard disk space, the clusters also have [multiple big databases installed](https://www.uppmax.uu.se/resources/databases/). **FXC LINK**

!!! warning 
    - To access bioinformatics tools, load the **bioinfo-tools** module first.
    

```note
- Bioinformatics tools require loading the “bioinfo-tools” module first.
```

### Some commands

- list all available modules (also bio-informatics if `bioinfo-tools` is loaded)
  - `module avail` or `ml av`

- Search for modules (full name not needed and case insensitive) 
  - `module avail <part of tool name>` or `ml av <part of toolname>`

- Load a module 
  - `module load <module name>` or `ml <module name>`

- Unload a module 
  - `module unload <module name>` or `ml -<module name>`

- List loaded modules 
  - `module list` or `ml`

- Display a brief module-specific help (not available for all modules)
  - `module help <module name>` or `ml help <module name>` 
 
- Search (like `avail`) but otherwise hidden modules (`bioinfo-tools` and Easybuild modules) 
  -  `module spider <part of tool name>` or `ml spider <module name>` 

## Installed software
- You can also find (almost) all installed software at:
    <https://www.uppmax.uu.se/resources/software/installed-software/>

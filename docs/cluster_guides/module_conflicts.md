---
tags:
  - module
  - conflict
  - conflicts
  - solve
  - resolve
  - fix
---

# How can I resolve problems with conflicting modules?

Sometimes you may experience conflicting [modules](../cluster_guides/modules.md).
An example would be that your program finds an incorrect library.
This can be caused by two or more modules providing libraries with the same name.

Since there are a lot of different modules installed at UPPMAX, we have no possibility to test the compatibility of all the modules.

If you get error messages that you think might be because of conflicting modules, you can do the following:

Check what modules you have loaded:

    module list

If you want to remove one module:

    module unload modulename

If you want to remove ALL modules:

    module purge

Then start to load the modules you need, one by one:

    module load modulename

Until you can run your program without errors.

UPPMAX recommends that you only load as many modules as you need for each program, to minimise the risk of having conflicting modules.

# Loading the Tkinter module

The [UPPMAX clusters](uppmax_cluster.md) use [a module system](modules.md)
to allow our users to easily use their favorite tools (with their
favorite version).

However, this does not always work as simple as expected.

Here a process is described when trying to load the `Tkinter` module.

## 1. The problem


We try to get this Python code to work:

```python
import turtle
```

Instead of creating a script, 
we will use `python3 -c "import turtle"` to let Python 
do exactly the same from the command-line.


We already loaded the module one should usually load first:

```
module load bioinfo-tools
```

As this is Python code, we need to load a Python module. We pick to use `python3`:

```
module load python3/3.11.4
```


Upon running the following Python code ...

```
python3 -c "import turtle"
```

... we get the error:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/sw/comp/python3/3.11.4/rackham/lib/python3.11/turtle.py", line 107, in <module>
    import tkinter as TK
  File "/sw/comp/python3/3.11.4/rackham/lib/python3.11/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named '_tkinter'
```

We search the module system for `tkinter` ...

```
module spider tkinter
```

and we get:

```
---------------------------------------------------------------------------------------
  Tkinter:
---------------------------------------------------------------------------------------
    Description:
      Tkinter module, built with the Python buildsystem

     Versions:
        Tkinter/2.7.15-fosscuda-2018b-Python-2.7.15
        Tkinter/3.6.6-intel-2018b-Python-3.6.6
        Tkinter/3.7.2-GCCcore-8.2.0
        Tkinter/3.8.6-GCCcore-10.2.0
        Tkinter/3.9.6-GCCcore-11.2.0

---------------------------------------------------------------------------------------
  For detailed information about a specific "Tkinter" package (including how to load the mo
dules) use the module's full name.
  Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider Tkinter/3.9.6-GCCcore-11.2.0
---------------------------------------------------------------------------------------
```

We load the latest version ...

```
module load Tkinter/3.9.6-GCCcore-11.2.0
```

and we get our error:

```
Lmod has detected the following error:  These module(s) or extension(s) exist
but cannot be loaded as requested: "Tkinter/3.9.6-GCCcore-11.2.0"
   Try: "module spider Tkinter/3.9.6-GCCcore-11.2.0" to see how to load the module(s).
```

## 2. Reading the doc

The error message is helpful by telling us what to do:

```
module spider Tkinter/3.9.6-GCCcore-11.2.0
```

When we run this, we get the following:

```
---------------------------------------------------------------------------------------
  Tkinter: Tkinter/3.9.6-GCCcore-11.2.0
---------------------------------------------------------------------------------------
    Description:
      Tkinter module, built with the Python buildsystem


    You will need to load all module(s) on any one of the lines below before the "Tkinter/3
.9.6-GCCcore-11.2.0" module is available to load.

      ABINIT/8.10.3
      Amber/20
      CDO/1.9.5
      GOTM/5.3-221-gac7ec88d
      MUMPS/5.5.0
      MUMPS/5.5.0-hybrid
      NCL-graphics/6.6.2
      NCO/4.8.1
      NCO/4.9.2
      NCO/4.9.3
      OpenFOAM/6
      OpenFOAM/7
      OpenFOAM/v1912
      PRISMS-PF/2.1.1
      PROJ/8.1.0
      QGIS/3.4.12
      Rosetta/3.7
      Siesta/4.1-MaX-1.0
      Siesta/4.1-b4
      Singular/4.1.2
      WPS/4.1
      WPS/4.3.1
      WRF/4.1.3
      WRF/4.1.3-dm+sm
      WRF/4.1.3-dmpar
      WRF/4.3.0-dm-gcc
      XCrySDen/1.5.60
      XCrySDen/1.6.2
      bioinfo-tools  augustus/3.3.3-CGP
      deal.II/9.1.1-gcc
      deal.II/9.1.1-intel
      ncview/2.1.7
      ncview/2.1.7-intel-2019b
      wrf-python/1.3.1
 
    Help:
      
      Description
      ===========
      Tkinter module, built with the Python buildsystem
      
      
      More information
      ================
       - Homepage: https://python.org/
      
```

We will need to 'load all module(s) on any one of the lines below'.
That is quite a big amount of modules to load!
Loading all modules is even likely to fail, due to version conflicts.

Instead, we need to think.

## 3. Try out a reasonable module

Looking at the list of modules,
we see mostly big complex software tools, such as OpenFOAM and Singularity.
We are looking for a module that seems simple and Python-related.

The first candidate is `wrf-python/1.3.1`. Let's try it:

```
module load wrf-python/1.3.1
```

This works fine! We are notified that some versions are changed.

???- question "How does that look like?"

	```
    The following have been reloaded with a version change:
      1) GCCcore/11.2.0 => GCCcore/7.3.0
      2) GMP/6.2.1-GCCcore-11.2.0 => GMP/6.1.2-GCCcore-7.3.0
      3) Python/3.9.6-GCCcore-11.2.0 => Python/3.6.6-intel-2018b
      4) SQLite/3.36-GCCcore-11.2.0 => SQLite/3.24.0-GCCcore-7.3.0
      5) Tcl/8.6.11-GCCcore-11.2.0 => Tcl/8.6.8-GCCcore-7.3.0
      6) Tk/8.6.11-GCCcore-11.2.0 => Tk/8.6.8-GCCcore-7.3.0
      7) Tkinter/3.9.6-GCCcore-11.2.0 => Tkinter/3.6.6-intel-2018b-Python-3.6.6
      8) X11/20210802-GCCcore-11.2.0 => X11/20180604-GCCcore-7.3.0
      9) XZ/5.2.5-GCCcore-11.2.0 => XZ/5.2.4-GCCcore-7.3.0
     10) binutils/2.37-GCCcore-11.2.0 => binutils/2.30-GCCcore-7.3.0
     11) bzip2/1.0.8-GCCcore-11.2.0 => bzip2/1.0.6-GCCcore-7.3.0
     12) expat/2.4.1-GCCcore-11.2.0 => expat/2.2.5-GCCcore-7.3.0
     13) fontconfig/2.13.94-GCCcore-11.2.0 => fontconfig/2.13.0-GCCcore-7.3.0
     14) freetype/2.11.0-GCCcore-11.2.0 => freetype/2.9.1-GCCcore-7.3.0
     15) libffi/3.4.2-GCCcore-11.2.0 => libffi/3.2.1-GCCcore-7.3.0
     16) libpng/1.6.37-GCCcore-11.2.0 => libpng/1.6.34-GCCcore-7.3.0
     17) libreadline/8.1-GCCcore-11.2.0 => libreadline/7.0-GCCcore-7.3.0
     18) ncurses/6.2-GCCcore-11.2.0 => ncurses/6.1-GCCcore-7.3.0
     19) util-linux/2.37-GCCcore-11.2.0 => util-linux/2.32-GCCcore-7.3.0
     20) zlib/1.2.11-GCCcore-11.2.0 => zlib/1.2.11-GCCcore-7.3.0
    ```

Now we try out again:

```
module load Tkinter/3.9.6-GCCcore-11.2.0
```

This works fine again! We are notified that some versions are changed.

???- question "How does that look like?"

    ```
    The following have been reloaded with a version change:
      1) GCCcore/7.3.0 => GCCcore/11.2.0
      2) GMP/6.1.2-GCCcore-7.3.0 => GMP/6.2.1-GCCcore-11.2.0
      3) Python/3.6.6-intel-2018b => Python/3.9.6-GCCcore-11.2.0
      4) SQLite/3.24.0-GCCcore-7.3.0 => SQLite/3.36-GCCcore-11.2.0
      5) Tcl/8.6.8-GCCcore-7.3.0 => Tcl/8.6.11-GCCcore-11.2.0
      6) Tk/8.6.8-GCCcore-7.3.0 => Tk/8.6.11-GCCcore-11.2.0
      7) Tkinter/3.6.6-intel-2018b-Python-3.6.6 => Tkinter/3.9.6-GCCcore-11.2.0
      8) X11/20180604-GCCcore-7.3.0 => X11/20210802-GCCcore-11.2.0
      9) XZ/5.2.4-GCCcore-7.3.0 => XZ/5.2.5-GCCcore-11.2.0
     10) binutils/2.30-GCCcore-7.3.0 => binutils/2.37-GCCcore-11.2.0
     11) bzip2/1.0.6-GCCcore-7.3.0 => bzip2/1.0.8-GCCcore-11.2.0
     12) expat/2.2.5-GCCcore-7.3.0 => expat/2.4.1-GCCcore-11.2.0
     13) fontconfig/2.13.0-GCCcore-7.3.0 => fontconfig/2.13.94-GCCcore-11.2.0
     14) freetype/2.9.1-GCCcore-7.3.0 => freetype/2.11.0-GCCcore-11.2.0
     15) libffi/3.2.1-GCCcore-7.3.0 => libffi/3.4.2-GCCcore-11.2.0
     16) libpng/1.6.34-GCCcore-7.3.0 => libpng/1.6.37-GCCcore-11.2.0
     17) libreadline/7.0-GCCcore-7.3.0 => libreadline/8.1-GCCcore-11.2.0
     18) ncurses/6.1-GCCcore-7.3.0 => ncurses/6.2-GCCcore-11.2.0
     19) util-linux/2.32-GCCcore-7.3.0 => util-linux/2.37-GCCcore-11.2.0
     20) zlib/1.2.11-GCCcore-7.3.0 => zlib/1.2.11-GCCcore-11.2.0
    ```

To see if it work, we run the Python code again:

```
python3 -c "import turtle"
```

This works!

We have now discovered how to load the Tkinter module successfully.

???- question "What is the solution as a one-liner?"

    The solution as a one-liner:

    ```
    module load bioinfo-tools python3/3.11.4 wrf-python/1.3.1 Tkinter/3.9.6-GCCcore-11.2.0; python3 -c "import turtle"
    ```

???- question "Which versions are used in the end?"

    Use `module list` to see which versions are used in the end:

    ```
    Currently Loaded Modules:
      1) uppmax
      2) bioinfo-tools
      3) python3/3.11.4
      4) icc/2018.3.222-GCC-7.3.0-2.30
      5) ifort/2018.3.222-GCC-7.3.0-2.30
      6) iccifort/2018.3.222-GCC-7.3.0-2.30
      7) impi/2018.3.222-iccifort-2018.3.222-GCC-7.3.0-2.30
      8) iimpi/2018b
      9) imkl/2018.3.222-iimpi-2018b
     10) intel/2018b
     11) cURL/7.60.0-GCCcore-7.3.0
     12) cftime/1.0.1-intel-2018b-Python-3.6.6
     13) Szip/2.1.1-GCCcore-7.3.0
     14) HDF5/1.10.2-intel-2018b
     15) netCDF/4.6.1-intel-2018b
     16) netcdf4-python/1.4.1-intel-2018b-Python-3.6.6
     17) xarray/0.12.1-intel-2018b-Python-3.6.6
     18) matplotlib/3.0.0-intel-2018b-Python-3.6.6
     19) GEOS/3.6.2-intel-2018b-Python-3.6.6
     20) NASM/2.13.03-GCCcore-7.3.0
     21) libjpeg-turbo/2.0.0-GCCcore-7.3.0
     22) LibTIFF/4.0.9-intel-2018b
     23) Pillow/5.3.0-intel-2018b-Python-3.6.6
     24) basemap/1.2.0-intel-2018b-Python-3.6.6
     25) PROJ/5.0.0-intel-2018b
     26) wrf-python/1.3.1-intel-2018b-Python-3.6.6
     27) GCCcore/11.2.0
     28) zlib/1.2.11-GCCcore-11.2.0
     29) binutils/2.37-GCCcore-11.2.0
     30) bzip2/1.0.8-GCCcore-11.2.0
     31) ncurses/6.2-GCCcore-11.2.0
     32) libreadline/8.1-GCCcore-11.2.0
     33) Tcl/8.6.11-GCCcore-11.2.0
     34) SQLite/3.36-GCCcore-11.2.0
     35) XZ/5.2.5-GCCcore-11.2.0
     36) GMP/6.2.1-GCCcore-11.2.0
     37) libffi/3.4.2-GCCcore-11.2.0
     38) OpenSSL/1.1
     39) Python/3.9.6-GCCcore-11.2.0
     40) expat/2.4.1-GCCcore-11.2.0
     41) libpng/1.6.37-GCCcore-11.2.0
     42) Brotli/1.0.9-GCCcore-11.2.0
     43) freetype/2.11.0-GCCcore-11.2.0
     44) util-linux/2.37-GCCcore-11.2.0
     45) fontconfig/2.13.94-GCCcore-11.2.0
     46) xorg-macros/1.19.3-GCCcore-11.2.0
     47) libpciaccess/0.16-GCCcore-11.2.0
     48) X11/20210802-GCCcore-11.2.0
     49) Tk/8.6.11-GCCcore-11.2.0
     50) Tkinter/3.9.6-GCCcore-11.2.0
    ```

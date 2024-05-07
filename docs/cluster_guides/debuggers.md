# Debuggers

There are debugging tools provided with each [compiler](compilers.md).

For C, C++, and Fortran programs the ordinary gnu debugger (gdb) works fine, 
but for Fortran90/95 programs using gdb doesn't work well. 

### The GNU debugger

The GNU debugger, gdb is provided with the GNU compilers. It works fine for C, C++ and Fortran. With older versions there were problems with fortran90/95.

Read more at the GNU debugger homepage.

In order to use gdb do the following.
load a recent gcc module and a gdb module (system gdb is from 2013!). 

$ module load gcc/10.3.0 gdb/11.2
compile your program with flags for debugging added, e.g. -ggdb

$ gcc -ggdb your-program.c -o your-program
run the gdb program:

$ gdb your-program
Then you can use the gdb commands, like run, break, step, help, ...

Exit with <Ctrl-D>.

### The intel debugger

The intel debugger, idb was provided with the intel compiler. Now it is deprecated and you are advised to use gdb (see above) here as well. 

In order to use gdb with intel do the following.
load the icc module

$ module load intel/20.4
compile your program with flags for debugging added, e.g. -g

$ icc -g your-program.c -o your-program
run the gdb program:

$ gdb your-program
Then you can use the gdb commands, like run, break, step, help, ...

Exit with <Ctrl-D>.

# Debuggers and profiling tools
https://www.uppmax.uu.se/support/user-guides/debuggers-and-profiling-tools/

Compilers supported at UPPMAX
UPPMAX supports two kind of compilers:

GNU project compilers
Intel compilers
This tutorial will show how to use the tools provided with the compilers and some other profiling tools. Since all these tools is strongly connected to the compiler they come with, it is recommended to only have that compiler module loaded.

To make sure that you don't have any other compiler loaded, learn from this example:

$ module list
Currently Loaded Modulefiles:
  1)  uppmax    2) intel/19.5
$ module unload intel
Debugging tools
There are debugging tools provided with each of the three compilers.

For C, C++, and Fortran programs the ordinary gnu debugger (gdb) works fine, but for Fortran90/95 programs using gdb doesn't work well. 

The GNU debugger
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

The intel debugger
The intel debugger, idb was provided with the intel compiler. Now it is depracated and you are advised to use gdb (see above) here as well. 

In order to use gdb with intel do the following.
load the icc module

$ module load intel/20.4
compile your program with flags for debugging added, e.g. -g

$ icc -g your-program.c -o your-program
run the gdb program:

$ gdb your-program
Then you can use the gdb commands, like run, break, step, help, ...

Exit with <Ctrl-D>.

Profiling tools
There are some profiling tools that are available at UPPMAX. Note: some profiling works best without optimization, i.e using the -O0 flag.

Intel VTune Profiler and Advisor
Intel's performance analysis suite can probably answer any question you have about the performance of your code, including MPI and OpenMP code.

VTune is focused choosing optimising techniques that will yield good results, whereas Amplifier is more broadly aimed at performance analysis.

Read more at the Vtune documentation and Advisor documentation.

In order to use VTune do the following:

$ module load intel intel-oneapi vtune

Making sure you have a graphical connection through X or ThinLinc, run VTune graphically:

$ vtune-gui
In order to use Advisor, do the following:

$ module load intel intel-oneapi advisor
Making sure you have a graphical connection through X or ThinLinc, run Advisor graphically:

$ advixe-gui
The GNU profiler
The GNU profiler, gprof is provided with the GNU compiler package.

Read more in the GNU gprof documentation.

In order to use gprof do the following.
Load a recent gcc module and a recent binutils module:

$ module load gcc
$ module load binutils
Compile your program with the -pg -g flags added

$ gcc -O0 -pg -g your-program.c -o your-program
run it:

$ ./your-program
then do:

$ gprof your-program gmon.out > output-file
For more options you run gprof like this:

gprof options [executable-file [profile-data-files…]] [> outfile]
Valgrind
Valgrind is a suite of simulation-based debugging and profiling tools for programs.
Valgrind contains several tools:

memcheck, for detecting memory-management problems in your program
cachegrind, for cache profiling
helgrind, finds data races in multithreded programs
callgrind, a call graph profiler
drd, a thread error detector
massif, a heap profiler
ptrcheck, a pointer checking tool
lackey, a simple profiler and memory tracer
You can find full documentation on valgrind in the Valgrind user manual. 

Valgrind works best with the gcc- and intel compilers. There is a system valgrid-3.15.0 (2020)

First load compiler:

$ module load gcc 
or

$ module load intel 
then you can use valgind by:

$ valgrind [options] ./your-program [your programs options]
How to use valgrind with mpi programs

Load your complier, openmpi and the valgrind module as before:


$ module load gcc/10.3.0 openmpi/3.1.6
or 

      $ module load intel/20.4 openmpi/3.1.6
As of now, Valgrind seems not compatible with openmpi/4.X.X.

Then run:

$ LD_PRELOAD=$VALGRIND_MPI_WRAPPER
$ mpirun -np 2 valgrind ./your-program

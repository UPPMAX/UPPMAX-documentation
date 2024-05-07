# Profilers

There are some profiling tools that are available at UPPMAX. 
Note: some profiling works best without optimization, i.e using the -O0 flag.

## Intel VTune Profiler and Advisor

Intel's performance analysis suite can probably answer any question you have about the performance of your code, including MPI and OpenMP code.

VTune is focused choosing optimizing techniques that will yield good results, whereas Amplifier is more broadly aimed at performance analysis.

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


### Valgrind

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

Valgrind works best with the gcc- and intel compilers. There is a system valgrind-3.15.0 (2020)

First load compiler:

$ module load gcc 
or

$ module load intel 
then you can use valgrind by:

$ valgrind [options] ./your-program [your programs options]
How to use valgrind with mpi programs

Load your compiler, openmpi and the valgrind module as before:


$ module load gcc/10.3.0 openmpi/3.1.6
or 

      $ module load intel/20.4 openmpi/3.1.6
As of now, Valgrind seems not compatible with openmpi/4.X.X.

Then run:

$ LD_PRELOAD=$VALGRIND_MPI_WRAPPER
$ mpirun -np 2 valgrind ./your-program

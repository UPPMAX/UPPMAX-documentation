#MPI and OpenMP user guide

Table of contents:

    Compiling and running parallel programs on UPPMAX clusters.
        Introduction
    Overview of available compilers from GCC and Intel and compatible MPI libraries
    Serial programs on the login node
        Fortran programs
        C programs
        Java programs
    Running serial programs on execution nodes
    MPI using the OpenMPI library
        C programs
        Fortran programs
    OpenMP
        C programs
        Fortran programs
    Pthreads

This is a short tutorial about how to use the queuing system, and how to compile and run MPI and OpenMP jobs.

For serial programs, see a short version of this page at Compiling source code.
Compiling and running parallel programs on UPPMAX clusters.
Introduction

These notes show by brief examples how to compile and run serial and parallel programs on the clusters at UPPMAX.

Section 1 show how to compile and run serial programs, written in fortran, c, or java, on the login nodes. Things work very much like on any unix system, but the subsections on c and java also demonstrate the use of modules.

Section 2 show how to run serial programs on the execution nodes by submitting them as batch jobs to the queue system SLURM.

Section 3 demonstrate parallel message passing programs in c, using the MPI system.

Section 4 demonstrate threaded programs in c using OpenMP directives. These programs must be executed on processors on the same node, since the threads have common memory areas.

Section 5, finally, demonstrate threaded programs usinig pthreads instead of OpenMP.

All programs are of the trivial "hello, world" type. The point is to demonstrate how to compile and execute the programs, not how to write parallel programs.
Overview of available compilers from GCC and Intel and compatible MPI libraries

    GCC
        v5: gcc/5.3.0 openmpi/1.10.3
        v6: gcc/6.3.0 openmpi/2.1.0
        v7: gcc/7.4.0 openmpi/3.1.3
        v8: gcc/8.3.0 openmpi/3.1.3
        v9: gcc/9.3.0 openmpi/3.1.3
        v10: gcc/10.3.0 openmpi/3.1.6 or openmpi/4.1.0 (latest available versions for Bianca)
        v11: gcc/11.2.0 openmpi/4.1.1
        v12: gcc/12.2.0 openmpi/4.1.4
        v13: gcc/13.2.0 openmpi/4.1.5

    Intel & openmpi
        v18: intel/18.3 openmpi/3.1.3
        v20: intel/20.4 openmpi/3.1.6 or openmpi/4.0.4

Note that Bianca does not have the latest combinations of GCC and OPENMPI but only up to gcc/10.3.0 openmpi/4.1.0.
Also note that on Bianca GCC must be loaded on its own line, before loading the openmpi module.

By default, for Open MPI 4.0 and later, infiniband ports on a device
are not used by default.  The intent is to use UCX for these devices.
You can override this policy by setting the btl_openib_allow_ib MCA parameter
to true.

 

Do this by the line below in your batch script or in your interactive environment

export OMPI_MCA_btl_openib_allow_ib=1

Serial programs on the login node
Fortran programs

Enter the following fortran program and save in the file hello.f

C     HELLO.F :  PRINT MESSAGE ON SCREEN
      PROGRAM HELLO
      WRITE(*,*) "hello, world";
      END 

To compile this you should decide on which compilers to use. At UPPMAX there are two different Fortran compilers installed gcc (gfortran) and Intel (ifort).

For this example we will use Gnu Compiler Collection (gcc) compilers installed on UPPMAX, so the gfortran command can be used to compile fortran code. The GFortran compiler is fully compliant with the Fortran 95 Standard and includes legacy F77 support. In addition, a significant number of Fortran 2003 and Fortran 2008 features are implemented. Fortran2008 and Fortran2018 has full support from gcc/9.

A module must first be loaded to use the compilers. You can check what is available and then load a specific version. Choose one recent or one you know will work for your needs.

$ module avail gcc

$ module load gcc/10.3.0

To compile, enter the command:

$ gfortran -o hello hello.f

to run, enter:

$ ./hello
hello, world

To compile with good optimization you can use the "-Ofast" flag to the compiler, but be a bit careful with the -Ofast flag, since sometimes the compiler is a bit overenthusiastic in the optimization and this is especially true if your code contains programming errors (which if you are responsible for the code ought to fix, but if this is someone elses code your options are often more limited). Should -Ofast not work for your code you may try with -O3 instead.

Intel oneAPI collection (intel) compilers are installed on UPPMAX, so the ifort command can be used to compile fortran code. The ifort compiler is fully compliant with the Fortran 95 Standard and includes legacy F77 support. In addition, a significant number of Fortran 2003 and Fortran 2008 features are implemented. Fortran2008 has full support from intel/18. Fortran2018 has full support from intel/19+.

If you want to use Intel, check what is available and choose one recent or one you know will work for your needs.

For Intel versions up to 20.4 you do as follows:

$ module avail intel

$ module load intel/20.4

To compile, enter the command:

$ ifort -o hello hello.f

For Intel versions from year 2021, do like this instead:

$ module load intel-oneapi compiler

$ module av compiler 

Choose the version you need, like 

$ module load compiler/2023.1.0 

To compile, enter the command:

$ ifx -o hello hello.f

to run, enter:

$ ./hello
hello, world

C programs

Enter the following c program and save in the file hello.c

/* hello.c :  print message on screen */
#include <stdio.h>
int main()
{
    printf("hello, world\n");
    return 0;
} 

To compile using gcc installed with the system (4.8.5, 2015) and with no optimization, use the gcc command.

$ gcc -o hello hello.c

To use a newer version of ggc we load a module:

$ module load gcc/10.3.0

$ gcc -o hello hello.c

with basic optimization:

$ gcc -O3 -o hello hello.c

c11 standard has full support from gcc/4.8, c17 standard (bug-fix) from gcc/8.

To use the intel compiler, first load the intel module:

$ module load intel/20.4

or for newer Intel versions (2021-, see above):

$ module load intel-oneapi compiler

$ module load compiler/2023.1.0 

and then compile with the command icc, or icx:

$ icc -o hello hello.c

or for newer versions:

$ icx -o hello hello.c

To run, enter:

$ ./hello
hello, world

c11 and c17 (bug fix) standards have support from intel/17+ (fully from 19).
Java programs

Enter the following java program and save in the file hello.java

/* hello.java :  print message on screen */
class hello {
public static void main(String[] args)
{
     System.out.println("hello, world");
}
}

Before compiling a java program, the module java has to be loaded.
To load the java module, enter the command:

$ module load java

To check that the java module is loaded, use the command:

$ module list

To compile, enter the command:

$ javac hello.java

The java module is not always needed to run the program.
To verify this, unload the java module:

$ module unload java

to run, enter:

$ java hello
hello, world

Running serial programs on execution nodes

Jobs are submitted to execution nodes through the resource manager.
We use SLURM on our clusters. 

To run the serial program hello as a batch job using SLURM, enter the following shell script in the file hello.sh:

#!/bin/bash -l
# hello.sh :  execute hello serially in SLURM
# command: $ sbatch hello.sh
# sbatch options use the sentinel #SBATCH
# You must specify a project
#SBATCH -A your_project_name
#SBATCH -J serialtest
# Put all output in the file hello.out
#SBATCH -o hello.out
# request 5 seconds of run time
#SBATCH -t 0:0:5
# request one core
#SBATCH -p core -n 1
./hello

The last line in the script is the command used to start the program.

Submit the job to the batch queue:

$ sbatch hello.sh

The program's output to stdout is saved in the file named at the -o flag.

$ cat hello.out
hello, world

MPI using the OpenMPI library

Before compiling a program for MPI we must choose, in addition to the compiler, which version of MPI we want to use. At UPPMAX there are two, openmpi and intelmpi. These, with their versions, are compatible only to a subset of the gcc and intel compiler versions. The lists below summarise the best choices.

    GCC
        v5: gcc/5.3.0 openmpi/1.10.3
        v6: gcc/6.3.0 openmpi/2.1.0
        v7: gcc/7.4.0 openmpi/3.1.3
        v8: gcc/8.3.0 openmpi/3.1.3
        v9: gcc/9.3.0 openmpi/3.1.3
        v10: gcc/10.3.0 openmpi/3.1.6 or openmpi/4.1.0
        v11: gcc/11.2.0 openmpi/4.1.1 (will work on Miarka)
        v12: gcc/12.2.0 openmpi/4.1.4
        v13: gcc/13.2.0 openmpi/4.1.5

    Intel & openmpi
        v18: intel/18.3 openmpi/3.1.3
        v20: intel/20.4 openmpi/3.1.6 or openmpi/4.0.4
    Intel & intelmpi
        load the corresponding version of intelmpi as of the intel compiler (versions up to 20.4)
        For all versions of intel from 2021 there is not necessarily a mpi library with same version as the compiler.

            $ module load intel-oneapi 

            check availability and load desired version
            $ module avail mpi  # showing both compilers and mpi ;-)
            Example:
            $ module load compiler/2023.1.0 mpi/2021.9.0 

Check this compatibility page for a more complete picture of compatible versions.

By default, for Open MPI 4.0 and later, infiniband ports on a device
are not used by default.  The intent is to use UCX for these devices.
You can override this policy by setting the btl_openib_allow_ib MCA parameter
to true.

Do this by the line below in your batch script or in your interactive environment

export OMPI_MCA_btl_openib_allow_ib=1

C programs

Enter the following mpi program in c and save in the file hello.c

/* hello.c :  mpi program in c printing a message from each process */
#include <stdio.h>
#include <mpi.h>
int main(int argc, char *argv[])
{
    int npes, myrank;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &npes);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    printf("From process %d out of %d, Hello World!\n", myrank, npes);
    MPI_Finalize();
    return 0;
}

Before compiling a program for MPI we must choose which version of MPI. At UPPMAX there are two, openmpi and intelmpi. For this example we will use openmpi.
To load the openmpi module, enter the command below or choose other versions according to the lists above.

$ module load gcc/10.3.0 openmpi/3.1.6

To check that the openmpi modules is loaded, use the command:

$ module list

The command to compile a c program for mpi is mpicc. Which compiler is used when this command is issued depends on what compiler module was loaded before openmpi

To compile, enter the command:

$ mpicc -o hello hello.c

You should add optimization and other flags to the mpicc command, just as you would to the compiler used. So if the gcc compiler is used and you wish to compile an mpi program written in C with good, fast optimization you should use a command similar to the following:

$ mpicc -fast -o hello hello.c

To run the mpi program hello using the batch system:

#!/bin/bash -l
# hello.sh :  execute parallel mpi program hello on slurm
# use openmpi
# command: $ sbatch hello.sh
# slurm options use the sentinel #SBATCH
#SBATCH -A your_project_name
#SBATCH -J mpitest
#SBATCH -o hello.out
# 
# request 5 seconds of run time
#SBATCH -t 00:00:05
#SBATCH -p node -n 8
module load gcc/10.3 openmpi/3.1.3
mpirun ./hello

The last line in the script is the command used to start the program.
The last word on the last line is the program name hello.

Submit the job to the batch queue:

$ sbatch hello.sh

The program's output to stdout is saved in the file named at the -o flag.
A test run of the above program yelds the following output file:

$ cat hello.out
From process 4 out of 8, Hello World!
From process 5 out of 8, Hello World!
From process 2 out of 8, Hello World!
From process 7 out of 8, Hello World!
From process 6 out of 8, Hello World!
From process 3 out of 8, Hello World!
From process 1 out of 8, Hello World!
From process 0 out of 8, Hello World! 

Fortran programs

The following example program does numerical integration to find Pi (inefficiently, but it is just an example):

program testampi
    implicit none
    include 'mpif.h'
    double precision :: h,x0,x1,v0,v1
    double precision :: a,amaster
    integer :: i,intlen,rank,size,ierr,istart,iend
    call MPI_Init(ierr)
    call MPI_Comm_size(MPI_COMM_WORLD,size,ierr)
    call MPI_Comm_rank(MPI_COMM_WORLD,rank,ierr)
    intlen=100000000
    write (*,*) 'I am node ',rank+1,' out of ',size,' nodes.'
 
    h=1.d0/intlen
    istart=(intlen-1)*rank/size
    iend=(intlen-1)*(rank+1)/size
    write (*,*) 'start is ', istart
    write (*,*) 'end is ', iend
    a=0.d0
    do i=istart,iend
           x0=i*h
           x1=(i+1)*h
           v0=sqrt(1.d0-x0*x0)
           v1=sqrt(1.d0-x1*x1)
           a=a+0.5*(v0+v1)*h
    enddo
    write (*,*) 'Result from node ',rank+1,' is ',a
    call MPI_Reduce(a,amaster,1, &
             MPI_DOUBLE_PRECISION,MPI_SUM,0,MPI_COMM_WORLD,ierr)
    if (rank.eq.0) then
           write (*,*) 'Result of integration is ',amaster
           write (*,*) 'Estimate of Pi is ',amaster*4.d0
    endif
    call MPI_Finalize(ierr)
    stop
end program testampi

The program can be compiled by this procedure, using mpif90:

$ module load intel/20.4 openmpi/3.1.6
$ mpif90 -Ofast -o testampi testampi.f90

The program can be run by creating a submit script sub.sh:

#!/bin/bash -l
# execute parallel mpi program in slurm
# command: $ sbatch sub.sh
# slurm options use the sentinel #SBATCH
#SBATCH -J mpitest
#SBATCH -A your_project_name
#SBATCH -o pi
#
# request 5 seconds of run time
#SBATCH -t 00:00:05
#
#SBATCH -p node -n 8
module load intel/20.4 openmpi/3.1.6

mpirun ./testampi

Submit it:

sbatch sub.sh

Output from the program on Rackham:

I am node             8  out of             8  nodes.
start is      87499999
end is      99999999
I am node             3  out of             8  nodes.
start is      24999999
end is      37499999
I am node             5  out of             8  nodes.
start is      49999999
end is      62499999
I am node             2  out of             8  nodes.
start is      12499999
end is      24999999
I am node             7  out of             8  nodes.
start is      74999999
end is      87499999
I am node             6  out of             8  nodes.
start is      62499999
end is      74999999
I am node             1  out of             8  nodes.
start is             0
end is      12499999
I am node             4  out of             8  nodes.
start is      37499999
end is      49999999
Result from node             8  is    4.0876483237300587E-002
Result from node             5  is    0.1032052706959522     
Result from node             2  is    0.1226971551244773     
Result from node             3  is    0.1186446918315650     
Result from node             7  is    7.2451466712425514E-002
Result from node             6  is    9.0559231928350928E-002
Result from node             1  is    0.1246737119371059     
Result from node             4  is    0.1122902087263801     
Result of integration is    0.7853982201935574     
Estimate of Pi is     3.141592880774230     

OpenMP

OpenMP uses threads that use shared memory. OpenMP is supported by both the gcc and intel compilers and in the c/c++ and Fortran languages. Don't mix with OpenMPI whis is an open source library for MPI. OpenMP is built in in all modern compiler libraries.

Depending on your preferences load the chosen compiler:

$ module load gcc/12.1.0

or

$ module load intel/20.4

C programs

Enter the following openmp program in c and save in the file hello_omp.c

/* hello.c :  openmp program in c printing a message from each thread */
#include <stdio.h>
#include <omp.h>
int main()
{
      int nthreads, tid;
      #pragma omp parallel private(nthreads, tid)
      {
            nthreads = omp_get_num_threads();
            tid = omp_get_thread_num();
           printf("From thread %d out of %d, hello, world\n", tid, nthreads);
    }
    return 0;
}

To compile, enter the command (note the -fopenmp or -qopenmp flag depending on compiler):

$ gcc -fopenmp -o hello_omp hello_omp.c

or

$ icc qfopenmp -o hello_omp hello_omp.c

Also here you should add optimization flags such as -fast as appropriate.

To run the openMP program hello using the batch system, enter the following shell script in the file hello.sh:

#!/bin/bash -l
# hello.sh :  execute parallel openmp program hello on slurm
# use openmp
# command: $ sbatch hello.sh
# slurm options use the sentinel #SBATCH
#SBATCH -J omptest
#SBATCH -A your_project_name
#SBATCH -o hello.out
#
# request 5 seconds of run time
#SBATCH -t 00:00:05
#SBATCH -p node -n 8
uname -n
#Tell the openmp program to use 8 threads
export OMP_NUM_THREADS=8
module load intel/20.4
# or gcc...
ulimit -s  $STACKLIMIT
./hello_omp

The last line in the script is the command used to start the program.

Submit the job to the batch queue:

$ sbatch hello.sh

The program's output to stdout is saved in the file named at the -o flag.
A test run of the above program yelds the following output file:

$ cat hello.out
r483.uppmax.uu.se
unlimited
From thread 0 out of 8, hello, world
From thread 1 out of 8, hello, world
From thread 2 out of 8, hello, world
From thread 3 out of 8, hello, world
From thread 4 out of 8, hello, world
From thread 6 out of 8, hello, world
From thread 7 out of 8, hello, world
From thread 5 out of 8, hello, world

Fortran programs

Enter the following openmp program in Fortran and save in the file hello_omp.f90

PROGRAM HELLO
INTEGER NTHREADS, TID, OMP_GET_NUM_THREADS, OMP_GET_THREAD_NUM
! Fork a team of threads giving them their own copies of variables
!$OMP PARALLEL PRIVATE(NTHREADS, TID)
! Obtain thread number
TID = OMP_GET_THREAD_NUM()
PRINT *, 'Hello World from thread = ', TID
! Only master thread does this
IF (TID .EQ. 0) THEN
 NTHREADS = OMP_GET_NUM_THREADS()
PRINT *, 'Number of threads = ', NTHREADS
END IF
! All threads join master thread and disband
!$OMP END PARALLEL
END

With gcc compiler: 

$ gfortran hello_omp.f90 -o hello_omp -fopenmp

and with Intel compiler: 

$ ifort hello_omp.f90 -o hello_omp -qopenmp

Run with:

$ ./hello_omp

Hello World from thread =            1
 Hello World from thread =            2
 Hello World from thread =            0
 Hello World from thread =            3
 Number of threads =            4

A batch file would look similar to the C version, above. 

Pthreads

Pthreads (Posix threads) are more low-level than openMP. That means that for a beginner it is easier to get rather expected gain only with a few lines with openMP. On the other hand it may be possible to gain more efficiency from your code with pthreads, though with quite some effort. Pthreads is native in c/c++. With additional installation of a POSIX library for Fortran it is possible to run it in there as well.

Enter the following program in c and save in the file hello_pthreads.c

/* hello.c :  create system pthreads and print a message from each thread */
#include <stdio.h>
#include <pthread.h>
// does not work for setting array length of "tid": const int NTHR = 8;
// Instead use "#define"
#define NTHR 8
int nt = NTHR, tid[NTHR];
pthread_attr_t attr;
void *hello(void *id)
{
     printf("From thread %d out of %d: hello, world\n", *((int *) id), nt);
     pthread_exit(0);
}
int main()
{
    int i, arg1;
    pthread_t thread[NTHR];
    /* system threads */
    pthread_attr_init(&attr);
    pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);
    /* create threads */
    for (i = 0; i < nt; i++) {
          tid[i] = i;
          pthread_create(&thread[i], &attr, hello, (void *) &tid[i]);
     }
    /* wait for threads to complete */
    for (i = 0; i < nt; i++)
            pthread_join(thread[i], NULL);
      return 0;
}

To compile, enter the commands

$ module load gcc/10.2.0
$ gcc -pthread -o hello_pthread hello_pthread.c

To run the pthread program hello using the batch system, enter the following shell script in the file hello.sh:

#!/bin/bash -l
# hello.sh :  execute parallel pthreaded program hello on slurm
# command: $ sbatch hello.sh
# slurm options use the sentinel #SBATCH
#SBATCH -J pthread
#SBATCH -A your_project_name
#SBATCH -o hello.out
#
# request 5 seconds of run time
#SBATCH -t 00:00:05
# use openmp programming environment
# to ensure all processors on the same node
#SBATCH -p node -n 8
uname -n
./hello_pthread

The last line in the script is the command used to start the program.
Submit the job to the batch queue:

$ sbatch hello.sh

The program's output to stdout is saved in the file named at the -o flag.
A test run of the above program yelds the following output file:

$ cat hello.out
r483.uppmax.uu.se
From thread 0 out of 8: hello, world
From thread 4 out of 8: hello, world
From thread 5 out of 8: hello, world
From thread 6 out of 8: hello, world
From thread 7 out of 8: hello, world
From thread 1 out of 8: hello, world
From thread 2 out of 8: hello, world
From thread 3 out of 8: hello, world

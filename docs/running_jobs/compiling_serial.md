# Compiling serial source code

For parallel programs, see MPI and OpenMP user guide.
## Fortran programs

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

## C programs

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

## Java programs

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


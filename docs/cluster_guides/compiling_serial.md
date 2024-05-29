# Compiling serial source code

For parallel programs, see [MPI and OpenMP user guide](compiling_parallel.md).

## Overview

Language|Compiler                 |Find guide at ...
--------|-------------------------|---------------------
C       |[GCC](../software/gcc.md)|[Compile C using GCC](../software/gcc_compile_c.md).
C       |Intel, `icc`             |[Compile C using icc](../software/icc_compile_c.md)
C       |Intel, `icx`             |[Compile C using icx](../software/icx_compile_c.md)
C++     |[GCC](../software/gcc.md)|[Compile C++ using GCC](../software/gcc_compile_cpp.md)
C++     |Intel, `icpc`            |[Compile C++ using icpc](../software/icpc_compile_cpp.md)
Java    |`javac`                  |[Compile Java using javac](../software/javac_compile_jave.md)
Fortran |GCC                      |See below
Fortran |Intel                    |See below

## Fortran programs

Enter the following fortran program and save in the file hello.f

``` fortran
C     HELLO.F :  PRINT MESSAGE ON SCREEN
      PROGRAM HELLO
      WRITE(*,*) "hello, world";
      END
```

### GCC

- To compile this you should decide on which compilers to use. At UPPMAX there are two different Fortran compilers installed gcc (gfortran) and Intel (ifort).

- For this example we will use Gnu Compiler Collection (gcc) compilers installed on UPPMAX, so the gfortran command can be used to compile fortran code. The GFortran compiler is fully compliant with the Fortran 95 Standard and includes legacy F77 support. In addition, a significant number of Fortran 2003 and Fortran 2008 features are implemented. Fortran2008 and Fortran2018 has full support from gcc/9.

- A module must first be loaded to use the compilers. You can check what is available and then load a specific version. Choose one recent or one you know will work for your needs.

``` console
$ module avail gcc

$ module load gcc/10.3.0
```

To compile, enter the command:

``` console
$ gfortran -o hello hello.f
```

to run, enter:

``` console
$ ./hello
hello, world
```

-To compile with good optimization you can use the "-Ofast" flag to the compiler, but be a bit careful with the -Ofast flag, since sometimes the compiler is a bit overenthusiastic in the optimization and this is especially true if your code contains programming errors (which if you are responsible for the code ought to fix, but if this is someone elses code your options are often more limited). Should -Ofast not work for your code you may try with -O3 instead.

### Intel 

- Intel oneAPI collection (intel) compilers are installed on UPPMAX, so the ifort command can be used to compile fortran code. The ifort compiler is fully compliant with the Fortran 95 Standard and includes legacy F77 support. In addition, a significant number of Fortran 2003 and Fortran 2008 features are implemented. Fortran2008 has full support from intel/18. Fortran2018 has full support from intel/19+.

- If you want to use Intel, check what is available and choose one recent or one you know will work for your needs.

For Intel versions up to 20.4 you do as follows:

``` console
$ module avail intel

$ module load intel/20.4
```

To compile, enter the command:

``` console
$ ifort -o hello hello.f
```

For Intel versions from year 2021, do like this instead:

``` console
$ module load intel-oneapi compiler
$ module av compiler
```

Choose the version you need, like

``` console
$ module load compiler/2023.1.0
```

To compile, enter the command:

``` console
$ ifx -o hello hello.f
```

to run, enter:

``` console
$ ./hello
hello, world
```


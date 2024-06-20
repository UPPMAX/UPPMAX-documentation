# Combinations of parallel libraries and compilers

Before compiling a program for MPI we must choose, in addition to the compiler, which version of MPI we want to use. At UPPMAX there are two, openmpi and intelmpi. These, with their versions, are compatible only to a subset of the gcc and intel compiler versions. The lists below summarise the best choices.

## Suggestions for compatibility Rackham, Snowy, Bianca

### GCC

- v5: gcc/5.3.0 openmpi/1.10.3
- v6: gcc/6.3.0 openmpi/2.1.0
- v7: gcc/7.4.0 openmpi/3.1.3
- v8: gcc/8.3.0 openmpi/3.1.3
- v9: gcc/9.3.0 openmpi/3.1.5
- v10: gcc/10.3.0 openmpi/**3.1.6** or openmpi/**4.1.0**
- v11: gcc/11.2.0 openmpi/4.1.1 **will work also on Miarka**
- v12: gcc/12.2.0 openmpi/4.1.4
- v13: gcc/13.2.0 openmpi/4.1.5

### Intel

- v18: intel/18.3 openmpi/3.1.3
- v20: intel/20.4 openmpi/**3.1.6** or openmpi/**4.0.4**

### Intel & intelmpi

- Load the corresponding version of intelmpi as of the intel compiler (versions up to 20.4)

### Intel after version 20.4

- For all versions of intel from 2021 there is not necessarily a mpi library with same version as the compiler.

```bash
$ module load intel-oneapi
```

- Check availability and load desired version

```bash
$ module avail mpi  # showing both compilers and mpi ;-)
```

- Example:

```bash
$ module load compiler/2023.1.0 mpi/2021.9.0    
```

### Suggestions for compatibility Rackham and Snowy

- GCC
    - v4: gcc/4.8.2 openmpi/1.7.4
    - v5: gcc/5.3.0 openmpi/1.10.3
    - v6: gcc/6.3.0 openmpi/2.1.0
    - v7: gcc/7.4.0 openmpi/3.1.3
    - v8: gcc/8.3.0 openmpi/3.1.3
    - v9: gcc/9.3.0 openmpi/3.1.3 or openmpi/4.0.3
    - v10: gcc/10.3.0 openmpi/**3.1.6*- #or openmpi/**4.1.1**
    - v11: gcc/11.3.0 openmpi/4.1.2
    - v12: gcc/12.2.0 openmpi/4.1.4
    - v13: gcc/13.1.0 openmpi/4.1.5

- Intel
    - v18: intel/18.3 openmpi/3.1.3
    - v20: intel/20.4 openmpi/**3.1.6*- # or openmpi/**4.1.1**

## Rackham

- Also on Snowy in *italic*
- Also on Snowy AND Bianca in ***bold***

GCC  | openmpi
-----| -------
4.8.2  |  *1.7.4*
5.2.0  |  *1.8.8*
5.3.0  |  ***1.10.1***
5.5.0  |  1.10.3
6.3.0  |  ***2.0.1***, 2.0.2, ***2.1.0***
6.4.0  |  2.1.1
7.1.0  |  2.1.0, 2.1.1
7.2.0  |  2.1.1, 2.1.2, 3.0.0
7.3.0  |  2.1.3, 3.0.0, *3.1.0*
7.4.0  |  *3.1.3*
8.1.0  |  3.0.1, 3.1.0
8.2.0  |  3.0.2, 3.1.0, *3.1.1*, ***3.1.2***, ***3.1.3***, 4.0.0
8.3.0  |  ***3.1.3***
8.4.0  |  3.1.5, 4.0.2
9.1.0  |  3.1.3
9.2.0  |  *3.1.3*, *3.1.4*, 3.1.5, 4.0.2
9.3.0  |  ***3.1.5***, *4.0.2*, *4.0.3*
10.1.0 |  ***3.1.6***, *4.0.3*
10.2.0 |  *3.1.6*, *4.0.4*, ***4.1.0***
10.3.0 |  ***3.1.6***, ***4.0.5***, ***4.1.0***, *4.1.1*
11.2.0 |  *4.1.1*, *4.1.2*
11.3.0 |  *4.1.2*, 4.1.3
12.1.0 |  *4.1.3*
12.2.0 |  *4.1.3*, *4.1.4*
12.3.0 |  *4.1.5*
13.1.0 |  *4.1.5*

Intel |   openmpi
----- |   -------
15.3    | 1.10.0, 1.10.1, 2.1.0
16.1    | 1.10.1, 1.10.2
17.1    | 2.0.1, 2.0.2,
17.2    | 2.0.2, 2.1.0
17.4    | 2.1.1, 3.0.0
18.0    | 3.0.0
18.1    | 2.1.2, 2.1.3, 3.0.0
18.2    | 2.1.3, 3.0.0, 3.1.0
18.3    | 3.0.2, 3.1.0, 3.1.1, ***3.1.2***, ***3.1.3***
19.4    | *3.1.4*
19.5    | 3.1.4
20.0    | 3.1.5, 3.1.6, *4.0.3*, 4.0.4
20.2    | ***3.1.6***, ***4.0.4***
20.4    | ***3.1.6***, ***4.0.4***, *4.1.0*, *4.1.1*

openmpi | gcc  | intel | pgi
------- | ---  | ----- | ---
1.7.4 |   4.8.2|
1.8.8 |   5.2.0|
1.10.0 |  | 15.3
1.10.1|   5.3.0|    15.3, 16.1
1.10.2|   |  16.1 |  16.9, 17.4, 17.7, 17.10
1.10.3|   5.5.0|
2.0.1 |   6.3.0  |  17.1
2.0.2 |   6.3.0  |  17.1, 17.2
2.1.0 |   6.3.0, 7.1.0 |   15.3, 17.2
2.1.1 |   6.4.0, 7.1.0, 7.2.0 |  17.4 |   17.4, 17.7
2.1.2 |   7.2.0  |  18.1 |  17.10, 18.1, 18.3
2.1.3 |   |  7.3.0 |                           18.1, 18.2              18.1
3.0.0 |   7.2.0, 7.3.0 |  17.4, 18.0, 18.1, 18.2 |  17.7, 17.10, 18.0 18.1 
3.0.1 |   8.1.0 | 
3.0.2 |   8.2.0  |                          18.3
3.1.0 |   7.3.0, 8.1.0, 8.2.0 | 18.2, 18.3  |   18.3
3.1.1 |   8.2.0  |                          18.3
3.1.2 |   8.2.0  |  18.3 |                    18.3
3.1.3 |   7.4.0, 8.2.0, 8.3.0, 9.1.0, 9.2.0| 18.3 |  18.3
3.1.4 |   9.2.0 |                           19.4, 19.5
3.1.5 |   8.4.0, 9.2.0, 9.3.0 |             20.0
3.1.6 |   10.1.0, 10.2.0, 10.3.0 |          20.0, 20.2, 20.4
4.0.0 |   8.2.0 | 
4.0.2 |   8.4.0, 9.2.0, 9.3.0 | 
4.0.3 |   9.3.0, 10.1.0  |                  20.0
4.0.4 |   10.2 |                            20.0, 20.2, 20.4 
4.0.5 |   10.3.0
4.1.0 |   10.2.0, 10.3.0 |                  20.4
4.1.1 |   10.3.0, 11.2.0 |                  20.4
4.1.2 |   11.2.0
4.1.3 |   12.1.0, 12.2.0
4.1.4 |   12.2.0
4.1.5 |   12.3.0, 13.1.0

## Bianca

GCC  | openmmpi
-----| -------- 
5.3.0| 1.10.1
5.4.0| 2.0.0, 2.0.1
6.1.0| 2.0.0, 2.0.1
6.2.0| 2.0.1
6.3.0| 2.0.1, 2.0.2, 2.1.0
6.4.0| 2.1.1
7.1.0| 2.1.0, 2.1.1
7.2.0| 2.1.1, 3.0.0
7.3.0| 3.0.0
8.1.0| 3.1.0
8.2.0| 3.1.2, 3.1.3
8.3.0| 3.1.3
9.3.0| 3.1.5
10.1.0| 3.1.6
10.2.0| 4.1.0
10.3.0| 3.1.6, 4.0.5, 4.1.0
11.2.0| 4.1.1

Intel |   openmpi
----- |   -------
15.3    | 1.10.0, 1.10.1
16.1    | 1.10.1, 1.10.2
16.3    | 2.0.0, 2.0.1
17.0    | 2.0.1
17.1    | 2.0.1, 2.0.2
17.2    | 2.0.2, 2.1.0
17.4    | 2.1.1, 3.0.0
18.3    | 3.1.2, 3.1.3
20.2    | 3.1.6, 4.0.4
20.4    | 3.1.6, 4.0.4

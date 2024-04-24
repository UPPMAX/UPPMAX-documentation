GAMESS-US versions 20170930 is installed on Rackham. Newer versions can be installed on request to UPPMAX support. Snowy currently lacks GAMESS-US.

Citing GAMESS papers
It is essential that you read the GAMESS manual thoroughly to properly reference the papers specified in the instructions. All publications using gamess should cite at least the following paper:

@Article{GAMESS,
author={M.W.Schmidt and K.K.Baldridge and J.A.Boatz and S.T.Elbert and
M.S.Gordon and J.J.Jensen and S.Koseki and N.Matsunaga and
K.A.Nguyen and S.Su and T.L.Windus and M.Dupuis and J.A.Montgomery},
journal={J.~Comput.~Chem.},
volume=14,
pages={1347},
year=1993,
comment={The GAMESS program}}
If you need to obtain GAMESS yourself, please visit the GAMESS website for further instructions.

Running GAMESS

Load the module using
module load gamess/20170930

Below is an example submitscript for Rackham, running on 40 cores (2 nodes with 20 cores each). It is essential to specify the project name:

#!/bin/bash -l
#SBATCH -J jobname
#SBATCH -p node -n 40
#SBATCH -A PROJECT
#SBATCH -t 03:00:00
 
module load gamess/20170930
 
rungms gms >gms.out
Memory specification
GAMESS uses two kinds of memory: replicated memory and distributed memory. Both kinds of memory should be given in the $SYSTEM specification. Replicated memory is specified using the MWORDS keyword and distributed memory with the MEMDDI keyword. It is very important that you understand the uses of these keywords. Check the GAMESS documentation for further information.

If your job requires 16MW (mega-words) of replicated memory and 800MW of distributed memory, as in the example below, the memory requirements per CPU core varies as 16+800/N where N is the number of cores. Each word is 8 bytes of memory, why the amount of memory per core is (16+800/N)*8. The amount of memory per node depends on the number of cores per node. Rackham has 20 cores per node, most nodes have 128 GB of memory, but 30 nodes have 512 GB and 4 nodes at 1 TB.


Communication
For intra-node communication shared memory is used. For inter-node communication MPI is used which uses the Infiniband interconnect.

# MOLCAS user guide

> How to run the program MOLCAS on UPPMAX

## Information
MOLCAS is an ab initio computational chemistry program. Focus in the program is placed on methods for calculating general electronic structures in molecular systems in both ground and excited states. MOLCAS is, in particular, designed to study the potential surfaces of excited states

This guide will help you get started running MOLCAS on UPPMAX. More detailed information on how to use Molcas can be found on the [official website](https://molcas.org/).

## Licensing
A valid license key is required to run Molcas on UPPMAX. The licence key should be kept in a directory named .Molcas under the home directory.

Molcas is currently free of charge for academic researchers active in the Nordic countries. You can get hold of a license by following [these instructions](https://www.molcas.org/order.html).

## Versions installed at UPPMAX
At UPPMAX the following versions are installed:

- 8.0 (serial)
- 7.8 (serial)
## Modules needed to run MOLCAS
In order to run MOLCAS you must first load the MOLCAS module. You can see all available versions of MOLCAS installed at UPPMAX with:

```bash
module avail molcas
```
Load a MOLCAS module with, eg:

```bash
module load molcas/7.8.082
```
## How to run MOLCAS interactively
If you would like to do tests or short runs, we recommend using the interactive command:
```bash
interactive -A your_project_name
```
This will reserve a node for you to do your test on. Note that you must provide the name of an active project in order to run on UPPMAX resources. After a short wait you will get access to the node. Then you can run MOLCAS by:
```bash
module load molcas/7.8.082
molcas -f test000.input
```
The `test000.input` looks like:

``` 
*$Revision: 7.7 $
************************************************************************
* Molecule: H2
* Basis: DZ
* Symmetry: x y z
* SCF: conventional
*
*  This is a test to be run during first run to verify
*  that seward and scf works at all
*
 
>export MOLCAS_PRINT=VERBOSE
 &GATEWAY
coord
2
angstrom
H  0.350000000  0.000000000  0.000000000
H -0.350000000  0.000000000  0.000000000
basis
H.DZ....
 
 &SEWARD
 
 &SCF
Title
 H2, DZ Basis set
 
 &RASSCF
Title
 H2, DZ Basis set
nActEl
 2  0 0
Ras2
 1 1 0 0 0 0 0 0
 
 &ALASKA
 
 &SLAPAF
 
 &CASPT2
```
See the [SLURM user guide](../cluster_guides/slurm.md) for more information on the interactive command. Don't forget to exit your interactive job when you have finished your calculation. Exiting will free the resource for others to use.

## Batch scripts for slurm
It's possible to run MOLCAS in the batch queue. Here is an example running MOLCAS on one core:

```sbatch
#!/bin/bash -l
#
#SBATCH -A <em>your_project_name</em>
#SBATCH -J molcastest
#SBATCH -t 00:10:00
#SBATCH -p core -n 1
 
module load molcas/7.8.082
 
#In order to let MOLCAS use more memory
export MOLCASMEM=2000
 
molcas -f test000.input
```
Again you'll have to provide your project name.

If the script is called `test000.job` you can submit it to the batch queue with:
```bash
sbatch test000.job
```

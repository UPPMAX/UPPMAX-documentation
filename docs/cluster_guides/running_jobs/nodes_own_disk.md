# How to use the nodes' own disk

## Short version

When possible, copy the files you want to use in the analysis to $SNIC_TMP at the start of the job, and store all output there as well. The last thing you do in the job is to copy the files you want to keep back to your project direcotry.

## Long version

Parallel network file systems are very fast when accessed from many nodes, but can nevertheless become a bottleneck. For instance, if many jobs on a single are doing many file operations, all those jobs may be fighting each other and degrading performance. Additionally, the metadata server on these kinds of file systems can be overburdened if very large numbers of files are created and/or removed. 

For this reason, jobs that perform a lot of file accesses, especially on temporary files, should use the compute node's local hard drive. If you do, then any slow-down due to file I/O is limited to the node(s) on which these jobs are running. 

The hard drive of the node is located at /scratch, and each job that runs on a node gets a folder created automatically with the same name as the jobid, /scratch/<jobid>.  This folder name is also stored in the environment variable $SNIC_TMP for ease of use. The idea is that you copy files that you will be reading randomly, such as indices and databases but not files of reads, to $SNIC_TMP first thing in the job. Files that you read as a stream from beginning to end, like files of reads, should remain in project storage and read from there.  You then run your analysis and have all the output files written to $SNIC_TMP as well. After the analysis is done, you copy back all the output files you want to keep to your project storage folder. Everything in /scratch/<jobid> will be deleted as soon as the job is finished, and you have no hope of recovering it after the job is completed.

An example would be a script that runs bwa to align read. Usually they look something like this:

``` bash
#!/bin/bash -l
#SBATCH -A snic2022-X-YYY
#SBATCH -t 12:00:00
#SBATCH -p core
#SBATCH -n 20
 
# load modules
module load bioinfo-tools bwa/0.7.17 samtools/1.14
 
# run the alignment and convert its output directly to
# a sorted bam format
bwa mem -t 16 /proj/snic2022-X-YYY/nobackup/ref/hg19.fa /proj/snic2022-X-YYY/rawdata/sample.fq.gz | samtools sort -@ 4 -M 10G -O bam - > /proj/snic2022-X-YYY/nobackup/results/sample.bam
```

The steps to be added are (1) copy the index to $SNIC_TMP but not the reads; (2) adjust your script to read read the index from $SNIC_TMP; and (3) copy the results back to project storage once the alignment is done.

```bash
#!/bin/bash
#SBATCH -A snic2022-X-YYY
#SBATCH -t 12:00:00
#SBATCH -p core
#SBATCH -n 20
 
# load modules
module load bioinfo-tools bwa/0.7.17 samtools/1.14
 
# copy the index files used in the analysis to $SNIC_TMP
cp /proj/snic2022-X-YYY/nobackup/ref/hg19.fa* $SNIC_TMP/
 
# go to the $SNIC_TMP folder to make sure any temporary files
# are created there as well
cd $SNIC_TMP
 
# run the alignment using the index in $SNIC_TMP and the reads
# from project storage. write the sorted BAM containing
# alignments directly to $SNIC_TMP. Use 16 threads for
# alignment and 4 threads for sorting and compression, and
# 20GB RAM for sorting. These values are appropriate for a
# full standard rackham node.
bwa mem -t 16 $SNIC_TMP/hg19.fa /proj/snic2022-X-YYY/rawdata/sample.fq.gz | samtools sort -@ 4 -m 20G -O bam - > $SNIC_TMP/sample.bam
 
# copy the results back to the network file system
cp $SNIC_TMP/sample.bam /proj/snic2022-X-YYY/nobackup/results/
```

It's not harder than that. This way, the index files are copied to $SNIC_TMP in a single operation, which is much less straining for the file system than small random read/writes. The network filesystem is used when gathering reads for alignment, and streaming reads are easy for that filesystem. When the alignment is finished the results is copied back to project directory so that it can be used in other analysis.

One problem that can happen is if your files and the results are too large for the node's hard drive. The drive is 2TiB on Rackham and 4TiB on Bianca, so it is unusual for the hard drive to be too small for the results of such analyses. If you run into this problem, please meail UPPMAX at support@uppmax.uu.se and we can look into the problem.

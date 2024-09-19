# Slurm troubleshooting

When using [Slurm](slurm.md), unexpected things may happen.
This page describes Slurm errors.

## 1. Invalid account or account/partition combination specified

### 1.1. Full error message

```text
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

### 1.2. To reproduce

```bash
touch do_something.sh
echo '#!/bin/bash' >> do_something.sh 
sbatch -A some_invalid_account do_something.sh 
```

### 1.3. Problem

As stated by the error message: you've used either:

- an invalid account (for example, `some_invalid_account` in the example above)
- an invalid combination of account and partition,
  for example using a Rackham account for a Snowy partition

Or, in less formal terms, you are using a NAISS project that is not
an active UPPMAX project for that UPPMAX cluster.

### 1.4. Solution

- [View your NAISS projects](https://docs.uppmax.uu.se/getting_started/project/#view-your-uppmax-projects)
  and see if the project you used is indeed an active UPPMAX project that can
  be used on the cluster you expect
- Use these in your scripts


## 2. Invalid project

### 2.1. Full error message

```text
````

sbatch: error: Errors in job submission:
sbatch: error: ERROR 1: Invalid project.
sbatch: error: Use the flag -A to specify an active project with allocation on this cluster.
sbatch: error: Batch job submission failed: Unspecified error```

### 2.2. To reproduce

```bash
sbatch my_script.sh -A my_project
```

### 2.3. Problem

The order of the arguments is incorrect.
The script to be submitted must be the last argument.

### 2.4. Solution

```bash
sbatch -A my_project my_script.sh
```

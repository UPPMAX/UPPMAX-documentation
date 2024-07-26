# Slurm troubleshooting

When using [Slurm](slurm.md), unexpected things may happen.
This page describes Slurm errors.

## Invalid account or account/partition combination specified

Full error message:

```text
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

To reproduce:

```bash
touch do_something.sh
echo '#!/bin/bash' >> do_something.sh 
sbatch -A some_invalid_account do_something.sh 
```

Problem:

As stated by the error message: you've used either:

- an invalid account (for example, `some_invalid_account` in the example above)
- an invalid combination of account and partition,
  for example using a Rackham account for a Snowy partition

Solution:

- [View your UPPMAX projects](https://docs.uppmax.uu.se/getting_started/project/#view-your-uppmax-projects)
- Use these in your scripts

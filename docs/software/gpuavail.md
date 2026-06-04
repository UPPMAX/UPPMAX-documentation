# `gpuavail`

`gpuavail` is a tool to see GPU availability on the UPPMAX HPC cluster.

On a UPPMAX HPC cluster, on a terminal, run:

```bash
gpuavail
```

It's output would look somewhat like this:

```bash
        GPU Availability
┏━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓
┃ GPU Type ┃ Available ┃ Total ┃
┡━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩
│ h100     │         4 │     4 │
│ l40s     │        18 │    40 │
│ t4       │         2 │    36 │
└──────────┴───────────┴───────┘
```

---
tags:
  - GPU
  - status
  - available
  - gpuavail 
---

# `gpuavail`

`gpuavail` is a tool to see GPU availability on Pelle.
It is not available on Bianca.

On Pelle, on a terminal, run:

```bash
gpuavail
```

Its output will look similar to this:

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

---
tags:
  - scp
  - secure copy protocol
  - program
  - software
  - tool
  - copy
---

# `scp`

The program `scp` allows you to transfer files to/from the UPPMAX HPC clusters
from a [md](terminal.md)

Although `scp` is an abbreviation of 'Secure copy protocol',
it is not considered 'secure' anymore:
instead, it is considered an outdated protocol:
[`rsync`](rsync.md) is a similar tool that is considered secure.

In general, using `scp` to copy files from a certain location to
another location, looks like this:

```bash
scp [from] [to]
```

UPPMAX guides can be found here:

Between          |UPPMAX guide
-----------------|---------------------------------------------------------------------------
Local and Bianca |Does not work, see [Bianca file transfer](../cluster/transfer_bianca.md.md)
Local and Pelle  |[File transfer to/from Pelle using `scp`](pelle_file_transfer_using_scp.md)
Local and Rackham|[File transfer to/from Rackham using `scp`](rackham_file_transfer_using_scp.md)

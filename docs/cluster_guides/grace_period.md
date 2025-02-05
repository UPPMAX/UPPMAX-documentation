---
tags:
  - grace
  - period
---

# Grace period

The grace period is the period of time that one can access an
HPC cluster without using a TOTP, for a cluster (e.g. a sensitive
data cluster) that requires [2FA](../getting_started/get_uppmax_2fa.md).

It exists to allow our users to access our HPC clusters
with tools that assume there is no 2FA needed,
i.e. there is no dialog where you can fill in your TOTP.

To start the grace period, log in on your favorite HPC cluster (again,
the log in will require a TOTP).
Now, you have around 5 minutes to connect your tools to that cluster.

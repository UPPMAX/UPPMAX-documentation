---
tags:
  - transfer
  - data transfer
  - file transfer
  - Rackham
  - FileZilla
  - filezilla
---

# File transfer to/from Rackham using FileZilla

There are multiple ways to [transfer data to/from Rackham](../cluster_guides/transfer_rackham.md).

Here, we show how to transfer files using a graphical tool called [WinSCP](../software/winscp.md).

To transfer files to/from Rackham using WinSCP, do:

- Start WinSCP
- Create a new site
- For that site, use all standards, except:
    - Set file protocol to 'SFTP'
    - Set host name to `rackham.uppmax.uu.se`
    - Set user name to `[username]`, e.g. `richel`

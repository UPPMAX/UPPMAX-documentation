---
tags:
  - transfer
  - data transfer
  - file transfer
  - Rackham
  - WinSCP
---

# File transfer to/from Pelle using WinSCP

There are multiple ways to [transfer data to/from Pelle](../cluster_guides/transfer_pelle.md).

Here, we show how to transfer files using a graphical tool called [WinSCP](../software/winscp.md).

To transfer files to/from Rackham using WinSCP, do:

- Start WinSCP

![WinSCP Pelle](./img/winscp_pelle_login.png)

- Create a new site
- For that site, use all standards, except:
    - Set file protocol to 'SFTP'
    - Set host name to `pelle.uppmax.uu.se`
    - Set user name to `[username]`, e.g. `sven`

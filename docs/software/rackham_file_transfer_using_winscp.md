---
tags:
  - transfer
  - data transfer
  - file transfer
  - Rackham
  - WinSCP
---

# File transfer to/from Rackham using WinSCP

There are multiple ways to [transfer data to/from Rackham](../cluster_guides/transfer_rackham.md).

Here, we show how to transfer files using a graphical tool called [WinSCP](../software/winscp.md).

To transfer files to/from Rackham using WinSCP, do:

- Start WinSCP

![WinSCP Rackham](./img/winscp_rackham_login.png)

- Create a new site
- For that site, use all standards, except:
    - Set file protocol to 'SFTP'
    - Set host name to `rackham.uppmax.uu.se`
    - Set user name to `[username]`, e.g. `sven`
    - Save
- Double-click on the saved session to the left OR Presse the "Login" button
- Enter password

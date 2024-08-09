# File transfer to/from Transit using WinSCP

There are multiple ways to [transfer files to/from Transit using a graphical tool](../cluster_guides/transit_file_transfer_using_gui.md)

Here it is shown how to transfer files using a graphical tool called WinSCP.

???- question "What is Transit?"

    See [the page about the UPPMAX Transit server](../cluster_guides/transit.md).

???- question "What are the other ways?"

    Other ways to transfer data to/from Transit are described [here](../cluster_guides/transfer_transit.md)

## Procedure

WinSCP is a secure file transfer tool that works under Windows.

To transfer files to/from Transit using WinSCP, do:

- Start WinSCP
- Create a new site
- For that site, use all standards, except:
    - Set file protocol to 'SFTP'
    - Set host name to `transit.uppmax.uu.se`
    - Set user name to `[username]`, e.g. `richel`

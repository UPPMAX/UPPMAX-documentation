# `rsync` on Bianca

[`rsync`](../software/rsync.md) is a command-line tool
for [file transfer](../cluster_guides/file_transfer.md).

This page describes how to use [`rsync`](../software/rsync.md) on [Bianca](../cluster_guides/bianca.md).

Using [`rsync`](../software/rsync.md) for direct file transfer
from a local computer to [wharf](../cluster_guides/wharf.md) fails,
as cannot `rsync` directly to [wharf](../cluster_guides/wharf.md).

It can be made to work (by using [transit](../cluster_guides/transit.md)), as described in
[the UPPMAX Bianca file transfer using rsync](../software/bianca_file_transfer_using_rsync.md).

???- question "How does it look like if I try to `rsync` directly to `wharf` anyways?"

    One cannot [`rsync`](../software/rsync.md) directly to [wharf](../cluster_guides/wharf.md).

    However, this is how it looks like:


    ```console
    sven@sven-N141CU:~$ rsync my_local_file.txt sven-sens2016001@bianca-sftp.uppmax.uu.se:/sven-sens2016001

    Hi!

    You are connected to the bianca wharf (sftp service) at
    bianca-sftp.uppmax.uu.se.

    Note that we only support SFTP, which is not exactly the
    same as SSH (rsync and scp will not work).

    Please see our homepage and the Bianca User Guide
    for more information:

    https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/

    If you have any questions not covered by the User Guide, you are
    welcome to contact us at support@uppmax.uu.se.

    Best regards,
    UPPMAX

    sven-sens2016001@bianca-sftp.uppmax.uu.se's password:
    protocol version mismatch -- is your shell clean?
    (see the rsync manpage for an explanation)
    rsync error: protocol incompatibility (code 2) at compat.c(622) [sender=3.2.7]
    ```

If you want to do file transfer to/from Bianca,
read [the UPPMAX page on Bianca file transfer using rsync](../software/bianca_file_transfer_using_rsync.md).

## Links

- [`rsync` homepage](https://rsync.samba.org/)

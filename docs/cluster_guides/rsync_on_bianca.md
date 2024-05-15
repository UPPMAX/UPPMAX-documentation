# `rsync` on Bianca

[`rsync`](../software/rsync.md) is a command-line tool
for [file transfer](../cluster_guides/file_transfer.md).

This page describes how to use [`rsync`](../software/rsync.md) on [Bianca](bianca.md).

One cannot `rsync` directly to `wharf`.

???- question "How does it look like if I try to `rsync` directly to `wharf` anyways?"

    One cannot `rsync` directly to `wharf`.

    However, this is how it looks like:


    ```
    richel@richel-N141CU:~$ rsync my_local_file.txt richel-sens2016001@bianca-sftp.uppmax.uu.se:/richel-sens2016001

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

    richel-sens2016001@bianca-sftp.uppmax.uu.se's password:
    protocol version mismatch -- is your shell clean?
    (see the rsync manpage for an explanation)
    rsync error: protocol incompatibility (code 2) at compat.c(622) [sender=3.2.7]
    ```


## Links

- [`rsync` homepage](https://rsync.samba.org/)

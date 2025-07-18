---
tags:
  - sftp
  - SFTP
  - Bianca
  - data transfer
  - file transfer
  - transfer
  - terminal
  - command-line
  - console
---

# Using `sftp` with Bianca

[`sftp`](../software/sftp.md) is a command-line program
to [transfer files to/from Bianca](../cluster_guides/transfer_bianca.md).

## Procedure

???- question "Would you enjoy a video?"

    See [a video showing how to `sftp` with Bianca](https://youtu.be/URWIubTVSZQ).

### 1. [Get inside of SUNET](../getting_started/get_inside_sunet.md)

[Get inside of SUNET](../getting_started/get_inside_sunet.md).

If needed, [start the grace period](../cluster_guides/grace_period.md).

### 2. Start `sftp`

```bash
sftp [user_name]-[project_id]@bianca-sftp.uppmax.uu.se:/[user_name]-[project_id]
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)
- `[user_name]` is the name of your [UPPMAX user account](../getting_started/user_account.md)

For example:

```bash
sftp sven-sens2016001@bianca-sftp.uppmax.uu.se:/sven-sens2016001
```

### 3. Supply password

`sftp` will ask for a password:

```bash
sven-sens2016001@bianca-sftp.uppmax.uu.se's password:
```

The password is your normal UPPMAX password directly followed by
the six digits from the [the `UPPMAX` 2-factor authentication](../getting_started/get_uppmax_2fa.md).
For example, if your password is `VerySecret` and the second factor code is `123456`
you would type `VerySecret123456` as the password in this step.

After typing in the password and 2FA one sees a welcome message
and the `sftp` prompt.

???- question "How does that look like?"

    This is the welcome message:

    ```text
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
    Connected to bianca-sftp.uppmax.uu.se.
    sftp>
    ```

???- question "How do I get rid of the welcome message?"

    Use `sftp`'s `-q` (which is short for 'quiet') flag:

    ```bash
    sftp -q sven-sens2016001@bianca-sftp.uppmax.uu.se
    ```

The last line, `sftp>` is the `sftp` prompt.

Once connected you will have to type the `sftp` commands to upload/download files.
See [the UPPMAX page on `sftp`](../software/sftp.md) how to do so.

With `sftp` you only have access to [your wharf folder](../cluster_guides/wharf.md).

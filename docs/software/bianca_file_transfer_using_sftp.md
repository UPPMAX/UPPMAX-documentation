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
sftp [user_name]@bianca-sftp.uppmax.uu.se
```

where `[user_name]` is the name of your [UPPMAX user account](../getting_started/user_account.md)


For example:

```bash
sftp sven@bianca-sftp.uppmax.uu.se
```

### 3. Supply password

`sftp` will ask for a password:

```bash
(sven@bianca-sftp.uppmax.uu.se) Password:
```

The password is your normal UPPMAX password. The typing will be invisible. Use the `enter` key to submit.

### 4. Supply second factor

`sftp` will ask for a second factor:

```bash
(sven@bianca-sftp.uppmax.uu.se) Password:
(sven@bianca-sftp.uppmax.uu.se) Second factor (TOTP):
```

This is the six digit code from the [the `UPPMAX` 2-factor authentication](../getting_started/get_uppmax_2fa.md).

After typing in the password and 2FA one sees the `sftp` prompt.

### 5. Navigating the wharf

While logged in to the wharf, type `ls` to list your available projects.

```bash
sftp> ls
sens2016001 sens2017625 sens2025123
```

Type `cd [project-id]/[user-name]` to enter the wharf of a given project.

See [the UPPMAX page on `sftp`](../software/sftp.md) how to use `sftp` to download and upload files.


Once connected you will have to type the `sftp` commands to upload/download files.
See [the UPPMAX page on `sftp`](../software/sftp.md) how to do so.

With `sftp` you only have access to [your wharf folder](../cluster_guides/wharf.md).

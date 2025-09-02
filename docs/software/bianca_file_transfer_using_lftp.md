---
tags:
  - lftp
  - Bianca
  - data transfer
  - file transfer
  - transfer
  - terminal
  - command-line
---

# Using `lftp` with Bianca

`lftp` is a command-line program
to [transfer files to/from Bianca](../cluster_guides/transfer_bianca.md).

Here, the procedure for file transfer is shown,
as well as some troubleshooting.

## Procedure

### 1. [Get inside of SUNET](../getting_started/get_inside_sunet.md)

[Get inside of SUNET](../getting_started/get_inside_sunet.md).

### 2. Start `lftp`

```bash
lftp sftp://[user_name]@bianca-sftp.uppmax.uu.se
``
where `[user_name]` is the name of your [UPPMAX user account](../getting_started/user_account.md)

For example:

```bash
lftp sftp://sven@bianca-sftp.uppmax.uu.se/
```

You'll be asked to type a password.

### 3. Enter password with TOTP

When asked for a password, type the UPPMAX password.

???- question "I don't see asterisks appear when I type"

    Well spotted!

    Indeed, you will not see the characters you type,
    which is common for Linux systems.

    Just type the password and press enter :-)

### 4. Enter the second factor

When asked for the second factor, type the six digit one-time password from your UPPMAX
two-factor authenticator.


## Troubleshooting

You need to "set net:connection_limit 1".
`lftp` may also defer the actual connection
until it's really required unless you end your connect URL with a path.

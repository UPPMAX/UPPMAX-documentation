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

!!! warning "This may have changed as of 2025-02-05"

    If the step below does not work anymore,
    [start the grace period](../cluster_guides/grace_period.md)
    and try again.

    If it still fails, please [contact UPPMAX support](../support.md).

```bash
lftp sftp://[user_name]-[project_id]@bianca-sftp.uppmax.uu.se/[user_name]-[project_id]/
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)
- `[user_name]` is the name of your [UPPMAX user account](../getting_started/user_account.md)

For example:

```bash
lftp sftp://sven-sens2025560@bianca-sftp.uppmax.uu.se/sven-sens2025560/
```

### 3. Enter passwrd with TOTP

When asked for a password,
type the password followed with a one-time password from your UPPMAX
two-factor authenticator.

For example, if your password is `VerySecret` and the 2FA app gives
you `123456`, then type `VerySecret123456`.


## Troubleshooting

You need to "set net:connection_limit 1".
`lftp` may also defer the actual connection
until it's really required unless you end your connect URL with a path.

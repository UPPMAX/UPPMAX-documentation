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
lftp sftp://sven-sens2016001@bianca-sftp.uppmax.uu.se/sven-sens2016001/
```

## Troubleshooting

You need to "set net:connection_limit 1".
`lftp` may also defer the actual connection
until it's really required unless you end your connect URL with a path.

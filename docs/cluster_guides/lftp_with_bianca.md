# Using `lftp` with Bianca

`lftp` is a command-line program
to [transfer files to/from Bianca](transfer_bianca.md).

With the command line SFTP client `lftp`,
you need to "set net:connection_limit 1".
`lftp` may also defer the actual connection
until it's really required unless you end your connect URL with a path.

[When inside of SUNET](../getting_started/get_inside_sunet.md)
(which can be on a local computer or on [Rackham](rackham.md)) do:

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

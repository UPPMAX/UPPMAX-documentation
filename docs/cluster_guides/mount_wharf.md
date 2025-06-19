# Mount a Bianca project

On transit, mount the wharf of your Bianca project:

```bash
mount_wharf [project_id]
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)

???- question "What about the `[path]` argument?"

    Well spotted!

    Indeed, the Transit server gives these arguments:

    ```bash
    mount_wharf [project_id] [path]
    ```

    However, the `[path]` argument is optional: if not
    given, a default will be used.

    To simplify matters, here we use the default.

for example:

```bash
mount_wharf sens2016001
```

The password is your normal UPPMAX password directly followed by
the six digits from the
[the `UPPMAX` 2-factor authentication](../getting_started/get_uppmax_2fa.md).
For example, if your password is `VerySecret` and the second factor code is `123456`
you would type `VerySecret123456` as the password in this step.

Now a folder called `sens2016001` is created.

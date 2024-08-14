# `chmod`

`chmod` is a Linux command to change the ownership of a folder

## How to create a folder in the shared project folder that only I can access?

Your project folders at `/proj/[naiss_project]` are shared by members of that
NAISS project.

If you need a folder that only you can access, assuming
that folder is called `my_private_folder`, do the following:

```bash
chmod 700 my_private_folder
```

???- question "How can I confirm it worked?"

    Use `ll`:

    ```bash
    $ ll
    drwxrwsr-x 2 sven my_group 4096 Aug 14 09:07 a_shared_folder/
    drwx--S--- 2 sven my_group 4096 Aug 14 09:06 my_private_folder/
    ```

    The first characters is what it is about:

    - `drwxrwsr-x`: accessible with group
    - `drwx--S---`: only accessible by you

Now, you can enter that folder:

```bash
cd my_private_folder
```

However, others cannot and get this error message:

```bash
bash: cd: my_private_folder/: Permission denied
```

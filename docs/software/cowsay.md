# cowsay

`cowsay` is a tool that commonly use as a toy example.

Because `cowsay` is not part of the Linux kernel,
users commonly need to install it.
Or in our case: load a [module](../cluster_guides/modules.md) to use it.

`cowsay` (the tool) is part of the identically-named `cowsay`
[module](../cluster_guides/modules.md).

Finding the [module](../cluster_guides/modules.md) that
has `cowsay` installed:

```bash
module spider cowsay
```

???- question "How does that look like?"

    You output will look similar to this:

    ```bash
    [sven@rackham1 ~]$ module spider cowsay

    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      cowsay: cowsay/3.03
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        This module can be loaded directly: module load cowsay/3.03

        Help:
           cowsay - use cowsay

    ```

Loading the latest version of the `cowsay` module:

```bash
module load cowsay/3.03
```

Now you can run `cowsay`:


```bash
cowsay hello
```

results in:

```text
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```


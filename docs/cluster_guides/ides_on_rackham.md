# IDEs on Rackham

![](./img/rstudio_in_action_480_x_270.png)

> RStudio is one of the IDEs that can be used on Rackham.

Here we show how to use some [IDEs](ides.md) on Rackham.

???- question "Forgot what an IDE is?"

    See at the general page on IDEs [here](ides.md).

In all cases, we login to the Rackham remote desktop environment.

???- question "Forgot how to login to a remote desktop environment?"

    See [here](../getting_started/login_rackham.md).

    Spoiler: go to [https://rackham.uppmax.uu.se/](https://rackham.uppmax.uu.se/)

In all cases, we use an interactive node: an IDE is a resource-heavy
program, so using it on a login node would slow down other users.

???- question "Forgot how to start an interactive node?"

    See [here](start_interactive_node_on_rackham.md).

???- question "Do you really want to use an IDE on Rackham?"

    Using an IDE on Rackham is cumbersome and
    there are superior ways to develop code on Rackham.

    However, using an IDE may make it easier for a new user to feel
    comfortable using Rackham.

    The [UPPMAX 'Programming Formalisms' course](https://github.com/UPPMAX/programming_formalisms)
    will teach you a superior workflow, 
    where development takes place on your own regular computer
    and testing is done using simulated/fake data.
    When development is done,
    the tested project is uploaded to Rackham and setup to
    use the real data instead.

    This avoids using a clumsy remote desktop environment,
    as well as many added bonuses.

When on an interactive node, start any of these IDEs:

- [Jupyter](jupyter.md)
- [RStudio](rstudio_on_rackham.md)
- [VSCodium](vscodium_on_rackham.md)


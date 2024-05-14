# `eog`

![Example use of eog](./img/eog.png)


`eog` is a tool to view images on an UPPMAX cluster.

To be able to see the images,
either use [SSH with X-forwarding](../software/ssh_x_forwarding.md)
or [login to a remote desktop](../getting_started/login.md)

Usage:


```
eog [filename]
```

for example:

```
eog my.png
```

???- question "Need an example image to work with?"

    In the terminal, do:

    ```
    convert -size 32x32 xc:transparent my.png
    ```

    This will create an empty PNG image.

???- question "How does this look like?"

    ![Example use of eog](./img/eog.png)

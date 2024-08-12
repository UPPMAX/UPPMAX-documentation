# `xeyes`

![`xeyes` in action](./img/xeyes.png)

`xeyes` is a program that shows two eyes. The `x` in its name refers
to the X11 display server, which is one of many ways to display
graphics on screen.

`xeyes` is used mostly diagnostically, i.e. to find
out if one used [SSH with X-forwarding](ssh_x_forwarding.md).
When `xeyes` is run, but does not show the eyes, it means
that [SSH with X-forwarding](ssh_x_forwarding.md) does not work.

## How to run `xeyes`

In a terminal, type:

```bash
xeyes
```

If you've logged in via [SSH with X-forwarding](ssh_x_forwarding.md)
and it works correctly, you will see this:

![`xeyes` in action](./img/xeyes_with_ssh_x_forwarding.png)

If you've logged in without [SSH with X-forwarding](ssh_x_forwarding.md)
or the [SSH client](ssh_client.md) is not setup correctly, you will see:

![`xeyes` not working](./img/xeyes_no_ssh_x_forwarding.png)


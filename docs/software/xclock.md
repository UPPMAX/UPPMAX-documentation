---
tags:
  - xclock
  - eyes
  - console
  - terminal
  - x-forwarding
---

# `xclock`

`xclock` is a program that shows a clock. The `x` in its name refers
to the X11 display server, which is one of many ways to display
graphics on screen.

`xclock` is used mostly diagnostically, i.e. to find
out if one used [SSH with X-forwarding](ssh_x_forwarding.md).
When `xclock` is run, but does not show the clock, it means
that [SSH with X-forwarding](ssh_x_forwarding.md) does not work.

## How to run `xclock`

In a terminal, type:

```bash
xclock
```

If you've logged in via [SSH with X-forwarding](ssh_x_forwarding.md)
and it works correctly, you will see this:

![`xclock` in action](./img/xclock_with_ssh_x_forwarding.png)

If you've logged in without [SSH with X-forwarding](ssh_x_forwarding.md)
or the [SSH client](ssh_client.md) is not setup correctly, you will see:

![`xclock` not working](img/xclock_no_ssh_x_forwarding.png)

The line that indicates the error is:

```console
Error: Can't open display:
```

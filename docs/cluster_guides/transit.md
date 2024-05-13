# Transit

Transit is an UPPMAX service that can be used to securely transfer files.

???- question "Is Transit a file server?"

    Transit is a service, not a file server.
    Transit is not a file server, as it does not store files.

    This can be observed by uploading files to Transit
    and then closing this connection
    before sending the files to a permanent location:
    the Transit-only files will disappear.

???- question "What is Transit?"

    ![From https://sv.wikipedia.org/wiki/Brevl%C3%A5da#/media/Fil:Brevl%C3%A5dor.jpg](./img/swedish_postbox_117_x_157.jpg)

    > A Swedish post box. The yellow post box is for non-regional mail,
    > the blue for regional mail.

    Transit can be viewed as [a post box](https://en.wikipedia.org/wiki/Post_box),
    where the file you upload is a letter.

    If you put a letter without an address in a post box,
    it will be thrown away.

    If you put an address on the letter,
    the letter will be delivered.
    Here, 'putting an address on the letter'
    is to copy the file to the desired location.

This page shows:

- [how to log in to Transit](#log-in-to-transit)
- [software on Transit](#software-on-transit)
- [file transfer using Transit](transfer_transit.md).

## Log in to Transit

Below is a step-by-step procedure to login to Transit.

### 1. Get within SUNET

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

### 2. Use SSH to login

On your local computer, start a terminal and use [`ssh`](../software/ssh.md) to login to Transit:

```
ssh [username]@transit.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```
ssh sven@transit.uppmax.uu.se
```

If you haven't setup using SSH keys, you will be asked for your UPPMAX password.

If this is your first time on Transit, you will be asked for adding
it to your list of known hosts. Type `yes`.

???- question "How does that look like?"

    This is how it looks like when you are asked
    for adding Transit to your list of known hosts.

    ![](./img/transit_add_to_known_hosts.png)

You are now logged in to Transit!

![](./img/logged_in_transit.png)

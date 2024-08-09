# Log in to Transit

Below is a step-by-step procedure to login to [Transit](../cluster_guides/transit.md).

???- question "Enjoy a video?"

  [See how to log in to Transit as a video](https://youtu.be/uXMOP-WVGIY).

## 1. Get within SUNET

[Get inside the university networks](../getting_started/get_inside_sunet.md).

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Use SSH to login

On your local computer, start a [terminal](../software/terminal.md)
and use [`ssh`](../software/ssh.md) to login to Transit:

```bash
ssh [username]@transit.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
ssh sven@transit.uppmax.uu.se
```

If you haven't setup using SSH keys, you will be asked for your UPPMAX password.

If this is your first time on Transit, you will be asked for adding
it to your list of known hosts. Type `yes`.

???- question "How does that look like?"

    This is how it looks like when you are asked
    for adding Transit to your list of known hosts.

    ![Transit is added to your list of known hosts](./img/transit_add_to_known_hosts.png)

You are now logged in to Transit!

???- question "How does that look like?"

    ```console
    richel@richel-N141CU:~/GitHubs/UPPMAX-documentation/docs/cluster_guides$ ssh richel@transit.uppmax.uu.se
    richel@transit.uppmax.uu.se's password: 
    Last login: Tue May 14 07:32:22 2024 from vpnpool188-185.anst.uu.se

    Transit server

    You can mount bianca wharf with the command

    mount_wharf PROJECT [path]

    If you do not give a path the mount will show up as PROJECT in your home
    directory.

    Note; any chagnes you do to your normal home directory will not persist.
    ```

# `transit`

`transit` is an UPPMAX server that can be used to securely transfer files.

This page shows how to login to `transit`.

For file transfer using `transit` see [here](transfer_transit.md).

## Login to `transit`

Below is a step-by-step procedure to login to `transit`.

### 1. Get within SUNET

???- tip "Forgot how to get within SUNET?"

    See [the 'Logging in to Bianca' page](../getting_started/login_bianca.md).

### 2. Use SSH to login

On your local computer, start a terminal and use `ssh` to login to `transit`: 

```
ssh [username]@transit.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```
ssh sven@transit.uppmax.uu.se
```

If you haven't setup using SSH keys, you will be asked for your UPPMAX password.

If this is your first time on `transit`, you will be asked for adding
it to your list of known hosts. Type `yes`.

???- question "How does that look like?"

    This is how it looks like when you are asked 
    for adding `transit` to your list of known hosts.

    ![](./img/transit_add_to_known_hosts.png)

You are now logged in to `transit`!

![](logged_in_transit.png)

# Transit

Transit is an UPPMAX service that can be used to securely transfer files.

???- question "Is Transit a file server?"

    Transit is not a file server, 
    as it does not store files.

    This can be observed by uploading files to Transit
    and then closing this connection
    before sending the files to a permanent location:
    the Transit-only files will disappear.

???- question "What is Transit?"

    Transit can be viewed as a post box,
    where the file you upload is a letter.

    If you put a letter without an address in a post box,
    it will be thrown away.

    If you put an address on the letter, 
    the letter will be delivered.
    Here, 'putting an address on the letter'
    is to copy the file to the desired location.

This page shows how to login to Transit.

For file transfer using Transit see [here](transfer_transit.md).

## Login to Transit

Below is a step-by-step procedure to login to Transit.

### 1. Get within SUNET

???- tip "Forgot how to get within SUNET?"

    See [the 'Logging in to Bianca' page](../getting_started/login_bianca.md).

### 2. Use SSH to login

On your local computer, start a terminal and use `ssh` to login to Transit: 

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

![](logged_in_transit.png)

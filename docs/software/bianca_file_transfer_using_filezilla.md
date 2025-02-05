---
tags:
  - FileZilla
  - Bianca
  - data transfer
  - file transfer
  - transfer
---

# File transfer to/from Bianca using FileZilla

Download and install from [UU Software Center](https://www.uu.se/en/staff/service-and-tools/tools-and-guides/manage-and-update-your-windows-computer/installing-or-ordering-software-windows).

You can also download the software from FileZilla website for [Windows](https://filezilla-project.org/download.php?platform=win64), [MacOS (intel)](https://filezilla-project.org/download.php?platform=osx) or [MacOS (Apple Silicon)](https://filezilla-project.org/download.php?platform=macos-arm64).

![FileZilla connected to Bianca](./img/filezilla_login_to_bianca_236_x_266.png)

> FileZilla connected to Bianca

There are multiple ways to [transfer data to/from Bianca](../cluster_guides/transfer_bianca.md).

Here, we show how to transfer files using a graphical tool called [FileZilla](filezilla.md).

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to Bianca
    using FileZilla, watch the video
    [here](https://youtu.be/V-iPQLjvByc?si=OMyH3REu-SoFQeI9)

To transfer files to/from Bianca using FileZilla, do the following steps:

### 1. Get inside SUNET

[Get inside of SUNET](../getting_started/get_inside_sunet.md).

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

### 2. Start FileZilla

Start FileZilla.

### 3. Select 'File | Site manager'

!!! warning "This may have changed as of 2025-02-05"

    If the step below does not work anymore,
    [start the grace period](../cluster_guides/grace_period.md)
    and try again.

    If it still fails, please [contact UPPMAX support](../support.md).

In FileZilla, from the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![The FileZilla 'File' menu contains the item 'Site manager'](./img/filezilla_file_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

### 4. Click 'New site'

In the 'Site Manager' dialog, click 'New site'

???- tip "Where is that?"

    It is here:

    !['New site' can be found at the bottom-left](./img/filezilla_site_manager.png)

    > 'New site' can be found at the bottom-left

### 5. Create a name for the site, e.g. `bianca-sens123456`

In the 'New Site' dialog, create a name for the site, e.g. `bianca-sens123456`.

### 6. Configure site

In the 'New Site' dialog, use all standards, except:

- Set protocol to 'SFTP - SSH File Transfer Protocol'
- Set host to `bianca-sftp.uppmax.uu.se`
- Set user to `[username]-[project]`, e.g. `sven-sens123456`

???- tip "How does that look like?"

    It looks similar to these:

    ![FileZilla settings for a user](./img/filezilla_setup_bianca_pavlin.png)

    ![FileZilla settings for another user](./img/filezilla_setup_bianca_sven.png)

!!! tip "Storing a password is useless"

    Because Bianca holds sensitive data,
    there is need to use the UPPMAX two-factor authentication
    code every time you login.
    Due to this, storing a password is hence useless

### 7. Click 'Connect'

In FileZilla, click 'Connect'

You will be asked for your password with two-factor identification, hence
type `[your password][2FA code]`, e.g. `VerySecret123456`.

Now you can transfer files between your local computer and [your `wharf` folder](../cluster_guides/wharf.md).

NOTE: Filezilla will ask for your password and two-factor for each file you transfer. To avoid that, go to
Site Manager > Transfer Settings > Limit number of simultaneous connections to 1.

???- tip "How does that look like?"

    It looks like this:

    ![FileZilla is ready to transfer files](./img/filezilla_login_to_bianca.png)

    > FileZilla is ready to transfer files

## Troubleshooting

### Access denied

Full error, in the FileZilla terminal:

```text
Status: Connecting to bianca-sftp.uppmax.uu.se...

Status: Using username "sven-sens2023613".

Status: Access denied

Error: Authentication failed.

Error: Critical error: Could not connect to server
```

Hypotheses:

- The user is not within SUNET

???- question "How do I know if I am within the university networks?"

    If you login via `eduroam` you are within the university networks.

    When unsure, go to the Bianca remote desktop website at
    [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se):
    if this page does not load, you are outside of the university networks.

    See [How to get inside of the university networks](../getting_started/get_inside_sunet.md)
    if you outside of the university networks.

- The account is not active

???- question "How do I know if the Bianca project is active?"

    A quick way to confirm your Bianca project is active:
    go to <https://bianca.uppmax.uu.se>
    and type your username. If the project is displayed, it is active.

    To confirm your project is active or inactive, use the SUPR NAISS website.
    See [the UPPMAX documentation on projects](../getting_started/project.md)
    how to see if your project is active?

- The user is not a member of the Bianca project

???- question "How do I know if I am a member of the Bianca project?"

    A quick way to confirm you are a member of the Bianca project:
    go to <https://bianca.uppmax.uu.se>
    and type your username. If the project is displayed,
    you are a member of the Bianca project.

    To confirm your project is active or inactive, use the SUPR NAISS website.
    See [the UPPMAX documentation on projects](../getting_started/project.md)
    how to see which projects you are a member of.

See [the UPPMAX page on contacting support](../support.md)
on how to contact us.

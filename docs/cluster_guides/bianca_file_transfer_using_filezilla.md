# File transfer to/from Bianca using FileZilla

![FileZilla connected to Bianca](./img/filezilla_login_to_bianca_236_x_266.png)

> FileZilla connected to Bianca

???- question "Would you like a video?"

    If you like to see how to do file tranfer from/to Bianca
    using FileZilla, watch the video
    [here](https://youtu.be/V-iPQLjvByc?si=OMyH3REu-SoFQeI9)

FileZilla is a [graphical tool to do file transfer to/from Bianca](bianca_fila_transfer_using_gui.md),
that works under Linux, Mac and Windows.

To transfer files to/from Bianca using FileZilla, do the following steps:

## 1. Get inside SUNET

Get inside SUNET.

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Start FileZilla

Start FileZilla.

## 3. Select 'File | Site manager'

In FileZilla, from the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![](./img/filezilla_file_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

## 4. Click 'New site'

In the 'Site Manager' dialog, click 'New site'

???- tip "Where is that?"

    It is here:

    ![](./img/filezilla_site_manager.png)

## 5. Create a name for the site, e.g. `bianca-sens123456`.

In the 'New Site' dialog, create a name for the site, e.g. `bianca-sens123456`.

## 6. Configure site 

In the 'New Site' dialog, use all standards, except:

 * Set protocol to 'SFTP - SSH File Transfer Protocol'
 * Set host to `bianca-sftp.uppmax.uu.se`
 * Set user to `[username]-[project]`, e.g. `richel-sens123456`

???- tip "How does that look like?"

    It looks similar to these:

    ![](./img/filezilla_setup_bianca_pavlin.png)

    ![](./img/filezilla_setup_bianca_richel.png)

!!! tip "Storing a password is useless"

    Because Bianca holds sensitive data,
    there is need to use the UPPMAX two-factor authentication
    code every time you login.
    Due to this, storing a password is hence useless

## 7. Click 'Connect'

In FileZilla, click 'Connect'

You will be asked for your password with two-factor identification, hence
type `[your password][2FA code]`, e.g. `VerySecret123456`.

Now you can transfer files between your local computer and [your `wharf` folder](wharf.md).

???- tip "How does that look like?"

    It looks like this:

    ![](./img/filezilla_login_to_bianca.png)

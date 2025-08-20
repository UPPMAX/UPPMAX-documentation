---
tags:
  - FileZilla
  - Pelle
---

# File transfer to/from Pelle using FileZilla

There are multiple ways to
[transfer data to/from Pelle](../cluster_guides/transfer_pelle.md).

Here, we show how to transfer files using a graphical tool
called [FileZilla](filezilla.md),
which is a secure file transfer tool
that works under Linux, Mac and Windows.

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to Pelle
    using FileZilla, watch the video
    `TODO`

To transfer files to/from Pelle using FileZilla, do
the following steps:

## 1. Start FileZilla

Start FileZilla.

## 2. Start FileZilla's site manager

From the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![The FileZilla 'File' menu contains the item 'Site manager'](./img/filezilla_file_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

## 3. Add a new site in FileZilla's site manager

In FileZilla's site manager, click 'New site'

???- tip "Where is that?"

    It is here:

    ![The FileZilla Site Manager](./img/filezilla_site_manager.png)

## 4. Setup the site

In FileZilla's site manager:

- create a name for the site, e.g. `Pelle`.
- for that site, use all standards, except:
    - Set protocol to 'SFTP - SSH File Transfer Protocol'
    - Set host to `pelle.uppmax.uu.se`
    - Set user to your UPPMAX username, e.g. `sven`
    - Set password to your UPPMAX password, e.g. `VerySecret`

???- tip "How does that look like?"

    It looks similar to this:

    ![FileZilla configured for Pelle](./img/filezilla_setup_pelle_sven.png)`

## 5. Connect to the site

Click 'Connect'.

## 6. Ready to transfer files

Now you can transfer files between your local computer and Pelle.

???- tip "How does that look like?"

    It looks like this:

    ![FileZilla is connected to Pelle](./img/filezilla_login_to_pelle.png)

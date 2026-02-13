---
tags:
  - FileZilla
  - Alvis
---

# File transfer to/from Alvis using FileZilla

???- question "Why is this page at UPPMAX?"

    It is the intention that this guide is moved to the C3SE documentation.
    However, it has not been suggested to be added to their documentaton
    yet.

HPC clusters have different ways to do
[file transfer using FileZilla](file_transfer_using_filezilla.md).

This page shows how to do so for Alvis.

![FileZilla connected to Alvis](filezilla_login_to_alvis.png)

> FileZilla connected to Alvis

## Procedure

???- question "Would you like a video?"

    See the YouTube video
    [file transfer from/to Alvis using FileZilla](https://youtu.be/A8zfd0o0uzI).

FileZilla is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from Alvis using FileZilla, do
the following steps:

### 1. Get inside SUNET

[Get inside of SUNET](../getting_started/get_inside_sunet.md).

???- question "Forgot how to get within SUNET?"

    See [the 'get inside the university networks' page](../getting_started/get_inside_sunet.md)

### 2. Install `putty-tools`

???- question "What if I don't use Linux?"

    Instead of following steps 2 and 3, follow the procedure at
    [the puttygen page, section 'Create SSH key files'](../software/puttygen.md#create-ssh-key-files).


```bash
sudo apt install putty-tools
```

### 3. Create the needed files in the `.ssh` folder

Navigate into the `.ssh` folder.

```bash
cd .ssh
```

#### 3.1 Create the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -t rsa -b 2048 -C "[alvis_username]@alvis.c3se.chalmers.se" -o [filename].ppk
```

For example:

```bash
puttygen -t rsa -b 2048 -C "svens@alvis.c3se.chalmers.se" -o alvis_filezilla.ppk
```

![Alvis file site manager](alvis_file_transfer_using_filezilla_select_file_site_manager.png)

#### 3.2 Extract the private SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O private-openssh-new [filename].ppk -o [filename]
```

For example:

```bash
puttygen -O private-openssh-new alvis_filezilla.ppk -o alvis_filezilla
```

#### 3.3 Extract the public SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O public-openssh [filename].ppk -o [filename].pub
```

For example:

```bash
puttygen -O public-openssh alvis_filezilla.ppk -o alvis_filezilla.pub
```

### 4. Add the public SSH key to `~/.ssh/authorised_keys`

Copy the public SSH key (in the `.pub` file)
to the `~/.ssh/authorised_keys` file on Alvis.

If that file does not exist yet, create it and set the right
permissions as such:

```bash
mkdir .ssh
touch .ssh/authorised_keys
chmod 700 .ssh/authorised_keys
chmod 700 .ssh
chmod 700 ~
```

### 5. Start FileZilla

Start FileZilla.

### 6. Start FileZilla's site manager

From the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![The FileZilla 'File' menu contains the item 'Site manager'](alvis_file_transfer_using_filezilla_select_file_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

### 7. Add a new site in FileZilla's site manager

In FileZilla's site manager, click 'New site'

???- tip "Where is that?"

    It is here:

    ![The FileZilla Site Manager](alvis_file_transfer_using_filezilla_select_file_site_manager.png)

### 8. Setup the site

In FileZilla's site manager:

- create a name for the site, e.g. `Alvis`.
- for that site, use all standards, except:
    - Set protocol to 'SFTP - SSH File Transfer Protocol'
    - Set host to `alvis1.c3se.chalmers.se` or `alvis2.c3se.chalmers.se`
    - Set user to `[username]`, e.g. `svens`
    - Set logon type: Key file
    - Upload the key file at `/.ssh/alvis_filezilla.ppk`
      from you local's computer

???- tip "How does that look like?"

    It looks similar to this:

    ![FileZilla configured for Alvis](filezilla_login_to_alvis_site_manager.png)

### 9. Connect to the site

Click 'Connect'.

### 10. Ready to transfer files

Now you can transfer files between your local computer and Alvis.

???- tip "How does that look like?"

    It looks like this:

    ![FileZilla is connected to Alvis](filezilla_login_to_alvis.png)

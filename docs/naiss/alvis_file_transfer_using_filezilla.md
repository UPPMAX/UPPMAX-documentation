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

There are multiple ways to transfer data to/from Alvis.

Here, we show how to transfer files using a graphical tool called FileZilla.

![FileZilla connected to Alvis](filezilla_login_to_alvis.png)

> FileZilla connected to Alvis

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to Alvis
    using FileZilla, watch the video [here](https://youtu.be/T4qqN_ljsS8)

FileZilla is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from Alvis using FileZilla, do
the following steps:

### 1. Install `putty-tools`

```bash
sudo apt install putty-tools
```

### 2. Create the needed files in the `.ssh` folder

Navigate into the `.ssh` folder.

```bash
cd .ssh
```

#### 2.1 Create the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -t rsa -b 2048 -C "[alvis_username]@alvis.c3se.chalmers.se" -o [filename].ppk
```

For example:

```bash
puttygen -t rsa -b 2048 -C "svens@alvis.c3se.chalmers.se" -o alvis_filezilla.ppk
```

#### 2.2 Extract the private SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O private-openssh-new [filename].ppk -o [filename]
```

For example:

```bash
puttygen -O private-openssh-new alvis_filezilla.ppk -o alvis_filezilla
```

#### 2.2 Extract the public SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O public-openssh [filename].ppk -o [filename].pub
```

For example:

```bash
puttygen -O public-openssh alvis_filezilla.ppk -o alvis_filezilla.pub
```

### 3. Add the public SSH key to `~/.ssh/authorized_keys`

```
mkdir .ssh
touch .ssh/authorized_keys
chmod 700 .ssh/authorized_keys
chmod 700 .ssh
chmod 700 ~
```

Copy the public SSH key (in the `.pub` file) to the 
`~/.ssh/authorized_keys` file on Alvis.


### 4. Start FileZilla

Start FileZilla.

### 5. Start FileZilla's site manager

From the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![The FileZilla 'File' menu contains the item 'Site manager'](filezilla_file_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

### 6. Add a new site in FileZilla's site manager

In FileZilla's site manager, click 'New site'

???- tip "Where is that?"

    It is here:

    ![The FileZilla Site Manager](filezilla_site_manager.png)

### 7. Setup the site

In FileZilla's site manager:

- create a name for the site, e.g. `Alvis`.
- for that site, use all standards, except:
    - Set protocol to 'SFTP - SSH File Transfer Protocol'
    - Set host to `alvis.c3se.chalmers.se`
    - Set user to `[username]`, e.g. `svens`
    - Set logon type: Key file
    - Upload the key file at `/.ssh/alvis_filezilla.ppk`
      from you local's computer

???- tip "How does that look like?"

    It looks similar to this:

    ![FileZilla configured for Alvis](filezilla_login_to_alvis_site_manager.png)

### 8. Connect to the site

Click 'Connect'.

### 9. Ready to transfer files

Now you can transfer files between your local computer and Alvis.

???- tip "How does that look like?"

    It looks like this:

    ![FileZilla is connected to Alvis](filezilla_login_to_alvis.png)

---
tags:
  - FileZilla
  - LUMI
---

# File transfer to/from LUMI using FileZilla

???- question "Why is this page at UPPMAX?"

    It was the intention that this guide
    would be moved to the CSC documentation.
    However, contacting CSC regarding this,
    made it clear that
    [CSS does not (yet) intend to document this](https://github.com/UPPMAX/naiss_file_transfer_course/issues/34#issuecomment-2889764104).

HPC clusters have different ways to do
[file transfer using FileZilla](file_transfer_using_filezilla.md).

This page shows how to do so for LUMI.

## Procedure

???- question "Would you like a video?"

    If you like to see how to do file transfer from/to LUMI
    using FileZilla, watch the video `TODO`

FileZilla is a secure file transfer tool that works under Linux, Mac and Windows.

To transfer files to/from LUMI using FileZilla, do
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
puttygen -t rsa -b 4096 -C "[lumi_username]@lumi.csc.fi" -o [filename].ppk
```

For example:

```bash
puttygen -t rsa -b 4096 -C "svens@lumi.csc.fi" -o lumi_filezilla.ppk
```

#### 3.2 Extract the private SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O private-openssh-new [filename].ppk -o [filename]
```

For example:

```bash
puttygen -O private-openssh-new lumi_filezilla.ppk -o lumi_filezilla
```

#### 3.3 Extract the public SSH key from the `.ppk` file

In the `.ssh` folder, from a terminal do:

```bash
puttygen -O public-openssh [filename].ppk -o [filename].pub
```

For example:

```bash
puttygen -O public-openssh lumi_filezilla.ppk -o lumi_filezilla.pub
```

### 4. Add the public SSH key to `~/.ssh/authorized_keys`

Copy the public SSH key (in the `.pub` file)
to the `~/.ssh/authorized_keys` file on LUMI.

If that file does not exist yet, create it and set the right
permissions as such:

```bash
mkdir .ssh
touch .ssh/authorized_keys
chmod 700 .ssh/authorized_keys
chmod 700 .ssh
chmod 700 ~
```

### 5. Start FileZilla

Start FileZilla.

### 6. Start FileZilla's site manager

From the menu, select 'File | Site manager'

???- tip "Where is that?"

    It is here:

    ![The FileZilla 'File' menu contains the item 'Site manager'](filezilla_site_manager.png)

    > The FileZilla 'File' menu contains the item 'Site manager'

### 7. Add a new site in FileZilla's site manager

In FileZilla's site manager, click 'New site'

???- tip "Where is that?"

    It is here:

    ![The FileZilla Site Manager](filezilla_site_manager.png)

### 8. Setup the site

In FileZilla's site manager:

- create a name for the site, e.g. `LUMI`.
- for that site, use all standards, except:
    - Set protocol to 'SFTP - SSH File Transfer Protocol'
    - Set host to `lumi.csc.fi`
    - Set user to `[username]`, e.g. `svensson`
    - Set logon type: Key file
    - Upload the key file at `/.ssh/lumi_filezilla.ppk`
      from you local's computer

???- tip "How does that look like?"

    It looks similar to this:

    `![FileZilla configured for LUMI](filezilla_login_to_lumi_site_manager.png)`

### 9. Connect to the site

Click 'Connect'.

### 10. Ready to transfer files

Now you can transfer files between your local computer and LUMI.

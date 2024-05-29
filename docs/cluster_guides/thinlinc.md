# ThinLinc

.                     |[Bianca](bianca.md)                                                     |[Rackham](rackham.md)
----------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------
Local ThinLinc client |.                                                                       |.
UPPMAX website        |![Rackham remote desktop](./img/rackham_remote_desktop_extract_file.png)|![Bianca remote desktop](./img/filezilla_file_on_bianca.png)

ThinLinc provides for a remote desktop environment for the UPPMAX clusters.

There are two ways of connecting to the clusters using ThinLinc,
using a local ThinLinc client or login using a webbrowser.
Here are the differences:

Parameter      |Local ThinLinc client|Web browser login
---------------|---------------------|-----------------
Install        |ThinLinc client      |Nothing [1]
Simplicity     |Easy                 |Trivial
Performance    |Higher               |Lower
Recommended for|Most use cases       |Small tasks, when other approach fails

- [1] You already have a webbrowser installed :-)

The first is by using the web client and connect from the browser.
This can be useful for smaller tasks
or if you are unable to install software on the computer you are currently using.
Please see below for more information.

The second option is to download the ThinLinc client,
which offers higher performance and is recommended for most users.
The client can be downloaded from the [official download page](https://www.cendio.com/thinlinc/download/).

- [ThinLinc on Bianca](thinlinc_on_bianca.md)
- [ThinLinc on Rackham](thinlinc_on_rackham.md)
- ThinLinc on Snowy: same as [ThinLinc on Rackham](thinlinc_on_rackham.md)

## Connecting

### Login node connection

You can connect with ThinLinc to get a graphical desktop session on a login node. 
These are subject to the same limitations normal login sessions 
are (memory and run time limits, don't do anything that might disturb other users).

In addition to the normal limitations, login node connections may have 
short (10-15) minute idle timeouts meaning your session may disappear if you leave it.

### Making the connection

After downloading and installing, you can launch the ThinLinc client, 
and should see a form where you can enter your username and 
password (and possibly a server name). If you only see the simple form:

![Login](img/c_555890-l_1-k_thinlincsimple.png)

you can click Advanced to be able to set the server name to connect to. 
Provided you have set it up earlier, you can also use key based authentication.

## Two factor authentication

The ThinLinc client connects over SSH which means 
it may be required to present a code from two factor authentication 
(**FIX LINK**). 
The ThinLinc client does not know to ask for this 
so you will need to use the grace time feature, 
similar to file transfers with SFTP/rsync. 
To do this, first you have to connect with regular SSH 
and present the required code. 
Once you have logged in over SSH you can safely exit again. 
The login server will remember that you just logged in for a few minutes 
and not ask for two factor authentication again, 
so make sure you do not wait too long to connect with the ThinLinc client.

## Server names

The server name to connect to is:

- [Bianca](bianca.md): `bianca-gui.uppmax.uu.se`
- [Rackham](rackham.md): `rackham-gui.uppmax.uu.se`

to make a login node connection.

If you are using the web interface do note 
that the server only accepts secure connections, 
so do not forget the `s` in `https://`.

## ThinLinc client options

Under the "Screen" tab, you can set the starting size of the session and choose to enable/disable Full screen mode. Typically, users prefer to turn off full screen mode.

Normally you don't have to change anything else here, and we have also disabled all "local devices" (USB-sticks, sound and printers) on server side. So no point to fiddle with these specific options.

## Web interface

The servers listed above also offer a HTML5 client available at the according https URLs:

<https://rackham-gui.uppmax.uu.se>

## ThinLinc usage

### How do I copy/paste within a ThinLinc session?"

- Windows/MAC: Right-click and choose, or
- Windows:
    - paste: `shift+insert`
    - copy: `ctrl+insert`

### How do I copy/paste between ThinLinc and locally?

![copy-paste](img/copy_paste.png)

- Like a "wharf" for clipboard

- Copy in ThinLinc by the ThinLinc command (see above) and it ends up here in the ThinLinc clipboard
    - Mark and copy with Windows/Mac command
    - Paste locally with Windows/Mac command

- Copy from locally
    - paste in the ThinLinc clipboard with Windows/Mac command
    - paste to ThinLinc place by the ThinLinc command (see above)


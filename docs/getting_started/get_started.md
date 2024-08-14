# Get started here

In order to use UPPMAX resources, you need to be a member of a project and a user account.

## PIs

Do you or members in your research group need compute and storage resources on a HPC cluster or Infrastructure-as-a-Service cloud? Learn how to apply for a project by following the link below.

- [Project apply](project_apply.md)

Are you interested in other services, e.g. large volume data storage?

Let us know by contacting UPPMAX Support at `support@uppmax.uu.se`!

## Users

Once you or someone in your group or collaboration has a project, you must apply for a user account by following the link below.

- [User account](user_account.md)

Have an account already? Then check out these basic user guides:

- [Bianca first steps](login_bianca.md)
- [Rackham first steps](login_rackham.md)
- [Snowy first steps](login_snowy.md)

## Students

Are you taking a university course that uses UPPMAX and need help? Ask your instructor! If they can't help, contact us through IT Support.

## Getting started: First login to UPPMAX

N.B. You are NOT supposed to log in to any webpage with the password and username you get via UPPMAX support,
with the exception of the [ThinLinc](../software/thinlinc.md) web interface.

In order to use the UPPMAX resources you must login to a dedicated login computer (or 'login node') using ssh ("secure shell"). On Linux/Unix computers this is done in the [terminal](../software/terminal.md) with the 'ssh' command. On Windows you can download a small free program called [MobaXterm](https://mobaxterm.mobatek.net/) (or an alternative of your choice) to connect via ssh.

Another option is to use the ThinLinc client, either the web based one or one you download, to get access to a full graphical User Interface with a desktop, webbrowser, terminal etc. The ThinLinc client download is available for Linux, macOS and Windows. For more information and to see which of our systems support ThinLinc please refer to our [graphical connection guide](../software/thinlinc.md).

If you are using Windows a more advanced option would be to install WSL (Windows Subsystem for Linux) which gives you a Linux-installation you can use on Windows. Please refer to [Microsoft's documentation on WSL](https://docs.microsoft.com/en-us/windows/wsl/) for more information.
The hostname used to login via SSH is:

```text
rackham.uppmax.uu.se
```

Note: This is a "round robin" address which will direct you to one of the physical login nodes, rackham1.uppmax.uu.se or rackham2.uppmax.uu.se, etc. (If needed, you can also login directly to one of these, by using their respective hostnames.)

## Specific for a Linux/Unix or a Mac computer

On Unix/Linux and Mac OS, start a terminal and use the ssh command, like so (substitute 'username' with your own username):

```bash
ssh username@rackham.uppmax.uu.se
```

- Note: change "rackham" to the name of the machine you want to connect to.
- In order to run graphical programs through SSH, you need to enable [X forwarding](../software/ssh_x_forwarding.md),
    i.e. use `ssh -X username@rackham.uppmax.uu.se`

## Specific for a Windows computer

If you are running windows you could download and install a terminal program like [MobaXterm](https://mobaxterm.mobatek.net/).

After downloading and extracting the zip archive you will have 2 files; MobaXterm_Personal_X.X.exe and MobaXterm_Personal_Customizer_X.X.exe

The Customizer file is only used if you have bought a license and can safely be deleted.

Double click the MobaXterm_Personal_X.X.exe and you should see a terminal window. Use the ssh command, like so (substitute 'username' with your own username):

```text
username@rackham.uppmax.uu.se
```

## Common for all systems (Windows, Linux, OSX)

If it is the first time you connect, you will also need to confirm the host key by pressing 'Yes' if you get pop-up question or by typing 'yes' if you get the question on the command line.

After this, it will ask you for your password. When you type your password, it will look as if nothing is happening. This is to keep others from seeing how many characters your password has, so just keep typing and press enter when you think you have typed it correctly.

A note for people using MobaXterm: It will ask you if you want to save your password. Press 'No' and check the box 'Do not show this message again'.

If you log in from outside of Sweden, or from a network that does not support forward and reverse DNS lookups, you will be asked to set up and use two factor authentication. Read about setting up two factor authentication.

Now you are logged in! To log out again, type 'exit'.

Note: The information displayed in the welcome screen contains very important information about the usage of UPPMAX, which might affect your jobs, such as scheduled downtime etc, so please read very carefully, and look out for any announcements!

## Changing your password

You should regularly change your password. This is done in the standard Linux way. Type:

    passwd

The system will prompt you for your current password, after which it will ask you for a new password and a confirmation of the new password. If you lose your password and need to reset it, follow this link (which you can also find on our homepage).

## Copying files from/to your UPPMAX account

### From a Linux or Unix computer

Copy a file from you computer to your home directory on UPPMAX:

```bash
scp some_local_file user@rackham.uppmax.uu.se:/home/username/some-file
```

Copy a file from your home directory on UPPMAX to your computer:

```bash
scp user@rackham.uppmax.uu.se:/home/username/some-file local_file_or_directory
```

To place the file in the directory you are currently standing in, use a dot ('.') as the local directory:

```bash
scp user@rackham.uppmax.uu.se:/home/username/some-file .
```

### From a Windows computer

If you are running windows you could download or upload files using the file browser in MobaXterm, or the WinSCP software to upload and download files in a similar fashion to how FTP clients work. Alternatively if you are using WSL you can follow the instructions for Linux above.

## Where are my files? (Or, what are the different file systems?)

You have access to the same home directory regardless of what cluster you have logged into. Here you store your private files.

All projects also have a central storage area under the /proj/[project id]/ directory path. I.e. when you first login to UPPMAX you will see your home directory, so you will have to change to the project directory if you want to transfer project data files.

Also note that UPPMAX uses different disk quotas on your home directory and other areas you have access to (like the project folder).

Example: to see who much disk space you use:

    uquota

We have a page with more information about different file storages and quotas that can be good to read.

### Your private files

When you log in to UPPMAX for the first time you only have the following files created by the system:

    ls -la
    total 68
    drwxr-x---  7 user     uppmax 4096 Jun  2 23:11 .
    drwxr-xr-x 19 root     root      0 Jun  9 13:16 ..
    -rw-r--r--  1 user     uppmax   24 Jan  9  2008 .bash_logout
    -rw-r--r--  1 user     uppmax  435 Apr 21  2008 .bash_profile
    -rw-r--r--  1 user     uppmax  446 Jan  9  2008 .bashrc
    drwxr-xr-x  2 user     uppmax 4096 Jan  9  2008 bin
    -rw-r--r--  1 user     uppmax  385 Jan  9  2008 .cshrc
    -rw-r--r--  1 user     uppmax  237 Jan  9  2008 .emacs
    drwxrwxrwx  1 user     uppmax   14 Jun  2 11:05 glob
    -rw-r--r--  1 user     uppmax  120 Jan  9  2008 .gtkrc
    -rw-r--r--  1 user     uppmax  279 Apr 21  2008 .login
    drwx--S---  2 user     uppmax 4096 May  2  2008 private
    -rw-r--r--  1 user     uppmax  307 Apr 21  2008 .profile
    -rw-r--r--  1 user     uppmax  220 Jan  9  2008 .zshrc

The files starting with a "." are hidden files — startup scripts or configuration files.

The default permission of your home directory is 750, i.e. you can do everything, people belonging to the same group can read and execute your files and other people can not do anything. For more info on file permissions see this page on the online Linux Handbook.

Also note the private sub-folder. Here you can put files that you want only you, and no one else, to be able to access. Each day we have a job that ensures that all users's private folders still can't be accessed by anyone else, even if the permissions somehow accidentally would change.

## Creating and editing files

### The nano text editor

There are several editors installed at UPPMAX. The one that is considered easiest to use for new users without graphics is nano.

Example: how to use nano:

    nano filename

Save and exit the file with:

    Control-O, Control-X

(You might need to answer "y" or "n" on some questions, and/or press "Enter" to confirm.)

Exit without saving with:

    Control-X

You can get more help with nano by pressing (inside nano):

    Control-G

### The Emacs text editor

Another very common editor, with more features (but a little harder to use), is emacs.

Example: how to use emacs:

    emacs filename

Do the editing you want, then save with:

    Control-x, Control-s

Exit emacs with:

    Control-x, Control-c

You can read a tutorial in emacs by doing:

    Control-h t

### The Gedit text editor

If you have logged in with [X forwarding](../software/ssh_x_forwarding.md)
(i.e. with `ssh -X username@rackham.uppmax.uu.se`)
or through ThinLinc, then you can run `gedit`,
a program that feels very similar to the Windows program Wordpad.

Example: how to run gedit from a terminal:

    gedit &

The ampersand (&) keeps gedit from taking over your terminal session. You can navigate files and exit the program with the mouse.

## Bash, bourne-again shell

Bash is the default Unix shell, a command-line interpreter and script host that provides a traditional user interface for the linux operating system at UPPMAX. Users direct the operation of the computer by entering command input as text for a command line interpreter to execute or by creating text scripts of one or more such commands.

The .bash_profile file is run whenever you login or when you start a login shell (as in starting a job in the queue).

The .bashrc file is run when an interactive shell that is not a login shell is started, or if it is called from the .bash_profile (as it is in the default configuration).

The .bash_logout file is run when you log out.

## Modules

In order to make running installed programs easier you should use the [module](../cluster_guides/modules.md) command. The different modules that are installed sets the correct environments that are needed for the programs to run, like PATH, LD_LIBRARY_PATH and MANPATH.

Example: checking what modules are available:

module avail

Example: checking what modules you have loaded:

module list

Example: loading a compiler and an mpi module:

module load intel/20.4 openmpi

Example, if you want to unload a module

module unload intel

## How to run jobs

All jobs should be run using the batch queues. Read more for bianca and rackham, and the Slurm queue system.

## UPPMAX homepage

Please check our homepage regularly for information, news and announcements. We will announce maintenance stops and down time there.

- <https://www.uu.se/en/centre/uppmax>
- <https://www.uppmax.uu.se>

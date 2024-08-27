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

See [Log in to an UPPMAX cluster](login.md).

## Changing your password

See [How to change your UPPMAX password](change_uppmax_password.md)

## Copying files from/to your UPPMAX account

See [How to transfer files from/to your UPPMAX account](../cluster_guides/file_transfer.md)

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

See [gedit](../software/gedit.md)

## Bash, bourne-again shell

Bash is the default Unix shell, a command-line interpreter and script host that provides a traditional user interface for the linux operating system at UPPMAX. Users direct the operation of the computer by entering command input as text for a command line interpreter to execute or by creating text scripts of one or more such commands.

The .bash_profile file is run whenever you login or when you start a login shell (as in starting a job in the queue).

The .bashrc file is run when an interactive shell that is not a login shell is started, or if it is called from the .bash_profile (as it is in the default configuration).

The .bash_logout file is run when you log out.

## Modules

In order to run installed programs,
one uses the [module](../cluster_guides/modules.md)
system.

## How to run jobs

All jobs should be run using [the job scheduler](../cluster_guides/slurm.md).

## UPPMAX homepage

Please check our homepage regularly for information, news and announcements.
We will announce maintenance stops and down time there.

- <https://www.uu.se/en/centre/uppmax>
- <https://www.uppmax.uu.se>

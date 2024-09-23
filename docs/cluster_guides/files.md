# Files on UPPMAX

## Where are my files? (Or, what are the different file systems?)

You have access to the same home directory regardless of what
cluster you have logged into. Here you store your private files.

All projects also have a central storage area under the `/proj/[project id]/` 
directory path, i.e. when you first login to UPPMAX,
you will see your home directory, so you will have to change to the project
directory if you want to transfer project data files.

Also note that UPPMAX uses different disk quotas on your home directory
and other areas you have access to (like the project folder).
Use [uquota](../software/uquota.md) to see who much disk space you use.

<!-- We have a page with more information about different file storages and quotas that can be good to read. [RB: where is that page?] -->

## Your private files

When you log in to UPPMAX for the first time you only have
the following files created by the system:

```bash
$ ls -la
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
```

The files starting with a `.` (i.e. a dot or period) are hidden files.
These are commonly startup scripts or configuration files.

The [default permission](https://en.wikipedia.org/wiki/File-system_permissions#Notation_of_traditional_Unix_permissions)
of your home directory is `750`,
i.e. you can do everything, people belonging to the same group
can read and execute your files and other people can not do anything.

Also note the `private` sub-folder: here you can put files that you want
only you, and no one else, to be able to access.
Each day we have a job that ensures that all users's private folders
still can't be accessed by anyone else,
even if the permissions somehow accidentally would change.

## Creating and editing files

Creating and editing files is taught:

- [UPPMAX intro day 1: use the remote desktop environment](https://uppmax.github.io/uppmax_intro_day_1/sessions/use_remote_desktop/)
- [UPPMAX intro day 1: use the terminal](https://uppmax.github.io/uppmax_intro_day_1/sessions/use_terminal/)

# Data transfer to/from Rackham

There are multiple ways to transfer files to/from Rackham:

Method                                                        |Features
--------------------------------------------------------------|---------------------------------------------
[Using a graphical program](#using-a-graphical-program)       |Graphical interface, intuitive, for small amounts of data only
[Using SCP](#using-SCP)                                       |Terminal, easy to learn, can be used in scripts
[Using SFTP](#using-SFTP)                                     |Terminal, easy to learn

Each of these methods is discussed in detail below.

## Using a graphical program

One can transfer files to/from Rackham using a graphical program.
A graphical interface is intuitive to most users.
However, it can be used for small amounts of data only
and whatever you do cannot be automated.

See [File transfer using a graphical program](rackham_file_transfer_using_gui.md)
for a step-by-step guide how to transfer files using
a graphical tool.

## Using SCP

One can transfer files to/from Rackham using SCP.
SCP is an abbreviation of 'Secure copy protocol',
however, it is not considered 'secure' anymore:
instead it is considered an outdated protocol.
The program `scp` allows you to transfer files to/from Rackham using SCP,
by coping them between your local computer and Rackham.

The process is:

1. Start a terminal on your local computer
2. In the terminal, copy files using `scp` to connect to Rackham:

```
scp [from] [to]
```

Where `[from]` is the file(s) you want to copy, and `[to]` is the destination.
This is quite a shorthand notation!

This is how you copy a file from your local computer to Rackham:

```
scp [local_filename] [username]@rackham.uppmax.uu.se:/home/[username]
```

where `[local_filename]` is the path to a local filename,
and `[username]` is your UPPMAX username, for example:

```
scp my_file.txt sven@rackham.uppmax.uu.se:/home/sven
```

To copy a file from Rackham to your local computer, do the command above in reverse order:

```
scp [username]@rackham.uppmax.uu.se:/home/[username]/[remote_filename] [local_folder]
```

where `[remote_filename]` is the path to a remote filename,
`[username]` is your UPPMAX username, 
and `[local_folder]` is your local folder, for example:

```
scp sven@rackham.uppmax.uu.se:/home/sven/my_remote_file.txt /home/sven
```

3. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

## Using SFTP

One can transfer files to/from Rackham using SFTP.
SFTP is an abbreviation of 'SSH File Transfer Protocol',
where 'SSH' is an abbreviation of 'Secure Shell protocol'
The program `sftp` allows you to transfer files to/from Rackham using SFTP.

The process is:

1. Start a terminal on your local computer
2. In the terminal, run `sftp` to connect to Rackham by doing:

```
sftp [username]@rackham.uppmax.uu.se 
```

where `[username]` is your UPPMAX username, for example:

```
sftp sven@rackham.uppmax.uu.se 
```

3. If asked, give your UPPMAX password. 
   You can get rid of this prompt if you have setup SSH keys

4. In `sftp`, upload/download files to/from Rackham

Basic `sftp` command can be found [https://www.uppmax.uu.se/support/user-guides/basic-sftp-commands/](here).

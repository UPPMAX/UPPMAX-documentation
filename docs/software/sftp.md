# SFTP

## 1. Getting Help

Once, you in the `sftp` prompt, check the available commands by
typing `?` or `help` at command prompt.
This will print out a list of the available commands and
give a short description of them. We'll cover the most common ones in this guide.

```bash
sftp> ?
Available commands:
cd path                       Change remote directory to 'path'
...
...
...
```

## 2. Check Present Working Directory

The command `lpwd` is used to check the Local present working directory,
whereas `pwd` command is used to check Remote working directory.

```bash
sftp> lpwd
Local working directory: /
sftp> pwd
Remote working directory: /tecmint/
lpwd – print the current directory on your system
pwd – print the current directory on the ftp server
```

## 3. Listing Files

Listing files and directories in local as well as remote system.

On Remote

```bash
sftp> ls
```

On Local

```bash
sftp> lls
```

## 4. Upload File

Put single or multiple files in remote system.

```bash
sftp> put local.profile
```

Uploading local.profile to /tecmint/local.profile

## 5. Upload Multiple Files

Putting multiple files on remote system.

```bash
sftp> mput *.xls
```

Another alternative to uploading many files is to tar and/or compress the files to a single file before uploading. The file transfer will stop in between every file, so the more file you have to upload the more stops it will make. This can have a dramatic impact on transfer speed if there are 1000s of files that you want to transfer. Running tar and/or zip on the files before transferring them will package all the files into a single file, so there will be no stops at all during the transfer.

## 6. Download Files

Getting single or multiple files in local system.

```bash
sftp> get SettlementReport_1-10th.xls
```

Fetching /tecmint/SettlementReport_1-10th.xls to SettlementReport_1-10th.xls Get multiple files on a local system.

```bash
sftp> mget *.xls
```

Note: As we can see by default the get command downloads the file to the local system with the same name. We can download remote file and store it with a different name by specifying the name at the end. (This applies only while downloading single file).

## 7. Switching Directories

Switching from one directory to another directory in local and remote locations.

On Remote

```bash
sftp> cd test
```

On Local

```bash
sftp> lcd Documents
```

## 8. Create Directories

Creating new directories on remote and local locations.

```bash
sftp> mkdir test
sftp> lmkdir Documents
```

## 9. Remove Directory or File

Remove directory or file in remote system.

```bash
sftp> rm Report.xls
sftp> rmdir sub1
```

Note: To remove/delete any directory from remote location, the directory must be empty.

## 10. Exit sFTP Shell

The `!` (exclamation mark) command drops us in local shell from where we can execute Linux commands. Type `exit` command where we can see sftp> prompt return.

```bash
sftp> !
[root@sftp ~]# exit
Shell exited with status 1
sftp>
```

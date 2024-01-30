# Basic toolkit


![Caption](./img/terminal.png)


!!! objectives
    - Let's dig into the most important BASH commands
    - We'll do a type-along session


???- question "Like videos?"

    Below usage of the command line is discussed in text.
    If you prefer video, [here](https://youtu.be/kjqLAx2bgJI) 
    is how to use the command-line on the UPPMAX Bianca cluster.
 
## We will cover these commands



### Navigation and file management

1. `pwd`  &emsp; present directory
1. `ls`  &emsp;list content
1. `cd`  &emsp;change directory
1. `mkdir`  &emsp;make directory
1. `cp`  &emsp;copy
1. `scp`  &emsp;securely remotely copy
1. `mv`  &emsp;move
1. `rm`  &emsp;remove
1. `rmdir`  &emsp;remove empty directory

### Read files and change file properties

10. `cat`  &emsp;print content on screen
11. `head`  &emsp;print first part
12. `tail`  &emsp;print last part
13. `less`  &emsp;browse content
14. `tar`  &emsp;compress or extract file
15. `chmod`  &emsp;change file permissions
16. `man`  &emsp;info about a command

## File system Navigation
### pwd — where are you now? “Print name of current/Working Directory”

```console 
$ pwd

$ pwd -P 
```
- ``-P`` gives you the physical path, 
  - ignores how you got there

 
### ls — list directory contents

Type ``ls`` to display the contents of the current directory.

```console
$ ls -a
```

``-a`` also shows hidden files and directories.

```console
$ ls -l
```
``-l`` gives you listed and detailed information.

```console
$ ls -lt
```

``-lt`` sorts things by time modified.

```console
$ ls –lrt
```

``-r`` gives reversed order, so in this case newest in last line.

```console
$ man ls
```

- for complete information about a command.
- TIP: `-$ man <command>` works for almost any command!
  - scroll with arrows and quit with ``q``.

 
### cd — Change the shell working Directory
- To change directory, use ``cd <target>``

!!! warning

    - Some of following steps will only be available for the Introduction course members.
    - These involve the `/proj/introtouppmax`` directory

```console
$ cd /proj/introtouppmax

$ pwd

$ ls

$ cd labs

$ pwd
```

!!! challenge Experiment with cd
    - Experiment with ``cd``. 
    - Try adding ``<spaces>`` or extra ``/`` in various places.
    - Use *tab completion* to avoid typos and typing ``ls`` a lot.

    - Figure out the use of the following:

    ```console
    $ cd -

    $ cd ..

    $ cd

    $ cd ~

    ```


    ??? solution
        - `cd -` : goes back to your last directory

        - `cd ..` : goes a level up in the hierarchy

        - `cd` : goes to home directory

        - `cd ~` : also goes to home directory


 

## Copy, Create, Move
### mkdir — make directories

!!! warning
    - Make sure you’re in your home directory by `cd ~`


- Create a new directory ``uppmax-intro``

```console
$ cd ~
$ mkdir uppmax-intro
```

- Go in there:

```console
$ cd uppmax-intro/
```

 
### cp — copy files and directories

- Copy files with: `cp <source> <target>`
- Set target to ``.`` to keep name and to point at present directory.

```console
$ cp /proj/introtouppmax/labs/linux_tutorial/ .
```

- Well, that didn’t work. What does the error say?
- So... try
```console
$ cp -r /proj/introtouppmax/labs/linux_tutorial/ .
```

``-r`` is for recursive, meaning including files and subdirectories!

- Move to your just created ``linux_tutorial/``

```console
$ cd linux_tutorial
```
- Make a copy of the file “newfile” in the same directory:

```console
$ cp newfile copyfile
```
 
### scp — secure copy (remote file copy program)

- Linux/MacOS: To copy data to/from Rackham, you can use ``scp`` **from the terminal on your local machine**:

#### Download from Rackham 
- Download
```console
[bob@macbook]$ scp bob@rackham.uppmax.uu.se:~/mydata copyofmydata

[bob@macbook]$ scp bob@rackham.uppmax.uu.se:~/mydata .                      # (keeping file name)
```


!!! example

    **Download the file ``first.txt``**
    
    -  In your local terminal:
    
    ```console
    [bob@macbook]$ scp <username>@rackham.uppmax.uu.se:~/first.txt .                      # (keeping file name)
    ```  
    
#### Upload to Rackham
- Upload from present directory on local machine to your home directory on cluster.
  - Example:
 
```console
[bob@macbook]$ scp myinput bob@rackham.uppmax.uu.se:~/copyofmyinput

[bob@macbook]$ scp myinput bob@rackham.uppmax.uu.se:~/                      # (keeping filename)
``` 

!!! example

    **upload the file ``first.txt`` after some modification**
    
    1. Open the file you just downloaded in any editor.
    2. Add a row, like: ``A new row``
    3. Save and quit.
    4. Upload your file but save it as ``second.txt`` on Rackham. In your local terminal:
    
    ```console
    [bob@macbook]$ scp first.txt <username>@rackham.uppmax.uu.se:~/second.txt                     # (new filename)
    ```
    
!!! seealso

    - [Rackham file transfer using scp](http://docs.uppmax.uu.se/cluster_guides/rackham_file_transfer_using_scp/)

 
### mv — move/rename file

- Moving files works just like copying files:
- `mv <source> <target>`
- Move the copy you just made to another place:
```console
$ mv copyfile ../
``` 
- Rename it.
```console
$ mv ../copyfile ../renamedfile
```
 
## Archiving
**tar — archiving and compression**

- We’re going to need more files. Let's extract the tar.gz file (tared and gzipped file)

```console
$ tar -vxzf files.tar.gz
```
- The flags mean:
        - <u>v</u>erbosely
        - e<u>x</u>tract
        - g<u>z</u>ipped
        - <u>f</u>ilename
- Order of flags may matter!
  - ``f`` should be in the start or in the end!
- You should see a list of files being extracted

!!! tip
    - To compress use the flag `-c`instead of `-x`

    ```console
    $ tar -czfv <tar file> <path/to/directory/file(s)-or-directory>
    ```
 
## Deleting
### rm — delete files  or directories

!!! Note
    - **Tip: make "rm" ask if you really want to erase:**
    - Within a session: Type in the command prompt

    ```console
    alias rm='rm -i'
    ```
    - Override asking with 

    ```console       
    rm –f <>
    ```
    - Do you want this to be the case everytime you start a new session?
       - Edit file ".bashrc" in /home directory by adding the above alias line on any but the first line.
    - These steps will also work for ``mv`` and ``cp``. 


- Deleting files works just like copying or moving them: `rm <target>`

- Try it out:
  
```console
$ rm ../renamedfile

$ rm this_is_empty
```

- hmmmm...

 
### rmdir — delete an empty directory

- We need another command to delete directories

```console
$ rmdir this_is_empty

$ rmdir this_has_a_file
```

- Problem again??
 
- Is there a way to use rm to delete directories?
 
!!! solution

    - Recursive commands `-r` are applied to directories and their contents
    ```console
    $ rm -r this_has_a_file
    ```


## Help
### man — manual, look up the right flags

- Nobody can remember whether it’s ``-R`` or `-r` for recursive, or if ``-f`` lets you choose a file or forces an action.

```console
$ man ls 
```

- shows you how to use ``ls`` and all its options
- Type `/<keyword>` to search for a keyword, use `n` (forward) and ´N` (backward) to scan through hits.
- Scroll with arrows.
- Type `q` to quit.
 
!!! challenge
    - Spend some time now to browse the man pages for the commands you’ve just learned!


 
<!--- 
- Not only user commands!

    Use sections like

        man 2 write

MANUAL SECTIONS
       The standard sections of the manual include:

       1      User Commands

       2      System Calls

       3      C Library Functions

       4      Devices and Special Files

       5      File Formats and Conventions

       6      Games et. Al.

       7      Miscellanea

       8      System Administration tools and Deamons
--->
 
## Let’s get wild with Wildcards
![Caption](./img/wildcards_bear.png)

```console
$ ls many_files

$ ls many_files/*.txt

$ ls many_files/file_1*1.docx
```

- Want to clean out temporary files ending in .tmp in all the subdirectories?

!!! warning
    - It could be wise to do `ls -a */*.tmp` first to see what will be deleted...

    ```console
    $ rm */*.tmp
    ```

!!! challenge Exercise
    - Exercise:  Create a new directory and move all .txt files in many_files to it.

 
## Reading files

- In Linux, you can (if you wish) also display files without being able to change them

```console
$ cd old_project

$ ls
```

- Hmm, which of these files are useful?

 
### cat - con<ins>cat</ins>enate files and print on the standard output

![Caption](./img/cat.png)

- ``cat`` dumps the contents of files to the terminal as text

```console
$ cat the_best
```

- Yummy!

```console
$ cat a
```

- What's this????

- **Concatenate** files with this wizardry:

```console
$ cat a the_best > combinedfiles.txt
```

- File ``a`` is written first and ``the_best`` is appended
 
### head — display the top (<u>head</u>ing) of a file


![Caption](./img/head.png)

```console
$ head a
```
- You can choose how many lines to display (default 10)

```console
$ head -n 4 a
```

 
### tail — display the end of a file


![Caption](./img/tail.png)

- Tail is the same as head, but for the other end.

```console
$ tail -n 5 a
```

- Handy to look at log files or to figure out the structure of a text file.

 
### less — read a whole file

- cat doesn’t really work for long files

```console
 $ less a
```

- Search with `/<keyword>` and `n`/`N`
- Hit `q` to quit.
- scroll with arrows.
- `man` uses `less!

     “less is more”
 
## History

- ``history`` shows previous commands
- You can rerun earlier commands by:
    - copy-pasting and pressing ``<enter>``
    - ``!990`` will run the command of line 990 of last `history` output.
- Search for earlier commands you just remember parts of:
    - history | grep 'jobstats'
- [More info](https://www.redswitches.com/blog/linux-history-command/)





## File permissions


![Caption](./img/permission.png)

### Example

```console
$ ls -l

drwxrwxr-x 2 marcusl marcusl 4096 Sep 19 2012 external_hdd 
-rwxr-xr-x 1 marcusl marcusl 17198 Jul 16 14:12 files.tar.gz
```

- Leading symbol:
  - `d` directory
  - `-` regular file
  - `l` symbolic link (more on this tomorrow)
  - Others exist, but you can ignore them for now

```console
$ ls -l
 
  drwxrwxr-x 2 marcusl marcusl 4096 Sep 19 2012 external_hdd

  -rwxr-xr-x 1 marcusl marcusl 17198 Jul 16 14:12 files.tar.gz
```
  
- Three sets of “rwx” permissions
  - rwx: r ead, w rite, ex ecute
  - User: the user account that owns the file (usually the one that created it)
  - Group: the group that owns the file (usually the *project group* in /proj/xyz or the user’s group elsewhere)
  - Others: everyone else on the system (literally a thousand strangers)

- r – read
  - Files: Read the contents of the file
  - Directories: List the files in the directory

- w – write
  - Files: Modify the file
  - Directories: Add, rename, or delete files in the directory

- x – execute
  - Files: Run the file as a program
  - Directories: Traverse the directory (e.g. with “cd”)


## Changing permissions
**chmod** — change file mode bits

**If you own, i.e. created, the file or directory, you can modify the content**

!!! admonition "Common issues"

    - Files with `w` can be modified and destroyed by accident. Protect your data!
    - If you want to share data or scripts with a person not in your project (e.g. support staff like me), you can!
    - If you want to keep non-members from even seeing which files you have, you can!


### Syntax

`chmod <mode> <files>`

- `<mode>` is of the form: For whom, Modify, What permission(s)
- For whom?
    - `u`: user/owner
    - `g`: group, often the members to a certain project
    - `o`: others
    - `a`: all
    - if not set changes are applied for user AND group
- Modify?
    - `+`: add permissions,
    - `-`: remove
    - `=`: set equal to
      - `=` usually causes unmentioned bits to be removed except that a directory's unmentioned set user and group ID bits are not affected.
- What permissions?
    - `r`, `w`, `x`, i.e. the actual permission

#### Examples

- `<mode>` can be e.g.:
  -  `u+x` : lets You (owner) run a script you just wrote
  -  `-w` : no write permissions for **owner+group**
    - warning: if `w` was already set for *others* it will be kept!!
  -  `+rw` : let user and group members read and edit this file, not others if not already set
  -  `=xw` : let group members go into your directory and put files there, but not see which files are there, others are not affected
  -  `a=xw` : set xw for everyone

- chmod takes flags as usual, e.g.
  -  `-R` for recursive (i.e. all files and sub-directories therein)

!!! admonition "chmod 755 style — binary sum — octal bit mask"

    - Online, you will come across e.g. `chmod 755 <file/dir>`. What does this mean? It’s an "octal bit mask”:

    - Each digit corresponds to the **binary sum** for the *owner*, *group* and *others*, respectively.
 
        - ``7 = 4 + 2 + 1 = r + w + x``   All permissions
        - ``5 = 4 + 0 + 1 = r +   + x``   Read and execute permission

    - 755 then means all permissions for owner, but limiting write permissions for the group and all others

    - What number would `rw` be?

    ??? solution
        6


 
???+ challenge "chmod — Hands-on"

    - In your *locally created* ``linux_tutorial`` directory, find important files and old saved data that you wouldn’t want to lose (*imagine*).
    - Directories: important_results/, old_project/
    - File: last_years_data
    - Use chmod to remove write permission from those files and directories (use the `-R` flag (not `-r`) to also do the files in the directories).
    - Take a moment to play around with chmod and explore the effects of permissions on files and directories.

    ??? solution 

        ```console
        $ chmod -wR <target>
        ```

## Links

 * A free online book about Linux: ['The Linux Command Line'](https://linuxcommand.org/tlcl.php).
 

# How can I display my disk quota?

To limit the amount of disk space each user can allocate we use a disk quota system at UPPMAX. The default disk quota is 32 GByte in your home directory. Every SNIC-project also comes with a default 128 GByte backed-up project storage. If more data is needed you may apply for an UPPMAX Storage Project and get more quota. UPPNEX project have a default 512 GByte backed-up project storage and a and 512 GB nobackup space.

You can display your current usage with the command [uquota](../software/uquota).

When you exceed your quota, the system will not let you write any more data and you have to either remove some files or request more quota. The 'uquota' command will also show the date and to what limit your quota will change to, if you have been given a larger quota.

To get more quota, send a mail to support (`support@uppmax.uu.se`) and state how much, for how long time, and why you need it. See the storage project application page for more information on how we handle and prioritise storage requests.

Here are two commands. The first results in a list of subdirectories ordered by size and proportion of total size. The second produces a list of the files in the current directory that take up most space. These may take a long time to complete, use 'ctrl-c' to stop the process if you change your mind.

```bash
du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}'
find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn
```

You should also read the [Disk Storage Guide](disk_storage_guide.md).
